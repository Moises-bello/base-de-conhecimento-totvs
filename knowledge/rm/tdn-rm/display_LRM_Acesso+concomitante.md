---
content_hash: 2135f3388d1b1ed1f2a9385ca0b46080fbdd8e7b87e1aa1f5a98d9329e9218cb
fetched_at: '2026-06-29T00:11:26.847598+00:00'
page_id: '721001288'
product: rm
source: tdn-rm
title: Acesso concomitante
type: documentation
url: https://tdn.totvs.com/display/LRM/Acesso+concomitante
version: 6
---

## **CONTEÚDO**

1. **Visão Geral**

Acesso ConcomitanteVisão Geral

## **01. VISÃO GERAL**

Ao acessar uma prescrição de forma concomitante, o sistema exibirá uma notificação informando ao usuário caso algum item seja alterado naquele momento.

Junto a notificação, é apresentado o recurso "Recarregar", para que a prescrição seja atualizada a pedido do usuário.

Para que essa funcionalidade seja habilitada, a tag **EnableRealTime** deve ser inserida no arquivo de configuração do **RM.Host.exe:**

**<add key="EnableRealtime" value="true" />**
