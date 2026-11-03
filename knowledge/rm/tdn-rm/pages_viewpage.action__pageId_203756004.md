---
content_hash: 91ad005cb16147f4a4dac72baf0bbe9fcd606b05edf1314bb773f5fbf3523b17
fetched_at: '2026-06-29T00:06:09.655225+00:00'
page_id: '203756004'
product: rm
source: tdn-rm
title: ER_PCREQ-7442_Importação_de_Arquivos_Orca
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=203756004
version: 15
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Projetos |
| **Segmento Executor** | Construção & Projetos | | |
| **Projeto1** | R\_C&P\_TOP008 | **IRM1** | PCREQ-7440 |
| **Requisito1** | PCREQ-7442 | **Subtarefa1** | PDR\_CP\_TOP008-2 |
| **Chamado2** | Não se aplica. | | |
| **Release de Entrega Planejada** | 12.1.8 | **Réplica** | Não |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 Permitir ao usuário realizar a importação de projetos e entidades relacionadas do RM Orca para o TOTVS Obras e Projetos.

## Definição da Regra de Negócio

1. **Informações Gerais**

A funcionalidade "Importar Dados do RM Orca" é habilitada quando não houver projeto aberto, ou seja, após a seleção de um projeto esta opção fica desabilitada.

Os dados das entidades listadas abaixo são importados a critério do usuário, com exceção da entidade de projetos que é obrigatório. São consideradas as hierarquias e relacionamentos destas entidades.

Entidades:

* Projetos;
* Parâmetros;
* Grupo de custos e insumos percentuais;
* Insumos e preços;
* Composições e seus recursos;
* Obras;
* Planilha, cronogramas, medições e sucessoras.

2. **Tela do Processo**

Para melhor entendimento as disposições das informações encontrassem no tópico dos protótipos de tela.

2.1.      **Origem de dados**

Com o RM Orca Instalado

* + Selecionar o diretório. Ao selecionar o diretório, o sistema procura pelo arquivo “FIRMA01\PROJETO.DAT”. Se não existir, o sistema procura pelo arquivo “FIRMA01\PROJETO2.DAT”.
  + Projetos disponíveis. Os projetos encontrados, são exibidos para escolha do usuário.

Sem o RM Orca Instalado

* + Diretório do Projeto. O usuário deve selecionar o PROJETO a ser importado.
  + Descrição do Projeto.

2.2.      **Código do Projeto no Obras e Projetos**

Informar o código do projeto que será importado. Não é permitido a sobreposição, devendo ser informado um código que não exista.

2.3.      **Itens Importados**

O Usuário poderá indicar ao sistema os itens a serem importados, para isto deverá marcar ou informar de acordo com a necessidade as seguintes opções:

**Projetos**

* + Filial**;**
  + Departamento;
  + Centro de Custo.

**Parâmetros** – Importar os parâmetros do projeto.

**Grupos de Custos** – Importar os grupos de custo.

**Unidades** – Validar as unidades e possibilitar ao usuário informar ou criar uma correspondente para substituição.

**Insumos** – importar insumos.

* + Descrição Completa de Insumos – Importar a descrição completa de insumos.
  + Moeda – Utilizado para importação de valor e valor improdutivo de insumos.
  + Marcar Preço Importados – Utilizado para marcar o preço ativo.
  + Habilitar Máscara para Insumos
    - Máscaras para Insumos

**Composições** – Importar as composições.

* + Descrição Completa de Composições – Importar a descrição completa de composições.

**Obras** – Importar a obras.

**Itens da Planilha** – Importar tarefas para planilha

* + Cronograma Previsto;
  + Cronograma Realizado;
  + Medições;
  + Dados do PERT – importar informações do PERT.
  + Ligações do PERT – Importar ligações de sucessoras para o PERT.
  + Manter Associação de Insumos – Manter o insumo/recurso associado a tarefa na planilha.
  + Descrição do Item na Planilha
    - Nome (Reduzido)
    - Descrição do Recurso Associado
    - Descrição 2

**Geral**

* + Converter Acentuação Feitas no DOS – Converte a acentuação de campos textos.

3. **Processo**

3.1.      **Criar Diretório Temporário e Copiar Arquivos**

