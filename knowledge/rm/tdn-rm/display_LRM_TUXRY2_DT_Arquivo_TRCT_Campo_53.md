---
content_hash: 8769f940974c2cff7d2af3c4028b20c3fba5eba28f9c3a41f0b8be7d57713c39
fetched_at: '2026-06-29T00:08:11.448394+00:00'
page_id: '243010076'
product: rm
source: tdn-rm
title: TUXRY2_DT_Arquivo_TRCT_Campo_53
type: documentation
url: https://tdn.totvs.com/display/LRM/TUXRY2_DT_Arquivo_TRCT_Campo_53
version: 116
---

# TERMO DE RESCISÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Termo de Rescisão* |
| **Situação/Requisito:** | Na emissão do TRCT no campo 53 a descrição está como "Insalubridade 60%". Isso acontece porque temos dois eventos de Insalubridade, o evento 0348 (Insalubridade 20%) e o 0349 (Insalubridade 40%). Contudo os percentuais valores são somados independente se o valor está zerado. |
| **Solução/Implementação:** | *Ajuste no arquivo TRCT campo 53 para informar descrição correta do percentual quando possuir mais de um evento e entre eles existir valores zerados. Agora o percentual do campo descrição quando o valor for zerado não é mais considerado.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TUXRY2 TVDVJY TUWKAL* |
| **Requisito (ISSUE):** |  |

divs
