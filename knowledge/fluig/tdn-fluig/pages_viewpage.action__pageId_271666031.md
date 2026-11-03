---
content_hash: d694c5bd3d01e4e4b4f264acb98ccf537a4078dbe63ebef3b1a90c3be9a39a6a
fetched_at: '2026-06-28T21:35:24.795411+00:00'
page_id: '271666031'
product: fluig
source: tdn-fluig
title: Backup da aplicação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271666031
version: 15
---

Atenção

Esta página foi revisada para considerar as configurações de server para a atualização 1.6 ou superiores.

# Índice

3true.\*ndicenone

# Objetivo

---

O objetivo deste guia é orientar o administrador do ambiente sobre a criação de cópias de segurança do banco de dados, pasta de instalação e diretório de arquivos do TOTVS Fluig Plataforma.

# Backup da aplicação

---

Para fazer o backup da aplicação da plataforma, o ideal é fazer um backup completo incluindo a pasta de instalação, volume completo e a base de dados. Esse backup pode ser manual ou automatizado, dependendo do que acharem melhor.  
  
Quanto ao backup do volume, basta salvar a pasta completa. O backup da instalação também pode ser da pasta completa, assim se necessário é possível restaurá-lo.

Confira a seguir o procedimento de acordo com o sistema operacional.

## Windows

---

falsewindowsParar serviços

**1.** Parar todos os serviços do Fluig (fluig\_RealTime, fluig\_Indexer, FLUIG).

Copiar banco de dados

**2.** Acessar o gerenciador do banco de dados e realizar cópia da base de dados do Fluig.

O gerenciamento do banco de dados é de responsabilidade do cliente. Acione sua equipe de TI para receber orientação de como fazer o *backup*.

Copiar instalação

**3.** Copiar os arquivos da aplicação (diretório de instalação e volume).

**3.1** Apagar as pastas temporárias data, log, servers e temp localizadas em [diretório\_instalação]\appserver\domain.

**3.2** Fazer a cópia de segurança dos diretórios de instalação (onde são armazenados os arquivos de sistema, responsáveis pelo funcionamento da plataforma) e de volume (onde ficam armazenados os documentos, formulários, templates e demais arquivos publicados pelos usuários na plataforma).

**A localização do volume é definida pelo administrador durante a criação da empresa no Fluig.**

## Linux

---

falseLinuxtrueL1Parar serviços

**1.**Parar todos os serviços do Fluig

|  |  |
| --- | --- |
| Utilizando o init | bashfluig |
| bashIndexer |
| bashRealTime |
| Utilizando o systemd | bashfluig |
| bashIndexer |
| bashRealTime |
| Sem serviços | bashfluig |
| bashIndexer |
| bashRealTime |

L2Copiar banco de dados

**2.** Acessar o gerenciador do banco de dados e realizar cópia da base de dados do Fluig.

O gerenciamento do banco de dados é de responsabilidade do cliente. Acione sua equipe de TI para receber orientação de como fazer o *backup*.

L3Copiar instalação

**3.** Copiar os arquivos da aplicação (diretório de instalação e volume).

**3.1** Apagar as pastas temporárias data, log, servers e temp localizadas em [diretório\_instalação]/appserver/domain.

bashPastas temporárias

**3.2** Fazer a cópia de segurança dos diretórios de instalação (onde são armazenados os arquivos de sistema, responsáveis pelo funcionamento da plataforma) e de volume (onde ficam armazenados os documentos, formulários, templates e demais arquivos publicados pelos usuários na plataforma).

bashPasta de InstalaçãobashVolumeDica

Saiba mais sobre a configuração e utilização de volumes em [Plataforma ❙ Volumes (wcmadmin)](https://tdn.totvs.com/x/jP-uDQ).