Cria um diretório temporário com a extensão $$$ e copia todos os arquivos. Copia todos os arquivos com extensão “DAT” e se o usuário marcou o “descrição completa para insumos” ou a "descrição completa para composições", são copiados os arquivos com extensão “DES”. Antes de iniciar a copia realizar o teste de espaço em disco.

Exemplo: *“C:\Inovação\R\_TOP007\12.1.8\PROJ889*” cria o diretório temporário “*'C:\INOVAÇÃO\R\_TOP007\12.1.8\PROJ889.$$$”.*

3.2.      **Informações para Processamento**

O usuário deve informar a localização dos arquivos a serem importados e fazer a opção de quais itens deseja importar. .

Após clicar em avançar o sistema deverá identificar todas as unidades necessárias para processamento que não não estão na base de dados e permitir ao usuário que informe a equivalente. . Somente após informar todas unidades equivalente e que será habilitado a opção de execução.

3.3.      **Projeto**

Ao importa o projeto existindo o RM Orca instalado, o sistema importa os dados do mesmo, senão não existir instalado é criado um novo projeto com a descrição informada pelo usuário. Adicionar no campo “endereço” o seguinte conteúdo “Projeto Importado em DD/MM/AAAA HH:MM:SS”. O código do projeto no TOTVS Construção e Projeto será sempre informado pelo usuário.

Inserir a permissão do usuário corrente no projeto.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Projetos (MPRJ)** | | **Valor Default** | **RM Orca Instalado** | | **RM Orca Não Instalado** |
| **Coluna** | **Descrição** | **PROJETO.DAT** | **PROJETO2.DAT** |
| CODCOLIGADA | Código da Coligada | Coligada Corrente |  |  |  |
| IDPRJ | Identificador do Projeto | AutoInc |  |  |  |
| CODPRJ | Código do Projeto |  |  |  | Informado pelo Usuário |
| DESCRICAO | Nome do Projeto |  | Nome\_Projeto | Nome | Informado pelo Usuário |
| RESPONSAVEL | Endereço |  | Endereco | Endereco | Projeto Importado em DD/MM/AAAA HH:MM:SS |
| RUA | Responsável |  | Cliente | Cliente |  |
| CAMPOLIVRE1 | Campo livre 1 |  |  | CampoLivre1 |  |
| CAMPOLIVRE2 | Campo livre 2 |  |  | CampoLivre2 |  |
| CAMPOLIVRE3 | Campo livre 3 |  |  | CampoLivre3 |  |
| CAMPOLIVRE4 | Campo livre 4 |  |  | CampoLivre4 |  |
| CAMPOLIVREVALOR1 | Campo Livre Valor 1 |  | 0(zero) | CampoLivre5 | 0(zero) |
| CAMPOLIVREVALOR2 | Campo Livre Valor 2 |  | 0(zero) | CampoLivre6 | 0(zero) |
| IDPAI | Id do pai | Autoinc do IDPRJ |  |  |  |

3.4.      **Parâmetros de Projeto**

Verifica a existência dos arquivos de parâmetros e períodos do projeto do RM Orca.

Cria o parâmetro para o projeto e alimenta de acordo com as tabelas de parâmetros, períodos e obras do RM Orca. Valida e grava máscara de insumo ser informada pelo usuário.

