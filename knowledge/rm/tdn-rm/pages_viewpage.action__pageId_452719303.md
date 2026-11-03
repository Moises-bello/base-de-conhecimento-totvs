---
content_hash: e8f72dc35850276bf1de2608595b07e45c12fa95a4904bbc0acd933783507f3f
fetched_at: '2026-06-29T00:10:05.845554+00:00'
page_id: '452719303'
product: rm
source: tdn-rm
title: PPE – Perfil de Pessoal das Estatais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719303
version: 8
---

## Objetivo

Desde março de 2014, o Departamento de Coordenação e Governança das Empresas Estatais (DEST) tornou obrigatório o envio mensal de informações pelas empresas por meio do **Sistema de Informações das Empresas Estatais (Siest)**.

O **PPE** (Plano de Profissionais das Estatais) compõe um dos cinco módulos do sistema, que dá suporte ao Ministério nas tomadas de decisão estratégicas.

O envio do PPE deve ser realizado **mensalmente, até o dia 15 do mês subsequente à competência**

🔔 **ATENÇÃO**

* + A geração do XML é **aplicável exclusivamente às Empresas Estatais Federais**, incluindo aquelas **dependentes do Tesouro Nacional**.
  + O processo de geração **não oferece suporte para eventos do tipo "Base de Cálculo"**.

O arquivo deve contemplar **todos os empregados com contrato de trabalho ativo**, incluindo:

* Cedidos e requisitados;
* Afastados ou licenciados, independentemente da natureza da licença;
* Detentores de cargos comissionados ou de função de confiança (inclusive de livre provimento);
* Dirigentes e conselheiros.

Além disso, o arquivo deve refletir a **situação cadastral vigente no último dia do mês de competência da informação**, abrangendo todos os vínculos citados.

## Documentação

O **TOTVS Folha de Pagamento** implementa o **PPE** com base nas seguintes regras e documentações oficiais:

