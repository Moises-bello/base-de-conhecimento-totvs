---
content_hash: 1c98249f3362715c4cd1874ba2d80d80ba028918465378166be0ab455c657fab
fetched_at: '2026-06-29T00:09:55.612770+00:00'
page_id: '448595736'
product: rm
source: tdn-rm
title: 4518701 FINANCEIRO01-10219 DT  Geração do boleto com Valor Liquido Parcial
  mas o desconto por antecipação não deve ser considerando no valor do boleto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=448595736
version: 1
---

# CALCULO VALOR LIQUIDO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão Financeira |
| **Função:** | Calculo valor liquido |
| **Situação/Requisito:** | Atualmente o cliente trabalha com o Desconto por Antecipação, ou seja, o lançamento/boleto tem um desconto até o vencimento. O cliente parametrizou seu convenio para gerar o Valor Código de Barras considerando o valor Liquido Parcial. Ao gerar o boleto o valor do boleto está considerando o tal desconto, mesmo que ele seja somente até o vencimento. Neste caso o cliente precisa trabalhar com a geração do boleto nesta forma(Valor Liquido Parcial) mas o desconto por antecipação não deve ser considerando no valor do boleto, visto que é somente até o vencimento este desconto é aplicado, neste caso gostaria que o sistema aplicasse o mesmo comportamento dos valores opcionais que descontam até o vencimento. |
| **Solução/Implementação:** | Otimização no serviço do calculo do valor liquido para não considerar o desconto por antecipação no calculo do valor liquido parcial. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | 12.1.21, 12.1.22, 12.1.23 |
