---
content_hash: 500553de57ea15739741239e3cee6f05d2ab27da54ee44c0435a901f70e96546
fetched_at: '2026-06-29T00:09:52.882351+00:00'
page_id: '439695526'
product: rm
source: tdn-rm
title: Pagamento de 13º Salário integralmente em meses anteriores a Dezembro (Com
  discriminação da média)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=439695526
version: 4
---

# **Pagamento de 13º Salário - 2015**

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Folha de Pagamento                      **Versão:**11.8X e 12.X |
| **Processo** | **:** | 13º Salário |
| **Subprocesso** | **:** | Cálculo e Lançamento do 13º |
| **Data da publicação** | **:** | 25/11/2016 |

#### **○ Parametrização 13º Salário – Com Média**

**• Cadastro de Eventos:** Visualização em Delphi: *Cadastros* | *Eventos*

Nova MDI: Aba *Administração de Pessoal* | *Eventos* | *Eventos*

Deverá existir na base de dados eventos cadastrados com os seguintes códigos de cálculo:

1543439857095\_-1605996941

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CC09 | - | Evento 1ª Parcela de 13º Salário |  |  |
| CC35 | - | Adiantamento 13º Salário |  |  |
| CC49 | - | IRRF 13º Salário |  |  |
| CC58 | - | Dedutível IRRF 13º Salário |  |  |
| CC66 | - | Diferença de 13º Salário |  |  |
| CC83 | - | Base de INSS 13º Salário Outro Emprego |  |  |
| CC101 | - | 13º Salário Pago pela Previdência |  |  |
| CC102 | - | 2ª Parcela de 13º Salário |  |  |
| CC103 | - | INSS 2ª parcela 13º Salário |  |  |
| CC106 | - | IRRF 13º Calculado pelo Usuário |  |  |
| CC144 | - | INSS 13º Outro Emprego |  |  |
| CC171 | - | Valor do INSS Descontado pela Previdência |  |  |
| CC172 | - | Valor do IRRF Descontado pela Previdência |  |  |
| **#DICA** **Para maiores informações sobre estes eventos acesse:** [{\*}{+}](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.eventos.aspx)[http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.eventos.aspx+\*](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.eventos.aspx+*) |  |  |  |  |  |  |

**• Cadastro/Sindicatos:**

Visualização em Delphi: *Cadastros* | *Sindicatos* 

Nova MDI: Aba *Administração de Pessoal* | *Sindicatos*

O cadastro de sindicato mantém, principalmente, as parametrizações de médias relativas a CLT ou Convenções Coletivas dos sindicatos dos trabalhadores. É dividido em pastas que contém parametrizações específicas de média de Férias, 13º Salário, Aviso Prévio, Licença Maternidade, Valores Associados do Sindicato e HomologNet. As parametrizações de 13º se encontram no: 

Cadastro de sindicatos em Delphi: Aba *13º Salário* | Sub-aba *Parâmetros de media* 

Cadastro de sindicatos .NET: Aba *13º Salário* | Sub-aba *Media 13º*  
   
Sindicato em Delphi  
  
 Sindicato .Net

|  |
| --- |
| **Atenção!**    \***Nas sub abas referente a eventos para pagamento de médias de 13º é preciso existir, obrigatoriamente, o grupo 0 (zero). O evento a ser informado no campo "Evento de Pagamento" deve conter o código de cálculo 102 e o no campo "Evento de Diferença", o código de cálculo 66. No grupo 0 (zero) de 13º Rescisão, o "Evento de Pagamento" terá código de cálculo 48 e o "Evento de Diferença", o código de cálculo código de cálculo 97.**   * + Caso a empresa trabalhe com médias discriminadas, outros grupos poderão ser criados. Os eventos informados nesses grupos deverão ter os mesmos códigos de cálculo do grupo 0 de 13º Salário (Evento de pagamento com C.C. 102 e Evento de Diferença com C.C 66).\* |

**Exemplo :** Eventos cadastrados na aba *13º Salário* | Sub-aba *Eventos p/ pag. de Media de 13º na 2º Parcela*.  
**Grupo 0:** Evento de Pagamento: CC 102 - 2ª parcela de 13º salário. Evento de Diferença: CC 66 - Dif. 2ª parcela de 13º salário. Evento para diferença por dissídio: CC 180 Dif. 13º salário por dissídio.  
**Grupo 1:** Evento de Pagamento: CC 102 - Média de H. Extra 13º salário 2ª parcela. Evento de Diferença: CC 66 - Dif. média de H. Extra 13º salário 2ª parcela. Evento para diferença por dissídio: CC 180 Dif. média H.Extra 13º salário p/ dissídio.  
**Grupo 2:** Evento de Pagamento: CC102 - Média de Comissão 13º salário 2ª parcela. Evento de Diferença: CC 66 - Dif. média de Comissão 13º salário 2ª parcela. Evento para diferença por dissídio: CC 180 Dif. média Comissão 13º salário p/ dissídio.

Delphi  
  
   
.Net

#### **○ Parâmetros de 13º Salário**

**• Parâmetros do TOTVS Folha de Pagamento**   
Determinaremos neste módulo os parâmetros para cálculo do 13º salário.

Visualização em Delphi: *Opções* | *Parâmetros* | *RM Labore* | Aba *Parâmetros 13º Salário*   
 

Nova MDI: Aba *Configurações*| *Parametrizador* | *13º Salário*

   
**Parâmetros**  
***Campos:***

**Utiliza salário atual p/ 1ª parcela :** Como este campo habilitado, o sistema assumirá como base de cálculo da 1º parcela do 13º, o salário do mês de pagamento (no caso de alteração de salário no mês do pagamento, normalmente em novembro) ao invés do salário do mês anterior.

**Exemplo 1**:

Histórico salarial do funcionário:

01/02/2012 - R$ 450,00

01/11/2012 - R$ 500,00

Com o parâmetro marcado, o sistema assumirá o salário do mês 11/12 (R$ 500,00).

Com o parametro desmarcado, será considerado o salário do mês anterior (R$ 450,00)

**Exemplo 2**:

Histórico salarial do funcionário:

01/02/2012 - R$ 450.00

01/10/2012 - R$ 500.00

Neste caso, o parâmetro não será influenciado, pois o funcionário não teve alterações de salário no mês de novembro (quando normalmente se paga a 1º parcela). Será considerado o salário do mês 10/12 ( R$ 500,00)

