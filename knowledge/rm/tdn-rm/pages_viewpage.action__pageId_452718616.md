---
content_hash: 0f592996d6161c20e9819ab9957c078d741860816fbdf1231338c2a69f003d82
fetched_at: '2026-06-29T00:10:00.896030+00:00'
page_id: '452718616'
product: rm
source: tdn-rm
title: Lançamento de Diferença Salarial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718616
version: 28
---

## **CONTEÚDO**

1. **V****isão Geral**
2. **Exemplo de utilização**
3. **Tela Lançamento de Diferença Salarial**
   1. **Principais Campos e Parâmetros**
4. **Tabelas utilizada**

**01. VISÃO GERAL**

Neste módulo será possível realizar o lançamento da diferença salarial para um funcionário ou para todos de uma única vez.

DICA

01 - Quando há cálculo de diferença salarial e for preciso alterar valores que afetarão no recálculo dessa diferença orientamos  cancelar todo o movimento e calcular a diferença novamente. O motivo é que quando recalcula um mesmo evento sobrepõe, mas se tiver um evento que no novo recálculo não deveria ser lançado, o sistema não exclui.

02 - Veja também informação importante no cálculo de diferença quando envolve Pensão Alimentícia no TDN [Código de Cálculo 13 - Pensão Alimentícia Judicial](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718801).

Importante

Quando houver necessidade de calcular diferença salarial e no período de tempo selecionado existe cálculo de retificação, o processo verificará se na tabela PFRETIFICACAOPERIODO existe o campo PERIODOORIGEMRETIF. Se este campo não existir será apresentada a mensagem: 

É necessário rodar o Atualizador para criar o campo "Período Original" na pasta "Retificações pagas no período" da ficha financeira do funcionário.

## **02. EXEMPLO DE UTILIZAÇÃO**

11Aumentos a Desconsiderar

Marcando os Motivos de Aumento Salarial a desconsiderar, o valor do aumento, será subtraído do valor do salário atual caso o aumento tenha sido na competência que se está referenciando a diferença.

**Exemplo:**

Funcionário tem o salario de R$1000,00 e recebeu um aumento no dia 01/04/2019 pelo motivo "Dissidio Coletivo" passando seu salário para R$1050,00.

No dia 18/04/2019, recebeu um novo aumento pelo motivo "Mérito", passando seu salário para R$1550,00.

Ao fazer a diferença salarial para o mês 04, marcando para desconsiderar aumentos do motivo "Dissidio Coletivo", o sistema pegará o salário mais recente que é R$1550,00 e subtrairá o valor do aumento desconsiderado (R$50,00 do aumento do dia 01/04/2019). O valor do salário considerado para cálculo será R$1500,00.

2Verbas Geradas por Diferença

Quando a empresa possuir funcionários com múltiplos vínculos e estando os parâmetros abaixo marcados em: Configurações | Parametrizador | Folha de Pagamento | Folha Normal | Geral:

* Calcula IRRF/INSS de Múltiplos Vínculos SEM chapa centralizadora
* Calcula INSS conforme eSocial

Ao processar um cálculo retroativo de diferença salarial, de funcionários com mais de um vínculo, o sistema irá armazenar a diferença das bases tributadas para 1ª, 2ª, 3ª e 4ª faixas na tabela PFVERBASDIS na competência de origem do cálculo. Essas bases podem ser acessadas em: Cadastro de Funcionários | Ficha Financeira | Verbas Geradas por Diferença.

**Exemplo:**

**Tabela de INSS Vigente;**

**SALÁRIO-DE-CONTRIBUIÇÃO (R$)             ALÍQUOTA PROGRESSIVA**

Até 1.045,00                                                               7,5%

De 1.045,01 até 2.089,60                                             9%

De 2.089,61 até 3.134,40                                             12 %

De 3.134,41 até 6.101,06                                                14% 

**Competência 04/2020**

