---
content_hash: 5a40e3c3c1b09f6bab0031d0b5634244685dfb700d02798239b953cd33403fe7
fetched_at: '2026-06-29T00:11:48.529671+00:00'
page_id: '82477730'
product: rm
source: tdn-rm
title: RMFIS00004_Controle de Diferimento
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00004_Controle+de+Diferimento
version: 6
---

**Definição do Processo**

---

O objetivo deste documento é oferecer uma visão geral a respeito das implementações realizadas no **TOTVS Gestão Fiscal** e demais sistemas para a geração das informações de Diferimento no arquivo digital do **EFD Contribuições**, oferecendo aos Clientes da Linha **RM** automatismo e agilidade no processo.

**Regras Gerais**

---

O Diferimento dos de PIS e COFINS já é tratado atualmente no TOTVS Gestão Fiscal, na apuração do PIS\PASEP e COFINS, porém, o mesmo é feito com base na separação por Centro de Custo. Todas as informações a respeito de diferimento dos tributos são segregadas por Centro de Custo. Com a EFD Contribuições, surgiu a necessidade de identificar estas operações diferidas por contratante do serviço.

Estas informações devem ser apresentadas nos seguintes registros da EFD Contribuições:

I. REGISTRO **M230**: informações adicionais de diferimento – PIS;

II. REGISTRO **M300**: contribuição de PIS/PASEP  diferida em períodos anteriores – valores a pagar no período – PIS;

III. REGISTRO **M630**: informações adicionais de diferimento – COFINS;

IV. REGISTRO **M700**: contribuição de Cofins diferida em períodos anteriores – valores a pagar no período – COFINS;

**Parametrização Necessária**

---

**Habilitar o sistema pera controle do Diferimento**

Acesse o Menu: **Opções | Parâmetros | Gerais Tabelas | (Avançar) | 03.01.06 – PIS | (Avançar)| Flag “Controla****Diferimento”**

---

**Campo Complementar**

Deve ser criado um campo complementar para indicar o “Código da Contribuição Social”, na tabela DITEM (Itens do lançamento) da seguinte forma:

• Nome Coluna: **CODCONTRIBSOCIAL**  
• Descrição: Código da Contribuição Social  
• Tipo: Alfanumérico  
• Tamanho: 2

**Obs**: Este campo será utilizado no registro **M300** – Campo 02 (**COD\_CONT**), para preenchimento, consulte o Guia Prático.

O campo Natureza do Crédito Diferido (M300) é gerada da seguinte maneira:

**Se** a Alíquota do PIS for 0,65% ou 1,65% o campo é preenchido com 01

**Se** a Alíquota da COFINS for 3,00% ou 7,60% o campo é preenchido com 01

**Se** a Alíquota do PIS for 0 e Alíquota por Valor for maior que 0 o campo é preenchido com 03

**Se** a Alíquota do COFINS for 0 e Alíquota por Valor for maior que 0 o campo é preenchido com 03

**Se** a Alíquota não se enquadrar em nenhuma dos valores acima o campo será será preenchido com 02

**O valor 04 - Crédito presumido Agroindústria não será gerado.**

**Calculo do Diferimento por Contratante**

---

Serão considerados os Lançamentos Fiscais associados a Clientes/Fornecedores  que sejam  Órgão Público.  Para verificar se seu Cli/For é órgão publico acesse o cadastro de Cliente/Fornecedor na **Aba Dados Fiscais | Sub Aba Classificação**

**Atenção**: Para a correta execução do processo, é necessário que os Movimentos criados no TOTVS Gestão de Estoque, Compras e Faturamento estejam integrados ao TOTVS Gestão Financeira e escriturados para o TOTVS Gestão Fiscal ou, caso não seja utilizado o TOTVS Gestão de Estoque, que os Lançamentos Fiscais criados no TOTVS Gestão Fiscal estejam integrados ao TOTVS Gestão Financeira. O processo irá efetuar todos os cálculos e armazenar as informações agrupadas e segregadas por Contratante e Código de Tipo de Crédito.

**Em hipótese nenhuma este controle será feito sem a integração com o TOTVS Gestão Financeira.**

**Cálculo do Valor Realizado/Diferido do mês de apuração:**

**a)** Serão selecionados os Lançamentos Fiscais de Saída emitidos no mês informado para a execução do processo, que possuam os tributos PIS ou COFINS. Será considerada a Data de Emissão do  
Lançamento Fiscal. O “Valor Contábil” destes lançamentos será armazenado como “Total de Vendas no período”;

**b)** Localizamos os Lançamentos Financeiros referentes aos Lançamentos Fiscais selecionados no item **A.**Totalizamos o “Valor Original” dos Lançamentos baixados. Caso o Lançamento tenha tido Baixa Parcial, será somado o “Valor Original” do Lançamento baixado no período menos o “Valor Original” do lançamento gerado na baixa parcial. Isto é feito pois os Descontos e Acréscimos financeiros não devem  
entrar no cálculo;

**c)** Verificamos a proporção dos Lançamentos Baixados (item **B**) em relação à todos os Lançamentos emitidos (item **A**);

**d)** Esta proporção será aplicada sobre o “Total de Vendas no período”. A diferença entre “Total de Vendas no Período” e o resultado da aplicação da proporção será armazenado como “Total de Vendas NÃO  
Recebidas no Período”;

**e)** Totalizamos os valores dos tributos PIS e COFINS dos Lançamentos Fiscais de Saída emitidos no mês informado para execução do processo. Estes valores serão armazenados, respectivamente como “Total de PIS no Período” e “Total de COFINS no Período”;

