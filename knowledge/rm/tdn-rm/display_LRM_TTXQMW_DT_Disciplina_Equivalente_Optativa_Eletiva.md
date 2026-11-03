---
content_hash: 3a6e8a12849d3657e1c686411e15211a8260257ba0d0c7e9bff7f735e7aea5c7
fetched_at: '2026-06-29T00:08:09.415979+00:00'
page_id: '239036516'
product: rm
source: tdn-rm
title: TTXQMW_DT_Disciplina_Equivalente_Optativa_Eletiva
type: documentation
url: https://tdn.totvs.com/display/LRM/TTXQMW_DT_Disciplina_Equivalente_Optativa_Eletiva
version: 122
---

# ANÁLISE CURRICULAR

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **TOTVS Gestão Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Histórico.* | *Análise Curricular.* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Equivalência*.* | *Disciplinas equivalentes da matriz curricular.* | | **Optativa/Eletiva** | *Disciplinas optativas/eletivas da matriz curricular.* | |
| **Cadastros Iniciais:** | *1) Informar uma disciplina como equivalente na matriz curricular do aluno.*  *2) Informar a mesma disciplina acima como optativa ou eletiva na matriz curricular do aluno.*  *3) Aprovar o aluno na disciplina acima, seja por matrícula ou aproveitamento de estudo.* |
| **Parâmetro(s):** | *Permitir que uma disciplina seja equivalente e optativa/eletiva na Análise Curricular.* |
| **Ponto de Entrada:** | *N/A.* |
| **Chamados Relacionados** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **País(es):** | *Todos.* |
| **Banco(s) de Dados:** | *Todos.* |
| **Tabelas Utilizadas:** | *SHISTDISCOPTELETIVAS* |
| **Sistema(s) Operacional(is):** | *Todos.* |

## Descrição

Criação de novo parâmetro para permitir que disciplinas equivalentes também sejam contabilizadas como optativas/eletivas na Análise Curricular.  
Para que o parâmetro acima gere efeito na análise curricular, a disciplina concluída pelo aluno deve ser cadastrada como equivalente e optativa/eletiva na matriz.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **Configurador (Educacional)**, acesse **Secretaria/Geral 2/5** e Configure o parâmetro a seguir:

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| **Nome:** | **Permitir que uma disciplina seja equivalente e optativa/eletiva na Análise Curricular.** |
| **Tipo:** | *Checkbox* |
| **Cont. Por.:** | *Desmarcado* |
| **Descrição:** | *Permitir que disciplinas equivalentes sejam contabilizadas como optativas/eletivas na Análise Curricular.* |

## Procedimento para Utilização

**Exemplo:**

       1.            Na Matriz Curricular informe uma disciplina como optativa/eletiva.

       2.            No cadastro de disciplinas equivalentes, cadastre a disciplina optativa criada anteriormente como disciplina equivalente a outra disciplina da mesma grade.

Desta forma a disciplina será equivalente e optativa/eletiva na mesma grade.

       3.            Crie/Matricule um aluno na matriz aplicada acima.

       4.            Aprove o aluno na disciplina que é equivalente e optativa eletiva na matriz curricular.

Aprovar o aluno com matrícula normal ou aproveitamento de estudo.

       5.            Acessar a visão de Curso/Habilitação do aluno e visualize a Análise Curricular.

**Obs.:** O acesso também pode ser realizado no portal do aluno, porém acessando o item Histórico.

       6.            A exibição da disciplina na análise curricular vai depender do novo parâmetro criado. Abaixo segue o comportamento do sistema, quando o parâmetro está marcado ou desmarcado.

Parâmetro:

false500ParametroAnaliseCurricularfade300trueDesmarcadoDesmarcadoDesmarcado

Ao visualizar a análise curricular a disciplina em questão irá eliminar a disciplina da grade como equivalência e não será contabilizada como disciplina optativa/eletiva.

Vale ressaltar que a disciplina será visualizada no grupo de disciplinas optativas/eletivas, porém não terá os créditos/carga horárias contabilizados para o aluno.

Exemplo de exibição da análise curricular:

**Obs.:**Sistema parametrizado para exibir resumo na análise curricular.

Visualização do grupo de disciplinas optativas/eletivas:

0MarcadoMarcadoMarcado

Ao visualizar a análise curricular a disciplina em questão irá eliminar a disciplina da grade como equivalência e também será contabilizada como disciplina optativa/eletiva.

A disciplina será visualizada no grupo de disciplinas optativas/eletivas e seus créditos/cargas horárias serão contabilizadas para o aluno.

Exemplo de exibição da análise curricular:

**Obs.:**Sistema parametrizado para exibir resumo na análise curricular.

Visualização do grupo de disciplinas optativas/eletivas:

divs
