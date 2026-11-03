---
article_id: 360027252794
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: ffad73ccb6ba4a118d6579969197968082f1f08261c92b14d8868ce5ec8ae77b
fetched_at: '2026-06-28T22:42:40.983070+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Cálculo realizado para a requisição
  do material no apontamento
type: support-article
updated_at: '2024-09-23T20:59:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027252794-Manufatura-Linha-Protheus-SIGAPCP-C%C3%A1lculo-realizado-para-a-requisi%C3%A7%C3%A3o-do-material-no-apontamento
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:45 min**  
**Dúvida**Ao realizar o apontamento de produção qual o cálculo realizado para determinar a quantidade a ser requisitada?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**No apontamento de produção o Sistema verifica o conteúdo do parâmetro **MV\_BXPROP - Proporcionaliza baixa automática de M.Prima** , se o conteúdo desse parâmetro for **S**, a rotina de apontamento verifica quanto a quantidade apontada corresponde da quantidade da **OP - Ordem de Produção**, dividindo a quantidade do apontamento pela quantidade da **OP** e multiplica esse índice pela quantidade de cada empenho, fazendo assim a requisição proporcional dos itens empenhados.  
  
**Exemplo:**Uma **OP** de 80 unidades, com o empenho de 120 unidades do material MP01.  
Com o parâmetro **MV\_BXPROP** igual a **S** o Sistema realiza o procedimento abaixo:  
Ao realizar o apontamento de 40 unidades, o Sistema vai verificar quanto as 40 peças que estão sendo apontadas correspondem ao total da **OP** e fará a requisição do material empenhado nesta proporção.  
  
Então o cálculo será:  
**(Quantidade apontada/Total da Ordem de Produção)\*Quantidade do empenho**  
**(40/80)\*120 = 60**  
  
Portanto requisitará 60 unidades do material MP01.  
  
Já se o parâmetro **MV\_BXPROP** tiver o conteúdo **N**, toda a requisição será feita no primeiro apontamento, portanto, requisitará as 120 unidades do material MP01.