**f)** A proporção calculada no item c será aplicada ao valor “Total de PIS no Período”. A diferença entre “Total de PIS no Período” e o resultado da aplicação da proporção será armazenado como “Total de PIS  
Diferido no Período”;

**g)** A proporção calculada no item c será aplicada aos valores “Total de COFINS no Período”. A diferença entre “Total de COFINS no Período” e o resultado da aplicação da proporção será armazenado como  
“Total de COFINS Diferido no Período”;

**2. Calculo do Valor do Crédito Diferido**

---

**A.** Para identificação do Total de Crédito do Período serão selecionados os Lançamentos Fiscais de Entrada, emitidos no mês informado para execução do processo, que tenham os Tributos PIS e/ou  
COFINS, com CST representativo de crédito. Os valores dos tributos PIS e COFINS destes Lançamentos serão totalizados e armazenados respectivamente como “Total de Crédito PIS no Período” e “Total de Crédito COFINS no Período”;

**B.** Como não há uma relação direta entre os créditos e as vendas, para conseguir identificar o quanto deste Total de Créditos é referente a determinado Contratante, teremos que descobrir qual a  
proporção entre total de vendas e as vendas que foram realizadas para o Contratante. Esta proporção será aplicada aos Totais de Crédito calculados no item a e o resultado será armazenado,  
por contratante, como “Total de Crédito PIS no Período” e “Total de Crédito COFINS no Período”;

**Exemplo:**

Total de Vendas no Período (todos os Contratantes): R$ 200.000,00

Total de Vendas no Período (Contratante **XPTO**): R$ 20.000,00

% do Total de Vendas do Contratante **XPTO** sobre o Total de Vendas Geral: 10%

Total de Créditos do Período: R$ 100.000,00

Total de Créditos do Contratante **XPTO**: R$100.000,00 X 10% = R$ 10.000,00

**C.** Para identificação do Crédito a ser diferido aplicaremos a proporção calculada no item 1.c sobre o total de Créditos do Período. O resultado será armazenado como “Total de Crédito PIS Diferido no  
Período” e “Total de Crédito COFINS Diferido no Período”;

**Exemplo:**

Total de Vendas no Período: R$ 200.000,00

Total de Vendas Recebidas no Período: R$ 150.000,00

% do Total de Vendas Recebidas sobre o Total de Vendas: 75%

Total de Créditos do Período: R$ 100.000,00

Total de Créditos Diferidos: 100.000,00 – (100.000,00 X 75%) = 25.000,00

**3. Cálculo do Valor Diferido em Períodos anteriores**

**a)** Serão selecionados os Lançamentos Fiscais de Saída emitidos em meses anteriores ao mês informado para a execução do processo, que possuam os tributos PIS ou COFINS e cujo Lançamento Financeiro associado tenha sido Baixado no mês informado para a execução do processo. Estes Lançamentos serão agrupados pelas seguintes informações:

**I**. Código da contribuição social

**II**. Natureza do Crédito Diferido (identificada através do CST do tributo);

**III**. Período de apuração da contribuição social Fiscal);

**IV**. Data de recebimento da receita (Baixa do Lançamento Financeiro);

**V**. Tributo (PIS ou COFINS).

**b)** Para cada conjunto de Lançamentos selecionado, serão armazenados, além dos campos indicados acima, os Valores Totais de PIS e COFINS, para a geração do campo “Valor da Contribuição Apurada,  
diferida em períodos anteriores”, dos registros **M300** e **M700**;

**c)** Para identificação do “Valor do Crédito a Descontar vinculado à contribuição diferida os valores de “Total de Vendas” e “Total de Créditos” já armazenados anteriormente para o Período de  
apuração do conjunto de trabalho em questão. Para conseguir identificar o quanto deste Total de Créditos é referente ao agrupamento que está sendo trabalhado entre total de vendas e as vendas deste agrupamento. Esta proporção será aplicada ao “Total de Créditos” o resultado será armazenado, por grupo de trabalho, como “Valor do Crédito a Descontar PIS” e “Valor do Crédito a Descontar COFINS”;

**Como fazer o cálculo no sistema**

---

Acesse o período de apuração em questão

Clique em Processos | Calculo dos Valores Diferimento e o cálculo será executado

Em seguida clique em Anexos | Controle de Diferimento

Após a execução, o sistema irá criar uma linha por Tipo de Credito informado no lançamento Fiscal:

Editando o  registro pode se verificar os valores gerados

Acessando, dentro do registro, o menu **Anexos** temos as informações de detalhamento do Diferimento em períodos anteriores

**Geração da Rotina(registros Gerados):**

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M200 |  |  |  |  |  |  |  |  |  |  |  |  |

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M210 |  |  |  | 0,00 |  |  |  |  |  | 9,90 | 0,00 |  |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| M230 | 22678197000155 | 800,00 | 600,00 | 9,90 | 0,00 |  |

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M600 |  |  |  |  |  |  |  |  |  |  |  |  |

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M610 |  |  |  | 7,60 |  |  |  |  |  | 45,90 | 0,00 |  |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| M630 | 22678197000155 | 800,00 | 600,00 | 45,90 | 0,00 |  |

|  |  |
| --- | --- |
| M990 | 8 |

**Figura 1 - Os valores expressados nesta planilha não são os mesmos utilizados nos prints (exemplos) acima.**

|  |  |
| --- | --- |
|  | **Para maiores informações:**   [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.CadDiferimento.aspx)  **COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****    **Canais de Atendimento:**  **Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal) |
