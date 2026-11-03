---
content_hash: 661402432f48352ac2c91aec4d6205fe9dccf6441e529d061c7fcb3e00230607
fetched_at: '2026-06-29T00:09:28.052944+00:00'
page_id: '423938637'
product: rm
source: tdn-rm
title: Apuração Virtual 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938637
version: 4
---

Empresas tributadas pelo Lucro Real anual com levantamento de balanço de suspensão /redução, Lucro Real ou Lucro Presumido com apuração trimestral, a ECF exige que as informações do Bloco K sejam enviadas com os valores de Ativo e Passivo fechados, ou seja, as contas de resultado deverão ser encerradas para que o resultado contábil de cada período seja apurado. Porém, de acordo com a (Lei nº 6.404/1976, art. 175 e Lei nº 9.430/1996, arts. 1º e 2º) para fins societários, o exercício social permanece com duração de 1 ano (encerrando-se, normalmente, em 31 de dezembro). Embora caiba à pessoa jurídica adotar procedimentos que permitam ao Fisco constatar a veracidade do resultado apurado, a elaboração de balanços/balancetes mensais/trimestrais não representa obrigatoriedade de encerramento das Contas de Resultado a cada mês/trimestre.

Quando o encerramento contábil é realizado anualmente, o processo de geração da ECF não consegue identificar os encerramentos trimestrais e consequentemente serão apresentadas inconsistências na validação do arquivo da ECF no PVA.

Para atender a necessidade citada acima, disponibilizamos o módulo de Apuração Virtual que possibilita criar estruturas de apuração contábil que poderão ser utilizadas na ECF ou como apoio gerencial. A Apuração Virtual calcula virtualmente o valor do resultado conforme as regras de cálculo, sem gerar nenhum impacto na escrituração contábil, ou seja, não gera nenhum lançamento contábil, apenas processa o valor.

Este recurso esta disponível no módulo Totvs Gestão Contábil, através do menu Escrituração Contábil|Apuração|Apuração Virtual.

**Parametrização Apuração Virtual**

1. Descrição da Apuração Virtual
2. Conta de apuração do Lucro: Conta que receberá o saldo pela apuração quando o saldo apurado for Credor. Serão listadas somente as contas analíticas e com a natureza da conta para emissão do SPED igual a "Patrimônio Liquido".
3. Conta de apuração do Prejuízo: Conta que receberá o saldo pela apuração quando o saldo apurado for Devedor. Serão listadas somente as contas analíticas e com a natureza da conta para emissão do SPED igual a "Patrimônio Liquido".
4. Utilizar na ECF?: Indica se a estrutura será utilizada na ECF ou como apoio gerencial. O sistema não permitirá a alteração na estrutura, após execução da ECF (Quando a opção "Utilizar na ECF" for igual a SIM)
5. Regras de cálculo da Apuração: Estabelece como o sistema vai processar o resultado contábil.

Para a regra de cálculo será  permitido utilizar somente contas que o campo "Natureza da conta para emissão do SPED "for igual a "Resultado".

Conta: Conta a ser considerada no calculo.

Tipo: Identifica a informação da conta que será utilizada no cálculo ( Crédito, Débito ou Movimentação ).

Operação: Indica se o valor processado pela regra de cálculo será subtraído ou somado.

O usuário poderá informar quantas regras de cálculo julgar necessário para apuração do lucro ou prejuízo do exercício.

**Exemplo:**

|  |  |  |  |
| --- | --- | --- | --- |
| **Conta** | **Tipo informação** | **Valor** | **Operação** |
| 3.1 | Movimentação | 4000 | Soma |
| 4.2 | Movimentação | 2000 | Subtrai |
| 5 | Movimentação | 500 | Subtrai |
|  | **Saldo** | **1500** | **Saldo < 0 = Credor**  **Saldo > 0 = Devedor** |

*Observação: para o cálculo não serão considerados os lançamentos que contenha histórico que seja de fechamento*

Neste exemplo o valor do saldo da conta de lucro ou prejuízo será de R$ 1500,00 devedor. Sendo assim, o sistema irá gerar um item no registro K155 (Detalhes dos Saldos Contábeis) com a conta de lucro ou prejuízo parametrizada na apuração virtual com o valor do saldo processado.

**Detalhamento de Execução da Apuração**

Demonstra o detalhamento do cálculo realizado pela execução da Apuração Virtual conforme o período da apuração. Neste detalhamento será possível identificar o  valor processado, natureza do saldo, usuário que executou, data de execução , além de demonstrar a memória de cálculo (valores processados para cada conta).

Observações:

* Detalhamentos originados da ECF não poderão ser apagados, a cada geração da ECF o sistema atualiza os dados dos detalhamentos, que representará as informações que foram enviadas para a ECF através do registro K155. O Campo Filial só será preenchido somente quando a apuração for executada para uma única filial, no caso da execução ser realizada para mais de uma Filial o campo ficará vazio.

**Simulação / Execução da Apuração Virtual**

Processa efetivamente as informações do estrutura da Apuração Virtual.

* Simulação: o processo será executado e não será gravado nenhum detalhamento de apuração, somente será listada no log a simulação. Para Apuração Virtual do tipo "ECF" será permitida a execução do processo somente como "Simulação", pois quem executa efetivamente a Apuração Virtual é a geração da ECF.
* Execução da Apuração: o processo será executado e sistema irá grava o detalhamento que será disponibilizado como anexo ou no cadastro da apuração virtual (aba: Detalhamento da Execução da Apuração). Esta opção ficará disponível somente quando o tipo da Apuração Virtual não for ECF, neste caso o usuário poderá executar a apuração para fins gerenciais.

**Validação:**

Caso exista algum lançamento manual realizado para conta de lucro ou prejuízo , ou seja, lançamento que o próprio usuário criou para a conta em função de alguma apuração manual ou ajuste, o mesmo será somado ao valor processado pela apuração virtual e será apresentada a mensagem abaixo no LOG

Registro K155 |Apuração Virtual |Identificamos que existe movimentação que não é de encerramento para a conta "{0}" no período de {1} á {2}, e a ECF Contábil esta parametrizada para executar a apuração virtual, esta situação poderá resulta em advertências no PVA.

Normalmente esta situação ocorre quando o usuário executa a apuração do lucro/prejuízo manualmente e realiza o lançamento, sugerimos que este processo seja realizado automaticamente pelo processo de Transferência de Grupos Contábeis ou que o lançamento realizado manualmente seja identificado por um histórico de fechamento

Se a solução for identificar o lançamento com um histórico de fechamento que não foi utilizado no encerramento anual, será necessário desmarcar a opção "Utilizar transferência de grupos contábeis para identificar o(s) encerramento(s)".
