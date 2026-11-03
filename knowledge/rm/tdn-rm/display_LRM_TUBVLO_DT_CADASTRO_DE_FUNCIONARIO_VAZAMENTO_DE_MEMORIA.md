---
content_hash: 85414d34e50575132c41dcc0edaf37308264fca7d6945e4c9ab092f55a8a3677
fetched_at: '2026-06-29T00:08:07.051324+00:00'
page_id: '236602367'
product: rm
source: tdn-rm
title: TUBVLO_DT_CADASTRO_DE_FUNCIONARIO_VAZAMENTO_DE_MEMORIA
type: documentation
url: https://tdn.totvs.com/display/LRM/TUBVLO_DT_CADASTRO_DE_FUNCIONARIO_VAZAMENTO_DE_MEMORIA
version: 116
---

# CADASTRO DE FUNCIONÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cadastro de Funcionários* |
| **Situação/Requisito:** | Ao abrir diversas vezes a tela de cadastro de funcionários, navegando entre as opções, eram retidas muitas handles em memória, chegando ao ponto de gerar exception creating window handle. |
| **Solução/Implementação:** | *Foram adicionados diversos tratamentos de eliminação de objetos não mais utilizados em memória* |
| **Chamados relacionados:** | *TUBVLO, TVHFBH* |

divs
