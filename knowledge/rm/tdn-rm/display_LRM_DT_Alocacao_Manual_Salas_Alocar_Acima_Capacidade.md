---
content_hash: 38fc319c63801428676581230160aa6ea69bcd290c013a1bf4a954f43565d240
fetched_at: '2026-06-29T00:08:23.077679+00:00'
page_id: '269444448'
product: rm
source: tdn-rm
title: DT_Alocacao_Manual_Salas_Alocar_Acima_Capacidade
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Alocacao_Manual_Salas_Alocar_Acima_Capacidade
version: 6
---

# Alocação manual de salas - Alocar acima da capacidade da sala

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM | | |
| ****Segmento Executor:**** | Educacional | | |
| **Módulo:** | Totvs Educacional | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Alocação manual de salas | Alocação manual de sala | | | |
| **Requisito (ISSUE):** | EDUEDU001-685 | | |
| **País:** | (X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

### Objetivo

Na alocação manual de salas, permitir associar uma turma/disciplina a uma sala mesmo que a capacidade desta seja menor que o total de alunos da turma/disciplina.

## Definição da Regra de Negócio

# Parametrização

Acessar: **Serviços Globais | Segurança | Perfis**

* Selecione o perfil do usuário
* Ir em anexo Parâmetros educacionais aba Geral
* Habilite “Permitir alocar salas com turmas/disciplinas acima da capacidade

# Alocação manual de sala

Acessar: **Módulo Educacional | Atividades acadêmicas | Infra-estrutura | Alocação de salas | Alocação manual**

* Informe o período letivo
* Selecione as turmas/disciplinas
* Selecione as salas
* Ao arrastar uma turma/disciplina para que possui número máximo de alunos = 50 , por exemplo, para uma sala com capacidade =40. O sistema irá informar que o número máximo de alunos é maior que a capacidade da sala.
* Para realizar  a alocação selecione o parâmetro “Permitir alocar salas com turmas/disciplinas acima da capacidade”
* Arraste a turma/disciplina para a sala

 

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Parâmetros educacionais do perfil do usuário | [Alteração] | Serviços globais -> Segurança -> Perfis -> Parâmetros educacionais | - |
| Alocação manual de salas | [Alteração] | Atividades acadêmicas -> Infra-estrutura -> Alocação de salas - > Alocação manual | - |

###