Cria um cash dos parâmetros atualizados.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Parâmetros (MPARAMETRO)** | **Valor Default** | **RM Orca** | | |
| **Coluna** | **PARA1.DAT** | **PERIODO.DAT** | **OBRA5.DAT** |
| CODCOLIGADA | Coligada Corrente |  |  |  |
| IDPRJ | AutoInc |  |  |  |
| BDIPRJ |  | BDI |  |  |
| BDIPRJSOBRETOTAL |  | FormaBDI='P' |  |  |
| BDIPRJATIVO | 1(um) |  |  |  |
| BDITRFATIVO |  | ComDif='S' |  |  |
| BDIGRPISMATIVO | 1(um) |  |  |  |
| FATORLEISOCIAL1 |  | LS1 |  |  |
| FATORLEISOCIAL2 |  | LS1 |  |  |
| CONSIDERARQUANTOBRAS |  | QuantObras='S' |  |  |
| CONSIDERARCASASDEC | 1(um) |  |  |  |
| CASASDECQUANTIDADES | 4(quatro) | DecimaisQuant |  |  |
| CASASDECTAXAS | 4(quatro) | DecimaisDif |  |  |
| CASASDECMONETARIOS | 4(quatro) | DecimaisVal |  |  |
| CASASDECPERCENTUAIS | 4(quatro) | DecimaisPerc |  |  |
| CASASDECCOEFICIENTES | 4(quatro) | DecimaisCoef |  |  |
| CASASDECESPECIAIS |  | DecimaisCoef |  |  |
| MASCARAINSUMO | Informado pelo Usuário (Opcional) |  |  |  |
| LEISOBRECUSTOUNITISM |  | FormaLeis='U' |  |  |
| NUMDIASPDO |  |  | NumeroDeDias |  |
| TIPOPDO |  |  | Periodicidade |  |
| DATAINICIOPDOS | Data do Sistema |  | DataInicioDoPeriodo |  |
| NUMPDOSCRONOG | 60(sessenta) |  |  |  |
| MASCARATAREFA |  | Q |  |  |
| DESCTAREFA |  | DefaultDescricao2 |  |  |
| CLIVRE1OBRA |  | UtilizarCampoLivreObra = true |  | CampoLivre1 |
| CLIVRE2OBRA |  | UtilizarCampoLivreObra = true |  | Descricao |
| CLIVRE3OBRA |  | UtilizarCampoLivreObra = true |  | CampoLivre3 |
| CLIVRE4OBRA |  | UtilizarCampoLivreObra = true |  | CampoLivre4 |
| CLIVREVALOR1OBRA |  | UtilizarCampoLivreObra = true |  | CampoLivre5 |
| CLIVREVALOR2OBRA | "Campo Livre Valor 2" | UtilizarCampoLivreObra = true |  |  |
| CLIVRE1CMP | "Campo Livre 1" | UtilizarCampoLivreComm = true |  |  |
| CLIVRE2CMP | "Campo Livre 2" | UtilizarCampoLivreComm = true |  |  |
| PERTSABADOS | 0(zero) |  |  |  |
| PERTDOMINGOS | 0(zero) |  |  |  |
| PERTFERIADOS | 0(zero) |  |  |  |
| PERTCALENDARIO | Em branco |  |  |  |
| INTEGRADONUCLEUS | 0(zero) |  |  |  |
| INTEGRADOOFICINA | 0(zero) |  |  |  |
| NUCLEUSTIPOMOVREQ | Nulo |  |  |  |
| INTEGRADOFLUXUS | 0(zero) |  |  |  |
| USARFATORK | 0(zero) |  |  |  |
| REPETIRCODAUXPLAN | 0(zero) |  |  |  |
| IGUALARRECURSOTAREFA | 0(zero) |  |  |  |

3.5.      **Cenários**

Insere os cenários principal e de 1 a 4.

3.6.      **Grupos de Custos**

Verifica a existência do arquivo de grupo de custos no RM Orca.

Realiza a importação dos grupos de custos.

A informações de grupo DNER e Custo serão necessários na importação de insumos.

Para os grupo de custos que no RM Orca está definido como custo igual ”P” deve incluir na tabela de Insumo Percentual (MPERCENT) os grupos relacionados.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Grupos de Custo (MGIS)** | | **Valor Default** | **RM Orca** | **Observação** |
| **Coluna** | **Descrição** | **GRUPO4.DAT** |
| CODCOLIGADA | Código da Coligada | Coligada Corrente |  |  |
| IDPRJ | Identificador do Projeto | Identificador do Projeto Importado |  |  |
| IDGIS | Identificador do Grupo de Custo | AutoInc | Posição no Arquivo - 1 |  |
| DESCGIS | Descrição do Grupo de Custo |  | DescricaoGrupo |  |
| GRUPODNER | Grupo Dner | A | GrupoDner |  |
| BDI | Bdi do Grupo de Custo |  | BDI |  |
| CODISMINI | Código Insumo Inicial |  | DeInsumo | Ver parâmetro tamanho código |
| CODISMFIM | Código Insumo Final |  | AInsumo | Ver parâmetro tamanho código |
| LEISOCIAL | Lei Social | 0(zero) | TipoItem = 'L' então LeiSocialNumero |  |
| PERCSOBREGRPDNER | Percentual Sobre o Grupo Dner |  | Custo = 'P' então  SobreGrupoDner |  |
|  |  |  |  |  |
| **Insumo Percentual (MPERCENT)** | | **Valor Default** | **RM Orca** | **Observação** |
| **Coluna** | **Descrição** | **GRUPO4.DAT** |
| CODCOLIGADA | Código da Coligada | Coligada Corrente |  |  |
| IDPRJ | Identificador do Projeto | Coligada Corrente |  |  |
| IDGIS | Identificador do Grupo de Custo | Identificador do Projeto Importado |  |  |
| IDPERC | Identificador de Insumo Percentual |  | SobreGrupoUnitario1 até SobreGrupoUnitario1 |  |

