---
content_hash: 3be36b232e39f7988149885704f0a6c52c2fa3cbe21f28401a5e1e2fd513d045
fetched_at: '2026-06-29T00:10:38.151754+00:00'
page_id: '543096627'
product: rm
source: tdn-rm
title: Abertura da Subapuração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=543096627
version: 1
---

Na abertura de um período de Subapuração, o sistema irá alterar o seu status para **Encerrado**.  
Para manter a integridade de saldo dos períodos de subapuração, sabendo que este é atualizado no momento do seu encerramento, o sistema irá fazer algumas consistências antes de Encerrar uma subapuração:

* O sistema somente permitirá a reabertura de um período de subapuração se todos os períodos posteriores estiverem em aberto.
* Não será possível alterar o Status na tela de cadastrado, o status será alterado somente quando abrir ou encerrar um Período através dos processos.
