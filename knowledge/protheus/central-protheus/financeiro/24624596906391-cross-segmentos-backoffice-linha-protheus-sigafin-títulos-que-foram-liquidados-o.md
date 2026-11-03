---
article_id: 24624596906391
category: Financeiro
content_hash: 849fc6d73ffe006d7c9b4e9537e29595f6b64d4e2e0434081f6c0365a4d18c4b
fetched_at: '2026-06-28T22:38:03.454949+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Títulos que foram liquidados
  ou Faturados não são levados para o painel do TAF
type: support-article
updated_at: '2024-08-26T21:22:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24624596906391-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-T%C3%ADtulos-que-foram-liquidados-ou-Faturados-n%C3%A3o-s%C3%A3o-levados-para-o-painel-do-TAF
---

**Dúvida**

Realizamos a liquidação de alguns títulos com impostos, mas não estão sendo levados para o painel do TAF.

Ambiente Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**

Ao gerar uma liquidação ou fatura e ao executar o extrator fiscal, é necessário informar a data de inclusão da nota fiscal e a data de baixa, de modo que o extrator leve em consideração a geração do registro correspondente.

Exemplo

Temos dois cenários, onde o parâmetro MV\_BX10925 está definido como 1.

Exemplo:

Incluído três títulos, cada um em determinado mês, realizado a liquidação dos três títulos no mês de julho

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624649867543)

## Na FKW, será gerado o registro dos impostos para cada título

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624596865047)

Após a liquidação, um novo registro será gerado na FKW para o título liquidado, contendo a soma de todos os títulos envolvidos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624649871639)

**Importante**

Caso a renegociação seja gerada com uma Natureza Financeira (SED) que não inclui IR/PCC, enquanto o título original tinha IR/PCC na baixa, os dados da natureza de rendimento não serão migrados para a FKW, pois o TX não será gerado. Nessas circunstâncias, a retenção não ocorrerá e, consequentemente, os tributos não serão enviados ao TAF.

**Observação:**

No exemplo em que o campo IRRF A2\_CALCIRF =1 é gerado durante a emissão, não será criado um novo registro ao realizar a liquidação.

Após realizar a baixa do título liquidado, os títulos dos impostos serão gerados, neste caso, agregando todos os impostos de PCC.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624649874071)

Na rotina do **Extrator Fiscal**, aba **Geração** configuração dos campos **Date de**: "informar a data 04/04/2024 até a **Data até**: 03/07/2024

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624649876887)

Ao executar o extrator fiscal, deve ser gerado o registro T154 para cada título da liquidação/fatura, incluindo o título liquidado/Faturado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624649878807)

O registro T158 será gerado apenas para o título liquidado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624649881111)

No painel constará apenas o registro do título a liquidado/ faturado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624649882647)

Cenários, onde o parâmetro MV\_BX10925 está definido como 2.

Devido à geração dos impostos na emissão, não será criado o registro na FKW para a liquidação/fatura relacionada a renegociação dos títulos, após sua execução. Ao rodar o extrator fiscal, será gerado um registro para cada nota no T154 e T158.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624596887063)

No painel do TAF também

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24624649885207)

**Saiba mais:**

[FAQ - 0018 - Como fica os tributos quando houver uma renegociação de títulos a pagar](https://tdn.totvs.com/pages/releaseview.action?pageId=781210644)

[Fique por dentro das atualizações do Reinf](https://tdn.totvs.com/display/public/PROT/Protheus+-+REINF+Suporte+Financeiro#Eventos--839875140)

[How To Reinf](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19775578473751-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-REINF-Bloco-40-Gera%C3%A7%C3%A3o-dos-layouts-T154-e-T158)
