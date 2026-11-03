---
content_hash: 545c8ca0901926472b4cbb69ec8ad6088c0f51bcd5b8fa649a7974e731a75b00
fetched_at: '2026-06-29T00:06:26.615263+00:00'
page_id: '225951582'
product: rm
source: tdn-rm
title: PPE_PERFIL_DE_PESSOAL_DAS_ESTATAIS
type: documentation
url: https://tdn.totvs.com/display/LRM/PPE_PERFIL_DE_PESSOAL_DAS_ESTATAIS
version: 156
---

# Perfil de Pessoal das Estatais

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Construção e Projetos.* |
| **Módulo:** | **Totvs Folha de Pagamento*.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *PPE.* | *Perfil de Pessoal das Estatais.* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Rubricas de Dispêndio Consolidadas | Rubricas de Dispêndio Consolidadas | | Histórico de Encargos | Histórico de Encargos | | Lançamentos das Despesas | Lançamentos das Despesas | | Funcionário | Funcionário | | Pessoas | Pessoas | | Orgão de Origem / Destino | Tabela Dinâmica Orgão de Origem / Destino | | Regime Jurídico | Tabela Dinâmica Regime Jurídico | | Área de Atuação | Tabela Dinâmica Área de Atuação | | Eventos | Eventos | | Envelope de Pagamento | Envelope de Pagamento | | Tipo de Benefício | Tabela Dinâmica Tipo de Benefício | | Cargos | Cargos | | Tabelas Salariais | Tabelas Salariais | | Faixas Salariais | Faixas Salariais | | Níveis Salariais | Níveis Salariais | | Funções | Funções | | Classificação do Cargo | Classificação do Cargo | | Tipo de Função | Tabela Dinâmica Tipo de Função | | Histórico de Afastamento | Histórico de Afastamento | | Motivo de Afastamento do Cliente | Motivo de Afastamento do Cliente | | Rubrica de Dispêndio Individual | Rubrica de Dispêndio Individual | | Cadastro de Curso | Cadastro de Curso | | Formação Acadêmica | Formação Acadêmica | | Tipo de Desconto | Tabela Dinâmica Tipo de Desconto | | Empréstimo | Empréstimo | | Parametrizador | Parametrizador | | Classificação do Cargo | Tabela Dinâmica Classificação do Cargo | |
| **Cadastros Iniciais:** | Tabela Dinâmica Orgão de Origem / Destino Tabela Dinâmica Regime Jurídico Tabela Dinâmica Área de Atuação Tabela Dinâmica Tipo de Benefício Tabela Dinâmica Tipo de Função Tabela Dinâmica Tipo de Desconto  Tabela Dinâmica Classificação do Cargo  Rubricas de Dispêndio Consolidadas Rubrica de Dispêndio Individual Eventos Motivo de Afastamento do Cliente Cadastro de Curso Formação Acadêmica Empréstimo  Classificação do Cargo Cargos Funções  Tabelas Salariais Faixas Salariais Níveis Salariais  Pessoas Funcionário  Parametrizador |
| **Parâmetro(s):** | PPE / Eventos que compõem ao Valor da Função: usado no campo Valor da Função nos Dados da Função. PPE / Eventos que compõem ao Valor do Complemento: usado no campo Valor do Complemento nos Dados da Função. |
| **Ponto de Entrada:** | *Folha Mensal / Relatórios da Folha / PPE* |
| **Chamados Relacionados** | TUJAA8 |
| **Requisito (ISSUE):** |  |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Tabelas Utilizadas:** | PDISCONS, VDESPESAS, PENCARGO, PFUNC, PPESSOA, PFDEPEND, PORGAOORIGDEST, PREGIMEJURIDICO, GFILIAL, PSECAO, PAREAATUACAO, PTIPOBENEFICIO, PEVENTO, PFFINANC, PCARGO, VNIVELFUNCAO, VFAIXASALARIAL, PFUNCAO, VTABELASALARIAL, PEVTVALORFUNCAO, PEVTVALORCOMPL, PMOTIVAFASTCLIENTE, PFHSTAFT, PDISPINDIV, VCURSOACAD, VFORMCAOCAD, PFEMPRT |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

O PPE - Perfil de Pessoal das Estatais deve ser enviado mensalmente, até o dia 15 do mês subsequente ao de competência.  
A regra se aplica a todas as Empresas Estatais Federais, inclusive as Dependentes Tesouro Nacional.  
Os dados requeridos:  
• Contemplam todos os empregados com contrato de trabalho ativo, aí incluídos os cedidos, os  
requisitados, os afastados ou em licença de qualquer natureza e os detentores de cargos  
comissionados ou de função de confiança (inclusive os de livre provimento), bem como dirigentes e  
conselheiros;  
• Devem refletir a situação cadastral dos empregados, dirigentes e conselheiros no último dia do mês  
de competência da informação.

O TOTVS Folha de Pagamento implementa o PPE conforme as regras:

