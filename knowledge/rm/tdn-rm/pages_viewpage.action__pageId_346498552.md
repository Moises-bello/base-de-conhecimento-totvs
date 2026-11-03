---
content_hash: 973dc70eba1420a9cd6c0e7f82ccfcdb4209ee998b3df761489f8152dc8b232e
fetched_at: '2026-06-29T00:08:54.823938+00:00'
page_id: '346498552'
product: rm
source: tdn-rm
title: DT Integração com o Pergamum - Chave de integração por RA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=346498552
version: 3
---

# INTEGRAÇÃO COM O PERGAMUM

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Gestão Educacional |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Exportação de usuários para o Pergamum | Integração com o Pergamum | | Geração automática de usuário do Pergamum | Integração com o Pergamum | |
| **Tickets relacionados** | Informe o(s) chamado(s) relacionado(s). |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | Informe o requisito relacionado (Issue). |
| **País(es):** | BRA |
| **Banco(s) de Dados:** | SQL Server / Oracle |
| **Tabelas Utilizadas:** | SPESSOAPERGAMUM |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

O processo de exportação de usuário visa criar um vínculo entre os usuários do Pergamum e a entidade do RM exportada (Aluno, Pessoa, Professor, Funcionário).

Até então, essa exportação era realizada utilizando como chave de integração os códigos de pessoa e CPF, que possui uma configuração comum no processo de parametrização do TOTVS Gestão Educacional.

Com a inclusão do RA como chave de integração, para alunos, essa parametrização foi quebrada. A partir dessa liberação, o sistema possuirá uma parametrização de chave de integração para o Aluno e outra para os demais usuários.

Essa quebra se fez necessária devido a utilização do RA, somente para o aluno.

Parâmetros:

***15.05 - Integração | 15.05.06 - Biblioteca | Biblioteca 4/5 | Chaves de Integração | Usuários***

***- Código de Pessoa***

***- CPF***

***15.05 - Integração | 15.05.06 - Biblioteca | Biblioteca 4/5 | Chaves de Integração | Alunos***

***- Código de Pessoa***

***- CPF***

***- RA***

Importante

A utilização do **RA** como chave de integração e a definição de uma máscara numérica pode gerar conflitos com códigos de outros usuários do Pergamum, já existentes, que utilizam o código de pessoa ou o CPF como chaves de integração.

Para os casos em que o código de **RA**, do aluno, coincidir com um código de outro usuário, esse aluno não será exportado e o mesmo deverá ser cadastrado no Pergamum e vinculado manualmente ao aluno, através do anexo "***Vínculo do usuário do Pergamum***".

Caso o código de **RA** seja *alfa-numérico*, deverá ser verificado com a equipe do ***Pergamum*** a alteração do campo de código de usuário para que permita receber esse tipo de valor.

Na exportação de Funcionários, Professores e Pessoas que forem, também, alunos matriculados, será exibido um parâmetro, no processo, que permitirá a opção de uso da chave de integração de usuários ou de alunos.

Caso seja optado por utilizar a chave de integração de alunos, e esse aluno possua mais de um RA matriculado, o sistema irá verificar se deverá enviar o primeiro encontrado ou todos. Essa parametrização poderá ser definida em:

***15.05 - Integração | 15.05.06 - Biblioteca | Biblioteca 4/5 | Chaves de Integração | "Caso um aluno possua mais de um RA cadastrado"***

- Enviar todos os RA do aluno para o Pergamum **(Todos os RA encontrados irão gerar um usuário no Pergamum)**

- Enviar o primeiro RA encontrado **(Apenas o primeiro RA encontrado irá gerar usuário no Pergamum)**

Caso essa opção não seja marcada, o sistema irá utilizar como chave o que foi parametrizado para a geração de chave de integração de usuários.

No processo de exportação, para as entidades Pessoa, Funcionário e Professor será exibida uma caixa de marcação, onde será permitida a opção de se utilizar a chave de integração parametrizada para aluno.

Caixa de marcação: ***"Caso o professor seja um aluno, utilizar o padrão de vínculo para o aluno"***

Após sua marcação será solicitado o período letivo em que o **RA** foi matriculado.

Processo de exportação de usuários para o Pergamum:

***Integrações | Pergamum | Exportar usuários para o Pergamum***
