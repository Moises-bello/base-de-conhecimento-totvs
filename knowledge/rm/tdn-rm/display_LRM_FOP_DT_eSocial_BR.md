---
content_hash: ca1eac9a3a994b8f83147845ea650152f000d93ba2e533ebade8a85eadc2f838
fetched_at: '2026-06-29T00:06:25.526626+00:00'
page_id: '224398657'
product: rm
source: tdn-rm
title: FOP_DT_eSocial_BR
type: documentation
url: https://tdn.totvs.com/display/LRM/FOP_DT_eSocial_BR
version: 5
---

### eSOCIAL

### Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *eSocial* |  | |
| **Versão/Release:** | 11.52 **|** 11.53 **|** 11.82 **|** 11.83 |

## Descrição

Este documento serve para que os usuários possam configurar dados que completam o eSocial

## Procedimento para Utilização

## CADASTROS EXISTENTES

### Funcionário e/ou Pessoas

**Dados da edição do cadastro**

Link Documentação Inclusão dos campos “Data de Emissão” e “Órgão Emissor” para carteira de motorista, além dos campos referentes ao RIC – Registro de Identidade Civil.

**Link Documentos Estrangeiros**   
Inclusão dos campos “Data de Naturalização”, habilitado apenas quando marcado o parâmetro “Naturalizado” e os campos “Órgão Emissor” e “Data da Emissão” referentes ao documento de Registro Nacional de Estrangeiro.

**Atenção!** A visão dos campos referentes à documentação de estrangeiros é habilitada somente quando no cadastro do Funcionário, link “Identificação”, a “Nacionalidade” for diferente de “10 – Brasileira”.

**Link Endereço Principal**

Incluído os campos “Tipo de Rua”, “Tipo de Bairro” e os referentes à “Moradia”. O campo “Tipo de Rua” é de preenchimento obrigatório, corresponde aos dados cadastrados no TOTVS Gestão Fiscal / agrupador Globais / Mais / Endereço / Tipo de Rua. De acordo com o leiaute do eSocial, a **Tabela 20 – Tabela de Tipos de Logradouros**, define os tipos de logradouros a serem utilizados. Para saber como parametrizar esses tipos de logradouros, acesse o tópico Novos Parâmetros, subtópico **Configurações Gerais, Conceito de Classificação para Tipo de Rua (De/Para).**

Sugerimos o preenchimento do campo “Tipo de Bairro” para atender à normalização do cadastro de endereço.

Os campos para informações de Moradia foram criados conforme consta no manual versão 1.0 do eSocial

**Link Informações Contratuais**

**Registro**

Para casos de reintegração, incluído os campos:

• Aba “Dados do Registro”, campo “Indicativo de Admissão”, deve ser preenchido com uma das seguintes opções: Normal, Decorrente de Ação Fiscal ou Decorrente de Decisão Judicial.

• Aba “Reintegração”, campo “Tipo de Reintegração”, informar: Reintegração por “Determinação Judicial”, “Reintegração por Anistia Legal” ou “Outros”. Informar, também, “Data da Reintegração” e “Data de Retorno Efetivo”.

**Dados do Estágio**

Para funcionários cujo “Tipo” for igual a T – Estagiário, link “Informações Contratuais / Salário|Jornada”, preencher o campo “Nível do Estágio” conforme opções determinadas pelo eSocial.

Os campos “Instituição de Ensino do Estágio” e “Agente de Integração do Estágio” podem ser previamente cadastrados por meio do cadastro de Entidades disponível no TOTVS Gestão de Pessoas ou por meio do ícone de inclusão na tela de localização de “Entidades”. Demais campos são do tipo texto.

**Link Informações para o cálculo / Situação**

Incluído o campo “Tipo de regime previdenciário”, preencher com um dos tipos pré-definidos no manual do eSocial.

**Link Sindicato / Dados do Sindicato**

**Dados Dirigente Sindical**

Incluído o campo “Categoria Empresa Origem” que corresponde às “Categorias do trabalhador”. Esse e os demais campos devem ser preenchidos com dados da empresa origem que detém o vinculo com empregado.

**Anexos do Cadastro de Funcionários**

**Registro Profissional**

Anexo incluído no cadastro de Funcionários, antes, o sistema possuía apenas o campo para informar o número do registro.

