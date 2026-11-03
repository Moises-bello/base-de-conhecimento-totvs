---
content_hash: ab2586a82b13c1fc112260c4e1bf31190faff89a5fd85a3d4d881f9026ce5c49
fetched_at: '2026-07-02T19:24:24.051901+00:00'
page_id: '454835698'
product: protheus
source: tdn-tec
title: Correção - TBtnBmp apresenta falha na transparência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=454835698
version: 1
---

Correção - TBtnBmp apresenta falha na transparência

|  |  |
| --- | --- |
| Situação | Ao utilizar componentes do tipo botão TBtnBmp usando como container uma Janela sem cor de fundo atribuído, o botão apresenta um pequeno quadrado branco de 10 x 10 pixels no canto superior esquerdo do botão. Esse comportamento fica evidente se algum outro componente com cor diferente de branco for posicionado atrás dos botões. |
| Ocorrência | O componente TBtnBmp tenta simular uma transparência obtendo a textura de fundo da Janela e aplicando tal textura em seu background. Em alguns casos ocorre que a textura não é aplicada corretamente e não preenche a totalidade do fundo do botão. |
| Correção | A aplicação de texturas como background do botão TBtnBmp foi removida pois nos testes realizados a falta dela não impactou na transparência. |
| Informações adicionais | * Referente ao chamado: PP-577 * Referente à ocorrência: ITEC-407 * Disponível em builds iguais ou superiores a 7.00.170117A - 17.3.0.5\_RC7 |
