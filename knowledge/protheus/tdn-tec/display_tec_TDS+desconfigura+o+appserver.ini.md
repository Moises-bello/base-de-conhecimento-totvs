---
content_hash: 9444169f52635db64bf30f6c03a992893bbe71241df62aced1ba8660275964ce
fetched_at: '2026-07-02T19:24:21.490951+00:00'
page_id: '267803754'
product: protheus
source: tdn-tec
title: TDS desconfigura o appserver.ini
type: documentation
url: https://tdn.totvs.com/display/tec/TDS+desconfigura+o+appserver.ini
version: 7
---

Aparentemente o TDS bagunça as configurações do server.

|  |  |
| --- | --- |
| Situação | Ao editar configurações do server as informações do appserver.ini são desconfiguradas. |
| Ocorrência | O usuário apresenta uma evidência que mostra o TDS bagunçando as configurações do servidor. |
| Correção | O erro ocorria no servidor durante a leitura do appserver.ini. Independentemente do tipo de quebra de linha encontrado (Windows ou Unix), o servidor envia ao TDS o appserver.ini com quebras de linhas do tipo Unix (LF) e ao requisitar a gravação do appserver.ini modificado, o TDS envia o appserver.ini modificado com a quebra do tipo Unix e caso o servidor estiver rodando em ambiente Windows ele trocará o terminador para o padrão Windows. Observar que o appserver.ini será gravado corretamente com o binário do servidor com a correção. Enquanto o binário não for liberado, para usuários do Windows que observem o appserver.ini bagunçado após utilizar o TDS, utilizem um editor de texto que trate quebras de linha de outros SO, como por exemplo o Notepad++ ou UltraEdit. |
| Informações adicionais | * Referente ao chamado: TVKMYY * Referente à ocorrência: SSIM-1238 * Disponível em builds superiores a 11.3.3 |