1. **Manual do DEST/PPE**  
   [Manual do PPE – Versão 1.1d (PDF)](https://www.gov.br/economia/pt-br/arquivos/planejamento/arquivos-e-imagens/secretarias/Arquivos/dest/documentacao/manual_do_ppe-versao-1-1d.pdf)
2. **Layout do Arquivo**  
   Define tipos, tamanhos, obrigatoriedade e hierarquia dos campos.  
   Leiaute\_Arquivo\_Versao\_1\_1c.xls
3. **Tabelas Auxiliares**  
   Contém os valores de referência utilizados nos campos do PPE.  
   tabelas\_auxiliares\_v\_1\_1\_f\_setembro2014.xls

🔔 **ATENÇÃO:**  
O parâmetro referente ao PPE está disponível **somente a partir da versão 12.1.31**.  
Para versões anteriores, será necessária a execução de um **script específico** na base de dados, que será liberado pela área de desenvolvimento mediante solicitação do usuário.

## Parametrização

No menu Administração de Pessoal | Funcionários, foi criada a aba "PPE". Para habilitar essa aba é necessário acessar o menu Parametrizador | Folha Normal | Geral 2/2 e marcar o parâmetro "Utiliza PPE".

Antes de gerar o PPE pela primeira vez, é necessário realizar o preenchimento de novos cadastros e configurações feitos de acordo com a necessidade do relatório, e a disponibilidade do Totvs Folha de Pagamento.  
   
1.     Cadastro de Funcionários - Foram criados novos campos:  
1.1.   Cadastro do Funcionário/Pessoa I Documentação:  
ü   Ano do Primeiro Emprego: Informar o ano do primeiro emprego do funcionário. Esse dado será levado para o campo "Ano do Primeiro Emprego" do registro "Dados do Empregado".  
1.2.   Cadastro do Funcionário/Pessoa I PPE:  
ü   Anos de Contribuição ao INSS: Informar o Tempo "em anos" de contribuição do empregado para o INSS - Instituto Nacional de Seguro Social, com dois algarismos. Caso seja o primeiro ano de contribuição do funcionário, esse campo não existirá no arquivo. Esse dado será levado para o campo "Anos de Contribuição para o INSS" do registro "Dados do Empregado".  
ü   Órgão de Origem/Destino: Informar o código do Órgão de Origem/Destino para o qual o empregado foi requisitado ou cedido, conforme Tabela 10 – Código de Órgãos. Esse dado será levado para o campo "Órgão de Origem / Destino" do registro "Dados do Empregado".  
ü   Regime Jurídico: Informar regime jurídico do empregado, conforme códigos constantes na Tabela 11 – Regime Jurídico. Esse dado será levado para o campo "Regime Jurídico" do registro "Dados do Empregado".  
1.3.   Cadastro do Funcionário I Anexos I Empréstimos: Nos Empréstimos contraído pelos Funcionários caso o código do tipo de desconto vinculado ao evento do empréstimo seja do tipo "99 - Empréstimo Consignado em Instituições Financeiras" deverá informar obrigatoriamente os novos campos do cadastro de empréstimo na aba PPE Consignado:  
ü   Banco Compensação: Informar o código COMPE do Sistema de Compensação Nacional atribuído para Instituição Financeira credora conforme a Tabela 23 – Instituições Financeiras. Esse dado será levado para o campo "Banco – Código Compe" do registro "Dados de Descontos em Folha".  
ü   Código do Contrato: Informar o código identificador do contrato do empréstimo consignado. Esse dado será levado para o campo "Contrato – Número Identificador" do registro "Dados de Descontos em Folha".  
ü   Data Final Prevista: Informar a data final prevista para a liquidação do contrato. Esse dado será levado para o campo "Contrato – Data Final" do registro "Dados de Descontos em Folha".  
ü   Data de Exclusão: No mês de liquidação do contrato ou da liquidação antecipada do empréstimo, informar a data do pagamento. Esse dado será levado para o campo "Data de Exclusão do Contrato" do registro "Dados de Descontos em Folha".  
ü   Motivo de Exclusão da Operação: Informar o código do motivo da exclusão do contrato, conforme códigos constantes da Tabela 24 – Motivo da Exclusão da Operação. Esse dado será levado para o campo "Motivo da Exclusão" do registro "Dados de Descontos em Folha".  
   
Atenção: Caso a empresa trabalhe com a importação de empréstimo consignado, fazendo apenas o lançamento diretamente no envelope do funcionário, será necessário o preenchimento desse cadastro para levar as informações corretamente.  
   
2.     Cadastro de Eventos - Foram criados novos campos localizados na aba PPE:  
ü   Tipo de Benefício: Ficará disponível para eventos do tipo "Provento", onde deverá informar o código do benefício, conforme definido na Tabela 15 – Tipo de Benefícios. Esse dado será levado para o campo "Tipo de Benefício" do registro "Dados de Benefícios".  
ü   Tipo de Desconto: Ficará disponível para eventos do tipo "Desconto", onde deverá informar o código do benefício, conforme definido na Tabela 22 – Tipo de Desconto em Folha. Esse dado será levado para o campo "Desconto - Código" do registro "Dados de Descontos em Folha".  
   
3.     Cadastro de Seção – Foi criado novo campo localizado na aba PPE:  
ü  Área de atuação: Área atual em que o empregado encontra-se em atuação na empresa conforme códigos definidos na Tabela 14 – Área de Atuação do Empregado.  
   
4.     Cadastro de Cargo – Foram criados novos campos localizado na aba Identificação:  
ü  Sigla: Informar a Sigla do cargo efetivo (emprego) ao qual o empregado encontra-se vinculado/enquadrado. Esse dado será levado para o campo "Cargo Efetivo - Sigla" do registro "Dados do Cargo Efetivo".  
ü  Classificação de Cargo/Função PPE: Informar o código de classificação da "Ocupação – Nome" ou do "Cargo Efetivo" do empregado, conforme códigos de constantes da Tabela 16 – Classificação de Cargo/Função. Esse dado será levado para o campo "Classificação do Cargo" do registro "Dados do Cargo Efetivo".  
   
5.     Cadastro de Função – Foram criados novos campos localizado na aba PPE:  
ü  Sigla: Informar a sigla da função/cargo. Ex: "ANA", "Analista", "ENG", etc. Esse dado será levado para o campo "Função - Sigla" do registro "Dados da Função".  
ü  Tipo de Função: Informar o código do tipo de função, de acordo com o estabelecido na Tabela 17 - Tipo de Função. Esse dado será levado para o campo "Função - Tipo" do registro "Dados da Função".  
   
6.     Cadastro de Grupos Ocupacionais – Foi criado um novo campo localizado na aba Identificação:  
ü  Código do Plano de Cargos: Informar o código do Plano de Cargos que associado ao Grupo ocupacional será vinculado ao Cargo do Funcionário.   
   
7.     Cadastro de Plano de Cargos (Totvs Gestão de Pessoas) – Foi criado um novo cadastro no Totvs Gestão de Pessoas, na Guia Gestão Organizacional I Tabelas Auxiliares I Plano de Cargos:  
ü  Código do Plano: Informar o código do plano de cargos para associação aos Grupos Ocupacionais.  
ü  Sigla: Sigla do Plano de Carreira, Cargos e Salários ao qual o empregado de carreira se encontra vinculado atualmente. Ex.: PCS, PCCS, SIRD, RAR1, etc. Esse dado será levado para o campo "Plano de Cargo - Sigla" do registro "Dados do Cargo Efetivo".  
ü  Descrição: Descrição do Plano de Cargos.  
ü  Situação: Informar a situação atual do Plano de Cargos ao qual o empregado de carreira se encontra vinculado. Situações válidas: "em operação", "em extinção" ou "em implantação". Esse dado será levado para o campo "Plano de Cargo - Situação" do registro "Dados do Cargo Efetivo".  
   
8.     Cadastro de Cursos Acadêmicos (Totvs Gestão de Pessoas) – Foi criado um novo campo no cadastro de Cursos Acadêmicos localizado na guia Planejamento e Captação I Tabelas Auxiliares I Cursos Acadêmicos no Totvs Gestão de Pessoas:  
ü  Código do curso na tabela 21 do PPE: Informar o código do curso/formação que o empregado detém, conforme definido na Tabela 21 – Cursos. Devem ser informados todos os cursos concluídos (completos) pelo empregado (nível superior, especialização ou MBA, mestrado ou doutorado). Esse dado será levado para o campo "Formação - Código" do registro "Dados de Formação Profissional".  
   
Obs.: Funcionário de nível superior completo, de grau de instrução 9 ou que possui letras: A, B, C, D, E, F, G, H e não tem formação Acadêmica Cadastrada o sistema irá incluir automaticamente a formação Acadêmica de código "3199999999 - Não disponível", conforme previsto na Tabela 21 – Cursos.  
   
9.     Cadastros PPE - Foram incluídos novos cadastros com informações exclusivas para geração do PPE localizados na guia PPE I Cadastros:  
   
9.1.   **Eventos Compõe Valor Função:** informe o código dos eventos que se lançados no envelope do funcionário serão somados e usados no campo "Valor da Função" no Registro "Dados da Função".   
   
9.2.   **Eventos Compõem Valor Complemento:** informe o código dos eventos que se lançados no envelope do funcionário serão somados e usados no campo "Valor do Complemento" no Registro "Dados da Função".   
   
   
9.3.   **Motivos Admissão TOTVS x PPE:** nas tabelas auxiliares do PPE existem motivos de admissão fixados (Tabela 9 – Motivo de Admissão) que podem não existir na base do Totvs Folha de Pagamento. Para isso foi criado o cadastro de relacionamentos, ou seja, um De/Para, onde o usuário deve informar o Motivo de Admissão existente no Totvs Folha de Pagamento e o que será relacionado no arquivo do PPE. Esses dados serão levados para o campo "Motivo de Admissão" no registro "Dados de Cada Empregado/Dados Básicos".  
   
9.4.   **Motivos Afastamento TOTVS x PPE:** nas tabelas auxiliares do PPE existem motivos de afastamento fixados (Tabela 18 – Motivo Afastamento) que podem não existir na base do Totvs Folha de Pagamento. Para isso foi criado o cadastro de relacionamentos, ou seja, um De/Para, onde o usuário deve informar o Motivo de Afastamento existente no Totvs Folha de Pagamento e o que será relacionado no arquivo do PPE. Esses dados serão levados para campo "Motivo do Afastamento ou Licença" do registro "Dados de Afastamento e Licenças/Dados de Cada Ocorrência".  
   
9.5.   **Motivos Demissão TOTVS x PPE:** nas tabelas auxiliares do PPE existem motivos de demissão fixados (Tabela 19 - Motivo Desligamento) que podem não existir na base do Totvs Folha de Pagamento. Para isso foi criado o cadastro de relacionamentos, ou seja, um De/Para, onde o usuário deve informar o Motivo de Demissão existente no Totvs Folha de Pagamento e o que será relacionado no arquivo do PPE. Esses dados serão levados para o campo "Motivo do Desligamento" no registro "Dados de Desligamento".  
   
9.6.   **Lançamento Manual de Dispêndio:** o usuário poderá realizar o lançamento manual de qualquer valor e quantidade de funcionários a ser levado para o registro de "Dispêndio Consolidado". Será considerado o mês e ano de competência, e o código do dispêndio consolidado, que deve ser cadastrado previamente. Apenas serão apresentados os dispêndios que sejam do tipo "Lançamento Manual".  
   
9.7.   **Dispêndio:** São informações sobre dispêndios com pessoal efetuados pela empresa, que podem ser apurados de forma consolidada ou individual por empregado.  
Deverão ser incluídos apenas os dispêndios utilizados pela empresa conforme os códigos existentes nas tabelas auxiliares 2 - Rubricas Consolidadas e 3 - Rubricas Individuais.  
O campo "Consolidado" serve para diferenciar se o dispêndio é individual ou consolidado. Quando estiver marcado será considerado um dispêndio consolidado, ou seja, que não é apurado de forma individualizada por empregado. Marcando esse parâmetro será habilitado o "Tipo de Obtenção" do dispêndio, ou seja, de onde serão buscados os valores e a quantidade de funcionários para a competência informada. Esses dados serão levados para os campos "Rubrica - Código", "Rubrica - Valor" e "Quantidade de Empregados" do registro "Dados de Dispêndios Consolidados". Os dispêndios consolidados podem ter os seguintes tipos de obtenção:  
ü   Encargos: Marcando esse tipo de obtenção, habilitará no cadastro do dispêndio a guia "Encargo", onde deverá ser informado os códigos dos encargos desejados para compor esse dispêndio consolidado. O sistema buscará os valores do histórico de encargos de acordo com os encargos informados.  
ü   Despesas do Vitae: Marcando esse tipo de obtenção, habilitará no cadastro do dispêndio a guia "Despesa", onde deverá ser informado os códigos das despesas do Vitae. As despesas são lançadas às turmas participante do funcionário, e serão consideradas de acordo com a sua data de lançamento.  
ü   Fórmula: Marcando esse tipo de obtenção, habilitará no cadastro do dispêndio um campo para informar a fórmula para o cálculo do valor do dispêndio. A fórmula será executada para cada funcionário, e o tratamento para a seleção desses funcionários deverá também ser feito na fórmula.  
ü   Eventos: Marcando esse tipo de obtenção, habilitará no cadastro do dispêndio a guia "Evento", onde deverá ser informado os códigos dos eventos desejados para compor esse dispêndio consolidado. O sistema buscará os valores da ficha financeira do funcionário.  
ü   Lançamento Manual: Marcando esse tipo de obtenção, não será habilitado nenhum outro campo, ele apenas será considerado para a informação do lançamento manual de dispêndio informado acima.  
Quando o Dispêndio for individual, ou seja, quando não marcar o parâmetro "Consolidado", o sistema assume automaticamente o tipo de obtenção "Eventos", habilitando a aba de seleção de eventos. Nesse caso os valores dos eventos lançados na ficha financeira do funcionário para a competência serão levados para os campos "Rubrica - Código" e "Rubrica – Valor" do registro "Dados de Cada Dispêndio".  
   
10.  PPE – Perfil de Pessoal das Estatais I Processo:  
Antes de acionar o PPE. Certifique-se que:  
   
ü  As Despesas com pessoal tenha sido lançada;  
ü  Os Encargos tenha sido gerado;  
ü  A Folha de Pagamento tenha sido processada;  
ü  O Valores de Dispêndio tenha sido lançados.  
   
No primeiro passo informe ano e mês de competência, período a ser considerado, dados básicos do código de quebra, filtro de funcionário, o caminho do arquivo a ser gerado o PPE e o Código SIEST Empresa (Conforme Tabela 1 - Codigo Siest das tabelas auxiliares).  
   
O próximo passo é apresentado a lista de coligadas onde pode ser personalizado os dados solicitados anteriormente para cada coligada.  
   
O Passo final é a confirmação do processo. O TOTVS Folha de pagamento irá gravar o arquivo com o nome e no diretório informado em um subdiretório denominado "Coligada 99" onde 99 é código da coligada.  
   
Dicas:  
ü  É necessário que o "De/Para de Endereço" localizado em Configurações I Parametrizador I eSocial esteja configurado. Isso será importante para que o sistema busque adequadamente o código do município a ser levado para o campo "Local de Trabalho" no registro "Dados dos Empregados". Além disso, informações como Histórico de seção e o endereço do cadastro da seção do funcionário também serão considerados. Caso não existam esses dados, o "Local de Trabalho" não será levado para o arquivo do PPE.  
ü  Os Históricos de seção, situação, função, salarial e afastamento sempre serão verificados durante a geração do PPE para informação de vários dados, por isso é importante que os mesmos estejam corretamente informados ou dados relacionados poderão não ser levados para o PPE.  
ü  Caso algum dado esteja com informação em branco ou zerada, o dado ou o bloco do registro relacionado poderá não ser gerado no PPE.

## Validação dos dados:

**Dados da Empresa Estatal**  
Os campos abaixo são informados no assistente do processo de geração do PPE.

|  |  |  |  |
| --- | --- | --- | --- |
| **Campo** | **Tag** | **Origem** | **Regra** |
| Competência - Ano e Mês | <anomescompetencia> | Parâmetro do Processo | Competência – Ano e Mês |
| Código SIEST da Empresa | <codigosiestempresa> | Parâmetro do Processo | Código SIEST da Empresa conforme Tabela 1 – Código SIEST |

**Dados de Cada Dispêndio Consolidado**  
Neste registro são demonstrados valores e quantidade de funcionários conforme registrado no Cadastro de Dispêndio e/ou Lançamento Manual de Dispêndio.

|  |  |  |  |
| --- | --- | --- | --- |
| **Campo** | **Tag** | **Origem** | **Regra** |
| Rubrica – Código | <codigorubricaconsolidado> | Cadastro de Dispêndio  (PDISPENDIO.CODSPE) | Código provindo do Cadastro de Dispêndio em que foi marcado o parâmetro "Consolidado". Os Dispêndios Consolidados deverão ser codificados conforme a Tabela 2-Rubricas Consolidadas. |
| Rubrica – Valor | <valorrubricaconsolidado> | Valor Calculado  1)     PFENCARGO.VALOR  2)     VDESPESA.VALOR  3)     Valor calculado pela fórmula  4)     PFFINANC.VALOR  5)     PFDISPENDIOCONSOLIDADO.VALOR | Somatório dos valores do dispêndio consolidado para cada código SPE, referente a competência informada, conforme a configuração feita:  1)     Encargos; ou  2)     Despesas com Pessoal do Vitae Ligado a pessoa do funcionário; ou  3)     Fórmula para obtenção do Valor. A quantidade será calculada pelo somatório de funcionário que o valor da formula seja maior que zero: Neste tipo o sistema irá processar cada funcionário executará a formula de cada dispêndio. Ao final irá sumarizar o valor por dispêndio e contará a quantidade de funcionário com valor maior que zero; ou  4)     Eventos lançados no Envelope; ou  5)     Lançamento Manual de dispêndio |
| Quantidade de Empregados | <quantidadebeneficiados> | Quantidade Calculada | Total de funcionários classificados pelo código de pessoa que participaram do dispêndio consolidado na competência referente ao Código SPE. Caso uma pessoa conste em mais de uma despesa, encargo e etc. para o mesmo Código SPE dentro da competência, ainda assim, deverá contabilizar apenas uma única vez para cada Código SPE. |