**- Calcula avos p/ 1ª parcela considerando meses até dezembro**: Habilite este campo somente se quiser que o sistema considere dezembro para o cálculo do número de avos para os funcionários admitidos no curso do ano, a partir de 18 de janeiro (inclusive).

 **- Calcula avos p/1ª parcela considerando meses até o atual:** Habilite este parâmetro para que o sistema considere o número de avos até o mês de pagamento da primeira parcela (normalmente, novembro), dos funcionários admitidos a partir de 18 de janeiro. **Exemplo**:

Um funcionário admitido em 05/08 terá direito a 4 (quatro) avos, se o mês de novembro for considerado para o cálculo do número de avos.

Deixe o campo em branco para que o sistema considere o número de avos até outubro dos funcionários admitidos a partir de 18 de janeiro (inclusive). **Exemplo**:

Um funcionário admitido em 05/08 terá direito a 3 (três) avos, se o mês de outubro for considerado para o cálculo.

**- Provisão de Eventos Adicionais de 13º Salário:** De acordo com a seleção dos parâmetros abaixo, o sistema irá considerar ou não os Eventos Adicionais de 13° Salário, na Geração de Histórico de Provisões:

\* Sempre Provisionar: Marcando esta opção o sistema irá considerar na Geração de Histórico de Provisões os Eventos Adicionais Globais, de 13° Salário.

\* Nunca Provisionar: Marcando esta opção o sistema não irá considerar na Geração de Histórico de Provisões os Eventos Adicionais Globais, de 13° Salário.

\* Provisionar de forma personalizada: Marcando esta opção, será habilitado nos Eventos Adicionais Globais o campo "Provisionar Evento". Com este campo será possível selecionar os eventos que irão ou não participar do cálculo da Geração do Histórico de Provisões.

**- Fórmula p/valor a somar ao 13º salário:** Selecione uma fórmula cujo resultado será adicionado à base de cálculo do 13º salário.

**- Meses de afastamentos por acidente de trabalho reduz avos de 13º:** Quando marcado, este parâmetro usará os afastamentos por acidente de trabalho (T) e Doença Ocupacional (O) para diminuir os avos de 13º que o funcionário tem direito. Se estiver desmarcado, esses tipo de afastamento não afetarão o cálculo.

***Observação:*** Pela lei os afastamentos por acidente de trabalho não devem reduzir o números de avos de 13º, porém, algumas empresas podem interpretar de outra forma ou terem previdência privada e desta forma, não irão considerar estes afastamentos no cálculo de 13º salário.

**Exemplo**: Suponha um afastamento por acidente de trabalho: 26/06 (16º dia seguinte ao do afastamento do trabalho) até 21/10.  
          Parâmetro marcado: 6/12 (anterior ao afastamento) + 2/12 (posterior ao afastamento) = 8/12 avos  
          Parâmetro desmarcado: 12/12 avos (o afastamento não reduz avos de 13º)

**- Bloqueia reversão automática de 13º salário no mês janeiro:** Marque essa opção para que, ao contabilizar a provisão mensal do 13º salário no mês de janeiro, o sistema considere o valor da provisão acumulada do mês anterior igual a zero . Logo, a provisão mensal e a provisão acumulada do mês de janeiro serão iguais. Esclarecemos que em dezembro a provisão acumulada é relativa a 12/12 avos e em janeiro a provisão acumulada é de apenas 1/12. Ao final de um ano contábil, é necessário uma reversão nas contas de resultado de provisão da contabilidade. O RM Labore faz isto automaticamente, quando o usuário opta pela provisão mensal ( que é o valor acumulado mês atual - o valor acumulado do mês anterior), pois esta é negativa e o sistema inverte as contas débito/crédito. Esta reversão só ocorre no mês de janeiro. Quando as empresas fazem a reversão por conta própria em dezembro ( o próprio contador faz um artifício contábil sem o conhecimento do RM Labore para que seja zerado o conteúdo das contas de resultado de provisão), NÃO É MAIS NECESSÁRIO a reversão automática das contas débito/crédito que o RM Labore faz. Logo, este recurso possibilita o bloqueio desta reversão de contas automaticamente. Confira os exemplos:

**Exemplo 1**:

1. Mês de Competência: janeiro
2. Parâmetro MARCADO: Bloqueia reversão automática de 13 salário no mês janeiro
3. Provisão acumulada do mês atual (Janeiro) = 41,67 (1/12)
4. Provisão acumulada do mês anterior (Dezembro)= 522,47 (12/12)
5. Contabilização Provisão dos Encargos tipos 7 (Provisão de 13º), 8(Provisão FGTS de 13º) e 9 (Provisão Encargos de 13º)
6. Conta Débito: 1.0001.0
7. Conta Crédito: 2.0001.0
8. Provisão Mensal = Provisão acumulada do mês atual (janeiro) - Provisão acumulada do mês anterior (dezembro)
9. Resultado = R$ 41,67 - 0 = R$ 41,67
10. Lançamento contábil:            Conta Débito: 1.0001.0 = 41,67

                    Conta Crédito: 2.0001.0 = 41,67 **Exemplo 2**:

1. Mês de Competência: janeiro
2. Parâmetro DESMARCADO: Bloqueia reversão automática de 13 salário no mês janeiro
3. Provisão acumulada do mês atual (Janeiro) = 41,67 (1/12)
4. Provisão acumulada do mês anterior (Dezembro)= 522,47 (12/12)
5. Contabilização Provisão dos Encargos tipos 7(Provisão de 13º), 8(Provisão FGTS de 13º) e 9(Provisão Encargos de 13º salário)
6. Conta Débito: 1.0001.0
7. Conta Crédito: 2.0001.0
8. Provisão Mensal = Provisão acumulada do mês atual (janeiro) - Provisão acumulada do mês anterior (dezembro)
9. Resultado = 41,67 - 522,47 = - 480,80 (valor negativo - reversão das contas débito/crédito)
10. Lançamento contábil:            Conta Débito: 2.0001.0 = R$480,80

                    Conta Crédito: 1.0001.0 = R$480,80  
   
