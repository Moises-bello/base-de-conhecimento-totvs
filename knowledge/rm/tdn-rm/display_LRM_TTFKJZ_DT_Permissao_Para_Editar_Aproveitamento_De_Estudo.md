---
content_hash: 4eb04229a7e65a7e9f12459b154877968c84614f11b1b73e6941f4ea60e9f6ed
fetched_at: '2026-06-29T00:06:10.334526+00:00'
page_id: '203760998'
product: rm
source: tdn-rm
title: TTFKJZ_DT_Permissao_Para_Editar_Aproveitamento_De_Estudo
type: documentation
url: https://tdn.totvs.com/display/LRM/TTFKJZ_DT_Permissao_Para_Editar_Aproveitamento_De_Estudo
version: 1
---

# Aproveitamento de estudo

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Educacional.* |
| **Módulo:** | *TOTVS Gestão Educacional.* |
| **Função:** | *Aproveitamento de estudo.* |
| **Situação/Requisito:** | *A permissão de editar aproveitamento de estudo está conflitando com a de excluir aproveitamento de estudo. Ao reestruturar as políticas de segurança*   *no sistema (EduActionModuleController), a de editar aproveitamento de estudo foi alterada para 30 e a de excluir para 31, e na action da tela de cadastro*  *de aproveitamento de estudo, a EduHistDiscFacAction, permaneceu a de editar como 31 e a de excluir como 30. Desta forma, mesmo dando permissão*  *ao usuário para realizar a edição, o mesmo não podia fazê-lo.* |
| **Solução/Implementação:** | *Correção nas tags de segurança em EduActionModuleController, setando a tag de editar aproveitamento de estudo para 31 e a de excluir para 30, mantendo*  *a ordem padrão das políticas de segurança no sistema que é primeiramente Incluir, em seguida Excluir e em seguida Editar.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *12.1.7.* |
