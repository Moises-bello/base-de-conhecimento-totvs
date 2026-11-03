---
content_hash: b9e096520ee4edcec2d966b009ad6e19cdbcb59f21768549cc4d9e2a994ffedd
fetched_at: '2026-06-29T00:08:58.004821+00:00'
page_id: '358454086'
product: rm
source: tdn-rm
title: DEDUMOBILE-1000 DT Envio de notificação de ocorrência por grupo no perfil educacional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=358454086
version: 89
---

# Notificação de ocorrência por grupo no perfil do educacional

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Cadastro de ocorrência do aluno |
| **Situação/Requisito:** | Ao acessar o anexo de ocorrências do aluno, e cadastrar uma ocorrência com um tipo de ocorrência que no perfil do aluno não está habilitado, o sistema está notificando os usuários do eduCONNECT, mesmo o usuário não tendo acesso ao tipo de ocorrência no perfil educacional. |
| **Solução/Implementação:** | Foi realizado um ajuste no TOTVS Gestão Educacional para o cadastro de ocorrência do aluno, de maneira que o sistema realize a notificação do aluno apenas se em seu perfil possuir acesso ao tipo de ocorrência no perfil educacional (Serviços Globais | Segurança | Perfis | anexo Parâmetros educacionais, aba ocorrências). |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs

Aperfeiçoado o envio de mensagens aos pais do aluno quando este estiver matriculado em dois ou mais cursos.
