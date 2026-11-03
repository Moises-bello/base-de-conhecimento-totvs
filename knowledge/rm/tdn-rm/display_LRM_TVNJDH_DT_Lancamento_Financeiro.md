---
content_hash: a0104a282f0d7fd0976f505adbd44ca12a52848ab2d8fbd799b6ef4d9cbc5abb
fetched_at: '2026-06-29T00:08:15.712641+00:00'
page_id: '244921794'
product: rm
source: tdn-rm
title: TVNJDH_DT_Lancamento_Financeiro
type: documentation
url: https://tdn.totvs.com/display/LRM/TVNJDH_DT_Lancamento_Financeiro
version: 110
---

# Lançamento Financeiro

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *Lançamento financeiro* |
| **Situação/Requisito:** | Ao realizar geração de lançamentos financeiros através da guia de INSS, o sistema está salvando a informação do IDLAN incorretamente na tabela PGPS, dessa forma fica uma referência divergente da tabela FLAN |
| **Solução/Implementação:** | Ajuste realizado para que o labore espere a geração dos lançamentos financeiros pelo Fluxus, para que ao salvar as informações na tabela PGPS, o IdLan esteja preenchido, mantendo um vínculo entre as guias geradas e seus respectivos lançamentos financeiros |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TVNJDH |
| **Requisito (ISSUE):** |  |

divs
