---
article_id: 19671600360855
category: Financeiro - Reinf
content_hash: 2caa77277c5b89e8cb7a46df01f0de3521eb473e9f1177cc5a6464d258e19f81
fetched_at: '2026-06-28T22:37:51.798305+00:00'
product: protheus
section_id: 17886892336407
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - REINF - Como gerar
  o IRRF no Reinf
type: support-article
updated_at: '2024-09-19T18:17:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19671600360855-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-REINF-Como-gerar-o-IRRF-no-Reinf
---

**Dúvida**Como gerar o IRRF no Reinf?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – Todas as versões  
  
**Solução**

Ao contrário do **PCC**, o **IRRF** pode ser gerado durante a **emissão, contabilização ou baixa para o Reinf**.

No cadastro do **Fornecedor**, na aba **Fiscais**, no campo **A2\_CALCIRF**.

**Normal - Emissão**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19671578583959)

**Comportamento no sistema:**

**IRRF na emissão é gerado no T154**, print no arquivo TXT

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19671604780311)

**IRRF - Baixa**

**IRRF na baixa é gerado o T158**, print no arquivo TXT

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19671586413079)  
 **IRRF - Normal - Contabilização**

Este procedimento aplica-se exclusivamente ao **IR na emissão** (**Tributo 12)**; os títulos com pagamento de **IR (tributo 28)** devem considerar apenas a data de pagamento do título.

Os parâmetros abaixo devem ser ajustados para considerar a contabilização:

**MV\_VENCIRF**=C

**MV\_VCTIRPF**=C

**MV\_TAFDT40**=1

Ao executar o **Extrator Fiscal**, aba **Financeiro**, ajustar o campo de seleção de **títulos a pagar**, conforme cenário abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24457075047575)

Desta forma será considerado o **IRRF na data da contabilização**.

Caso seja necessário ajustar o **envio do IRRF**, pode usar o PE a seguir para auxiliá-lo no processo

[F989DTCTB - Ponto de entrada para manipular a data contábil do T154](https://tdn.totvs.com/pages/releaseview.action?pageId=806757590)

**Saiba mais:**

[Quais os fatos geradores serão considerados no extrator financeiro?](https://tdn.totvs.com/pages/releaseview.action?pageId=737543501)

[Fique por dentro das atualizações Reinf Protheus](https://tdn.totvs.com/display/public/PROT/Protheus+-+REINF+Suporte+Financeiro#Eventos--839875140)

[How To - Reinf](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19775578473751)
