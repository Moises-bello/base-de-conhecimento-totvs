---
content_hash: 38eb4e2196f73d625574f21e80a9e06f58bd17a04c9d258adcf05c700182b124
fetched_at: '2026-06-29T00:11:09.992470+00:00'
page_id: '640891623'
product: rm
source: tdn-rm
title: Lançamento de Honorários médicos na conta do paciente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=640891623
version: 28
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Validações**
3. **Cálculo do valor**
4. **Fator de acomodação**
5. **Lançamento de taxas automáticas vinculadas ao porte anestésico**
6. **Lançamento da hora extra**
7. **Multiplicador de via de acesso**
8. **Multiplicador da função do médico**
9. **Lançamento do gabarito**
   1. Parâmetros do gabarito
   2. Passos para associar um gabarito na conta
10. **Divisão de cobrança por percentual**
11. **Divisão cobrança por valor**
12. **Diferença de honorário para gastos particulares**
13. **Regras dentro/fora da conta**
14. **Tabelas utilizadas**

sumarioVisão Geral

## **01. VISÃO GERAL**

A aba de honorários serve para lançar todos os procedimentos executados por um prestador e por sua equipe. São procedimentos do tipo consultas, visitas, cirurgias, etc.

Validações

## **02. VALIDAÇÕES**

* **Validações do Atendimento**
  + Deverá estar com o status diferente de "Cancelado"

* **Validações da Parcial**
  + Deverá estar com o status diferente de "Faturada", "Liberada" ou "Cancelada".
  + Não poderá ter nota fiscal emitida e o convênio particular.
* **Validações do Centro de custo**
  + Obrigatório se o parâmetro "Centro de Custo obrigatório nos lançamentos?" estiver marcado em Parâmetros Gerais > Faturamento II
  + Paciente interno
    - * Obrigatório se o parâmetro "Centro de Custo vinculado ao leito sem possibilidade de alteração" estiver marcado
  + Paciente Externo
    - Obrigatório se o parâmetro "Centro de Custo vinculado a Estação de Trabalho sem possibilidade de alteração" estiver marcado
* **Validações do item do Honorário**
  + Item estornado não pode ser alterado
  + O item especial não pode ser alterado. Deve ser estornado e incluído novamente pela página Especial.
  + O valor do honorário incluído deverá ser maior que 0.
  + Não é permitido lançamento honorário para o prestador principal fora da conta.
  + O código da **Função do Médico** é obrigatório.
* **Validações do campo Data Realização**
  + A data da taxa deve estar dentro do período da parcial
  + A data/hora de início não pode ser maior que a data/hora final
  + A hora não pode ser igual 24:00. Deve-se lançar com a hora igual a 00:00 e acrescentar 1 dia na data
* **Validações da Compatibilidade**
  + Compatibilidade do procedimento VS sexo. Caso esteja configurado na tabela de procedimentos, o sexo do paciente no procedimento, o sistema verifica a parametrização
  + Compatibilidade do procedimento com o tipo de paciente (interno, externo). O sistema critica internação com lançamento de procedimentos na faixa de consulta em consultório ou consulta em pronto socorro.
Cálculo do valor

## **03. CÁLCULO DO VALOR**

Para o cálculo do valor do honorário, o sistema segue a seguinte ordem de prioridade nas tabelas a consultar:

1. Tabelas de preços diferenciadas (se existir para o plano)
   1. Tabela especial
   2. Tabela de procedimentos
2. Tabelas das condições contratuais
   1. Tabela especial
   2. Tabela de procedimentos

Se não encontrar o item na tabela especial, o sistema procura na tabela de procedimento.

As tabelas podem ser tanto em reais, quanto em quantidade de CH. Para o uso de CH é necessário configurar no cadastro de Condições Financeiras, os valores de CH.

Para tabela CBHPM é utilizado o valor do porte, que também pode ser configurado nas Condições Financeiras.

**Valor do procedimento = (valor da tabela) \* (fator acomodação) \* (1 + (percentual hora extra / 100)) \* (percentual função/100) \* (percentual via/100)**

Fator de acomodação

## **04. FATOR DE ACOMODAÇÃO**

O fator de acomodação é o que está relacionado à classe do leito utilizado pelo paciente. Caso não esteja num leito, o fator considerado terá o valor 1.

Na classe de acomodação é associado o tipo de acomodação (apartamento, enfermaria, etc).

No cadastro das Condições Contratuais, existe o anexo Acomodação. É nele que se definem os fatores de multiplicação.

Lançamento de taxas automáticas vinculadas ao porte anestésico

## **05. LANÇAMENTO DE TAXAS AUTOMÁTICAS VINCULADAS AO PORTE ANESTÉSICO**

