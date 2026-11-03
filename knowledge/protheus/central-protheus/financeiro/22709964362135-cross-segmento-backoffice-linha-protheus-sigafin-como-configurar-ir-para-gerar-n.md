---
article_id: 22709964362135
category: Financeiro
content_hash: 39382aab6ededd4e77c1221e0ea39c86d5ca89a480dfeea03535a67fc126b713
fetched_at: '2026-06-28T22:38:01.058412+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Como configurar IR
  para gerar no contas à receber '
type: support-article
updated_at: '2024-04-15T21:13:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22709964362135-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Como-configurar-IR-para-gerar-no-contas-%C3%A0-receber
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22709936368535) Tempo aproximado para leitura: **05:00:00 min****Dúvida**

Cálculo de IRRF no contas a receber quando cliente não retém, como faço para gerar o título de IR no meu contas a receber:

**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - Financeiro - Todas as versões  
  
**Solução**

Para geração do **IR no contas a receber** é necessário seguir o boletim técnico abaixo, contudo, alguns clientes precisam fazer a auto retenção, ou seja, o responsável pelo recolhimento é do prestador do serviço, não do tomador.

Boletim de correção no cálculo de **IRRF de Contas a Receber:   
Saiba Mais**

[http://tdn.totvs.com/pages/releaseview.action?pageId=47908805](https://tdn.totvs.com/pages/releaseview.action?pageId=274314263)

Para geração do **IR no contas à receber**:

**Cliente**

1. No cadastro do **Cliente,** aba **Fiscais**, configure os seguintes campos:

Recolhe IRRF (A1\_RECIRRF) = SIM

**Natureza**

2. No cadastro do **Natureza**, aba **Impostos**, configure os seguintes campos:

**Calcula IRRF (ED\_CALCIRF)** = SIM

**Porc IRRF (ED\_PERCIRF)** = Alíquota desejada

**Recolhe IRRF (ED\_RECIRF)** = 3 - Cad.Cliente

**Importante:**

Após correção da rotina a retenção do IRRF, é possível gerar o imposto tanto no **contas a receber** como no **contas a pagar**, conforme a parametrização.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22709964346903)
