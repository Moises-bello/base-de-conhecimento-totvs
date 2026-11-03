---
content_hash: ead9e8aba15a5f7bac4102989d43563311337e20e70e1352aed3f341a39f02b5
fetched_at: '2026-06-29T00:12:15.225378+00:00'
page_id: '973048625'
product: rm
source: tdn-rm
title: Grupo UB - Informações dos tributos IBS / CBS e Imposto Seletivo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=973048625
version: 26
---

| Grupo UB - Informações dos tributos IBS / CBS e Imposto Seletivo | | | | | |
| --- | --- | --- | --- | --- | --- |
|  | **Campo** | **Ele** | **Pai** | **Ocorrência** | **Campo de Origem** |
| **UB01** | **IS** | **G** | **M01** | **0-1** | **Não será gerado em 2026** |
| UB02 | CSTIS | E | UB01 | 1-1 |  |
| UB03 | cClassTribIS | E | UB01 | 1-1 |  |
| **UB04** | **-x-** | **G** | **UB01** | **0-1** | **Não será gerado em 2026** |
| UB05 | vBCIS | E | UB04 | 1-1 |  |
| UB06 | pIS | E | UB04 | 1-1 |  |
| UB07 | pISEspec | E | UB04 | 0-1 |  |
| **UB08** | **-x-** | **G** | **UB04** | **0-1** | **Não será gerado em 2026** |
| UB09 | uTrib | E | UB08 | 1-1 |  |
| UB10 | qTrib | E | UB08 | 1-1 |  |
| UB11 | vIS | E | UB04 | 1-1 |  |
| **UB12** | **IBSCBS** | **G** | **M01** | **0-1** | Será gerado caso possua tributo IBS ou CBS e se algum deles possuir um dos campos preenchidos: Situação Tributária (CST) ou Classif. Tributária. |
| UB13 | CST | E | UB12 | 1-1 | TTRBMOV.SITUACAOTRIBUTARIA |
| UB14 | cClassTrib | E | UB12 | 1-1 | TTRBMOV.CLASSTRIB |
| **UB14k** | **-x-** | **G** | **UB12** | **0-1** |  |
| **UB15** | **gIBSCBS** | **CG** | **UB14k** |  | Será gerado de acordo com a [tabela de CSTs](https://dfe-portal.svrs.rs.gov.br/Cff/ClassificacaoTributaria), seguindo o índice **IndIBSCBS**. Para que essa tabela seja importada no TOTVS Gestão Fiscal e seus valores sejam utilizados na geração dos grupos da NF-e, veja . |
| UB16 | vBC | E | UB15 | 1-1 | TTRBMOV.BASEDECALCULO |
| **UB17** | **gIBSUF** | **G** | **UB15** | **1-1** |  |
| UB18 | pIBSUF | E | UB17 | 1-1 | TTRBMOV.ALIQUOTACHEIA  Quando for gerado o grupo ***gTribRegular*** (Tributação Regular), a tag ***<pIBSUF>*** será **zerada**. |
| **UB21** | **gDif** | **G** | **UB17** | **0-1** | Será gerado de acordo com a [tabela de CSTs](https://dfe-portal.svrs.rs.gov.br/Cff/ClassificacaoTributaria), seguindo o índice **IndDif**. Para que essa tabela seja importada no TOTVS Gestão Fiscal e seus valores sejam utilizados na geração dos grupos da NF-e, veja . |
| UB22 | pDif | E | UB21 | 1-1 | TTRBMOV.PCTDIFERIMENTO |
| UB23 | vDif | E | UB21 | 1-1 | TTRBMOV.TRIBUTODIFERIDO |
| **UB24** | **gDevTrib** | **G** | **UB17** | **0-1** |  |
| UB25 | vDevTrib | E | UB24 | 1-1 |  |
| **UB26** | **gRed** | **G** | **UB17** | **0-1** |  |
| UB27 | pRedAliq | E | UB26 | 1-1 | TTRBMOV.PCTREDUCAOALIQUOTA |
| UB28 | pAliqEfet | E | UB26 | 1-1 | TTRBMOV.ALIQUOTA |
|  | **-x-** |  |  |  |  |
| UB35 | vIBSUF | E | UB17 | 1-1 | TTRBMOV.VALOR  Quando houver valor de diferimento (**vDif**) no tributo do item, esse valor será subtraído do cálculo final da tag, seguindo a fórmula: **vIBSUF = (gIBSCBS / vBC × (pIBSUF / 100)) – vDif** |
| **UB36** | **gIBSMun** | **G** | **UB15** | **1-1** |  |
| UB37 | pIBSMun | E | UB36 | 1-1 | TTRBMOV.ALIQUOTACHEIA  Quando for gerado o grupo ***gTribRegular*** (Tributação Regular), a tag ***<pIBSMun>*** será **zerada**. |
| **UB40** | **gDif** | **G** | **UB15** | **1-1** |  |
| UB41 | pDif | E | UB40 | 1-1 | TTRBMOV.PCTDIFERIMENTO |
| UB42 | vDif | E | UB40 | 1-1 | TTRBMOV.TRIBUTODIFERIDO |
| **UB43** | **gDevTrib** | **G** | **UB36** | **0-1** |  |
| UB44 | vDevTrib | E | UB43 | 1-1 |  |
| **UB45** | **gRed** | **G** | **UB36** | **0-1** |  |
| UB46 | pRedAliq | E | UB45 | 1-1 | TTRBMOV.PCTREDUCAOALIQUOTA |
| UB47 | pAliqEfet | E | UB45 | 1-1 | TTRBMOV.ALIQUOTA |
|  | **-x-** |  |  |  |  |
| UB54 | vIBSMun | E | UB36 | 1-1 | TTRBMOV.VALOR  Quando houver valor de diferimento (**vDif**) no tributo do item, esse valor será subtraído do cálculo final da tag, seguindo a fórmula: **vIBSMun= (gIBSCBS / vBC × (pIBSUF / 100)) – vDif** |
|  | **-x-** |  |  |  |  |
| UB54a | vIBS | E | UB15 | 1-1 | Valor do IBS (soma de vIBSUF e vIBSMun). Quando houver crédito presumido com indicador “*IndDeduzCredPres*=1”, o vCredPres será subtraído desse valor.  *O* indicador *IndDeduzCredPres* é definido na **Regra Tributária**, aba **Detalhes dos Tributos**, campo **Deduz Crédito Presumido**. A **Regra Tributária** correspondente deve estar vinculada no **Item do Movimento**.  Para mais informações, acesse a documentação: |
| **UB55** | **gCBS** | **G** | **UB15** | **1-1** |  |
| UB56 | pCBS | E | UB55 | 1-1 | TTRBMOV.ALIQUOTACHEIA  Quando for gerado o grupo ***gTribRegular*** (Tributação Regular), a tag ***<pCBS>*** será **zerada**. |
| **UB59** | **gDif** | **G** | **UB55** | **1-1** |  |
| UB60 | pDif | E | UB59 | 1-1 | TTRBMOV.PCTDIFERIMENTO |
| UB61 | vDif | E | UB59 | 1-1 | TTRBMOV.TRIBUTODIFERIDO |
| **UB62** | **gDevTrib** | **G** | **UB55** | **0-1** |  |
| UB63 | vDevTrib | E | UB62 | 1-1 |  |
| **UB64** | **gRed** | **G** | **UB55** | **0-1** |  |
| UB65 | pRedAliq | E | UB64 | 1-1 | TTRBMOV.PCTREDUCAOALIQUOTA |
| UB66 | pAliqEfet | E | UB64 | 1-1 | TTRBMOV.ALIQUOTA |
|  | **-x-** |  |  |  |  |
| UB67 | vCBS | E | UB55 | 1-1 | TTRBMOV.VALOR  Quando houver valor de diferimento (**vDif**) no tributo do item, esse valor será subtraído do cálculo final da tag, seguindo a fórmula: **vCBS = (gIBSCBS / vBC × (pCBS / 100)) – vDif**  Quando houver crédito presumido com indicador “*IndDeduzCredPres*=1”, o vCredPres será subtraído desse valor.   * *O* indicador *IndDeduzCredPres* é definido na **Regra Tributária**, aba **Detalhes dos Tributos**, campo **Deduz Crédito Presumido**. * A **Regra Tributária** correspondente deve estar vinculada no **Item do Movimento**. * Para mais informações, acesse a documentação: |
| **UB68** | **gTribRegular** | **G** | **UB15** | **0-1** | Este grupo será gerado se houver uma Regra Tributária Regular associada à Regra Tributária informada no Item do Movimento. |
| UB69 | CSTReg | E | UB68 | 1-1 | DREGRATRIBUTARIA.SITUACAOTRIBUTARIA |
| UB70 | cClassTribReg | E | UB68 | 1-1 | DREGRATRIBUTARIA.CLASSTRIB |
| UB71 | pAliqEfetRegIBSUF | E | UB68 | 1-1 | TTRBMOV.ALIQUOTACHEIA |
| UB72 | vTribRegIBSUF | E | UB68 | 1-1 | TTRBMOV.BASEDECALCULO \*  TTRBMOV.ALIQUOTACHEIA |
| UB72a | pAliqEfetRegIBSMun | E | UB68 | 1-1 | TTRBMOV.ALIQUOTACHEIA |
| UB72b | vTribRegIBSMun | E | UB68 | 1-1 | TTRBMOV.BASEDECALCULO \*  TTRBMOV.ALIQUOTACHEIA |
| UB72c | pAliqEfetRegCBS | E | UB68 | 1-1 | TTRBMOV.ALIQUOTACHEIA |
| UB72d | vTribRegCBS | E | UB68 | 1-1 | TTRBMOV.BASEDECALCULO \*  TTRBMOV.ALIQUOTACHEIA |
| **UB82a** | **gTribCompraGov** | **G** | **UB15** | **0-1** |  |
| UB82b | pAliqIBSUF | E | UB82a | 1-1 | TTRBMOV.ALIQUOTA |
| UB82c | vTribIBSUF | E | UB82a | 1-1 | TTRBMOV.VALOR  - TTRBMOV.TRIBUTODIFERIDO |
| UB82d | pAliqIBSMun | E | UB82a | 1-1 | TTRBMOV.ALIQUOTA |
| UB82e | vTribIBSMun | E | UB82a | 1-1 | TTRBMOV.VALOR  - TTRBMOV.TRIBUTODIFERIDO |
| UB82f | pAliqCBS | E | UB82a | 1-1 | TTRBMOV.ALIQUOTA |
| UB82g | vTribCBS | E | UB82a | 1-1 | TTRBMOV.VALOR - TTRBMOV.TRIBUTODIFERIDO |
| **UB84** | **gIBSCBSMono** | **CG** | **UB14a** | **1-1** |  |
| **UB84a** | **gMonoPadrao** | **G** | **UB84** | **0-1** |  |
| UB85 | qBCMono | E | UB84a | 1-1 |  |
| UB86 | adRemIBS | E | UB84a | 1-1 |  |
| UB87 | adRemCBS | E | UB84a | 1-1 |  |
| UB88 | vIBSMono | E | UB84a | 1-1 |  |
| UB89 | vCBSMono | E | UB84a | 1-1 |  |
| **UB90** | **gMonoReten** | **G** | **UB84** | **0-1** |  |
| UB91 | qBCMonoReten | E | UB90 | 1-1 |  |
| UB92 | adRemIBSReten | E | UB90 | 1-1 |  |
| UB93 | vIBSMonoReten | E | UB90 | 1-1 |  |
| UB93a | adRemCBSReten | E | UB90 | 1-1 |  |
| UB93b | vCBSMonoReten | E | UB90 | 1-1 |  |
| **UB94** | **gMonoRet** | **G** | **UB84** | **0-1** |  |
| UB95 | qBCMonoRet | E | UB94 | 1-1 |  |
| UB96 | adRemIBSRet | E | UB94 | 1-1 |  |
| UB97 | vIBSMonoRet | E | UB94 | 1-1 |  |
| UB98 | adRemCBSRet | E | UB94 | 1-1 |  |
| UB98a | vCBSMonoRet | E | UB94 | 1-1 |  |
| **UB99** | **gMonoDif** | **G** | **UB84** | **0-1** |  |
| UB100 | pDifIBS | E | UB99 | 1-1 |  |
| UB101 | vIBSMonoDif | E | UB99 | 1-1 |  |
| UB102 | pDifCBS | E | UB99 | 1-1 |  |
| UB103 | vCBSMonoDif | E | UB99 | 1-1 |  |
|  | **-x-** |  |  |  |  |
| UB104 | vTotIBSMonoItem | E | UB84 | 1-1 |  |
| UB105 | vTotCBSMonoItem | E | UB84 | 1-1 |  |
| **UB106** | **gTransfCred** | **CG** | **UB14a** | **1-1** |  |
| UB107 | vIBS | E | UB106 | 1-1 |  |
| UB108 | vCBS | E | UB106 | 1-1 |  |
| **UB109** | **gCredPresIBSZFM** | **G** | **UB14a** | **0-1** |  |
| UB110 | tpCredPresIBSZFM | E | UB109 | 1-1 |  |
| UB111 | vCredPresIBSZFM | E | UB109 | 0-1 |  |
| **UB119** | **-x-** | **G** | **UB12** | **0-1** |  |
| **UB120** | **gCredPresOper** | **CG** | **UB119** | **1-1** |  |
| UB121 | vBCCredPres | E | UB120 | 1-1 |  |
| UB122 | cCredPres | E | UB120 | 1-1 | TTRBMOV.CODCREDPRESUMIDO  O campo é gerado no XML com **zero à esquerda** sempre que o código possuir apenas **1 caractere**.  **Exemplo:**   * Valor informado: `4` * Valor gerado no XML: `04` |
| **UB123** | **gIBSCredPres** | **G** | **UB120** | **0-1** |  |
| UB124 | pCredPres | E | UB123 | 1-1 | TTRBMOV.PCCREDPRESUMIDO |
| UB125 | vCredPres | CE | UB123 | 1-1 | TTRBMOV.VALORCREDPRESUMIDO |
| UB126 | vCredPresCondSus | CE | UB123 | 1-1 |  |
| **UB127** | **gCBSCredPres** | **G** | **UB120** | **0-1** |  |
| UB128 | pCredPres | E | UB127 | 1-1 | TTRBMOV.PCCREDPRESUMIDO |
| UB129 | vCredPres | CE | UB127 | 1-1 | TTRBMOV.VALORCREDPRESUMIDO |
| UB130 | vCredPresCondSus | CE | UB127 | 1-1 |  |
