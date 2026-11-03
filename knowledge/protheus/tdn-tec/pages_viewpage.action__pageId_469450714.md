---
content_hash: 488b6f05fb38f3919c2555dea1549a70262a657e19949af6e3cac08b1b999e6e
fetched_at: '2026-07-02T19:24:24.229367+00:00'
page_id: '469450714'
product: protheus
source: tdn-tec
title: Correção - Campo TGet aceita data menor que 01/01/1900
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=469450714
version: 1
---

Correção - Campo TGet aceita data menor que 01/01/1900

|  |  |
| --- | --- |
| Situação | Um campo TGet sem validação de faixa de datas pelo bloco de código bValid permite a gravação de data 31/12/1899 e inferiores quando a data é selecionada através do calendário do campo TGet utilizando o mouse. |
| Ocorrência | Em uma tela de cadastro do ERP, abrir o calendário de um campo TGet do tipo data e somente com o mouse escolher uma data inferior a 01/01/1900 e, logo em seguida sem que este campo perca o foco, clicar em Salvar no formulário. Desta maneira a data inválida é gravada. |
| Correção | Foi aplicada uma correção onde o SmartClient executa a validação do TGet do tipo data assim que o botão Salvar do formulário receber o evento de clique. Neste momento se a data for inferior a 01/01/1900, o conteúdo desse campo é automaticamente excluído antes da gravação. |
| Informações adicionais | * Referente ao chamado: 4268576 * Referente à ocorrência: MTEC-2273 * Disponível em builds iguais ou superiores a 13.2.3.40 |
