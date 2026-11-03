---
content_hash: a80706e1c96fbb4179ef319e50c46ad142ed6701f6cd042c716dd53b1c6bd01f
fetched_at: '2026-06-29T00:10:10.677204+00:00'
page_id: '452719904'
product: rm
source: tdn-rm
title: Histórico de Contribuição Sindical
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719904
version: 2
---

O Histórico de Contribuição Sindical tem o objetivo de registrar cada contribuição sindical (data, valor do desconto e sindicato do empregado), caso não se trate de profissional liberal (neste caso, a contribuição é a cargo do profissional).   
 Podem-se historiar, também, eventuais alterações nos valores de contribuição.   
 Os dados refletirão as informações lançadas no cadastro do funcionário ou diretamente no Histórico de Contribuição Sindical do Funcionário, como Data, Sindicato e Valor (da contribuição).  
    
 **Observação:**  
 A situação do empregado no que se refere à contribuição sindical deve estar definida em   
 Informações para o cálculo:

* **N** - Não descontou
* **J** - Já descontou
* **L** - Liberal

**Contribuição Sindical x Insuficiência de Saldo**  
 Utilizando-se a rotina "Utiliza controle de saldo de verbas" e na movimentação de algum funcionário teve saldo insuficiente para desconto da contribuição sindical, deverá ser marcado o campo "Desconto da contribuição Sindical" para o status de **"Já descontou",** logo após a liberação da competência, evitando assim novos descontos em meses seguintes.  
    
 Este procedimento deve ser efetuado sempre que o Sistema levar para a tabela de Insuficiência de Verbas o desconto da contribuição sindical. Caso contrário, o evento lançado na Insuficiência de verbas será lançado para o movimento em outro evento sem o código de cálculo 12 - Contribuição Sindical e conseqüentemente acontecerá um novo desconto da contribuição sindical, já que o status de desconto permanece "Não descontou".  
    
 **Observação:**  
 A atualização de "Já descontou" é realizada automaticamente somente para os funcionários que tiveram o Código de Cálculo 12 - Contribuição Sindical lançados na movimentação financeira e que obteve suficiência de saldos para efetuar este desconto.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funcionários
