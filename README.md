# VPN Configs

[![Frequent Update](https://github.com/pog7x/vpn-configs/actions/workflows/frequent_update.yml/badge.svg)](https://github.com/pog7x/vpn-configs/actions/workflows/frequent_update.yml)

Automated aggregator that collects free VPN configuration files from multiple open-source repositories across GitHub and mirrors them into a single, regularly updated location.

## How It Works

1. A GitHub Actions workflow runs **every hour** on a cron schedule.
2. The script reads a curated list of source URLs from `urls.txt`.
3. Each source is fetched, deduplicated via MD5 hash comparison, and saved to the `githubmirror/` directory.
4. The table below is regenerated with the latest update timestamps.

## Configs

|Num|                                                 File                                                |                    Source                    |Update time|Update date|
|---|-----------------------------------------------------------------------------------------------------|----------------------------------------------|-----------|-----------|
| 1 | [`1.txt`](https://raw.githubusercontent.com/pog7x/vpn-configs/refs/heads/master/githubmirror/1.txt) |               sakha1370/OpenRay              |   13:00   | 06.09.2026|
| 2 | [`2.txt`](https://raw.githubusercontent.com/pog7x/vpn-configs/refs/heads/master/githubmirror/2.txt) |             sevcator/5ubscrpt10n             |   19:18   | 14.07.2026|
| 3 | [`3.txt`](https://raw.githubusercontent.com/pog7x/vpn-configs/refs/heads/master/githubmirror/3.txt) |           yitong2333/proxy-minging           |   13:00   | 06.09.2026|
| 4 | [`4.txt`](https://raw.githubusercontent.com/pog7x/vpn-configs/refs/heads/master/githubmirror/4.txt) |                 acymz/AutoVPN                |   12:59   | 06.09.2026|
| 5 | [`5.txt`](https://raw.githubusercontent.com/pog7x/vpn-configs/refs/heads/master/githubmirror/5.txt) |         miladtahanian/V2RayCFGDumper         |   13:00   | 06.09.2026|
| 6 | [`6.txt`](https://raw.githubusercontent.com/pog7x/vpn-configs/refs/heads/master/githubmirror/6.txt) |           roosterkid/openproxylist           |   12:59   | 06.09.2026|
| 7 | [`7.txt`](https://raw.githubusercontent.com/pog7x/vpn-configs/refs/heads/master/githubmirror/7.txt) |            Epodonios/v2ray-configs           |   13:00   | 06.09.2026|
| 8 | [`8.txt`](https://raw.githubusercontent.com/pog7x/vpn-configs/refs/heads/master/githubmirror/8.txt) |             CidVpn/cid-vpn-config            |   13:00   | 06.09.2026|
| 9 | [`9.txt`](https://raw.githubusercontent.com/pog7x/vpn-configs/refs/heads/master/githubmirror/9.txt) |mohamadfg-dev/telegram-v2ray-configs-collector|   12:59   | 06.09.2026|
| 10|[`10.txt`](https://raw.githubusercontent.com/pog7x/vpn-configs/refs/heads/master/githubmirror/10.txt)|               mheidari98/.proxy              |   13:00   | 06.09.2026|
| 11|[`11.txt`](https://raw.githubusercontent.com/pog7x/vpn-configs/refs/heads/master/githubmirror/11.txt)|          youfoundamin/V2rayCollector         |   12:59   | 06.09.2026|
| 12|[`12.txt`](https://raw.githubusercontent.com/pog7x/vpn-configs/refs/heads/master/githubmirror/12.txt)|            expressalaki/ExpressVPN           |   08:17   | 27.05.2026|
| 13|[`13.txt`](https://raw.githubusercontent.com/pog7x/vpn-configs/refs/heads/master/githubmirror/13.txt)|          MahsaNetConfigTopic/config          |   23:11   | 25.07.2026|
| 14|[`14.txt`](https://raw.githubusercontent.com/pog7x/vpn-configs/refs/heads/master/githubmirror/14.txt)|              LalatinaHub/Mineral             |   17:19   | 05.09.2026|
| 15|[`15.txt`](https://raw.githubusercontent.com/pog7x/vpn-configs/refs/heads/master/githubmirror/15.txt)|        miladtahanian/Config-Collector        |   13:00   | 06.09.2026|
| 16|[`16.txt`](https://raw.githubusercontent.com/pog7x/vpn-configs/refs/heads/master/githubmirror/16.txt)|             Pawdroid/Free-servers            |   12:59   | 06.09.2026|
| 17|[`17.txt`](https://raw.githubusercontent.com/pog7x/vpn-configs/refs/heads/master/githubmirror/17.txt)|         MhdiTaheri/V2rayCollector_Py         |   13:00   | 06.09.2026|
| 18|[`18.txt`](https://raw.githubusercontent.com/pog7x/vpn-configs/refs/heads/master/githubmirror/18.txt)|                 free18/v2ray                 |   12:59   | 06.09.2026|
| 19|[`19.txt`](https://raw.githubusercontent.com/pog7x/vpn-configs/refs/heads/master/githubmirror/19.txt)|           MhdiTaheri/V2rayCollector          |   13:00   | 06.09.2026|
| 20|[`20.txt`](https://raw.githubusercontent.com/pog7x/vpn-configs/refs/heads/master/githubmirror/20.txt)|               Argh94/Proxy-List              |   13:00   | 06.09.2026|
| 21|[`21.txt`](https://raw.githubusercontent.com/pog7x/vpn-configs/refs/heads/master/githubmirror/21.txt)|                shabane/kamaji                |   13:16   | 04.09.2026|
| 22|[`22.txt`](https://raw.githubusercontent.com/pog7x/vpn-configs/refs/heads/master/githubmirror/22.txt)|         wuqb2i4f/xray-config-toolkit         |   13:00   | 06.09.2026|
| 23|[`23.txt`](https://raw.githubusercontent.com/pog7x/vpn-configs/refs/heads/master/githubmirror/23.txt)|        igareck/vpn-configs-for-russia        |   13:00   | 06.09.2026|
| 24|[`24.txt`](https://raw.githubusercontent.com/pog7x/vpn-configs/refs/heads/master/githubmirror/24.txt)|                Mr-Meshky/vify                |   13:00   | 06.09.2026|
| 25|[`25.txt`](https://raw.githubusercontent.com/pog7x/vpn-configs/refs/heads/master/githubmirror/25.txt)|             V2RayRoot/V2RayConfig            |   10:28   | 05.07.2026|

## Quick Start

```bash
# Clone the repository
git clone https://github.com/pog7x/vpn-configs.git
cd vpn-configs

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export GH_TOKEN="your_github_token"
export REPO_NAME="owner/repo"

# Run
python main.py
```

## Requirements

| Package | Purpose |
|---------|---------|
| [aiohttp](https://pypi.org/project/aiohttp/) | Async HTTP requests |
| [aiofiles](https://pypi.org/project/aiofiles/) | Async file I/O |
| [PyGithub](https://pypi.org/project/PyGithub/) | GitHub API integration |
| [py-markdown-table](https://pypi.org/project/py-markdown-table/) | Markdown table generation |

## Disclaimer

This project is provided for **educational and informational purposes only**. The maintainers do not host, create, or endorse any VPN configurations — all files are mirrored from publicly available open-source repositories. Use at your own risk and in compliance with your local laws.