* Do Manual do DEST /  PPE obtido em <http://www.planejamento.gov.br/secretarias/upload/Arquivos/dest/documentacao/140919_manual_ppe-versao_1_1d.pdf/view>,
* Planilha: Leiaute\_Arquivo\_Versao\_1\_1c.xls, aqui é definida os tipos e tamanho do campos assim com sua obrigatoriedade e hierarquia dos registros
* Planilha: tabelas\_auxiliares\_v\_1\_1\_f\_setembro2014-1.xls, aqui é informado os valores de cada tabela auxiliar.

Nas tabelas abaixo são descrita a origem e a regra de obtenção de cada campo para compor os registros que constam no arquivo PPE a ser gerado, conforme informado no Manual Módulo PPE - Versão 1.1c - Agosto de 2014:

A campos que possui o detalhamento de equivalência de dados prefixados do TOTVS Folha de Pagamento com as informações contidas nas tabelas da Planilhas  tabelas\_auxiliares\_v\_1\_1\_f\_setembro2014-1.xls. Estas informações estão loga abaixo aos dados de cada registro.

**Dados Header Autenticação**

|  |  |  |
| --- | --- | --- |
| **Campo** | **Origem** | **Regra** |
| Usuário | Parâmetro do Processo | Parâmetro Usuário |
| Senha | Parâmetro do Processo | Parâmetro Senha |
| Data Criação | Parâmetro do Processo | Parâmetro Data Criação |
| Data Expiração | Parâmetro do Processo | Parâmetro Data Expiração |

**Dados da Empresa Estatal**

|  |  |  |
| --- | --- | --- |
| **Campo** | **Origem** | **Regra** |
| Competência - Ano e Mês | Parâmetro do Processo | Competência – Ano e Mês |
| Código Siest da Empresa | Parâmetro do Processo | Código Siest da Empresa |

**Dados de Cada Dispêndio Consolidado.**

Neste registro são demonstrados valores de encargos  do TOTVS folha de pagamento, e despesas com pessoal do TOTVSGestão de Pessoas. Vide Tabela 2-Rubricas Consolidadas

|  |  |  |
| --- | --- | --- |
| **Campo** | **Origem** | **Regra** |
| Rubrica – Código | PRUBRICACONS.CODSPE (Novo) referente ao relacionamento com os campos:  VDESPESAS.CODDISPCONS (Novo)  PENCARGO.CODDISPCONS (Novo) | Código provindo da tabela PRUBRICACONS. Cadastro de Rubrica Consolidada (Novo) que implementa a Tabela 2-Rubricas Consolidadas  Encargos e despesas que tenham sido vinculados a Rubrica consolidada, dentro da competência informada nos parâmetros do processo. |
| Rubrica – Valor | VDESPESAS.VALOR  PFENCARGO.VALOR | Somatório dos valores de despesas com data de lançamento na competência informada no processo do PPE, somado ao valor dos encargos na competência, referente ao Código SPE |
| Quantidade de Empregados | PFUNC.CODPESSOA | Total de funcionários classificados pelo código de pessoa que participaram do dispêndio consolidado na competência referente ao Código SPE. Caso uma pessoa conste em mais de uma despesa ou encargo para o mesmo Código SPE dentro da competência, ainda assim, deverá contabilizar apenas uma unica vez para cada Código SPE. |

**Dados de Cada Empregado / Dados Básicos**

Neste registro é informado todos os funcionários conforme definido no filtro do processo de emissão do PPE.

