---
content_hash: e9f72fc30f0ee42909b79ac4284ec9c3b1e642b45183a1fb14b59ba39cf5e58e
fetched_at: '2026-06-29T00:08:18.608926+00:00'
page_id: '265783780'
product: rm
source: tdn-rm
title: TVUW59_DT_Troca_Codigo_Secao
type: documentation
url: https://tdn.totvs.com/display/LRM/TVUW59_DT_Troca_Codigo_Secao
version: 117
---

# TROCA CÓDIGO DE SEÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Troca de código de seção* |
| **Situação/Requisito:** | *Ao realizar o processo de troca de código de uma seção, quando a base possui registros nas tabelas VPPRAMEDICOESEPI , VPPRAMEDICOESDANOSAUDE , VPPRAMEDICOESFONTEGERA , VPPRAMEDICOESMEDIDAS, VPPRAMEDICOESMEDIDASPROPOSTA , VPPRAMEDICOESMEIOPROPAGA (Recolhimento/Avaliação de Risco/EPI) , quando o processo é atualizado o sistema não atualiza nos dados da tabela o valor referente ao novo código de seção, deixando ainda o código antigo na tabela, causando assim erro de informação.* |
| **Solução/Implementação:** | *Foi ajustado o sistema para que quando for realizado o processo de troca de código de seção o sistema altere também a informação do código de seção nas tabelas VPPRAMEDICOESEPI *VPPRAMEDICOESEPI , VPPRAMEDICOESDANOSAUDE , VPPRAMEDICOESFONTEGERA , VPPRAMEDICOESMEDIDAS, VPPRAMEDICOESMEDIDASPROPOSTA , VPPRAMEDICOESMEIOPROPAGA*  .* |
| **Chamados relacionados:** | *TVUW59* |

divs
