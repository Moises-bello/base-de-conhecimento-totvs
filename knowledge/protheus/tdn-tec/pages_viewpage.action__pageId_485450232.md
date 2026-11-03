---
content_hash: 1508a786325f3b7f660f0468288a5ddf38ddd06547971115e07c8b1b53cbee57
fetched_at: '2026-07-02T19:24:24.288022+00:00'
page_id: '485450232'
product: protheus
source: tdn-tec
title: Exit TopClient Thread (<dbaccess-thread-id>) [TERMINATED] (IOs <io-count> /
  RCV <received-bytes> / SND <sent-bytes> )
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=485450232
version: 2
---

INLINE

A mensagem é registrada quando uma conexão foi interrompida ou quando a conexão for dada como encerrada (na camada de rede) antes da notificação de encerramento e do processamento da solicitação de encerramento.

Em geral, a causa do encerramento é registrada antes dessa mensagem.

| Parâmetro | Descrição |
| --- | --- |
| <dbaccess-thread-id> | Corresponde ao processo interno do true que atende àquela conexão. |
| <io-count> | Corresponde a quantidade de I/O realizada pelo processo <dbaccess-thread-id> até o término da conexão. |
| <received-bytes> | Corresponde a quantidade de bytes recebidos pelo processo <dbaccess-thread-id> até o término da conexão. |
| <sent-bytes> | Corresponde a quantidade de bytes enviados pelo processo <dbaccess-thread-id> até o término da conexão. |

A informação que mais utilizamos neste contexto é a <dbaccess-thread-id>, pois qualquer mensagem relacionada a este processo será registrada juntamente a esse valor enquanto ele estiver sendo executado, ao ser registrado no dbconsolel.log, vai informar o número da <thread> ao qual a ocorrência pertence.