|  |  |  |
| --- | --- | --- |
| **Campo** | **Origem** | **Regra** |
| CPF | ppessoa.cpf | Campo CPF do cadastro de pessoa |
| Pis / Pasep | pfunc.pispasep | Campo PIS/PASEP do cadastro de pessoa |
| Nome da Mãe | pfdepend.nome de grau 7 | Nome do dependente de grau 7 vinculado ao Funcionário.  Se não houver informe “Sem Registro” |
| Carteira Trabalho | ppessoa.carteiratrab | Carteira de trabalho do cadastro de pessoa |
| Carteira Trabalho - Série | ppessoa.seriecarttrab | Serie da Carteira de trabalho do cadastro de pessoa |
| Carteira Trabalho - UF | ppessoa.ufcarttrab | uf Carteira de trabalho do cadastro de pessoa |
| Ano do Primeiro Emprego | PPESSOA.ANO1EMPREGO (Novo) | Campo "Ano do Primeiro Emprego" do cadastro de pessoa |
| Matrícula | pfunc.chapa | Chapa do cadastro de funcionário |
| Sexo | ppessoa.sexo | Campo sexo da Pessoa |
| Data de Nascimento | ppessoa.dtnascimento | Campo da Data de Nascimento do cadastro de Pessoa |
| Raça / Cor | ppessoa.corraca | Vide Equivalência Cor / Raça TOTVS Folha de pagamento x Tabela 5 - Raça-Cor. PCORRACA |
| Pessoa com Deficiência | ppessoa | Analise dos campos do cadastro de Pessoa.  Se (DEFICIENTEFISICO ou DEFICIENTEAUDITIVO ou DEFICIENTEFALA ou  DEFICIENTEVISUAL ou DEFICIENTEMENTAL ou BRPDH)  ENTÃO retornar “S”  SENÃO retonrar “N” |
| Tipo de Deficiência | ppessoa | Vide Equivalência Tipo de Deficiência TOTVS Folha de pagamento (Campo de pessoa) x Tabela 6 Tipo de Deficiência  Cadastro de Funcionário Aba RAIS grupo "Deficiente" |
| Nacionalidade | ppessoa.nacionalidade | Vide Equivalência Nacionalidade TOTVS Folha de pagamento x Tabela 7 Nacionalidade |
| Ano de Chegada no Brasil | ppessoa.datachegada | Obter o ano no formato AAAA. Campo Data de Chegada do Cadastro de Pessoa |
| Grau de Instrução | ppessoa.grauinstrucao | Equivalência Grau de Instrução TOTVS Folha de pagamento x Tabela 8 - Grau de Instrução |
| Data de Admissão | pfunc.dataadmissao | Campo Data de Admissão do Cadastro de Funcionário |
| Motivo de Admissão | PMOTIVADMISSAOCLI.DESCRICAO (Novo) | Usuário deverá popular a tabela dinâmica “Motivo de Admissão Cliente” com os códigos informados na Tabela 9 - Motivo de Admissão  Obter da tabela dinâmica PMOTIVADMISSAOCLI O valor do campo descrição referente PFUNC.MOTIVOADMISSAO. O cliente deverá fazer o DE/PARA entre a PMOTADMISSAOe a PMOTIVADMISSAOCLI, o código deve ser o mesmo da atual Motivo de Admissão, e na descrição informar o código daTabela 19 – Motivo Desligamento. (Novo) |
| Órgão de Origem / Destino | PFUNC.CODORGAOORIGDEST (Novo) | Campo Orgão Origem / Destino conforme informado na Tabela Dinâmica Órgão de Origem / Destino. (PORGAOORIGDEST) (Novo)  Tabela 10 - Código de Órgãos |
| Regime Jurídico | PFUNC.CODREGIMEJURIDICO (Novo) | Campo Regime Juridico conforme informado na Tabela Dinâmica Regime Jurídico (PREGIMEJURIDICO) (Novo)  Tabela 11 - Regime Jurídico. |
| Anos de Contribuição para o INSS | PFUNC.ANOSCONTRIBUICAOINSS (Novo) | Campo Anos De Contribuição INSS do Cadastro de Funcionário |
| Aposentadoria - Ano/Mês | pfunc.dtaposentadoria | Ano e Mês do campo Data de Aposentadoria do Cadastro de Funcionário Aba Situação |
| Jornada de Trabalho (Atual) | pfunc.jornadamensal | Vide calculo e Equivalência De / Para Tabela 12 - Jornada de Trabalho |
| Ocupação CBO (Atual) | pfuncao.cbo2002 | Somente números, sem ponto, espaços, traços ou rifem. Função do funcionário de acordo com o seu histórico na competência informada. |
| Local de Trabalho - Município | gfilial.cidade -> PFUNC.CODFILIAL | Campo cidade do cadastro das filiais referente a filial em que o funcionário está lotado |
| Área de Atuação (Atual) | PSECAO.CODAREAATUACAO (Novo) | Campo Área de Atuação vinculado a seção do funcionário de acordo com o histórico de seção da competência informada.  Conforme informado na Tabela Dinâmica Área de Atuação (PAREAATUACAO) |

**Dados de Benefícios:**

|  |  |  |
| --- | --- | --- |
| Campo | Origem | Regra |
| Tipo de Benefício | PEVENTO.CODTIPOBENEFICIO (Novo) | Listar de forma única o código dos benefícios que o funcionário recebeu no mês/ano da competência informada no seu envelope de pagamento (PFFINANC).  Campo Tipo de Beneficio no cadastro de evento conforme Tabela Dinâmica Tipo de Benefício ( PTIPOBENEFICIO  ) (Novo) |

**Dados do Cargo Efetivo:**

Informações sobre Carreira e Cargo Efetivo do empregado. Preencher os campos constantes nesse bloco, somente no caso de empregado de carreira do quadro permanente da empresa, admitidos conforme códigos 10, 11, 22 e 23 da Tabela 9 – Motivo de Admissão Analisar o De / Para para equivalência Motivo Admissão Cliente. Para os demais empregados não preencher os campos constantes nesse bloco de informações.

O Totvs Folha de Pagamento não implementa detalhamento de Ocupação para o Cargo. A Ocupação somente é tratado pelo código CBO vinculado a função.

Deve ser observado o histórico de função referente a competência informada a fim de obter o cargo relacionado a função.

O Dados de Tabela, Faixa, Nivel e Referencia Salarial são obtidos do Totvs Gestão de Pessoas (Vitae). Vinculados ao funcionário.