**- Ignora eventos que incidem salário:** Selecione esta opção caso queira desconsiderar os eventos que incidem em salário para os cálculos da base de 13º. Se for considerá-los, desmarque o parâmetro e lembre que os eventos devem ser lançados antes do cálculo do 13º salário.

 **- Paga eventos adicionais na 1ª parcela de 13º salário:** Marque este campo para que os eventos adicionais globais de 13º salário sejam considerados no pagamento da 1ª parcela.

***Atenção:*** estes eventos não serão discriminados no movimento da 1ª parcela de 13º salário. Serão discriminados apenas no movimento da 2ª parcela de 13º salário.

 **- Evento de código de cálculo 106 inibe o evento de código de cálculo 49:** Se o parâmetro for marcado, ao ser lançado o evento com o CC106 - IRRF 13º CALCULADO PELO USUÁRIO na movimentação do funcionário o sistema irá zerar o evento CC49 - I.R.R.F. 13º Salário.Se o parâmetro não for marcado, for lançado na movimentação do funcionário o evento com o CC106 - IRRF 13º CALCULADO PELO USUÁRIO e este valor for menor que o evento de CC49, que seria calculado automaticamente pelo sistema , o sistema irá considerar os dois eventos. Esta diferença será lançada no evento de CC49.Caso o valor informado no evento CC106 seja maior ou igual ao valor do evento de CC49, o sistema irá zerar o evento CC49.

Na visualização dos parâmetros, existe a flag **"Lança desconto de arredondamento (código** **de cálculo 21)**

Se o parâmetro for marcado, o sistema lançará o evento com código de cálculo 314 para armazenar o valor do arredondamento (cc21), para que o mesmo seja descontado no próximo período.

Este tratamento foi implementado para o sistema não descontar o evento com código de cálculo '21-Arredondamento Descontos' no lançamento do 13º Salário. E atender a 1º e 2º parcela do 13º Salário.

**Exemplo:** No período 1 foram realizados os seguintes lançamentos:  
Cod.     Descrição                        Valor              Prov/Desc/Base

0008    Desconto de faltas           1.000,00         Desconto

0020    Arredondamento              1.000,00          Provento

**Liquido: 0,00 (zero)**

No período 2 foi processado o lançamento da 1º parcela com o parâmetro 'Lança desconto de arredondamento (código de cálculo 21)' MARCADO:

Cod.    Descrição                                     Valor              Prov/Desc/Base

0009    1ª Parcela 13º                              500,00            Provento

0314    Base Arredondamento(cc314)   1.000,00          Base

**Liquido: 500,00**

Se for realizado um lançamento para o funcionário no período 3 é descontado o arredondamento.

Cod.    Descrição                                      Valor              Prov/Desc/Base

9999    Provento                                      1.300,00          Provento

0021    Arredondamento Desc.(cc21)    1.000,00          Desconto

**Liquido: 300,00**   
  
**Códigos Fixos no 13º Salário**   
Esta aba é utilizada para definir quais os "tipos de códigos fixos" serão lançados ao calcular o 13º salário. Esses tipos são previamente cadastrados na tabela dinâmica INT42 e tem a função de agrupar "códigos fixos" para efeito de lançamento na movimentação.    
"Códigos fixos" são eventos que ocorrem com regularidade e devem ser lançados na movimentação mensal do funcionário por um período determinado. Esses eventos são associados no cadastro do funcionário em:  
 

Visualização em Delphi: *Cadastros* | *Funcionários* | Aba *Base de calculo* | Sub-aba *Códigos Fixos* Nova MDI: Aba *Admistração de Pessoal* | *Funcionários* | Opção *Informações para o calculo* | *Códigos Fixos*

  Parâmetros do sistema Delphi

Parâmetros do sistema .NET  
  
   
**Fórmulas adicionais pra a base 13º**

É utilizada para informar referências de fórmulas cujos resultados serão adicionados a base de cálculo do 13º na 2ª parcela.

Fórmulas adicionais em Delphi

Fórmulas adicionais .NET

**Eventos Adicionais Globais**

Poderão ser informados eventos que serão lançados, de forma global, juntamente com o cálculo do 13º Salário.

Eventos adicionais Delphi

  Eventos adicionais .NET

#### **○ 1ª Parcela de 13º Salário (Automático)**

Através destes módulos será realizado o lançamento do 13º salário sem média discriminada.

Visualização em Delphi: *Movimento* | *Folha de Pagamento* | *Lançamentos Automáticos* | *Décimo Terceiro* *Salário*  
   
  
  
 

Visualização em .Net: *Movimento* | *13º Salário (.NET)* | *Lançamento*  
  

Nova MDI: Aba *Folha Mensal* | *Calculo 13º*

***Preenchimento dos campos:***

**• Primeira parcela:** Marque este campo se a empresa está processando a primeira parcela para o pagamento.

**• Ajustar primeira parcela:** Este campo ficará marcado como padrão sempre que for lançada a 1ª parcela.

O parâmetro funciona da seguinte forma: Suponhamos que foi realizado o adiantamento do 13º salário no mês de Julho/12, para um funcionário que tem o salário de R$ 1000,00. Em Novembro/12 ele recebeu um aumento salarial e passou a receber R$1500,00.

Para que o ajuste referente a alteração salarial seja efetuado ao lançar novamente a 1ª parcela, o parâmetro "Ajustar 1ª Parcela" deverá ser marcado. Desse modo, os seguintes eventos referentes a 13º serão lançados:

-1ª Parcela de 13º Salário (Código de Cálculo 9) no valor de R$ 750,00 (Provento);

-Adiantamento de 13º Salário (Código de Cálculo 35) no valor de R$ 500,00 (Desconto).

Onde a diferença referente ao aumento salarial corresponde a R$ 250,00.

Se este parâmetro não estiver marcado, o sistema verificará que o evento de 1ª Parcela de 13º Salário já foi lançado (Código de Cálculo 009) e não fará o lançamento do ajuste.

**○ 1ª Parcela com Média discriminada**

**1º Passo:** Criar fórmula que fará o cálculo da média dos eventos discriminados. Abaixo segue exemplo lembrando que é de responsabilidade do usuário criar a fórmula que atenderá as necessidades da empresa. Acesse:

Visualização em Delphi: *Cadastros* | *Fórmulas*

Nova MDI: Aba *Administração de Pessoal* | *Fórmulas*  
   
**Código:** A0020

**Título:** Média 13º na 1ª Parcela