**Dados de Cada Empregado / Dados Básicos**  
Neste registro é informado todos os funcionários conforme definido no filtro do processo de emissão do PPE.

|  |  |  |  |
| --- | --- | --- | --- |
| **Campo** | **Tag** | **Origem** | **Regra** |
| CPF | <cpfempregado> | Cadastro de Funcionário/Pessoa  PPESSOA.CPF | Campo CPF do cadastro de pessoa |
| PIS / PASEP | <pispasep> | Cadastro de Funcionário  PFUNC.PISPASEP | Campo PIS/PASEP do cadastro de pessoa |
| Nome da Mãe | <nomemae> | Cadastro de Funcionário I Dependentes  PFDEPEND.NOME de grau 7 | Nome do dependente de grau 7 vinculado ao Funcionário.  Se não houver será informado "Sem Registro" |
| Carteira Trabalho | <carteiratrabalho> | Cadastro de Funcionário/Pessoa  PPESSOA.CARTEIRATRAB | Carteira de trabalho do cadastro de pessoa |
| Carteira Trabalho - Série | <seriecarteiratrabalho> | Cadastro de Funcionário/Pessoa  PPESSOA.SERIECARTTRAB | Serie da Carteira de trabalho do cadastro de pessoa |
| Carteira Trabalho - UF | <ufcarteiratrabalho> | Cadastro de Funcionário/Pessoa  PPESSOA.UFCARTTRAB | UF Carteira de trabalho do cadastro de pessoa |
| Ano do Primeiro Emprego | <anoprimeiroemprego> | Cadastro de Funcionário/Pessoa  PPESSOA.ANO1EMPREGO | Campo "Ano do Primeiro Emprego" do cadastro de pessoa |
| Matrícula | <matricula> | Cadastro de Funcionário  PFUNC.CHAPA | Chapa do cadastro de funcionário |
| Sexo | <sexo> | Cadastro de Funcionário/Pessoa  PPESSOA.SEXO | Campo sexo da Pessoa |
| Data de Nascimento | <datanascimento> | Cadastro de Funcionário/Pessoa  PPESSOA.DTNASCIMENTO | Campo da Data de Nascimento do cadastro de Pessoa |
| Raça / Cor | <racacor> | Cadastro de Funcionário/Pessoa  PPESSOA.CORRACA | Conforme Tabelas de Equivalência Cor/Raça TOTVS Folha de pagamento x Tabela 5 - Raça-Cor. |
| Pessoa com Deficiência | <deficientehabilitado> | Cadastro de Funcionário/Pessoa  PPESSOA | Análise dos campos do cadastro de Pessoa. Se (DEFICIENTEFISICO ou DEFICIENTEAUDITIVO ou DEFICIENTEFALA ou DEFICIENTEVISUAL ou DEFICIENTEMENTAL ou BRPDH) forem marcados então retornará "S", caso contrário retornar "N". |
| Tipo de Deficiência | <tipodeficiencia> | Cadastro de Funcionário/Pessoa  PPESSOA | Será verificado o cadastro de Funcionário, aba RAIS grupo "Deficiente" conforme Tabelas de Equivalência Tipo de Deficiência TOTVS Folha de pagamento (Campo de pessoa) x Tabela 6 Tipos de Deficiência.  Este campo é obrigatório se Pessoa com Deficiência = "S". |
| Nacionalidade | <nacionalidade> | Cadastro de Funcionário/Pessoa  PPESSOA.NACIONALIDADE | Conforme Tabelas de Equivalência Nacionalidade TOTVS Folha de pagamento x Tabela 7 Nacionalidades |
| Ano de Chegada no Brasil | <anochegada> | Cadastro de Funcionário/Pessoa  PPESSOA.DATACHEGADA | Obter o ano no formato AAAA. Campo "Data de Chegada ao Brasil" do Cadastro de Pessoa I Documentos Estrangeiros  Obs.: Esse campo é obrigatório somente se nacionalidade <> "10" e <> "20" |
| Grau de Instrução | <grauinstrucao> | Cadastro de Funcionário/Pessoa  PPESSOA.GRAUINSTRUCAO | Conforme Tabelas de Equivalência Grau de Instrução TOTVS Folha de pagamento x Tabela 8 - Grau de Instrução |
| Data de Admissão | <dataadmissao> | Cadastro de Funcionário  PFUNC.DATAADMISSAO | Campo Data de Admissão do Cadastro de Funcionário |
| Motivo de Admissão | <motivoadmissao> | Cadastro Motivo Admissão TOTVS X PPE  PMOTIVADMISSAOCLI.CODPPE | Obtido do cadastro "Motivo Admissão TOTVS x PPE". O usuário deverá fazer o De/Para entre a Tabela Dinâmica Motivo de Admissão e o motivo de Admissão PPE de acordo com a Tabela 09 – Motivo de Admissão. |
| Órgão de Origem / Destino | <orgaoorigemdestino> | Cadastro de Funcionário  PFUNC. CODORGORIDES | Campo Órgão Origem/ Destino de acordo com a Tabela 10 - Código de Órgãos.  Este campo é obrigatório se: **Motivo de Admissão** = "20" ou "21"; ou  **Motivo do Afastamento ou Licença** = "40", "41", "71", "80", "81", "85" ou "86". |
| Regime Jurídico | <regimejuridico> | Cadastro de Funcionário  PFUNC. CODREGJURI | Campo Regime Jurídico conforme informado na Tabela 11 - Regime Jurídico. |
| Anos de Contribuição para o INSS | <anoscontribuicao> | Calculado.  PFUNC.DATAADMISSAO  PFUNC.ANOSCONTRIBINSS | Será o somatório dos anos completos referente a data de admissão até a competência informada e o valor existente no campo "Anos De Contribuição ao INSS" do Cadastro de Funcionário. |
| Aposentadoria - Ano/Mês | <anomesaposentadoria> | Cadastro de Funcionário  PFUNC.DTAPOSENTADORIA | Ano e Mês do campo "Data de Aposentadoria" do Cadastro de Funcionário Aba Situação.  O campo será levado se:  1)     O funcionário estiver ativo, ou seja, ultima situação na competência informada for diferente de Demissão;  2)     A data da aposentadoria estiver preenchida;  3)     O Motivo da Admissão for 10, 11, 22 ou 23. |
| Jornada de Trabalho | <jornadatrabalho> | Cadastro de Funcionário  PFUNC.JORNADAMENSAL | Conforme Tabelas de Equivalência De/Para Tabela 12 - Jornada de Trabalho.  Obs.: Não serão considerados os minutos de jornadas. Exemplo: 120:30h será considerada a faixa de 120 h. |
| Ocupação CBO | <ocupacaocbo> | Cadastro de Função  PFUNCAO.CBO2002 | Somente números, sem ponto, espaços, traços ou hífen. Verificado o registro existente no histórico de função no último dia da competência informada. |
| Local de Trabalho - Município | <codigomunicipio> | Cadastro de Seção  PSECAO.CODMUNICIPIO | O sistema tomará como base o código do município da última seção do funcionário conforme a competência informada. E através do relacionamento com as tabelas de classificação de município obtém o código a ser informado no PPE.  Para isso deverá informar a classificação do município no Parametrizador. E fazer os devidos relacionamentos de acordo com a tabela 20 – Municipios no cadastro de municípios. |
| Área de Atuação | <areaatuacaocargo> | Cadastro de Seção  PSECAO.CODAREAATUACAO | Campo Área de Atuação vinculado a seção do funcionário conforme seu histórico de seção no último dia da competência informada. |

