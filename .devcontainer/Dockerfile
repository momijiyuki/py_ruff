# FROM mcr.microsoft.com/vscode/devcontainers/base:bullseye
FROM python:3.11-bullseye

ARG USERNAME="codes"
ARG USERUID="1000"
ARG USERGID="1000"

ENV DEBIAN_FRONTEND=noninteractive \
    LANG=ja_JP.UTF-8 \
    LANGUAGE=ja_JP:ja \
    LC_ALL=ja_JP.UTF-8 \
    TZ=JST-9 \
    TERM=xterm \
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]$(__git_ps1 "(%s)")\$ '

COPY user_registration.sh /tmp/install_lib/
COPY bin/ /tmp/install_lib/bin/
COPY requirements.txt /home/$USERNAME/

RUN apt-get update && \
    apt-get purge -y imagemagick imagemagick-6-common && \
    apt-get install -y --no-install-recommends \
    bash-completion \
    openssh-client \
    iproute2 \
    procps \
    curl \
    tree \
    ca-certificates \
    vim \
    python3-tk \
    less \
    libc6 \
    libgcc1 \
    libicu[0-9][0-9] \
    libstdc++6 \
    zlib1g \
    locales \
    sudo \
    man-db \
    manpages \
    manpages-dev \
    git \
    tzdata && \
    apt-get -y upgrade --no-install-recommends && \
    apt-get autoremove -y && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/* && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8


RUN bash /tmp/install_lib/user_registration.sh
#  && \
#     bash /tmp/install_lib/install.sh

WORKDIR /home/$USERNAME

RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt && \
    curl -o /home/$USERNAME/.git-completion.bash https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash \
    -o /home/$USERNAME/.git-prompt.sh https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh && \
    echo 'PATH="$HOME/.local/bin:$PATH"' >> /home/$USERNAME/.bashrc && \
    echo 'source $HOME/.git-completion.bash' >> /home/$USERNAME/.bashrc && \
    echo 'source $HOME/.git-prompt.sh\nGIT_PS1_SHOWDIRTYSTATE=true' >> /home/$USERNAME/.bashrc && \
    echo "PS1='"${PS1}"'" >> /home/$USERNAME/.bashrc

USER $USERNAME
