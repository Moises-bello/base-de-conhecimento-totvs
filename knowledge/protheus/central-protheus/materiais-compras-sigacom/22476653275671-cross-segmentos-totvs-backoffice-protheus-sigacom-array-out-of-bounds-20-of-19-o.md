---
article_id: 22476653275671
category: Materiais - Compras (SIGACOM)
content_hash: 3a360fc6ddbab0666367eb96884afff4c4c740aa7348a30ea859dce6f2e37c7c
fetched_at: '2026-06-28T22:41:14.217578+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - array out of bounds
  [20] of [19] on MATA116A(MATA116.PRW) '
type: support-article
updated_at: '2024-04-08T13:40:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22476653275671-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-array-out-of-bounds-20-of-19-on-MATA116A-MATA116-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22476627751063) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao acessar a Rotina de Conhecimento de Frete MATA116 e tentar incluir um CTE o sistema gera o errorlog abaixo.

array out of bounds [20] of [19] on MATA116A(MATA116.PRW) 15/02/2024 10:32:39 line : 206  
**Ambiente**Protheus – Compras – A partir da versão 12.1.2210  
  
**Causa**Esse errorlog foi gerado na linha do fonte onde é verificado o Novo Parâmetro da Natureza de Rendimento , muito possivelmente não haja esse parâmetro na sua rotina. O Parâmetro de Natureza de Rendimento é um facilitador que foi desenvolvido para que possamos digitar uma Natureza de Rendimento e ela seja aplicada para todos os itens do CTE, sem que tenhamos que preencher item a item.

![](https://tdn.totvs.com/download/attachments/811698811/image-2023-12-13_14-28-20.png?version=1&modificationDate=1702488500300&api=v2)

**Solução**

Por gentileza, aplique o pacote abaixo e valide inicialmente em ambiente teste/homologação onde a mesma situação esteja ocorrendo. Observação: Sempre realize backup antes de qualquer atualização.  
<https://suporte.totvs.com/portal/p/10098/download?e=1134090> para a release 2210  
<https://tdn.totvs.com/pages/viewpage.action?pageId=811701840>

<https://tdn.totvs.com/display/PROT/PCOM14007+-+MATA116+-+REINF+-+Facilitador+de+Preenchimento+da+Natureza+de+Rendimento>

Se mesmo após a aplicação dos pacotes acima o parâmetro não aparecer na tela da rotina, por favor desabilite todos os pontos de entrada seguindo criteriosamente as três formas da documentação abaixo. Isso é necessário pois, por exemplo, o ponto MT116TEL é executado no início da função MATA116A (Digitacao de Conhecimento de Frete) e substitui a tela padrão de parâmetros. O ponto de entrada deve colocar todos os parâmetros no array “aParametros”, e poderá exibi-los, opcionalmente, numa tela customizada . Dessa forma, se o parâmetro da natureza de rendimento não estiver nesse PE não vai aparecer.

MT116TEL - Insere parâmetros ao Array  
link: <http://tdn.totvs.com.br/pages/releaseview.action?pageId=6085459>

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
