---
content_hash: c3acb4006e897761f7032bf3837d58b41876b6a930d4262128ee234a17c9b1b0
fetched_at: '2026-06-29T00:09:31.970224+00:00'
page_id: '425458804'
product: rm
source: tdn-rm
title: Atendimentos
type: documentation
url: https://tdn.totvs.com/display/LRM/Atendimentos
version: 4
---

O Cadastro dos  dos alunos é realizado através do RM Totvs Educacional Web, o aluno deverá ter o perfil: Outras Permissões > RM Portal > Acadêmico > Solicitações  habilitado para possibilitar a abertura dos atendimentos no menu: Solicitações.

Através do executável, o usuário da secretaria poderá acompanhar os atendimentos, analisar e posicionar os atendimentos abertos pelos alunos.

Observação

Caso utilizem a parametrização disponível no TOTVS Aprovações e Atendimento (CRM):

* Parâmetros > Atendimentos > Visão de atendimentos

Alterando a consulta SQL responsável por recuperar os registros para a visão dos atendimentos

Para o funcionamento correto da tela de Atendimento no Educacional (Alunos > Anexos > Atendimento):

* Deve seguir as regras solicitadas pelo TOTVS Aprovações e Atendimento (CRM)
* E realizar o JOIN entre as tabelas HATENDIMENTOBASE e HCLIENTEATENDIMENTO, pois o Educacional utiliza a coluna RAALUNO