3.7.      **Unidades**

Verifica a existência dos arquivos de insumos e composições no RM Orca.

Avalia a falta ou a existência de unidades não cadastradas no Construção e Projetos. Caso existam, as mesmas são exibidas para o usuário no início do processo para permitindo adicionar uma equivalente. Deve considerar as unidades dos insumos que o grupo de custo não esteja definido como “P” (percentual). Estas informações são utilizadas no momento de importação dos insumos e composição.

3.8.      **Insumos**

Verifica a existência do arquivo de insumos no RM Orca.

Valida existência do grupo de custos.

Se usuário informou máscara para o insumo, a mesma é aplicada.

Se grupo de custo igual a “P” (insumo percentual), informar a unidade “%”.

Verifica se o usuário informou que deve importar a descrição completa de insumos.

Importa os preços 1 e 2. Considera para cada preço a importação do valor e valor improdutivo. Adiciona a moeda a informada pelo usuário como produtiva e improdutiva.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Insumos (MISM)** | | **Valor Default** | **RM Orca** | **Observação** |
| **Coluna** | **Descrição** | **INSUMO7A.DAT** |
| CODCOLIGADA | Código da Coligada | Coligada Corrente |  |  |
| IDPRJ | Identificador do Projeto | Identificador do Projeto Importado |  |  |
| IDISM | Identificador do Insumo | Autoinc |  |  |
| CODAPLIC | Código da Aplicação = M | M |  |  |
| CODISM | Código do Insumo |  | Num\_Item | Verifica Máscara e parâmetro tamanho código |
| DESCISM | Descrição do Insumo |  | Descricao | Converter acentuação |
| CODUND | Unidade |  |  |  |
| GRUPODNER | Grupo Dner |  |  | Resgatar o GRUPODNER do grupo de custo. |
| IDISMPRC | Identificador do Preço de Insumo | Nulo |  |  |
| IDGIS | Identificador do Grupo de Custo |  | Grupo | Identificar o correspondente cadastrado. |
| VALOR | Valor | 0(zero) |  |  |
| VALORSEMLEIS | Valor sem Leis | 0(zero) |  |  |
| VALORIMPRODUTIVO | Valor Improdutivo | 0(zero) |  |  |
|  |  |  |  |  |
| **Descrição Completa de Insumos (MISMDESC)** | | **Valor Default** | **RM Orca** | **Observação** |
| **Coluna** | **Descrição** | **Ixxxxxx.DES** |
| CODCOLIGADA | Código da Coligada | Coligada Corrente |  |  |
| IDPRJ | Identificador do Projeto | Identificador do Projeto Importado |  |  |
| IDISM | Identificador do Insumo | Identificador do Insumo Importado |  |  |
| DESCRICAOCOMPLETA | Desc. Completa do Insumo |  | Texto do Arquivo |  |
|  |  |  |  |  |
| **Preços de Insumo (MISMPRC)** | | **Valor Default** | **RM Orca** | **Observação** |
| **Coluna** | **Descrição** | **INSUMO7A.DAT** |
| CODCOLIGADA | Código da Coligada | Coligada Corrente |  |  |
| IDPRJ | Identificador do Projeto | Identificador do Projeto Importado |  |  |
| IDISM | Identificador do Insumo | Identificador do Insumo Importado |  |  |
| IDPRJPRC | Identificador do Projeto | Identificador do Projeto Importado |  |  |
| IDISMPRC | Identificador do Preço do Insumo | Autoinc |  |  |
| DESCISMPRC | Descrição do Preço do Insumo | "Preço 1" ou "Preço 2" |  | Informar de acordo com o preço importado |
| VALOR | Valor |  | Preco1 ou Preco2 | Informar de acordo com o preço importado |
| VALORIMPRODUTIVO | Valor Improdutivo |  | Preco\_Imp1 ou Preco\_Imp2 | Informar de acordo com o preço importado |
| CODUND | Unidade | Código da unidade do insumo importado |  |  |
| DATAATUALIZACAO | Data de Atualização do Preço |  | Data1 | Se não informada, colocar a do sistema. |
| CODMOEVALOR | Moeda do Valor | Informada pelo usuário |  |  |
| CODMOEVALORIMPRODUTIVO | Moeda do Valor Improdutivo | Informada pelo usuário |  |  |
| MOEDAINDEXACAO | Moeda de Indexação | Nulo |  |  |

