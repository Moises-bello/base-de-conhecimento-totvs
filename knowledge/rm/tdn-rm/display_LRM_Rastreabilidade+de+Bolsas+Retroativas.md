---
content_hash: d8a8e9124a2dbf911c2df2e0bdbf4bde003d1fe7d64c3b9375f5baff8d40e8d9
fetched_at: '2026-06-29T00:09:38.088131+00:00'
page_id: '425918465'
product: rm
source: tdn-rm
title: Rastreabilidade de Bolsas Retroativas
type: documentation
url: https://tdn.totvs.com/display/LRM/Rastreabilidade+de+Bolsas+Retroativas
version: 3
---

---

A inclusão ou exclusão de Bolsa Retroativa assim como o aproveitamento de crédito ou débito gerado pela Bolsa Retroativa, cria registros que nos possibilitam rastrear suas origens ou destinos (aproveitamentos). A 'Rastreabilidade' de Bolsa Retroativa consiste na exibição destas informações e são apresentadas como Anexos de Contrato, Parcela e Bolsa, que poderão ser acessadas nos caminhos:  
 *(Contrato | Anexos | Rastreabilidade de bolsa retroativa)*  
 *(Contrato | Parcela | Anexos | Rastreabilidade de bolsa retroativa)*  
 *(Contrato | Bolsa    | Anexos | Rastreabilidade de bolsa retroativa)*

A Rastreabilidade acessada a partir do Contrato mostrará todas as movimentações geradas pela Bolsa Retroativa para este Contrato, incluindo as movimentações de todas as suas Bolsas e Parcelas.

A Rastreabilidade acessada a partir da Parcela somente mostrará as movimentações geradas para esta Parcela.

A Rastreabilidade acessada a partir da Bolsa somente mostrará as movimentações geradas para esta Bolsa no Contrato.

− A inclusão de uma Bolsa Retroativa em parcelas cujos lançamentos financeiros estiverem 'Baixados' criará registros de rastreabilidade com o Tipo 'Origem' e Classificação 'Crédito'.  
− A inclusão de uma Bolsa Retroativa em parcelas cujos lançamentos financeiros estiverem 'Em aberto' criará registros de rastreabilidade tanto do Tipo 'Origem' indicando a inclusão da Bolsa Retroativa quanto do Tipo 'Destino' indicando o aproveitamento dos créditos originados nestas parcelas com a criação de 'Vínculos'.  
− O processo de *'Desfazer'* a inclusão de Bolsa Retroativa, excluirá todos os registros de rastreabilidade gerados para a bolsa em questão.  
− A 'Exclusão' de uma Bolsa Retroativa, criará registros com o Tipo 'Origem' e Classificação 'Débito'.  
− A geração do lançamento financeiro de uma parcela que aproveite valores dos créditos de Bolsa Retroativa, criará registros com o Tipo 'Destino' e Classificação 'Crédito'.

Cada um destes registros criados para demonstrar a *'Rastreabilidade'* de Bolsas Retroativas, além de informar cada Tipo de movimentação realizada, informa também o valor correspondente à cada movimentação realizada, a referência das parcelas e dos lançamentos afetados entre outras informações.
