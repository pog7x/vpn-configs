import asyncio
import hashlib
import json
import logging
import os
import urllib
import zoneinfo
from datetime import datetime
from http import HTTPMethod

import aiofiles
import aiohttp
from py_markdown_table.markdown_table import markdown_table

from ghwrapper import GihubWrapper

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

GH_TOKEN = os.environ.get("GH_TOKEN")
REPO_NAME = os.environ.get("REPO_NAME")

CONFIGS_DIRECTORY = "githubmirror"
CONFIG_FILE_PATH = f"{CONFIGS_DIRECTORY}/%d.txt"

FETCH_RETRIES_COUNT = 3
RETRY_TIMEOUT = 3
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/143.0.0.0 Safari/537.36"
    )
}


class DownloadAndSave:  # TODO to rename and remove
    def __init__(self, url: str, number: int, info: None | dict, ghapi: GihubWrapper):
        self._url = url
        self._number = number
        self._cfg_file_path = CONFIG_FILE_PATH % self._number
        self._info = self.get_or_create_info(info=info)
        self._ghapi = ghapi

    def extract_source_name(self) -> str:
        res = "Source"

        try:
            parsed = urllib.parse.urlparse(self._url)
            path_parts = parsed.path.split("/")

            if len(path_parts) > 2:
                res = f"{path_parts[1]}/{path_parts[2]}"
            else:
                res = parsed.netloc
        except:
            logger.exception(f"Extract source name from URL {self._url} error")

        return res

    def get_or_create_info(self, info: dict, force: bool = False) -> dict:
        if info and not force:
            return info

        zone = zoneinfo.ZoneInfo("Europe/Moscow")
        datetime_now = datetime.now(zone)
        now_time, now_date = datetime_now.strftime("%H:%M"), datetime_now.strftime("%d.%m.%Y")

        return {
            "Num": self._number,
            "File": f"[`{self._number}.txt`]({self._cfg_file_path})",
            "Source": f"[{self.extract_source_name()}]({self._url})",
            "Update time": now_time,
            "Update date": now_date,
        }

    async def is_equal_urls_config(self, new_data: str) -> bool:
        old_data, new_data = b"", new_data.encode()
        try:
            async with aiofiles.open(self._cfg_file_path, "r", encoding="utf-8") as file:
                old_data = (await file.read()).encode()
        except FileNotFoundError:
            ...
        except:
            logger.exception(f"{self._number} | Compare configs data unexpected error")
        else:
            return hashlib.md5(old_data).hexdigest() == hashlib.md5(new_data).hexdigest()
        return False

    async def download_and_save(self) -> dict:
        try:
            data = await self.fetch_data()
        except Exception:
            logger.exception(f"Number {self._number} | config fetching error")
            return

        try:
            if not (await self.is_equal_urls_config(data)):
                await self._ghapi.update_or_create_file(
                    self._cfg_file_path,
                    msg=f"🚀 Updating config file 📁 {self._cfg_file_path}",
                    content=data,
                )
                logger.info(f"📁 {self._number} | Config saved successfully {self._cfg_file_path}")

                self._info = self.get_or_create_info(info=self._info, force=True)
        except Exception:
            logger.exception(f"Number {self._number} | writing to file error")

        return self._info

    async def fetch_data(self) -> None | str:
        async with aiohttp.ClientSession() as session:
            for retry in range(FETCH_RETRIES_COUNT):
                try:
                    resp = await session.request(method=HTTPMethod.GET, url=self._url, headers=HEADERS)
                    resp.raise_for_status()
                    return (await resp.read()).decode(encoding="cp437")
                except (aiohttp.ClientError, asyncio.CancelledError):
                    logger.warning(
                        f"Retry #{retry} | URL {self._url} error status code: {resp.status_code}. Sleeping..."
                    )

                await asyncio.sleep(RETRY_TIMEOUT)


class Main:
    MARKDOWN_LIST = []

    def __init__(self):
        self._ghapi = GihubWrapper(gh_token=GH_TOKEN, repo_name=REPO_NAME)

    async def run_download(self, url: str, _id: int, info: None | dict, urls_dict: dict):
        new_info = await DownloadAndSave(url=url, number=_id + 1, info=info, ghapi=self._ghapi).download_and_save()
        urls_dict[url] = new_info
        self.MARKDOWN_LIST[_id] = new_info

    async def gather_coros(self, urls: list, urls_dict: dict):
        await asyncio.gather(
            *[
                self.run_download(url=url, _id=_id, info=urls_dict.get(url), urls_dict=urls_dict)
                for _id, url in enumerate(urls)
            ]
        )

    async def run(self):
        if not os.path.exists(CONFIGS_DIRECTORY):
            os.makedirs(CONFIGS_DIRECTORY)

        with open("urls.txt", "r") as file:
            urls = [line.strip() for line in file.readlines()]

        try:
            with open("urls.json", "r") as urls_json:
                urls_dict = json.load(urls_json)
        except:
            urls_dict = {}

        if len(urls) != len(urls_dict):
            urls_dict = {}

        self.MARKDOWN_LIST = [0] * len(urls)

        await self.gather_coros(urls, urls_dict)

        markdown = markdown_table(self.MARKDOWN_LIST).set_params(row_sep="markdown", quote=False).get_markdown()

        await self._ghapi.update_or_create_file(
            file_path="README.md",
            msg="📝 Updating table in README.md",
            content=markdown,
        )

        await self._ghapi.update_or_create_file(
            file_path="urls.json",
            msg="📝 Обновление urls.json",
            content=json.dumps(urls_dict),
        )


if __name__ == "__main__":
    asyncio.run(Main().run())
