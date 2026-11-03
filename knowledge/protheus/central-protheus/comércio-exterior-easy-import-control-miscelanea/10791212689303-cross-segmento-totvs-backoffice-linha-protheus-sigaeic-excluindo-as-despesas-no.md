---
article_id: 10791212689303
category: Comércio Exterior - Easy Import Control - Miscelanea
content_hash: 394e80de6a7b2f4c636ab38b65d4ddca392c9b9068c6c70b3614457d30a04a89
fetched_at: '2026-06-28T22:39:42.044812+00:00'
product: protheus
section_id: 1500001549702
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus -SIGAEIC -  Excluindo as despesas
  no sistema, que não consta do arquivo de integração do despachante.
type: support-article
updated_at: '2022-12-08T12:40:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10791212689303-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Excluindo-as-despesas-no-sistema-que-n%C3%A3o-consta-do-arquivo-de-integra%C3%A7%C3%A3o-do-despachante
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Excluindo as despesas no sistema quando estas não consta no arquivo de integração do despachante.  
  
**Ambiente** Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**Na integração das despesas o sistema sempre fará a exclusão das despesas integradas anteriormente para incluir as novas; No caso das despesas do numerário caso ainda não possuam nota serão excluídas para que as despesas constantes no novo arquivo de integração sejam integradas.

Caso haja a necessidade de alteração de fluxo, sugerimos que seja utilizado o Ponto de Entrada **DELDESP**.  
Neste ponto de entrada poderá alterar a variável **lDeletaSWD** para **.F.** assim o sistema não efetuará a exclusão das despesas já integradas em arquivo anterior que não possuam nota.

Ao encontrar uma despesa igual ja constante nas despesas do desembaraço durante a integração, o sistema irá perguntar se deseja sobrepor ou não, ao responder sim, a despesa será alterada para os dados da nova despesa que está sendo integrada, caso responda não, manterá a despesa atual.

**Saiba mais:**[Integração Despachante](https://tdn.totvs.com/pages/releaseview.action?pageId=306860028)[Ponto de entrada DELDESP](https://tdn.totvs.com/pages/viewpage.action?pageId=692557346).
