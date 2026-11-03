---
content_hash: 37fb1d00473a91f92f9e727a3570a479dd2b6444cfd3cbedfc2a5f31cd0e3acb
fetched_at: '2026-06-29T00:08:56.454193+00:00'
page_id: '351376543'
product: rm
source: tdn-rm
title: Evento S-1280
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-1280
version: 5
---

Leiautestrue1Leiaute 2.5.00

Mapeamento dos campos para o leiaute 2.5.00

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro eSocial** | **Campo eSocial** | **Tabela RM** | **Coluna RM** | **Informações do calculo** |
| ideEvento | indRetif |  |  | Conforme manual |
| ideEvento | nrRecibo |  | PROTOCOLO |  |
| ideEvento | indApuracao |  | INDAPURACAO |  |
| ideEvento | perApur |  |  |  |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| infoSubstPatr | indSubstPatr | PESOCIALFOLHAMENSAL | INDSUBSPATRONAL |  |
| infoSubstPatr | percRedContrib | PESOCIALFOLHAMENSAL | PERCALIQPATRONAL |  |
| infoAtivConcom | fatorMes | PESOCIALFOLHAMENSAL | FATORMES |  |
| infoAtivConcom | fator13 | PESOCIALFOLHAMENSAL | FATOR13 |  |

true1Leiaute S-1.0

Mapeamento dos campos para o leiaute S-1.0

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro eSocial** | **Campo eSocial** | **Tabela RM** | **Coluna RM** | **Informações do calculo** |
| ideEvento | indRetif |  |  | Conforme manual |
| ideEvento | nrRecibo |  | PROTOCOLO |  |
| ideEvento | indApuracao |  | INDAPURACAO |  |
| ideEvento | perApur |  |  | Informação recuperada através dos campos 'MESCOMP e ANOCOMP' da Tabela PESOCIALFOLHAMENSAL |
| ideEvento | indGuia |  |  | Campo gerado com valor fixo '1' apenas para empregador com natuzera jurídica 402-2 - Segurado Especial |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| infoSubstPatr | indSubstPatr | PESOCIALFOLHAMENSAL | INDSUBSPATRONAL |  |
| infoSubstPatr | percRedContrib | PESOCIALFOLHAMENSAL | PERCALIQPATRONAL |  |
| infoAtivConcom | fatorMes | PESOCIALFOLHAMENSAL | FATORMES |  |
| infoAtivConcom | fator13 | PESOCIALFOLHAMENSAL | FATOR13 |  |
| infoPercTransf11096 | percTransf | PESOCIALFOLHAMENSAL | PERCENTCONTRIBSOCIEDADEFIMLUCR |  |