* **Coligada 1**

           Salário : R$ 600,00 

              **Envelope :**

                    Horas Normais :   R$ 600,00

                     Base tributada de INSS Folha 1 faixa :  600,00  - 7,5 %

                     INSS : 45,00  - 7,5 %

* **Coligada 2**

             Salário : R$ 400,00       

              **Envelope:**

                     Horas Normais :  400,00

                     Base tributada de INSS Folha 1 faixa :  400,00  - 7,5 %

                     INSS : 30,00  - 7,5 %

**Competência 05/2020**

* **Coligada 1**

**Reajuste Salarial**

                Novo Salário: R$ 1.000,00   ( Diferença Salarial: R$ 400,00)

**Calculando a diferença salarial retroativo a competência 4**

**Diferenças do período Mês/Ano: 4/2020 Período: 1**----------------------------------------------------------------------------  
Código    Descrição                                                    Ref.            Hora                  Valor  
0001  HORAS NORMAIS                                           220,00         220:00               400,00 P  
0003  INSS                                                                 9,00            000:00               35,32 D  
0238  BASE DE FGTS DIF SALARIAL 0,00                                      000:00               400,00 B  
s428  BASE TRIBUTADA DE INSS FOLHA 1º FAIXA    7,50             000:00              45,00 B  
S429  BASE TRIBUTADA DE INSS FOLHA 2º FAIXA    9,00            000:00               355,00 B

Ao calcular a diferença salarial, o sistema soma as bases de todos os vínculos do funcionário na competência do cálculo da diferença (04/2020), verifica o que já foi tributado e em qual faixa o valor da diferença se enquadra.. As faixas referentes reajuste salarial são Armazenadas na tabela PFVERBASDIS.  

No exemplo, as bases de INSS foram somadas nas duas coligadas verificando-se que já havia sido tributado R$ 1.000,00 na 1ª faixa, restando o valor de R$ 45,00 para tributar nessa faixa. O valor restante R$ 355,00 foi tributado na segunda faixa, resultando em um desconto de INSS de R$ 35,32 sendo: 

* 7,5% de R$ 45,00 = 3,37
* 9% de R$ 355,00 = 31,95

**Valor Armazenado na Ficha Financeira - Verbas Geradas por Diferença (PFVERBASDIS):**

* Horas normais      R$ 400,00
* INSS                      R$ 35,32 (7,5% de R$ 45,00 + 9% de R$ 355,00)
* Base tributada de INSS folha 1 faixa  -  R$ 45,00
* Base Tributada de INSS  folha 2 faixa -  R$ 355,00

**Envelope de diferença acumulada até o período Mês/Ano: 5/2020 Período: 1****----------------------------------------------------------------------------**Código     Descrição                                   Ref.               Hora                    Valor  
0244  DIFERENCA SALARIAL - DISSÍDIO   220,00           220:00                 400,00 P  
0237  INSS DIFERENCA SALARIAL             9,00              000:00                 35,32 D  
0238  BASE DE FGTS DIF SALARIAL           0,00              000:00                 400,00 B

3Atestado retroativo CC 145

Ao realizar o cálculo da diferença salarial quando há inclusão de atestado médico de forma retroativa, haverá o recálculo dos eventos de CC2 - DIAS TRABALHADOS e CC145 - ATESTADO MÉDICO, verificando a soma dos códigos de cálculo e subtraindo o valor calculado no envelope original.

Cenário com dados fictícios:

Envelope Original lançado evento CC2 -  30 DIAS TRABALHADOS 3192,80

Inclusão de 5 dias de atestado no histórico de afastamento retroativo

Aumento salarial para 4500

Envelope recalculado evento CC2 - 25 DIAS TRABALHADOS 3750 + evento CC145 - 5 DIAS DE ATESTADO 750 

Somando os dois eventos seria 4500 SALÁRIO COM AUMENTO

DIFERENÇA ENTRE 4500 - 3192,80 = 1307,20

No lançamento da diferença será considerado da seguinte forma:

CC2 - 25 DIAS TRABALHADOS 557,20 

CC145 - 5 DIAS DE ATESTADO 750 

