---
content_hash: 11a9b424edd646ad6551330cbbce4f627d898a626a13487ca6348fa3bb7558c2
fetched_at: '2026-06-29T00:06:17.158072+00:00'
page_id: '212905493'
product: rm
source: tdn-rm
title: Cópia de TRXHXM_DT_ERRO_Movimentacao_Com_Multa_Sem_Centro_De_Custo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=212905493
version: 2
---

# MOVIMENTAÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Bibliotecária* |
| **Função:** | *Movimentações* |
| **Situação/Requisito:** | *Ao realizar o processo de devolução de uma movimentação quando o parâmetro "Rateio Centro de Custo/Natureza Orçamentária" estiver marcado como "Não obrigatório" o centro de custo não está sendo preenchido no lançamento gerado.* |
| **Solução/Implementação:** | *O método responsável por validar o uso do rateio por centro de custo estava utilizando um objeto do Fluxus que não permitia a correta validação se o reateio estava definido para o centro de custo ou não.*  *Foi realizado um ajuste, alterando o objeto utilizado por outro mais coerente com a validação necessária.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.42* |
| **Versão Corrigida:** | *Versão na qual está sendo feita a manutenção deste programa.* |
| **Versão Expedida:** | *Versão em que o programa será oficialmente expedido.* |

divs
