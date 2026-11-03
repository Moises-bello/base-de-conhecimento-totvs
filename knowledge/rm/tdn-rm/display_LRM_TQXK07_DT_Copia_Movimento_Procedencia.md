---
content_hash: 16d4750acaec3f2c7c32088f8504938f95119ea33fb26ffa6899a7d06d8f4b4f
fetched_at: '2026-06-29T00:08:19.302242+00:00'
page_id: '267780215'
product: rm
source: tdn-rm
title: TQXK07_DT_Copia_Movimento_Procedencia
type: documentation
url: https://tdn.totvs.com/display/LRM/TQXK07_DT_Copia_Movimento_Procedencia
version: 111
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Gestão de Estoque, Compras e Faturamento* |
| **Função:** | *Cópia de Movimento* |
| **Situação/Requisito:** | Durante o processo de faturamento, o sistema não mantém a procedência informada no movimento de origem. |
| **Solução/Implementação:** | Fizemos um ajuste na rotina responsável por carregar o default do campo CST, o qual é utilizado na identificação da procedência.  O Default só será atribuído se o campo estiver nulo, ou seja, durante o processo de faturamento, se a informação tiver sido copiada do movimento de origem, a mesma será mantida. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | N/A |

divs
