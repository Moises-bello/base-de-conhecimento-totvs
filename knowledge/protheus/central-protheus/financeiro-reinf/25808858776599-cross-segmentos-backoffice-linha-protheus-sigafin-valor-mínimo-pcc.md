---
article_id: 25808858776599
category: Financeiro - Reinf
content_hash: c3c90d5e52adbbbd03418d4e7b5020c817944a4d69af92f45cb43117d7376f84
fetched_at: '2026-06-28T22:37:51.720771+00:00'
product: protheus
section_id: 17886892336407
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Valor mínimo PCC
type: support-article
updated_at: '2025-11-13T14:24:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25808858776599-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Valor-m%C3%ADnimo-PCC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25815987147031) Tempo aproximado para leitura: **00:05 min**

**Dúvida**

Porque o PCC com valor inferior a R$10,00 não aparece no painel?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.33.

**Solução**

Quando a soma dos **impostos de PIS, COFINS e CSLL** não atinge o valor mínimo de R$10, será gerada apenas a **NF**. Na inclusão do segundo título, que atinge o valor mínimo, será gerada a **NF** juntamente com os **TXs** dos impostos de **PCC,** com a soma dos valores de ambos os **títulos.**

1º Inclusão do primeiro registro e os impostos

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25808890185367)

2º Inclusão do segundo registro e os impostos

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25808858757527)

3º No **Financeiro** será gerado o segundo registro com a soma dos dos impostos

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25808858758807)**

No **TXT** para o **PCC** sempre será gerado no **T158** como pode ser observado neste cenário é levado a **base do PCC,** porém sem o valor dos tributos.

**Importante**

O **PCC** pode ser gerado de forma individual ou agregada. Essa escolha deve ser validada pela área fiscal da empresa.

**Cenário Individual**

|T158|2020||FPCCP 01|20240821|0||20240821|01|||

|T158AA|15002|300|2||||||

|T158AB|11|300|**15**|0|

|T158AB|18|300|**5**|0|  **=> Valor acumulado para cada tributo**

|T158AB|10|300|**3,25**|0|

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25808890192919)

**Cenário Agregado**

|T158|1010||FPCCP 01|20240821|0||20240821|01|||

|T158AA|15002|200|2||||||

|T158AB|29|200|0|0| **=> PCC sem valor do tributo**

|T158|2020||FPCCP 01|20240821|0||20240821|01|||

|T158AA|15002|300|2||||||

|T158AB|29|300|23,25|0| **=> Valor acumulado somando todos os tributos das duas NFs**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25808890194327)

**Saiba mais**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - REINF - Código da receita no TAF diferente do código da receita da Nota](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18664117621143-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-REINF-C%C3%B3digo-da-receita-no-TAF-diferente-do-c%C3%B3digo-da-receita-da-Nota?source=search)

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - REINF - Como enviar os impostos IR, PIS, COFINS e CSLL agregados no bloco 40](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17887265370647-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-REINF-Como-enviar-os-impostos-IR-PIS-COFINS-e-CSLL-agregados-no-bloco-40?source=search)
