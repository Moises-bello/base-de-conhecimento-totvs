---
content_hash: 9fe459d916f39290d9d6eaf2da2993a1b0c67289de409969233433401f4e1fe2
fetched_at: '2026-06-29T00:09:18.574984+00:00'
page_id: '421388726'
product: rm
source: tdn-rm
title: FIN - Ajuste a Valor Presente | AVP
type: documentation
url: https://tdn.totvs.com/display/LRM/FIN+-+Ajuste+a+Valor+Presente+%7C+AVP
version: 50
---

Esta página detalha os passos necessários para realizar o cálculo de Ajuste a Valor Presente (AVP) no TOTVS Gestão Financeira - Linha RM.

#f5f5f5#363636Ajuste a Valor Presente - AVP

## **Conteúdo**

32trueConteúdo

## **01. Introdução**

O Ajuste a Valor Presente é um processo para descapitalizar um montante futuro, retirando os juros compostos sobre ele aplicado.  
Tem por objetivo viabilizar a aplicação de dispositivos da lei das S/A´s nº 11.638, promulgada em Dezembro de 2007, nos arts. 183 e 184, que estabelece que os elementos do ativo e do passivo exigível decorrentes de operações de longo prazo deverão ser ajustados ao valor presente, sendo os demais, de curto prazo, ajustados quando houver efeito relevante.   
  
*Redação dada pela Lei nº 11.638, de 2007:*

* *Art. 183, VIII – os elementos do ativo decorrentes de operações de longo prazo serão ajustados a valor presente, sendo os demais ajustados quando houver efeito relevante.*
* *Art. 184, III – as obrigações, encargos e riscos classificados no passivo exigível a longo prazo serão ajustados ao seu valor presente, sendo os demais ajustados quando houver efeito relevante.*

O objetivo de ajustar o valor de um direito ou uma obrigação é demonstrar o valor presente de um fluxo de caixa futuro.

## **02. Cadastros**

### **Eventos Contábeis**

*BackOffice | Gestão Financeira | Cadastros | Contabilidade | Evento Contábil*

Por se tratar de um princípio contábil, no Backoffice RM é necessário realizar o cadastro de 2 eventos que serão utilizados para gerar as operações contábeis.   
No item do evento contábil estarão disponíveis três campos: Valor Original (Valor calculado com Valor Original do lançamento + Valores Opcionais configurados + Valores de Integração configurados), Valor Presente e Juros AVP.

**1º Evento:** Este evento será utilizado para contabilizar a operação na data da inclusão e a **Provisão do AVP**.

falseExemplo

Vamos usar como exemplo uma venda de serviço com as seguintes informações:

Nota Fiscal:       R$3.102,00  
Valo Presente:   R$3.078,22  
Juros:                 R$    23,78

Neste caso, **debitamos** o **valor da venda** de serviço em **Cliente**, e **creditamos** o **valor presente** como **Receita**  e o **valor de juros** como **AVP**.

|  |  | Débito | Crédito |
| --- | --- | --- | --- |
| D | Clientes | R$3.102,00 |  |
| C | Receita de Serviço |  | R$3.078,22 |
| C | AVP |  | R$23,78 |

**2º Evento:** Este evento será utilizado para realizar a **Reversão** mês a mês de valores de juros ora apropriado como AVP, agora como receita ou despesa.

falseExemplo

Seguindo o mesmo exemplo que provisionamos acima, vamos considerar que o cálculo de juros do 1º mês foi no valor de R$6,85  
Neste caso, **debitamos** o **valor de juros** do AVP provisionado e **creditamos** o **mesmo valor** como **receita financeira**.

|  |  | Débito | Crédito |
| --- | --- | --- | --- |
| D | AVP | R$6,85 |  |
| C | Receita Financeira |  | R$6,85 |

Esta apropriação será realizada mês a mês até que o valor de juros provisionado seja revertido totalmente como receita ou despesa.

**Para os cenários onde é feito o Cálculo do AVP para Recebimento com Cartão**

A partir da versão 12.1.2402, temos a possibilidade de calcular o AVP para Recebimento com Cartão. Para o correto funcionamento do processo considerando esse novo contexto, será necessário configurar eventos contábeis distintos dos que temos cadastrados para o AVP de Lançamentos para a contabilização dos valores de AVP para Cartão.

