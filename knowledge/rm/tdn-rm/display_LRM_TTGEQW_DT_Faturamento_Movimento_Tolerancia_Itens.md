---
content_hash: 6d2bc59bb7b019546fdcc77a45b6e13208567a831e483ce4ab1c5dec1c6a33ee
fetched_at: '2026-06-29T00:06:13.982632+00:00'
page_id: '208349575'
product: rm
source: tdn-rm
title: TTGEQW_DT_Faturamento_Movimento_Tolerancia_Itens
type: documentation
url: https://tdn.totvs.com/display/LRM/TTGEQW_DT_Faturamento_Movimento_Tolerancia_Itens
version: 1
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
| **Versões/Release:** | *12.1.7* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

divs
