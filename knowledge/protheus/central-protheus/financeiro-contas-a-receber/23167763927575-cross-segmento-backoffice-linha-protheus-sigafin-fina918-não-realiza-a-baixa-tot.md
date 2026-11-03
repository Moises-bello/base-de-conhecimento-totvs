---
article_id: 23167763927575
category: Financeiro - Contas a Receber
content_hash: 3345c7101ebe02545251265cda089fdd57c6147ed6244ef4236a7899c71a016a
fetched_at: '2026-06-28T22:38:13.758512+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA918 - Não realiza
  a baixa total somente parcial.
type: support-article
updated_at: '2024-05-02T12:28:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23167763927575-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA918-N%C3%A3o-realiza-a-baixa-total-somente-parcial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23167763915799) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Ao realizar a baixa do FINA918 o sistema sempre deixa o título parcialmente baixado?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA918 - Todas as versões  
  
**Solução**O parâmetro **MV\_LJGERTX** na rotina **Conciliação de Pagamentos** define qual campo da tabela **Arquivo de Conciliação TEF (FIF)** será considerado na verificação com o campo Valor **(E1\_VALOR)** da tabela Contas a **Receber (SE1)** no processo de conciliação **(baixa do título).**

Se o parâmetro estiver igual a **.T.** o campo **Valor da Venda** **(FIF\_VLBRUT)** será considerado e se estiver **.F.** o campo **Valor Liquido** **(FIF\_VLLIQ)** será considerado na conciliação.

O parâmetro também define qual campo será considerado na somatória de registros na aba **Totais**.

**Saiba mais:**

[MV\_LJGERTX](https://tdn.totvs.com/pages/releaseview.action?pageId=203764928)

[FINA918 - Conciliação de Pagamentos](https://tdn.totvs.com/pages/releaseview.action?pageId=655196877)
