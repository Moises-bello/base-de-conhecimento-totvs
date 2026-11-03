---
content_hash: cc1464991185eca1047aa686c795470a2a7602c2fc64671cb4c3eb9421658059
fetched_at: '2026-06-29T00:10:47.662745+00:00'
page_id: '560653260'
product: rm
source: tdn-rm
title: Grupo para quando o RPS/DPS substitui outro documento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=560653260
version: 8
---

### Voltar para [Layout único de integração da NFS-e com o TSS](https://tdn.totvs.com/pages/viewpage.action?pageId=560652116)

| Nome | Pai | Tipo Elemento | Ocorrência | Tipo Dado | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **substituicao** | **[rps](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143227)** | **G** | **0-1** | **--** | **Tag raiz para as informações sobre a substituição de um documento.** |  |  |
| serierps | substituicao | E | 1-1 | Alfanumérico | Série do RPS a ser substituído. | TMOV.SERIE |  |
| numerorps | substituicao | E | 1-1 | Numérico | Número do RPS a ser substituído. | TMOV.NUMEROMOV |  |
| numeronfse | substituicao | E | 1-1 | Numérico | Número da NFS-e a ser substituída. |  |  |
| idnfse | substituicao | E | 1-1 | Alfanumérico | ID da NFS-e no ERP a ser substituída. | Concatena TMOV.CODCOLIGADA + TMOV.IDMOV resultando em um numero aleatorio (num) Se num > 9 {           pos = tamanho do num - 9;           num = num.Remove(pos, pos); } idnfse = 100000000-num |  |
| tipo | substituicao | E | 1-1 | Numérico | Tipo do documento. Os conteúdos possíveis são:  •  1 – RPS;  •  2 – Nota Fiscal Conjugada (Mista);  •  3 – Cupom. |  |  |
| dtemissaonfse | substituicao | E | 1-1 | Date | Data da emissão da NFS-e a ser substituída. Formato AAAA-MM-DD | TMOV.DATAEMISSAO |  |
