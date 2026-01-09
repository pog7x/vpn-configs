import logging

from github import Auth, Github, GithubException

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class GihubWrapper:
    def __init__(self, gh_token: str, repo_name: str):
        self._gh = Github(auth=Auth.Token(gh_token))
        self._repo_name = repo_name
        self._repo = self._gh.get_repo(self._repo_name)

    async def get_content(self, file_path: str):
        try:
            return self._repo.get_contents(file_path)
        except GithubException as e:
            if e.status == 404:
                logger.exception(f"❌ {file_path} не найден в репозитории")
            else:
                raise
            return None

    async def update_or_create_file(self, file_path: str, msg: str, content: str, sha: None | str = None):
        try:
            if not sha:
                if not (file_content := await self.get_content(file_path=file_path)):
                    logger.info(f"Файл {file_path} не найден, создание...")
                    return await self.create_file(file_path=file_path, msg=msg, content=content)

                sha = file_content.sha
            return self._repo.update_file(path=file_path, message=msg, content=content, sha=sha)
        except:
            logger.exception(f"⚠️ Ошибка при обновлении {file_path}")
            raise

    async def create_file(self, file_path: str, msg: str, content: str):
        try:
            return self._repo.create_file(path=file_path, message=msg, content=content)
        except:
            logger.exception(f"⚠️ Ошибка при создании {file_path}")
            raise