**Dados de Benefícios**  
Informar somente no caso de o empregado receber, no mês de competência das informações, um ou mais Benefícios constantes da Tabela 15 – Tipo de Benefícios.

|  |  |  |  |
| --- | --- | --- | --- |
| **Campo** | **Tag** | **Origem** | **Regra** |
| Tipo de Benefício | <tipobeneficios> | Ficha Financeira / Cadastro de Eventos / Tabela Dinâmica PPETAB15 | O tipo de benefício é vinculado no cadastro de eventos para eventos do tipo "Provento" ou "Base" (PEVENTO.CODTPBENEFICIO).  Serão listados os tipos de benefícios que foram vinculados aos eventos lançados no envelope de pagamento do funcionário para o mês/ano de geração (PFFINANC). |

**Dados do Cargo Efetivo:**  
Informações sobre Carreira e Cargo Efetivo do funcionário. Preencher os campos constantes nesse bloco, somente no caso de empregado de carreira do quadro permanente da empresa, admitidos conforme códigos 10, 11, 22 e 23 da Tabela 9 – Motivo de Admissão (Analisar o "De / Para" para equivalência Motivo Admissão Cliente). Para os demais empregados não preencher os campos constantes nesse bloco de informações.  
O TOTVS Folha de Pagamento não implementa detalhamento de Ocupação para o Cargo. A Ocupação somente é tratado pelo código CBO vinculado a função. Sendo assim as informações de Ocupação serão as mesmas já definida pelo cargo.  
Deve ser observado o histórico de função referente ao último dia da competência informada a fim de obter o cargo relacionado a função, o grupo ocupacional vinculado ao cargo e por fim o plano de cargos existente no grupo ocupacional. Na inexistência de algum desses dados as informações desse bloco de registro poderão não ser levados para o arquivo PPE.  
O Dados de Tabela, Faixa, Nível e Referencia Salarial são obtidos do TOTVS Gestão de Pessoas (Vitae) vinculados ao funcionário.

