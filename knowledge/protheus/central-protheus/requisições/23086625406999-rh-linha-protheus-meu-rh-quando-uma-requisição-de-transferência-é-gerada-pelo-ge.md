---
article_id: 23086625406999
category: REQUISIÇÕES
content_hash: 1b6c0c945b81e51a4b70afe967e472e61086d4b3b98894d587df82eb0ae8c373
fetched_at: '2026-06-28T22:44:37.555042+00:00'
product: protheus
section_id: 10299632459799
source: central-protheus
title: RH - Linha Protheus - Meu RH - Quando uma requisição de transferência é gerada
  pelo Gestor, qual a data que ela é efetivada no Protheus
type: support-article
updated_at: '2025-07-29T12:06:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23086625406999-RH-Linha-Protheus-Meu-RH-Quando-uma-requisi%C3%A7%C3%A3o-de-transfer%C3%AAncia-%C3%A9-gerada-pelo-Gestor-qual-a-data-que-ela-%C3%A9-efetivada-no-Protheus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23086650903191) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Quando uma requisição de transferência é gerada pelo Gestor, qual a data que ela é efetivada no Protheus  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – Todas as versões  
  
**Solução**Quando o Gestor solicitar uma requisição de transferência, a algum de seus subordinados, **a data do dia da gravação, será gerada no pedido.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23086650906775)  
  
Rotina para o RH atender a solicitação - **TCFA040**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23086650918039)  
  
Nota-se que, a **data do pedido é 23/04/2024** porém a **data que o RH irá atender, será 24/04/2024.**  
  
Com isso, ao efetivar a transferência, **a data que será gravada na SRE**, ou seja, no histórico do funcionário, será a **data base do Protheus, no caso, 24/04/2024.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23086650923927)  
Requisição atendida:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23086650929175)  
  
Histórico de Transferência (tabela SRE)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23086650933527)  
  
Se for solicitado que o RH atenda, nesse caso, **na mesma data da solicitação do Gestor**, será necessário **retroagir a data base do Protheus** para gravação do dia anterior.  
  
**Saiba Mais:  
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[CLIQUE AQUI para acessar a documentação de referência do MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**