|  |  |  |
| --- | --- | --- |
| **Campo** | **Origem** | **Regra** |
| Plano Cargos e Salários - Sigla | PCARGO.SIGLAPLANO (Novo) | Campo Sigla do Plano no Cadastro de Cargo. |
| Plano Cargos e Salários - Situação | Descrição a que ser refere o campo PCARGO.SITUACAO (Novo) | Campo Situação do Cargo do Cadastro de Cargo.  Dados Validos são: 1 - em operação; 2 - em extinção; 3 - em implantação. |
| Carreira | PCARGO.DESCRICAO | Campo Descrição |
| Cargo Efetivo - Nome | PCARGO.NOME | Campo Descrição do Cargo. |
| Cargo Efetivo - Sigla | PCARGO.SIGLA (Novo) | Campo Sigla do Cargo |
| Cargo Efetivo - Código | PCARGO.CODIGO | Campo Código do Identificador do Cargo. |
| Faixa Salarial | VNIVELFUNCAO.NOMENIVEL | Referente a tabela, e faixa do funcionário.  No caso de inexistência de faixa salarial (grupo, classe ou nível), informar nesse campo a palavra “Única” |
| Referência Salarial | VFAIXASALARIAL.NOMEFAIXA | Referente a tabela, e faixa do funcionário. |
| Salário Base | PFUNC.SALARIO | Campo Salário do Cadastro do Funcionário. do Histórico salarial referente a competência Informado |
| Ocupação - Nome | PCARGO.NOME | Totvs Folha de Pagamento Não implementa este detalhamento  Se não houver, repetir o nome do cargo efetivo constante do Plano de Cargos |
| Ocupação - Sigla | PCARGO.SIGLA | Totvs Folha de Pagamento Não implementa este detalhamento  Se não houver, repetir a sigla do cargo efetivo constante do Plano de Cargos |
| Classificação Cargo | PCARGO.CODCLASSCARGO (Novo) | Campo a ser escolhido do Cadastro Classificação do Cargo (PCODCLASSCARGO). Tabela 16 - Classificação de Cargo/Função |

**Dados da Função:**

Informações sobre Função ocupada pelo Funcionário (de carreira ou não), conforme Plano de Funções (PF) ou Quadro Temporário, bem como de dados da atividade de Dirigente e de Conselheiro. O campo “Função – Tipo” abaixo sempre deve ser preenchido/enviado, observando a tipologia de função definida na Tabela 17 – Tipo de Função.

Deve ser observado o histórico de função referente a competência informada.

|  |  |  |
| --- | --- | --- |
| **Campo** | **Origem** | **Regra** |
| Função - Tipo | PFUNCAO.CODTIPOFUNCAO (Novo) | Informar conforme registros da Tabela Dinâmica Tipo de Função ( PTIPOFUNCAO) (Novo) |
| Função - Nome | PFUNC.NOME | Nome completo da função/cargo exercida pelo empregado/dirigente/conselheiro, sem abreviar. É obrigatório se se Função - Tipo <> “0” |
| Função - Sigla | PFUNCAO.SIGLA (Novo) | Campo Sigla do cadastro de Função. |
| Função - Código | PFUNCAO.CODIGO | É obrigatório se se Função - Tipo <> “0", "1", "2" e "3" |
| Faixa Salarial | PFUNC.CODNIVEL | No caso de inexistência de faixa salarial (grupo, classe ou nível), informar nesse campo a palavra “Única”.  É obrigatório se se Função - Tipo <> “0", "1", "2" e "3" |
| Referência Salarial | PFUNC.GRUPOSALARIAL | É obrigatório se se Função - Tipo <> “0", "1", "2" e "3" |
| Valor de Referencia | VTABELASALARIAL.SALARIO | Valor do campo Salário referente a tabela salarial da função (PFUNCAO.CODTABELA) e nível e faixa correspondente ao funcionário (PFUNC: CODNIVELSAL e GRUPOSALARIAL).  É obrigatório se se Função - Tipo <> “0", "1", "2", "3" e não informou Valor da Função e Valor do Complemento. |
| Valor da Função | É a soma dos valores dos eventos na ficha financeira referente a competência informada que constam na lista de eventos no parametrizador "PPE / Eventos que compõem ao Valor da Função" (Novo). | É obrigatório se se Função - Tipo <> “0", "1", "2", "3" e não informou Valor de Referência e Valor do Complemento.  Estes eventos são informados no Parametrizador em PPE / Eventos que compõem ao Valor da Função: usado no campo Valor da Função nos Dados da Função. (PEVTVALORFUNCAO) (Novo) |
| Valor do Complemento | É a soma dos valores dos eventos na ficha financeira referente a competência informada que constam na lista de eventos no parametrizado "PPE / Eventos que compõem ao Valor do Complemento". | É obrigatório se se Função - Tipo <> “0", "1", "2", "3" e não informou Valor de Referência e Valor do Complemento.  Estes eventos são informados no Parametrizador em "PPE / Eventos que compõem ao Valor do Complemento": usado no campo Valor do Complemento nos Dados da Função. ( PEVTVALORCOMPL) (Novo) |
| Classificação da Função | PCARGO.CODCLASSCARGO (Novo) | Código de Classificação do cargo vinculado a função do funcionário (Novo)  Campo a ser escolhido do Cadastro Classificação do Cargo (PCODCLASSCARGO). Tabela 16 - Classificação de Cargo/Função |

