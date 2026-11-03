---
content_hash: f5a9592b4b175c09df99637fd5ad132efa418f367a789747dd1481406cf22d81
fetched_at: '2026-07-02T19:24:25.112676+00:00'
page_id: '498465538'
product: protheus
source: tdn-tec
title: Correção - SmartClient para Mac OS apresenta relatório de erros após encerramento
  normal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=498465538
version: 1
---

Correção - SmartClient para Mac OS apresenta relatório de erros após encerramento normal

|  |  |
| --- | --- |
| Situação | Mesmo encerrando o SmartClient da maneira correta, instantes após o fechamento pode ser apresentado um relatório de erros do sistema operacional acusando o erro de "Segmentation fault". |
| Ocorrência | O erro pode ocorrer devido a uma tentativa de limpeza do cache de fontes do sistema operacional utilizado pelo SmartClient. |
| Correção | Foi aplicada uma correção no SmartClient para que a limpeza do cache de fontes seja realizada instantes antes do encerramento. No entanto, o Sistema Operacional pode estar com um cache de fontes já corrompido. Neste caso, somente a correção do SmartClient não é suficiente, sendo necessária a limpeza manual na estação em que apresentar o problema, rodando os seguintes comandos no terminal:  atsutil databases -removeUser atsutil server -shutdown atsutil server -ping  ( <https://www.macworld.com/article/1139383/fontcacheclear.html> ) |
| Informações adicionais | * Referente ao chamado: 5259650 * Referente à ocorrência: MTEC-2456 * Disponível em builds iguais ou superiores a 13.2.3.41 |