Para isso, acesse *BackOffice | Gestão Financeira | Cadastros | Contabilidade | Evento Contábil* e realize o cadastro dos novos eventos.

Os eventos específicos do AVP para recebimento com cartão devem nos campos "*Buscar Filial/Departamento em*" e "*Buscar Centro de Custo em*" considerar como opção o "Extrato", que é a entidade que controlará o AVP de recebimento com cartão e de onde serão considerados os defaults para a contabilização.

Bem como, nos itens de evento cadastrados na aba "Itens Evento" o campo Aplicar deve ter selecionada a nova opção específica "AVP Extrato (Ajuste a Valor Presente)".

Centro de custo obrigatório na contabilização

Caso o parâmetro "Centro de Custo obrigatório" esteja habilitado no TOTVS Gestão Contábil (em *Ambiente | Configuração | Parâmetros | TOTVS Gestão Contábil | Lançamentos | Manutenção de Lançamentos | Etapa 9 - Manutenção dos Lançamentos Contábeis)*, é importante estar atento ao cadastro do evento contábil para que esteja definido um valor para o campo "Aplicar Centro de Custo em". Se esse campo não estiver configurado apresentará erro na contabilização do processo do AVP e os registros não serão gerados.

Além disso, no extrato referente ao Recebimento com Cartão que deva ser considerado no processamento do AVP, precisa ser informado o Centro de Custo para que ele seja identificado pela rotina de contabilização do processo do AVP e os registros sejam gerados e contabilizados corretamente.

Para habilitar AVP de Recebimento com Cartão

Para que o evento contábil possa ser gravado com sucesso, considerando a opção de Extrato, é necessário executar o atualizador da versão a partir da release 12.1.2402.

Para mais detalhes de como parametrizar o AVP de Recebimento com Cartão, ver o tópico 03.

### **Moedas**

*BackOffice | Gestão Financeira | Movimentações Bancárias | Moedas | Moedas e Índices*

O Ajuste a Valor Presente será realizado mediante descontos que considerem os **juros embutidos pré-fixados** com base em uma **taxa fixa.**

No cadastro de Moedas e índices, deve-se incluir um índice específico para o cálculo de AVP.

falseObservação

O sistema irá considerar a **data de emissão** ou **data da competência** (de acordo com a data base parametrizada) dos títulos como base de busca da cotação que será utilizada no processo. Caso não encontre uma cotação no mesmo dia, o sistema irá buscar a primeira data anterior.

### **Valores Opcionais**

*BackOffice | Gestão Financeira | Ambientes | Parâmetros | TOTVS Gestão Financeira*

O Ajuste a Valor Presente irá usar os valores opcionais parametrizados para compor o AVP no processo de cálculo juntamente com o Valor Original do lançamento financeiro. Mais informações sobre os valores opcionais acesse .

### **Valores de Integração**

*BackOffice | Gestão Financeira | Cadastros| Valores de Integração*

O Ajuste a Valor Presente irá usar os valores de integração parametrizados para compor o AVP no processo de cálculo juntamente com o Valor Original do lançamento financeiro. Mais informações sobre os Valores de Integração acesse .

## **03. Parametrização**

BackOffice | Gestão Financeira | Ambiente | Configuração | Parâmetros | TOTVS Gestão Financeira | Integração Contábil | Ajuste a Valor Presente

Temos disponível a parametrização de dois tipos de AVP. Abaixo iremos agrupar as parametrizações que impactam diretamente em cada um dos cálculos.

falseLançamento Financeiro

Parametrização referente ao AVP dos lançamentos financeiros em aberto, referente a títulos A Pagar e A Receber

**Evento Contábil | Provisão e Reversão**: Informar os eventos cadastrados no tópico 2.

**Indexador**: Informar o índice cadastrado no tópico 2.

**Valor Relevante:** Somente os lançamentos financeiros que tiverem ovalor calculado (Valor Original + Valores Opcionais + Valores de Integração)maior ou igual ao valor relevante informado neste campo serão objetos de cálculo do AVP.  
Observação: O cálculo do Valor Relevante não usa o Valor Líquido, mas sim o cálculo indicado acima (Valor Original + Valores Opcionais + Valores de Integração).

