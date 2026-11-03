---
content_hash: 14fc41b97b8eefc2ffe433369e4d1833a131f88e1c4e93d4ae76b27bf8a28ed4
fetched_at: '2026-06-29T00:12:16.622074+00:00'
page_id: '994626361'
product: rm
source: tdn-rm
title: Informações do CTe Outros Serviços
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=994626361
version: 1
---

# ide - Identificação do CT-e

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **ide** | **[infCte](https://tdn.totvs.com/pages/viewpage.action?pageId=981000770)** | **1-1** | **Grupo** | **Identificação do CT-e** |
| cUF | ide | 1-1 | Elemento | GFILIAL.ESTADO  Estado da Filial Emitente |
| cCT | ide | 1-1 | Elemento | TMOV.CODCOLIGADA + TMOV.IDMOV   DetalhescCTRegra Concatena TMOV.CODCOLIGADA + TMOV.IDMOV resultando em um numero aleatório (num)  **Se** num **>** 8 caracteres  {   pos = tamanho do num - 8;   num = num.Remove(pos, pos);  }  cCT = 100000000-num Exemplo Exemplo:  Idmov = 111111111  Coligada = 20  num = 20111111111 (20+ 111111111) pos = (11-8) num = 201**111**11111 a partir da posição 3 remove 3 números cCT = 79888889 (100000000-20111111) |
| CFOP | ide | 1-1 | Elemento | Código da CFOP que foi selecionada no Movimento |
| natOp | ide | 1-1 | Elemento | Descrição da CFOP que foi selecionada no Movimento |
| mod | ide | 1-1 | Elemento | Código do modelo de Documento informado no Movimento (CT-eOS: 67) |
| serie | ide | 1-1 | Elemento | TMOV.SERIE  Serie do Movimento |
| nCT | ide | 1-1 | Elemento | TMOV.NUMEROMOV  Número do Movimento |
| dhEmi | ide | 1-1 | Elemento | TMOV.HORARIOEMISSAO  **Se** o campo HORARIOEMISSAO não esteja preenchido, será o TMOV.DATAEMISSAO |
| tpImp | ide | 1-1 | Elemento | TTMVEXT.FORMATODACTE  Formato preenchido nos parâmetros do CT-e no Tipo de Movimento |
| tpEmis | ide | 1-1 | Elemento | TPARFILIAL.MODALIDADECTE   * 1 - Normal; 4-EPEC pela SVC; * 5 - Contingência FSDA; * 7 - Autorização pela SVC-RS; * 8 - Autorização pela SVC-SP |
| cDV | ide | 1-1 | Elemento | Digito verificador da chave de acesso |
| tpAmb | ide | 1-1 | Elemento | TPARFILIAL.AMBIENTECTE  Definido nos parâmetros do CT-e |
| tpCTe | ide | 1-1 | Elemento | TMOVTRANSP.TIPOCTE  Definido no Movimento |
| procEmi | ide | 1-1 | Elemento | 0 - Valor fixo |
| verProc | ide | 1-1 | Elemento | será gerado com a versão do RM |
| cMunEnv | ide | 1-1 | Elemento | Será gerado conforme a classificação IBGE do município da Filial Emitente |
| xMunEnv | ide | 1-1 | Elemento | Será gerado com a descrição do município da Filial Emitente |
| UFEnv | ide | 1-1 | Elemento | Estado da Filial emitente |
| modal | ide | 1-1 | Elemento | TTMVEXT.MODAL  Definido nos parâmetros do Tipo de Movimento |
| tpServ | ide | 1-1 | Elemento | TMOVTRANSP.TIPOSERVICOCTE  Definido no Movimento |
| cMunIni | ide | 1-1 | Elemento | Caso exista o grupo LocColeta esse campo é igual ao locColeta.cMun. Caso não exista, esse campo é igual a enderReme.cMun |
| xMunIni | ide | 1-1 | Elemento | Caso exista o grupo LocColeta esse campo é igual ao locColeta.xMun. Caso não exista, esse campo é igual a enderReme.xMun |
| UFIni | ide | 1-1 | Elemento | Caso exista o grupo LocColeta esse campo é igual ao locColeta.UF. Caso não exista, esse campo é igual a enderReme.UF |
| cMunFim | ide | 1-1 | Elemento | Caso exista o grupo LocEnt esse campo é igual ao locEnt.cMun. Caso não exista, esse campo é igual a enderDest.cMun |
| xMunFim | ide | 1-1 | Elemento | Caso exista o grupo locEnt esse campo é igual ao locEnt.xMun. Caso não exista, esse campo é igual a enderDest.xMun |
| UFFim | ide | 1-1 | Elemento | Caso exista o grupo locEnt esse campo é igual ao locEnt.UF. Caso não exista, esse campo é igual a enderDest.UF |
| indIEToma | ide | 1-1 | Elemento | Será gerado conforme o cadastro do Cliente/Fornecedor campo Contribuinte do ICMS.  1 – Contribuinte ICMS; 2 – Contribuinte isento de inscrição; 9 – Não Contribuinte |
| **toma3** | **ide** | **1-1** | **Grupo de Escolha** |  |
| **toma4** | **ide** | **1-1** | **Grupo de Escolha** |  |
