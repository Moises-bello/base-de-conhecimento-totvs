---
content_hash: 17dd238c8e661689ea5e7cfba5e0db755cf61fc6bd1a353d7bde4da924437921
fetched_at: '2026-06-29T00:10:27.856759+00:00'
page_id: '516648172'
product: rm
source: tdn-rm
title: Cadastro Esquema de Apuração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=516648172
version: 1
---

## 

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela inicial**
   1. **Outras Ações / Ações relacionadas**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

A ferramenta de Esquemas de Apuração **consiste na extração de dados de sistemas terceiros ou de outras aplicações TOTVS.**

Um esquema nada mais é que uma integração que pode ser disponibilizada através de um comando SQL juntamente com as informações de acesso ao banco de dados como, **endereço do servidor, nome de usuário e senha** para que o sistema de Custos seja capaz de extrair as informações **diretamente no ambiente de origem**. Qualquer banco de dados com suporte **ODBC** poderá ser utilizado.

Após a execução do comando SQL será criado um **repositório** com esses dados dentro do sistema de Custos, para que esses dados sejam utilizados por diversos processos. Essa apuração deverá ser executada por **empresa, filial e período**. Esse **repositório** de dados do Gestão de Custos possui será gravado de acordo com o seu **destino**.

Caso não seja possível uma conexão direta ao banco de dados, a integração poderá ser realizada através de **arquivos texto** ou **planilhas Excel**. Nesses casos os arquivos deverão ser extraídos diretamente do sistema de origem, respeitando as mesmas regras acimas citadas, como **empresa, filial e período**.

O sistema de Gestão de Custos pode buscar informações em vários sistemas, por exemplo, Contas Hospitalares, Estoque, Contas a Pagar, Contas a Receber, Caixa e Bancos, Faturamento, Intercâmbio, Pagamento ao Prestador, Contabilidade, etc.

## **02. EXEMPLO DE UTILIZAÇÃO**

|  |  |
| --- | --- |
| Menu/Caminho: | Cadastros / Esquemas de Apuração |

## **03. TELA INICIAL**

**Outras Ações / Ações relacionadas**

| Ação | Descrição |
| --- | --- |
| Procedimento para inclusão de cadastro esquema de apuração | 1. Clique em **Incluir** (Página em branco) para incluir um novo esquema de apuração. 2. O campo **Código Esquema** irá gerar um código automático pelo sistema assim que o registro for salvo. 3. No campo **Esquema** informe uma breve descrição. 4. No campo **Destino**selecione uma das opções onde os dados serão gravados no repositórios do sistema:    1. Cadastro Centro Custo    2. Cadastro Conta Custo    3. Lançamento Conta Direta    4. Lançamento Conta Indireta    5. Quantidade Produzida    6. Base de Rateio    7. Consumo Hospitalar    8. Custo Médio    9. Consumo Pacote 5. Clique em **OK** para salvar e fechar a tela ou clique em **Salvar** para salvar e permanecer em tela. |

## **04. TABELAS UTILIZADAS**

* **Cadastrando Esquemas de Apuração Detalhe**
* Essa tela é acessada a partir da tela de cadastros de Esquema de Apuração acima clicando no botão Anexos / Esquema Apuração Detalhe.

1. Clique em Incluir (Página em branco) para incluir um novo esquema de apuração.
2. No campo Vigência informe um período no formato ano/mês.
3. No campo Código Sentença SQL informe o código da consulta SQL que irá buscar as informações no sistema

* **Layout Cadastro Centro de Custo**
* Esse esquema de apuração é **opcional** e deverá ser utilizado caso seja optado em utilizar a mesma codificação de **Centros de Custos da Contabilidade** (o que é altamente recomendado).
* Durante a fase de implantação a primeira execução irá trazer todos os centros a serem importados, nas demais só serão importados os novos centros cadastrados pela Contabilidade.
* Importante! Como essa consulta SQL irá ler dados na tabela de **cadastro** da Contabilidade, não existirá uma uma coluna de **Período de Competência**, dessa forma para contornar o parâmetro de Período de Competência, informar na consulta SQL da seguinte forma: @PERIODOCOMPETENCIA = @PERIODOCOMPETENCIA