|  |  |  |  |
| --- | --- | --- | --- |
| **Campo** | **Tag** | **Origem** | **Regra** |
| Plano Cargos e Salários - Sigla | <siglaplano> | Cadastro de Plano de Cargos (Totvs Gestão de Pessoas)  VPLANOCARGO. SIGLAPLANO | Campo Sigla do Cadastro de Planos que é vinculado ao Grupo Ocupacional do cadastro do Cargo, que por sua vez é relacionado à função existente no histórico de função do último dia da competência informada. |
| Plano Cargos e Salários - Situação | <situacaoplano> | Cadastro de Plano de Cargos (Totvs Gestão de Pessoas)  VPLANOCARGO.SITUACAO | Campo Sigla do Cadastro de Planos que é vinculado ao Grupo Ocupacional do cadastro do Cargo, que por sua vez é relacionado à função existente no histórico de função do último dia da competência informada.  Dados Válidos são: 1 – "Em Operação"; 2 – "Em Extinção"; 3 – "Em Implantação". |
| Carreira | <carreira> | Cadastro do Grupo Ocupacional  VGRUPOOCUPACIONAL.DESCRICAO | Campo Descrição do grupo ocupacional associado ao Cargo da Função existente no histórico de função do último dia da competência informada. |
| Cargo Efetivo - Nome | <cargoefetivo> | Cadastro de Cargo  PCARGO.NOME | Campo Descrição do Cargo do Cargo que por sua vez foi vinculado a função referente ao histórico de função do último dia da competência informada. |
| Cargo Efetivo - Sigla | <siglacargo> | Cadastro de Cargo  PCARGO.SIGLA | Campo Sigla do Cargo que por sua vez foi vinculado a função referente ao histórico de função do último dia da competência informada. |
| Cargo Efetivo - Código | <codigocargo> | Cadastro de Cargo  PCARGO.CODIGO | Campo Código do Identificador do Cargo que por sua vez foi vinculado a função referente ao histórico de função do último dia da competência informada. |
| Faixa Salarial | <faixasalarialcargo> | Histórico de Função / Cadastro de funcionários  PFHSTFCO.CODNIVEL / PFUNC.CODNIVELSAL / Única | Referente a tabela, e nível do funcionário. Conforme seu histórico de Função. Não existindo no histórico de função buscará do cadastro de funcionário.  No caso de inexistência do nível salarial no histórico de função e no cadastro do funcionário, será informado neste campo a palavra "Única". |
| Referência Salarial | <graucargo> | Histórico de Função / Cadastro de funcionários  PFHSTFCO.CODNIVEL / PFUNC.GRUPOSALARIAL / Única | Referente a tabela, e Faixa do funcionário conforme seu histórico de Função. Não existindo no histórico de função buscará do cadastro de funcionário.  No caso de inexistência da faixa salarial no histórico de função e no cadastro do funcionário, será informado neste campo a palavra "Única". |
| Salário Base | <salariobase> | Histórico Salarial / Cadastro do funcionário  PFHSTSAL.VALOR  PFUNC.SALARIO | Referente ao valor informado no histórico salarial do funcionário na competência informada.  No caso de inexistência do histórico salarial será retornado o campo Salário do Cadastro do Funcionário. |
| Ocupação - Nome | <nomeocupacao> | Cadastro de Cargo  PCARGO.NOME | TOTVS Folha de Pagamento Não implementa este detalhamento. Será o mesmo valor informado no campo Cargo Efetivo - Nome  Se não houver, repetirá o nome do cargo efetivo constante do Plano de Cargos. |
| Ocupação - Sigla | <siglaocupacao> | Cadastro de Cargo  PCARGO.SIGLA | TOTVS Folha de Pagamento Não implementa este detalhamento. Será o mesmo valor descrito no campo Cargo Efetivo - Sigla  Se não houver, repetirá a sigla do cargo efetivo constante do Plano de Cargos. |
| Classificação Cargo | <classificacaocargo> | Cadastro de Cargo  PCARGO.CODCLASSCARGO | Campo "Classificação do Cargo" existente no cadastro de Cargos que deve ser preenchido conforme a Tabela 16 - Classificação de Cargo/Função. |

