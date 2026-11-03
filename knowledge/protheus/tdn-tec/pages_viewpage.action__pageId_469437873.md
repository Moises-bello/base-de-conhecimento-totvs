---
content_hash: 8ecb214dc07271b8512b20c3508e0761d5769b157b52dbe760d41f33617217c5
fetched_at: '2026-07-02T19:24:24.207550+00:00'
page_id: '469437873'
product: protheus
source: tdn-tec
title: Thread (<thread>) disconnected prematurely! (RECEIVEBLOCK)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=469437873
version: 1
---

INLINE

A mensagem é registrada quando uma conexão for dada como encerrada (na camada de rede) antes da notificação de encerramento e do processamento da solicitação de encerramento.

A mensagem por si só não indica um erro, mas sim que "alguma coisa aconteceu com esta conexão, pois ela foi embora sem se despedir".

## Causa

Dentre as causas possíveis temos:

* Queda da aplicação;
* Queda de rede;
* Queda de energia;
* Etc.

## Observações

Em builds anteriores a 42.20141119, era apresentada a mensagem "`Thread (<thread>) communication failure! (RECEIVEBLOCK).`"

## Sobre o encerramento de conexões TCP

O término de conexões requer:

1. Que a aplicação envie uma mensagem de encerramento;
2. Que o servidor receba a mensagem de encerramento e processe a finalização;
3. Que o servidor envie uma mensagem para confirmar o término da conexão e feche o *socket*;
4. Que a aplicação feche o *socket*.
