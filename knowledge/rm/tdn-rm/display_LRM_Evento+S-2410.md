---
content_hash: fe11f6bc32313f7db5b7b882b9b634241164662d946f04266583ac6efeb72755
fetched_at: '2026-06-29T00:11:10.079154+00:00'
page_id: '641165870'
product: rm
source: tdn-rm
title: Evento S-2410
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-2410
version: 2
---

Leiautes1Leiaute S-1.0

Mapeamento dos campos para o leiaute S-1.0

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Registro\_eSocial | Campo\_eSocial | Tabela\_RM | Coluna\_RM | Informações\_do\_calculo |
| ideEvento | indRetif |  |  | Conforme manual |
| ideEvento | nrRecibo |  | PROTOCOLO |  |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| beneficiario | cpfBenef | PPESSOA | CPF |  |
| beneficiario | matricula | PFUNC | MATRICULABENEFICIARIO |  |
| beneficiario | cnpjOrigem | PFUNC | CNPJRESPONSAVELMATRICULA |  |
| infoBenInicio | cadIni |  |  |  |
| infoBenInicio | indSitBenef | PFBENEFICIO | SITUACAOBENEFICIO |  |
| infoBenInicio | nrBeneficio | PFBENEFICIO | NUMEROBENEFICIO |  |
| infoBenInicio | dtIniBeneficio | PFBENEFICIO | DATAINICIOBENEFICIO |  |
| infoBenInicio | dtPublic | PFBENEFICIO | DATACONCESSAOBENEFICIO |  |
| dadosBeneficio | tpBeneficio | PFBENEFICIO | TIPOBENEFICIO |  |
| dadosBeneficio | tpPlanRP | PFBENEFICIO | TIPOPLANOSEGREGACAOMASSA |  |
| dadosBeneficio | dsc | PFBENEFICIO | DESCRICAOORIGEMBENEFICIO |  |
| dadosBeneficio | indDecJud | PFBENEFICIO | BENEFICIODETERMINACAOJUDICIAL |  |
| infoPenMorte | tpPenMorte | PFBENEFICIO | TIPOPENSAOMORTE |  |
| infoPenMorte | dtInst | PFBENEFICIO | DTOBITOINSTITUIDORPENSAOMORTE |  |
| infoBenTermino | dtTermBeneficio | PFBENEFICIOSUSPENSAO | DATASUSPENSAOBENEFICIO |  |
| infoBenTermino | mtvTermino | PFBENEFICIOSUSPENSAO | MOTIVOSUSPENSAOBENEFICIO |  |
