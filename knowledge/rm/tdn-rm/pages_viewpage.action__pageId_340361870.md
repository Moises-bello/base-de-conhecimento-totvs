---
content_hash: a79f9fdb93614f499f13f768dbd343fc9e1b7c5de1b5a5e4d7fb149fb81b5bcf
fetched_at: '2026-06-29T00:08:52.389150+00:00'
page_id: '340361870'
product: rm
source: tdn-rm
title: PORTALMOBILE01-3599 DT Segurança de perfil para cadastro de categoria
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=340361870
version: 96
---

# Segurança de perfil para cadastro de categoria

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Segurança de perfil para cadastro de categoria |
| **Situação/Requisito:** | Quando um usuário possuir mais de um perfil do sistema Educacional, e no seu primeiro perfil não possuir nenhuma permissão para as categorias do eduCONNECT (Cadastro de perfil > Parâmetros educacionais > Central de Comunicação > Configuração de permissões às categorias do eduCONNECT), o sistema está exibindo erro ao tentar acessar uma mensagem pré-configurada no processo "Agendamento/envio de mensagens". |
| **Solução/Implementação:** | Foi realizado ajuste na rotina para obter as categorias de acesso para todos os perfis do usuário, assim caso o usuário possua mais de um perfil, o sistema irá verificar todas as categorias que possui acesso e exibir apenas categorias que o usuário pode acessar. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs

Aperfeiçoado o envio de mensagens aos pais do aluno quando este estiver matriculado em dois ou mais cursos.
