---
article_id: 21676695230871
category: esocial - Periódicos
content_hash: f362f70f1ed90212b2244ec113e9254a115ab3e8397350c5129d8875876f494c
fetched_at: '2026-06-28T22:47:09.193401+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Como é gerado o XML para o eSocial quando o funcionário
  possui férias a partir do leiaute S-1.0
type: support-article
updated_at: '2024-12-26T16:04:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21676695230871-RH-RM-FOP-eSocial-Como-%C3%A9-gerado-o-XML-para-o-eSocial-quando-o-funcion%C3%A1rio-possui-f%C3%A9rias-a-partir-do-leiaute-S-1-0
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21676655898007) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como é gerado o XML para o eSocial quando o funcionário possui férias a partir do leiaute S-1.0?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir das versões 12.1.29.278, 12.1.31.193, 12.1.32.131 e Superiores  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
1. Verifique se os eventos constam cadastrados corretamente no "De/Para eventos férias eSocial (S-1200)" no [Parametrizador | eSocial | Configurações Gerais 6/7](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17203402479255-RH-RM-FOP-eSocial-Parametrizador-eSocial-Configura%C3%A7%C3%B5es-Gerais-6-7) e [Parametrizador | eSocial | Configurações Gerais 7/7](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6805437378455-RH-RM-FOP-eSocial-Parametrizador-eSocial-Configura%C3%A7%C3%B5es-Gerais-7-7?source=search), conforme exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21676655899031)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21676695217815)

2. Cadastre e lance as férias;

![](https://tdn.totvs.com/download/attachments/627729108/image2021-7-6_9-7-48.png?version=1&modificationDate=1625575584647&api=v2)

![](https://tdn.totvs.com/download/attachments/627729108/image2021-7-6_9-8-16.png?version=1&modificationDate=1625575584590&api=v2)

3. No envelope de pagamento será lançado os eventos referentes ao recibo de férias e a verba de dias  trabalhados;

![](https://tdn.totvs.com/download/attachments/627729108/image2021-7-6_9-12-38.png?version=1&modificationDate=1625575584537&api=v2)

4. Ao gerar o xml do evento S-1200 serão gerados dois grupos <dmDev>, sendo um com a tag <ideDmDev> conforme o número do envelope de pagamento e outro <ideDmDev> conforme recibo de férias (o numero do ideDmDev será da data de pagamento das férias);

4.1. <ideDmDev> conforme envelope de pagamento, eventos de IRRF e base de INSS serão substituídos pelos eventos cadastrados no parametrizador;

![](https://tdn.totvs.com/download/attachments/627729108/image2021-7-6_9-39-30.png?version=1&modificationDate=1625575584337&api=v2)

![](https://tdn.totvs.com/download/attachments/627729108/image2021-7-6_9-21-20.png?version=1&modificationDate=1625575584437&api=v2)

4.2. <ideDmDev> com a data de pagamento conforme recibo de férias e eventos colocados no parametrizador.

![](https://tdn.totvs.com/download/attachments/627729108/image2021-7-6_9-39-57.png?version=1&modificationDate=1625575584267&api=v2)

5. Ao gerar o evento S-1210 será gerado o líquido correspondente ao dois recibos.

![](https://tdn.totvs.com/download/attachments/627729108/image2021-7-6_9-51-3.png?version=1&modificationDate=1625575863817&api=v2)

**Importante**

* Caso possua eventos de médias no recibo de férias esses eventos serão somados aos eventos de antecipação de férias.
* Caso utilize tomador de serviço o recibo de férias será gerado para o tomador empresa.

**Saiba mais**  
Para mais informações acesse:  
[S-1200 e S-1210: Recibo de Férias no leiaute S-1.0 - Linha RM - TDN (totvs.com)](https://tdn.totvs.com/pages/releaseview.action?pageId=627729108#1-1)
