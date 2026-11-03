---
content_hash: 48fb19f85fb09e763fe3fa9050df81409e038c13a9fa6be73bd08ca4e3987b02
fetched_at: '2026-06-29T00:10:53.821246+00:00'
page_id: '586708591'
product: rm
source: tdn-rm
title: Permitir que uma disciplina seja equivalente e optativa/eletiva na Análise
  Curricular
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=586708591
version: 2
---

## Descrição

Este parâmetro permite que as disciplinas equivalentes também sejam contabilizadas como optativas/eletivas na Análise Curricular.  
Para que o parâmetro gere efeito na análise curricular, a disciplina concluída pelo aluno deve ser cadastrada como equivalente e optativa/eletiva na matriz curricular.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **Configurador (Educacional)**, acesse **Secretaria/Geral 2/7** e Configure o parâmetro a seguir:

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
