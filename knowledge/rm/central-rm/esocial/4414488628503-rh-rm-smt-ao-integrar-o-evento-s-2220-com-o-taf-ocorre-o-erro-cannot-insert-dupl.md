---
article_id: 4414488628503
category: eSocial
content_hash: 29938dd8083026730b8d46ad5dd790ccaf2ae01409848ab89ea1182ffe6130fa
fetched_at: '2026-06-28T22:47:39.110537+00:00'
product: rm
section_id: 1500000912221
source: central-rm
title: 'RH - RM - SMT - Ao integrar o evento S-2220 com o TAF ocorre o erro: "Cannot
  insert duplicate key row in object ''dbo.C9W990''"'
type: support-article
updated_at: '2026-03-05T17:35:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414488628503-RH-RM-SMT-Ao-integrar-o-evento-S-2220-com-o-TAF-ocorre-o-erro-Cannot-insert-duplicate-key-row-in-object-dbo-C9W990
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16035189644311) Tempo aproximado para leitura: 00:02:00 min****Ocorrência**Ao integrar o evento S-2220 com o TAF, há o retorno com a seguinte mensagem de erro:  
Cannot insert duplicate key row in object 'dbo.C9W990' with unique index 'C9W990\_UNQ'. The duplicate key value is (01, 000001, 30112103868356, 20211015, 001424 , 0). O que fazer?

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Segurança e Saúde Ocupacional – A partir da 12.1.31 e superiores  
  
**Causa**Conforme leiaute do evento S-2220 no eSocial, o grupo <exame> possui como chave os campos **<dtExm>**e **<procRealizado>**, portanto não é possível informar o mesmo procedimento em dois exames diferentes na mesma data. 

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414477380119)

![](https://totvssuporte.zendesk.com/attachments/token/VBGAvGfOzPNN69zAxTuz2hOVP/?name=inline-404624002.png)  
  
**Solução**A orientação é localizar junto à [tabela 27](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-nt-03-2021-html/tabelas.html#27) do eSocial se há algum outro procedimento mais adequado relacionado ao exame que foi inserido, para que não hajam códigos de procedimentos iguais na mesma data.  

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34095527392919)  
  
Entendemos a situação, porém é uma limitação do leiaute, será necessário abertura de uma demanda junto ao governo para validar qual seria o procedimento a ser realizado em uma situação que ocorra dois exames com a mesma classificação da tabela 27.  
  
**Saiba Mais**

Para maiores informações, acesse:

- [RH - RM - SMT - Dúvidas frequentes sobre a geração do eventos de SST para o eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414423920535-TOTVS-RH-Linha-RM-SMT-D%C3%BAvidas-frequentes-sobre-a-gera%C3%A7%C3%A3o-do-eventos-de-SST-para-o-eSocial)