3.9.      **Composições**

Verifica a existência do arquivo de composições no RM Orca.

Verifica a existência do arquivo de insumos no RM Orca..

Valida descrição da composição e logar erro caso não exista.

Verifica se o usuário informou a para importar a descrição completa de composições.

Verifica os insumos associados de 1 a 30  na estrutura do RM Orca, para importar como recursos.

Se o código do insumo for negativo é considerado uma composição.

Se o recurso for de produção, verifica a distância média de transporte. Para recurso que seja um insumo é considerado o coeficiente produtivo.

Se usuário marcou “Dados do PERT”, importa conteúdo do campo equipe do recurso.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Composições (MCMP)** | | **Valor Default** | **RM Orca** | **Observação** |
| **Coluna** | **Descrição** | **COMP7A.DAT** |
| CODCOLIGADA | Código da Coligada | Coligada Corrente |  |  |
| IDPRJ | Identificador do Projeto | Identificador do Projeto Importado |  |  |
| IDCMP | Identificador da Composição | Autinc |  |  |
| CODCMP | Código da Composição |  | Composicao | Verificar parâmetro tamanho código |
| DESCCMP | Descrição da Composição |  | Descricao |  |
| TIPOCOMPOSICAO | Tipo da composição | 0(zero) | Producao | Se "Produção" do RM Orca maior que 0(zero) Colocar 1. |
| CAMPOLIVRE1 | Campo Livre 1 |  | CampoLivre1 | Se parâmetro "UtilizarCampoLivreComm" desmarcado deve limpar o campo |
| CAMPOLIVRE2 | Campo Livre 2 |  | CampoLivre2 | Se parâmetro "UtilizarCampoLivreComm" desmarcado deve limpar o campo |
| CODUND | Unidade |  | Unidade |  |
| PRODUCAOPORHORA | Produção por Hora | Nulo | Producao | Se "Produção" do RM Orca maior que 0(zero). |
| EXCLUSIVA | Exclusiva | 0(zero) |  |  |
|  |  |  |  |  |
| **Descrição Completa de Composições (MCMPDESC)** | | **Valor Default** | **RM Orca** | **Observação** |
| **Coluna** | **Descrição** | **Cxxxxxx.DES** |
| CODCOLIGADA | Código da Coligada | Coligada Corrente |  |  |
| IDPRJ | Identificador do Projeto | Identificador do Projeto Importado |  |  |
| IDCMP | Identificador da Composição | Identificador da composição Importada |  |  |
| DESCRICAOCOMPLETA | Desc. Completa da Composição |  | Texto do Arquivo |  |
|  |  |  |  |  |
| **Recursos de Composição (MRECCMP)** | | **Valor Default** | **RM Orca** | **Observação** |
| **Coluna** | **Descrição** | **COMP7A.DAT** |
| CODCOLIGADA | Código da Coligada | Coligada Corrente |  |  |
| IDPRJ | Identificador do Projeto | Identificador do Projeto Importado |  |  |
| IDCMP | Identificador da Composição | Identificador da composição Importada |  |  |
| IDPRJREC | Ident. Projeto Origem do Recurso | Identificador do Projeto Importado |  |  |
| IDREC | Identificador do Recurso | AutoInc |  |  |
| IDCMPFILHA | Identificador da Composição Auxiliar | Nulo | Insumo | Informar se recurso for uma composição |
| IDISM | Identificador do Insumo | Nulo | Insumo | Informar se recurso for um insumo |
| GRUPODNER | Grupo Dner |  |  | Grupo DNER do recurso importado |
| QUANTIDADE | Quantidade |  | Coef |  |
| ATIVO | Ativo | 1(um) |  |  |
| DMT | Dmt - Distância Média de Transporte | 1(um) | Produtivo |  |
| COEFICIENTEPRODUTIVO | Coeficiente Produtivo | 1(um) | Produtivo |  |
| EQUIPE | Equipe H/H | 1(um) | Equipe |  |
| COEFICIENTEIMPRODUTIVO | Coeficiente Improdutivo | 0(zero) |  |  |