**Texto:** CALCMED(201) / 2  
 

**2º Passo:** Cadastrar um evento de média que seja do tipo Provento, Valor, com Código de Cálculo 9 e incidência em FGTS. No campo "fórmula de valor", associe a fórmula criada no 1º passo.  
   
  
   
**3º Passo:** Acesse o módulo de sindicato e desmarcar a opção "Paga média na 1ª Parcela".

Visualização em Delphi: *Cadastros* | *Sindicatos*| *Parâmetros*  
    
 

Nova MDI: Aba *Administração de Pessoal* | *Sindicatos*

**4º Passo:** Execute o pagamento da primeira parcela através do módulo:    
 

Visualização em Delphi: *Movimento* | *Folha de Pagamento* | *Lançamentos Automáticos* | *Décimo Terceiro* *Salário*  
 

Visualização em .Net: *Movimento* | *13º Salário (.NET)* | *Lançamento*   
 

Nova MDI: Aba *Folha Mensal* | *Calculo 13º*

**5º Passo:** Crie um grupo de evento específico para lançar os eventos de médias. Na aba "Eventos do grupo", informe o evento criado no 2º passo.

Visualização em Delphi: *Movimento* | *Folha de Pagamento* | *Lançamentos Automáticos* | *Grupo de* *Eventos*.   
  
Visualização em .Net: *Movimento* | *Folha de Pagamento* | *Lançamentos Automáticos* | *Grupo de* *Eventos.Net*.  
  
Nova MDI: Aba *Folha Mensal* | *Lançamentos* | *Grupo de Eventos.*  
  

**6º Passo:** Lance o Grupo de Eventos.

**○ Pagamento de 13º Salário integralmente em meses anteriores a Dezembro (Com discriminação da média)**

Para o pagamento da 2ª parcela antecipadamente, deve-se observar que os encargos de INSS e IRRF serão recolhidos para os órgãos competentes **apenas no mês de Dezembro** (mês da quitação). Isso se deve ao fato de que o pagamento ocorrido em novembro ou em outros meses anteriores ao mês de dezembro são antecipações (adiantamento).

|  |
| --- |
| **Atenção!**  **Para efetuar o lançamento do 13º integral em meses anteriores, a preparação do sistema deverá ser a mesma dos passos acima. Para o cálculo do valor do 13º antecipado, a parametrização a ser utilizada está indicada abaixo.** |

**PREPARAÇÃO DO SISTEMA**  
Cadastrar as fórmulas Básicas para o cálculo  
 

Visualização em Delphi: *Cadastros* | *Fórmulas*  
 

Nova MDI: Aba *Administração de Pessoal* | *Fórmulas*

**Código:** CHAPA

**Título:** Chapa

**Texto:** Chapa

-----  
**Código:** ANO

**Título:** Ano

**Texto:** Ano

-----

**Código:** MES

**Título:** Mês de Competência

**Texto:** MES

-----

**Código:** COLIGADA

**Título:** Coligada

**Texto:** Coligadacorrente

-----  
**Código:** PERIODO

**Título:** Período atual

**Texto:** Periodo  
-----

**• 1º Passo:** Cadastre a seguinte consulta SQL

 Visualização em Delphi: *Utilitários* | *Consultas SQL*  
 

Nova MDI: Aba *Gestão* | *Visões de dados*  
 

**Código:** 13SALARIO

**Título:** 13º salário pago durante o ano

**Texto:**

**SELECT SUM**(VALOR) VALOR **FROM PFFINANC** (**NOLOCK**), **PEVENTO** (**NOLOCK**), **PPARAM** (**NOLOCK**)

**WHERE** PFFINANC.CODCOLIGADA=PEVENTO.CODCOLIGADA **AND** PPARAM.CODCOLIGADA=PFFINANC.CODCOLIGADA **AND** PEVENTO.CODIGO=PFFINANC.CODEVENTO **AND**PFFINANC.CHAPA=:FRM\_CHAPA **AND** PEVENTO.CODIGOCALCULO='9' **AND** (PFFINANC.MESCOMP<>PPARAM.MESCOMP **OR** PFFINANC.NROPERIODO<> :FRM\_PERIODO) **AND**PFFINANC.ANOCOMP=PPARAM.ANOCOMP **AND** PFFINANC.CODCOLIGADA=:FRM\_COLIGADA

**• 2º Passo:** Cadastrar as seguintes fórmulas   
 

Visualização em Delphi: *Cadastros* | *Formulas*   
 

Nova MDI: Aba *Administração de Pessoal* | *Formulas*

|  |
| --- |
| **Atenção!**  **As fórmulas não consideram os meses de admissão caso o número de dias trabalhados sejam inferiores 15 dias.** |

**Código:** A0011

**Título:** AVOS 13 SALÁRIO INTEGRAL EM MESES ANTERIORES A DEZEMBRO

**Texto:**

SE SFUNC<>'P' E SFUNC<>'M' E SFUNC<>'R' E SFUNC<>'L' ENTAO

          NROAVOS13+ABS(MES-12)

SENAO

          NROAVOS13

FIMSE

**Código:** A0012

**Título:** 13 SALÁRIO INTEGRAL EM MESES ANTERIORES A DEZEMBRO

**Texto:**

execsql('13SALARIO');

SE SFUNC<>'P' E SFUNC<>'M' E SFUNC<>'R' E SFUNC<>'L' ENTAO

          (RC/12)\*(NROAVOS13+ABS(MES-12))-resultsql('13SALARIO','valor')

SENAO

          (RC/12)\*(NROAVOS13)-resultsql('13SALARIO','valor')

FIMSE

Caso queira que as fórmulas adicionais de 13º informadas nos módulos abaixo sejam consideradas, a fórmula anterior (A0012) deverá ser alterada da seguinte forma:

Fórmula:

execsql('13SALARIO');

SE SFUNC<>'P' E SFUNC<>'M' E SFUNC<>'R' E SFUNC<>'L' ENTAO

          ((RC + FOR("XXXX") + FOR("YYYY"))/12) \* (NROAVOS13+ABS(MES-12))

SENAO

          ((RC + FOR("XXXX") + FOR("YYYY"))/12) \* (NROAVOS13)

FIMSE

Onde houver XXXX ou YYYY deverá ser alterado para as fórmulas adicionais existentes.\*

