---
content_hash: 28c8ff92b8c58861bdecd3fed704beb912f2b3aac33ad8086cd063f0ff723462
fetched_at: '2026-06-29T00:08:17.961775+00:00'
page_id: '260538889'
product: rm
source: tdn-rm
title: TVUCXF_DT_Sindicato
type: documentation
url: https://tdn.totvs.com/display/LRM/TVUCXF_DT_Sindicato
version: 112
---

# CAMPO GLOBAL / CADASTRO SINDICATO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cadastro Sindicato / Campo Global* |
| **Situação/Requisito:** | Quando a flag 'Global' do campo 'Fornecedor para lançamento financeiro' está desmarcada na tela de cadastro do sindicato, porém no cadastro do cliente fornecedor a flag 'Global' está marcada, ao tentar realizar o processo de 'Cópia de sindicatos entre coligadas' é apresentado erro. |
| **Solução/Implementação:** | Ao acessar a tela de Sindicato e editar um sindicato, deve buscar o valor do campo 'Global' do cadastro do Cliente/Fornecedor para preencher o campo 'Global' do 'Fornecedor para lançamento financeiro'. |
| **Chamados relacionados:** | TVUCXF |

divs
