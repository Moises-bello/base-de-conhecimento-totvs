---
content_hash: be6cfb70e10e5feba2a3244b552c130712db8f2d631f4215c28a90f17dc8a338
fetched_at: '2026-06-29T00:09:32.332264+00:00'
page_id: '425458826'
product: rm
source: tdn-rm
title: Associação Desconto por Antecipação a Bolsa Condicional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458826
version: 11
---

---

Com desconto por antecipação da bolsa você tem a possibilidade de informar se a bolsa condicional será ou não aplicada de acordo com a data limite dos itens de desconto.

O cadastro do desconto por antecipação associado à bolsa estará disponível no anexo "Desconto por antecipação da bolsa" no cadastro de bolsa.

 (Importante lembrar de habilitar a permissão no perfil do usuário)

IMPORTANTE

* Só será permitido cadastrar os descontos por antecipação da bolsa caso o parâmetro do Educacional 'Mantém fórmula default para valor opcional / integração de bolsas condicionais' esteja marcado e a bolsa seja do tipo condicional.
* Não será possível alterar o tipo de bolsa para incondicional caso essa bolsa já tenha descontos por antecipação cadastrados.
* O menu "Desconto por antecipação da bolsa" disponível no anexo do cadastro de bolsa somente ficará habilitado se a bolsa selecionada for uma bolsa condicional.
Regras para processamento

Caso tenha um item de desconto por antecipação associado à bolsa condicional, significa que o aluno somente terá direito à bolsa se o pagamento for realizado até a data limite do item do desconto por antecipação vinculado à bolsa, ou seja, a bolsa passa a ser condicionada ao pagamento do desconto por antecipação estipulado.

Exemplo:

Bolsa "Você Merece": 10%, vinculada ao desconto por antecipação "Pagamento até o dia 10, ganha 10%".

O Aluno somente irá ganhar os 10% de bolsa se realizar o pagamento até o dia 10 do vencimento do boleto.

Observação: Caso não tenha nenhum desconto por antecipação associado à bolsa, a regra de processamento da bolsa não é alterada, ou seja, ao processar o valor da bolsa o sistema não realizará nenhuma validação com relação ao desconto por antecipação.

Em quais processos o sistema aplicará a regra?

Geração de Lançamento

Durante a geração de lançamento, caso seja identificado descontos por antecipação para o aluno, o mesmo será processado já identificando os valores de pagamento para cada vencimento do desconto por antecipação (dependendo da parametrização do sistema o valor da bolsa vai considerar o valor do desconto por antecipação, mas em alguns casos pode ser necessário ter disponível o valor sem desconto por antecipação e recuperar através da fórmula ValorBolsaLan o valor desconsiderando o desconto por antecipação). O valor para pagamento apresentado já considerará a perda da bolsa, caso a bolsa esteja condicionada a um desconto por antecipação.

Simulação de Parcela

Na visão de parcela é possível selecionar a parcela e realizar a simulação dos valores, neste momento o sistema também apresentará colunas demonstrando os valores para pagamento conforme cada vencimento do desconto por antecipação. O valor para pagamento apresentado já considerará a perda da bolsa, caso a bolsa esteja condicionada a um desconto por antecipação.

Baixa de Lançamento

Para que o sistema considere a perda da bolsa que está condicionada a um desconto por antecipação, durante a baixa do lançamento será necessário utilizar na fórmula uma função de fórmula que calcule o valor da bolsa considerando a data da baixa, pois somente durante a baixa do lançamento é que saberemos qual é o desconto por antecipação ao qual o aluno terá direito e se o mesmo dará direito à bolsa.

Importante:

Para utilizar o recurso de perda da bolsa condicionada conforme o desconto por antecipação, o valor da bolsa condicional deverá sempre ser processado por fórmula .

*Veja no documento  "**Fórmula Valor de Bolsa Condicional Conforme Desconto Por Antecipação**"* *c**omo utilizar este recurso.*

Bolsa Condicionada ao Desconto por AntecipaçãoBolsa Condicionada ao Desconto por AntecipaçãoProcesso de associação de desconto por antecipação à bolsas condicionais

Este processo visa facilitar a associação de descontos por antecipação à bolsas condicionais a fim de que essas bolsas sejam válidas até um vencimento específico conforme descrito previamente no tópico **Bolsa Condicionada ao Desconto por Antecipação**.

O mesmo se encontrará em processos da visão de bolsas conforme abaixo:

Somente bolsas "**CONDICIONAIS**" poderão ser selecionadas para processamento, caso seja selecionada alguma bolsa "**INCONDICIONAL**", o sistema exibirá uma mensagem para o usuário e não permitirá prosseguir conforme abaixo:

O processo também só estará visível, se o parâmetro de sistema "***Mantem fórmula default para valor opcional / integração de bolsas condicionais***" estiver marcado

São três status possíveis para os registros de associação do processo:

1. **Banco de dados**: Indica que a associação entre o desconto por antecipação e a bolsa já existe no banco de dados. Esse registro permanecerá inalterado na execução do processo.
2. **Inclusão**: Indica que a associação entre o desconto por antecipação e a bolsa será incluída no banco de dados após execução do processo. Somente terão esse status, os registros que não existiam no banco de dados. Caso a associação do desconto já exista para alguma bolsa, o sistema não adicionará nenhuma linha na grid de associação.
3. **Exclusão**: Indica que a associação entre o desconto por antecipação e a bolsa será excluída no banco de dados após execução do processo. Somente os registros carregados do banco de dados terão esse status. Caso o usuário tenha incluído no processo uma associação que não existia previamente no banco de dados, o respectivo registro será excluído da grid de associações.

Segue abaixo a tela do processo:

Após execução do processo, o sistema exibirá um log com todas as inclusões e exclusões feitas conforme abaixo:

 Veja Também

---
