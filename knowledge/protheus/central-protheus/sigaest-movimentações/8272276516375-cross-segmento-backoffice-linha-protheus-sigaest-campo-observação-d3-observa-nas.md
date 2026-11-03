---
article_id: 8272276516375
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 04937590f4964fdc6da038fd9c43c9fa5f2c2fb02fe65e72afea2a1021d12697
fetched_at: '2026-06-28T22:38:54.344756+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - campo Observação
  (D3_OBSERVA) nas rotinas MATA261, MATA241 e MATA250 '
type: support-article
updated_at: '2022-08-19T11:57:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8272276516375-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-campo-Observa%C3%A7%C3%A3o-D3-OBSERVA-nas-rotinas-MATA261-MATA241-e-MATA250
---

**Dúvida**As rotinas de *Transferência entre Armazéns (MATA261)* e *Apontamento de Produção (MATA250)* não apresentam o campo de **Observação (D3\_OBSERVA)**, somente é apresentado esse campo na rotina de *Movimentações Internas (MATA241)*.

Preciso incluir um campo de Observação nessas rotinas, como proceder?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Estoque Custos - Todas as versões  
  
**Solução**

***Para a rotina MATA261:***

A rotina MATA261 passa por um array com os campos que devem ser apresentados em tela, para essa rotina é necessário criação de campo de Usuário e utilizar os Pontos de Entrada MA261CPO e M261D3O. 

Veja documentação dos Pontos de Entrada nos link abaixo:

*MA261CPO - Inclui campos para digitação em array*  
[*https://tdn.totvs.com/pages/releaseview.action?pageId=6087616*](https://tdn.totvs.com/pages/releaseview.action?pageId=6087616)

*M261D3O: Atualiza campos ou arquivos na gravação.*  
[*https://tdn.totvs.com/pages/releaseview.action?pageId=236602023*](https://tdn.totvs.com/pages/releaseview.action?pageId=236602023)

***Para a rotina MATA250***

A rotina MATA250 passa por um array com os campos que devem ser apresentados em tela, para apresentar o campo D3\_OBSERVA deve customizar com o ponto de entrada A250FLDS. 

Veja documentação do Ponto de Entrada no link abaixo:

*[https://tdn.totvs.com/display/PROT/A250FLDS](https://tdn.totvs.com/display/public/PROT/A250FLDS)*

Saiba Mais:  
[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
