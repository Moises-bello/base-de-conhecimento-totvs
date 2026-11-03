---
content_hash: 0fac74af3fadf4e7fa68e76440689cef87467f34135b1a4055f45e5ab4e38c55
fetched_at: '2026-06-29T00:08:12.926155+00:00'
page_id: '243654384'
product: rm
source: tdn-rm
title: TVEAJU_DT_Validar_Cei_Ao_Editar_Rateio_Tomador_Funcionario
type: documentation
url: https://tdn.totvs.com/display/LRM/TVEAJU_DT_Validar_Cei_Ao_Editar_Rateio_Tomador_Funcionario
version: 114
---

# RATEIO DE TOMADORES

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rateio de Tomadores* |
| **Situação/Requisito:** | Inconsistência no rateio de tomador de serviços, o sistema esta setando o ID da tabela pfrateiotomador para 0 (zero) quando edita o rateio de tomador e há um cei que não existe. |
| **Solução/Implementação:** | Alterado o cadastro de rateio de tomador e distribuição do sefip para atualizar o cei informado no rateio do funcionário.  - Cadastro de Rateio: Será atualizado ao editar algum campo;  - Processo Distribuição do SEFIP: Parâmetro que caso marcado o sistema irá atualizar para todos os funcionários, que tem o ID do tomador preenchido, o campo CEI. |
| **Chamados relacionados:** | *TVEAJU* |

divs