**Dados de Afastamento e Licenças / Dados de Cada Ocorrência:**

Afastamentos do Funcionário ocorrido na competência informado.

|  |  |  |
| --- | --- | --- |
| Campo | Origem | Regra |
| Motivo do Afastamento ou Licença | PMOTIVAFASTCLIENTE.DESCRICAO (Novo) | Obter da tabela dinâmica Dinâmica "Motivo de Mudança de Situação Cliente" (PMOTIVAFASTCLIENTE) O valor do campo DESCRICAO referente PFHSTAFT.MOTIVO. O cliente deverá fazer o DE / PARA entre a Tabela Dinâmica Motivo de Mudança de Situação (PMUDSITUACAO) e a PMOTIVAFASTCLIENTE, o código deve ser o mesmo do Motivo de Situação Atual, e na descrição informar o código relativo a Tabela 18 – Motivo de Afastamento/Licença. |
| Data do Afastamento ou Licença | PFHSTAFT.DTINICIO | Data de Inicio do Afastamento  Formato: “AAAA-MM-DD” |
| Data do Retorno | PFHSTAFT.DTFINAL | Não informar se não houve retorno (Data final não informada)  Formato: “AAAA-MM-DD” |
| Dias Afastados no mês | (Final – Inicio) + 1 | O valor do campo Final deve ser o menor valor entre o último dia da competência e data final quando informado. Não sendo a data final informada assumir último dia da competência.  Início maior data entre o início do afastamento ou primeiro dia da competência. |

**Dados de Desligamento:**

Somente para funcionários que foram demitidos (situação “D”) em que a data do histórico de situação “D” esteja na competência informada.

|  |  |  |  |
| --- | --- | --- | --- |
| Campo | Origem | Regra |  |
| Data do Desligamento | PFHSTSIT.DATAMUDANCA | Última situação “D” na competência informado.  Campo Data de Mudança do Histórico de situação 'D" |  |
| Motivo do Desligamento | PMOTIVDEMISSAOCLI.DESCRICAO (Novo) | Usuário deverá popular a tabela dinâmica “Motivo de Demissão Cliente” com os códigos informados na Tabela 19 - Motivo Desligamento  Obter da tabela dinâmica  “Motivo de Demissão Cliente” (PMOTIVDEMISSAOCLI) O valor do campo descrição referente PFUNC.MOTIVODEMISSAO. O cliente deverá fazer o DE/PARA entre a PMOTIVDEMISSAO e a PMOTIVDEMISSAOCLI, o código deve ser o mesmo da atual “Motivo de Demissão”, e na descrição a informar o código da Tabela 19 – Motivo Desligamento. (Novo) |  |

**Dados de Cada Dispêndio:**

Os registros abaixo são obtidos do novo cadastro Rubrica Individual conforme a Tabela 3-Rubricas Individuais (Novo), vinculada ao Evento e lançado na ficha financeira do funcionário na competência informada.

|  |  |  |
| --- | --- | --- |
| **Campo** | **Origem** | **Regra** |
| Rubrica - Código | PRUBINDIVIDUAL.CODSPE (Novo) | Código CODSPE do dispêndio individualizado associado ao evento. |
| Rubrica - Valor | PFFINANC.VALOR | Somatório individualizado pelo código SPE do evento na ficha financeira para a competência informada |

**Dados de Cada Formação Profissional**

Cadastro de formação acadêmica do Totvs Gestão de Pessoal vinculado a pessoa do Funcionário.

|  |  |  |
| --- | --- | --- |
| **Campo** | **Origem** | **Regra** |
| Formação - Código | VCURSOACAD.CODEMPRESA(Novo) | Campo Código da Empresa do curso vinculado a formação da pessoa atrelada ao funcionário.  Informar conforme descrito na Tabela 21 - Cursos |
| Formação - Ano | Vformacaoacad. anotermino | Ano de término referente ao curso vinculado a formação da pessoa atrelada ao funcionário. |

**Dados de Cada Desconto em Folha**

Deverá ser listado o valor do somatório do evento de desconto que tenha sido associado ao tipo de desconto (pevento. CODTPDESCONTO), possuindo ou não empréstimo (PFEMPRT) ao funcionário

