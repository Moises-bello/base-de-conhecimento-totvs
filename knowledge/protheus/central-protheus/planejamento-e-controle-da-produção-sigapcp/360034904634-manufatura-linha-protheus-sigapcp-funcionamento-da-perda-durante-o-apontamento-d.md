---
article_id: 360034904634
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 34fd05c2ea3e7beb50c647063bfacbb19a2793857d35029f78dde21f71d50c8c
fetched_at: '2026-06-28T22:42:43.313643+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Funcionamento da perda durante o apontamento
  de produção
type: support-article
updated_at: '2021-07-26T17:52:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034904634-Manufatura-Linha-Protheus-SIGAPCP-Funcionamento-da-perda-durante-o-apontamento-de-produ%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura:**00:02:30 min****Dúvida**Como funciona a **Perda** durante o apontamento de produção através das rotinas **MATA250 - Produção Simples** e **MATA681 - Produção MOD2**?  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Parâmetro **MV\_PERDINF - Identifica se a quantidade de perda informada nos informativa (.T.) ou se compõe o saldo da OP (.F.)** igual a **.T.**O Sistema considera que a quantidade de perda, informada nos apontamentos de produção, é apenas **informativa**. Neste caso, a baixa de empenhos é realizada proporcionalmente à quantidade produzida, desconsiderando a quantidade perdida.  
  
**Exemplo**  
Considere a seguinte estrutura:  
**PA**  
|\_\_**MP** - Quantidade 1  
  
Abertura de uma **OP** **- Ordem de produção** de 50 unidades para o produto **PA - Produto Acabado**.  
O Sistema gera um empenho proporcional, também de 50 unidades, para o produto **MP - Matéria-prima**.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045400714/mceclip1.png)

Para os casos em que a quantidade perdida não é contabilizada no saldo da ordem de produção, mas que é necessário efetuar requisições referentes à perda, utilize os seguintes procedimentos:

1. Configure o parâmetro **MV\_DIGIPER -** **Classificação da perda** com conteúdo igual a **S**;
2. No **MATA685 - Apontamento Perda**, configure a pergunta **F12 - Requisita produto origem?** com **Sim**;

Com esta configuração, sempre que realizado apontamento de produção e informada a perda, uma tela é aberta para inclusão dos itens perdidos.  
  
Se o parâmetro **MV\_DIGIPER** tiver conteúdo igual a **N**, a tela para inclusão dos itens perdidos não será apresentada e os apontamentos de perda devem ser informados através da rotina **MATA685.**Parâmetro **MV\_PERDINF** igual a **.F.**No Sistema a quantidade de perda informada nos apontamentos de produção é considerada na composição do saldo da ordem de produção. Neste caso, a baixa de empenhos é realizada proporcionalmente à quantidade produzida mais a quantidade de perda informada.  
  
**Exemplo**  
Considere a seguinte estrutura:  
**PA**  
|\_\_**MP** - Quantidade 1  
  
Abertura de uma **OP** de 50 unidades para o produto **PA**.  
O Sistema gera um empenho proporcional, também de 50 unidades, para o produto **MP**.

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046260573/mceclip0.png)**

Neste caso, a quantidade perdida é considerada na composição do saldo da ordem de produção e as requisições de matéria-prima foram proporcionais à quantidade produzida mais a quantidade perdida, sem necessidade de intervenção manual.  
  
Para os casos em que for necessária a realização de classificação quanto à perda, utilize os seguintes procedimentos:

1. Configure o parâmetro **MV\_DIGIPER** com conteúdo igual a **S**;
2. No **MATA685** configure a pergunta **F12 - Requisita produto origem?** com **Não**, pois as requisições de perda são geradas automaticamente.
