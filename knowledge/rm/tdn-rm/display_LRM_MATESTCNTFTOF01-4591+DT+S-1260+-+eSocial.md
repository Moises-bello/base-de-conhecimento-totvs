---
content_hash: 33a84a15c4c39744f656d765ab6502a81eb3d76ffb4073230e901c4780b6eeda
fetched_at: '2026-06-29T00:10:14.481750+00:00'
page_id: '461907395'
product: rm
source: tdn-rm
title: MATESTCNTFTOF01-4591 DT S-1260 - eSocial
type: documentation
url: https://tdn.totvs.com/display/LRM/MATESTCNTFTOF01-4591+DT+S-1260+-+eSocial
version: 10
---

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | Movimento |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | MATESTCNTFTOF01-4591 | **IRM/EPIC1** | MATESTCNTFTOF01-4655 |
| **Requisito/Story/Issue1** | MATESTCNTFTOF01-4591 | **Subtarefa1** | NA |
| **Chamado/Ticket2** | NA | | |
| **País** | ( x ) Brasil | | |
| **Outros** | NA | | |

## 

## Objetivo

Criação de um serviço de geração de arquivo .xml para uso do TOTVS Gestão de Folha de Pagamento, que retornará dados necessários para a geração da rotina eSocial, mais especificamente o registro S-1260 - Comercialização da Produção Rural Pessoa Física

Esse é um documento complementar a documentação do bloco S-1250 quem vêem acrescentar informações para o bloco S-1260.

Documento S-1250: 

## Descrição

Implementação da possibilidade de vinculo de Movimentos de Exportação, em outros movimentos de Exportação para geração de Remessa Parcelada de Exportação.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação de um dos pacote de atualizações abaixo:

* 12.1.24 ou superiores.

## Procedimento para Utilização

Caso seja necessário a geração de Notas de Remessa Parcelada de Exportação, o vinculo dessa nota com a Nota de Exportação deve ser realizado também pela pela tela de **Relac. Mov. Exportação.**

**Após selecionado o Movimento será feito o filtro de acordo com combinação de parâmetros para a formação do indicador de comercialização descritos em Informações no Sistema no quadro abaixo.****Serão apresentados no eSocial apenas os movimentos que se enquadrarem em um dos indicadores de Comercialização:**

**Parâmetros da sentença:**

{cpfComplementar} : {Se existir na base trocar por: FCFOCOMPL.CPFCOMPLEMENTAR}

:CODCOLIGADA : {Código da coligada que vai buscar os dados para S-1260}

:CODFILIAL: {Código da filial que vai buscar os dados para S-1260}

{tipoMov} : "2.2%"

{listaTipoDoc}: ' 04', '55', '1B'

**Sentença que retorna os dados a serem processador para o bloco S-1260. Observe que apenas os registros que atendem a regra do “ideAdquir = {3,7,8} são reportados:**

SELECT  TMOV.CODCOLIGADA, TMOV.CODFILIAL, TMOV.IDMOV, TITMMOV.VALORBRUTOITEM VALORBRUTO,

                TMOV.DATAEMISSAO, TMOV.NUMEROMOV, TMOV.SERIE, TMOV.CODCFO, TMOV.CODCFONATUREZA,

                FCFO\_CFO.PESSOAFISOUJUR FPESSOAFISOUJUR, FCFO\_CFO.RAMOATIV FRAMOATIV, FCFO\_CFO.CGCCFO FCGCCFO,

                FCFO\_CFO.PESSOAFISOUJUR FPESSOAFISOUJUR, FCFO\_CFO.ENTIDADEEXECUTORAPAA FENTIDADEEXECUTORAPAA,

                TITMMOV.NSEQITMMOV, TPRODUTODEF.PRDISENTOFUNRURAL, TMOVFISCAL.OPERACAOCONSUMIDORFINAL,

                DCFOP.CODNAT {cpfComplementar}

  FROM

                TMOV (NOLOCK)

                LEFT JOIN TMOVFISCAL (NOLOCK)

                   ON TMOVFISCAL.CODCOLIGADA = TMOV.CODCOLIGADA AND

                          TMOVFISCAL.IDMOV = TMOV.IDMOV

                LEFT JOIN DCFOP (NOLOCK)

                   ON DCFOP.CODCOLIGADA = TMOV.CODCOLIGADA AND

                          DCFOP.IDNAT = TMOV.IDNAT

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

                         FCFO\_CFO.CGCCFO IS NOT NULL

                LEFT JOIN FCFOCOMPL (NOLOCK)

                   ON FCFOCOMPL.CODCOLIGADA = FCFO\_CFO.CODCOLIGADA AND

                          FCFOCOMPL.CODCFO = FCFO\_CFO.CODCFO