**Dias longo prazo:** Número de dias considerado pela empresa como uma operação de longo prazo.   
Exemplo: Se informado 100, todos os títulos que tiverem 100 ou mais dias entre a data de emissão ou data de competência e a data de vencimento são considerados como longo prazo e serão objetos de cálculo de AVP.

**Tabela que define o AVP:** A tabela definida neste parâmetro será utilizada para filtrar os lançamentos que terão cálculo de AVP.

* Tipo de Documento: será apresentada a opção "Usar Ajuste a Valor Presente" em Parâmetros no cadastro de tipo de documento.   
  Apenas lançamentos com tipo de documentos com esta opção marcada serão objetos de cálculo do AVP.

* Cliente/Fornecedor: será apresentada a opção "Usar Ajuste a Valor Presente" em Dados Adicionais no cadastro de cliente/fornecedor.   
  Apenas lançamentos de clientes/fornecedores com esta opção marcada serão objetos de cálculo do AVP.

**Data base do cálculo do AVP:**  A data base definida nesse parâmetro será utilizada para realização do cálculo do valor presente, assim como para a busca da cotação e para definir se um título é de longo prazo.

Caso esteja parametrizada como "Data de competência", serão considerados para o cálculo do AVP:

* o dia primeiro do mês/ano de competência definido no lançamento financeiro;
* a data de emissão, caso o mês/ano de competência não esteja informado no lançamento financeiro.
* lançamentos com data de vencimento maior ou igual à data de competência.
falseExtrato de Caixa

Parametrização para o cálculo do AVP dos extratos de caixa não compensados, referente ao recebimento de cartão de crédito.

**Calcular AVP para recebimento de cartão**: Esta opção permite que se calcule o AVP para os recebimentos através de cartão de crédito.

**Evento Contábil | Provisão e Reversão de cartão**: Informar os eventos cadastrados no tópico 2.

**Valor Relevante:** Somente os extratos com valor maior ou igual ao valor relevante informado neste campo serão objetos de cálculo do AVP.  
Observação: O valor considerado é individual de cada extrato gerado (parcela), e não do pagamento total do cartão.

**Dias longo prazo:** Número de dias considerados pela empresa como uma operação de longo prazo.   
Exemplo: Se informado 100, todos os extratos que tiverem 100 ou mais dias entre a data do extrato e a data de vencimento do extrato serão considerados como longo prazo e serão objetos de cálculo de AVP.

É considerada sempre a data do extrato gerado na baixa com cartão.

Importante

Os eventos utilizados para contabilização do AVP de lançamentos financeiros devem ser diferentes dos eventos utilizados para a contabilização do AVP dos extratos de caixa.

Ver detalhes no tópico 2

*BackOffice | Gestão Financeira | Ambiente | Configuração | Parâmetros | TOTVS Gestão Financeira | Integração Contábil | Lote Contábil*

Devem ser cadastrados e informados lotes contábeis que serão usados como default para a inclusão e o estorno dos lançamentos contábeis de AVP.

## **04. Processo de AVP**

*BackOffice | Gestão Financeira | Operações Financeiras | Ajuste a Valor Presente*

O processamento de AVP pode ser executado conforme a necessidade de registro destes juros.  
A contabilização da provisão, reversão e respectivos estornos dos Juros de AVP será realizada conforme os eventos contábeis parametrizados.

Orientações

Para atender as exigências de provisões e apropriações mensais, sugerimos a execução do processo mensalmente, informando o período da seguinte forma:

**Data Inicial**: Data de quando o processo de AVP foi iniciado na empresa. Importante que esta data seja anterior à data de emissão/data de competência dos títulos que serão objetos de cálculo do AVP.

**Data Final**: O último dia do mês que está sendo processado o AVP.

**Exemplo**: A empresa decidiu que todos os títulos emitidos a partir de Janeiro/2023 serão objetos de cálculo do AVP.

Para o cálculo do AVP em **Janeiro/2023**, executar o processo com o período: **01/01/2023** a **31/01/2023**.

