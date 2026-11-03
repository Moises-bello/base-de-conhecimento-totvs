---
content_hash: c9defd1b08206e62579d1dd1e80a6a678ba3a0e0b37289a62dcd9eb217cdcb04
fetched_at: '2026-06-29T00:11:10.575450+00:00'
page_id: '644306590'
product: rm
source: tdn-rm
title: Evento S-2420
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-2420
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
| ideBeneficio | cpfBenef | PPESSOA | CPF |  |
| ideBeneficio | nrBeneficio | PFBENEFICIO | NUMEROBENEFICIO |  |
| infoBenTermino | dtTermBeneficio | PFBENEFICIOSUSPENSAO | DATASUSPENSAOBENEFICIO |  |
| infoBenTermino | mtvTermino | PFBENEFICIOSUSPENSAO | MOTIVOSUSPENSAOBENEFICIO |  |
| infoBenTermino | cnpjOrgaoSuc | PFBENEFICIOSUSPENSAO | CNPJORGAOSUCESSOR |  |
| infoBenTermino | novoCPF | PPESSOA | CPF |  |
