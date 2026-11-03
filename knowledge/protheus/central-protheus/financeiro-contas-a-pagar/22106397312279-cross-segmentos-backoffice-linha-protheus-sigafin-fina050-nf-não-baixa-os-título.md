---
article_id: 22106397312279
category: Financeiro - Contas a Pagar
content_hash: d158733e5c621cf37cbb83c59c57498640ab6b1337d4005b885ce4de9a04dbe6
fetched_at: '2026-06-28T22:38:08.578625+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA050 - NF não baixa
  os títulos TX automaticamente da mesma forma que no contas a receber
type: support-article
updated_at: '2024-03-20T11:27:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22106397312279-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA050-NF-n%C3%A3o-baixa-os-t%C3%ADtulos-TX-automaticamente-da-mesma-forma-que-no-contas-a-receber
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22106397268119) Tempo aproximado para leitura: **00****:03:00 min** **Dúvida**Ao realizar a baixa total do título a pagar do tipo: NF não baixa os títulos TX automaticamente da mesma forma que no contas a receber.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões**Solução**

Quando há retenção dos impostos na emissão no contas a pagar, assim que emitir a **NF** a pagar é gerado os títulos do tipo **TX** correspondente a cada imposto **(PIS, COFINS, CSLL, IRRF...)**. Efetuado a baixa da **NF**, é realizado o pagamento para o fornecedor, e não sofrerá baixa os títulos **TX**, pois são títulos correspondente a **UNIAO** e não ao Fornecedor. Por isso que não é baixado automaticamente os títulos **TX** quando **NF** sofre baixa.

No **contas a receber**, se trata de recolhimento dos impostos **(abatimentos)** é de responsabilidade do cliente e não da empresa. Assim que efetua a baixa do **título no contas a receber,** os títulos de abatimentos serão baixados e a NF a receber sofrerá baixa.

**Importante:**

Quais os modos de identificação de um **título a pagar com imposto** em relação ao título gerador?

<http://tdn.totvs.com/pages/releaseview.action?pageId=232821364>

**Saiba mais:**[Comportamento ao baixar totalmente uma NF com retenção no contas a pagar](https://tdn.totvs.com/pages/releaseview.action?pageId=370606378)