Totalizando 1307,20 que é o valor da diferença calculada acima

Para conhecimento

Quando houver situação em que o funcionário tem um atestado retroativo para somar a outro atestado já lançado será feito um cálculo proporcional para os dias trabalhados e para os dias de atestado. 

**Por exemplo:**

No envelope original tem 2 dias de atestado e foram lançados 13 dias retroativos.

Então tem que calcular a diferença de 15 dias e o sistema tem que simular quanto seria o valor de 15 dias no salário anterior, para saber o valor da diferença.

No envelope original para o cálculo dos 2 dias teríamos:

                     Total de dias de atestado médico: 2

                     Valor do Atestado Médico: 2.102,49 / 30 \* 2 = 140,166000

                     Valor do evento: 140,17

Ou seja, deu 140.166 que foi arredondado para 140.17

Fazendo a conta inversa para encontrar o salário considerando que 2 dias são 140.17

140.17 / 2 \* 30 = 2102.55

Logo depois a conta para encontrar os 15 dias seria

2102,55 / 30 \* 15 = 1051,275

4Atestado retroativo CC 445Atenção

Quando houver lançamento retroativo de atestado médico com  CC445 - ATESTADO MÉDICO SEM INCIDÊNCIA EM INSS deverá primeiro existir o cálculo da retificação para ser feita a restituição do INSS descontado no envelope original antes do cálculo da diferença salarial.

Ao realizar o cálculo da diferença salarial retroativa quando há inclusão de atestado médico sem incidência de INSS de forma retroativa, haverá o recálculo dos eventos de CC2 - DIAS TRABALHADOS e CC445 - ATESTADO MÉDICO SEM INCIDÊNCIA EM INSS, verificando a soma dos códigos de cálculo e a subtração do valor calculado do valor original.

Cenário com dados fictícios:

Primeiro deve existir o cálculo da retificação para ser feita a restituição do INSS descontado no envelope original

Envelope Original lançado evento CC2 -  30 DIAS TRABALHADOS 4905

Inclusão de 5 dias de atestado no histórico de afastamento retroativo

Aumento salarial para 5905

Envelope recalculado evento CC2 - 25 DIAS TRABALHADOS 4920,83 + evento CC145 - 5 DIAS DE ATESTADO 984,17 

Somando os dois eventos seria 5905 SALÁRIO COM AUMENTO

DIFERENÇA ENTRE 5905 - 4905 = 1000

No lançamento da diferença será considerado da seguinte forma:

CC2 - 25 DIAS TRABALHADOS 833,33 

CC145 - 5 DIAS DE ATESTADO 166,67

Totalizando 1000 que é o valor da diferença calculada acima

## **03.** **TELA Lançamento de Diferença Salarial**

**Principais Campos e Parâmetros**

|  |  |
| --- | --- |
| **Campo** | **Descrição** |
| Seleção de funcionários | Selecione os funcionários |
| Quebra de Seção | Seleção a quebra de seção |
| Dissídio/Convenção/Acordo Coletivo | Selecione de acordo com o tipo de cálculo que precisa ser feito. |
| Competência Inicial | Informar a partir de qual competência será calculada a diferença salarial |
| Competência Final | Informar até qual competência será calculada a diferença salarial |
| Aumentos a Desconsiderar | Marcando os Motivos de Aumento Salarial a desconsiderar, o valor do aumento, será subtraído do valor do salário atual caso o aumento tenha sido na competência que se está referenciando a diferença. |
| Dados do dissídio/convenção/acordo coletivo | Quando selecionada a opção Dissídio "Sim", será   habilitado o lookup "Dados do dissídio/convenção/Acordo coletivo". O cadastro pode ser feito através deste lookup ou através menu eSocial| [Dissídio/Acordo Coletivo](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718631)   Atenção Este campo é utilizado para o eSocial leiaute [S-1200 - Remuneração do Trabalhador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719412). |

## **04. TABELAS UTILIZADAS**

* PFPERFF
* PFFINANC
* PFVERBASDIS
