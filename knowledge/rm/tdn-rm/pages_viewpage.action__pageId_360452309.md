---
content_hash: c974d3f8ee87f5d6a8d2fb5db220213324e4940057079a4fd6c30ae239d66433
fetched_at: '2026-06-29T00:08:58.634135+00:00'
page_id: '360452309'
product: rm
source: tdn-rm
title: DT Geração de usuários - Atribuição de permissão para todos os níveis de ensino
  matriculados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=360452309
version: 4
---

# GERAÇÃO DE USUÁRIO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Geração de Usuários* | *Geração de Usuários* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Cadastro de Alunos** | *Cadastro de Alunos* | |
| **Cadastros Iniciais:** | * *Para geração de usuários para cada entidades é necessário o cadastro dos itens:*   + *Aluno;*   + *Responsáveis do aluno;*   + *Responsável financeiro do aluno;* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *EDUCACIONAL01-3965* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *Sql Server e Oracle* |

## Descrição

Evolução no processo de geração de usuário (alunos, responsáveis do aluno, responsável financeiro do aluno) para que seja possível a atribuição de permissões a todos os níveis de ensino para os quais o aluno tenha matrícula no período letivo.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da Release ***12.1.17.274***.

## Procedimento para Utilização

O processo de geração de usuário foi alterado para permitir, que por opção, sejam atribuídas as permissões para todos os níveis de ensino para os quais o aluno possui matrícula.

Essa atribuição é realizada caso o parâmetro "**Atribuir permissão à todos os níveis de ensino matriculados**", na primeira etapa, seja marcado no processo para a geração de usuário para alunos e responsáveis.

Após sua execução o usuário criado terá acesso a todos os níveis de ensino em que o aluno tiver matrícula no período letivo e que pode ser verificado em:

***Serviços Globais | Segurança | Usuários | Anexos: Usuário/Filial***