WHERE TMOV.CODCOLIGADA = :CODCOLIGADA AND

                TMOV.CODFILIAL = :CODFILIAL AND

                TMOV.CODTMV LIKE {tipoMov}  AND

                TMOV.DATAEMISSAO >= :DATAEMISSAO\_INI AND

                TMOV.DATAEMISSAO <= :DATAEMISSAO\_FIM AND

                TMOV.STATUS <> 'C' AND

                FTDO.CODMODDOC IN ({listaTipoDoc}) AND

                DCFOP.CODNAT NOT LIKE '2.921%' AND DCFOP.CODNAT NOT LIKE '2.949%'     (**O movimento com natureza de Operação do tipo "2.921%" e "2.949%", na comercialização de produtos deve ser ignorada**)

**A partir do release 12.1.25 a consulta a ser utilizada será:**

SELECT  TMOV.CODCOLIGADA, TMOV.CODFILIAL, TMOV.IDMOV, TITMMOV.VALORBRUTOITEM VALORBRUTO,

                TMOV.DATAEMISSAO, TMOV.NUMEROMOV, TMOV.SERIE, TMOV.CODCFO, TMOV.CODCFONATUREZA,

                FCFO\_CFO.PESSOAFISOUJUR FPESSOAFISOUJUR, FCFO\_CFO.RAMOATIV FRAMOATIV, FCFO\_CFO.CGCCFO FCGCCFO,

                FCFO\_CFO.PESSOAFISOUJUR FPESSOAFISOUJUR, FCFO\_CFO.ENTIDADEEXECUTORAPAA FENTIDADEEXECUTORAPAA,

                TITMMOV.NSEQITMMOV, TPRODUTODEF.PRDISENTOFUNRURAL, TMOVFISCAL.OPERACAOCONSUMIDORFINAL,

                DCFOP.CODNAT,  PESOCIALCLIFOR.CPF

  FROM

                TMOV (NOLOCK)

                LEFT JOIN TMOVFISCAL (NOLOCK)

                   ON TMOVFISCAL.CODCOLIGADA = TMOV.CODCOLIGADA AND

                          TMOVFISCAL.IDMOV = TMOV.IDMOV

                LEFT JOIN DCFOP (NOLOCK)

                   ON DCFOP.CODCOLIGADA = TMOV.CODCOLIGADA AND

                          DCFOP.IDNAT = TMOV.IDNAT

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

                         FCFO\_CFO.CGCCFO IS NOT NULL

                LEFT JOIN PESOCIALCLIFOR (NOLOCK)

                   ON PESOCIALCLIFOR.CODCOLIGADA = FCFO\_CFO.CODCOLIGADA AND

                          PESOCIALCLIFOR.CODCFO = FCFO\_CFO.CODCFO

WHERE TMOV.CODCOLIGADA = :CODCOLIGADA AND

                TMOV.CODFILIAL = :CODFILIAL AND

                TMOV.CODTMV LIKE {tipoMov}  AND

                TMOV.DATAEMISSAO >= :DATAEMISSAO\_INI AND

                TMOV.DATAEMISSAO <= :DATAEMISSAO\_FIM AND

                TMOV.STATUS <> 'C' AND

                FTDO.CODMODDOC IN ({listaTipoDoc})

