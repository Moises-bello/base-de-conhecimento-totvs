---
article_id: 14560826394391
category: FÉRIAS
content_hash: 5fb00a03a4137039bf79293fc7481822fbe2290984919274bce2e86732257a20
fetched_at: '2026-06-28T22:44:34.532275+00:00'
product: protheus
section_id: 10299705719575
source: central-protheus
title: RH - Linha Protheus - MEU RH - Quais parâmetros são levados em consideração
  para solicitação de férias
type: support-article
updated_at: '2026-06-16T18:59:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14560826394391-RH-Linha-Protheus-MEU-RH-Quais-par%C3%A2metros-s%C3%A3o-levados-em-considera%C3%A7%C3%A3o-para-solicita%C3%A7%C3%A3o-de-f%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27269520820503) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida:**  
Quais parâmetros são levados em consideração para solicitação de férias no MEU RH.  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - MEU RH - Todas as versões  
  
**Solução**  
Existem dois parâmetros que podem ser modificados para adequar as regras de férias especificas da empresa, são eles:  
  
**MV\_DSOLFER** - Quantidade de dias antes do final do período aquisitivo que as férias poderão ser solicitadas.  
**MV\_PORDFER**- Define a quantidade de dias de antecedência para solicitação de férias.  
  
O Portal Meu RH utiliza o conteúdo do parâmetro **MV\_PORDFER** para calcular a quantidade de dias de antecedência para solicitar Férias  todavia esse parâmetro não trata o limite de dias a serem tirados de Férias considerando o final do período concessivo do trabalhador conforme  parâmetro **MV\_DSOLFER**.  
  
Considerando os dados abaixo:  
Período Aquisitivo => 01/09/2018 a 30/09/2019  
Período Concessivo => 01/09/2019 a 30/09/2020  
  
Informando 45 dias no parâmetro **MV\_DSOLFER**, o sistema irá contabilizar que a data de início de férias limite é no dia **01/09/2021** (30/09/2021 – 30 + 1) pois assim ele poderá pedir 30 dias de férias a partir do dia 01/09/2021 e ainda retornar a tempo do término do período, evitando assim o pagamento de férias em dobro.  
  
Após alteração será necessário que o servidor seja reiniciado para que estes valores estejam ativos no portal.  
  
Para saber um pouco mais sobre os parâmetros e, suas funcionalidades, [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14492033545623).  
  
**Saiba Mais**  
[**CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH**](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
