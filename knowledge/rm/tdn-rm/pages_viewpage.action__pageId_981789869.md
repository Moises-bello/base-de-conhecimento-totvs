---
content_hash: 491afc83902776563cf9fddb55fbab8a316ee7015c6207910bf07a0ba8060f0d
fetched_at: '2026-06-29T00:12:15.759543+00:00'
page_id: '981789869'
product: rm
source: tdn-rm
title: Informações do ICMS de partilha com a UF - CT-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=981789869
version: 2
---

# ICMSUFFim - Informações do ICMS de partilha com a UF de término do serviço de transporte na operação interestadual

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **ICMSUFFim** | **[imp](https://tdn.totvs.com/pages/viewpage.action?pageId=981002580)** | **0-1** | **Grupo de Escolha** | **Grupo é gerado nas seguintes condições, considerando informações do Movimento:** **- Código Natureza inicia com 6** **- Operação Consumidor Final = 1** **- Natureza Fiscal for do tipo Saída (DCFOP.TIPOMOVIMENTO = S)** **- Operação Interestadual (DCFOP.ORIGEMDESTINO = F)** |
| vBCUFFim | ICMSUFFim | 1-1 | Elemento | TTRBMOV.BASEDECALCULO |
| pFCPUFFim | ICMSUFFim | 1-1 | Elemento | DREGRAICMS.PERICMSFCP |
| pICMSUFFim | ICMSUFFim | 1-1 | Elemento | DREGRAICMS.ALIQSUBST  Alíquota interna da UF de término da prestação de serviço, conforme preenchido no campo 'Alíquota S.T./Interna D.A. (%)' (DREGRAICMS.ALIQSUBST) da Regra de ICMS vinculada à natureza fiscal utilizada; |
| pICMSInter | ICMSUFFim | 1-1 | Elemento | DREGRAICMS.ALIQICMS  Alíquota interestadual das UF envolvidas na prestação de serviço, conforme preenchido no campo 'Alíquota ICMS (%)' (DREGRAICMS.ALIQICMS) da Regra de ICMS vinculada à natureza fiscal utilizada; |
| vFCPUFFim | ICMSUFFim | 1-1 | Elemento | vBCUFFim \* pFCPUFFim % |
| vICMSUFFim | ICMSUFFim | 1-1 | Elemento | **Se** DREGRAICMS.PERICMSESTDESTINO> 0   ( (vBCUFFim \* pICMSUFFim %) - (vBCUFFim \* pICMSInter %)) \* PERICMSESTDESTINO % |
| vICMSUFIni | ICMSUFFim | 1-1 | Elemento | **Se** vICMSUFFim > 0   ( (vBCUFFim \* pICMSUFFim %) - (vBCUFFim \* pICMSInter %)) - vICMSUFFim |
