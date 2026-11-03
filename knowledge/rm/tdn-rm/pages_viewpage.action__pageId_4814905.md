---
content_hash: 60b945c46f8610b567ec50cbf50ed841d9d6e6d579e47a5c5e0e031391bd37cb
fetched_at: '2026-06-29T00:10:19.484669+00:00'
page_id: '4814905'
product: rm
source: tdn-rm
title: Gerar pagamento a Maior ou a Menor gerando Conta Corrente e utilizar ou não
  o processo de “Aproveitar valores de conta corrente”
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4814905
version: 54
---

---

Os pagamentos a Maior do que os valores devidos ou a Menor ocorrem com frequência e merecem um tratamento diferenciado, abaixo será explicado como parametrizar e qual o processo seguir:

Parametrização do sistemaVrOpcional/IntegraçãoValores Opcionais / IntegraçãoValores Opcionais / Integração

Acesse a documentação  nas abas:

* Fin - Vlrs. Opcionais/Integração 1/3 (configuração dos campos Pagamento a maior e menor)
* Fin - Vlrs. Opcionais/Integração 2/3 (configuração dos campos Acrescenta e Desconta)

Cadastro do Cliente/FornecedorCadastro do Cliente/Fornecedor

* ***Acesse: Cadastros / Clientes Fornecedores***  
  Verifique se o “Cliente/ Fornecedores” está habilitado tanto para pagar como para receber.

Selecione o “Cliente /Fornecedor” ( Editar em seguida )

Marque a opção em Classificação: “AMBOS”

Débitos e Créditos na Conta Corrente

A conta corrente do aluno pode ser atualizada de duas maneiras:

1. No momento da baixa, registrando pagamentos efetuados a Maior ou a Menor que os valores devidos
2. Na inclusão ou exclusão de Bolsas Retroativas aplicadas em lançamentos já baixados.

Aqui vamos explicar o processo do momento da baixa de um lançamento.

Como exemplo iremos mostrar a atualização da Conta Corrente do aluno através de uma das atividades muito frequentes nas instituições de ensino que é o recebimento a maior ou a menor que o valor devido.

- Lançamento da parcela 1 do aluno já gerado e incluído no TOTVS Gestão Financeira no valor de R$ 1.000,00.

- No TOTVS Gestão Financeira, vamos realizar a baixa deste lançamento onde o aluno vai pagar um valor Menor que o valor devido, somente R$ 800,00:

Selecione o lançamento do aluno no valor de R$ 1.000,00 (**=1**) e execute a baixa.   
No campo **‘Pgto a Menor’**parametrizado anteriormente, indique R$ 200,00 (**=2**), assim o sistema atualizará automaticamente o ‘Valor da Baixa’ para R$ 800,00 (**=3**).

- O valor pago a menor foi lançando automaticamente como **Débito** na Conta Corrente do aluno.   
Para visualizar, acesse no TOTVS Educacional o cadastro do Aluno | Anexos | Conta Corrente do aluno:

**O processo acima é o mesmo para pagamento a maior, mas no pagamento a maior na conta corrente do aluno teremos uma linha com Natureza : C****(crédito)**

No *TOTVS Gestão Financeira* ao cancelar a baixa do lançamento que teve pagamento a maior ou menor e consequentemente a originou a conta corrente, o sistema irá remover da conta corrente os valores relativos ao débito ou crédito correspondente a baixa. 

Como aproveitar os valores da Conta Corrente do AlunoGerando a próxima mensalidade:

Como o sistema já foi parametrizado anteriormente para permitir aproveitar os valores na próxima mensalidade, vamos então gerar a próxima mensalidade do aluno.

- Acesse o cadastro do aluno, selecione a próxima parcela e execute o processo ‘Gerar lançamentos’:

- Ao final do processo, acesse novamente o TOTVS Gestão Financeira e edite o lançamento gerado.   
Na aba Valores | Adicionais. Repare que o valor da Conta Corrente foi aproveitado no lançamento financeiro através do campo ‘Acrescenta no líquido’ parametrizado anteriormente.

**Observação:**