|  |  |  |
| --- | --- | --- |
| **Campo** | **Origem** | **Regra** |
| Desconto - Código | PEVENTO.CODTPDESCONTO (Novo) | Código obtido no cadastro da tabela dinâmica Tipo de Desconto (PTPDESCONTO) (Novo) referente a Tabela 22 – Tipo de Desconto em Folha. |
| Desconto - Valor | PFINANC.VALOR | Somatório do evento para o funcionário lançado na ficha financeira conforme a competência informada |
| Banco - Código Compe | PFEMPRT.CODBANCO (Novo) | Informar somente se o tipo do desconto for ‘99’ - Empréstimo Consignado em Instituições Financeiras |
| Contrato - Número Identificador | PFEMPRT.CONTRATO (Novo) | Informar somente se o tipo do desconto for ‘99’ - Empréstimo Consignado em Instituições Financeiras |
| Contrato - DataI Inicial | PFEMPRT.DTEMPRESTIMO | Informar somente se o tipo do desconto for ‘99’ - Empréstimo Consignado em Instituições Financeiras |
| Contrato - Data Final | PFEMPRT.FINALDESCONTO (Novo) | Informar somente se o tipo do desconto for ‘99’ - Empréstimo Consignado em Instituições Financeiras |
| Contrato - Valor | PFFINANC.VALOR | Somatório do valor do evento na ficha financeira. - Empréstimo Consignado em Instituições Financeiras |
| Quantidade de Parcelas | PFEMPRT.QTDEPARCELAS (Novo) | Informar somente se o tipo do desconto for ‘99’ - Empréstimo Consignado em Instituições Financeiras |
| Data - Primeiro Mês de Desconto | Mês do campo PFEMPRT.INICIODESCONTO | Informar somente se o tipo do desconto for ‘99’ - Empréstimo Consignado em Instituições Financeiras |
| Data - Exclusão do Contrato | PFEMPRT.DTEXCLUSAO (Novo) | Corresponde a data de liquidação do contrato. Mesmo que o tipo seja diferente de ‘99’- Empréstimo Consignado em Instituições Financeiras. |
| Motivo da Exclusão do Contrato | PFEMPRT.CODMOTIVEXCLUSAO (Novo) | Estando a Data-Exclusão preenchida deve ser informado este campo.  Tipos Validos: 1 - Operação Paga; 2 - Operação Liquidada Antecipadamente  3 – Outros. Tabela Dinâmica Motivo de Exclusão (PMOTIVEXCLUSAO) |

Empréstimo Consignado em Instituições Financeiras

**Equivalência Cor / Raça TOTVS Folha de pagamento x Tabela 5 - Raça-Cor**

|  |  |  |
| --- | --- | --- |
| **TOTVS**  **Tabela Dinâmica Cor / Raça**  **( PCORRACA)** | **TABELA 5** | **Descrição** |
| 0 - Indígena | 1 | Indígena |
| 2 - Branca | 2 | Branca |
| 4 - Preta | 3 | Negra |
| 8 - Parda | 4 | Parda |
| 6 - Amarela | 5 | Amarela |
| 9 - Não Informado  ou  10 - Não Declarado | 9 | Não Informado |
|  |  |  |

**Equivalência Tipo de Deficiência TOTVS Folha de pagamento x Tabela 6 - Tipo Deficiência**

|  |  |  |
| --- | --- | --- |
| **TOTVS**  **Campo da PPESSOA** | **Tabela 6** | **Descrição** |
| Se DEFICIENTEFISICO OU DEFICIENTEFALA  E não for as demais | 1 | Física |
| Se DEFICIENTEAUDITIVO e não for as demais | 2 | Auditiva |
| Se DEFICIENTEVISUAL e não for as demais | 3 | Visual |
| Se DEFICIENTEMENTAL e não for as demais | 4 | Intelectual ou Mental |
| Se mais de um caso acima | 5 | Múltipla |
| Se BRPDH independente dos casos acima | 6 | Reabilitado |
| Se não atende nenhum dos casos acima | 9 | Não Informado |

**Equivalência Nacionalidade TOTVS Folha de pagamento x Tabela 7 - Nacionalidade**

|  |  |  |
| --- | --- | --- |
| TOTVS  PPESSOA.NACIONALIDADE  Tabela dinâmica Nacionalidade (PCODNACAO) | Tabela 7 | Descrição |
| 10 | 10 | Brasileiro |
| 20 | 20 | Naturalizado Brasileiro |
| 30 | 21 | Alemão |
| 175 | 22 | Angolano |
| 21 | 23 | Argentino |
| 31 | 24 | Belga |
| 22 | 25 | Boliviano |
| 32 | 26 | Britânico |
| 34 | 27 | Canadense |
| 23 | 28 | Chileno |
| 42 | 29 | Chinês |
| 026 | 30 | Colombiano |
| 185 | 31 | Congolês |
| 43 | 32 | Coreano |
| 027 | 33 | Equatoriano |
| 35 | 34 | Espanhol |
| 37 | 35 | Francês |
| Ser criado | 36 | Haitiano |
| 255 | 37 | Indiano |
| 39 | 38 | Italiano |
| 41 | 39 | Japonês |
| 36 | 40 | Norte-americano (EUA) |
| 273 | 41 | Paquistanês |
| 24 | 42 | Paraguaio |
| 089 | 43 | Peruano |
| 45 | 44 | Português |
| 348 | 45 | Russo |
| 38 | 46 | Suíço |
| 173 | 47 | Sul - Africano |
| 25 | 48 | Uruguaio |
| 092 | 49 | Venezuelano |
| Ser criado na Tab.Dinam. PCODNACAO | 80 | Outros latino-americanos |
| Ser criado na Tab.Dinam.  PCODNACAO | 81 | Outros asiáticos |
| Ser criado na Tab.Dinam.  PCODNACAO | 82 | Outros Europeus |
| Ser criado na Tab.Dinam.  PCODNACAO | 83 | Outros Africanos |
| Ser criado na Tab.Dinam.  PCODNACAO | 99 | Outros |