|  |  |  |  |
| --- | --- | --- | --- |
| **Coluna SQL** | **Tipo** | **Descrição** | **Obrigatório** |
| CDCENTROCUSTO | Alfanumérico 45 | Código do Centro de Custo | Sim |
| NOCENTROCUSTO | Alfanumérico 80 | Descrição do Centro de Custo | Sim |

* **Layout Cadastro Conta Custo**
* Esse esquema de apuração é **opcional** e deverá ser utilizado caso seja optado em utilizar a mesma codificação de **Contas de Custos da Contabilidade** (o que é altamente recomendado).
* Durante a fase de implantação a primeira execução irá trazer todos as contas a serem importadas, nas demais só serão importadas as novas contas cadastrados pela Contabilidade.
* Importante! Como essa consulta SQL irá ler dados na tabela de **cadastro** da Contabilidade, não existirá uma uma coluna de **Período de Competência**, dessa forma para contornar o parâmetro de Período de Competência, informar na consulta SQL da seguinte forma: @PERIODOCOMPETENCIA = @PERIODOCOMPETENCI

|  |  |  |  |
| --- | --- | --- | --- |
| **Coluna SQL** | **Tipo** | **Descrição** | **Obrigatório** |
| CDCONTACUSTO | Alfanumérico 45 | Código da Conta de Custo | Sim |
| NOCONTACUSTO | Alfanumérico 80 | Descrição da Conta de Custo | Sim |
| TPCONTA | Alfanumérico 1 | Tipo da Conta de Custo. Enviar **A** para conta Analítica e **S** para conta Sintética | Sim |

* **Layout Lançamento Conta Direta**
* Esse esquema de apuração é **obrigatório** e deverá retornar todos os lançamentos de **despesas** ou **custos** lançadas dentro de um determinado período.
* É possível ter uma **única integração**, pegando todos as despesas da **Contabilidade** ou **diversas integrações** buscando as despesas nos sistemas de origem, como no **Contas a Pagar, Folha de Pagamento,** etc.
* Contas diretas são aquelas onde é possível identificar diretamente quem Centro de Custo teve despesa para aquela Conta. Exemplos de contas diretas: Salários, Manutenção, Materiais e Medicamentos.

|  |  |  |  |
| --- | --- | --- | --- |
| **Coluna SQL** | **Tipo** | **Descrição** | **Obrigatório** |
| CDPERIODOCOMPETENCIA | Numérico 10 | Período de competência dos lançamentos. Enviar no formato YYYYMM. | Sim |
| CDCONTACUSTO | Alfanumérico 45 | Código da Conta de Custo | Sim |
| CDCENTROCUSTO | Alfanumérico 45 | Código do Centro de Custo | Sim |
| VLLANCAMENTO | Numérico 14,2 | Valor do Lançamento | Sim |
| CDCENARIO | Alfanumérico 16 | Código do Cenário | Não |

* **Layout Lançamento Conta Indireta**
* Esse esquema de apuração é **opcional** e deverá retornar todos os lançamentos de **despesas** ou **custos** lançadas dentro de um determinado período.
* Ao **contrário** dos lançamentos **diretos**, quando temos lançamentos onde não são identificados para quais centros de custos ocorreram a despesa, temos que importa-las para o centro de custo como lançamentos **indiretos**. Exemplos de contas indiretas: Água, Energia Elétrica.

