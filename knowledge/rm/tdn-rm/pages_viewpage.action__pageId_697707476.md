---
content_hash: d4b3f6c8411667e9dd820e76bd1e9ad30508708cd7d139315998f9223e1395bc
fetched_at: '2026-06-29T00:11:21.595198+00:00'
page_id: '697707476'
product: rm
source: tdn-rm
title: Fop - Fórmulas / Funções - E
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=697707476
version: 17
---

**EMEMBROCIPA**

Esta variável retorna se o funcionário é membro da CIPA e recebe uma data como parâmetro.

Se a coligada não tem integração com o TOTVS Gestão de Pessoas, a função irá verificar se o campo 'Membro da CIPA' no cadastro de Funcionários está marcado ou não e ignora a data que foi passada como parâmetro. Se a coligada tem integração com o TOTVS Gestão de Pessoas, o sistema irá verificar se o funcionário foi ou é membro da CIPA de acordo com a data informada no parâmetro da fórmula.

Sintaxe: EMEMBROCIPA ('DATA’)  
Tipo de Retorno:   0 ou 1  
  
**Exemplo:**

Coligada sem integração com TOTVS Gestão de Pessoas  
EMEMBROCIPA ('01/02/2022')

Retorno da função será 0 (zero) caso o parâmetro em Cadastros Funcionários / Dados da Cipa esteja desmarcado

Retorno da função será 1 (um) caso o parâmetro em Cadastros Funcionários / Dados da Cipa esteja marcado

Coligada com integração com TOTVS Gestão de Pessoas  
EMEMBROCIPA ('01/02/2022')

Retorno da função será 0 (zero) caso nesta data o funcionário não era membro da Comissão da CIPA registrada em TOTVS Gestão de Pessoas / Cadastros / Comissões da CIPA

Retorno da função será 1 (um) caso nesta data o funcionário membro da Comissão da CIPA registrada em TOTVS Gestão de Pessoas / Cadastros / Comissões da CIPA

**EP**

Retorna o valor de eventos programados.

Sintaxe: EP ( STRING )      
Tipo de Retorno: VALOR

**Exemplo:**

No anexo do cadastro de funcionários tem um evento programado de código 9999 com o valor de R$1.000,00

EP (‘9999’)

Retorna R$1.000,00

**EPROFES**  
Retorna se um funcionário é professor no TOTVS Educacional.

Sintaxe: EPROFES ('CHAPA')  
Tipo de Retorno:  
S: É professor  
N: Não é professor  
  
**Observação**  
Esta função de fórmula funciona se houver integração com o TOTVS Educacional e serão verificados os seguintes itens no TOTVS Educacional:

* Se o salário é processado através do TOTVS Folha de Pagamento, configurado no parametrizador
* Se a função do funcionário no TOTVS Folha de Pagamento é a mesma definida do TOTVS Educacional
* Se o professor cadastrado está vinculado a uma chapa de funcionário do TOTVS Folha de Pagamento

**Exemplo:**   
EPROFES ('00001')   
Onde '00001' é a chapa do funcionário professor então retorna ‘S’

EPROFES ('00002')

Onde '00002' é a chapa do funcionário administrativo então retorna ‘N’

**ESCREVELOG**

Escreve uma mensagem no Log  
Sintaxe: ESCREVELOG ( STRING )  
Mais informações em [ESCREVELOG](https://tdn.totvs.com.br/pages/viewpage.action?pageId=381051703#Fun%C3%A7%C3%B5esGlobais-ESCREVELOG)

**EVENTOCORRENTE**

Código do Evento Corrente – código do evento que está sendo calculado no momento da execução do processo.  
Se esta função for executada fora do cálculo do envelope o retorno será sempre em branco**.**

Sintaxe: EVENTOCORRENTE   
Tipo de Retorno: STRING

**Exemplo:**

Supondo que o usuário queira descontar a pensão sobre a 1ª parcela do 13º salário nas férias por fórmula.

Crie a fórmula para o cálculo de pensão sobre 1ª parcela de 13º salário pago nas férias, como por exemplo assim:

SE EVENTOCORRENTE  = '9120' E PROCESSO = 'FERIAS'

ENTAO /\*13O SALARIO NAS FERIAS\*/  
    VFER('0038') \* 0.10  
SENAO  
    500  
FIMSE

Informe a fórmula no evento do código do EVENTOCORRENTE, no caso do exemplo é o 9120.

No anexo Adicionais de Férias informe o evento, no caso do exemplo é o 9120.

Ao calcular as férias será demonstrado da seguinte forma:

              Calculando evento: 9120 - PENSÃO 13º SALÁRIO POR FÓMRULA

              Código de Cálculo 0 - Prioridade 81

                     Execução da fórmula EVENTOCO

                     Processando variável EVENTOCORRENTE

                        Código do Evento Corrente: 9120

                     Processando variável PROCESSO

                        Processo que está sendo executado no momento: FERIAS

                     Processando variável VFER

                        Valor do evento 0038: 6.522,75

                     Valor retornado pela fórmula EVENTOCO: 652,28

                     Valor do evento: 652,28

**Observação:** A demonstração acima é considerando dados fictícios do exemplo. Atente-se para a prioridade de cálculo desse evento ser maior que a prioridade do evento que será calculado o valor como no nosso exemplo o evento ‘9120’ tem prioridade maior que o evento ‘0038’.

**EVTPROGCORRENTE**

Evento Programado Corrente - Função auxiliar para a função de fórmula TABEVTPROG

Quando a fórmula TABEVTPROG (Veja [Funções de Fórmula T](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718252)) for utilizada no processo de Alteração Global de Eventos Programados deverá informar neste campo a variável EVTPROGCORRENTE ('ID').

Sintaxe: EVTPROGCORRENTE ( STRING )      
Tipo de Retorno: INDEFINIDO

**Exemplo:**

Supondo que esteja no processo de Alteração Global de Eventos Programados utilizando a fórmula:

TABEVTPROG('VALOR','S','9999', EVTPROGCORRENTE ('ID')) \* 1.1  
Serão alterados todos os valores dos eventos programados com código 9999 encontrado no anexo do funcionário.

**EVTSALCORRENTE**

Evento Salarial Corrente - Retorna o evento de salário composto que está sendo correntemente processado pela alteração salarial global.

**Atenção:**

Esta função só poderá ser usada para alteração global salarial nas fórmulas de aumento salarial.

Desta forma, seu uso deve ser restrito à função de Alteração Global de Salários. Na tela de cadastramento de fórmulas possui uma opção que indica se a fórmula será automaticamente testada ao ser gravada: "Testa fórmula automaticamente ao salvar", esta opção fica por padrão marcada. Ao colocar em uma fórmula a expressão ValSalComp (EvtSalCorrente) com esta opção marcada, a rotina tentará processá-la e, como não pode obter um retorno correto de EvtSalCorrente já que este processamento está sendo realizado fora da rotina de Alteração Global de Salários, emite a mensagem de que o parâmetro da função deve ser uma string. Assim sendo, basta cadastrar e/ou alterar as fórmulas que utilizem a função EvtSalCorrente com a opção de testar automaticamente a fórmula ao salvar desmarcada.

Sintaxe: EVTSALCORRENTE

Tipo de Retorno: STRING

**Exemplo:**

VALSALCOMP (EVTSALCORRENTE) \* 1.10

Onde a fórmula retornará um aumento salarial de 10% para cada salário composto encontrado no cadastro ao processar a alteração salarial global para salário composto.

**EXECSQL**

Executa uma Consulta SQL - Executa uma consulta SQL previamente cadastrada

Sintaxe: EXECSQL ( STRING )

Tipo de Retorno: VALOR

Mais informações em [EXECSQL](https://tdn.totvs.com.br/pages/viewpage.action?pageId=381051703#Fun%C3%A7%C3%B5esGlobais-EXECSQL)

**EXISTECF**

Existe código fixo - Testa a existência de código fixo no anexo do funcionário.

EXISTECF (STRING)

VALOR

**Exemplo:**

EXISTECF (‘0034’)

Se o evento estiver cadastrado como código fixo, a função retornará 1. Caso contrário, retornará 0.

**EXISTEEP**

Existe evento programado - Testa a existência de evento programado no anexo do funcionário.

EXISTEEP (STRING)

VALOR

**Exemplo:**

EXISTEEP (‘9999’)

Se o evento estiver cadastrado como evento programado, a função retornará 1. Caso contrário, retornará 0.
