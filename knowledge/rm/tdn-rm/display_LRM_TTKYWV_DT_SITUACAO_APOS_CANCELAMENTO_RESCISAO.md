---
content_hash: b4601f2d02a8b36cbcf6aaf19c347b9aba5a403fad8e083ec1ad23557962264f
fetched_at: '2026-06-29T00:06:12.919870+00:00'
page_id: '205921690'
product: rm
source: tdn-rm
title: TTKYWV_DT_SITUACAO_APOS_CANCELAMENTO_RESCISAO
type: documentation
url: https://tdn.totvs.com/display/LRM/TTKYWV_DT_SITUACAO_APOS_CANCELAMENTO_RESCISAO
version: 2
---

# CANCELAMENTO DA RESCISÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cancelamento da rescisão* |
| **Situação/Requisito:** | *Não atualizando a situação do funcionário de acordo com o histórico de situação* |
| **Solução/Implementação:** | Após o cancelamento da rescisão a situação do funcionário será atualizada de acordo com a última ocorrência no histórico de situação diferente de "D". A exceção a está regra é se a data de admissão for maior que a competência atual. Neste caso a situação passa ser 'Z'. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTKYWV |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

divs
