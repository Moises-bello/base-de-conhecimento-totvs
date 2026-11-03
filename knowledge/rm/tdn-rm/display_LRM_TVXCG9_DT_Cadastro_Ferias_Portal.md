---
content_hash: bf5ffd26b804f0722172d90ef6ede6be367ae43b5cac9616a36ba566cf94c5e2
fetched_at: '2026-06-29T00:08:19.345422+00:00'
page_id: '267781845'
product: rm
source: tdn-rm
title: TVXCG9_DT_Cadastro_Ferias_Portal
type: documentation
url: https://tdn.totvs.com/display/LRM/TVXCG9_DT_Cadastro_Ferias_Portal
version: 112
---

# CADASTRO DE FÉRIAS PELO PORTAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cadastro de férias pelo Portal.* |
| **Situação/Requisito:** | Quando um usuário acessa o RM Portal para efetuar a Sugestão de Férias de um Período Aquisitivo Futuro, o Saldo Disponível aparece 30 dias porém ao cadastrar e salvar, o sistema retorna erro, informando uma restrição no saldo disponível conforme o Período Aquisitivo Atual, desta forma o sistema está realizando a validação das faltas de acordo com o período atual e não de acordo com o período futuro. |
| **Solução/Implementação:** | *Foi ajustado o sistema para que no momento em que for realizada sugestão de férias futuras pelo portal, o sistema considere as faltas do período futuro e não do período atual como estava sendo feito.* |
| **Chamados relacionados:** | TVXCG9 |

divs