**Equivalência Grau de Instrução TOTVS Folha de pagamento x Tabela 8  Grau de Instrução**

|  |  |  |
| --- | --- | --- |
| **TOTVS**  **PPESSOA.GRAUINSTRUCAO**  **Tabela Dinâmica "Grau de Instrução" (PCODINSTRUCAO)** | **Tabela 8** | **Descrição** |
| Se '2' ou '3' ou '4' | 10 | Fundamental Incompleto |
| '5' | 11 | Fundamental Completo |
| Deve ser criado na Tab.Dinam. PCODINSTRUCAO | 12 | Fundamental Completo (Técnico) |
| ‘6’ | 20 | Médio Incompleto |
| ‘7’ | 21 | Médio Completo |
| Deve ser criado na Tab.Dinam.  PCODINSTRUCAO | 22 | Técnico Incompleto |
| ‘7A’ | 23 | Técnico Completo |
| ‘8’ | 30 | Superior Incompleto |
| ‘9’ | 31 | Superior Completo |
| ‘A’ | 40 | Especialização ou MBA Incompleto |
| ‘B’ | 41 | Especialização ou MBA Completo |
| ‘C’ | 50 | Mestrado Incompleto |
| ‘D’ | 51 | Mestrado Completo |
| ‘E’ | 60 | Doutorado Incompleto |
| Se 'F' ou 'G' ou 'H' | 61 | Doutorado Completo |

**Calculo e Equivalência para Tabela 12 - Jornada de Trabalho**

|  |  |  |
| --- | --- | --- |
| **TOTVS Folha de Pagamento**  **PFUNC.JORNADAMENSAL / 60** | **Tabela 12** | **Descrição** |
| Igual 100 | 20 | 20 horas semanais |
| Igual 120 | 24 | 24 horas semanais |
| Igual 150 | 30 | 30 horas semanais |
| Igual 180 | 36 | 36 horas semanais |
| Igual 200 | 40 | 40 horas semanais |
| Igual 220 | 44 | 44 horas semanais |
| Diferente dos valores acima | 99 | Outras |

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(Patch a ser definido)* deste chamado.

1. Aplique o patch do chamado e execute uma vez a rotina*do executor de script para a criação dos cadastros, tabelas dinâmica e novos campos no TOTVS Folha de Pagamento e TOTOVS Gestão de Pessoas.*

## Procedimento para Configuração

1)      Baixe e instale o pach (a ser definido)

2)      Execute o script de criação no banco de dados para os novos cadastros, tabelas dinâmicas e campos dos cadastros já existente.

3)      Insira os dados no Cadastro de Rubrica Consolidada localizado no Menu RH / Folha de Pagamento / Encargos / Cadastros / Rubrica Consolidada. Será Polulado a tabela PRUBRICACONS

1. No Cadastro de Encargos em RH / Folha de Pagamento / Encargos / Cadastros. Vincule o código da Rubrica Consolidado aos encargos
2. No Cadastro de Despesas do Vitae em RH / Gestão de Pessoas / Gestão Organizacional / Tabela Auxilires / Tipos de Despesas. Vincule o código da Rubrica Consolidada.
3. Efetue a Geração de Encargos;
4. Efetue o lançamento de Despesas;
5. As informações de Encargos e Despesas irão compor o Registro “**Dados de Cada Dispêndio Consolidado**”.

4)      Informe pelo cadastro de pessoa ou pelo cadastro de funcionário o campo 1º Emprego em Documentação / Carteira de Trabalho.

5)      Popule a Tabela Dinâmica Motivo de Admissão Cliente (PMOTIVADMISSAOCLI ) com o de / para referente a tabela dinâmica Motivo de Admissão (PMOTADMISSAO). o código deve ser o mesmo da atual Motivo de Admissão, e na descrição informar o código da Tabela 19 – Motivo Desligamento.

6)      Popular a tabela dinâmica Órgão de Origem / Destino. (PORGAOORIGDEST) conforme a Tabela 10 - Código de Órgãos e vincular o seu código no Cadastro de funcionário na Aba Dados do Registro

7)      Popular a Tabela Dinâmica Regime Jurídico (PREGIMEJURIDICO) conforme a Tabela Tabela 11 - Regime Jurídico e vincular o seu código no Cadastro de funcionário na Aba Dados do Registro

8)      Informar o valor do Campo Anos De Contribuição INSS do Cadastro de Funcionário aba FGTS / SEFIP

9)      Popular a Tabela dinâmica Área de Atuação e vincular ao campo Área de atuação no cadastro de seção Na Aba Identificação. Tabela 14 - Área de Atuação do Empregado.

