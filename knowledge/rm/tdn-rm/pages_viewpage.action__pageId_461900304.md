---
content_hash: 4d6fac3262a5f4dfe77be92b0dc5b68183f5ae1ef82b78a7bfe699d497f49bd4
fetched_at: '2026-06-29T00:10:14.445938+00:00'
page_id: '461900304'
product: rm
source: tdn-rm
title: DT Novo Ensino Médio - Atividades Ofertadas - Ensino Básico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=461900304
version: 80
---

# NOVO ENSINO MÉDIO - ATIVIDADES OFERTADAS - ENSINO BÁSICO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **Totvs Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Cadastro de atividade ofertada* | **Cadastro de atividade ofertada** |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Inscrição de aluno na atividade ofertada* | **Inscrição de aluno na atividade ofertada** | | *Componentes* | *Componentes* | | *Modalidades* | *Modalidades* | | *Grupo de atividade* | **Grupo de atividade** | | *Tipo de participação* | **Tipo de participação** | | *Atividade curricular* | *Atividade curricular* | |
| **Cadastros Iniciais:** | * *Componente;*   + *Modalidade.* * *Curso / Série;* * *Aluno matriculado.* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *EDUCACIONAL01-7566 / EDUCACIONAL01-7567 / EDUCACIONAL01-7568* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *Sql Server e Oracle* |
| **Tabelas Utilizadas:** | *SATIVIDADE, SATIVIDADEALUNO* |
| **Sistema(s) Operacional(is):** | *Windows 7, 8 e 10* |

## Descrição

Foi disponibilizado no contexto do ensino básico o cadastro de atividades ofertadas, bem seus anexos e cadastros auxiliares para que seja possível ofertar uma atividade extra curricular neste contexto.

Além disso foi criado um anexo chamado Atividades curriculares no cadastro do aluno, com intuito de visualizar todas as atividades do aluno.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da release 12.1.24.

## Cadastro de Atividade Oferta - Ensino Básico

Para cadastrar uma atividade ofertada, deve-se acessar o menu Atividades Acadêmicas | Acadêmico | Atividades ofertadas.

Importante

Os campos referente a carga horária aproveitada e créditos foram ocultados. Apenas são disponíveis para o nível superior.

Para que a oferta seja válida é necessário vincular pelo menos um curso/série no anexo do cadastro da atividade.

## Inscrição de Aluno em Atividade Oferta - Ensino Básico

A inscrição do aluno é feita pelo anexo Alunos inscritos dentro do cadastro da atividade.

O mesmo poderá ser feito pelo anexo Atividades curriculares dentro do cadastro do aluno. Sendo que neste anexo é possível ver todas as atividades do aluno.

Importante

Os campos referente a carga horária aproveitada e créditos foram ocultados. Apenas são disponíveis para o nível superior.

## Processo de Inscrição de Aluno em Atividade Oferta - Ensino Básico

A inscrição em lote de alunos, poderá ser feita pelo processo de inscrição de dentro do cadastro da atividade oferta ou pelo menu Atividade acadêmicas | Atividades ofertas - Inscrições.

 

Importante

Os campos referente a carga horária aproveitada e créditos foram ocultados da entidade Aluno. Apenas são disponíveis para o nível superior.

Importante

A validação de choque de horário irá ocorrer ao se inscrever um aluno que possui turmas/disciplinas com horários conflitantes com a atividade ofertada.

divs
