---
content_hash: a9bf88fcada27c906ba8203fdfc0b90c2f45b15cec991c7f704001f6ed59257e
fetched_at: '2026-06-29T00:11:33.842671+00:00'
page_id: '761006653'
product: rm
source: tdn-rm
title: Cálculo do IRRF Simplificado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=761006653
version: 42
---

**CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **O que é necessário**
4. **Exemplo de utilização**
5. **Demais Informações**
6. **Tabelas utilizadas**

## **01. VERSÕES**

false

**A partir dos patches/releases:**

* 12.1.2205.267
* 12.1.2209.222
* 12.1.2302.144
* 12.1.2306
* e Superiores

## **02. VISÃO GERAL**

Com a entrada do IRRF Simplificado, o produto deve fazer o cálculo IRRF, lançado o desconto mais benéfico para o funcionário, ou seja, o de menor valor apurado.

Para isto será necessário executar a comparação do cálculo de IRRF para cada funcionário considerando o cálculo mais benéfico entre a base de cálculo com o valor de dedução simplificada e a base de cálculo com o valor das deduções legais.

**Veja mais informações** [IRRF – Ajuste na Tabela do Imposto de Renda](https://www.totvs.com/blog/fiscal-clientes/irrf-ajuste-na-tabela-do-imposto-de-renda/)

## **03. O QUE É NECESSÁRIO**

Atualização de base de dados para criação do parâmetro “Desconsiderar desconto simplificado do IRRF” em parâmetros do cadastro de Funcionários e das colunas nas tabelas PFPERFF, PFPERFFCOMPL e PFUFERIASRECIBO, indicando se o cálculo daquele período foi considerado a dedução simplificada. Estes campos serão apenas visíveis e não editáveis nos respectivos cadastros.

ATENÇÃO:

Quando as deduções são com valores menores que o limite de dedução simplificado do IRRF cadastrado nos valores fixos será demonstrado no detalhamento do log de cálculo. Caso os valores de deduções sejam maiores e, consequentemente, mais benéficos para o funcionário, não será demonstrado o detalhamento no log de cálculo.

ATENÇÃO - LEMBRETE

**Para a criação dos campos acima é necessário atualização da base de dados.**

**ATENÇÃO:** **Se o campo estiver com a informação NULL é porque no momento de executar o atualizador estava com o cálculo do período da ficha financeira já existente. Somente com a execução do cálculo que esse campo deve ser preenchido de acordo com as regras descritas em Demais Informações desse documento.**

1true1Execução do scriptExecução do script

Para a criação dos campos acima é necessárioexecutar o script através do sistema RM.Atualizador.exe.

**ATENÇÃO**: Após executar o atualizador, é necessário reiniciar novamente o host porque o novo parâmetro possui defensivo que olha o cache de parâmetros.

2Tabelas de Cálculo

A tabela de imposto de renda no cadastro de [Tabelas de Cálculo](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719528) deve estar sempre atualizada. 

3Valores Fixos

Inserir valor fixo no cadastro de [Valores Fixos](https://tdn.totvs.com/display/LRM/Valores+Fixos#1-1) com a finalidade “Valor a deduzir no IRRF simplificado”, com atenção para as datas de vigência.

4Cadastro de Funcionários

Existe a possibilidade de não calcular para funcionários que optarem pelo cálculo integral sem comparar com o valor simplificado marcando o parâmetro “[Desconsiderar desconto simplificado do IRRF](https://tdn.totvs.com/pages/viewpage.action?pageId=452719181)” em parâmetros do cadastro de Funcionários. Essa marcação poderá ser feita pelo processo de Alteração Global de Campos.

5Incidência de EventosATENÇÃO

A marcação do campo Valor Dedutível ou Estorna IRRF é de responsabilidade do usuário, sendo que o valor dedutível refere-se ao que é dedução legal e o valor que estorna é o valor que abate na base do imposto de renda, por exemplo falta.

O cálculo considerará para o cálculo das deduções legais:

* Valor do INSS
* Valor a deduzir por dependentes - de acordo com a parametrização do cadastro de dependentes
* Valor Dedutível - Eventos marcados como Dedutível IRRF em seus respectivos cálculos Folha, 13º salário ou Férias. Observação: Atentem-se para eventos como Pensão Alimentícia, por exemplo, que será considerado de acordo com a marcação da incidência do evento.

Veja abaixo exemplo na marcação dos campos:

**EVENTO MARCADO COMO DEDUTÍVEL DE IRRF**

No log de cálculo será apresentado conforme abaixo:

Valor Dedutível = 822,00 + Valor do INSS: 166,77 = 988,77 DEDUÇÕES LEGAIS QUE É MAIOR QUE 528,00 PREVIAMENTE CADASTRADO NOS VALORES FIXOS

Proventos = 2.055,01 - 988,77 = Base de IRRF: 1.066,24

**EVENTO MARCADO COMO ESTORNA IRRF**

No log de cálculo será apresentado conforme abaixo:

O valor do adiantamento entra como Descontos = 822,00

Proventos = 2.055,01 - Descontos = 822,00 = Base de IRRF: 1.233,01

Valor do INSS: 166,77  
Total das deduções do funcionário: 166,77  
Valor a deduzir no IRRF Simplificado: 528,00  
Base de IRRF: 1.233,01 - 528,00 = 705,01

## **04. EXEMPLO DE UTILIZAÇÃO**

11Folha

**COM DEDUÇÃO SIMPLIFICADA:**

Base IRRF:3.218,75

Valor dedução somente INSS: 437,81

valor dedução simplificado: 528,00

Base após dedução INSS: 2780,94 - Valor do IRRF: Base(2.780,94) \* 7,5000% - 158,40 = 50,170500

Base após dedução Simplificado: 2690,75 - Valor do IRRF: Base(2.690,75) \* 7,5000% - 158,40 = 43,406250

**Veja abaixo o log de cálculo:**

              Calculando evento: **0004 - IRRF**  
              Código de Cálculo 4 - Prioridade 83  
                     Base de IRRF:   
                         Proventos = 3.218,75  
                         Descontos = 0,00  
                         Valor Dedutível = 0,00  
                         Base Líquida = 3.218,75  
                     Nro. dependentes de IRRF: 0  
                     Valor a deduzir por dependentes: 189,59  
                     Valor do INSS: 437,81  
**Total das deduções do funcionário: 437,81**  
**Valor a deduzir no IRRF Simplificado: 528,00**  
**Base de IRRF: 3.218,75 - 528,00 = 2.690,75**  
                     Limite Superior da Faixa na Tabela de IRRF: 2.826,65  
                     Percentual da Faixa na Tabela de IRRF: 7,5000 %  
                     Valor a Deduzir da Faixa na Tabela de IRRF: 158,40  
                     Valor do IRRF: Base(2.690,75) \* 7,5000% - 158,40 = 43,406250  
                     Valor do evento: 43,40

**SEM DEDUÇÃO SIMPLIFICADA:**

Base IRRF:5.000,00

Valor dedução somente INSS: 536,17

valor dedução simplificado: 528,00

Base após dedução INSS: 4463,83 - Valor do IRRF: Base(4.463,83) \* 22,5000% - 651,73 = 352,631750

Base após dedução Simplificado: 4472,00 - Valor do IRRF: Base(4.472,00) \* 22,5000% - 651,73 = 354,470000

**Veja abaixo o log de cálculo:**

              Calculando evento: **0004 - IRRF**

              Código de Cálculo 4 - Prioridade 83

                     Base de IRRF: 

                         Proventos = 5.000,00

                         Descontos = 0,00

                         Valor Dedutível = 0,00

                         Base Líquida = 5.000,00

                     Nro. dependentes de IRRF: 0

                     Valor a deduzir por dependentes: 189,59

                     Valor do INSS: 536,17

                     **Base de IRRF: 4.463,83**

                     Limite Superior da Faixa na Tabela de IRRF: 4.664,68

                     Percentual da Faixa na Tabela de IRRF: 22,5000 %

                     Valor a Deduzir da Faixa na Tabela de IRRF: 651,73

                     Valor do IRRF: Base(4.463,83) \* 22,5000% - 651,73 = 352,631750

                     Valor do evento: 352,63

213º Salário

**COM DEDUÇÃO SIMPLIFICADA:**

Base IRRF:3.000,00

Valor dedução somente INSS: 268,99

valor dedução simplificado: 528,00

##### Base após dedução INSS: 2731,01 - Valor do IRRF: Base(2.731,01) \* 7,5000% - 158,40 = 46,425750

Base após dedução Simplificado: 2472,00 - Valor do IRRF: Base(2.472,00) \* 7,5000% - 158,40 = 27,000000

**Veja abaixo o log de cálculo:**

              Calculando evento: **0049 - IRRF 13º SALARIO**

              Código de Cálculo 49 - Prioridade 83

                      Base de IRRF: 

                         Proventos = 3.000,00

                         Descontos = 0,00

                         Valor Dedutível = 0,00

                         Base Líquida = 3.000,00

                      Nro. dependentes de IRRF: 0

                     Valor a deduzir por dependentes: 189,59

                     Valor do INSS: 268,99

                     **Total das deduções do funcionário: 268,99**

**Valor a deduzir no IRRF Simplificado: 528,00**

**Base de IRRF: 3.000,00 - 528,00 = 2.472,00**

                     Limite Superior da Faixa na Tabela de IRRF: 2.826,65

                     Percentual da Faixa na Tabela de IRRF: 7,5000 %

                     Valor a Deduzir da Faixa na Tabela de IRRF: 158,40

                     Valor do IRRF: Base(2.472,00) \* 7,5000% - 158,40 = 27,000000

                     Valor do evento: 27,00

3Férias

**COM DEDUÇÃO SIMPLIFICADA:**

Base IRRF:3.309,20

Valor dedução somente INSS: 263,10

valor dedução simplificado: 528,00

##### Base após dedução INSS: 3046,10 - Valor do IRRF: Base(3.046,10) \* 15,0000% - 370,40 = 86,515000

Base após dedução Simplificado: 2781,20 - Valor do IRRF: Base(2.781,20) \* 7,5000% - 158,40 = 50,190000

**Veja abaixo o log de cálculo:**

              Calculando evento: **0030 - IRRF FERIAS**  
              Código de Cálculo 30 - Prioridade 83  
                     Base de IRRF:   
                         Proventos = 3.309,20  
                         Descontos = 0,00  
                         Valor Dedutível = 0,00  
                         Base Líquida = 3.309,20  
                     Nro. dependentes de IRRF: 0  
                     Valor a deduzir por dependentes: 189,59  
                     Valor do INSS: 263,10  
                    **Total das deduções do funcionário: 263,10**  
**Valor a deduzir no IRRF Simplificado: 528,00**  
**Base de IRRF: 3.309,20 - 528,00 = 2.781,20**  
                     Limite Superior da Faixa na Tabela de IRRF: 2.826,65  
                     Percentual da Faixa na Tabela de IRRF: 7,5000 %  
                     Valor a Deduzir da Faixa na Tabela de IRRF: 158,40  
                     Valor do IRRF: Base(2.781,20) \* 7,5000% - 158,40 = 50,190000  
                     Valor do evento: 50,19

4Rescisão

**COM DEDUÇÃO SIMPLIFICADA:**

**Veja abaixo o log de cálculo dos três cálculos e IRRF:**

              Calculando evento: **0004 - IRRF**  
              Código de Cálculo 4 - Prioridade 83  
                        Base de IRRF:   
                         Proventos = 3.000,00  
                         Descontos = 0,00  
                         Valor Dedutível = 0,00  
                         Base Líquida = 3.000,00  
                     Nro. dependentes de IRRF: 0  
                     Valor a deduzir por dependentes: 189,59  
                     Valor do INSS: 268,99  
**Total das deduções do funcionário: 268,99**  
**Valor a deduzir no IRRF Simplificado: 528,00**  
**Base de IRRF: 3.000,00 - 528,00 = 2.472,00**  
                     Limite Superior da Faixa na Tabela de IRRF: 2.826,65  
                     Percentual da Faixa na Tabela de IRRF: 7,5000 %  
                     Valor a Deduzir da Faixa na Tabela de IRRF: 158,40  
                     Valor do IRRF: Base(2.472,00) \* 7,5000% - 158,40 = 27,000000  
                     Valor do evento: 27,00  
                
              Calculando evento: **0049 - IRRF 13º SALARIO**  
              Código de Cálculo 49 - Prioridade 83  
                     Base de IRRF:   
                         Proventos = 2.992,60  
                         Descontos = 0,00  
                         Valor Dedutível = 0,00  
                         Base Líquida = 2.992,60  
                     Nro. dependentes de IRRF: 0  
                     Valor a deduzir por dependentes: 189,59  
                     Valor do INSS: 94,32  
**Total das deduções do funcionário: 94,32**  
**Valor a deduzir no IRRF Simplificado: 528,00**  
**Base de IRRF: 2.992,60 - 528,00 = 2.464,60**  
                     Limite Superior da Faixa na Tabela de IRRF: 2.826,65  
                     Percentual da Faixa na Tabela de IRRF: 7,5000 %  
                     Valor a Deduzir da Faixa na Tabela de IRRF: 158,40  
                     Valor do IRRF: Base(2.464,60) \* 7,5000% - 158,40 = 26,445000  
                     Valor do evento: 26,44  
                
              Calculando evento: **0061 - IRRF FÉRIAS ENVELOPE**  
              Código de Cálculo 61 - Prioridade 83  
                     Base de IRRF:   
                         Proventos = 5.317,76  
                         Descontos = 0,00  
                         Valor Dedutível = 0,00  
                         Base Líquida = 5.317,76  
                      Nro. dependentes de IRRF: 0  
                     Valor a deduzir por dependentes: 189,59  
**Total das deduções do funcionário: 0,00**  
**Valor a deduzir no IRRF Simplificado: 528,00**  
**Base de IRRF: 5.317,76 - 528,00 = 4.789,76**  
                     Limite Superior da Faixa na Tabela de IRRF: 99.999.999.999,00  
                     Percentual da Faixa na Tabela de IRRF: 27,5000 %  
                     Valor a Deduzir da Faixa na Tabela de IRRF: 884,96  
                     Valor do IRRF: Base(4.789,76) \* 27,5000% - 884,96 = 432,224000  
                     Valor do evento: 432,22

5Flags do IRRFSIMPLIFICADOAtenção

A apresentação em tela da marcação dos campos, citada abaixo, estará disponível somente a partir da versão 12.1.2306 e superiores.

IMPORTANTE

Veja também Demais Informações desse documento.

Veja também o [DT - IRRF Simplificado - Indicativo de Cálculo no Período da Ficha Financeira](https://tdn.totvs.com.br/pages/viewpage.action?pageId=827305670)

Quando houver cálculo de IRRF usando o valor simplificado, os campos IRRFSIMPLIFICADO, IRRF13SIMPLIFICADO e IRRFFERSIMPLIFICADO serão marcados no banco. 

No período da ficha financeira (PFPERFF) e no período da ficha financeira complementar (PFPERFFCOMPL) serão demonstrados conforme print abaixo:

**EXEMPLO DO CÁLCULO DE RESCISÃO**

No recibo de férias (PFUFERIASRECIBO) será demonstrado IRRFSIMPLIFICADO conforme print abaixo:

**Observação:** A demonstração do IRRFSIMPLIFICADO no recibo de férias não será feita no período da ficha financeira (PFPERFF). A demonstração feita no período da ficha financeira será referente ao cálculo de férias na rescisão e diferença de férias.

6Log do Parâmetro "Desconsiderar Desconto Simplificado do IRRF" marcado

Quando o Parâmetro "[Desconsiderar Desconto Simplificado do IRRF](https://tdn.totvs.com/pages/viewpage.action?pageId=452719181)" será demonstrado no log para que o usuário saiba o motivo daquele cálculo não ter usado o desconto simplificado de IRRF.

**Veja exemplo de log abaixo**:

              Calculando evento: 0004 - IRRF  
              Código de Cálculo 4 - Prioridade 83  
                     Base de IRRF:   
                         Proventos = 3.218,75  
                         Descontos = 0,00  
                         Valor Dedutível = 0,00  
                         Base Líquida = 3.218,75  
                     Nro. dependentes de IRRF: 0  
                     Valor a deduzir por dependentes: 189,59  
                     Valor do INSS: 437,81  
                     Total das deduções do funcionário: 437,81  
                     Valor a deduzir no IRRF Simplificado: 528,00  
                     **Parâmetro "Desconsiderar Desconto Simplificado do IRRF" está marcado no cad.Funcionário.**  
                     Base de IRRF: 2.780,94  
                     Limite Superior da Faixa na Tabela de IRRF: 2.826,65  
                     Percentual da Faixa na Tabela de IRRF: 7,5000 %  
                     Valor a Deduzir da Faixa na Tabela de IRRF: 158,40  
                     Valor do IRRF: Base(2.780,94) \* 7,5000% - 158,40 = 50,170500  
                     Valor do evento: 50,17

7Lançamento dos códigos de cálculoIMPORTANTE

Liberado a partir das versões:

12.1.2402.255

12.1.2406.200

12.1.2410.130

12.1.2502 e superiores

Quando houver desconto do simplificado no período da ficha financeira será lançado o código de cálculo de acordo com o tipo de lançamento

* Código de cálculo [477 -  VALOR A DEDUZIR DE IRRF SIMPLIFICADO FOLHA](https://tdn.totvs.com.br/pages/viewpage.action?pageId=892139184)
* Código de cálculo [478 - VALOR A DEDUZIR DE IRRF SIMPLIFICADO FÉRIAS](https://tdn.totvs.com.br/pages/viewpage.action?pageId=892139208)
* Código de cálculo [479 - VALOR A DEDUZIR DE IRRF SIMPLIFICADO 13º SALÁRIO](https://tdn.totvs.com.br/pages/viewpage.action?pageId=892139220)

 

IMPORTANTE

Esses códigos de cálculos serão lançados por período no envelope de pagamento e serão usados exclusivamente para o envio no XML do eSocial.

É de responsabilidade do usuário informar o código de incidência 68 no cadastro de eventos vinculados aos códigos de cálculo acima.

O processo de cálculo continuará preenchendo os campos indicativos do período da ficha financeira e recibo de férias quando for utilizado o desconto simplificado.

Esses códigos de cálculos não serão usados no processo da DIRF.

Caso não queira enviar esse evento no XML do eSocial, insira no Paramertrizador / eSocial / Registros Inativos / Eventos a Desconsiderar.

Nos cálculos abaixo foram usados o valor do desconto simplificado para obter o IRRF então nos respectivos envelopes foram lançados os eventos base de cálculo com o valor do desconto simplificado.

Lançamento na folha de pagamento

Lançamento na 13º salário

Lançamento nas férias

Lançamento na rescisão

## **05.****DEMAIS INFORMAÇÕES**

O comportamento para os campos IRRFSIMPLIFICADO, IRRF13SIMPLIFICADO e IRRFFERSIMPLIFICADO:

* Se o cálculo de IRRF estiver usando o valor simplificado para dedução então os campos serão marcados no banco com valor 1, mesmo que não tenha desconto de IRRF para o funcionário, ou seja, após a apuração da base de IRRF e aplicação do cálculo, o valor do desconto de IRRF foi zero.
* Se o cálculo de IRRF não está usando o valor simplificado para dedução, ou seja, o mais benéfico para o funcionário são as deduções legais, então os campos serão marcados no banco com 0 (zero), mesmo que não tenha desconto de IRRF para o funcionário.
* Se não atingiu a faixa para desconto de IRRF, ou seja, a base tributável esteja na faixa isenta de IRRF conforme configurado na tabela de Cálculo de IRRF vigente, então os campos serão marcados no banco com 0 (zero), independente se o valor simplificado for mais benéfico que as deduções legais.
* Se houver cálculo de IR no mesmo caixa, mesmo que naquele período não tenha base de IR, será marcado com valor 0 ou 1 conforme as regras acima.
* Se não não houver cálculo de IR no caixa, os campos serão marcados com o valor 0 (zero).

## **06. TABELAS UTILIZADAS**

* PVALFIX
* PFUNC
* PFPERFF
* PFPERFFCOMPL
* PFUFERIASRECIBO
