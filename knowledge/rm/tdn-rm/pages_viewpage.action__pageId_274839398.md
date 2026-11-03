---
content_hash: 1b7bc82b26b7c7245a3e3862bdc492bca63544c0552eebdaead5a923264de54d
fetched_at: '2026-06-29T00:08:34.756807+00:00'
page_id: '274839398'
product: rm
source: tdn-rm
title: 699031 FOPROTINAS01-227 MANAD Funcionário Autônomo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274839398
version: 97
---

# MANAD

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | MANAD |
| **Situação/Requisito:** | Ao gerar o arquivo MANAD para funcionário do tipo autônomo o campo ’10 – DT\_ADMISSAO’ do registro K050 considera a data de admissão do funcionário, porém conforme as instruções contidas no layout do MANAD para contribuintes individuais (trabalhadores autônomos) o campo dever ser apresentado vazio. |
| **Solução/Implementação:** | Tratar data de admissão no registro K050 para ir vazia em casos de funcionários autônomos. |
| **Tickets relacionados:** | 699031 |

divs