Exemplo: O funcionário “Marcelo Mattar” tinha em seu registro o Número de Registro Profissional 558744. No anexo “Registro Profissional” foi gerado o cadastro com esse número, conforme consta na imagem abaixo:

Para o eSocial, os dados devem ser completados com as informações faltantes, conforme exemplo imagem abaixo:

O campo “Código do Órgão da Classe” permite a inclusão de itens pelo usuário por meio de sua edição, ou, por meio de menu específico: RH / TOTVS Gestão de Pessoas / Acompanhamento / Tabelas Auxiliares / Órgão de Classe.   
Os Órgão de Classe deverão ser cadastrados com o campo “Código” preenchido com a SIGLA do Órgão, como por exemplo: CREA, CRP e etc.

**Estabilidade**

**Cadastro criado para atender os eventos S-2340 - Estabilidade – Início e S-2345 - Estabilidade – Término, a partir do layout 2.0 os eventos foram retirados.**

Incluído o anexo “Estabilidade”, pode conter dados inseridos manualmente ou automaticamente

• **Automática** – incluída a partir da alteração da situação do funcionário para um dos tipos de afastamento: T – Acidente de Trabalho, S-Mandato Sindical, M-Serviço Militar, além dos cadastros originados do TOTVS Gestão de Pessoas: Candidatos da CIPA e membro Eleito CIPA (titular ou suplente);

• **Manual** – não originadas pelos afastamentos mencionados acima, registro incluído pelo usuário do sistema, pode ter origem dos tipos:

Gravidez;   
Convenção Coletiva de Trabalho;   
Membro do Conselho Nacional da Previdência Social (CNPS);   
Membro de Comissão de Conciliação Prévia;   
Empregados eleitos diretores de sociedades cooperativas;   
Membros do Conselho Curador do FGTS;  
 Outros.

As estabilidades geradas, automaticamente ou manualmente, terão os códigos identificados conforme consta no eSocial.

**Histórico de Afastamento**

Incluída a aba eSocial no sub anexo Histórico de Afastamento disponível no Cadastro de Funcionários, anexo Históricos, para o preenchimento de dados específicos. Nas informações de atestado, o campo “Emitente” faz referência ao cadastro de Profissional da Saúde, localizado no TOTVS Segurança e Medicina do Trabalho / Cadastros / Profissional da Saúde.

O campo CID faz referência aos itens cadastrados no TOTVS Segurança de Medicina do Trabalho / PCMSO / CID.   
Os campos “Acidente de Trânsito” serão habilitados quando o afastamento for do tipo “O – Doença Ocupacional”, “P – Afastamento Previdência Social” ou “T – Acidente de Trabalho”.   
O campo “Ônus da Cessão” será habilitado quando o TOTVS Folha de Pagamento estiver configurado para utilizar tomador de serviço.   
Os campos de “Mandato Sindical” serão habilitados quando o afastamento for do tipo “S – Mandato Sindical”.

Ao alterar o campo “Motivo do Afastamento” o sistema registra, automaticamente, um histórico dessa alteração, pois deve constar em arquivo específico ao enviar os dados para o eSocial. Esse histórico é acessado por meio do anexo “Histórico do Afastamento”, subanexo “Histórico do Motivo de Afastamento”

**Consultas Realizadas**

**O cadastro foi alterado a**partir da versão 12**, nas versões atuais essas informações são cadastradas em Consultas Médicas/ Abrir Prontuário Médico.**

Anexo Segurança e Medicina / Consultas Realizadas.

Esse cadastro pertence ao TOTVS Segurança e Medicina do Trabalho, mas pode ser acessado por meio do TOTVS Folha de Pagamento, desde que o usuário tenha permissão de acesso a esse cadastro no TOTVS Segurança e Medicina do Trabalho.  
Incluído o campo “Tipo da Consulta E-Social”, deve ser preenchido com os tipos pré-definidos no manual do eSocial. O campo “Código do Médico” passa a listar os registros do cadastro “Profissionais da saúde” vinculados a um CRM, com isso, o “Número de CRM” é carregado automaticamente.   
Incluído o parâmetro “Apto com Restrição” para o grupo de informações “Situação Final”, conforme indicada no manual do eSocial.

**Atenção!** Os processos que realizam o lançamento de exames, do TOTVS Segurança e Medicina do Trabalho, foram adaptados para conter os novos campos aqui mencionados. Ao selecionar uma das opções da “Situação Final”, o sistema acata a opção marcada e desconsidera o cálculo realizado para definir essa situação, independente dos resultados dos exames.

