---
article_id: 17534396709911
category: Financeiro
content_hash: b19d9546ba90724da834b666f4d03a4d0666240cd49b71918304cc842ff459c8
fetched_at: '2026-06-28T22:38:04.154172+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - EXTFISXTAF - Envio
  do título para o Extrator fiscal
type: support-article
updated_at: '2023-09-28T16:44:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17534396709911-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-EXTFISXTAF-Envio-do-t%C3%ADtulo-para-o-Extrator-fiscal
---

**Dúvida**

Na inclusão do título, era gerado os blocos T154 e T158, enviado ao TAF, porém a nova regra é gerar o bloco T154 na emissão do título e o T158 na baixa do título principal.  
Qual Comportamento do sistema em relação à geração do bloco T154?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**

Devido à alteração da nova regra foi alterado o processo, o **bloco T154** ao rodar o extrator como TXT é enviado o **bloco T154**

Título **PCC** e **IR** na emissão com PCC em 14/08/2023

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17535875053207)

Dados gerados pelo **extrator** no mês 08/2023:

Envio **PCC**

|T154|03030||FPCCP 01|20230814|0||||||3000|||||||||0|0|0|0|0|0|0|0|0|0||||0||||3||||||||||0|0|0||||  
|T154AB|1|3000|

Envio **IR**, em casos que o **IR é na emissão**

|T154|01||F03IRPC01|20230814|0||||||9000|||||||||0|0|0|0|0|0|0|0|0|0||||0||||3||||||||||0|0|0||||  
|T154AG|15002|2|9000||||||  
|T154AH|12|9000|90|0|  
|T154AB|1|9000|

Ao rodar o **Extrator** como banco de dados, no mês 09/2023 é enviado o **T154**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17533311677591)

Quando o envio é do **PCC** não será exibido o título no **painel gestor**. Porém, quando o título possui o **IR** **na emissão** será enviada

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17533630454167)

Após a baixa do título pai, os blocos se tornaram independentes, porém, no **extrator** será enviado os dois blocos **T154** e **T158** novamente.

**Extrator em TXT:**

**|T154|01||F03IRPC01|20230914|0||||||9000|||||||||0|0|0|0|0|0|0|0|0|0||||0||||3||||||||||0|0|0||||**  
**|T154AG|15002|2|9000||||||**  
**|T154AH|12|9000|90|0|**  
**|T154AB|1|9000|**  
**|T154|03030||FPCCP 01|20230914|0||||||3000|||||||||0|0|0|0|0|0|0|0|0|0||||0||||3||||||||||0|0|0||||**  
**|T154AB|1|3000|**  
|T158|01||F03IRPC01|20230914|0||20231019|01|||  
|T158AA|15002|9000|2||||||  
|T158AB|11|9000|270|0|  
|T158AB|18|9000|90|0|  
|T158AB|10|9000|58,5|0|  
|T158|03030||FPCCP 01|20230914|0||20231019|01|||  
|T158AA|15002|3000|2||||||  
|T158AB|11|3000|90|0|  
|T158AB|18|3000|30|0|  
|T158AB|10|3000|19,5|0|

**Extrator banco de dados**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17534125783959)

Como pode ser observado, é reenviado o **T154** com status "**Alterado**" em amarelo, somente para indicar que é um reenvio, mas não afetará o período já apurado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17534353581847)

No painel constará os registros gerados pela baixa do título principal para apuração com seus devidos impostos. 

**Saiba mais**

<https://tdn.totvs.com/pages/releaseview.action?pageId=737543501>
