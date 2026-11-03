---
content_hash: a473c88c7d07f332b8d39a86cf34cebdabfb996cc8c1b9053e8f5ba37dec9146
fetched_at: '2026-06-29T00:08:42.351739+00:00'
page_id: '287069419'
product: rm
source: tdn-rm
title: 1192868 FINANCEIRO01-1794 Solicitar exclusão baixa cheque
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=287069419
version: 102
---

# Solicitar exclusão de contabilização de baixa de um item de baixa de cheque.

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Solicitar Exclusão de Contabilização |
| **Situação/Requisito:** | Ao criar um item de baixa do tipo cheque para um lançamento contábil o sistema cria o item de baixa como não contábil.  Ao passar pelos processos de Integrar no Lote 0, Regerar e Cancelar a Baixa o sistema modifica o item de baixa para não contábil, porém ainda existe contabilização no SALDUS. |
| **Solução/Implementação:** | Agora o sistema valida se também existe IDOPERACAO no item de baixa, se sim, a opção do Solicitar Exclusão também será apresentada. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | 1192868 |
| **Requisito:** | FIN000128 |

divs
