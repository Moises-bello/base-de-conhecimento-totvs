---
content_hash: 2fc2d9aa3e8e83328374793d9ca829652adbf9bfe94de855f3d9915173a0d342
fetched_at: '2026-07-02T19:24:27.869102+00:00'
page_id: '686463600'
product: protheus
source: tdn-tec
title: 'Application Server - Warning: tClientMonitor still in use ... waiting'
type: documentation
url: https://tdn.totvs.com/display/tec/Application+Server+-+Warning%3A+tClientMonitor+still+in+use+...+waiting
version: 2
---

tClientMonitor still in use waiting

tClientMonitor still in use waiting

No uso do load balance do true, o Load Balance inicia uma conexão de monitoramento dedicada para cada true Secundário configurado.

Cada thread de monitoramento conectada em um true fica em realizando requisições de status peridiocamente e o próprio mecanismo de balanceamento pode solicitar alguma informação a qualquer momento. Enquanto um pedido está sendo processado, essa requisição possui uma proteção de uso.

Quando alguma requisição está em execução e o processo de encerramento da thread de monitoramento se inicia pode aparecer a mensagem **tClientMonitor still in use...** até que a requisição seja concluída.

Essa mensagem é apenas um aviso e não é necessário nenhuma ação.