**Código:** A0016

**Título:** MEDIA DE 13 SALÁRIO INTEGRAL EM MESES ANTERIORES A DEZEMBRO

**Texto:**

execsql('13SALARIO');

SE SFUNC<>'P' E SFUNC<>'M' E SFUNC<>'R' E SFUNC<>'L' ENTAO

          (CALCMED(2)/12)\*(NROAVOS13+ABS(MES-12))

SENAO

          (CALCMED(2)/12)\*(NROAVOS13)

FIMSE

**Código:**A0013

**Título:** INSS DE ANTECIPAÇÃO DE 13º SALARIO

**Texto:**

execsql('13SALARIO');

TI(FOR('A0012') + FOR('A0016') - resultsql('13SALARIO','valor'))

**Código:**PENS13PR

**Título:** Pensão sobre líquido de 13º salário antecipado (liquido)

**DELPHI:**

DECL PERC, CONT, X; SETVAR (CONT,1); SE TABDEP ('DTNASCIMENTO' ,'V' ,CONT) <>0 ENTAO REPITA SE TABDEP ('DTNASCIMENTO','V',CONT) <>0 E TABDEP ('INCPENSAO','S',CONT) ='1' ENTAO SETVAR (PERC, TABDEP ('PERCENTUAL' , 'V', CONT) / 100); SETVAR (X,1) SENAO "" FIMSE; SETVAR (CONT,CONT+1)  ATE X=1 OU TABDEP ('DTNASCIMENTO' ,'V' ,CONT) =0 FIMSE;   
SE X>0 ENTAO DECL LIQUIDO, VLRBASEIRRF, VLRINSS, VLRINSS2, VLR,CONTADOR; SETVAR (LIQUIDO, C('8001') + C('8005'));

/\***Se quiser deduzir o valor adiantado basta diminuir o valor do evento cc 35\***/ SETVAR (VLRINSS, TI (LIQUIDO)); SETVAR (VLRINSS2, TI2(LIQUIDO)); SETVAR (VLRBASEIRRF, LIQUIDO); REPITA SETVAR (VLR, ((LIQUIDO-VLRINSS- TR (VLRBASEIRRF-VLRINSS2-VLR)) \* PERC)); SETVAR (CONTADOR, CONTADOR+1) ATE CONTADOR= 7; VLR SENAO 0 FIMSE

**.NET:**

DECL PERC, CONT, X;  
SETVAR (CONT,1);  
SE TABDEP ('DTNASCIMENTO' ,'D' ,CONT) <> DATANULA ENTAO  
          REPITA  
                    SE TABDEP ('DTNASCIMENTO','D',CONT) <> DATANULA E TABDEP ('INCPENSAO','S',CONT) ='1' ENTAO  
                              SETVAR (PERC, TABDEP ('PERCENTUAL' , 'V', CONT) / 100);  
                              SETVAR (X,1)  
                    SENAO ''  
                    FIMSE;  
          SETVAR (CONT,CONT+1)  
          ATE X=1 OU TABDEP ('DTNASCIMENTO' ,'D' ,CONT) = DATANULA  
FIMSE;  
   
SE X>0 ENTAO  
          DECL LIQUIDO, VLRBASEIRRF, VLRINSS, VLRINSS2, VLR,CONTADOR;  
          SETVAR (LIQUIDO, C('8001') + C('8005')); /\***Se quiser deduzir o valor adiantado basta diminuir o valor do evento cc 35\***/  
          SETVAR (VLRINSS, TI (LIQUIDO));  
          SETVAR (VLRINSS2, TI2(LIQUIDO));  
          SETVAR (VLRBASEIRRF, LIQUIDO);  
          REPITA  
                    SETVAR (VLR, ((LIQUIDO-VLRINSS- TR (VLRBASEIRRF-VLRINSS2-VLR)) \* PERC)); SETVAR (CONTADOR, CONTADOR+1)  
          ATE CONTADOR= 7; VLR  
SENAO 0  
FIMSE

|  |
| --- |
| **Atenção!**  **A fórmula acima somente deverá ser criada caso queira descontar a pensão sobre o pagamento do 13º salário integral. Neste, o usuário também deverá cadastrar um evento do tipo desconto/valor sem incidências e associar a fórmula PENS13PR.** |

**Código:** A0014

**Título:** IRRF DE ANTECIPAÇÃO DE 13º SALÁRIO

**Texto:**

EXECSQL('13SALARIO'); DECL BCALC;

SETVAR(BCALC,FOR('A0012')+FOR('A0016')+RESULTSQL('13SALARIO','VALOR'));

TR(BCALC-TI(BCALC)- FOR('PENS13PR'))

   
**Código:** A0015

**Título:** DESCONTO DE INSS E IRRF ANTECIPADO

**Texto:** MV(15,ANO,'8003')+MV(15,ANO,'8002')

|  |
| --- |
| **Atenção!**   **Em caso do desconto do evento de pensão, incluir na fórmula acima +MV(15,ANO,'XXXX'), onde XXXX deve ser substituído pelo código do evento de pensão criado conforme descrito na observação da fórmula PENS13PR.** |

**• 4º Passo: Cadastrar os seguintes eventos**   
 

Visualização em Delphi: *Cadastros* | *Eventos*   
 

Nova MDI: Aba *Administração de Pessoal* | *Eventos* | Opção *Eventos*

**Código:** 8001

**Descrição:** Adiantamento de 13º Salário Provento/Valor, com Código de Cálculo 09. Incide FGTS e RAIS No campo "Fórmula valor" informar a fórmula de código A0012. No campo "Fórmula Referência" informar a fórmula de código A0011.

-----

**Código:** 8005

**Descrição:** Média de adiantamento de 13º Salário Provento/Valor, com Código de Cálculo 09. Incide FGTS e RAIS No campo "Fórmula valor" informar a fórmula de código A0016. No campo "Fórmula Referência" informar a fórmula de código A0011.

-----

**Código:** 8002

**Descrição:** INSS 13º Salário (antecipado) Desconto/Valor, sem Código de Cálculo. No campo "Fórmula valor" informar a fórmula de código A0013.

-----  
**Código:** 8003

**Descrição:** IRRF 13º Salário (antecipado) Desconto/Valor, sem Código de Cálculo. No campo "Fórmula valor" informar a fórmula de código A0014.