**Dados da Função:**  
Informações sobre Função ocupada pelo Funcionário (de carreira ou não), conforme Plano de Funções (PF) ou Quadro Temporário, bem como de dados da atividade de Dirigente e de Conselheiro.   
Deve ser observado o histórico de função do funcionário referente ao último dia da competência informada, e o tipo de função informado no cadastro de Função. A inexistência desses campos poderá fazer com que dados ou o próprio bloco do registro não sejam levados para o PPE.

|  |  |  |  |
| --- | --- | --- | --- |
| **Campo** | **Tag** | **Origem** | **Regra** |
| Função - Tipo | <tipofuncao> | Cadastro de Função  PFUNCAO.CODTIPOFUNCAO | Referente ao código do tipo de função, de acordo com o estabelecido na Tabela 17- Tipo de Função.  Caso seja "0" (zero), os outros campos da Função serão omitidos no XML gerado. |
| Função - Nome | <nomefuncao> | Cadastro de Função  PFUNCAO.NOME | Nome completo da função/cargo exercida pelo empregado/dirigente/conselheiro, sem abreviar. É obrigatório se Função - Tipo for diferente de "0 - Não Ocupante" de acordo com o estabelecido na Tabela 17- Tipo de Função. |
| Função - Sigla | <siglafuncao> | Cadastro de Função  PFUNCAO.SIGLA | Campo "Sigla" do cadastro de Função. |
| Função - Código | <codigofuncao> | Cadastro de Função  PFUNCAO.CODIGO | Campo "Código" do cadastro de Função.  É obrigatório se Função – Tipo for diferente de "0 - Não Ocupante", "1 - Dirigente", "2 - Conselheiro" e "3 - Exercício Temporário" de acordo com o estabelecido na Tabela 17- Tipo de Função. |
| Faixa Salarial | <faixasalarialfuncao> | Cadastro de Funcionário  PFUNC.CODNIVEL | No caso de inexistência de faixa salarial (grupo, classe ou nível), informará nesse campo a palavra "Única".  É obrigatório se Função – Tipo for diferente de "0 - Não Ocupante", "1 - Dirigente", "2 - Conselheiro" e "3 - Exercício Temporário" de acordo com o estabelecido na Tabela 17- Tipo de Função.  O Totvs Folha de Pagamento não contempla o tratamento para o conceito de Remuneração Global, por isso este campo terá o seu valor prefixado com a palavra "Única" para todos os funcionários. |
| Referência Salarial | <graufuncao> | Cadastro de Funcionário  PFUNC.GRUPOSALARIAL | É obrigatório se Função – Tipo for diferente de "0 - Não Ocupante", "1 - Dirigente", "2 - Conselheiro" e "3 - Exercício Temporário" de acordo com o estabelecido na Tabela 17- Tipo de Função.  O Totvs Folha de Pagamento não contempla o tratamento para o conceito de Remuneração Global, por isso este campo terá o seu valor prefixado com a palavra "Única" para todos os funcionários. |
| Valor de Referencia | <valorreferencia> | Tabela Salarial  VTABELASALARIAL.SALARIO | Valor do campo Salário referente a tabela salarial da função e nível e faixa correspondente ao funcionário.  É obrigatório se se Função - Tipo <> "0", "1", "2", "3" e não informou Valor da Função e Valor do Complemento.   O Totvs Folha de Pagamento não contempla o tratamento para o conceito de Remuneração Global, por isso este campo não será levado para o PPE. |
| Valor da Função | <valorfunção> | Calculado  Cadastro de Eventos Compõe Valor Função  Ficha financeira  PEVTVALORFUNCAO  PFFINANC | É a soma dos valores dos eventos na ficha financeira referente a competência informada que constam na lista de eventos no cadastro "Eventos que compõem ao Valor da Função"  É obrigatório se se Função - Tipo <> "0", "1", "2", "3" e não informou Valor de Referência e Valor do Complemento. |
| Valor do Complemento | <valorcomplemento> | Calculado  Cadastro de Eventos Compõe Valor Função  Ficha financeira  PEVTVALORCOMPL  PFFINANC | É a soma dos valores dos eventos na ficha financeira referente a competência informada que constam na lista de eventos no cadastro "Eventos que compõem ao Valor do Complemento"  É obrigatório se se Função - Tipo <> "0", "1", "2", "3" e não informou Valor de Referência e Valor da função. |
| Classificação da Função | <classificacaofuncao> | Cadastro de Função  PFUNCAO.CODCLASSFUNCAO | Código de Classificação da função do funcionário.  Campo a ser escolhido do Cadastro Classificação da Função conforme Tabela 16 - Classificação de Cargo/Função |

**Dados de Afastamento e Licenças / Dados de Cada Ocorrência:**  
Refere-se a afastamentos do Funcionário ocorrido na competência informada.  
Serão analisadas as informações do histórico de situação e de afastamentos do funcionário.

|  |  |  |  |
| --- | --- | --- | --- |
| **Campo** | **Tag** | **Origem** | **Regra** |
| Motivo do Afastamento ou Licença | <motivoafastamento> | Cadastro de Motivo Afastamento TOTVS X PPE  PMOTIVAFASTCLIENTE.CODPPE | Obtido do cadastro "Motivo Afastamento TOTVS x PPE". O usuário deverá fazer o De/Para entre a Tabela Dinâmica Motivo de Mudança de Situação e o motivo de Afastamento PPE de acordo com a Tabela 18 - Motivo Afastamento |
| Data do Afastamento ou Licença | <dataafastamento> | Histórico de Afastamento  PFHSTAFT.DTINICIO | Data de Início do Afastamento  Formato: "AAAA-MM-DD" |
| Data do Retorno | <dataretornoafastamento> | Histórico de Afastamento  PFHSTAFT.DTFINAL | Data de retorno do afastamento dentro da competência informada.  Caso o funcionário continue afastada por toda competência, esse campo não será informado no PPE. |
| Dias Afastados no mês | <quantidadediasafastamento> | Calculado.  PFHSTAFT.DTFINAL PFHSTAFT.DTINICIO  Início da competência  Fim da competência | Número de dias (quantidade de dias) em que o empregado ficou afastado ou de licença,  no mês a que se refere a informação (máximo de 31 dias)  Não sendo informada a data final do afastamento, será considerado o último dia da competência a data final para o cálculo desse campo. |