|  |  |  |  |
| --- | --- | --- | --- |
| **Coluna SQL** | **Tipo** | **Descrição** | **Obrigatório** |
| CDPERIODOCOMPETENCIA | Numérico 10 | Período de competência dos lançamentos. Enviar no formato YYYYMM. | Sim |
| CDCONTACUSTO | Alfanumérico 45 | Código da Conta de Custo | Sim |
| VLLANCAMENTO | Numérico 14,2 | Valor do Lançamento | Sim |

* **Layout Base Rateio**
* Esse esquema de apuração é responsável por trazer todos os lançamentos quantitativos ou monetários de cada centro de custo que servem como dados estatísticos para os Critérios de Rateios. Exemplo: Número de Funcionários, Número de Requisições a Estoque, Custo Fixo Tesouraria, etc.

|  |  |  |  |
| --- | --- | --- | --- |
| **Coluna SQL** | **Tipo** | **Descrição** | **Obrigatório** |
| CDPERIODOCOMPETENCIA | Numérico 10 | Período de competência dos lançamentos. Enviar no formato YYYYMM. | Sim |
| CDCENTROCUSTO | Alfanumérico 45 | Código do Centro de Custo | Sim |
| QTLANCAMENTO | Numérico 33,15 | Quantidade do Lançamento | Sim |

* **Layout Quantidade Produziada**
* Esse esquema de apuração é **opcional** e deverá retornar todos os lançamentos relacionados com produção realizados pelos Centros de Custos Produtivos: Exemplo: Número de Atendimento no Pronto Socorro, Horas de Centro Cirúrgico, Número de exames do Laboratório, etc.
* O sistema de Custos possui um **parâmetro** onde é definido se a importação da **Quantidade Produzida** será realizada através de **Esquema de Apuração** ou **Automática**. Quando selecionada automática, o sistema após a importação do **Consumo Hospitalar** irá fazer a contagem das quantidades produzidas e suas respectivas ponderações quando necessárias. Consultar a documentação do layout do Consumo Hospitalar e das Volumes das Quantidade Produzidas.

|  |  |  |  |
| --- | --- | --- | --- |
| **Coluna SQL** | **Tipo** | **Descrição** | **Obrigatório** |
| CDPERIODOCOMPETENCIA | Numérico 10 | Período de competência dos lançamentos. Enviar no formato YYYYMM. | Sim |
| CDCENTROCUSTO | Alfanumérico 45 | Código do Centro de Custo que realizou a produção | Sim |
| QTPRODUZIDA | Numérico 8,2 | Quantidade produzida | Sim |

* **Layout Consumo Hospitalar**
* Esse esquema de apuração é responsável por importar **todos os insumos utilizados no atendimento** do paciente durante um período de competência.
* Em linhas o gerais o Consumo Hospitalar é a fotografia do atendimento do paciente com todos os insumos utilizados durante o período de competência como, materiais, medicamentos, OPME, taxas, diárias e exames.
* A consulta SQL deverá ser capaz de retornar toda a produção **realizada** para aquele período, tanto para os atendimentos que ainda estejam **fechados** ou em **aberto**, que neste caso deverá ser feito um **provisionamento da cobrança**.
* Os **pacotes**aplicados na conta não deverão ser enviados nesta integração, pois será apurada posteriormente no esquema de apuração de **Consumo Pacote.**Os **itens** **que foram empacotados** deverão ser enviados linha a linha com o seu respetivo **valor cobrado,**como se a cobrança da conta fosse do tipo **conta aberta**.
* Além dos registros do atendimento, são solicitados **dados referentes**a descrições como por exemplo nos dados do **Paciente**, como **nome,** **sexo** e **data de nascimento**, esses dados assim como os demais listados abaixo são considerados **Cadastros Auxiliares** e **importados** nos seus respectivos **repositórios internos** do Gestão de Custos. Isso é necessário para o correto funcionamento do sistema, pois os dados são normalizados em nossas tabelas, por conta disso o sistema não permite que códigos iguais, mas com descrições diferentes, para esses casos o que irá prevalecer é sempre o último registro analisado pelo sistema durante a etapa de importação.
* + Tabela CID
  + Convênio
  + Médico
  + Paciente
  + Unidade de Atendimento
  + Procedimento Grupo (Especialidade)
  + Procedimento
  + Unidade Medida
  + Tabela Insumo
  + Grupo Insumo
  + Insumo

    Os cadastros auxiliares abaixo serão populados automaticamente durante a importação do consumo hospitalar. Alguns destes cadastros além dos campos de descrição possuem campos próprios do Gestão de Custos que serão utilizados durante o processo de cálculo do custo do paciente.

  Campos necessários para atendimentos internos e externos, como **materiais, medicamentos, taxas, diárias**, etc**.**