**Obs.**: Os esquemas XSD podem ser verificados no site do eSocial (<http://portal.esocial.gov.br/institucional/documentacao-tecnica>). Utilizar versão 2.5.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Nível** | **Campo** | **Tipo** | **Tamanho** | **Ocorrência** | **Obrig.** | **Descrição** | **Informação no Sistema** | **Observações** |
| 1 | tpComerc |  |  | 1-5 | O | Registro que apresenta o valor total da comercialização por tipo de comercialização |  |  |
| 1.1 | indComerc | N | 1 | 1-1 | O | Registro que apresenta o valor total da comercialização por tipo de comercialização | Indicativo de Comercialização: 2 - Comercialização da Produção efetuada diretamente no varejo a consumidor final ou a outro produtor rural pessoa física por Produtor Rural Pessoa Física, inclusive por Segurado Especial ou por Pessoa Física não produtor rural; 3 - Comercialização da Produção por Prod. Rural PF/Seg. Especial - Vendas a PJ (exceto Entidade inscrita no Programa de Aquisição de Alimentos - PAA) ou a Intermediário PF; 7 - Comercialização da Produção Isenta de acordo com a Lei n° 13.606/2018; 8 - Comercialização da Produção da Pessoa Física/Segurado Especial para Entidade inscrita no Programa de Aquisição de Alimentos - PAA; 9 - Comercialização da Produção no Mercado Externo. Valores Válidos: 2, 3, 7, 8, 9. | - Se a nota foi emitida a consumidor final (TMOVFISCAL.OPERACAOCONSUMIDORFINAL = 1) ou o cliente da nota for produto rural pessoa física (FCFO.PESSOAFISOPUJUR = F) e (FCFO.RAMOATIV = 16)  Então 2 - Se o cliente da nota for pessoa jurídica não inscrita no PAA (FCFO.PESSOAFISOPUJUR = J) e (FCFO.ENTIDADEEXECUTORAPAA = 0) ou o cliente da nota for pessoa física (FCFO.PESSOAFISOPUJUR = F) e (FCFO.RAMOATIV <> 16)  Então 3  - Se o item do movimento for um produto isento de tributação FUNRURAL (TPRODUTODEF.PRDISENTOFUNRURAL = 1)  Então 7  - Se o cliente da nota for pessoa jurídica inscrita no PAA (FCFO.PESSOAFISOPUJUR = J) e (FCFO.ENTIDADEEXECUTORAPAA = 1)  Então 8  - Se a nota for de exportação (DCFOP.CODNAT = 7.xx)  Então 9    Ordem -> 7,9,3,8,2 e demais | Deve ser gerada para cada indicativo de aquisição. |
| 1.2 | vrTotCom | N | 14,2 | 1-1 | O | Preencher com o valor total da comercialização. Validação: Deve ser maior que zero. Se {indComerc} for igual a [3, 7], deve corresponder a soma do campo {vrComerc} dos registros vinculados. | Somatório do valor bruto (TITMMOV.VALORBRUTOITEM) de cada nota correspondente ao indicativo informado no campo indComerc. Se indComerc for igual a [3, 7], deve corresponder a soma do campo vrComerc dos registros vinculados. |  |
| 1.3 | ideAdquir |  |  | 0-9999 | O (se indComerc = (3,7,8) | Identificação dos Adquirentes da Produção. |  | Para cada Indicativo de Comercialização, deve ser gerado um registro para cada cliente da nota. |
| 1.3.1 | tpInsc | N | 1 | 1-1 | O | Preencher com o código correspondente ao tipo de inscrição, conforme tabela 5. Validação: Se {indComerc} for igual a [3, 7], deve ser igual a [1,2]. Se {indComerc} for igual a [8], deve ser igual a [1]. | Se o campo indComerc = 3 ou 7 e o cliente for pessoa jurídica (FCFO.PESSOAFISOPUJUR = J)  Então 1  Se o campo indComerc = 3 ou 7 e o cliente for pessoa física (FCFO.PESSOAFISOPUJUR = F)  Então 2  Se o campo indComerc = 8  Então 1 |  |
| 1.3.2 | nrInsc | C | 15 | 1-1 | O | Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição indicado no campo {tpInsc}. Validação: A inscrição informada deve ser compatível com o {tpInsc} e diferente da inscrição do declarante. | FCFO.CGCCFO ou FCFOCOMPL.CPFCOMPLEMENTAR (Se Produtor Rural e Pessoa Física com CNPJ cadastrado no campo FCFO.CGCCFO) | A partir do release 12.1.25 considerar  FCFO.CGCCFO ou PESOCIALCLIFOR.CPF |
| 1.3.3 | vrComerc | N | 14,2 | 1-1 | O | Valor bruto da comercialização da produção. Validação: Deve ser maior que zero. | Somatório do valor bruto (TITMMOV.VALORBRUTOITEM) das notas correspondentes ao cliente indicado no campo nrInscProd. |  |
| 1.4 | nfs |  |  | 0-999 | F |  | Detalhamento das notas fiscais relativas à comercialização de produção com o adquirente identificado no registro superior. | Para cada cliente informado em ideAdquir, deve ser gerado um registro para cada NF-e |
| 1.4.1 | serie | C | 5 | 0-1 | NO | Informar o número de série da nota fiscal/fatura. | TMOV.SERIE |  |
| 1.4.2 | nrDocto | C | 20 | 1-1 | O | Número da Nota Fiscal/Fatura. | TMOV.NUMEROMOV |  |
| 1.4.3 | dtEmisNF | D |  | 1-1 | O | Data de Emissão da Nota Fiscal/Fatura. Validação: O mês/ano da emissão da nota fiscal deve ser igual ao mês/ano indicado no registro de abertura do arquivo. | TMOV.DATAEMISSAO |  |
| 1.4.4 | vlrBruto | N | 14,2 | 1-1 | O | Preencher com o valor bruto da(s) nota(s) fiscal(is). | TITMMOV.VALORBRUTOITEM |  |
| 1.4.5 | vrCPDescPR | N | 14,2 | 1-1 | O | Preencher com o valor da Contribuição Previdenciária descontada pelo adquirente na comercialização de produção. Se não houver informação, preencher com 0 (zero). | Valor (TTRBMOV.VALOR) do imposto FUNRural (Imposto informado em TTRBMOV.CODTRB cujo Tipo do Tributo (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e Tipo de Recolhimento (DTRIBUTO.TIPORECOLHIMENTO) seja "FUNRural") das notas indicadas.  Caso não tenha valor, informar 0. |  |
| 1.4.6 | vrRatDescPR | N | 14,2 | 1-1 | O | Valor da contribuição destinada ao financiamento dos benefícios concedidos em razão do grau de incidência da incapacidade laborativa decorrente dos riscos ambientais do trabalho, incidente sobre a comercialização de produção rural de produtor rural. Se não houver informação, preencher com 0 (zero). | Valor (TTRBMOV.VALOR) do imposto GILRAT (Imposto informado em TTRBMOV.CODTRB cujo Tipo do Tributo (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e Tipo de Recolhimento (DTRIBUTO.TIPORECOLHIMENTO) seja "GILRAT") das notas indicadas.  Caso não tenha valor, informar 0. |  |
| 1.4.7 | vrSenarDesc | N | 14,2 | 1-1 | O | Valor da contribuição destinada ao SENAR, incidente sobre a comercialização de produção rural de produtor rural pessoa física/segurado especial. Se não houver informação, preencher com 0 (zero). | Valor (TTRBMOV.VALOR) do imposto SENAR (Imposto informado em TTRBMOV.CODTRB cujo Tipo do Tributo (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e Tipo de Recolhimento (DTRIBUTO.TIPORECOLHIMENTO) seja "SENAR") das notas indicadas.  Caso não tenha valor, informar 0. |  |
| 1.5 | infoProcJud |  |  | 0-10 | OC | Informações de Processos Judiciais com decisão/sentença favorável ao contribuinte e relativos à contribuição incidente sobre a comercialização. |  | Para cada cliente informado em ideProdutor, deve ser gerado um registro para cada processo judicial informado.  Caso não haja processo judicial, não gerar o grupo. |
| 1.5.1 | tpProc | N | 1 | 1-1 | O | Preencher com o código correspondente ao tipo de processo: 1 - Administrativo; 2 - Judicial. Valores Válidos: 1, 2. | DPROCESSOJUDICIAL.TIPOPROCESSO referente ao IDPROCESSOREFERENCIADO da DLAFMOVPROCESSOJUD para o IDMOV das notas do cliente. |  |
| 1.5.2 | nrProc | C | 21 | 1-1 | O | Informar um número de processo cadastrado através do evento S-1070, cujo {indMatProc} seja igual a [1]. Validação: Deve ser um número de processo administrativo ou judicial válido e existente na Tabela de Processos (S-1070). | DPROCESSOJUDICIAL.NUMERO referente ao IDPROCESSOREFERENCIADO da DLAFMOVPROCESSOJUD para o IDMOV das notas do cliente. |  |
| 1.5.3 | codSusp | N | 14 | 1-1 | O | Código do Indicativo da Suspensão, atribuído pelo empregador em S-1070. Validação: A informação prestada deve estar de acordo com o que foi informado em S-1070. | DPROCESSOJUDICIAL.NATUREZAJUDICIAL referente ao IDPROCESSOREFERENCIADO da DLAFMOVPROCESSOJUD para o IDMOV das notas do cliente. |  |
| 1.5.4 | vrCPSusp | N | 14,2 | 0-1 | NO | Valor da Contribuição Previdenciária com exigibilidade suspensa. Validação: Preenchimento obrigatório se {vrRatSusp} e {vrSenarSusp} não tiverem sido preenchidos. Deve ser um valor maior que zero. | Somatório do Valor Ret. Suspensa Judicialmente do imposto FUNRural (Imposto informado em TTRBMOV.CODTRB cujo Tipo do Tributo (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e Tipo de Recolhimento (DTRIBUTO.TIPORECOLHIMENTO) seja "FUNRural") das notas correspondentes ao cliente indicado no campo nrInsc. |  |
| 1.5.5 | vrRatSusp | N | 14,2 | 0-1 | NO | Valor da contribuição para Gilrat com exigibilidade suspensa. Validação: Preenchimento obrigatório se {vrCPSusp} e {vrSenarSusp} não tiverem sido preenchidos. Deve ser um valor maior que zero. | Somatório do Valor Ret. Suspensa Judicialmente do imposto GILRAT (Imposto informado em TTRBMOV.CODTRB cujo Tipo do Tributo (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e Tipo de Recolhimento (DTRIBUTO.TIPORECOLHIMENTO) seja "GILRAT") das notas correspondentes ao cliente indicado no campo nrInsc. |  |
| 1.5.6 | vrSenarSusp | N | 14,2 | 0-1 | NO | Valor da contribuição para o Senar com exigibilidade suspensa. Validação: Preenchimento obrigatório se {vrCPSusp} e {vrRatSusp} não tiverem sido preenchidos. Deve ser um valor maior que zero. | Somatório do Valor Ret. Suspensa Judicialmente do imposto SENAR (Imposto informado em TTRBMOV.CODTRB cujo Tipo do Tributo (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e Tipo de Recolhimento (DTRIBUTO.TIPORECOLHIMENTO) seja "SENAR") das notas correspondentes ao cliente indicado no campo nrInsc. |  |

DT - S-1260 - Novo recurso - Possibilidade de desconsiderar a comercialização do indicador igual a 3
