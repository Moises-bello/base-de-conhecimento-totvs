---
article_id: 4402768068887
category: RH - Relatórios
content_hash: c6519e4ba11e8b9630aaa4619ca8b117a008029baf75a0a68c727028d9b7f222
fetched_at: '2026-06-28T22:44:43.582468+00:00'
product: protheus
section_id: 32419371267223
source: central-protheus
title: RH - Linha Protheus - PON - Horas Valorizadas no Espelho de Ponto
type: support-article
updated_at: '2025-10-21T20:59:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402768068887-RH-Linha-Protheus-PON-Horas-Valorizadas-no-Espelho-de-Ponto
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35601865091479) Tempo aproximado para leitura: 00:01:30 min**  
Dúvida**Espelho de Ponto está exibindo coluna e campo de Horas Valorizadas.  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico – A partir da versão 12.1.23  
  
**Solução**Foi liberada uma melhoria no fonte do **Relatório** de **Espelho de Ponto (PONR010)**, onde passa a ser exibida uma **coluna** com o **total de Horas Valorizadas** por dia e ao final, no ***box*** de **Banco de Horas**, é exibido os **campos** com o ****Saldo Anterior Valorizado**** e ****Saldo Atual Valorizado.****  
  
Segue um exemplo prático:  
O funcionário teve estes eventos calculados no período de **21/09 À 20/10.**  
A hora é valorizada de acordo com o cadastro do Evento - aba de Banco de Horas - campo Percentual.  
  
O **evento 102- HORAS EXTRAS BH 70%**, tem valorização, no caso a valorização é de 170%, ou seja, além da hora extra realizada acrescentará mais 70% em cima desta HE.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35791257445783)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35791257446551)  
  
  
Depois de processar o **Cálculo Mensal**, no **Banco de Horas** foi gravado desta forma:  
  
O dia em que houve horas extras, o evento tem valorização em **70%** e foram realizadas 01h à cada dia portanto, o total de **horas valorizadas** em cada dia é de **01h42** (01h HE + 00h42m por conta da valorização de 70% de 01h).  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35791257447831)  
  
Seguindo o  exemplo, segue explicação sobre o **S.Valorizad.(Saldo valorizado):**  
**S.Valorizad.** do dia 19/09 igual à 3h24   
**S.Valorizad.** do dia 22/09 igual à 5h06 (soma-se **S.Valorizad.** anterior-19/09 igual à 3h24 com **H.Valorizad.** atual-22/09 igual à 1h42).   
Aplica-se da mesma forma aos demais lançamentos, linha à linha. O **S.Valorizad.** final ficará neste exemplo com 28h54.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35791257448599)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35791257449623)  
  
Após avaliarmos as movimentações do **Banco de Horas,** vamos ao relatório de **Espelho de Ponto com as Horas Valorizadas do BH,** para emissão teremos as perguntas "**Imprime Banco de Horas**" e "**Imprime Horas Valorizadas?" que deverão ficar com Sim:**![](https://centraldeatendimento.totvs.com/hc/article_attachments/35791257450903)  
  
No espelho de ponto será emitido o período de **21/09 À 20/10** será apresentado a coluna **Hr.Val** Somando cada linha desta coluna será possível chegar no total das **Horas Valorizadas** deste período emitido no espelho que é **25h30.** Ou seja, **Saldo Aterior Valorizado** relacionado ao dia **19/09** com **03h24 + as Horas Valorizadas** no período **25h30** que fica com o **Saldo Atual Valorizado** de **28h54**Veja como ficou no Espelho de Ponto:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35791257451671)  
  
**Saiba mais:**[Espelho de Ponto com Saldo de Banco de Horas Valorizado](https://tdn.totvs.com/display/public/PROT/DT+Viabilizar+o+Saldo+de+Banco+de+Horas+Valorizado+Incluindo+as+Horas+do+Saldo+Anterior+Valorizado+no+Espelho+de+Ponto)[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
