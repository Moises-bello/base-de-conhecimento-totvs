---
content_hash: 0479a4a2c868dfcf07ef07294dd1799ccdef73aedecd8b1a566c36e09d8e6250
fetched_at: '2026-06-29T00:08:56.477605+00:00'
page_id: '351376554'
product: rm
source: tdn-rm
title: Evento S-1300
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-1300
version: 3
---

Leiautestrue1Leiaute 2.5.00

Mapeamento dos campos para o leiaute 2.5.00

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro eSocial** | **Campo eSocial** | **Tabela RM** | **Coluna RM** | **Informações do calculo** |
| ideEvento | indApuracao |  | INDAPURACAO |  |
| ideEvento | perApur |  |  | Informação recuperada através dos campos 'MESCOMP e ANOCOMP' da Tabela PESOCIALFOLHAMENSAL |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| contribSind | cnpjSindic |  |  | Informação recuperada através dos campos "CNPJCONTRASSIST, CNPJCONTRASSOC, CNPJCONTRCONF e  CNPJCONTRSINDIC" na tabela PRAISPARSEC |
| contribSind | tpContribSind |  |  | Caso PRAISPARSEC.VALORCONTRSINIC maior que ZERO retorna "1";  Caso PRAISPARSEC.VALORCONTRASSOC maior que ZERO retorna "2";  Caso PRAISPARSEC.VALORCONTRASSIST maior que ZERO retorna "3";  Caso PRAISPARSEC.VALORCONTRCONF maior que ZERO retorna "4"; |
| contribSind | vlrContribSind |  |  | Informação recuperada através dos campos "VALORCONTRASSIST, VALORCONTRASSOC,  VALORCONTRCONF e  VALORCONTRSINIC" na tabela PRAISPARSEC |