**Dados de Desligamento:**  
Somente para funcionários que foram demitidos (situação "D") em que a data do histórico de situação com valor "D" esteja na competência informada.

|  |  |  |  |
| --- | --- | --- | --- |
| **Campo** | **Tag** | **Origem** | **Regra** |
| Data do Desligamento | <datadesligamento> | Histórico de Situação  PFHSTSIT.DATAMUDANCA | Última situação "D" na competência informado.  Campo Data de Mudança do Histórico de situação 'D" |
| Motivo do Desligamento | <naturezadesligamento> | Cadastro de Motivo de Desligamento TOTVS x PPE  PMOTIVDEMISSAOCLI.CODCLIENTE (Novo) | Obtido do cadastro "Motivo de Desligamento TOTVS x PPE" O usuário deverá fazer o De/Para entre a Tabela Dinâmica Motivo de Demissão e o motivo de desligamento PPE de acrodo com a Tabela 19 - Motivo Desligamento. |

**Dados de Cada Dispêndio:**  
Os registros abaixo são obtidos do cadastro de Dispêndio, caso os eventos informados nos dispêndios individuais estejam lançados na ficha financeira do funcionário na competência informada.

|  |  |  |  |
| --- | --- | --- | --- |
| **Campo** | **Tag** | **Origem** | **Regra** |
| Rubrica - Código | <codigorubrica> | Cadastro de Dispêdio  PDISPENDIO.CODSPE | Código CODSPE do dispêndio individual em que o flag "Consolidado" esteja desmarcado.  O sistema considerará os eventos informados no dispêndio individual que foram lançados no envelope do funcionário para a competência informada. |
| Rubrica - Valor | <valorrubrica> | Calculado  PDISPENDIO.CODSPE  PDISPENDIOEVENTO.CODEVENTO  PFFINANC.VALOR | Somatório dos valores do dispêndio individual para cada código SPE, referente a competência informada, conforme a configuração feita no Cadastro de Dispêndio. |

**Dados de Cada Formação Profissional**  
Deverá preencher os campos abaixo, conforme o grau de instrução (cursos completos constantes na Tabela 8 - Grau de Instrução) e de acordo com a formação acadêmica de cada empregado, dirigente ou conselheiro definida na Tabela 21 – Cursos.  
Cadastro de formação acadêmica do TOTVS Gestão de Pessoas está vinculado a pessoa do Funcionário.

|  |  |  |  |
| --- | --- | --- | --- |
| **Campo** | **Tag** | **Origem** | **Regra** |
| Formação - Código | <codigoformacao> | Cadastro de Cursos Acadêmicos (Totvs Gestão de Pessoas)  VCURSOACAD. CODCURSOPPE | Campo "Código do Curso na Tabela 21 do PPE" do Curso Acadêmico vinculado à Formação Acadêmica da pessoa atrelada ao funcionário.  Obs.: Caso o funcionário possua grau de instrução no Totvs Folha de Pagamento igual a 9, A, B, C, D, E, F, G ou H, e não tenha sido informado sua formação acadêmica, ou não tenha preenchido no cadastro da formação o código da Tabela 21 - Cursos, ou o andamento do curso esteja diferente de "Concluído", o sistema automaticamente irá informar uns dos seguintes códigos:   * "3199999999 - Não Disponível", caso o grau de instrução do funcionário seja 9, A, C ou E; * "4199999999 - Não Disponível", caso o grau de instrução seja B; * "5199999999 - Não Disponível", caso o grau de instrução seja D; * "6199999999 - Não Disponível", caso o grau de instrução seja F, G ou H. |
| Formação - Ano | <anoformacao> | Cadastro de Funcionário/Pessoa I Formação Acadêmica  (Totvs Gestão de Pessoas)  VFORMACAOCAD.ANOTERMINOV | Ano de término referente ao curso vinculado a formação da pessoa.  Será informado apenas caso a data de término da formação correspondente seja preenchida. Não é informado para os registros "3199999999 - Não Disponível", "4199999999 - Não Disponível", "5199999999 - Não Disponível", "6199999999 - Não Disponível". |

**Dados de Cada Desconto em Folha**  
Os campos abaixo devem ser informados com base nos descontos efetuados pela empresa na folha de pagamento do empregado, dirigente ou conselheiro, relativos às consignações de responsabilidade exclusiva do empregado, conforme a natureza do desconto/benefício constante da Tabela 22 – Tipo de Desconto em Folha.  
O tipo de desconto deve ser previamente informado no cadastro do evento, e o valor correspondente será buscado na ficha financeira do funcionário na competência informada.