### Eventos

**Natureza da Rubrica (eSocial)**

Localizado na aba “Identificação”. Deve ser preenchido conforme itens pré-definidos na **Tabela 3 – Natureza das rubricas da folha de pagamento, do Manual 1.0 do eSocial.**

**Incidência Suspensa, Tipo de Processo e Número de Processo:**

Localizado na aba “Inc. Proventos” (habilitada para eventos do tipo provento/base de cálculo). Esses campos são utilizados para informar se o evento possui ou não incidência suspensa em INSS, IRRF, FGTS, Contribuição Sindical e Salário Maternidade. Havendo incidência suspensa, o número de processo deve ser informado, bem como o campo “Extensão da Decisão/Sentença”.

### Seções

Tipo da Lotação:  
Localizado na aba Identificação. Deve ser preenchido conforme “Tabela 10 – Tipos de Lotação” do Manual 1.0 do eSocial.

CNO da obra própria:  
 habilitado quando o “Tipo de Lotação” for igual a:   
02 - Obra Própria - Pessoa Jurídica, ou:   
03 - Obra de Construção Civil (Empreitada Parcial ou Subempreitada).   
22 - Obra Própria - Pessoa Física;

CAEPF: habilitado quando o “Tipo de Lotação” for igual a:   
21 – Escritório, Consultório, etc. - Pessoa Física;   
23 – Estabelecimento Rural – Pessoa Física;

### Ocorrência de Acidente de Trabalho

Cadastro disponível no TOTVS Segurança e Medicina do Trabalho, menu CAT / Ocorrências Acidente Trabalho. Ele foi adaptado para contemplar as informações: Código da Situação Geradora, alteração do campo Cód. Agente(s) Causador(es), alteração do campo Parte(s) do corpo atingida(s), inclusão Logradouro e Número do local do acidente, inclusão Município do local do acidente – conforme tabela IBGE, inclusão CNPJ do local do acidente, inclusão Cód. und. Atendimento médico (CNES) e alteração dos dados do médico.

Na aba “Local do Acidente de Trabalho” preencher os campos “Logradouro do local do acidente”, “Número do local do acidente”, “UF do local do acidente”, “Código do município do acidente” e “CNPJ do local do acidente”.

Na aba “Atestado médico” os novos campos são “Cód. Médico”, “CRM do Médico”, “UF do Médico”, “Nome do Médico”, todos referentes ao cadastro de Profissional da Saúde. Ao selecionar um registro de um profissional da saúde, todos os demais dados serão preenchidos automaticamente.

A ocorrência de acidente de trabalho também pode ser acessada por meio do cadastro de Funcionários anexo Segurança e Medicina / Acidente de Trabalho.

### Processos Jurídicos

Cadastro disponível no TOTVS Gestão de Pessoas / Gestão Organizacional / Processos Jurídicos / Processos Jurídicos. Os processos cadastrados devem se relacionar com os processos que, eventualmente, possam ser vinculados a cadastros que possuam informação de processo, por exemplo, cadastro de Eventos.

## **Novos Cadastros**

Incluído na nova interface do TOTVS Folha de Pagamento (MDI .Net), o menu “eSocial (beta)”. Neste, disponibilizamos os cadastros Informações do Empregador e Software House, e também o processo “Gerar Carga Inicial”.

**Atenção!** Chamamos de “beta” devido as constantes mudanças propostas pelo Governo para o leiaute do arquivo a ser enviado para o eSocial.

### Empregador

**A partir da versão 12.1.16, ocorreram alterações na tela para atender o layout 2.2 do eSocial.**

Contém dados do empregador, o sistema aceita um cadastro de Empregador por Coligada.

### Software House

Contém os dados da empresa fornecedora do software de folha de pagamento. Após inclusão deve ser relacionado ao cadastro de Empregador.

### Profissional da Saúde

Disponível no TOTVS Segurança e Medicina do Trabalho / Cadastros / Profissional de Saúde.

**Atenção!** O sistema permite cadastrar um Profissional da Saúde mesmo que não tenha um registro de Pessoa cadastrado na base. Caso o Profissional da Saúde conste no registro de Pessoas, basta localizar o registro existente, sendo que, somente serão listadas as pessoas vinculadas a um órgão da área da saúde.

### Cadastro Órgão de Classe

