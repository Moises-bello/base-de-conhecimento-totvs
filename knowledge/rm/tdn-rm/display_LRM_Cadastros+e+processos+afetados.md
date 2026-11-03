---
content_hash: bca1c35607ddea05b5015915a92ae2ab8d98aa4d31698a9d997ff5fefe7ecd64
fetched_at: '2026-06-29T00:09:33.915766+00:00'
page_id: '425459081'
product: rm
source: tdn-rm
title: Cadastros e processos afetados
type: documentation
url: https://tdn.totvs.com/display/LRM/Cadastros+e+processos+afetados
version: 5
---

---

**- Processo de aproveitamento de valores em conta corrente**

O valor de crédito ou débito retroativo gerado no contrato, aba 'Valores créditos/débitos gerados', não será alterado após execução do processo de aproveitamento de valores em conta corrente.  
  
**- Baixa de lançamentos**

A baixa de lançamentos de devolução originados pela inclusão de uma bolsa retroativa atualizará o respectivo saldo retroativo pendente do contrato, aba 'Valores créditos/débitos gerados' no cadastro do contrato do aluno e também da bolsa no contrato.  
  
**- Simulação de valores na visão de parcelas do contrato**

A simulação de valores deverá levar em consideração o parâmetro de forma de aproveitamento do crédito ('*Aplicar devolução nas próximas parcelas'* ou '*Dividir devolução pela quantidade de parcelas restantes*') para saber o valor da devolução a ser utilizado no cálculo do valor líquido da parcela, se esta não possuir lançamento gerado. Se a parcela possuir algum lançamento gerado, a simulação de valores somente exibirá um valor de crédito retroativo caso o lançamento gerado por essa parcela tenha aproveitado algum valor.

Caso a forma de aproveitamento do crédito seja '*Devolver em espécie'* ou a forma de utilização do crédito esteja definida como *"Utilizar a movimentação em Conta Corrente",* o valor do crédito será desconsiderado.

A coluna **"*Valor Crédito Retroativo*"** da Grid, somente, será exibida se a forma de utilização do crédito for *Criar Devolução*.  
  
**-** **Processo de Vínculos de lançamentos**

A remoção de Vínculo originado de créditos do processo de inclusão/exclusão de bolsa retroativa, feita diretamente dentro do TOTVS Gestão Financeira, excluirá o crédito do lançamento e atualizará o valor pendente para o crédito de bolsa retroativa do contrato, aba 'Valores créditos/débitos gerados'.  
  
**-** **Processo de exclusão/cancelamento de bolsas**

Não será permitida a exclusão/cancelamento de bolsas retroativas através do processo **"Excluir/Cancelar bolsas"**na visão de contratos, bolsas do contrato e no assistente financeiro.

O processo validará se a bolsa a ser excluída é retroativa e não permitirá a execução do mesmo.

Será exibida uma mensagem informando que bolsas retroativas só podem ser excluídas através do processo de Inclusão/Exclusão de bolsas retroativas.   
  
**-** **Cadastro de lançamentos**

Não será permitido alterar os valores do lançamento a pagar de devolução, gerado pela inclusão da bolsa retroativa.

- **Cadastro de bolsas do contrato**

Os campos, no cadastro de bolsas do contrato, ficarão desabilitados para edição quando a bolsa incluída for *retroativa*.

Não será permitida a exclusão de uma bolsa quando ela for classificada como *retroativa*.