Ao salvar um honorário, o sistema verifica se existe taxas para serem lançadas na conta de acordo com as validações abaixo:

* Parâmetro das condições contratuais estiver marcado
* Quando existir o porte anestésico do procedimento incluído
* Somente na inclusão do honorário
* Função do médico for Cirurgião
* Tipo do procedimento for Principal
Lançamento da hora extra

## **06. LANÇAMENTO DA HORA EXTRA**

O sistema verifica se o atendimento é de urgência/emergência, se a data de lançamento está dentro das regras de hora extra e aplicará o percentual, de acordo com as parametrizações no cadastro de "Padrão de Faturamento e Codificação"

Multiplicador de via de acesso

## **07. MULTIPLICADOR DE VIA DE ACESSO**

O fator a ser utilizado depende dos valores configuras no Padrão de faturamento e codificação utilizados nas Condições Contratuais e a via informada no lançamento

Multiplicador da função do médico

## **08. MULTIPLICADOR DA FUNÇÃO DO MÉDICO**

Já o fator multiplicador para a função do médico, também deve ser definida no Padrão de faturamento e codificação utilizados nas Condições Contratuais.

Somente para as funções abaixo é que possuem valores parametrizáveis. As demais funções são 100% em cima do valor do procedimento

* Primeiro auxiliar
* Outros auxiliares (2º, 3º, 4º)
* Auxiliar de anestesista
* Instrumentador

Lançamento do gabarito

## **09. LANÇAMENTO DO GABARITO**

Ao salvar um honorário, o sistema verifica se existe um gabarito em aberto para a conta e se comporta de acordo com os parâmetros gerais:

* Se os parâmetros estiverem marcados: "Verificar existência de Gabarito ao incluir novo item - Elaboração de Contas"  e "Ação ao identificar Gabarito: Questionar inclusão no pacote". O sistema pede a confirmação do usuário para incluir o honorário no pacote. Ou seja, o honorário será cobrada além do pacote.
* Se os parâmetros estiverem marcados: "Verificar existência de Gabarito ao incluir novo item - Elaboração de Contas"  e "Ação ao identificar Gabarito: Incluir automaticamente no pacote". O sistema não pede confirmação e incluirá o honorário automaticamente junto com o pacote.
* Caso não tenha um gabarito em aberto, o honorário não será cobrada

Parâmetros do gabarito

### **09.01** **PARÂMETROS DO GABARITO**

 Passos para associar um gabarito na conta

### **09.02** PASSOS PARA ASSOCIAR UM GABARITO NA CONTA

Divisão de cobrança por percentual

## **10.** **DIVISÃO DE COBRANÇA POR PERCENTUAL**

Existem duas forma de realizar o lançamento da divisão de cobrança, uma por valor e outra em percentuais.

**Divisão de cobrança por valor**

A divisão de cobrança por valor é configurado no cadastro do procedimento através da tela **Tabela de Procedimentos e Serviços.**

O lançamento de divisão de cobrança por valor, corresponde a realizar o lançamento para a instituição e outro para o prestador, esses valores podem ser realizado em **CH** ou em **Reais**.

* **Em CH**, devem ser utilizadas as colunas **Valor Operacional CH** e **Honorário CH**.
* **Em Reais**, devem ser preenchidas as colunas **Custo Operacional R$** e **Honorário R$**.

Abaixo exemplo de procedimento utilizando CHs.

Importante! O sistema não permite que sejam misturados valores CH ou em Reais.

**Divisão de cobrança por percentual**

Para realizar a divisão por percentual, é necessário realizar o cadastro da regra de cada prestador e os respectivos honorários e percentual que cada um receberá.

O percentual restante da divisão será lançado em nome do prestador principal da unidade de faturamento.

**Lançamento da Divisão de Cobrança**

* Incluir um novo registro e informar o prestador do lançamento que possui a regra de divisão.
* O campo "Divisão de cobrança" deve ser marcado antes de se incluir o registro. Após a sua inclusão, após salvo o campo não pode ser alterado. Se digitado errado, os lançamentos devem ser estornados.
* Salvar o registro e o sistema irá buscar a regra cadastrada da divisão e irá realizar o segundo lançamento automaticamente.
* Para o prestador executante, o honorário sempre será lançado como fora da conta.

Primeiro lançamento, que deverá ser digitado no sistema.

**Exemplo cadastro do procedimento ou serviço.**

**Exemplo de lançamento da divisão por percentual**

Segundo lançamento que foi gerado após salvar o registro.

Divisão cobrança por valor

## **11.** **DIVISÃO DE COBRANÇA POR VALOR**

