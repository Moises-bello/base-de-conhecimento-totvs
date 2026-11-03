---
content_hash: 4d5738aff189a820ac43c921ab9d23135032ad1cbf0c39712115bb95187f64c7
fetched_at: '2026-06-29T00:08:23.071542+00:00'
page_id: '269444026'
product: rm
source: tdn-rm
title: 217943_DT_Inscricao_Candidato_Excedente_Lancamento
type: documentation
url: https://tdn.totvs.com/display/LRM/217943_DT_Inscricao_Candidato_Excedente_Lancamento
version: 113
---

# INSCRIÇÃO DE CANDIDATO EXCEDENTE

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Processo Seletivo* |
| **Função:** | *Inscrição de candidato excedente* |
| **Situação/Requisito:** | *Um processo seletivo que utilize controle de vagas com cadastro de excedente, quando um candidato é inscrito como excedente e o processo seletivo possui valor, o lançamento financeiro não é gerado, porém ao cancelar ou excluir uma inscrição, o candidato excedente deve ter sua inscrição e o lançamento gerado, porém caso o valor do processo seletivo seja zero (0) e a área ofertada possua valor, o sistema não gera o lançamento pois está considerando o valor do processo seletivo, que neste caso é zero (0), sendo que o que deve ser considerado é o valor da área ofertada.* |
| **Solução/Implementação:** | *Foi feito um ajuste no processo de cancelamento e exclusão de inscrições para que quando for alterar um candidato excedente para inscrito o sistema carregue o valor da área ofertada, assim, gerando o lançamento e também com o valor correto.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
