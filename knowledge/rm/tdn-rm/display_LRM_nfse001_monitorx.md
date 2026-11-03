---
content_hash: e53341dc2da9580d8b89129be12398be9cdd0dee08d93c273a944bf7afa2291d
fetched_at: '2026-06-29T00:10:53.858921+00:00'
page_id: '588698500'
product: rm
source: tdn-rm
title: nfse001_monitorx
type: documentation
url: https://tdn.totvs.com/display/LRM/nfse001_monitorx
version: 2
---

Caso não seja autorizada a NFS-e ou não obtido o retorno da mesma é chamado o método nfse001\_monitorx para analisar a situação da nota.

* Regra geral: neste caso será verificado se o TSS retornou um **ERRO** maior ou igual a 200 , caso não seja retornado o **ERRO** é verificado as tag de **STATUS e RECOMENDACAO**:

Quando o lote da NFS-e estiver travado:

| STATUS = 2 → Se a NFS-e estiver sido enviada a mais de 2 horas a mesma deverá ser rejeitada apresentando a mensagem:  *A NFS-e esta aguardando transmissão do lote desde {horário de envio} devido a falta de retorno da prefeitura o lote será descartado e a NFS-e deverá ser reenviada..*  Ou  STATUS = 3 → Será atribuído o código 200 e a NFS-e será rejeitada.    Caso não atenda nenhum dos status acima a NFS-e manterá como pendente até que o TSS mude algum dos campos verificados no monitorrx apresentando a mensagem:  *NFS-e esta aguardando retorno da prefeitura desde {horário de envio}. Em {horário de envio - 2h} o lote será descartado e um novo envio poderá ser solicitado, gentileza aguardar..* |
| --- |

Para rejeição:

| É verificado se o campo **RECOMENDACAO c**ontêm****as seguintes frases:  *"LOTE RECUSADO"*  *"ASSINAR"*  *"RETRANSMITA"*  *Ou*  *STATUS = 5*  *Caso seja um cancelamento é verificado se o campo **STATUS  = 7**e **STATUSCANC = 3*** |
| --- |

Erros não catalogados ou não esperados:

| É verificado se o campo **RECOMENDACAO c**ontêm a**** seguinte frase:  *"ERRO NÃO CATALOGADO"*  ***Caso não seja localizado a NFS-e não ficará rejeitada, mantendo seu status inicial.*** |
| --- |
