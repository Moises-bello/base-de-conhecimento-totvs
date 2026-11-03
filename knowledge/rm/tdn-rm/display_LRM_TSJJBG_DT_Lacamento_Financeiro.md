---
content_hash: 54712f1ddff134f1e04fc364e42bedbb5ff4f31578e58b3c35f7addad47008c4
fetched_at: '2026-06-29T00:06:24.256142+00:00'
page_id: '224115086'
product: rm
source: tdn-rm
title: TSJJBG_DT_Lacamento_Financeiro
type: documentation
url: https://tdn.totvs.com/display/LRM/TSJJBG_DT_Lacamento_Financeiro
version: 124
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *Lançamento financeiro* |
| **Situação/Requisito:** | Ao inserir um lançamento originado do RM Labore do tipo Contábil e com data de emissão anterior à data de criação, mesmo com o Parâmetro de data default da contabilização estar como Emissão, o sistema insere a contabilização com a data do sistema. Isto só acontece quando o lançamento é originado do Labore. |
| **Solução/Implementação:** | Otimizado geração de lançamento financeiro, para que o Labore não preencha a data de contabilização do lançamento ao enviar para o fluxus, visto que no parametrizador do fluxus há um parâmetro que define qual a data deve ser preenchida.  Caminho do parâmetro no fluxus: Acessar os parâmetros do fluxus, item 02.01 - contas a pagar. Ao avançar acessar item "Contab. Inclusão Pagar". Este parâmetro definirá a data a ser preenchida |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TSJJBG, TUCVU0 |
| **Requisito (ISSUE):** |  |

divs
