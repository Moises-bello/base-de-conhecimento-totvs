---
content_hash: 36b3d0ce747ee61cb4e944651b1b4380d7bdf970b2ecf8f4ace79b8d44a199d3
fetched_at: '2026-06-29T00:06:17.201727+00:00'
page_id: '213975383'
product: rm
source: tdn-rm
title: TTGEQW_DT_Faturamento_Movimento_Tolerancia_Item
type: documentation
url: https://tdn.totvs.com/display/LRM/TTGEQW_DT_Faturamento_Movimento_Tolerancia_Item
version: 3
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Gestão de Estoque, Compras e Faturamento* |
| **Função:** | Faturar Movimento |
| **Situação/Requisito:** | Ao alterar a unidade de medida no faturamento de movimentos, o sistema não faz a conversão para o campo de  quantidade do movimento, e se utilizado tolerância para o item, o sistema não faz a conversão para consistir  a tolerância, consequentemente é acionada exceção barrando o processo de faturamento |
| **Solução/Implementação:** | Melhoria no processo de faturamento de movimento parametrizado para utilizar tolerância(Quantidade/Preço) no item. Mesmo alterando a unidade de medida, quantidade e preço a consistência é acionada caso atinja o limite mínimo e máximo de tolerância para o determinada produto |
| **Conversores e Parâmetros:** | Não se aplica |
| **Chamados relacionados:** | *Não se aplica* |
| **Requisito (ISSUE):** | Não se aplica |
| **Versões/Release:** | *12.1.8* |
| **Versão Corrigida:** | 12.1.8 |
| **Versão Expedida:** | 12.1.8 |

divs
