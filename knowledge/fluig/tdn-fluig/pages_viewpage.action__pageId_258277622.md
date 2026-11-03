---
content_hash: 4128a08f8ce5c44cc650df4df73dc996f050f0f0ae90115ea923e9260c14eeab
fetched_at: '2026-06-28T21:35:23.735909+00:00'
page_id: '258277622'
product: fluig
source: tdn-fluig
title: Habilitar atualização automática da Timeline
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=258277622
version: 7
---

Atenção

Esta página é destinada para atualizações 1.6 e superiores do TOTVS Fluig Plataforma.

# Índice

4true.\*ndicenone

# Objetivo

---

A plataforma possui a opção de atualizar automaticamente a *timeline*, assim os novos *posts* aparecem na *timeline* sem a necessidade de recarregar a página.

# Configuração

---

Para habilitar este recurso, é necessário:

falsesteps-disable-chatpasso1Passo 1

* Acesse a plataforma com o usuário **wcmadmin**:

passo2Passo 2

* Acesse **Painel de controle** → **WCM** → **Empresas.**

passo3Passo 3

* Selecione a empresa em que deseja habilitar a atualização automática da *timeline* e clique em **Editar**.

passo4Passo 4

* Na empresa desejada, clique no botão **Cadastrar dados adicionais** e adicione:

|  |  |
| --- | --- |
| **Chave** | **Valor** |
| realtime.enabled | true |

Observação

Para desativar este recurso, altere o valor da chave realtime.enabled para "false".

fimPronto

* Pronto. Após isso, os novos posts serão atualizados na Timeline sem recarregar a página.

Importante

Para utilizar este recurso, o serviço fluig\_RealTime deve estar iniciado.
