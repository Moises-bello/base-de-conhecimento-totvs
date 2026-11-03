---
article_id: 36017397980823
category: Financeiro - Movimentação Bancária
content_hash: f96908af0c76ce30521c0044d1efb7613c8186335cebd5b2fdbed7236eae511b
fetched_at: '2026-06-28T22:38:19.386330+00:00'
product: protheus
section_id: 1500001550402
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Como funciona
  o campo E5_SITUACA nas movimentações financeiras de estorno
type: support-article
updated_at: '2025-10-31T17:33:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36017397980823-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-Como-funciona-o-campo-E5-SITUACA-nas-movimenta%C3%A7%C3%B5es-financeiras-de-estorno
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36017397963799) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**  
Como funciona o campo E5\_SITUACA nas movimentações financeiras?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
O campo **E5\_SITUACA** segue o comportamento abaixo nas carteiras a receber e pagar.  
  
**Contas a receber**:  
Quando uma baixa é cancelada via **FINA070,** é preenchido somente o campo **E5\_DTCANBX**com a data do cancelamento da baixa e o campo **E5\_SITUACA**permanece vazio.

* Quando sofre uma exclusão de baixa, o movimento tem o campo **D\_E\_L\_E\_T\_**marcado com '\*'.
* Quando o título passa por uma liquidação e a liquidação é cancelada, o campo **E5\_SITUACA**é preenchido com 'C' e o **E5\_DTCANBX**fica vazio.
* Quando a compensação é estornada, é gerado um movimento de estorno e os campos em questão ficam em branco.
* Quando a compensação é excluída, é marcado somente o campo **D\_E\_L\_E\_T\_**

**Contas a pagar**:  
Quando uma baixa é cancelada via **FINA080,**é preenchido o **E5\_SITUACA**= 'C' e **E5\_DTCANBX**com a data do cancelamento da baixa.

* Quando sofre uma exclusão de baixa, o movimento tem o campo **D\_E\_L\_E\_T\_**marcado com '\*'.
* Quando a compensação é estornada, é gerado um movimento de estorno e os campos em questão ficam em branco.
* Quando a compensação é excluída, é marcado somente o campo **D\_E\_L\_E\_T\_**
* Quando cancelado uma fatura, os campos em questão ficam em branco e somente é marcado o campo **D\_E\_L\_E\_T\_**

**Saiba mais fsfsdsdsds**  
[Movimentos Bancários - FINA100 - Financeiro - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=501480542)
