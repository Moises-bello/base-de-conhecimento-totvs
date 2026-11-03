---
content_hash: 709007f9acf85b510efd09835d5a68f3a23dccc1024b753b2b0326a96564d96f
fetched_at: '2026-06-29T00:08:42.400543+00:00'
page_id: '287070868'
product: rm
source: tdn-rm
title: ER MATESTCNTFTOF01-785 Registro S-1250 - eSocial
type: documentation
url: https://tdn.totvs.com/display/LRM/ER+MATESTCNTFTOF01-785+Registro+S-1250+-+eSocial
version: 151
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## **Informações Gerais**

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | Movimento |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | MATESTCNTFTOF01 | **IRM/EPIC1** | MATESTCNTFTOF01-785 |
| **Requisito/Story/Issue1** | MATESTCNTFTOF01-813 | **Subtarefa1** | NA |
| **Chamado/Ticket2** | NA | | |
| **País** | ( x ) Brasil | | |
| **Outros** | NA | | |

## **Objetivo**

O Decreto nº 8373/2014 instituiu o **Sistema de Escrituração Digital das Obrigações Fiscais, Previdenciárias e Trabalhistas (****eSocial****).** Por esse sistema, os empregadores passarão a comunicar ao Governo, de forma unificada, as informações relativas aos trabalhadores, como vínculos, contribuições previdenciárias, folha de pagamento, comunicações de acidente de trabalho, aviso prévio, escriturações fiscais e informações sobre o FGTS.

 O eSocial torna-se obrigatório a partir de janeiro de 2018 para empresas com faturamento acima de 78 milhões e em junho de 2018 para todas as outras.

Em virtude disso, iremos criar um serviço de geração de arquivo .xml para uso do TOTVS Gestão de Folha de Pagamento, que retornará dados necessários para a geração da rotina eSocial, mais especificamente o registro S-1250 - Aquisição de Produção Rural, conforme leiaute definido pela Receita Federal do Brasil.

## **Definição da Regra de Negócio**

Implementações Necessárias - Item de Movimento

* Em **Tributos e Valores | Tributos**, na grid de edição de tributos deverá ser incluída uma nova coluna chamada **Valor Ret. Suspensa Judicialmente**, do tipo valor, tamanho 9. Essa coluna conterá o valor que não foi retido do imposto devido decisão/ordem proferida em processo judicial e será preenchida manualmente pelo usuário para cada tributo em que couber tal informação.  
  Essa coluna vai estar sempre visível, mas somente poderá ser editada quando o tributo correspondente for do tipo (DTRIBUTO.TIPOTRIBFISC) "INSS" ou "FUNRural".

Serviço de Geração dos Dados

O serviço que será implementado será chamado pelo TOTVS Gestão de Recursos Humanos, que irá passar os parâmetros de Filial e Competência (mês/ano) para o TOTVS Gestão de Estoque, Compras e Faturamento. Com esses parâmetros, o TOTVS Gestão de Estoque, Compras e Faturamento deverá gerar as informações que serão utilizadas na geração da rotina e-Social, em formato de arquivo .xml.

Para isso, deve-se filtrar as NF-es de entrada (FTDO.CODMODDOC = 55, 04 ou 1B, Tipo Movimento 1.2.xx) em que o fornecedor (TMOV.CODCFO) ou fornecedor origem/destino (TMOV.CODCFONATUREZA) seja produtor rural (FCFO.RAMOATIV = 16). Os dados deverão ser gerados conforme o leiaute abaixo:

**Obs.:** Os esquemas XSD podem ser verificados no site do eSocial (<http://portal.esocial.gov.br/institucional/documentacao-tecnica>). Utilizar versão 2.4.

**IMPORTANTE:** Para a Parametrização e Apuração de Tributos - FUNRURAL, GILRAT, SENAR \ INSS, INSS15, INSS20 e INSS25  segue o link:

**Pessoa Jurídica:**

**Pessoa Física/Jurídica:**

* Parametrização:

**FTDO.CODMODDOC = 55, 04 ou 1B**

**(TMOV.CODCFO) ou fornecedor origem/destino (TMOV.CODCFONATUREZA)**

**(FCFO.RAMOATIV = 16)**

******(FCFOCOMPL.CPFCOMPLEMENTAR - Se Produtor Rural é Pessoa Física com CNPJ cadastrado)******

**(FCFOCOMPL.INDOPCCP****- Deverá ser preenchido com o código 1 e 2 conforme layout do eSocial 02.05, para indicar a opção do produtor rural pela forma de tributação da contribuição previdenciária.)**

Crie a tabela dinâmica com os dados abaixo

**e cadastre o campo complementar**

**Nome:** INDOPCCP

**Tamanho:**10

**Tipo:** Alfanumérico

A partir do release **12.1.25** as informações acima de CPF do Produtor Rural e Indicativo da forma de tributação estarão disponíveis no cadastro de **Cliente/Fornecedor,**anexo **eSocial** campos **CPF** e **Indicativo da opção pelo produtor rural pela forma de tributação da contribuição previdenciária.**

**INCLUSÃO DO MOVIMENTO (DO TIPO “COMPRAS” COM CLASSIFICAÇÃO 1.2.XX):**

**INCLUSÃO DO MOVIMENTO (DO TIPO “COMPRAS” COM CLASSIFICAÇÃO 1.2.XX) PESSOA FÍSICA:**

* Manter as mesmas parametrizações para inclusão de Movimento Pessoa Jurídica acrescentando as seguintes Etapas:

Acessar o Cadastro da Filial e selecionar a opção Anexos >> Dados Fiscais:

* Acessar os parâmetros do Tipo de Movimento na Etapa Fis - Natureza:

* Marcando o Parâmetro acima o campo Fornecedor Origem/Destino ficará habilitado para edição:

**APÓS A INCLUSÃO DO MOVIMENTO, O REGISTRO DEVERÁ APARECER NO RESULTADO DA CONSULTA: (Consulta oficial do serviço)**

BuscaMovimentosClassificadosESocialAquisicaoProduto(codcoligada, codFilial, mes, ano)

        SELECT  TMOV.CODCOLIGADA, TMOV.CODFILIAL, TMOV.IDMOV, TITMMOV.VALORBRUTOITEM VALORBRUTO,

                TMOV.DATAEMISSAO, TMOV.NUMEROMOV, TMOV.SERIE, TMOV.CODCFO,

                FCFO\_CFO.PESSOAFISOUJUR FPESSOAFISOUJUR, FCFO\_CFO.RAMOATIV FRAMOATIV, FCFO\_CFO.CGCCFO FCGCCFO,

                TMOV.CODCFONATUREZA,

                FCFO\_NAT.PESSOAFISOUJUR JPESSOAFISOUJUR, FCFO\_NAT.RAMOATIV JRAMOATIV, FCFO\_NAT.CGCCFO JCGCCFO,

                TITMMOV.NSEQITMMOV, TPRODUTODEF.PRDISENTOFUNRURAL, FCFOCOMPL.CPFCOMPLEMENTAR (**somente se o campo estiver criado na base de dados**)

          FROM

                TMOV (NOLOCK)

                JOIN TITMMOV (NOLOCK)

                  ON TITMMOV.CODCOLIGADA = TMOV.CODCOLIGADA AND

                     TITMMOV.IDMOV = TMOV.IDMOV

                JOIN TPRODUTODEF (NOLOCK)

                  ON TPRODUTODEF.CODCOLIGADA = TITMMOV.CODCOLIGADA AND

                     TPRODUTODEF.IDPRD = TITMMOV.IDPRD

                JOIN FTDO (NOLOCK)

                  ON FTDO.CODCOLIGADA = TMOV.CODCOLIGADA AND

                      FTDO.CODTDO = TMOV.CODTDO

                LEFT JOIN FCFO FCFO\_CFO (NOLOCK)

                  ON FCFO\_CFO.CODCOLIGADA = TMOV.CODCOLCFO AND

                      FCFO\_CFO.CODCFO = TMOV.CODCFO AND

                      FCFO\_CFO.RAMOATIV = 16 AND

                      FCFO\_CFO.CGCCFO IS NOT NULL

                LEFT JOIN FCFO FCFO\_NAT (NOLOCK)

                  ON FCFO\_NAT.CODCOLIGADA = TMOV.CODCOLCFONATUREZA AND

                      FCFO\_NAT.CODCFO = TMOV.CODCFONATUREZA AND

                      FCFO\_NAT.RAMOATIV = 16 AND

                      FCFO\_NAT.CGCCFO IS NOT NULL

                LEFT JOIN DCFOP

                  ON DCFOP.IDNAT = TMOV.IDNAT AND

                      DCFOP.CODCOLIGADA = TMOV.CODCOLIGADA

                LEFT JOIN FCFOCOMPL (NOLOCK)

                  ON FCFOCOMPL.CODCOLIGADA = FCFO\_CFO.CODCOLIGADA AND

                        FCFOCOMPL.CODCFO = FCFO\_CFO.CODCFO

          WHERE TMOV.CODCOLIGADA = :CODCOLIGADA AND

                TMOV.CODFILIAL = :CODFILIAL AND

                TMOV.CODTMV LIKE '1.2%'  AND

                TMOV.DATAEMISSAO >= :DATAEMISSAO\_INI AND

                TMOV.DATAEMISSAO <= :DATAEMISSAO\_FIM AND

                FTDO.CODMODDOC = :CODMODDOC AND

                TMOV.STATUS<> 'C' AND

                ((FCFO\_NAT.RAMOATIV IS NOT NULL) OR (FCFO\_CFO.RAMOATIV IS NOT NULL)) AND

               DCFOP.CODNAT NOT LIKE '1.451%' AND DCFOP.CODNAT NOT LIKE '1.921%' AND DCFOP.CODNAT NOT LIKE '1.949%'     (**O movimento com natureza de Operação dos tipos: "X.202%, X.411%", "X.451%, **"X.452%, "X.453%,** X.554%, **"X.905%,** X.921%" e "X.949%" (onde X é um prefixo que será substituído por um dos****algarismos seguintes****: "1", "2", "3" e "8"), na aquisição de produtos, devem ser ignoradas**)

**Exceção**

 - Item que for produto e natureza "2.949.XX" vai ser considerado no S-1250

**INFORMAR OS PARÂMETROS:**

CODCOLIGADA;

CODFILIAL;

CODMODDOC: 55, 04 ou 1B

DATAEMISSAO: Data Emissão do Movimento

**A partir do release 12.1.25 utilizar a consulta abaixo:**

SELECT  TMOV.CODCOLIGADA, TMOV.CODFILIAL, TMOV.IDMOV, TITMMOV.VALORBRUTOITEM VALORBRUTO,

                TMOV.DATAEMISSAO, TMOV.NUMEROMOV, TMOV.SERIE, TMOV.CODCFO,

                FCFO\_CFO.PESSOAFISOUJUR FPESSOAFISOUJUR, FCFO\_CFO.RAMOATIV FRAMOATIV, FCFO\_CFO.CGCCFO FCGCCFO,

                TMOV.CODCFONATUREZA,

                FCFO\_NAT.PESSOAFISOUJUR JPESSOAFISOUJUR, FCFO\_NAT.RAMOATIV JRAMOATIV, FCFO\_NAT.CGCCFO JCGCCFO,

                TITMMOV.NSEQITMMOV, TPRODUTODEF.PRDISENTOFUNRURAL, PESOCIALCLIFOR.CPF, PESOCIALCLIFOR.INDOPCCP

          FROM

                TMOV (NOLOCK)

                JOIN TITMMOV (NOLOCK)

                  ON TITMMOV.CODCOLIGADA = TMOV.CODCOLIGADA AND

                     TITMMOV.IDMOV = TMOV.IDMOV

                JOIN TPRODUTODEF (NOLOCK)

                  ON TPRODUTODEF.CODCOLIGADA = TITMMOV.CODCOLIGADA AND

                     TPRODUTODEF.IDPRD = TITMMOV.IDPRD

                JOIN FTDO (NOLOCK)

                  ON FTDO.CODCOLIGADA = TMOV.CODCOLIGADA AND

                      FTDO.CODTDO = TMOV.CODTDO

                LEFT JOIN FCFO FCFO\_CFO (NOLOCK)

                  ON FCFO\_CFO.CODCOLIGADA = TMOV.CODCOLCFO AND

                      FCFO\_CFO.CODCFO = TMOV.CODCFO AND

                      FCFO\_CFO.RAMOATIV = 16 AND

                      FCFO\_CFO.CGCCFO IS NOT NULL

                LEFT JOIN FCFO FCFO\_NAT (NOLOCK)

                  ON FCFO\_NAT.CODCOLIGADA = TMOV.CODCOLCFONATUREZA AND

                      FCFO\_NAT.CODCFO = TMOV.CODCFONATUREZA AND

                      FCFO\_NAT.RAMOATIV = 16 AND

                      FCFO\_NAT.CGCCFO IS NOT NULL

                LEFT JOIN DCFOP

                  ON DCFOP.IDNAT = TMOV.IDNAT AND

                      DCFOP.CODCOLIGADA = TMOV.CODCOLIGADA

                LEFT JOIN PESOCIALCLIFOR (NOLOCK)

                  ON PESOCIALCLIFOR.CODCOLIGADA = FCFO\_CFO.CODCOLIGADA AND

                        PESOCIALCLIFOR.CODCFO = FCFO\_CFO.CODCFO

          WHERE TMOV.CODCOLIGADA = :CODCOLIGADA AND

                TMOV.CODFILIAL = :CODFILIAL AND

                TMOV.CODTMV LIKE '1.2%'  AND

                TMOV.DATAEMISSAO >= :DATAEMISSAO\_INI AND

                TMOV.DATAEMISSAO <= :DATAEMISSAO\_FIM AND

                FTDO.CODMODDOC = :CODMODDOC AND

                TMOV.STATUS<> 'C' AND

                ((FCFO\_NAT.RAMOATIV IS NOT NULL) OR (FCFO\_CFO.RAMOATIV IS NOT NULL)) AND

 DCFOP.CODNAT NOT LIKE '1.451%' AND DCFOP.CODNAT NOT LIKE '1.921%' AND DCFOP.CODNAT NOT LIKE '1.949%'    (**O movimento com natureza de Operação dos tipos "Y.202%, Y.411%", "Y.451%, "Y.452%, "Y.453%, Y.554%, "Y.905%, Y.921%" e "Y.949%" (onde Y é um prefixo que será substituído por um dos algarismos seguintes: "5", "6", "7" e "9"), na venda de produtos, devem ser ignoradas**)

**Após selecionado o Movimento será feito o filtro de acordo com combinação de parâmetros para a formação do indicador de aquisição descritos em Informações no Sistema no quadro abaixo.****Serão apresentados no eSocial apenas os movimentos que se enquadrarem em um dos indicadores de Aquisição:**

| Nível | Campo | Tipo | Tamanho | Ocorrência | Obrig. | Descrição | Informação no Sistema | Observações |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | tpAquis |  |  | 1-3 | O | Registro preenchido por Pessoa Jurídica em geral, quando o estabelecimento identificado no registro superior efetuar aquisição de produtos rurais de pessoa física. O registro também deve ser preenchido nas seguintes situações: - Por PF, quando a mesma adquire produção de produtor rural pessoa física ou segurado especial para venda no varejo a consumidor final pessoa física; - Por Entidade inscrita no Programa de Aquisição de Alimentos (PAA), quando a mesma efetuar a aquisição de produtos rurais no âmbito do PAA, de produtor rural pessoa física ou pessoa jurídica. |  |  |
| 1.1 | indAquis | N | 1 | 1-1 | O | Indicativo da Aquisição: 1 - Aquisição da produção de produtor rural pessoa física ou segurado especial em geral; 2 - Aquisição da produção de produtor rural pessoa física ou segurado especial em geral por Entidade do PAA; 3 - Aquisição da produção de produtor rural pessoa jurídica por Entidade do PAA.  4 - Aquisição da produção de produtor rural pessoa física ou segurado especial em geral - Produção Isenta (Lei 13.606/2018); 5 - Aquisição da produção de produtor rural pessoa física ou segurado especial em geral por Entidade do PAA - Produção Isenta (Lei 13.606/2018); 6 - Aquisição da produção de produtor rural pessoa jurídica por Entidade do PAA - Produção Isenta (Lei 13.606/2018)  Valores Válidos: 1, 2, 3, 4, 5, 6. | - Se filial não inscrita no PAA e fornecedor origem/destino (TMOV.CODCFONATUREZA ou TMOV.CODCFO) for pessoa física (FCFO.PESSOAFISOPUJUR = F) e produtor rural (FCFO.RAMOATIV = 16) Então 1 - Se filial inscrita no PAA e fornecedor origem/destino (TMOV.CODCFONATUREZA ou TMOV.CODCFO) for pessoa física (FCFO.PESSOAFISOPUJUR = F) e produtor rural (FCFO.RAMOATIV = 16) Então 2 - Se filial inscrita no PAA e fornecedor (TMOV.CODCFO) for pessoa jurídica (FCFO.PESSOAFISOPUJUR = J) e produtor rural (FCFO.RAMOATIV = 16) Então 3  - Se filial não inscrita no PAA e fornecedor origem/destino (TMOV.CODCFONATUREZA) for pessoa física (FCFO.PESSOAFISOPUJUR = F) e produtor rural (FCFO.RAMOATIV = 16) e Produção Insenta (TPRODUTODEF.PRDISENTOFUNRURAL = 1) Então 4  - Se filial inscrita no PAA e fornecedor origem/destino (TMOV.CODCFONATUREZA) for pessoa física (FCFO.PESSOAFISOPUJUR = F) e produtor rural (FCFO.RAMOATIV = 16) e Produção Insenta (TPRODUTODEF.PRDISENTOFUNRURAL = 1) Então 5  - Se filial inscrita no PAA e fornecedor (TMOV.CODCFO) for pessoa jurídica (FCFO.PESSOAFISOPUJUR = J) e produtor rural (FCFO.RAMOATIV = 16) e Produção Insenta (TPRODUTODEF.PRDISENTOFUNRURAL = 1) Então 6  **Obs.:** 1. A indicação de filial inscrita no PAA será implementada pela equipe do TOTVS Gestão Fiscal. Issue FISCAL01-1606. | Deve ser gerada para cada indicativo de aquisição. |
| 1.2 | vlrTotAquis | N | 14,2 | 1-1 | O | Valor total da aquisição correspondente ao indicativo informado em {indAquis}. Validação: Deve corresponder a soma de {vlrBruto} dos registros vinculados. | Somatório do valor bruto (TITMMOV.VALORBRUTOITEM) de cada nota correspondente ao indicativo informado no campo indAquis. |  |
| 1.3 | ideProdutor |  |  | 1-9999 | O | Registro que identifica os produtores rurais dos quais foi efetuada aquisição da produção pelo contribuinte declarante. |  | Para cada Indicativo de Aquisição, deve ser gerado um registro para cada produtor rural do qual foi adquirido produção. |
| 1.3.1 | tpInscProd | N | 1 | 1-1 | O | Informar [1] (CNPJ) ou [2] (CPF). Validação: Se {indAquis} for igual a [1, 2], deve ser igual a [2]. Se {indAquis} for igual a [3], deve ser igual a [1]. Valores Válidos: 1, 2. | Se o campo indAquis = 1 ou 2 Então 2 Se o campo indAquis = 3 Então 1 |  |
| 1.3.2 | nrInscProd | C | 14 | 1-1 | O | Número de inscrição do produtor no CPF ou no CNPJ, de acordo com o definido no campo {tpInscProd}. Validação: Deve ser um CPF ou CNPJ válido, de acordo com o {tpInscProd}. Deve ser diferente da inscrição do declarante. | FCFO.CGCCFO ou FCFOCOMPL.CPFCOMPLEMENTAR (Se Produtor Rural e Pessoa Física com CNPJ cadastrado no campo FCFO.CGCCFO) | A partir da release 12.1.25 será considerado:  FCFO.CGCCFO ou PESOCIALCLIFOR.CPF(Se Produtor Rural e Pessoa Física com CNPJ cadastrado no campo FCFO.CGCCFO) |
| 1.3.3 | vlrBruto | N | 14,2 | 1-1 | O | Preencher com o valor bruto da aquisição da produção rural. Validação: Deve ser maior que zero. | Somatório do valor bruto (TITMMOV.VALORBRUTOITEM) das NF-es correspondentes ao fornecedor indicado no campo nrInscProd. |  |
| 1.3.4 | vrCPDescPR | N | 14,2 | 1-1 | O | Preencher com o valor da Contribuição Previdenciária descontada pelo adquirente de produção de produtor rural - sub-rogação. Se não houver valor a ser informado, preencher com 0 (zero). | Somatório do valor (TTRBMOV.VALOR) do imposto FUNRural (Imposto informado em TTRBMOV.CODTRB cujo **Tipo do Tributo** (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e **Tipo de Recolhimento** (DTRIBUTO.TIPORECOLHIMENTO) seja "FUNRural") das NF-es correspondentes ao fornecedor indicado no campo nrInscProd.  Caso não tenha valor, informar 0. |  |
| 1.3.5 | vrRatDescPR | N | 14,2 | 1-1 | O | Valor da contribuição destinada ao financiamento dos benefícios concedidos em razão do grau de incidência da incapacidade laborativa decorrente dos riscos ambientais do trabalho, incidente sobre a aquisição de produção rural de produtor rural. Se não houver informação, preencher com 0 (zero). | Somatório do valor (TTRBMOV.VALOR) do imposto GILRAT (Imposto informado em TTRBMOV.CODTRB cujo **Tipo do Tributo** (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e **Tipo de Recolhimento** (DTRIBUTO.TIPORECOLHIMENTO) seja "GILRAT") das NF-es correspondentes ao fornecedor indicado no campo nrInscProd.  Caso não tenha valor, informar 0. |  |
| 1.3.6 | vrSenarDesc | N | 14,2 | 1-1 | O | Valor da contribuição destinada ao SENAR, incidente sobre a aquisição de produção rural de produtor rural pessoa física/segurado especial. Se não houver valor a ser informado, preencher com 0 (zero). | Somatório do valor (TTRBMOV.VALOR) do imposto SENAR (Imposto informado em TTRBMOV.CODTRB cujo **Tipo do Tributo** (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e **Tipo de Recolhimento** (DTRIBUTO.TIPORECOLHIMENTO) seja "SENAR") das NF-es correspondentes ao fornecedor indicado no campo nrInscProd.  Caso não tenha valor, informar 0. |  |
| 1.3.7 | nfs |  |  | 0-9999 | O | Detalhamento das notas fiscais relativas a aquisição de produção do produtor rural identificado no registro superior, não sendo obrigatório nas aquisições de produção de pessoa física/segurado especial. |  | Para cada produtor rural pessoa jurídica informado em ideProdutor, deve ser gerado um registro para cada NF-e |
| 1.3.7.1 | serie | C | 5 | 0-1 | O | Informar o número de série da nota fiscal/fatura. | TMOV.SERIE |  |
| 1.3.7.2 | nrDocto | C | 20 | 1-1 | O | Número da Nota Fiscal/Fatura. | TMOV.NUMEROMOV |  |
| 1.3.7.3 | dtEmisNF | D |  | 1-1 | O | Data de Emissão da Nota Fiscal/Fatura. Validação: O mês/ano da emissão da nota fiscal deve ser igual ao mês/ano indicado no registro de abertura do arquivo. | TMOV.DATAEMISSAO |  |
| 1.3.7.4 | vlrBruto | N | 14,2 | 1-1 | O | Preencher com o valor bruto da(s) nota(s) fiscal(is) | TITMMOV.VALORBRUTOITEM |  |
| 1.3.7.5 | vrCPDescPR | N | 14,2 | 1-1 | O | Preencher com o valor da Contribuição Previdenciária descontada pelo adquirente de produção de produtor rural - sub-rogação. Se não houver informação, preencher com 0 (zero). | Valor (TTRBMOV.VALOR) do imposto FUNRural (Imposto informado em TTRBMOV.CODTRB cujo **Tipo do Tributo** (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e **Tipo de Recolhimento** (DTRIBUTO.TIPORECOLHIMENTO) seja "FUNRural") das NF-e indicada.  Caso não tenha valor, informar 0. |  |
| 1.3.7.6 | vrRatDescPR | N | 14,2 | 1-1 | O | Valor da contribuição destinada ao financiamento dos benefícios concedidos em razão do grau de incidência da incapacidade laborativa decorrente dos riscos ambientais do trabalho, incidente sobre a aquisição de produção rural de produtor rural. Se não houver informação, preencher com 0 (zero). | Valor (TTRBMOV.VALOR) do imposto GILRAT (Imposto informado em TTRBMOV.CODTRB cujo **Tipo do Tributo** (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e **Tipo de Recolhimento** (DTRIBUTO.TIPORECOLHIMENTO) seja "GILRAT") das NF-e indicada.  Caso não tenha valor, informar 0. |  |
| 1.3.7.7 | vrSenarDesc | N | 14,2 | 1-1 | O | Valor da contribuição destinada ao SENAR, incidente sobre a aquisição de produção rural de produtor rural pessoa física/segurado especial. Se não houver informação, preencher com 0 (zero). | Valor (TTRBMOV.VALOR) do imposto SENAR (Imposto informado em TTRBMOV.CODTRB cujo **Tipo do Tributo** (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e **Tipo de Recolhimento** (DTRIBUTO.TIPORECOLHIMENTO) seja "SENAR") das NF-e indicada.  Caso não tenha valor, informar 0. |  |
| 1.3.8 | infoProcJud |  |  | 0-10 | OC | Registro preenchido quando o Produtor Rural (pessoa física ou segurado especial), identificado em {ideProdutor}, ou o próprio declarante, possuir processo judicial com decisão/sentença determinando a não retenção, pelo adquirente, das contribuições incidentes sobre a aquisição de produção. |  | Para cada produtor rural informado em ideProdutor, deve ser gerado um registro para cada processo judicial informado.  Caso não haja processo judicial, não gerar o grupo. |
| 1.3.8.1 | nrProcJud | C | 20 | 1-1 | OC | Informar um número de processo judicial cadastrado através do evento S-1070, cujo {indMatProc} seja igual a [1]. Validação: O processo deve existir na tabela de processos (S-1070). | DPROCESSOJUDICIAL.NUMERO referente ao IDPROCESSOREFERENCIADO da DLAFMOVPROCESSOJUD para o IDMOV das NF-es do Produtor Rural |  |
| 1.3.8.2 | codSusp | N | 14 | 1-1 | OC | Código do Indicativo da Suspensão, atribuído pelo empregador em S-1070. Validação: A informação prestada deve estar de acordo com o que foi informado em S-1070. | DPROCESSOJUDICIAL.NATUREZAJUDICIAL referente ao IDPROCESSOREFERENCIADO da DLAFMOVPROCESSOJUD para o IDMOV das NF-es do Produtor Rural |  |
| 1.3.8.3 | vrCPNRet | N | 14,2 | 1-1 | OC | Valor da Contribuição Previdenciária que deixou de ser retida pelo declarante em decorrência de decisão/sentença judicial. | Somatório do **Valor Ret. Suspensa Judicialmente** do imposto FUNRural (Imposto informado em TTRBMOV.CODTRB cujo **Tipo do Tributo** (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e **Tipo de Recolhimento** (DTRIBUTO.TIPORECOLHIMENTO) seja "FUNRural") das NF-es correspondentes ao fornecedor indicado no campo nrInscProd. |  |
| 1.3.8.4 | vrRatNRet | N | 14,2 | 1-1 | OC | Valor da GILRAT, incidente sobre a aquisição de produção rural de produtor rural, cuja retenção deixou de ser efetuada em decorrência de decisão/sentença judicial. | Somatório do **Valor Ret. Suspensa Judicialmente** do imposto GILRAT (Imposto informado em TTRBMOV.CODTRB cujo **Tipo do Tributo** (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e **Tipo de Recolhimento** (DTRIBUTO.TIPORECOLHIMENTO) seja "GILRAT") das NF-es correspondentes ao fornecedor indicado no campo nrInscProd. |  |
| 1.3.8.5 | vrSenarNRet | N | 14,2 | 1-1 | OC | Valor da contribuição destinada ao SENAR, incidente sobre a aquisição de produção rural de produtor rural pessoa física/segurado especial, e que deixou de ser retida em decorrência de decisão/sentença judicial. | Somatório do **Valor Ret. Suspensa Judicialmente** do imposto SENAR (Imposto informado em TTRBMOV.CODTRB cujo **Tipo do Tributo** (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e **Tipo de Recolhimento** (DTRIBUTO.TIPORECOLHIMENTO) seja "SENAR") das NF-es correspondentes ao fornecedor indicado no campo nrInscProd. |  |

Legenda:

O - Obrigatório  
OC - Obrigatório se existir a informação  
F - Facultativo  
N - Não apresentar informação

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [ACAA040 – Parâmetros] | [Alteração] | [Atualizações -> Acadêmico-> Tesouraria] | - |

**Tabelas Utilizadas**

* TMOV - Movimento
* TTRBMOV - Tributos do Movimento/Item de movimento
* FCFO - Cliente/Fornecedor
* GFILIAL - Filial
* FTDO - Tipo de Documento
* PESOCIALCLIFOR - Relacionamento do eSocial com Cliente/Fornecedor (a partir do release 12.1.25)

## Dicionário de Dados

|  |  |
| --- | --- |
| **Campo** | AQUISICAOPAA |
| **Tipo** | DLOGICONULL |
| **Tamanho** | 2 |
| **Valor Inicial** | NULL |
| **Mandatório** | Sim (  ) Não (  ) |
| **Descrição** | Indicativo de aquisição de produtor rural no âmbito do PAA |
| **Título** | Aquisição PAA |
| **Picture** | NA |
| **Help de Campo** | Indicar se o item de movimento é referente a um produto de produtor rural adquirido no âmbito do PAA (Programa de Aquisição de Alimentos). |

|  |  |
| --- | --- |
| **Campo** | VALORRETSUSPJUDIC |
| **Tipo** | RMDVALOR4 |
| **Tamanho** | 9, 4 |
| **Valor Inicial** | NULL |
| **Mandatório** | Sim (  ) Não (  ) |
| **Descrição** | Valor de Retenção Suspensa Judicialmente |
| **Título** | Valor Ret. Suspensa Judicialmente |
| **Picture** | NA |
| **Help de Campo** | Informar o valor do imposto que não foi retido devido decisão/ordem judicial de processo. |

**Consulta alterada com a informação de indicador de aquisição:**

SELECT  TMOV.CODCOLIGADA, TMOV.CODFILIAL, TMOV.IDMOV, TITMMOV.VALORBRUTOITEM VALORBRUTO,

                TMOV.DATAEMISSAO, TMOV.NUMEROMOV, TMOV.SERIE, TMOV.CODCFO,

                FCFO\_CFO.PESSOAFISOUJUR FPESSOAFISOUJUR, FCFO\_CFO.RAMOATIV FRAMOATIV, FCFO\_CFO.CGCCFO FCGCCFO,

                TMOV.CODCFONATUREZA,

                FCFO\_NAT.PESSOAFISOUJUR JPESSOAFISOUJUR, FCFO\_NAT.RAMOATIV JRAMOATIV, FCFO\_NAT.CGCCFO JCGCCFO,

                TITMMOV.NSEQITMMOV, TPRODUTODEF.PRDISENTOFUNRURAL,

                CASE

                                  WHEN (DFILIAL.FILIALPAA <> 1 OR DFILIAL.FILIALPAA IS NULL)  AND FCFO\_NAT.PESSOAFISOUJUR = 'F' AND FCFO\_NAT.RAMOATIV = 16 AND TPRODUTODEF.PRDISENTOFUNRURAL <> 1THEN 1

                                  WHEN DFILIAL.FILIALPAA = 1 AND FCFO\_NAT.PESSOAFISOUJUR = 'F' AND FCFO\_NAT.RAMOATIV = 16 AND TPRODUTODEF.PRDISENTOFUNRURAL <> 1 THEN 2

                                  WHEN DFILIAL.FILIALPAA = 1 AND FCFO\_CFO.PESSOAFISOUJUR = 'J' AND FCFO\_CFO.RAMOATIV = 16 AND TPRODUTODEF.PRDISENTOFUNRURAL <> 1 THEN 3

                                  WHEN (DFILIAL.FILIALPAA <> 1 OR DFILIAL.FILIALPAA IS NULL) AND FCFO\_NAT.PESSOAFISOUJUR = 'F' AND FCFO\_NAT.RAMOATIV = 16 AND TPRODUTODEF.PRDISENTOFUNRURAL = 1 THEN 4

                                  WHEN DFILIAL.FILIALPAA = 1 AND FCFO\_NAT.PESSOAFISOUJUR = 'F' AND FCFO\_NAT.RAMOATIV = 16 AND TPRODUTODEF.PRDISENTOFUNRURAL = 1 THEN 5

                                  WHEN DFILIAL.FILIALPAA = 1 AND FCFO\_CFO.PESSOAFISOUJUR = 'J' AND FCFO\_CFO.RAMOATIV = 16 AND TPRODUTODEF.PRDISENTOFUNRURAL = 1 THEN 6

                                  END INDAQUISICAO

          FROM

                TMOV (NOLOCK)

                JOIN TITMMOV (NOLOCK)

                  ON TITMMOV.CODCOLIGADA = TMOV.CODCOLIGADA AND

                     TITMMOV.IDMOV = TMOV.IDMOV

                JOIN TPRODUTODEF (NOLOCK)

                  ON TPRODUTODEF.CODCOLIGADA = TITMMOV.CODCOLIGADA AND

                     TPRODUTODEF.IDPRD = TITMMOV.IDPRD

                JOIN FTDO (NOLOCK)

                  ON FTDO.CODCOLIGADA = TMOV.CODCOLIGADA AND

                      FTDO.CODTDO = TMOV.CODTDO

                LEFT JOIN FCFO FCFO\_CFO (NOLOCK)

                  ON FCFO\_CFO.CODCOLIGADA = TMOV.CODCOLCFO AND

                      FCFO\_CFO.CODCFO = TMOV.CODCFO AND

                      FCFO\_CFO.RAMOATIV = 16 AND

                      FCFO\_CFO.CGCCFO IS NOT NULL

                LEFT JOIN FCFO FCFO\_NAT (NOLOCK)

                  ON FCFO\_NAT.CODCOLIGADA = TMOV.CODCOLCFONATUREZA AND

                      FCFO\_NAT.CODCFO = TMOV.CODCFONATUREZA AND

                      FCFO\_NAT.RAMOATIV = 16 AND

                      FCFO\_NAT.CGCCFO IS NOT NULL

                LEFT JOIN DFILIAL

                             ON DFILIAL.CODCOLIGADA = TMOV.CODCOLIGADA AND

                                   DFILIAL.CODFILIAL = TMOV.CODFILIAL

                    WHERE TMOV.CODCOLIGADA = :CODCOLIGADA AND

                TMOV.CODFILIAL = :CODFILIAL AND

                TMOV.CODTMV LIKE '1.2%'  AND

                TMOV.DATAEMISSAO >= :DATAEMISSAO\_INI AND

                TMOV.DATAEMISSAO <= :DATAEMISSAO\_FIM AND

                FTDO.CODMODDOC = :CODMODDOC AND

TMOV.STATUS<> 'C' AND

                ((FCFO\_NAT.RAMOATIV IS NOT NULL) OR (FCFO\_CFO.RAMOATIV IS NOT NULL))

**INFORMAR OS PARÂMETROS:**

CODCOLIGADA;

CODFILIAL;

CODMODDOC: 55, 04 ou 1B

DATAEMISSAO: Data Emissão do Movimento

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