-----  
**Código:** 8004

**Descrição:** Desconto de INSS13º e IRRF13º (antecipado) Provento/Valor, sem Código de Cálculo. No campo "Fórmula valor" informar a fórmula de código A0015.

**• 5º Passo:** Realize o lançamento dos eventos 8001, 8002, 8003 e 8005 através do módulo:    
 

Visualização em Delphi: *Movimento* | *Folha de Pagamento* | *Lançamentos Automáticos* | *Grupo de Eventos*.   
 

Visualização em .Net: *Movimento* | *Folha de Pagamento* | *Lançamentos Automáticos* | *Grupo de* *Eventos.Net*.   
 

Nova MDI: Aba *Folha Mensal* | *Lançamentos* | *Grupo de Eventos.*

**PROCEDIMENTOS A SER REALIZADO NA COMPETÊNCIA DEZEMBRO (Somente para quem efetuou o pagamento integral antecipado)**

**6º Passo:** Lançar o evento 8004, através do módulo*:*    
 

Visualização em Delphi: *Movimento* | *Folha de Pagamento* | *Lançamentos Automáticos* | *Grupo de Eventos*.    
 

Visualização em .Net: *Movimento* | *Folha de Pagamento* | *Lançamentos Automáticos* | *Grupo de* *Eventos.Net*.    
 

Nova MDI: Aba *Folha Mensal* | *Lançamentos* | *Grupo de Eventos.*  
   
**7º Passo:** Na competência Dezembro deverá efetuar o processamento de 13º Salário normalmente através do módulo    
 

Visualização em Delphi: *Movimento* | *Folha de Pagamento* | *Lançamentos Automáticos* | *Décimo Terceiro* *Salário*  
 

Visualização em Delphi Maquina de Calulo: *Movimento* | *13º Salário (.NET)* |

Visualização Nova MDI: Aba *Folha Mensal* | *Calculo 13º* ]

**8º Passo:** Efetuar a geração do SEFIP e de todas as guias.

|  |
| --- |
| **Atenção!**   **O recolhimento do INSS de 13º salário e IRRF de 13º salário deve ocorrer em dezembro, pois a legislação de IRRF (texto abaixo) informa que o IRRF deve ser calculado no ato da quitação e na verdade a quitação só ocorre em dezembro, pois podem ocorrer diferenças salariais, diferenças de médias e até mesmo de tabelas de cálculo o que acarretaria problemas no cálculo da diferença de INSS e IRRF.**  **O INSS só é aceito no SEFIP da competência 13 (veja manual do SEFIP). Se recolhido anteriormente não será possível a geração deste SEFIP automaticamente na competência de dezembro.** **• Lembramos que, ao emitir a DIRF, o IRRF e o INSS do funcionário irá aparecer na competência Dezembro.** |

#### **○ Processamento – 2ª Parcela de 13º Salário (Mês de Dezembro)**

Acesse o módulo:   
 

Visualização em Delphi: *Movimento* | *Folha de Pagamento* | *Lançamentos Automáticos* | *Décimo Terceiro* *Salário*  
 

Visualização em Delphi Maquina de Cálculo: *Movimento* | *13º Salário (.NET)* | *Lançamento* Nova MDI: Aba *Folha Mensal* | *Cálculo 13º* ***Preenchimento dos campos:***

**Segunda parcela:** Marque este campo se a empresa for processar a 2ª parcela de 13º salário. Situações a observar:

* Funcionário comissionista, será efetuado o cálculo da média ou considerado o mínimo garantido do sindicato.

  Quando o funcionário tiver afastado por acidente de trabalho:

* Lançar um evento de Salário Pago na Previdência, (Desconto, Valor, com CC101), onde deverá ser informado o valor que o funcionário recebeu no período que esteve afastado (Lembrando que o valor do 13º Salário pago pela previdência deverá ser apurado junto ao funcionário).
* A empresa não poderá trabalhar com as médias discriminadas apenas no 13º Salário ou apenas no 13º Rescisão, pois afeta o cálculo de INSS de ambas as partes.
* Lançamento de pensão alimentícia poderá ser feito através dos códigos fixos, lembrando que o evento precisa ter o código de cálculo 120.

  Quando o funcionário possuir outro emprego:   Empresas que fazem o cálculo paralelo:

* Criar o Evento INSS 13º Outro Emprego (Base de Cálculo, Valor, Com CC144), informar o valor caso já tenha sido descontado na outra empresa o INSS. Caso contrário, deverá ser lançado o evento com CC83, onde o sistema efetuará a proporcionalização.
* Criar o Evento Base de INSS 13º outro emprego (Base de Cálculo, com CC83), informar o valor da Base de incidência de INSS do outro emprego para que seja proporcionalizado.

  Empresas que não fazem cálculo paralelo (proporcional nas duas empresas):

* Criar o Evento INSS 13º Outro Emprego (Base de Cálculo, Valor, Com CC182), informar o valor da base da INSS de 13º na outra empresa.
* O código de cálculo 83 será calculado automaticamente.

|  |
| --- |
| **Atenção!**   **No dia 20/12 deverá ser gerado SEFIP de 13º, marcando o campo "SEFIP para 13º salário", Informando o percentual de INSS recolhido pela empresa. Este SEFIP não gera recolhimento de FGTS, pois ele é utilizado apenas para declaração do valor de INSS de 13º salário que foi pago pela empresa na guia de GPS.** |

**Cálculo para funcionários que eram mensalistas e passaram a ser comissionistas** Nesse caso, o sistema calcula 13° salário somente a partir do mês que se tornou comissionista, por isso é necessário utilizar o roteiro.

***Cadastrar a consulta SQL:***  
 

Visualização em Delphi: *Utilitários* | *Consultas SQL*

Nova MDI: Aba *Gestão* | *Visões de dados*

Verifica qual o último mês que o funcionário recebeu dias trabalhados ou horas normais, ou seja, último mês como mensalista/horista.

**Código:** ULTIMOMES

**Título:** Ultimo mês que o funcionário recebeu dias trabalhados ou horas normais

**Texto:**

SELECT MAX(PFFINANC.MESCOMP) AS ULTIMOMES **FROM** PFFINANC, PEVENTO, PPARAM