|  |  |  |  |
| --- | --- | --- | --- |
| **Coluna SQL** | **Tipo** | **Descrição** | **Obrigatório** |
| CDPERIODOCOMPETENCIA | Numérico 10 | Período de competência dos lançamentos. Enviar no formato YYYYMM. | Sim |
| TPATENDIMENTO | Alfanumérico 50 | Tipo de atendimento. Campo **livre que identifica** o atendimento, exemplos: Pronto Socorro, Ambulatório, Internação. | Sim |
| CDPACIENTE | Alfanumérico 25 | Código do **paciente**. | Sim |
| NOPACIENTE | Alfanumérico 255 | Nome completo do **paciente**. | Sim |
| CDSEXO | Alfanumérico 25 | Sexo do paciente, valores possíveis **M** ou **F**. | Sim |
| DTNASCIMENTO | Data e Hora | Data de **nascimento** do paciente | Sim |
| CDCID | Alfanumérico 10 | Código do **CID**, pode ser enviado o CID de **entrada** para conta **aberta** ou CID de **saída** para conta **fechada**. | Sim |
| NOCID | Alfanumérico 255 | Descrição do **CID**, respeitar a mesma regra de negócio acima. | Sim |
| DTALTA | Data e Hora | Data da **alta** do paciente, caso paciente esteja ainda internado, enviar em branco. | Sim |
| DTLANCAMENTO | Data e Hora | Data e hora em que o insumo foi **lançado** na conta do paciente. | Sim |
| CDCHAVEORIGEM | Alfanumérico 50 | Código **sequencial** **único** que identifica o registro lançado no sistema Hospitalar que está sendo integrado. | Sim |
|  |  |  |  |
| --- | --- | --- | --- |
| CDCONVENIO | Alfanumérico 50 | Código do **convênio**, se paciente particular, enviar o código do convênio particular. | Sim |
| NOCONVENIO | Alfanumérico 255 | Descrição do **convênio**, respeitar a mesma regra de negócio acima. | Sim |
| CDCENTROCUSTO | Alfanumérico 45 | Código do **centro de custo** onde o paciente está alocado. Caso o sistema Hospitalar **não** possua essa informação, o **código da unidade de atendimento** deverá ser obrigatório o seu envio e configurado o de-para no Gestão de Custos através da tela de cadastros da **Unidade de Atendimento**. | Sim |
|  |  |  |  |
| --- | --- | --- | --- |
| CDTABELAINSUMO | Alfanumérico 50 | Código da **tabela insumo** onde ficam gravados os insumos que podem ser lançados no atendimento do paciente como TUSS, CBHPM, Sigtap, ou tabela própria. **Atenção!** Caso o sistema hospitalar a ser integrado utilize uma **tabela própria** e os registros exibidos em tela fazem uso dessa tabela, retornar o **código da tabela própria**, caso contrário utilizar o código da **tabela do convênio**acordada com o convênio**.** | Sim |
| NOTABELAINSUMO | Alfanumérico 255 | Descrição da tabela insumo, respeitar a mesma regra de negócio acima. | Sim |
| CDGRUPOINSUMO | Alfanumérico 50 | Código do **grupo insumo**que define o que é material, medicamento, taxa, exames, etc. | Sim |
| NOGRUPOINSUMO | Alfanumérico 255 | Descrição do **grupo insumo**, respeitar a mesma regra de negócio acima. | Sim |
| CDINSUMO | Alfanumérico 50 | Código do **insumo lançado** na conta do paciente. Não enviar insumos **excluídos** ou **devolvidos**, assim como e**receitas de terceiros**, como honorários médicos pagos pela **operadora** diretamente ao **médico**. **Atenção!** Caso o sistema hospitalar a ser integrado utilize uma **tabela própria** e os registros exibidos em tela fazem uso dessa tabela, retornar o **código da tabela própria**, caso contrário utilizar o código da **tabela do convênio**acordada com o convênio**.** | Sim |
| NOINSUMO | Alfanumérico 500 | Descrição do **insumo**, respeitar a mesma regra de negócio acima. | Sim |
| QTUTILIZADA | Numérico 14,2 | **Quantidade utilizada real** do insumo. Considerar se houveram **devoluções** ou **perdas**. | Sim |
| VLCUSTOUNITARIO | Numérico 14,2 | **Valor do custo unitário do insumo** somente para materiais e medicamentos que possuem o custo médio salvo no **próprio** sistema Hospitalar. Caso o **custo médio** seja realizado em outro sistema, enviar em branco esse campo e utilizar o esquema de apuração com destino **Custo Médio** para que ele seja importado posteriormente. | Não |
| VLCUSTOTOTAL | Numérico 14,2 | **Valor do custo total**, respeitar a mesma regra de negócio acima. | Não |
| QTCOBRADA | Numérico 14,2 | **Quantidade cobrada** do convênio ou particular. | Sim |
| VLCOBRADOUNITARIO | Numérico 14,2 | **Valor cobrado unitário** do convênio ou particular. | Sim |
| VLCOBRADOTOTAL | Numérico 14,2 | **Valor cobrado total** do convênio ou particular. | Sim |
| STATUSITEM | Alfanumérico 25 | Se o insumo foi cobrado de particular ou convênio, enviar o status como **PG** (Pagante), caso o insumo foi uma cortesia ou filantropia, enviar **NP** (Não Pagante). | Sim |
| CDUNIDADEMEDIDA | Alfanumérico 10 | Código da **unidade de medida**, enviar somente para medicamentos, materiais e OPME, para os demais enviar em branco. | Sim |
| NOUNIDADEMEDIDA | Alfanumérico 100 | Descrição da **unidade de medida**, respeitar a mesma regra de negócio acima. | Sim |
| CDUNIDADEATENDIMENTO | Alfanumérico 50 | Código da **unidade de atendimento** (setor) onde o paciente está internado. | Não |
| NOUNIDADEATENDIMENTO | Alfanumérico 255 | Descrição da **unidade de atendimento** (setor) onde o paciente está internado. | Não |
| DTPACIENTEADMISSAO | Data e Hora | Data e hora em que o paciente **entrou** na unidade de atendimento (setor). **Atenção!** Caso a data seja inferior que do período de competência que está sendo apurado, o importador irá forçar para que essa data e hora seja o primeiro dia do mês a zero horas. | Não |
| DTPACIENTESAIDA | Data e Hora | Data e hora em que o **saiu** na unidade de atendimento (setor). **Atenção!** Caso o paciente ainda esteja internado, a data e hora o importador irá forçar a data e hora seja o último dia do mês as 23:59:59 | Não |