Para o cálculo do AVP em **Fevereiro/2023**, executar o processo com o período: **01/01/2023** a **28/02/2023.**

Para o cálculo do AVP em **Março/2023**, executar o processo com o período: **01/01/2023 a 31/03/2023**, e assim sucessivamente. 

O processo pode ser executado de forma retroativa, desde que as datas sejam preenchidas corretamente, conforme exemplo acima.

Será realizado o registro e contabilização para todos os lançamentos financeiros que atendem às condições abaixo:

* Data de emissão/data de competência dentro do período informado na chamada do processo;
* Tipo contábil: "Contábil" ou "Baixa contábil";
* Número de dias entre a data de emissão/data de competência e a data de vencimento maior ou igual ao parâmetro "Dias Longo Prazo". Se a data de vencimento for anterior à data de emissão/competência, o lançamento não é considerado;
* Valor calculado (Original + Opcionais + Integração) maior ou igual ao parâmetro "Valor Relevante" ou Lançamentos com Status de AVP diferente de "Revertido totalmente" e "Não calculado" e data de emissão/data de competência maior que a data final informada.

No caso dos recebimentos via cartão de crédito, as seguintes condições devem ser respeitadas:

* Data do extrato dentro do período informado na chamada do processo;
* Extrato gerado a partir da baixa com meio de pagamento do tipo "Cartão";
* Extrato gerado a partir de lançamentos do tipo contábil "Contábil", "Baixa Contábil" ou "Baixa a Contabilizar";
* Valor do extrato maior ou igual ao parâmetro "Valor Relevante" ou extratos com Status de AVP diferente de "Revertido totalmente" e "Não calculado" e data maior que a data final informada.
* Número de dias entre a data do extrato e a data de vencimento do extrato maior ou igual ao parâmetro "Dias Longo Prazo".

Importante

No cálculo do AVP para recebimento do cartão, a data de vencimento do extrato é essencial. No sistema ela é preenchida nos seguintes casos:  
 Recebimento via TEF: sempre será preenchida  
 Recebimento via POS: será preenchida quando os dados do cartão forem preenchidos.

falseObservação

Período informado para processamento será consistido com o período contábil e com a data de fechamento parametrizados no menu *Opções | Parâmetros | TOTVS Gestão Financeira | Integração Contábil | Lançamentos Contábeis | Período Contábil.*

Após a execução do processo, os registros de AVP podem ser visualizados através da edição do lançamento financeiro (menu Anexos | Ajuste a Valor Presente). Para os recebimentos por cartão de crédito, os registros de AVP ficam disponíveis na edição de extratos de caixa (menu Anexos | Ajuste a Valor Presente).  
À medida que operações forem realizadas com o lançamento financeiro e o cálculo de AVP for processado, estes registros podem ter seus respectivos status alterados para:

* Calculado: operação teve o cálculo de provisão de AVP
* Revertido Parcialmente: operação teve o AVP parcialmente revertido, pois o último processo de AVP executado foi anterior a data de vencimento
* Revertido Totalmente: operação teve o AVP totalmente revertido, pois o último processo de AVP executado foi no mesmo mês da data de vencimento
* Estornado: operação sofreu alterações que estornaram o AVP

Editando os registros, e clicando no botão Contabilização, pode-se visualizar a respectiva contabilização.

falseObservações

Em situações onde a contabilização do AVP não for gerada porque o juros calculado no período for R$0,00, será gerado um registro de AVP e essa informação será exibida no log do processo.

O botão "Contabilização" ficará desabilitado quando o registro estiver estornado ou no caso acima, onde a contabilização não é gerada.

## **05. Cálculos**

### **Provisão do AVP**

* A provisão, como o próprio nome diz, provisiona o valor de **juros total** de AVP da operação, calculado pela diferença entre o **Valor Presente** e o **Valor Futuro,** através da fórmula **Juros AVP = VF – VP**
* A provisão do AVP será realizada para os lançamentos que estiverem com status AVP como "Não Calculado" ou "Estornado", na data de emissão/data de competência do lançamento.
* A provisão segue o regime de competência, e irá ocorrer na data de emissão/data de competência do título. Para isso, o período de contabilidade prevista estar aberto nesta data.
* O status será atualizado para "Calculado'.

