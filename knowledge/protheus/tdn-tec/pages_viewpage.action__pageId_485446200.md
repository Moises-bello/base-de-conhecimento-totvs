---
content_hash: 2149db5e49cd371de1f4281eebc66642d6ea2646207cd938371095068b832a02
fetched_at: '2026-07-02T19:24:24.280701+00:00'
page_id: '485446200'
product: protheus
source: tdn-tec
title: End TopClient Thread (<dbaccess-thread-id>) (IOs <io-count> / RCV <received-bytes>
  / SND <sent-bytes> )
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=485446200
version: 1
---

INLINE

A mensagem é registrada quando uma conexão, estabelecida entre o servidor de aplicação e o gateway do banco de dados, é encerrada.

| Parâmetro | Descrição |
| --- | --- |
| <dbaccess-thread-id> | Corresponde ao processo interno do true que atende àquela conexão. |
| <io-count> | Corresponde a quantidade de I/O realizada pelo processo <dbaccess-thread-id> até o término da conexão. |
| <received-bytes> | Corresponde a quantidade de bytes recebidos pelo processo <dbaccess-thread-id> até o término da conexão. |
| <sent-bytes> | Corresponde a quantidade de bytes enviados pelo processo <dbaccess-thread-id> até o término da conexão. |

A informação que mais utilizamos neste contexto é a <dbaccess-thread-id>, pois qualquer mensagem relacionada a este processo será registrada juntamente a esse valor enquanto ele estiver sendo executado, ao ser registrado no dbconsolel.log, vai informar o número da <thread> ao qual a ocorrência pertence.
