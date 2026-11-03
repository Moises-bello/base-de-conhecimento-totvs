---
article_id: 360059785234
category: Financeiro - Contas a Receber - PIX
content_hash: 48ff3db21dfddfcffd64ca90b34bc97d5db7f3aa09e686b73fbd46743253f8c1
fetched_at: '2026-06-28T22:38:16.524148+00:00'
product: protheus
section_id: 1500001539301
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA890 - IDCNAB X
  IDTRAN
type: support-article
updated_at: '2022-04-29T20:22:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059785234-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA890-IDCNAB-X-IDTRAN
---

**Dúvida**Qual a diferença entre IDCNAB e IDTRAN ?

**Ambiente**Cross Segmento - Backoffice Linha Protheus - Financeiro - FINA890 - A partir das versões 12.1.25  
 **Solução**Para boletos, a chave forte que identifica um título no sistema bancário é o conteúdo do campo **E1\_IDCNAB**.  
No PIX temos também uma chave forte, nos manuais é chamada de **TRANSACTION ID** (TXID) e no sistema fica armazenado na tabela **Monitor PIX**, no campo **F71\_IDTRAN**.  
Dessa forma para o **Contas a Receber** os títulos poderão ter **E1\_IDCNAB**, se a cobrança for efetuada por boleto, **F71\_IDTRAN** pelo PIX ou as duas formas caso possua os dois tipos de cobranças.  
No PIX do **Contas a Pagar** a chave de identificação continuará sendo o **E1\_IDCNAB**.

**Saiba mais**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=569478747>