**10)** Popular a Tabela Dinâmica Tipo de Benefício (PTIPOBENEFICIO ) e vincular aos Eventos no Cadastro de Eventos Na Aba Identificação. A fim de compor o registro “**Dados de Benefícios”**

11)    Deve ser informado os novos campos no cadastro de cargo a saber:Sigla do Plano, Situação, Sigla do Cargo e Código de Classificação do Cargo. Para Este último é necessário inserir os dados no cadastro Classificação do Cargo (PCODCLASSCARGO) em RH / Folha de Pagamento / Cargos/Funções / Classificação do Cargo. Tabela 16 - Classificação de Cargo/Função

12)    Deverá popular a tabela Dinâmica Tipo de Função ( PCODTIPOFUNCAO)

13)    No cadastro de função vincular o Tipo de Função para compor o Registro “**Dados da Função**”, Informa também os novos campos: SIGLA, Código de classificação do cargo.

**14)**Efetuar o de para entre as Tabelas dinâmicas "Motivo de Mudança de Situação Cliente" (PMOTIVAFASTCLIENTE)  e “Motivo de Mudança de Situação” (PMUDSITUACAO)  o código deve ser o mesmo do Motivo de Situação Atual, e na descrição informar o código relativo a Tabela 18 – Motivo de Afastamento/Licença. A fim de ser preenchido o campo Motivo do Afastamento ou Licença do registro **Dados de Afastamento e Licenças / Dados de Cada Ocorrência.**

**15)** Efetuar o de para entre as Tabelas dinâmicas “Motivo de Demissão Cliente” (PMOTIVDEMISSAOCLI)  e “Motivo de Demissão” (PMOTIVDEMISSAO)  o código deve ser o mesmo do Motivo de Demissão Atual, e na descrição informar o código relativo a Tabela 19 – Motivo Desligamento. A fim de ser preenchido o campo “Motivo do Desligamento” do Motivo do Desligamento**.**

16)    Inserir os dados da Tabela 3-Rubricas Individuais (PRUBINDIVIDUAL) em RH / Folha de Pagamento / Administração de Pessoal / Evento / Rubricas Individuais. No cadastro de Evento em Identificação vincular o evento a sua Rubrica individual. Esta informação será utilizada para compor o campo “Rubrica – Código” do Registro “**Dados de Cada Dispêndio**”.

17)    Informar o código empresa a ser demonstrado no campo “Formação – Código” do Registro “Dados de Cada Formação Profissional” no cadastro de Cursos do TOTVS Gestão de Pessoa.

18)    Popular a Tabela dinâmica Tipo de Desconto (PTPDESCONTO) referente a Tabela 22 – Tipo de Desconto em Folha. E Vincular aos eventos de Desconto no Cadastro de Evento na Aba “Inc. Desconto”.

19)    Popular a Tabela Dinâmica Motivo de Exclusão (PMOTIVEXCLUSAO). Usa para vincular ao móvito de excluso ao empréstimo do funcionário, vinculado há um evento em que o tipo de desconto tenha sido informado.

20)    Nos Empréstimos contraído pelos Funcionários caso o código do tipo de desconto vinculado ao evento do empréstimo seja do tipo ‘99’ deverá informar os novos campos a saber:

1. Banco - Código Compensação
2. Contrato - Número Identificador
3. Contrato - Data Final
4. Quantidade de Parcelas
5. Data - Exclusão do Contrato
6. Motivo da Exclusão do Contrato, obtido pela Tabela Dinâmica Motivo de Exclusão (PMOTIVEXCLUSAO).

21)  No parametrizar do TOTVS Folha de pagamento em RH / Folha de Pagamento / Configurações / Parametrizador / 06.01.07 - Perfil de Pessoal das Estatais. informar os eventos que irão compor:

1. PPE / Eventos que compõem ao Valor da Função: usado no campo Valor da Função nos Dados da Função. (PEVTVALORFUNCAO)
2. PPE / Eventos que compõem ao Valor do Complemento: usado no campo Valor do Complemento nos Dados da Função. (PEVTVALORCOMPL)

## Procedimento para Utilização

1)      Antes de acionar o PPE. Certifique-se que:

1. As Despesas com pessoal tenha sido lançada
2. Os Encargos tenha sido gerado;
3. A Folha de Pagamento tenha sido processada

2)      Acesse no Menu *Folha Mensal / Relatórios da Folha / PPE O Wizzard para gerar o PPE.*

3)      *No primeiro passo informe dados básicos do código de quebra, filtro de funcionário, ano mês de competência, caminho e nome do arquivo a ser gerado o PPE. Estes dados serão comuns a todas as coligadas*

4)      O próximo passo informe os dados para Usuário, Senha, Data de Criação e Data de Expiração que irá compor o registro “**Dados Header Autenticação”.**

5)      *O próximo passo é apresentado a lista de coligadas onde pode ser personalizado todos os dados solicitado nos passos anteriores para cada coligada.*

6)      *O Passo final é a confirmação do processo. O TOTVS Folha de pagamento irá gravar o arquivo com o nome e no diretório informado em um subdiretório denominado “Coligada99” onde 99 é código da coligada.*

divs
