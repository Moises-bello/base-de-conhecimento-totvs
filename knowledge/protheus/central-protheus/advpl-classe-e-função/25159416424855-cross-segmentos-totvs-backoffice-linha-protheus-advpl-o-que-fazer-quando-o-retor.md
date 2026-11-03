---
article_id: 25159416424855
category: ADVPL - Classe e Função
content_hash: 7d86ef21c5b351f839823357152e7c495585532dfb9776fec9ff95703801d2b9
fetched_at: '2026-06-28T22:40:21.628725+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - O que fazer quando
  o retorno de um JSON maior que 2MB, utilizando a classe FWRest não apresenta no
  Client do Webservice(Postman)?
type: support-article
updated_at: '2024-07-26T14:21:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25159416424855-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-O-que-fazer-quando-o-retorno-de-um-JSON-maior-que-2MB-utilizando-a-classe-FWRest-n%C3%A3o-apresenta-no-Client-do-Webservice-Postman
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25159426955415) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**O que fazer quando o retorno de um JSON maior que 2MB, utilizando a classe FWRest não apresenta no Client do Webservice(Postman)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS ADVPL - Todas as versões  
  
**Solução**

Neste caso, como o JSON de retorno da API que está consumindo é extenso, você pode utilizar paginação para filtrar a quantidade de registros retornados por página com o page e pageSize.  
   
Documentação:  
[Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Paginação com page e pageSize](https://centraldeatendimento.totvs.com/hc/pt-br/articles/24473848681367-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Pagina%C3%A7%C3%A3o-com-page-e-pageSize?source=search)  
   
Ou você pode salvar a resposta num arquivo.:  
Para salvar a resposta de uma API em um arquivo usando o Postman, siga estes passos:  
1. Faça a requisição: Execute a solicitação como de costume.  
2. Clique nos três pontos no canto superior direito do painel de resposta.  
3. Selecione "Save Response" e escolha onde deseja salvar o arquivo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25159426956055)

Isso permitirá que você armazene a resposta completa sem se preocupar com limitações de exibição no Postman.  
  
**Saiba mais**[FWRest](https://tdn.totvs.com/display/public/framework/FWRest)