3.10.      **Planilha de Atividades**

Verifica  no RM Orca a existência do arquivo de obras, tarefas, composições, insumos e calendário.

Caso não exista o arquivo de calendário deve considerado como default a jornada de 8 horas e 5 dias úteis.

3.10.1.    **Importando a obra**

Verificar a existência do arquivo de obras no RM Orca.

A obras são importadas para a planilha de atividades e para entidade de obras.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Tarefas (MTAREFA)** | | **Valor Default** | **RM Orca** | **Observação** |
| **Coluna** | **Descrição** | **OBRA5.DAT** |
| CODCOLIGADA | Código da Coligada | Coligada Corrente |  |  |
| IDPRJ | Identificador do Projeto | Identificador do Projeto Importado |  |  |
| IDTRF | Identificador da Tarefa | Autoinc |  |  |
| CODTRF | Código da Tarefa |  | Num\_Obra | Utilizar máscara ### |
| NOME | Nome |  | Descricao |  |
| IDPAI | Identificador da Tarefa Pai | Valor definido em IDTRF |  |  |
| DESCRICAO | Descrição da Tarefa |  | Descricao |  |
| QUANTIDADE | Quantidade |  | QuantObras |  |
| VALOR | Valor Cotado | Nulo |  |  |
| CODUND | Unidade | Nulo |  |  |
| BLOQUEADA | Bloqueada | 0(zero) |  |  |
| SUBOBRA | Subobra | 0(zero) |  |  |
| SERVICO | Serviço | 0(zero) |  |  |
| IDCMP Identificador de Composição |  | Nulo |  |  |
| IDISM | Identificador do Insumo | Nulo |  |  |
| BDI | Bdi da Tarefa | Nulo |  |  |
| UTILIZARVALOR | Utilizar Valor | 0(zero) |  |  |
| ATIVA | Ativa | 1(um) |  |  |
|  |  |  |  |  |
| **Obras (MOBRA)** | | **Valor Default** | **RM Orca** | **Observação** |
| **Coluna** | **Descrição** | **OBRA5.DAT** |
| CODCOLIGADA | Código da Coligada | Coligada Corrente |  |  |
| IDPRJ | Identificador do Projeto | Identificador do Projeto Importado |  |  |
| IDTRF | Identificador da Tarefa | Identificador da tarefa importada |  |  |
| CAMPOLIVRE1 | Campo Livre 1 |  | CampoLivre1 | Informar se o parâmetro "Utilizar Campo Livre Obra" estiver marcado. Limitar o tamanho em 20. |
| CAMPOLIVRE2 | Campo Livre 2 |  | CampoLivre3 |  |
| CAMPOLIVRE3 | Campo Livre 3 |  | CampoLivre4 |  |
| CAMPOLIVRE4 | Campo Livre 4 |  | CampoLivre5 |  |
| CAMPOLIVREVALOR1 | Campo Livre Valor 1 |  | CampoLivre2 |  |
| CAMPOLIVREVALOR2 | Campo Livre Valor 2 | Nulo |  |  |
| DATAFIM | Data de Fim | Nulo | DataFim |  |
| DATAINICIO | Data de Início | Nulo | DataInicio |  |

3.10.2.   **Importando Tarefas**

Verifica a existência do arquivo de tarefas no RM Orca.

Valida a existência da tarefa “pai”.

Quando o usuário marcar a opção “Manter a associação dos insumos” a unidade deve ser a do insumo, senão marcado usa o default “VB”(verba).  As tarefas definidas como verbas devem receber o valor do insumo.

