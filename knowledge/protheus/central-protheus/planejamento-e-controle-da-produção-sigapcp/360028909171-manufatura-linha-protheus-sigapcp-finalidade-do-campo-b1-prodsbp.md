---
article_id: 360028909171
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 07ab0b8e2a7bb2535fd150f061ebfc22a09441c829260390affe6b9fd72dc6b7
fetched_at: '2026-06-28T22:42:43.246874+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Finalidade do campo B1_PRODSBP
type: support-article
updated_at: '2022-09-01T12:35:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028909171-Manufatura-Linha-Protheus-SIGAPCP-Finalidade-do-campo-B1-PRODSBP
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:01:15 min****Dúvida**Qual a finalidade do campo **B1\_PRODSBP**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
O campo **B1\_PRODSBP**  **- Atende Nec?**tem por finalidade determinar se um produto deve ser adquirido **Comprando** ou **Produzindo** quando for **subproduto** de uma outra estrutura, além do campo **B1\_PRODSBP**, no campo **B1\_ESTORI - Estr. Origem** deve ser informado o produto que deve ser produzido para obter-se o produto em questão.  
  
Nos demais casos, o Sistema define se gerará uma **Solicitação de Compra** ou uma **Ordem de Produção** com base na existência ou não de estrutura.  
  
**Exemplo**  
Tendo as duas estruturas

![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360029638531/Capturar.PNG)

O sinal negativo da estrutura acima, indica um subproduto.

![Capturar2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360029646732/Capturar2.PNG)

Ao produzir o **PA01**, informamos que vamos consumir o produto **MP01** e vamos obter também o **MP02**, que vem a ser um **subproduto**.  
  
Na estrutura do **PA02** precisamos dos materiais **MP03** e **MP02**. O **MP02** podemos obter de duas formas, comprando ou produzindo o **PA01**, neste caso utiliza-se o campo **B1\_PRODSBP** para determinar como dever ser obtido o **MP02**, se **produzindo** o **PA01** ou se **comprando**.  
  
**Saiba mais**  
Caso tenha dúvidas sobre a funcionalidade do subproduto acesse o artigo: [Manufatura - Linha Protheus - SIGAPCP - Como cadastrar e qual é o funcionamento do subproduto.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025539152)