Como neste exemplo o aluno possuía um **Débito** na Conta Corrente proveniente de um pagamento efetuado a menor, ao gerar a próxima parcela, este valor foi aproveitado através do campo ‘Acrescenta no líquido’, aumentado assim o valor líquido do lançamento.   
Se o valor da Conta Corrente do aluno fosse um **Crédito**, referente, por exemplo, a um pagamento feito a maior, ao gerar a próxima parcela, este valor seria aproveitado através do campo ‘Desconta no líquido’, diminuindo assim o valor líquido do lançamento.

- Repare que a Conta Corrente do aluno foi automaticamente atualizada, sendo retirado o valor aproveitado no lançamento financeiro anterior. Neste caso a Conta Corrente do aluno voltou a ficar zerada.

- Se a baixa deste lançamento financeiro for realizada, repare que o valor ‘Original’ continua os mesmos R$ 1.000,00 (**=1**) e que o campo ‘Acrescenta no líquido’ é preenchido automaticamente com o valor aproveitado da Conta Corrrente R$ 200,00 (**=2**), refletindo automaticamete no  ‘Valor da Baixa’ deste lançamento = R$ 1.200,00 (**=3**).

Os lançamentos do TOTVS Gestão Financeiro:

* Que aproveitaram valores da conta corrente do aluno e foram excluídos na ordem do aproveitamento, o sistema voltara para a conta corrente o valor com uma linha correspondendo ao crédito ou debito.  
  Ex: Conta Corrente de R$400, aproveitou crédito na parcela 2 á 5 de R$100, ao excluir os lançamentos na seguinte ordem parcela 5,4 e 3 o sistema manterá uma linha correspondente ao saldo no valor de R$300.
* Que aproveitaram a conta corrente do aluno e foram excluídos independente da ordem do aproveitamento (de forma aleatória), o sistema voltara para a conta corrente uma linha separada correspondendo ao crédito ou debito referente ao cancelamento de cada lançamento.  
  Ex: Conta Corrente de R$400, aproveitou crédito na parcela 2 á 5 de R$100, ao excluir os lançamentos da parcela 2 e 3 o sistema criará duas linhas na conta corrente no valor de R$100 cada.
Executando o processo ‘Aproveitar valores em conta corrente’ 

Considere para o exemplo a seguir que o aluno possui um **Crédito** na sua Conta Corrente, proveniente de um pagamento anterior, efetuado a maior. O lançamento financeiro era de R$ 1.000,00 mas o aluno pagou R$ 100,00 a mais, ficando então com este valor pago a maior registrado como crédito na sua Conta Corrente.

- Vamos aproveitar o valor existente na Conta Corrente do aluno executando o processo ‘Aproveitar valores em conta corrente’*.*Este processo cria automaticamente lançamentos financeiros com os valores aproveitas.

* Se o valor aproveitado da Conta Corrente for um **Débito**, o sistema incluirá uma nova parcela do contrato do aluno com o seu respectivo lançamento financeiro para o aluno pagar futuramente o seu boleto quitando assim o seu débito.
* Se o valor aproveitado da Conta Corrente for um for um **Crédito**, o sistema não criará vínculo com o contrato do aluno, pois neste caso incluirá somente o lançamento financeiro para pagar ao aluno o valor que este efetuou a maior. Neste caso específico, o responsável financeiro do aluno precisa ser também um ‘Cliente’ para que o sistema consiga incluir um lançamento do tipo a pagar para o aluno.

- Primeiramente certifique-se de que o responsável financeiro do aluno está classificado como **‘Ambos’** indicando estar habilitado tanto para pagar (Cliente) como para receber (Fornecedor). No TOTVS Gestão Financeira, edite o cadastro de cliente/fornecedor e certifique-se.

- Volte ao TOTVS Educacional, acesse o cadastro do Aluno e em Anexo a sua Conta Corrente. Em seguida execute o processo ‘Aproveitar valores em conta corrente’*.*

- No TOTVS Gestão Financeira, o lançamento financeiro do tipo a pagarfoi incluído para o responsável do aluno no valor aproveitado da Conta Corrente R$ 100,00 e, neste caso, este lançamento não possuirá vínculo com nenhum contrato.

- Pronto, no final do processo, o sistema irá atualizar automaticamente a Conta Corrente do aluno, excluindo o valor aproveitado. Neste caso a Conta Corrente do aluno voltou a ficar zerada.

 Veja Também

---