Quando vinculado a composição a unidade será a definida na composição.

3.10.2.1.    **Importar dados do PERT**

Importa as datas de início e fim de planejamento se existentes.

Importa as datas de início e fim calculadas se a data de início calculada existir. Verifica a data em relação a data de início da obra prevalecendo a mais recente.

Importa as datas de início e fim cedo se a data de início cedo existir. Verificar a data em relação a data de início da obra prevalecendo a mais recente.

Importa as datas de início e fim tarde se a data de início tarde existir. Verificar a data em relação a data de início da obra prevalecendo a mais recente.

Importa as datas de início e fim real se a data de início real existir.

Importa a duração se existir.

3.10.2.2.    **Importar Cronograma Previsto**

Importa o cronograma realizado para cada período.

3.10.2.3.    **Importar Cronograma Realizado**

Importa o cronograma realizado para cada período.

3.10.2.4.    **Importar Medição**

Verifica e validar as tarefas "pais". Caso a tarefa não possua um “pai”, não deverá ser importada.

3.10.2.5.    **Ligações do PERT**

Importa as tarefas sucessoras.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Tarefas (MTAREFA)** | | **Valor Default** | **RM Orca** | **Observação** |
| **Coluna** | **Descrição** | **PLAN7A.DAT** |
| CODCOLIGADA | Código da Coligada | Coligada Corrente |  |  |
| IDPRJ | Identificador do Projeto | Identificador do Projeto Importado |  |  |
| IDTRF | Identificador da Tarefa | Autoinc |  |  |
| CODTRF | Código da Tarefa |  | Plano | Verificar parâmetro máscara. |
| NOME | Nome |  | Plano2 |  |
| BLOQUEADA | Bloqueada | 0(zero) |  |  |
| SUBOBRA | Subobra | 0(zero) |  |  |
| BDI | Bdi da Tarefa |  | BDI |  |
| ATIVA | Ativa |  | STATUS |  |
| DESCRICAO | Descrição da Tarefa |  | Descricao | Validar opção do usuário para o preenchimento. |
| SERVICO | Serviço | 0(zero) |  |  |
| IDPRJREC | Ident. Projeto Origem do Recurso | Identificador do Projeto Importado |  | Limpar este campo se não houver recurso associado. |
| IDISM | Identificador do Insumo |  |  | Se recurso for insumo. |
| IDCMP | Identificador de Composição |  |  | Se recurso for composição. |
| CODUND | Unidade |  |  | Unidade do Recurso ou Verba. |
| UTILIZARVALOR | Utilizar Valor | 0(zero) |  | Colocar 1(um) se tarefa definida como verba. |
| QUANTIDADE | Quantidade |  | Quant |  |
| DATAINICIOPLAN | Data de Início Planejada | Nulo | Pert.DIFixada | Verifica opção do usuário para importar PERT. |
| DATAFIMPLAN | Data de Fim Planejada | Nulo | Pert.DTFixada | Verifica opção do usuário para importar PERT. |
| DATAINICIOCALC | Data de Início Calculada | Nulo | Pert.DataInicioCalculada | Verifica opção do usuário para importar PERT. Validar data início da obra. |
| DATAFIMCALC | Data de Fim Calculada | Nulo | Pert.DataFimCalculada | Verifica opção do usuário para importar PERT. Validar data início da obra. |
| DATAINICIOCEDO | Data de Início Cedo | Nulo | Pert.PDI | Verifica opção do usuário para importar PERT. Validar data início da obra. |
| DATAFIMCEDO | Data de Fim Cedo | Nulo | Pert.PDT | Verifica opção do usuário para importar PERT. Validar data início da obra. |
| DATAINICIOTARDE | Data de Início Tarde | Nulo | Pert.UDI | Verifica opção do usuário para importar PERT. Validar data início da obra. |
| DATAFIMTARDE | Data de Fim Tarde | Nulo | Pert.UDT | Verifica opção do usuário para importar PERT. Validar data início da obra. |
| DATAINICIOREAL | Data de Início Real | Nulo | Pert.DataInicioReal | Verifica opção do usuário para importar PERT. |
| DATAFIMREAL | Data de Fim Real | Nulo | Pert.DataFimReal | Verifica opção do usuário para importar PERT. |
| DURACAOPLAN | Duração Fixada | Nulo | Pert.Duracao | Verifica opção do usuário para importar PERT. |
| DURACAOCALC | Duração Programada | Nulo | Pert.DuracaoCalculada | Verifica opção do usuário para importar PERT. |
| DURACAOREAL | Duração Real | Nulo | Pert.DuracaoReal | Verifica opção do usuário para importar PERT. |
| FOLGACALC | Folga Calculada | Nulo | Pert.FL | Verifica opção do usuário para importar PERT. |
|  |  |  |  |  |
| **Cronograma Planejado (MTRFPLAN)** | | **Valor Default** | **RM Orca** | **Observação** |
| **Coluna** | **Descrição** | **PLAN7A.DAT** |
| CODCOLIGADA | Código da Coligada | Coligada Corrente |  | Verificar opção do usuário para importar cronograma previsto. |
| IDPRJ | Identificador do Projeto | Identificador do projeto importado |  |  |
| IDTRF | Identificador da Tarefa | Identificador da tarefa importada |  |  |
| NUMPERIODO | Número do Período |  | Posição no "array" | De 1 até 60 períodos. |
| PERCPLANEJADO | Percentual Planejado |  | Cronograma |  |
|  |  |  |  |  |
| **Cronograma Realizado (MTRFREAL)** | | **Valor Default** | **RM Orca** | **Observação** |
| **Coluna** | **Descrição** | **PLAN7A.DAT** |
| CODCOLIGADA | Código da Coligada | Coligada Corrente |  | Verificar opção do usuário para importar cronograma realizado. |
| IDPRJ | Identificador do Projeto | Identificador do projeto importado |  |  |
| IDTRF | Identificador da Tarefa | Identificador da tarefa importada |  |  |
| NUMPERIODO | Número do Período |  | Posicao no "array" | De 1 até 60 períodos. |
| PERCREALIZADO | Percentual Realizado |  | Executado |  |
|  |  |  |  |  |
| **Cronograma Medido (MTRFMEDIDO)** | | **Valor Default** | **RM Orca** | **Observação** |
| **Coluna** | **Descrição** | **PLAN7A.DAT** |
| CODCOLIGADA | Código da Coligada | Coligada Corrente |  | Verificar opção do usuário para importar medições. |
| IDPRJ | Identificador do Projeto | Identificador do projeto importado |  |  |
| IDTRF | Identificador da Tarefa | Identificador da tarefa importada |  |  |
| NUMPERIODO | Número do Período |  | Posicao no "array" | De 1 até 60 períodos. |
| NUMMEDICAO | Número da Medição | 1(um) | Medicao |  |
| QUANTMEDIDA | Quantidade Medida |  |  |  |
| VALORDEDUZIDO | Valor Deduzido |  | Retencao | Se Retenção < 0 |
| VALORRETIDO | Valor Retido |  | Retencao | Se Retenção > 0 |
|  |  |  |  |  |
| **Tarefas Sucessoras (MTRFSUC)** | | **Valor Default** | **RM Orca** | **Observação** |
| **Coluna** | **Descrição** | **PLAN7A.DAT** |
| CODCOLIGADA | Código da Coligada | Coligada Corrente |  | Verificar opção do usuário para importar ligações do PERT |
| IDPRJ | Identificador do Projeto | Identificador do projeto importado |  |  |
| IDTRF | Identificador da Tarefa | Identificador da tarefa importada |  |  |
| IDTRFSUC | Identificador da Tarefa Sucessora |  | Pert.Suc |  |
| TIPOLIGACAO | Tipo de Ligação |  | Pert.TipoDeLigacao |  |
| DEFASAGEM | Defasagem |  | Pert.Lag |  |

3.11.   **Eliminar arquivos temporários**

Após o término do processamento os arquivos copiados temporariamente são eliminados.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Importar Dados do RM Orca | Criação | Projetos-> Construção e Projetos-> Projeto-> agrupador Utilitários->  Conversões-> Importar Dados do RM Orca | - |
|  |  |  |  |
|  |  |  |  |

***Tabelas Utilizadas***

* *Não se Aplica.*

## Protótipo de Tela

**Protótipo 01 - Opções de Importação**

****Protótipo 02 - Unidades não Encontradas****

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