**WHERE** PFFINANC.CODCOLIGADA=PEVENTO.CODCOLIGADA **AND** PPARAM.CODCOLIGADA=PFFINANC.CODCOLIGADA **AND** PEVENTO.CODIGO=PFFINANC.CODEVENTO **AND**PFFINANC.CHAPA=:FRM\_CHAPA **AND** (PEVENTO.CODIGOCALCULO='2' **OR** PEVENTO.CODIGOCALCULO='1') **AND** PFFINANC.ANOCOMP=PPARAM.ANOCOMP **AND**PFFINANC.CODCOLIGADA=:FRM\_COLIGADA **AND**

(**SELECT** PFFINANC.VALOR **WHERE** PEVENTO.CODIGOCALCULO='2')>0

**Fórmula para pagar 13° sobre os meses que o funcionário era mensalista:** Esta fórmula foi criada considerando para média o ano todo. Se o cliente deseja pagar média sobre 6 meses, por exemplo, a fórmula deve ser adaptada.

*Fórmula 1ª parcela:*

**Código:** 1parcela

**Título:** 1ª parcela

**Texto:**

EXECSQL('ULTIMOMES');   
DECL(MENSAL);

SE TFUNC='O' E EXECSQL('ULTIMOMES')>0 E MES=11 ENTAO

SETVAR(MENSAL,RESULTSQL('ULTIMOMES','ULTIMOMES')); (RANT(MTDATA(1,MENSAL,ANO))/12)\*((NROAVOS13+1)-(12-MENSAL))/2

SENAO 0

FIMSE

*Fórmula para o evento com C.C 102 :*

**Código:**2parcela

**Título:** 2ª parcela

**Texto:**

EXECSQL('ULTIMOMES');  
DECL(MENSAL);

SE TFUNC='O' E EXECSQL('ULTIMOMES')>0 E MES=12 ENTAO

SETVAR(MENSAL,RESULTSQL('ULTIMOMES','ULTIMOMES')); (RANT(MTDATA(1,MENSAL,ANO))/12)\*((NROAVOS13)-(12-MENSAL))/2

SENAO 0

FIMSE

**O usuário deverá lançar o 13° normalmente pelo módulo automático. O sistema pagará as verbas para todos os funcionários e também para o comissionista, incluindo as médias do ano todo.**

**Criar um evento com código de cálculo 9 e outro com código de cálculo 102, com a fórmula acima, para pagamento do valor referente aos meses que o funcionário era mensalista. Informar a fórmula no evento com C.C 102 somente após o pagamento da primeira parcela, pois a mesma interfere no cálculo.**

***Fórmula considerando os últimos 6 meses para o cálculo de 13° :***

**Código:** 1parcela

**Título:** 1ª parcela

**Texto:**

EXECSQL('ULTIMOMES');

DECL(MENSAL);

SE TFUNC='O' E RESULTSQL('ULTIMOMES','ULTIMOMES')>=5 E MES=11 ENTAO

SETVAR(MENSAL,RESULTSQL('ULTIMOMES','ULTIMOMES')); (RANT(MTDATA(1,MENSAL,ANO))/12)((NROAVOS13+1)(12(MENSAL-1)))/2

SENAO 0

FIMSE

***Fórmula para o calculo da 2ª parcela:***

**Código:** 2parcela

**Título:** 2ª parcela

**Texto:**

EXECSQL('ULTIMOMES');

DECL(MENSAL);

SE TFUNC='O' E RESULTSQL('ULTIMOMES','ULTIMOMES')>=5 E MES=12 ENTAO

SETVAR(MENSAL,RESULTSQL('ULTIMOMES','ULTIMOMES')); (RANT(MTDATA(1,MENSAL,ANO))/12)((NROAVOS13)-(12-MENSAL+2))/2

SENAO 0

FIMSE

**Exemplo da fórmula considerando 6 últimos meses:**

Funcionário recebia 500,00 até o mês 9, deixou de ser mensalista e passou a ser comissionista. O cálculo será na competência 11, considerando do mês 6 ao mês 11: (500/6) \* 4 = 333,33 1ª parcela : 166,66 Competência 12, considerando do mês 7 ao mês 12 : (500/6) \* 3 = 250,00 2ª parcela : 125,00 O valor de 1ª e 2ª parcela sobre a comissão será pago no evento normal.

**\*Como é feito o Cálculo de Médias** As médias são utilizadas nos cálculos de 13º salário, férias, aviso prévio e licença maternidade. Para que o sistema faça o cálculo de médias é preciso que a parametrização esteja feita de forma correta.

Média (Estatística) - É o número obtido somando-se os valores medidos e dividindo-se a soma obtida pelo número de medições. É usada como síntese, valor representativo do conjunto de dados. É particularmente útil em distribuições simétricas. É a região da distribuição de freqüências onde se concentra a maioria das observações.

**Exemplo de cálculo de média:** Salário R$ 1257,14 Jornada Mensal 220:00 Salário Hora: Salário/Jornada => 1257,14 / 220 = 5,7142 Hora Extra 75% = 5,7142 + 75% => 5,7142\*1,75 = R$ 10,00

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| *TOTVS Folha de Pagamento* |  |  |  |  | 28 |  |  |  |
| *Nº 0000xx\_GDP-RH* |  |  |  |  |  |  |  |  |
| **Mês e ano** | **Evento** | **Nome** |  |  |  |  | **Horas** | **Valor** |
| 02/2010 | 0157 | Horas extras 75% |  |  |  |  | 10:00 | R$ 100,00 |
| 03/2010 | 0157 | Horas extras 75% |  |  |  |  | 10:00 | R$ 100,00 |
| 05/2010 | 0157 | Horas extras 75% |  |  |  |  | 20:00 | R$ 200,00 |
| 07/2010 | 0157 | Horas extras 75% |  |  |  |  | 10:00 | R$ 100,00 |
| 10/2010 | 0157 | Horas extras 75% |  |  |  |  | 10:00 | R$ 100,00 |
|  |  |  |  |  |  |  |

Numero de meses com horas extras = 5 Soma de horas 60:00.

Soma do dos valores R$ 600,00

**Média do período de 01/01/2010 a 31/12/2010**

Número de meses do período acima: 12 meses

Salário atual R$ 2200,00

Jornada Mensal 220:00 / Salário Hora: Salário/Jornada => 2200,00 / 220 = R$ 10,00

Hora Extra 75% = 10,00 + 75% => 10,00 \* 1,75 = R$ 17,50

