# python + ruff

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## 公式リポジトリとドキュメント

microsoft公式リポジトリ
- [devcontainer features][devcontainers_common_utils]
- [devcontainer archive][vscode_dev_containers]

ruff
- [tutorial][ruff_tutorial]
- [rules][ruff_rules]

Bookmark
[![](https://raw.githubusercontent.com/alefragnani/vscode-bookmarks/master/images/vscode-bookmarks-logo-readme.png)][code_mookmarks]
- [解説][bookmarks_intro]

1. `ctrl` + `alt` + `k` でbookmarkのオンオフ
2. `ctrl` + `alt` + `j` / `l` でbookmarkの前後へジャンプ
<!-- ////////////////////////////////////////////////////////////////////////////////////////// -->

## 参考サイト

- [rye + uv + ruff][rye_ruff]
- [ruffの紹介][introduction_ruff]
- [venvの使い方][how_to_use_venv]
- [ユーザアカウントの追加][adding_user_accounts]

<!-- ////////////////////////////////////////////////////////////////////////////////////////// -->

## ユーザ追加部 (抜粋)

```sh
groupadd --gid $USER_GID $USERNAME
useradd -s /bin/bash --uid $USER_UID --gid $USERNAME -m $USERNAME
echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME
chmod 0440 /etc/sudoers.d/$USERNAME
EXISTING_NON_ROOT_USER="${USERNAME}"
user_rc_path="/home/${USERNAME}"

if [ ! -f "${user_rc_path}/.bashrc" ] || [ ! -s "${user_rc_path}/.bashrc" ] ; then
    cp  /etc/skel/.bashrc "${user_rc_path}/.bashrc"
fi

# Restore user .profile defaults from skeleton file if it doesn't exist or is empty
if  [ ! -f "${user_rc_path}/.profile" ] || [ ! -s "${user_rc_path}/.profile" ] ; then
    cp  /etc/skel/.profile "${user_rc_path}/.profile"
fi
if [ -z "${USER}" ]; then export USER=$(whoami); fi
if [[ "${PATH}" != *"$HOME/.local/bin"* ]]; then export PATH="${PATH}:$HOME/.local/bin"; fi
```

install packages
```{.line-numbers}
bash-completion
curl
ca-certificates
vim-tiny
less
procps
iproute2
sudo
locales
tzdata

libc6
libgcc1
libicu[0-9][0-9]
libstdc++6
zlib1g

man-db
manpages
manpages-dev

openssh-client
git
tree
```

[devcontainers_common_utils]: https://github.com/devcontainers/features/tree/main/src/common-utils
[vscode_dev_containers]: https://github.com/microsoft/vscode-dev-containers
[ruff_tutorial]: https://docs.astral.sh/ruff/tutorial/
[ruff_rules]: https://docs.astral.sh/ruff/rules/
[code_mookmarks]: https://marketplace.visualstudio.com/items?itemName=alefragnani.Bookmarks
[bookmarks_intro]: https://web-souko.com/vscode-bookmarks/
[rye_ruff]: https://zenn.dev/dena/articles/rye_python_in_devcontainer
[introduction_ruff]: https://gihyo.jp/article/2023/03/monthly-python-2303
[how_to_use_venv]: https://qiita.com/shun_sakamoto/items/7944d0ac4d30edf91fde
[adding_user_accounts]: https://qiita.com/Spritaro/items/602118d946a4383bd2bb

[robust_python]: https://www.oreilly.co.jp/books/9784814400171/
[pydantic_docs]: https://docs.pydantic.dev/latest/
