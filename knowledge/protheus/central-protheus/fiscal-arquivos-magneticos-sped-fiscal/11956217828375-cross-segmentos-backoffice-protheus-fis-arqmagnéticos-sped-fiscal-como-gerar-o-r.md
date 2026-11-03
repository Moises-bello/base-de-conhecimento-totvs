---
article_id: 11956217828375
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 8c4fe48c6e5d2c76c5c167803865002ab6871c25537a1b4061fbd308f024f912
fetched_at: '2026-06-28T22:42:03.574667+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - SPED FISCAL
  - Como gerar o registro C197 e E115 no Sped Fiscal para o estado do RJ pela rotina
  MATA985?
type: support-article
updated_at: '2023-02-01T19:41:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11956217828375-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-gerar-o-registro-C197-e-E115-no-Sped-Fiscal-para-o-estado-do-RJ-pela-rotina-MATA985
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Dúvida:**

Como gerar o registro **C197** e **E115** para as novas determinações do Rio de Janeiro?

**Ambiente**

Microsiga Protheus - Livros Fiscais - A partir da versão 12.1.25  
  
**Solução**

Estado do Rio de Janeiro houveram algumas alterações sobre o registro **C197** e **E115** dentro do Sped Fiscal seguindo as determinações abaixo:

**![](https://totvssuporte.zendesk.com/attachments/token/wDujJRaWMw0k7IZyGGdtKVRha/?name=image.png)**

Para atender esta nova legislação, realize o seguinte procedimento:

O código de reflexo apresentado na rotina MATA985 também deve ser informado na TES (**MATA080**) que irá utilizar na escrituração da nota, pelo campo **CC7\_CODLAN** (Cod Lan).

Campos de preenchimentos necessários na TES:

![](http://tdn.totvs.com/download/attachments/238035285/image2016-7-7%2020%3A10%3A16.png?version=1&modificationDate=1467933016000&api=v2)

Via rotina **Cadastro de lançamento de Apuração de ICMS (MATA985**), efetue a amarração do código de reflexo que está de acordo com sua operação fiscal:  
  
![](https://totvssuporte.zendesk.com/attachments/token/wmr1ECc0KCvlCDpdFqzy7RdTa/?name=image.png)  
  
Após isso, amarrando pela rotina **Valores Declaratórios** (**FISA140)** os dados do produto:

![](https://totvssuporte.zendesk.com/attachments/token/FemhN8efcP79xW2GDMr0Yn877/?name=image.png)

Para liberar os campos de grupo de produto e grupo de clientes na rotina acima configurar os seguintes parâmetros:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11956135856151)  
Na rotina **Informações Adicionais da Apuração** (**MATA017)** anexe os dados para que alimente a tabela **CDV** e gerar o registro **E115**:  
  
![](https://totvssuporte.zendesk.com/attachments/token/jvnnkHhs6Yd3ILWnghrvWgXYe/?name=image.png)  
  
Após este processo, rode a rotina **Apuração de ICMS** (**MATA953**) e gere o arquivo Sped Fiscal.  
  
Txt gerado.  
  
![](https://totvssuporte.zendesk.com/attachments/token/yS1QBamjuiGaZWImu5okZCWkH/?name=image.png)  
  
Para que você possua documentação complementar e que te auxilie a configurar conforme sua necessidade fiscal, segue:  
  
<https://tdn.totvs.com/pages/viewpage.action?pageId=640905665>  
  
<https://tdn.totvs.com/pages/releaseview.action?pageId=699806534>
