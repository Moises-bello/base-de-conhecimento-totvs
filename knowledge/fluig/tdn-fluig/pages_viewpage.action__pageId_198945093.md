---
content_hash: 3183957db2194b18eae852bebb532cf1d9a31c79bbcd75114013171e88d4a37b
fetched_at: '2026-06-28T21:35:19.196349+00:00'
page_id: '198945093'
product: fluig
source: tdn-fluig
title: ARQ - Erro ao enviar notificação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=198945093
version: 8
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**TOTVS Fluig Plataforma

**Versão:** 1.5.x e 1.6

# Ocorrência

No log da plataforma é apresentada a mensagem 'Error sending notification to...' e não é enviada notificação para a central de notificações do usuário.

# Causa

Esta mensagem é apresentada quando a plataforma não conseguiu enviar a notificação para o serviço Realtime.

# Solução

#### Atualização 1.6 ou superiores

Verifique se o serviço Realtime está iniciado. No caso de erro ao iniciar o serviço, recrie os serviços do Fluig no sistema operacional, conforme procedimento abaixo:

* Acessar a pasta raiz de instalação da plataforma via linha de comando;
* Digitar: nodeSetup.bat uninstall (para desinstalar os serviços);
* Digitar: nodeSetup.bat install (para reinstalar os serviços).

#### Atualização 1.5.x

Verifique se o serviço Realtime está rodando. No caso de erro ao iniciar o serviço, recrie os serviços do Fluig no sistema operacional, conforme procedimento abaixo:

* Acessar a pasta /jboss/bin do diretório de instalação da plataforma via linha de comando;
* Digitar: service64.bat uninstall (para desinstalar os serviços);
* Digitar: service64.bat install (para reinstalar os serviços).