Cadastro relacionado ao Registro Profissional. Pode ser realizado na própria visão da inclusão de um Registro Profissional, disponível no cadastro de Funcionários, ou por meio do menu Acompanhamento / Tabelas Auxiliares / Órgão de Classe, disponível no TOTVS Gestão de Pessoas.

No sistema, o usuário verificará que os Órgãos “CRM – Conselho Regional de Medicina” e “CRO – Conselho Regional de Odontologia” já estarão cadastrados automaticamente.   
O campo “Órgão da Área de Saúde” quando marcado indica que apenas profissionais cadastrados e vinculados a esse órgão é que serão listados no campo “Emitente” do cadastro de Histórico de Afastamento.   
Nos cadastros de CAT (Ocorrência de acidente de trabalho), ASO (Atestado de Saúde Ocupacional) – Consultas Realizadas e no processo de Lançamento de Exames, somente profissionais com CRM serão listados nos respectivos campos que fazem referência a “médicos”.

## **Novos Parâmetros**

### eSocial (Folha de Pagamento)

Incluído parâmetros para a emissão do eSocial por meio da folha de pagamento. Esses estão disponíveis em RH / TOTVS Folha de Pagamento / Configurações / Parametrizador, processo “eSocial”.

Por meio desses parâmetros o usuário associa itens do eSocial, pré-definidos e padronizados em manual, aos itens da Folha de Pagamento que são usados desde a sua implantação. Os parâmetros disponíveis na Folha são:

**Configurações Gerais:**

As informações configuradas nos campos acima devem ser, previamente, cadastradas no TOTVS Gestão Fiscal, responsável pelo cadastramento de informações gerais de endereços.

**Conceito de Classificação para Tipo de Rua (De/Para):** os dados desse campo devem ser configurados e cadastrados no TOTVS Gestão Fiscal / Cadastros / agrupador Mais... / Endereço / Classificação de Tipo de Rua.   
O conceito de classificação tem a função de definir a qual órgão o Tipo de Rua é classificado. Por exemplo: eSocial, Receita Federal, Ministério do Trabalho, IBGE, etc. Para eSocial consta em seu manual a tabela com as informações utilizadas como tipos de ruas, localizada pela descrição Tabela 20 – Tabela de Tipos de Logradouros. Para tal, foi incluído no cadastro de Classificação de Tipo de Rua, o item 1 – Tipo de Logradouros eSocial , conforme imagem abaixo.

Ainda no TOTVS Gestão Fiscal, o usuário deve acessar o cadastro Tipo de Rua, para relacionar o item 1 – Tipo de Logradouros eSocial, aos cadastros já existentes nesse menu ou que tenham que ser cadastrados.

*Exemplo:*   
Na tabela do eSocial está definido:  
**Código 04 – Avenida**

No TOTVS Gestão Fiscal, no cadastro de Tipo de Rua, o item equivalente é o: **Código 06 – Avenida.**

Dessa forma, para proceder com a configuração, o usuário deve acessar Anexos / Codificação de Tipo de Rua para relacionar o item **1 – Tipo de Logradouros eSocial.**

Além do item do tipo de Logradouro, informar, também, o código do Logradouro da tabela do eSocial, conforme imagem abaixo:

Inclusão do item de classificação: 1 – Tipo de Logradouros eSocial Código: 04 (da tabela Logradouros do eSocial – item 04 Avenida)

A classificação de Tipo de Rua “1 – Tipo de Logradouros eSocial” deve ser relacionada ao parametrizador do TOTVS Folha de Pagamento.

**Conceito de Classificação para Códigos de Município:** o item informado nesse campo segue a classificação de Município do IBGE, conforme definido no manual do eSocial.   
Os menus para cadastro desses itens de classificação são próprios, estão localizados no TOTVS Gestão Fiscal / Cadastros / agrupador Mais... / Endereço / Classificação de Município.   
A lógica dessa configuração é a mesma do passo a passo anterior, porém, nos menus específicos no TOTVS Gestão Fiscal: “Classificação de Município” e “Municípios”.

**Conceito de Classificação para Códigos de Países (De/Para):** o item informado nesse campo segue a classificação de Países da RFB, conforme definido no manual do eSocial.   
Os menus para cadastro dos itens de Classificação de Código de Países são próprios, estão localizados no TOTVS Gestão Fiscal / Cadastros / agrupador Mais... / Endereço / Classificação de País.   
A lógica dessa configuração é a mesma do passo a passo anterior, porém, nos menus específicos no TOTVS Gestão Fiscal: “Classificação de Países” e “Países”.

