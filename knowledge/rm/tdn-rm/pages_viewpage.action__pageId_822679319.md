---
content_hash: 4c9a438b2ab9a96f87585843a97415785ba72fcd56f4d87b1cc7b3f42dd7cd67
fetched_at: '2026-06-29T00:11:46.054593+00:00'
page_id: '822679319'
product: rm
source: tdn-rm
title: infDPS/subst
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=822679319
version: 6
---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Pai | Obrigatório | Origem | Descrição |
| **subst** | **infDPS** | **Não** | **Grupo** | **Grupo de informações relativas à NFS-e a ser substituída** |
| chSubstda | infDPS/subst | Sim | Chave gravada na nota que está sendo substituída  TMOV.CHAVEACESSONFE | Chave de Acesso da NFS-e a ser substituída. |
| cMotivo | infDPS/subst | Sim | Aba Integrações, Fiscal, Campo "Motivo da Substituição" na nota substituta.  TMOV.MOTIVOSUBSTITUICAO | Código de justificativa para substituição de NFS-e:  01 - Desenquadramento de NFS-e do Simples Nacional; 02 - Enquadramento de NFS-e no Simples Nacional; 03 - Inclusão Retroativa de Imunidade/Isenção para NFS-e; 04 - Exclusão Retroativa de Imunidade/Isenção para NFS-e; 05 - Rejeição de NFS-e pelo tomador ou pelo intermediário se responsável pelo recolhimento do tributo; 99 - Outros;   Na geração do XML, **zeros à esquerda serão removidos**. Ou seja:   * Se o código cadastrado for **“01”**, o XML exibirá **“1”** * Se for **“02”**, o XML exibirá **“2”** |
| xMotivo | infDPS/subst | Não | Aba Integrações, Fiscal, Campo "Justificativa da Substituição" na nota substituta.  TMOV.JUSTIFICATIVASUBSTITUICAO | Descrição do motivo da substituição da NFS-e quando o emitente deve descrever o motivo da substituição para outros motivos (cMotivo = 9). |

Mais informações sobre a substituição:
