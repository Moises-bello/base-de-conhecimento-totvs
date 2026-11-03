---
content_hash: 4e5223b598298e7805b33a4aeeb13fa5381470980263af2ecd3d75dfdf5bf658
fetched_at: '2026-06-29T00:10:18.361355+00:00'
page_id: '479829367'
product: rm
source: tdn-rm
title: Evento S-1260
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-1260
version: 5
---

Leiautestrue2Leiaute 2.5.00Leiaute 2.5.00

Mapeamento dos campos para o leiaute 2.5.00

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro**  **eSocial** | **Campo**  **eSocial** | **Tabela RM** | **Coluna RM** | **Informações do calculo** |
| ideEvento | indRetif |  |  | Conforme manual |
| ideEvento | nrRecibo |  | PROTOCOLO |  |
| ideEvento | indApuracao |  | INDAPURACAO |  |
| ideEvento | perApur |  |  | Informação recuperada através dos campos 'MESCOMP e ANOCOMP' da Tabela PESOCIALFOLHAMENSAL |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| ideEstabel | nrInscEstabRural |  |  | Caso PSECAO.CAEPF |
| tpComerc | indComerc |  |  | - Se a nota foi emitida a consumidor final (TMOVFISCAL.OPERACAOCONSUMIDORFINAL = 1) ou o cliente da nota for produto rural pessoa física (FCFO.PESSOAFISOPUJUR = F) e (FCFO.RAMOATIV = 16)  Então retorna 2  - Se o cliente da nota for pessoa jurídica não inscrita no PAA (FCFO.PESSOAFISOPUJUR = J) e (FCFO.ENTIDADEEXECUTORAPAA = 0) ou o cliente da nota for pessoa física (FCFO.PESSOAFISOPUJUR = F) e (FCFO.RAMOATIV <> 16)  Então retorna 3  - Se o item do movimento for um produto isento de tributação FUNRURAL (TPRODUTODEF.PRDISENTOFUNRURAL = 1)  Então retorna 7  - Se o cliente da nota for pessoa jurídica inscrita no PAA (FCFO.PESSOAFISOPUJUR = J) e (FCFO.ENTIDADEEXECUTORAPAA = 1)  Então retorna 8  - Se a nota for de exportação (DCFOP.CODNAT = 7.xx)  Então retorna 9 |
| tpComerc | vrTotCom |  |  | Somatório do valor bruto (TITMMOV.VALORBRUTOITEM) de cada nota correspondente ao indicativo informado no campo indComerc.  Se indComerc for igual a [3, 7], deve corresponder a soma do campo vrComerc dos registros vinculados. |
| ideAdquir | tpInsc |  |  | Se o campo indComerc = 3 ou 7 e o cliente for pessoa jurídica (FCFO.PESSOAFISOPUJUR = J)  Então retorna 1   Se o campo indComerc = 3 ou 7 e o cliente for pessoa física (FCFO.PESSOAFISOPUJUR = F)  Então retorna 2  Se o campo indComerc = 8  Então retorna 1 |
| ideAdquir | nrInsc |  |  | FCFO.CGCCFO ou FCFOCOMPL.CPFCOMPLEMENTAR (Se Produtor Rural e Pessoa Física com CNPJ cadastrado no campo FCFO.CGCCFO) |
| ideAdquir | vrComerc |  |  | Somatório do valor bruto (TITMMOV.VALORBRUTOITEM) das notas correspondentes ao cliente indicado no campo nrInscProd. |
| nfs | serie |  |  | TMOV.SERIE |
| nfs | nrDocto |  |  | TMOV.NUMEROMOV |
| nfs | dtEmisNF |  |  | TMOV.DATAEMISSAO |
| nfs | vlrBruto |  |  | TMOV.VALORBRUTO |
| nfs | vrCPDescPR |  |  | Somatório do valor (TTRBMOV.VALOR) do imposto FUNRural (Imposto informado em TTRBMOV.CODTRB cujo Tipo do Tributo (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e Tipo de Recolhimento (TTRBMOV.TIPORECOLHIMENTO) seja "FUNRural") das NF-es correspondentes ao fornecedor indicado no campo nrInscProd.    Caso não tenha valor, informar 0. |
| nfs | vrRatDescPR |  |  | Somatório do valor (TTRBMOV.VALOR) do imposto GILRAT (Imposto informado em TTRBMOV.CODTRB cujo Tipo do Tributo (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e Tipo de Recolhimento (TTRBMOV.TIPORECOLHIMENTO) seja "GILRAT") das NF-es correspondentes ao fornecedor indicado no campo nrInscProd.    Caso não tenha valor, informar 0. |
| nfs | vrSenarDesc |  |  | Somatório do valor (TTRBMOV.VALOR) do imposto SENAR (Imposto informado em TTRBMOV.CODTRB cujo Tipo do Tributo (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e Tipo de Recolhimento (TTRBMOV.TIPORECOLHIMENTO) seja "SENAR") das NF-es correspondentes ao fornecedor indicado no campo nrInscProd.    Caso não tenha valor, informar 0. |
| infoProcJud | tpProc |  |  | DPROCESSOJUDICIAL.TIPOPROCESSO referente ao IDPROCESSOREFERENCIADO da DLAFMOVPROCESSOJUD para o IDMOV das notas do cliente. |
| infoProcJud | nrProcJud |  |  | DPROCESSOJUDICIAL.NATUREZAJUDICIAL referente ao IDPROCESSOREFERENCIADO da DLAFMOVPROCESSOJUD para o IDMOV das NF-es do Produtor Rural |
| infoProcJud | codSusp |  | CodSusp |  |
| infoProcJud | vrCPNRet |  |  | Somatório do Valor Ret. Suspensa Judicialmente do imposto FUNRural (Imposto informado em TTRBMOV.CODTRB cujo Tipo do Tributo (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e Tipo de Recolhimento (TTRBMOV.TIPORECOLHIMENTO) seja "FUNRural") das NF-es correspondentes ao fornecedor indicado no campo nrInscProd. |
| infoProcJud | vrRatNRet |  |  | Somatório do Valor Ret. Suspensa Judicialmente do imposto GILRAT (Imposto informado em TTRBMOV.CODTRB cujo Tipo do Tributo (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e Tipo de Recolhimento (TTRBMOV.TIPORECOLHIMENTO) seja "GILRAT") das NF-es correspondentes ao fornecedor indicado no campo nrInscProd. |
| infoProcJud | vrSenarNRet |  |  | Somatório do Valor Ret. Suspensa Judicialmente do imposto SENAR (Imposto informado em TTRBMOV.CODTRB cujo Tipo do Tributo (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e Tipo de Recolhimento (TTRBMOV.TIPORECOLHIMENTO) seja "SENAR") das NF-es correspondentes ao fornecedor indicado no campo nrInscProd. |

true2Leiaute S-1.0Leiaute S-1.0

Mapeamento dos campos para o leiaute S-1.0

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro**  **eSocial** | **Campo**  **eSocial** | **Tabela RM** | **Coluna RM** | **Informações do calculo** |
| ideEvento | indRetif |  |  | Conforme manual |
| ideEvento | nrRecibo |  | PROTOCOLO |  |
| ideEvento | perApur |  |  | Informação recuperada através dos campos 'MESCOMP e ANOCOMP' da Tabela PESOCIALFOLHAMENSAL |
| ideEvento | indGuia |  |  | Campo gerado com valor fixo '1' apenas para empregador com natuzera jurídica 402-2 - Segurado Especial |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| ideEstabel | nrInscEstabRural |  |  | Caso PSECAO.CAEPF |
| tpComerc | indComerc |  |  | - Se a nota foi emitida a consumidor final (TMOVFISCAL.OPERACAOCONSUMIDORFINAL = 1) ou o cliente da nota for produto rural pessoa física (FCFO.PESSOAFISOPUJUR = F) e (FCFO.RAMOATIV = 16)  Então retorna 2  - Se o cliente da nota for pessoa jurídica não inscrita no PAA (FCFO.PESSOAFISOPUJUR = J) e (FCFO.ENTIDADEEXECUTORAPAA = 0) ou o cliente da nota for pessoa física (FCFO.PESSOAFISOPUJUR = F) e (FCFO.RAMOATIV <> 16)  Então retorna 3  - Se o item do movimento for um produto isento de tributação FUNRURAL (TPRODUTODEF.PRDISENTOFUNRURAL = 1)  Então retorna 7  - Se o cliente da nota for pessoa jurídica inscrita no PAA (FCFO.PESSOAFISOPUJUR = J) e (FCFO.ENTIDADEEXECUTORAPAA = 1)  Então retorna 8  - Se a nota for de exportação (DCFOP.CODNAT = 7.xx)  Então retorna 9 |
| tpComerc | vrTotCom |  |  | Somatório do valor bruto (TITMMOV.VALORBRUTOITEM) de cada nota correspondente ao indicativo informado no campo indComerc.  Se indComerc for igual a [3, 7], deve corresponder a soma do campo vrComerc dos registros vinculados. |
| ideAdquir | tpInsc |  |  | Se o campo indComerc = 3 ou 7 e o cliente for pessoa jurídica (FCFO.PESSOAFISOPUJUR = J)  Então retorna 1   Se o campo indComerc = 3 ou 7 e o cliente for pessoa física (FCFO.PESSOAFISOPUJUR = F)  Então retorna 2  Se o campo indComerc = 8  Então retorna 1 |
| ideAdquir | nrInsc |  |  | FCFO.CGCCFO ou FCFOCOMPL.CPFCOMPLEMENTAR (Se Produtor Rural e Pessoa Física com CNPJ cadastrado no campo FCFO.CGCCFO) |
| ideAdquir | vrComerc |  |  | Somatório do valor bruto (TITMMOV.VALORBRUTOITEM) das notas correspondentes ao cliente indicado no campo nrInscProd. |
| nfs | serie |  |  | TMOV.SERIE |
| nfs | nrDocto |  |  | TMOV.NUMEROMOV |
| nfs | dtEmisNF |  |  | TMOV.DATAEMISSAO |
| nfs | vlrBruto |  |  | TMOV.VALORBRUTO |
| nfs | vrCPDescPR |  |  | Somatório do valor (TTRBMOV.VALOR) do imposto FUNRural (Imposto informado em TTRBMOV.CODTRB cujo Tipo do Tributo (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e Tipo de Recolhimento (TTRBMOV.TIPORECOLHIMENTO) seja "FUNRural") das NF-es correspondentes ao fornecedor indicado no campo nrInscProd.    Caso não tenha valor, informar 0. |
| nfs | vrRatDescPR |  |  | Somatório do valor (TTRBMOV.VALOR) do imposto GILRAT (Imposto informado em TTRBMOV.CODTRB cujo Tipo do Tributo (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e Tipo de Recolhimento (TTRBMOV.TIPORECOLHIMENTO) seja "GILRAT") das NF-es correspondentes ao fornecedor indicado no campo nrInscProd.    Caso não tenha valor, informar 0. |
| nfs | vrSenarDesc |  |  | Somatório do valor (TTRBMOV.VALOR) do imposto SENAR (Imposto informado em TTRBMOV.CODTRB cujo Tipo do Tributo (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e Tipo de Recolhimento (TTRBMOV.TIPORECOLHIMENTO) seja "SENAR") das NF-es correspondentes ao fornecedor indicado no campo nrInscProd.    Caso não tenha valor, informar 0. |
| infoProcJud | tpProc |  |  | DPROCESSOJUDICIAL.TIPOPROCESSO referente ao IDPROCESSOREFERENCIADO da DLAFMOVPROCESSOJUD para o IDMOV das notas do cliente. |
| infoProcJud | nrProc |  |  | DPROCESSOJUDICIAL.NATUREZAJUDICIAL referente ao IDPROCESSOREFERENCIADO da DLAFMOVPROCESSOJUD para o IDMOV das NF-es do Produtor Rural |
| infoProcJud | codSusp |  | CodSusp |  |
| infoProcJud | vrCPSusp |  |  | Somatório do Valor Ret. Suspensa Judicialmente do imposto FUNRural (Imposto informado em TTRBMOV.CODTRB cujo Tipo do Tributo (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e Tipo de Recolhimento (TTRBMOV.TIPORECOLHIMENTO) seja "FUNRural") das NF-es correspondentes ao fornecedor indicado no campo nrInscProd. |
| infoProcJud | vrRatSusp |  |  | Somatório do Valor Ret. Suspensa Judicialmente do imposto GILRAT (Imposto informado em TTRBMOV.CODTRB cujo Tipo do Tributo (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e Tipo de Recolhimento (TTRBMOV.TIPORECOLHIMENTO) seja "GILRAT") das NF-es correspondentes ao fornecedor indicado no campo nrInscProd. |
| infoProcJud | vrSenarSusp |  |  | Somatório do Valor Ret. Suspensa Judicialmente do imposto SENAR (Imposto informado em TTRBMOV.CODTRB cujo Tipo do Tributo (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e Tipo de Recolhimento (TTRBMOV.TIPORECOLHIMENTO) seja "SENAR") das NF-es correspondentes ao fornecedor indicado no campo nrInscProd. |
