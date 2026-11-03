---
article_id: 23142667071639
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 857482bcd6164bfe5147e6e4b6f1782eed7ab4c7b715bfdd58829436dd1f0bcf
fetched_at: '2026-06-28T22:42:45.877095+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Requisição dos empenhos no apontamento
  total
type: support-article
updated_at: '2024-04-30T12:02:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23142667071639-Manufatura-Linha-Protheus-SIGAPCP-Requisi%C3%A7%C3%A3o-dos-empenhos-no-apontamento-total
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23142667054871) Tempo aproximado para leitura: **00:00:55 min** **Dúvida**Como se dá a requisição dos materiais empenhados no apontamento total?   
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**Ao realizar um apontamento preenchendo o campo **Parcial/Total** com o conteúdo **Total**, o Sistema avalia os parâmetro **MV\_BXPROP  e MV\_BXSD4TL.**Se o parâmetro **MV\_BXSD4TL** tem o conteúdo **T** ou o parâmetro **MV\_BXPROP** tem o conteúdo **N** o Sistema requisita todo o saldo empenhado.  
Já se o parâmetro **MV\_BXSD4TL** tem o conteúdo **F** e o parâmetro **MV\_BXPROP** tem o conteúdo **S**é realizado o cálculo de proporção da quantidade apontada em relação a quantidade da **OP** e será requisitada essa proporção dos materiais empenhados.  
  
**Exemplo**Considerando uma **OP** de 10 com 10 de um determinado componente empenhado.  
Ao apontar 3 com um apontamento parcial, é requisitado 3 do componente.  
Na sequência é realizado o ajuste de empenho alterando quantidade origem para 15 e o saldo para 12.  
Com o parâmetro **MV\_BXSD4TL** com o conteúdo **T** ou o parâmetro **MV\_BXPROP** igual a **N**, ao realizar o apontamento total de 7 é requisitado o saldo de 12 do componente.  
Já com o parâmetro **MV\_BXPROP** igual a **S** e o parâmetro **MV\_BXSD4TL** com o conteúdo **F** , o Sistema calcula a proporção da quantidade apontada com relação a quantidade da **OP**, e aplica este fator ao item empenhando, (7/10)\*15 = 10,5. Portando 10,5  é a quantidade a requisitada do componente e o empenho é zerado.  
  
**Legenda  
OP - Ordem de produção  
MV\_BXPROP - Proporcionaliza baixa automática da matéria-prima  
MV\_BXSD4TL - Permite baixar 100% da quantidade empenhada quando for produção Total**
