---
content_hash: 6edf0f29d7413efd967670eb9e2349b6ca86d34a844e1802d09ea11e0afadc49
fetched_at: '2026-06-29T00:08:45.761653+00:00'
page_id: '315887691'
product: rm
source: tdn-rm
title: 1485519 CONTROLADORIA01-628 DT Configuração Relatórios Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=315887691
version: 93
---

# Relatórios Contábeis

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | Relatórios Contábeis |
| **Situação/Requisito:** | O sistema está apresentando inconsistência ao gerar os balancetes, saindo com os valores errados. Foi observado que o cliente possui muitas preferências gravadas para os relatórios, porém ao exclui-las e fechar o relatório o sistema recupera as preferencias que deveriam ser excluídas, assim os valores saem divergentes. |
| **Solução/Implementação:** | O componente responsável por armazenar e excluir as configurações dos relatórios contábeis foi alterado. Ao clicar no botão excluir, sem selecionar uma configuração, é enviada uma mensagem solicitando a seleção da configuração a ser excluída. Desta maneira as preferências são excluídas permanentemente. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |

divs
