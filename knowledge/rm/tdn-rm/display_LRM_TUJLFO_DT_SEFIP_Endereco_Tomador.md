---
content_hash: ccde11a9a2140f842ae6befe788a63500b95f7e71c85700d80fce20d5ed6efe8
fetched_at: '2026-06-29T00:06:28.594399+00:00'
page_id: '233756245'
product: rm
source: tdn-rm
title: TUJLFO_DT_SEFIP_Endereco_Tomador
type: documentation
url: https://tdn.totvs.com/display/LRM/TUJLFO_DT_SEFIP_Endereco_Tomador
version: 116
---

# GERAÇÃO DO SEFIP

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Geração do SEFIP |
| **Situação/Requisito:** | Ao gerar a SEFIP com o código de recolhimento 150 ou 155, o endereço do tomador (Cliente/Fornecedor) dos funcionários, não está sendo levado para o arquivo da SEFIP e ao validar o arquivo no aplicativo da caixa são apresentadas mensagens informando não conformidades. |
| **Solução/Implementação:** | Criação de método responsável por fornecer os dados referente ao endereço dos tomadores de serviços. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUJLFO; TULM93 |

divs
