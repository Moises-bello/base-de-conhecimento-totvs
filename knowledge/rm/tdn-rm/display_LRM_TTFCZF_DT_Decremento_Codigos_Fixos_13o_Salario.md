---
content_hash: 414ce196e36b8dc7beaa0802684e2bac208d1369de022565a41ffe58d29fb2ea
fetched_at: '2026-06-29T00:06:08.005725+00:00'
page_id: '201741991'
product: rm
source: tdn-rm
title: TTFCZF_DT_Decremento_Codigos_Fixos_13o_Salario
type: documentation
url: https://tdn.totvs.com/display/LRM/TTFCZF_DT_Decremento_Codigos_Fixos_13o_Salario
version: 1
---

# DECREMENTO NÚMERO VEZES CÓDIGOS FIXOS DE 13o.SALÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Décimo Terceiro* |
| **Situação/Requisito:** | *No processo de lançamento da 2a.parcela do 13o.salário, quando é selecionada a opção para lançar códigos fixos, o número de vezes no cadastro é decrementado a cada lançamento.* |
| **Solução/Implementação:** | *O número de vezes do cadastro de Códigos Fixos só pode ser decrementado uma vez.*  *Deverá ser verificado se o evento já existe no envelope, e no caso afirmativo, não efetuar o decremento.*  *Assim, se o lançamento da 2a.parcela for refeito, o número de vezes permanecerá inalterado..* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTFCZF* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.7* |