* Se o paciente teve passagem pelo **bloco cirúrgico**além dos campos acima informando quais**materiais, medicamentos, OPMEs e taxas**foram utilizados na cirurgia**,**será necessário **retornar em todos os registros que fazem parte da folha de sala**os **seguintes campos abaixo.**
* Se o paciente não passou por cirurgia, os campos devem retornar em branco.

| **Coluna SQL** | **Descrição** | **Tipo** | **Obrigatório** |
| --- | --- | --- | --- |
| CDPROCEDIMENTOGRUPO | Alfanumérico 50 | Código da **especialidade do procedimento** realizado no Bloco Cirúrgico. Se na folha de sala não possuir a especialidade exata, enviar a especialidade principal do médico cirurgião. | Sim |
| NOPROCEDIMENTOGRUPO | Alfanumérico 255 | Descrição da **especialidade do procedimento**, respeitar a mesma regra de negócio acima. | Sim |
| CDPROCEDIMENTO | Alfanumérico 50 | Código do **procedimento** realizado no Bloco Cirúrgico. | Sim |
| NOPROCEDIMENTO | Alfanumérico 255 | Descrição do **procedimento** realizado no Bloco Cirúrgico. | Sim |
| DTPROCEDIMENTOINICIO | Data e Hora | Data e hora que o paciente **entrou** no Bloco Cirúrgico para realizar o procedimento. | Sim |
| DTPROCEDIMENTOFIM | Data e Hora | Data e hora que o paciente **saiu** do Bloco Cirúrgicopara realizar o procedimento. | Sim |
| CDMEDICO | Alfanumérico 50 | **CRM** ou **CPF** do médico que executou o procedimento no Bloco Cirúrgico. | Sim |
| NOMEDICO | Alfanumérico 255 | Nome do médico que executou o procedimento no Bloco Cirúrgico. | Sim |