Para a divisão de cobrança por valor, é necessário que se informe o campo "Divisão de cobrança" e "Prestador divisão de honorários" estejam preenchidos.

O campo "Divisão de cobrança" deve ser marcado antes de se incluir o registro. Após a sua inclusão, o campo não pode ser alterado.

No campo Prestador deve-se informar o prestador principal  e o prestador da divisão, será o que receberá o valor do honorário.

Ao realizar o lançamento, informe o prestador como sendo aquele que receberá os custos operacionais.

DivisaoCobrancaIPSEMG e IAMSPE

Para esses convênios a regra para obter a tabela DTS é a mesma da regra geral. A diferença está na obtenção dos valores.

Acesse o menu Cadastros | Faturamento | Outros Cadastros | Tabela de procedimentos e serviços.

Filtre pelo código da tabela utilizada pelo convênio e selecione um item de honorários. Em Anexos, selecione a opção "IPSEMG/IAMSPE - Valores".

O sistema seleciona o valor de acordo com a vigência mais atual e o valor unitário de honorário corresponde ao campo Vlr. Total e o valor total corresponderá à quantidade de honorários multiplicado pelo valor unitário.

**Observação** : Para o convênio **IAMSPE**, as configurações da Condição Contratual/Padrão de Faturamento citado acima não são obedecidas para cálculo do percentual de função, %via de acesso, % de acréscimo, etc (como é feito com os demais convênios no sistema).

O **IAMSPE** tem seu próprio cálculo de faturamento.

Para percentual de Função segue:

Cirurgião = 100%

Primeiro Auxiliar = 30%

Demais auxiliares (1,2,3,4) = 20%

**Lançamento Cirurgia Mesma Via – Iamspe**

Deve seguir a seguinte parametrização, acessar a tabela de Padrão de Faturamento e codificação e informar a faixa.

1º Procedimento: SP, SH, SADT = 100%

2º Procedimento:

SH, SADT = 20%

SP = 50%

Exemplo :

**Percentual SP será 50% a partir do segundo procedimento, para todos.**

**VALORES IAMPES – MESMA VIA: percentual SH, SADT conforme tabela**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | CODIGO | SP | SH | SADT | VL TOTAL |
| 1 | 33004080 | 585,0000  100% | 863,8600 100% | 53,7000 100% | 1697,5600 100% |
| 2 | 33005060 | 405,6000  50% =  202,80 | 679,3000  20% =  135,86 | 20,4000  20% =  4,08 | 1249,6000  20% = 342,74 |
| 3 | 42010039 | 175,5000  50% =  87,75 | 113,0600  20% =  22,612 | 4,4800  20% = 0,896 | 390,5400  111,258 |
| 4 | 42704073 | 322,9200  50% = 161,46 | 1113,9800  10% =111,398 | 64,8000  10% = 6,48 | 1646,0000  279,238 |
| 5 | 75500116 | 71,4000  50% = 35,70 | 357,6000  10% =35,76 | 36,7000  10% = 3,67 | 465,7000 |

**Observação: Ao lançar o procedimento na ELABORAÇÃO DA CONTA , tem que estar marcado a opção "Mesma via" caso contrario o calculo não funciona.**

Diferença de honorário para gastos particulares

## **12.** **DIFERENÇA DE HONORÁRIO PARA GASTOS PARTICULARES**

A diferença de honorário ocorre quando o plano do paciente é na acomodação enfermaria e ele é alocado num leito superior. Com isso, os honorários médicos que seriam cobrados em dobro em função do fator de acomodação, são calculados com o fator parametrizado para a enfermaria e o restante é lançado em gastos particulares.

Caso seja informado a tabela de preço para os gastos particulares, o valor lançado será calculado em função dessa tabela. Caso contrario, o preço é o da tabela do convênio.

O fator de acomodação utilizado é o do parâmetro em destaque.

 Regras dentro/fora da conta

## **13.** **REGRA DENTRO/FORA DA CONTA**

* Se no momento da inclusão do Honorário o usuário marcar a opção **Fora da Conta,**verificar o credenciamento do prestador junto ao convênio:
  + Se **Indireto:** gravar a coluna HONORARIOFORA com o valor FALSO
  + Se **Direto**: gravar VERDADEIRO.
* Se no momento da inclusão do Honorário a opção **Fora da Conta** desmarcada, gravar a coluna HONORARIOFORA com o valor FALSO.
* Se existir regra de dentro/fora da conta, este deve prevalecer. Ver cadastro de Regra dentro/fora da conta.

## **07.****TABELAS UTILIZADAS**

* SZATENDHONOARIO