|  |  |  |  |
| --- | --- | --- | --- |
| **Campo** | **Tag** | **Origem** | **Regra** |
| Desconto - Código | <codigodesconto> | Cadastro de Eventos  PEVENTO.CODTPDESCONTO | Código obtido no cadastro de Eventos I PPE, que teve o evento a ele associado de acordo com a Tabela 22 – Tipo de Desconto em Folha e possui o evento na ficha financeira do funcionário na competência informada. |
| Desconto - Valor | <valordesconto> | Ficha Financeira  PFINANC.VALOR | Somatório do evento lançado na ficha financeira do funcionário conforme a competência informada |
| Banco - Código Compensação | <numerobanco> | Cadastro do Funcionário I Empréstimo  PFEMPRT.CODBANCO | Esse campo será Informado somente se o tipo do desconto associado ao evento lançado na ficha financeira for "99 - Empréstimo Consignado em Instituições Financeiras", e existir a devida informação do código de banco de compensação no cadastro de empréstimo do funcionário. |
| Contrato - Número Identificador | <identificadorcontrato> | Cadastro do Funcionário I Empréstimo  PFEMPRT.CONTRATO | Esse campo será Informado somente se o tipo do desconto associado ao evento lançado na ficha financeira for "99 - Empréstimo Consignado em Instituições Financeiras", e existir a devida informação do código contrato no cadastro de empréstimo do funcionário. |
| Contrato - Data Inicial | <datainiciocontrato> | Cadastro do Funcionário I Empréstimo  PFEMPRT.DTEMPRESTIMO | Esse campo será Informado somente se o tipo do desconto associado ao evento lançado na ficha financeira for "99 - Empréstimo Consignado em Instituições Financeiras", e existir a devida informação da data do empréstimo no cadastro de empréstimo do funcionário. |
| Contrato - Data Final | <datafimcontrato> | Cadastro do Funcionário I Empréstimo  PFEMPRT.FINALDESCONTO | Esse campo será Informado somente se o tipo do desconto associado ao evento lançado na ficha financeira for "99 - Empréstimo Consignado em Instituições Financeiras", e existir a devida informação da data final prevista no cadastro de empréstimo do funcionário. |
| Contrato - Valor | <valorcontrato> | Cadastro do Funcionário I Empréstimo  PFEMPRT.VALORORIGINAL | Esse campo será Informado somente se o tipo do desconto associado ao evento lançado na ficha financeira for "99 - Empréstimo Consignado em Instituições Financeiras", e existir a devida informação do valor original no cadastro de empréstimo do funcionário. |
| Quantidade de Parcelas | <quantidadeparcelas> | Cadastro do Funcionário I Empréstimo  PFEMPRT.NROPARCELAS | Esse campo será Informado somente se o tipo do desconto associado ao evento lançado na ficha financeira for "99 - Empréstimo Consignado em Instituições Financeiras", e existir a devida informação do Nro de Parcelas no cadastro de empréstimo do funcionário. |
| Data - Primeiro Mês de Desconto | <mesprimeirodesconto> | Cadastro do Funcionário I Empréstimo  Mês do campo PFEMPRT.INICIODESCONTO | Mês do campo "Início do Desconto" no cadastro de empréstimo do funcionário. Esse campo será Informado somente se o tipo do desconto associado ao evento lançado na ficha financeira for "99 - Empréstimo Consignado em Instituições Financeiras", e existir a devida informação da data de início do desconto no cadastro de empréstimo do funcionário. |
| Data - Exclusão do Contrato | <dataexclusaocontrato> | Cadastro do Funcionário I Empréstimo  PFEMPRT.DTEXCLUSAO | Corresponde a data de liquidação do contrato mesmo que antecipadamente. Esse campo será Informado somente se o tipo do desconto associado ao evento lançado na ficha financeira for "99 - Empréstimo Consignado em Instituições Financeiras", e existir a devida informação da data de exclusão no cadastro de empréstimo do funcionário. |
| Motivo da Exclusão do Contrato | <motivoexclusao> | Cadastro do Funcionário I Empréstimo  PFEMPRT.CODMOTIVEXCLUSAO | Estando a Data-Exclusão preenchida deve ser informado este campo o código do motivo da exclusão do contrato, conforme códigos constantes da Tabela 24 –Motivo da Exclusão da Operação.  Esse campo será Informado somente se o tipo do desconto associado ao evento lançado na ficha financeira for "99 - Empréstimo Consignado em Instituições Financeiras", e existir a devida informação da data de exclusão do contrato e o motivo no cadastro de empréstimo do funcionário. |

**Tabelas de Equivalência**  
De acordo com o Manual do PPE e suas tabelas auxiliares, foi necessário estabelecer algumas tabelas de equivalência entre informações existentes no Totvs Folha de Pagamento e o que será considerado no arquivo do PEE:  
**Equivalência Cor / Raça TOTVS Folha de pagamento x PPE Tabela 5 - Raça-Cor**

|  |  |  |
| --- | --- | --- |
| **TOTVS**  **Tabela Dinâmica Cor / Raça** | **PPE Tabela 5** | **Descrição** |
| 0 - Indígena | 1 | Indígena |
| 2 - Branca | 2 | Branca |
| 4 - Preta | 3 | Negra |
| 8 - Parda | 4 | Parda |
| 6 - Amarela | 5 | Amarela |
| 9 - Não Informado Ou 10 - Não Declarado ou quando estiver em branco ou nulo no cadastro. | 9 | Não Informado |

**Equivalência Tipo de Deficiência TOTVS Folha de pagamento x PPE Tabela 6 - Tipo Deficiência**

|  |  |  |
| --- | --- | --- |
| **TOTVS**  **Campo da PPESSOA** | **PPE Tabela 6** | **Descrição** |
| Se DEFICIENTEFISICO OU DEFICIENTEFALA  E não for as demais | 1 | Física |
| Se DEFICIENTEAUDITIVO e não for as demais | 2 | Auditiva |
| Se DEFICIENTEVISUAL e não for as demais | 3 | Visual |
| Se DEFICIENTEMENTAL e não for as demais | 4 | Intelectual ou Mental |
| Se mais de um caso acima | 5 | Múltipla |
| Se BRPDH independente dos casos acima | 6 | Reabilitado |
| Se não atende nenhum dos casos acima | 9 | Não Informado |

**Equivalência Nacionalidade TOTVS Folha de pagamento x PPE Tabela 7 - Nacionalidade**

|  |  |  |
| --- | --- | --- |
| **TOTVS**  **Tabela dinâmica Nacionalidade** | **PPE Tabela 7** | **Descrição** |
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

**Equivalência Grau de Instrução TOTVS Folha de pagamento x PPE Tabela 8 Graus de Instrução**

|  |  |  |
| --- | --- | --- |
| **TOTVS**  **Tabela Dinâmica "Grau de Instrução"** | **PPE Tabela 8** | **Descrição** |
| Se '2' ou '3' ou '4' | 10 | Fundamental Incompleto |
| '5' | 11 | Fundamental Completo |
| *O Labore não trata Formação técnica no grau de instrução* | 12 | Fundamental Completo (Técnico) |
| '6' | 20 | Médio Incompleto |
| '7' | 21 | Médio Completo |
| *O Labore não trata Formação técnica no grau de instrução* | 22 | Técnico Incompleto |
| *O Labore não trata Formação técnica no grau de instrução* | 23 | Técnico Completo |
| '8' | 30 | Superior Incompleto |
| '9' | 31 | Superior Completo |
| 'A' | 40 | Especialização ou MBA Incompleto |
| 'B' | 41 | Especialização ou MBA Completo |
| 'C' | 50 | Mestrado Incompleto |
| 'D' | 51 | Mestrado Completo |
| 'E' | 60 | Doutorado Incompleto |
| Se 'F' ou 'G' ou 'H' | 61 | Doutorado Completo |

**Calculo e Equivalência para PPE Tabela 12 - Jornada de Trabalho**

|  |  |  |
| --- | --- | --- |
| **TOTVS**  **Jornada do Funcionário** | **PPE Tabela 12** | **Descrição** |
| Igual 100 | 20 | 20 horas semanais |
| Igual 120 | 24 | 24 horas semanais |
| Igual 150 | 30 | 30 horas semanais |
| Igual 180 | 36 | 36 horas semanais |
| Igual 200 | 40 | 40 horas semanais |
| Igual 220 | 44 | 44 horas semanais |
| Diferente dos valores acima | 99 | Outras |
