---
article_id: 19837428461207
category: Financeiro - Reinf
content_hash: e44816cd4f08a027f8a0b3527a54727ea1795ccfda9736267b4a893acd88c0e8
fetched_at: '2026-06-28T22:37:51.880796+00:00'
product: protheus
section_id: 17886892336407
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Valor mínimo IRRF
type: support-article
updated_at: '2024-09-19T19:13:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19837428461207-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Valor-m%C3%ADnimo-IRRF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26492663801495)** Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**

IRRF com valor inferior a R$ 10,00 não aparece no painel

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**

**1º Cenário onde o IRRF é na emissão:**

Quando o título que não atingiu o valor mínimo for incluído, será gerada apenas a NF. Na inclusão do segundo título, que atinge o valor mínimo, será gerada a **NF** juntamente com o **TX** do **imposto de IRRF**, com a soma dos valores de ambos os títulos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19848476338583)

No **TXT** para o **IRRF na emissão** é gerado no **T154**, como pode ser observado neste cenário é levado a **base do IRRF**, porém sem o valor do tributo

|T154|852|01|F03IRPC01|20231214|0||01|852|01||500|||||||||0|0|0|0|0|0|0|0|0|0||||0||||1||||||||||0|0|0||||20231214|  
|T154AG|15002|2|500||||||  
|T154AH|12|500|0|0| => **IRRF sem o valor do tributo**  
|T154AB|1|500|

No **Painel** também será sem o tributo de **IRRF**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19848373789975)

Quando o valor acumulativo é superior aos R$ 10,00, o **TX do IRRF** é gerado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19848538188183)

No **TXT** é gerado o tributo com a somatória do **IRRF** das notas

|T154|963|01|F03IRPC01|20231214|0||01|963|01||1000|||||||||0|0|0|0|0|0|0|0|0|0||||0||||1||||||||||0|0|0||||20231214|  
|T154AG|15002|2|1000||||||  
|T154AH|12|1000|15|0| => **IRRF acumulado**  
|T154AB|1|1000|

No **Painel** ficará será enviado o mesmo que o **TXT**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19848419338775)

**1º Cenário onde o IRRF é na Baixa:**

A diferença é que ao gerar o segundo título, não será gerado o **TX**, será gerada apenas quando o segundo título for baixado.

![Gravar_2024_07_09_12_20_43_705.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/24759466700695)

**Primeira NF**

|T154|1010||F7070 01|20240709|0||||||500|||||||||0|0|0|0|0|0|0|0|0|0||||0||||3||||||||||0|0|0|||||  
|T154AB|1|500|

|T158|1010||F7070 01|20240709|0||20240709|01|||  
|T158AA|15002|500|2|||||| **>>> sem o IRRF**  
|T158AB|28|500|0|0|

**Segunda NF**

|T154|2020||F7070 01|20240709|0||||||10000|||||||||0|0|0|0|0|0|0|0|0|0||||0||||3||||||||||0|0|0|||||  
|T154AB|1|10000|

|T158|2020||F7070 01|20240709|0||20240709|01|||  
|T158AA|15002|10000|2||||||  
|T158AB|28|10000|105|0| **>>>>Valor do IRRF da primeira NF será somado a segunda NF**

No painel o mesmo comportamento

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24759462585239)

**Saiba mais:**

[FAQ - 0021 - Como são tratadas as retenções dispensadas por ser inferior a R$ 10,00?](https://tdn.totvs.com/pages/releaseview.action?pageId=804053851)

[Fique por dentro das atualizações Reinf Protheus](https://tdn.totvs.com/display/public/PROT/Protheus+-+REINF+Suporte+Financeiro#Eventos--839875140)

[How To - Reinf](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19775578473751)
