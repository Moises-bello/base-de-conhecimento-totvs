---
content_hash: b8dfa64098f24d13e9421edfb63aab2e71e4897b52fa765f8c056af08c016338
fetched_at: '2026-06-29T00:10:59.227826+00:00'
page_id: '614725588'
product: rm
source: tdn-rm
title: Exceções a anonimização no TOTVS Construção Obras e Projetos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=614725588
version: 22
---

## Exceções aos casos de eliminação de dados pessoais

Em algumas exceções, sujeitas ao controle da ANPD, os dados podem ser conservados pelo controlador:

* Caso exista necessidade de cumprimento de obrigação legal ou regulatória;
* Em casos de estudos por órgãos de pesquisa, desde que os dados estejam anonimizados;
* Também em casos de transferência a terceiros, desde que sejam respeitados os requisitos de tratamento de dados dispostos na lei;
* Uso exclusivo do controlador, vedado o acesso por terceiros e desde que os dados sejam anonimizados.

Papeis aos quais se aplica exceções:

| Papel | Restrições | Mensagem de Bloqueio |
| --- | --- | --- |
| Cliente / Fornecedor | Existência de Contratos em Projetos não revisados ou concluídos e cancelados. | Exemplo: "Existe um ou mais contratos com este Cliente/Fornecedor de CPF '99.999.999/9999-99' no Totvs Construção Obras e Projetos.  Contratos encontrados:  Contrato: 1207/2011 Código de Projeto: 0000 Coligada: 1 Contrato: 1207/2011 Código de Projeto: 0000 Coligada: 1  ..."  Obs.: Limitado a exibição de cinco contratos. |
| Cliente / Fornecedor | Existência de Projeto não Concluído ou cancelado com o Cliente Fornecedor. | Exemplo:  "Existe um projeto ativo com este Cliente Fornecedor.  Projetos encontrados: Projeto: 0001 Coligada: 1  Projeto: 0001 Coligada: 1" |
| Funcionário | Existência de Membro de Equipe Ativo | Quando não será permitido anonimizar:   * Quando o funcionário tem apontamentos de mão de obra vinculados a ele. * Quando o funcionário tem apropriações vinculadas. * Quando o funcionário está ativo em equipe de mobilidade. * Quando o  funcionário está vinculado a um usuário de coletor ativo. * Quando funcionário tem apontamento e devido a legislação xyz necessário manter histórico de 5 anos |
| Externo |  | Quando não será permitido anonimizar:   * Quando o terceiro tem apontamentos de mão de obra vinculados a ele. * Quando o terceiro tem apropriações vinculadas. * Quando o terceiro está ativo em equipe de mobilidade. * Quando o  terceiro está vinculado a um usuário de coletor ativo. * Quando terceiro tem apontamento e devido a legislação xyz necessário manter histórico de 5 anos |
| Pessoa |  |  |
