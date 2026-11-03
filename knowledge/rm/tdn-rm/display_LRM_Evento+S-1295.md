---
content_hash: 7c066ff9715f371e6c205034940d73153827d388fc64847d5c0d4da22932388b
fetched_at: '2026-06-29T00:08:56.459349+00:00'
page_id: '351376548'
product: rm
source: tdn-rm
title: Evento S-1295
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-1295
version: 3
---

Leiautestrue1Leiaute 2.5.00

Mapeamento dos campos para o leiaute 2.5.00

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro eSocial** | **Campo eSocial** | **Tabela RM** | **Coluna RM** | **Informações do calculo** |
| ideEvento | indRetif |  |  | Conforme manual |
| ideEvento | nrRecibo |  | PROTOCOLO |  |
| ideEvento | indApuracao |  | INDAPURACAO |  |
| ideEvento | perApur |  |  | Informação recuperada através dos campos 'MESCOMP e ANOCOMP' da Tabela PESOCIALFOLHAMENSAL |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| ideRespInf | nmResp | PESOCIALFOLHAMENSAL | NOMECONTATO |  |
| ideRespInf | cpfResp | PESOCIALFOLHAMENSAL | CPFCONTATO |  |
| ideRespInf | telefone | PESOCIALFOLHAMENSAL | TELEFONECONTATO |  |
| ideRespInf | email | PESOCIALFOLHAMENSAL | EMAILCONTATO |  |