**Tipos de média** Cálculo da média por valor: Soma dos valores encontrados no período / número de meses analisados R$ 600,00 / 12 = 50,00

**Cálculo da média por horas** Soma das horas encontradas no período / número de meses analisados 60:00h / 12 = 5:00h Médias das horas multiplicado pelo valor das horas com seu percentual, atualmente 5:00h \* R$ 17,50 = R$ 87,50. Veja que a média por horas considera o salário atual.

**Observações para admitidos em Janeiro e para afastados durante o ano**

* Para funcionários admitidos até 17 de janeiro (inclusive), o Sistema calculará metade (50%) do salário contratual percebido no "Mês Anterior" ao do pagamento. Para funcionários admitidos após 17 de janeiro, o Sistema calculará o número de avos a que o funcionário tem direito (da admissão até o mês anterior ao pagamento) e pagará a metade do total encontrado.

* Para funcionários afastados por acidente de trabalho, o 13º será pago integralmente. Para descontar o 13º pago pela previdência, deverá ser lançado na movimentação do mês de dezembro, o evento de desconto com CC 101, com o valor de 13º pago pela previdência.

* O evento com CC 101 é um evento de Desconto tipo Valor. O valor informado neste código de calculo será deduzido também da base de calculo do 13º salário para o cálculo do IRRF e INSS.

* Para funcionários afastados pela previdência, o 13º será pago somente sobre os avos aos quais o funcionário terá direito. As incidências do FGTS, INSS, IRRF serão somente sobre o valor pago pelo sistema ao funcionário.
* Para funcionárias que tiveram dias de afastamento por licença maternidade durante o ano o sistema irá calcular o valor normalmente (como é calculado para os demais funcionários), porém na guia de INSS e no SEFIP os valores referente ao valor do 13º salário pago pela previdência serão calculados da seguinte forma: Soma dos eventos de CC 102 (ou CC48 caso venha a ser rescisão) / nº de avos que estão sendo pagos / 30 \* Número de dias de afastamento dentro do ano. Estes valores sobre os dias de afastamento por licença maternidade não aparecerão na movimentação e nem na folha analítica, para que seja impresso na folha analítica deverá ser criada uma fórmula.

**Informações Legais:** [ **DECRETO Nº 57.155, DE 3 DE NOVEMBRO DE 1965**|[{+}](http://legislacao.planalto.gov.br/legislacao.nsf/Viw_Identificacao/DEC%2057.155-1965?OpenDocument)<http://legislacao.planalto.gov.br/legislacao.nsf/Viw_Identificacao/DEC%2057.155-1965?OpenDocument+>]**.** [ [{\_}{+}](http://www.planalto.gov.br/CCIVIL/decreto/1950-1969/D57155.ht+_)<http://www.planalto.gov.br/CCIVIL/decreto/1950-1969/D57155.ht+_+_>*|*[{\_}{+}](http://www.planalto.gov.br/CCIVIL/decreto/1950-1969/D57155.htm)<http://www.planalto.gov.br/CCIVIL/decreto/1950-1969/D57155.htm+_>*]*m

**LEI No 4.090, DE 13 DE JULHO DE 1962.** [ [{+}](http://www.planalto.gov.br/ccivil/leis/L4090.ht+)<http://www.planalto.gov.br/ccivil/leis/L4090.ht++>|[{+}](http://www.planalto.gov.br/ccivil/leis/L4090.htm)<http://www.planalto.gov.br/ccivil/leis/L4090.htm+>]m

**LEI No 4.749, DE 12 DE AGOSTO DE 1965**|[{+}](http://legislacao.planalto.gov.br/legislacao.nsf/Viw_Identificacao/lei%204.749-1965?OpenDocument)<http://legislacao.planalto.gov.br/legislacao.nsf/Viw_Identificacao/lei%204.749-1965?OpenDocument+>]**.** [ [{+}](http://www.planalto.gov.br/ccivil/Leis/L4749.ht+)<http://www.planalto.gov.br/ccivil/Leis/L4749.ht++>[}](http://www.planalto.gov.br/ccivil/Leis/L4749.htm)<http://www.planalto.gov.br/ccivil/Leis/L4749.htm+>]m

**LEI Nº 7.855, DE 24 DE OUTUBRO DE 1989.** [ [{+}](http://www.planalto.gov.br/ccivil/Leis/L7855.htm#art+)<http://www.planalto.gov.br/ccivil/Leis/L7855.htm#art++>|[{+}](http://www.planalto.gov.br/ccivil/Leis/L7855.htm#art3)[http://www.planalto.gov.br/ccivil/Leis/L7855.htm#art3](http://www.planalto.gov.br/ccivil/Leis/L7855.htm#art3+)

**LEI DELEGADA Nº 13, DE 27 DE AGOSTO DE 1992.** [ [{+}](http://www.planalto.gov.br/ccivil/Leis/LDL/Ldl13.ht+)<http://www.planalto.gov.br/ccivil/Leis/LDL/Ldl13.ht++>|[{+}](http://www.planalto.gov.br/ccivil/Leis/LDL/Ldl13.htm)[http://www.planalto.gov.br/ccivil/Leis/LDL/Ldl13.htm](http://www.planalto.gov.br/ccivil/Leis/LDL/Ldl13.htm+)

**IMPOSTO DE RENDA SOBRE O 13º SALÁRIO.** [ [{+}](http://www.receita.fazenda.gov.br/PessoaJuridica/DIRF/Mafon2003/escladicionais.ht+)<http://www.receita.fazenda.gov.br/PessoaJuridica/DIRF/Mafon2003/escladicionais.ht++>|[{+}](http://www.receita.fazenda.gov.br/PessoaJuridica/DIRF/Mafon2003/escladicionais.htm#Gratifica%E7%E3o%20de%20Natal%20(13%BA%20SAL%C1RIO))[http://www.receita.fazenda.gov.br/PessoaJuridica/DIRF/Mafon2003/escladicionais.htm#Gratifica%E7%E3o%20de%20Natal%20(13%BA%20SAL%C1RIO)](http://www.receita.fazenda.gov.br/PessoaJuridica/DIRF/Mafon2003/escladicionais.htm#Gratifica%E7%E3o%20de%20Natal%20(13%BA%20SAL%C1RIO)+)
