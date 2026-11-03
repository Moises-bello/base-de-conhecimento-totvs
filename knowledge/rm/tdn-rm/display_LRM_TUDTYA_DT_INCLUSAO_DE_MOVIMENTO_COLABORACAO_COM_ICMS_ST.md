---
content_hash: e906082a3b5dbd6b3a754d0b93b533b01639f1563367cbedc1274beb7adea897
fetched_at: '2026-06-29T00:06:28.882330+00:00'
page_id: '233764408'
product: rm
source: tdn-rm
title: TUDTYA_DT_INCLUSAO_DE_MOVIMENTO_COLABORACAO_COM_ICMS_ST
type: documentation
url: https://tdn.totvs.com/display/LRM/TUDTYA_DT_INCLUSAO_DE_MOVIMENTO_COLABORACAO_COM_ICMS_ST
version: 118
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | [TOTVS Gestão de Estoque, Compras e Faturamento - Manutenção](http://tdn.totvs.com/pages/viewpage.action?pageId=223916937) |
| **Função:** | *Inclusão de Movimento via Totvs Colaboração* |
| **Situação/Requisito:** | Ao realizar a 'Inclusão de Movimento com Arquivo XML', mesmo com a opção 'Busca Valores Totvs Colab', encontrada na etapa de tributação do item nos parâmetros do tipo de movimento, definida para 'Tipo de Movimento - não comparar com XML' quando o imposto é o 'ICMS ST' o sistema está buscando os valores do XML e não calculando com base nos parâmetros do sistema, conforme esperado. |
| **Solução/Implementação:** | Ajuste na Comparação de Tributos para Totvs Colaboração, quando o tributo for ICMSST |
| **Conversores e Parâmetros:** | *12.1.10* |
| **Chamados relacionados:** | TUDTYA |
| **Requisito (ISSUE):** | MOV000161 - TOTVS Colaboração |

divs
