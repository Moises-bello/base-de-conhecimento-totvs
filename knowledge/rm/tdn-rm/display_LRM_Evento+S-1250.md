---
content_hash: d55598242e378fe25593c984296992fb08524119fdba42ccad9a19858e26162b
fetched_at: '2026-06-29T00:08:58.783646+00:00'
page_id: '361440302'
product: rm
source: tdn-rm
title: Evento S-1250
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-1250
version: 12
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
| ideEstabAdquir | tpInscAdq |  |  | [1] (CNPJ) ou [3] (CAEPF) |
| ideEstabAdquir | nrInscAdq |  |  | Caso PSECAO.PESSOAFISICA seja Pessoa Física retorna PSECAO.CAEPF, senão retorna PSECAO.CGC |
| tpAquis | indAquis |  |  | Se filial não inscrita no PAA e fornecedor origem/destino (TMOV.CODCFONATUREZA ou TMOV.CODCFO) for pessoa física (FCFO.PESSOAFISOPUJUR = F) e produtor rural (FCFO.RAMOATIV = 16)  Então 1  Se filial inscrita no PAA e fornecedor origem/destino (TMOV.CODCFONATUREZA ou TMOV.CODCFO) for pessoa física (FCFO.PESSOAFISOPUJUR = F) e produtor rural (FCFO.RAMOATIV = 16)  Então 2  Se filial inscrita no PAA e fornecedor (TMOV.CODCFO) for pessoa jurídica (FCFO.PESSOAFISOPUJUR = J) e produtor rural (FCFO.RAMOATIV = 16)  Então 3  Se filial não inscrita no PAA e fornecedor origem/destino (TMOV.CODCFONATUREZA) for pessoa física (FCFO.PESSOAFISOPUJUR = F) e produtor rural (FCFO.RAMOATIV = 16) e Produção Insenta (TPRODUTODEF.PRDISENTOFUNRURAL = 1)  Então 4  Se filial inscrita no PAA e fornecedor origem/destino (TMOV.CODCFONATUREZA) for pessoa física (FCFO.PESSOAFISOPUJUR = F) e produtor rural (FCFO.RAMOATIV = 16) e Produção Insenta (TPRODUTODEF.PRDISENTOFUNRURAL = 1)  Então 5  Se filial inscrita no PAA e fornecedor (TMOV.CODCFO) for pessoa jurídica (FCFO.PESSOAFISOPUJUR = J) e produtor rural (FCFO.RAMOATIV = 16) e Produção Insenta (TPRODUTODEF.PRDISENTOFUNRURAL = 1) |
| tpAquis | vlrTotAquis |  |  | Somatório do valor bruto (TMOV.VALORBRUTO) de cada nota correspondente ao indicativo informado no campo indAquis. |
| ideProdutor | tpInscProd |  |  | Se o campo indAquis = 1 ou 2 retorna 2  Se o campo indAquis = 3 retorna 1 |
| ideProdutor | nrInscProd |  |  | FCFO.CGCCFO ou FCFOCOMPL.CPFCOMPLEMENTAR (Se Produtor Rural e Pessoa Física com CNPJ cadastrado no campo FCFO.CGCCFO)    A partir da release 12.1.25 será considerado: FCFO.CGCCFO ou PESOCIALCLIFOR.CPF (Se Produtor Rural e Pessoa Física com CNPJ cadastrado no campo FCFO.CGCCFO) |
| ideProdutor | vlrBruto |  |  | Somatório do valor bruto (TMOV.VALORBRUTO) das NF-es correspondentes ao fornecedor indicado no campo nrInscProd. |
| ideProdutor | vrCPDescPR |  |  | Somatório do valor (TTRBMOV.VALOR) do imposto FUNRural (Imposto informado em TTRBMOV.CODTRB cujo Tipo do Tributo (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e Tipo de Recolhimento (TTRBMOV.TIPORECOLHIMENTO) seja "FUNRural") das NF-es correspondentes ao fornecedor indicado no campo nrInscProd.    Caso não tenha valor, informar 0. |
| ideProdutor | vrRatDescPR |  |  | Somatório do valor (TTRBMOV.VALOR) do imposto GILRAT (Imposto informado em TTRBMOV.CODTRB cujo Tipo do Tributo (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e Tipo de Recolhimento (TTRBMOV.TIPORECOLHIMENTO) seja "GILRAT") das NF-es correspondentes ao fornecedor indicado no campo nrInscProd.    Caso não tenha valor, informar 0. |
| ideProdutor | vrSenarDesc |  |  | Somatório do valor (TTRBMOV.VALOR) do imposto SENAR (Imposto informado em TTRBMOV.CODTRB cujo Tipo do Tributo (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e Tipo de Recolhimento (TTRBMOV.TIPORECOLHIMENTO) seja "SENAR") das NF-es correspondentes ao fornecedor indicado no campo nrInscProd.    Caso não tenha valor, informar 0. |
| ideProdutor | indOpcCP |  | IndOpcCP |  |
| nfs | serie |  |  | TMOV.SERIE |
| nfs | nrDocto |  |  | TMOV.NUMEROMOV |
| nfs | dtEmisNF |  |  | TMOV.DATAEMISSAO |
| nfs | vlrBruto |  |  | TMOV.VALORBRUTO |
| nfs | vrCPDescPR |  |  | Somatório do valor (TTRBMOV.VALOR) do imposto FUNRural (Imposto informado em TTRBMOV.CODTRB cujo Tipo do Tributo (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e Tipo de Recolhimento (TTRBMOV.TIPORECOLHIMENTO) seja "FUNRural") das NF-es correspondentes ao fornecedor indicado no campo nrInscProd.    Caso não tenha valor, informar 0. |
| nfs | vrRatDescPR |  |  | Somatório do valor (TTRBMOV.VALOR) do imposto GILRAT (Imposto informado em TTRBMOV.CODTRB cujo Tipo do Tributo (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e Tipo de Recolhimento (TTRBMOV.TIPORECOLHIMENTO) seja "GILRAT") das NF-es correspondentes ao fornecedor indicado no campo nrInscProd.    Caso não tenha valor, informar 0. |
| nfs | vrSenarDesc |  |  | Somatório do valor (TTRBMOV.VALOR) do imposto SENAR (Imposto informado em TTRBMOV.CODTRB cujo Tipo do Tributo (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e Tipo de Recolhimento (TTRBMOV.TIPORECOLHIMENTO) seja "SENAR") das NF-es correspondentes ao fornecedor indicado no campo nrInscProd.    Caso não tenha valor, informar 0. |
| infoProcJud | nrProcJud |  |  | DPROCESSOJUDICIAL.NATUREZAJUDICIAL referente ao IDPROCESSOREFERENCIADO da DLAFMOVPROCESSOJUD para o IDMOV das NF-es do Produtor Rural |
| infoProcJud | codSusp |  | CodSusp |  |
| infoProcJud | vrCPNRet |  |  | Somatório do Valor Ret. Suspensa Judicialmente do imposto FUNRural (Imposto informado em TTRBMOV.CODTRB cujo Tipo do Tributo (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e Tipo de Recolhimento (TTRBMOV.TIPORECOLHIMENTO) seja "FUNRural") das NF-es correspondentes ao fornecedor indicado no campo nrInscProd. |
| infoProcJud | vrRatNRet |  |  | Somatório do Valor Ret. Suspensa Judicialmente do imposto GILRAT (Imposto informado em TTRBMOV.CODTRB cujo Tipo do Tributo (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e Tipo de Recolhimento (TTRBMOV.TIPORECOLHIMENTO) seja "GILRAT") das NF-es correspondentes ao fornecedor indicado no campo nrInscProd. |
| infoProcJud | vrSenarNRet |  |  | Somatório do Valor Ret. Suspensa Judicialmente do imposto SENAR (Imposto informado em TTRBMOV.CODTRB cujo Tipo do Tributo (DTRIBUTO.TIPOTRIBFISC) seja "FUNRural" e Tipo de Recolhimento (TTRBMOV.TIPORECOLHIMENTO) seja "SENAR") das NF-es correspondentes ao fornecedor indicado no campo nrInscProd. |