* **Layout Consumo Pacote**
* Todos os lançamentos de consumo de pacote.

| **Coluna SQL** | **Descrição** | **Tipo** | **Obrigatório** |
| --- | --- | --- | --- |
| CDATENDIMENTO | Código do Atendimento | Texto (50) | Sim |
| DTATENDIMENTO | Data de Admissão do Paciente | Data/Hora | Sim |
| CDPACIENTE | Código do Paciente | Texto (25) | Sim |
| NOPACIENTE | Nome do Paciente | Texto (255) | Sim |
| CDSEXO | Sexo do Paciente | Texto (25) | Não |
| DTNASCIMENTO | Data de Nascimento | Data/Hora | Não |
| CDCONVENIO | Código do Convênio | Texto (50) | Sim |
| NOCONVENIO | Nome do convênio | Texto (255) | Sim |
| CDUNIDADEATENDIMENTOPACOTE | Código da Unidade Atendimento do Pacote | Texto (50) | Sim\* |
| NOUNIDADEATENDIMENTOPACOTE | Nome da Unidade Atendimento do Pacote | Texto (255) | Sim\* |
| CDCENTROCUSTOPACOTE | Código do Centro Custo do Pacote | Texto (45) | Sim\* |
| DTPACOTE | Data do Pacote | Data/Hora | Não |
| CDPACOTE | Código do Pacote | Texto (50) | Sim |
| NOPACOTE | Nome do Pacote | Texto (255) | Sim |
| NRNOTAFISCAL | Númer da Nota Fiscal | Texto (50) | Não |
| VLPACOTE | Valor do Pacote | Numérico (14,2) | Sim |
| DTLANCAMENTO | Data do Lancamento do Insumo | Data/Hora | Sim |
| CDCENTROCUSTOINSUMO | Código do Centro Custo do Insumo | Texto (45) | Sim |
| CDGRUPOINSUMO | Código do Grupo Insumo | Texto (50) | Sim |
| NOGRUPOINSUMO | Nome do Grupo Insumo | Texto (255) | Sim |
| CDINSUMO | Código do Insumo | Texto (50) | Sim |
| NOINSUMO | Nome do Insumo | Texto (255) |  |
| QTCOBRADA | Quantidade Cobrada | Numérico (14,2) | Sim |
| VLCOBRADOUNITARIO | Valor Cobrado Unitário | Numérico (14,2) | Sim |
| TPCOBRANCA | Tipo Cobrança | "P" - Pacote  "E" - Exceção | Sim |
