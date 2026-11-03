---
content_hash: 161815edbfccf85e311c540f3776cad0035b4e2c4a1c9a2a47fb8d70b1681a9d
fetched_at: '2026-06-29T00:08:05.150517+00:00'
page_id: '235585858'
product: rm
source: tdn-rm
title: Integração Modelo 1
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235585858
version: 5
---

A integração do TOTVS Educacional com o Scientia Enterprise foi planejada para que seja possível utilizar as funcionalidades de geração de quadro de horário, alocação de professores e alocação de salas disponíveis no Scientia Timetabler para geração de oferta de Turma/Disciplina no TOTVS Educacional.

Ao utilizar esta integração, o Scientia Timetabler será a ferramenta padrão para planejamento e organização do quadro de horários, alocação de Professores e Salas para as respectivas Turmas/Disciplinas do TOTVS Educacional.

Esta integração é dividida em dois processos principais, Exportação de dados do TOTVS Educacional para o Scientia Enterprise e Importação de dados do Scientia Enterprise para o TOTVS Educacional.

O processo de exportação de dados para o Scientia Enterprise é um recurso que envia os dados essenciais dos cadastros do TOTVS Educacional, permitindo a utilização do Scientia Enterprise para alocar professores, salas e gerar as ofertas de horários das Turmas/Disciplinas. No envio das informações o processo utiliza mascaras pré-definidas para que a relação entre informações dos dois sistemas seja identificada corretamente, possibilitando que a leitura da oferta montada seja realizada.

O processo de importação de dados é o recurso que permite que os agendamentos realizados no Scientia Timetabler sejam importados para o TOTVS Educacional, possibilitando assim que os horários da oferta de Turma/Disciplina e as alocações de Professores e Salas para estas Turmas/Disciplinas sejam atualizadas. Este processo busca informações das Atividades do Scientia que obedeçam as chaves criadas no processo de exportação.

**Documento Técnico:**

**Apresentação:**

**Arquivo LDF:**

**Script para liberar views para consulta:**

**Importação de  disponibilidades:**