**Associação da Nação com o País**

As nacionalidades utilizadas nos cadastros de funcionários devem ser associadas ao código de País equivalente. Essa associação funciona a partir da seleção de uma nacionalidade e de um país, ambos em campos correspondentes.  
 A cada seleção, clicar no botão “Associar”. Repita as seleções a cada associação realizada. Realize esse procedimento apenas para as nacionalidades utilizadas nos cadastros de funcionários.

**Parâmetros de Afastamento**

Incluído o parâmetro de afastamento para relacionar os tipos de afastamentos que são definidos no eSocial (Licença Paternidade, Mandato Eleitoral, Participação de Curso ou Programas de Qualificação, Cessão de Trabalhador, Cárcere) com os tipos e motivos de afastamentos que são usados no TOTVS Folha de Pagamento que possuam equivalência.

**Tipos de Anotação eSocial**

O manual define os tipos de “Fatos Relevantes”. Para atender essa demanda, relacione o tipo de anotação pessoal do TOTVS Folha de Pagamento ao “Tipo de Anotação ESocial” que possua equivalência.

### ASO (SMT)

Incluído no “Parametrizador” do TOTVS Segurança e Medicina do Trabalho, parâmetros que definem a origem dos dados utilizados para emitir o arquivo S-2420 – Atividades Desempenhadas. Esses parâmetros estão localizados em Configurações / Parametrizador, processo eSocial e estão relacionados aos dados de Atividades do PPP (Perfil Profissiográfico Previdenciário). Caso não haja integração com o TOTVS Segurança e Medicina do Trabalho, os dados de atividades desempenhadas são informados por meio do cadastro de Funções do TOTVS Folha de Pagamento.

Os itens selecionados determinam a origem das informações para a emissão dos dados de Atividades Desempenhadas emitidos para o eSocial.

## Novos Processos

### Gerar Carga Inicial

Os itens selecionados determinam a origem das informações para a emissão dos dados de Atividades Desempenhadas emitidos para o eSocial.

Nesse processo, tem-se as opções para emissão dos arquivos:

S-1000 – Informações do Empregador: arquivo que contém informações originadas do cadastro “Informações do Empregador”;  
 S-1010 – Tabela de Rubricas: arquivo que contém informações originadas do cadastro de Rubricas;   
S-1020 – Tabela de Lotações / Departamentos: arquivo que contém informações originadas do cadastro de Seções;   
S-1030 – Tabela de Cargos: arquivo que contém informações originadas do cadastro de Funções;   
S-1050 – Tabela de Horários / Turnos de Trabalho: arquivo que contém informações originadas do cadastro de Horários;   
S-1060 – Tabela de Estabelecimentos/Obras: arquivo que contém informações originadas do cadastro de Seções que utilizam CEI Construção Civil;  
 S-1070 – Tabela de Processos Administrativos / Judiciais: arquivo que contém informações originadas do cadastro de Processos Jurídicos do TOTVS Gestão de Pessoas;   
S-2100 – Evento de Cadastro Inicial do Vínculo: arquivo que contém informações do cadastro de Funcionários e que, também, envolve dados de Pessoa.

Observação: o campo “Quebra de Seção” e botão “Seleção de Funcionários”, somente serão habilitados quando for selecionada a opção de geração do arquivo S-2100 – Evento de Cadastro Inicial do Vínculo.   
Para emissão dos arquivos, definir o diretório para a gravação dos arquivos XML. O processo é finalizado após avançar a tela e concluir o processo.

# Informações Adicionais

A versão a liberar conta com implementações para o eSocial com emissão dos arquivos de informações referentes a “Movimentações” e “Manutenções”. Para uso desse pacote, o sistema deve operar com o Cálculo .Net – Nova Máquina de Cálculo, por melhor atender as alterações sugeridas pelo governo para o eSocial. Saiba como converter o cálculo, acesse: . Pensando cada vez mais na satisfação do cliente, a TOTVS, permitirá que cada cliente se programe para essa conversão, a partir da liberação da versão 11.52 até a data de carga inicial. Clientes com base de dados na versão 11.82 não precisam converter, pois já estão com o Cálculo .Net ativado.
