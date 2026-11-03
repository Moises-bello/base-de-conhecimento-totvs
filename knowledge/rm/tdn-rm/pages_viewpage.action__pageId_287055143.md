---
content_hash: e554fcea8b155606016adbfd27d185f2ba479f5330a914f4775d189a9f85b9f6
fetched_at: '2026-06-29T00:08:42.144814+00:00'
page_id: '287055143'
product: rm
source: tdn-rm
title: EDUCACIONAL01-2375 DT Geração de Usuários para Responsáveis do Aluno
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=287055143
version: 104
---

# GERAÇÃO DE USUÁRIOS PARA RESPONSÁVEIS DO ALUNO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Geração de Usuários |
| **Situação/Requisito:** | Foi identificado que, se tentarmos executar o processo de geração de usuário para um aluno sem responsáveis e sem período letivo, marcando apenas os parâmetros: "Gerar usuário para aluno sem matricula no período letivo" e "Gerar usuário para responsável financeiro" o sistema encerra o processo como finalizado com sucesso mesmo sem gerar nenhum usuário e não possuir LOG.  Gostaria que verificasse também se o parâmetro "Gerar usuário para aluno sem matricula no período letivo" geraria o usuário do aluno, ou se apenas é uma PERMISSÃO de gerar sem matricula. Caso seja apenas uma permissão, solicito a alteração de sua nomenclatura e que o parâmetro só possa ser habilitado quando o de gerar usuário para aluno estiver marcado. |
| **Solução/Implementação:** | Alterações no processo de Geração de Usuários do Cadastro de Aluno:  - Alterada a opção "Gerar usuários para alunos sem matrícula no período letivo" para "Considerar alunos sem matrícula no período letivo"  - Essa opção ficará desabilitada quando a opção "Gerar usuários para alunos" não estiver marcada.  - Ao rodar o processo com a opção "Gerar usuários para responsáveis (pai, mãe e responsável acadêmico)" marcada, o sistema irá verificar se o aluno possui algum responsável cadastrado, e caso contrário irá gerar uma mensagem de erro.  - Corrigido problema na verificação de filiação falecida: O sistema não deve gerar usuário para filiação falecida, porém, por causa de uma falha na validação, estava gerando. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
