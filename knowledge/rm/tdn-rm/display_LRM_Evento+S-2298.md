---
content_hash: 4e52558ab2c73d7f9d1a049215c50c1140eb29b6aed677617d9f68148f055aa2
fetched_at: '2026-06-29T00:08:56.259959+00:00'
page_id: '351376341'
product: rm
source: tdn-rm
title: Evento S-2298
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-2298
version: 6
---

Leiautestrue1Leiaute 2.5.00

Mapeamento dos campos para o leiaute 2.5.00

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro eSocial** | **Campo eSocial** | **Tabela RM** | **Coluna RM** | **Informações do calculo** |
| ideEvento | indRetif |  |  | Conforme manual |
| ideEvento | nrRecibo |  | PROTOCOLO |  |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| ideVinculo | cpfTrab | PPESSOA | CPF |  |
| ideVinculo | nisTrab |  |  | Caso seja autônomo e FCFO.NIT estiver preenchido, retorna FCFO.NIT, caso contrário, retorna FCFO.CIAUTONOMO;  Caso não seja autônomo e codCateg diferente de contribuinte individual (721, 722, 723, 731, 734, 738, 761, 771) retorna PFUNC.PISPASEP, caso contrario, retorna PFUNC.CI |
| ideVinculo | matricula | PFUNC | MATRICULAESOCIAL |  |
| infoReintegr | tpReint | PFUNC | TIPOREINTEGRACAO |  |
| infoReintegr | nrProcJud | PFUNC | NROPROCESSOJUDICIAL |  |
| infoReintegr | nrLeiAnistia | PFUNC | NROLEIANISTIA |  |
| infoReintegr | dtEfetRetorno | PFUNC | DATARETORNOEFETIVO |  |
| infoReintegr | dtEfeito | PFUNC | DATAREINTEGRACAO |  |
| infoReintegr | indPagtoJuizo | PFUNC | INDPAGTOJUIZO |  |

true1Leiaute S-1.0Mapeamento dos campos para o leiaute S-1.0

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro\_eSocial** | **Campo\_eSocial** | **Tabela\_RM** | **Coluna\_RM** | **Informações\_do\_calculo** |
| ideEvento | indRetif |  |  | Conforme manual |
| ideEvento | nrRecibo |  | PROTOCOLO |  |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| ideVinculo | cpfTrab | PPESSOA | CPF |  |
| ideVinculo | matricula | PFUNC | MATRICULAESOCIAL |  |
| infoReintegr | tpReint | PFUNC | TIPOREINTEGRACAO |  |
| infoReintegr | nrProcJud | PFUNC | NROPROCESSOJUDICIAL |  |
| infoReintegr | nrLeiAnistia | PFUNC | NROLEIANISTIA |  |
| infoReintegr | dtEfetRetorno | PFUNC | DATARETORNOEFETIVO |  |
| infoReintegr | dtEfeito | PFUNC | DATAREINTEGRACAO |  |
