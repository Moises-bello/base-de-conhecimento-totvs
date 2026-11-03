---
content_hash: 5e844b04be49793c6de437fa1449271755a91daf1c70714ef88ddc63bbdf3c7d
fetched_at: '2026-06-29T00:08:38.284431+00:00'
page_id: '285646611'
product: rm
source: tdn-rm
title: 1081012 MSAU-12001 DT Carregar Dados Paciente BPA
type: documentation
url: https://tdn.totvs.com/display/LRM/1081012+MSAU-12001+DT+Carregar+Dados+Paciente+BPA
version: 104
---

# BPA não puxa dados do paciente

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | BPA SUS |
| **Situação:** | A tela de lançamento de BPA não carregava dados do paciente ao incluir um novo registro. |
| **Solução:** | Devido a migração para tecnoliga .Net a logica de funcionamento desta tela mudou.  Como um paciente pode ter uma ou mais parciais, agora o usuário deverá clicar em pesquisar (botão "...") e realizar a busca do paciente pela tela de pesquisa.  Automaticamente já são exibidas as parciais do paciente evitando realizar uma pesquisa adicional como no modo antigo. |

divs
