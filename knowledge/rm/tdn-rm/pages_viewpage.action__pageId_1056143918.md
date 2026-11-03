---
content_hash: a4c484c0fcb56b5cebbf5ff3edce57236fa6b4d2eb668113bfc347258c9001f6
fetched_at: '2026-06-29T00:05:51.954489+00:00'
page_id: '1056143918'
product: rm
source: tdn-rm
title: Grupo para quando o RPS/DPS substitui outro documento (TPF)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1056143918
version: 1
---

### Voltar para [Layout único de integração da NFS-e com o TPF](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143731)

| Nome | Pai | Tipo Elemento | Ocorrência | Tipo Dado | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **substituicao** | **[rps](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143860)** | **G** | **0-1** | **--** | **Tag raiz para as informações sobre a substituição de um documento.** |  |  |
| serierps | substituicao | E | 1-1 | Alfanumérico | Série do RPS a ser substituído. | TMOV.SERIE |  |
| numerorps | substituicao | E | 1-1 | Numérico | Número do RPS a ser substituído. | TMOV.NUMEROMOV |  |
| numeronfse | substituicao | E | 1-1 | Numérico | Número da NFS-e a ser substituída. |  |  |
| idnfse | substituicao | E | 1-1 | Alfanumérico | ID da NFS-e no ERP a ser substituída. | Concatena TMOV.CODCOLIGADA + TMOV.IDMOV resultando em um numero aleatorio (num) Se num > 9 {           pos = tamanho do num - 9;           num = num.Remove(pos, pos); } idnfse = 100000000-num |  |
| tipo | substituicao | E | 1-1 | Numérico | Tipo do documento. Os conteúdos possíveis são:  •  1 – RPS;  •  2 – Nota Fiscal Conjugada (Mista);  •  3 – Cupom. |  |  |
| dtemissaonfse | substituicao | E | 1-1 | Date | Data da emissão da NFS-e a ser substituída. Formato AAAA-MM-DD | TMOV.DATAEMISSAO |  |
| chave | substituicao | v(50) | 0-1 | string | Chave de Acesso da NFS-e Substituída | Campo TMOV.CHAVEACESSONFE do movimento que esta sendo substituído |  |
| codigoMotivo | substituicao | c(2) | 0-1 | string | Código do Motivo da substituição | TMOV.MOTIVOSUBSTITUICAO | Os valores aceitos são: 01 - Desenquadramento de NFS-e do Simples Nacional; 02 - Enquadramento de NFS-e no Simples Nacional; 03 - Inclusão Retroativa de Imunidade/Isenção para NFS-e; 04 - Exclusão Retroativa de Imunidade/Isenção para NFS-e; 05 - Rejeição de NFS-e pelo tomador ou pelo intermediário se responsável pelo recolhimento do tributo; 99 – Outros;  Uso específico para NFS-e Modelo Nacional |
| descricaoMotivo | substituicao | v(255) | 0-1 | string | Descrição do Motivo da substituição | TMOV.JUSTIFICATIVASUBSTITUICAO | Ao ser informado, deve conter no mínimo 15 caracteres.  Uso específico para NFS-e Modelo Nacional |
