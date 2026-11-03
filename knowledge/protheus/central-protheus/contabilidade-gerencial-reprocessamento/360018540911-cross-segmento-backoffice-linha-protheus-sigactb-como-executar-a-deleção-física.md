---
article_id: 360018540911
category: Contabilidade Gerencial - Reprocessamento
content_hash: e4afae4ee05377bc36ef5841193479f9dc09abca91f16749f8ec270989590f77
fetched_at: '2026-06-28T22:40:41.961645+00:00'
product: protheus
section_id: 1500001548742
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Como executar a deleção
  física e lógica de saldos reprocessados via rotina CTBA190?
type: support-article
updated_at: '2022-03-21T12:15:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018540911-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-executar-a-dele%C3%A7%C3%A3o-f%C3%ADsica-e-l%C3%B3gica-de-saldos-reprocessados-via-rotina-CTBA190
---

**Dúvida**Como executar a deleção física e lógica de saldos reprocessados via rotina CTBA190?  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.  
  
**Solução**

E necessário configurar o parâmetro MV\_CTB190D como Tipo Lógico, conteúdo .T. ou .F. com a seguinte descrição:

"Indica se os registros serão excluídos fisicamente na rotina CTBA190 "Reprocessamento Contábil". T = Exclui Fisicamente, F = Não Exclui Fisicamente"
