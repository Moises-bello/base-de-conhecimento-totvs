---
content_hash: 46d62f883c387bbcd454c38e23fd782fe5e487b54dcdec3e7627ead624ee007c
fetched_at: '2026-06-29T00:08:52.322265+00:00'
page_id: '338378886'
product: rm
source: tdn-rm
title: PORTALMOBILE01-3581 DT Cadastro de mensagem de notificação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=338378886
version: 94
---

# Cadastro de mensagem de notificação

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Cadastro de mensagem de notificação com o objetivo "Boleto próximo ao vencimento". |
| **Situação/Requisito:** | No cadastro de mensagem de notificação, quando selecionamos o objetivo "Boleto próximo ao vencimento", o sistema insere a mensagem com o tipo de execução fixa, mas na verdade deveria ser "eventual", para possibilitar ao usuário selecionar a mensagem pré-configurada no processo de Agendamento/envio de mensagens. |
| **Solução/Implementação:** | Foi realizado ajuste no cadastro de mensagens de notificação, de maneira que ao selecionar o objetivo "Boleto próximo ao vencimento", o sistema possa salvar a mensagem com tipo de execução eventual, permitindo assim que o usuário selecione essa mensagem no processo de Agendamento/envio de mensagens. |
| **Conversores e Parâmetros:** | Foi disponibilizado um script especifico para realizar a conversão das mensagens para eventuais com o objetivo "Boleto próximo ao vencimento". Esse script se encontra no conversor da versão atual (12.1.20), caso deseje executar o mesmo em versão anterior, deve-se solicitar ao suporte da TOTVS este script especifico (ExecSql.TOTVSEducacional.PORTALMOBILE01-3581\_CN.2018.02\_06). |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs

Aperfeiçoado o envio de mensagens aos pais do aluno quando este estiver matriculado em dois ou mais cursos.
