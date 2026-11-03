---
article_id: 8276124721559
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: c23f2ca47417b75558e5fac7cc729959b4cd3e9c7d5f259943c84ddd9eca2f37
fetched_at: '2026-06-28T22:42:00.848797+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS -   Arq. Magnéticos - Como gerar
  o registro  D101 do Sped Fiscal?
type: support-article
updated_at: '2022-08-19T12:19:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8276124721559-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-registro-D101-do-Sped-Fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar o registro **D101** do **Sped Fisca**l?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Solução**O registro **D101** é gerado com o intuito de prestar informações complementares do **CT-e (modelos 57, 63 e 67)** em operações interestaduais destinadas  à **Consumidor Final não Contribuinte do ICMS.**

Para geração do registro **D101** deve ser realizada a seguinte configuração nos cadastro de  **Clientes** e de **TES**:

**1 - Cadastro de Clientes:**

**Aba Cadastrais**

- Campo **Tipo - A1\_TIPO** = F

**-** Campo **Insc. Estadual (A1\_INSCR)** **deve** estar em **BRANCO** ou **ISENTA**

**Aba Fiscais**

 - Campo **Contribuinte (A1\_CONTRIB)** com conteúdo **Não**

**2 - Cadastro de TES**

**Aba Impostos**

- Campo **Calcula ICMS (F4\_ICM)** = SIM

- Campo **Calc. Difal (F4\_DIFAL)** = SIM

- Campo **Calc.Dif.ICM (F4\_COMPL)** = SIM

Após, gere o **pedido de vendas** utilizando os cadastros criados e em seguida gere o **Sped Fiscal**. Será gerado o **registro D101**: **![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8276124076823/mceclip0.png)**