### **Reversão do AVP**

* A reversão é a **apropriação** do **juros total provisionado do AVP** como **receita** ou **despesa** ao longo do tempo (mensalmente), calculado pela diferença entre o **Valor Presente atua**l e o **Valor Presente do Período anterior,** através da fórmula **Juros AVP = VP – VP anterior**
* A reversão do AVP será realizada para os lançamentos que estiverem com status AVP como "Calculado" ou "Revertido Parcialmente".
* O status será atualizado para "Revertido totalmente" ou "Revertido parcialmente".

### **Valor Presente**

Para os dois cálculos acima precisamos conhecer o **Valor Presente**.

Valor Presente é o **valor atual** de pagamentos futuros **descontados** a uma taxa de **juros** do custo do dinheiro do tempo.

O **cálculo** é realizado a partir da fórmula **VP = VF / (1+i)^n**

Onde:  
**VP** = Valor Presente.  
**n** = número de dias corridos entre a data de emissão/data de competência e a data de vencimento do lançamento.\*\*  
**i** = taxa de juros (indexador informado nas parametrizações). Caso não exista cotação para o mesmo dia da data de emissão/data de competência do título, o sistema irá buscar a primeira data anterior.  
**VF =** Valor Futuro = Valor calculado do lançamento (Valor Original + Valores Opcionais configurados + Valores de Integração configurados).

\*\* Para o cálculo da reversão, o número de dias considera a data final informada na execução do processo.

Importante

Como na linha RM trabalhamos com o período em dias, aplicamos uma equivalência na taxa ( i ), através de um fator diário.  
**FatorDiário** = Fator mensal / Numero Dias = 1/30 = 0,333333333333333

Com isso, a fórmula de cálculo do AVP sofre uma alteração: **VP = VF / ((1+i)^FatorDiario)****^n**

## **06. Estorno do AVP**

Se um lançamento financeiro tiver registros de AVP gerados e ocorrerem situações que possam influenciar no cálculo do seu Valor Presente, o sistema atualizará os status destes registros para "Estorno Pendente". Desta forma, ao gerarmos novamente o processo de AVP para o período em questão, os registros serão estornados.

O estorno será executado da seguinte maneira:

* Se a contabilização dos registros já tiver sido integrada ao lote "0" da contabilidade, serão gerados lançamentos contábeis de estorno;
* Se a contabilização dos registros estiver apenas em lote, ela será excluída.

**Situações que alteram o status dos registros de AVP para "Estorno Pendente"**

* Na alteração do valor original, data de emissão, data de competência, data de vencimento, valores opcionais (somente os configurados) ou valores de integração (configurados) do lançamento financeiro;
* Na inclusão ou no cancelamento de fatura;
* Na inclusão ou no cancelamento do acordo;
* No cancelamento da baixa parcial.

No caso do AVP de cartão, no momento do cancelamento da baixa, os extratos com Status AVP diferentes de "Não Calculado" serão alterados para "Estorno Pendente".

## **07. Restrições**

Para garantir a integridade do processo, existem algumas restrições/informações que devem ser observadas:

* **Exclusão:** Só será permitida a exclusão de lançamentos que não tenham registros de AVP ou que esses estejam estornados.
* **Parcelamento:** Lançamentos que possuem cálculo de AVP não poderão ser parcelados.
* **Faturamento:** Não serão gerados cálculos para o lançamento faturado, somente para os respectivos vencimentos de fatura.
* **Acordo:** No processo de Geração de Acordo, somente os lançamentos gerados pelo acordo é que terão AVP calculados. Caso o lançamento de origem do acordo tenha registros de AVP anteriores a esse processo, eles serão estornados.
* **Baixa Parcial:**Quando um lançamento tiver sua baixa parcial realizada, teremos continuidade no cálculo de AVP para ele, pois a provisão dos juros já foi realizada em período anterior e desta forma será necessário reverter estes juros integralmente.  
  O lançamento gerado pela baixa parcial, se atender aos parâmetros para geração de AVP, terá calculado seu AVP normalmente.
