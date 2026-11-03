---
content_hash: a7566612103c8765e8aa37119f1b6ef5a9484b9dac9a2114dc6fabc1ad8e41d4
fetched_at: '2026-06-29T00:08:20.918272+00:00'
page_id: '268596881'
product: rm
source: tdn-rm
title: TVWDEV_DT_SEFIP_AFASTAMENTO_INVALIDEZ
type: documentation
url: https://tdn.totvs.com/display/LRM/TVWDEV_DT_SEFIP_AFASTAMENTO_INVALIDEZ
version: 114
---

# SEFIP

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Emissão dos registros 30 e 32* |
| **Situação/Requisito:** | Funcionário que tenha afastamento na competência por aposentadoria por invalidez código SEFIP "U3" mesmo não tendo valores a recolher deve constar o arquivo SEFIP.RE. |
| **Solução/Implementação:** | Para o SEFIP folha, quando o funcionário mesmo não tendo valores a serem recolhidos, mas possui afastamento com motivo de aposentadoria por invalidez. Este funcionário irá para o SEFIP.RE.  Porém para que a importação e execução no programa do SEFIP seja validado é necessário que haja pelo menos um funcionário com valores a recolher para filial. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TVWDEV* |
| **Requisito (ISSUE):** |  |

divs
