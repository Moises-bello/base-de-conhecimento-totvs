---
content_hash: 9ed011d9852afc3be14bd8dd630eb15d6e61b9dd4878aa3a7ec4bd35ce962140
fetched_at: '2026-06-29T00:06:13.124338+00:00'
page_id: '208339787'
product: rm
source: tdn-rm
title: TTIVK8_DT_Analise_Curricular
type: documentation
url: https://tdn.totvs.com/display/LRM/TTIVK8_DT_Analise_Curricular
version: 1
---

# ANÁLISE CURRICULAR

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Análise curricular* | *Análise curricular* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Equivalências* | *Equivalências.* | |
| **Cadastros Iniciais:** | *1. Cadastro de equivalência ou grupo de equivalência.*  *2. Selecionar um aluno que tenha matrícula em uma ou mais disciplinas de equivalência.*  *3. Reprovar o aluno em uma ou mais disciplinas equivalentes.* |
| **Parâmetro(s):** | *1) *Educacional | Secretaria | Geral 2/4 |* Exibir disciplinas equivalentes reprovadas na análise curricular.* |
| **Ponto de Entrada:** | *N/A.* |
| **Chamados relacionados** | *TSTA67* |
| **Requisito (ISSUE):** | *N/A.* |
| **País(es):** | *Todos.* |
| **Banco(s) de Dados:** | *Todos.* |
| **Tabelas utilizadas:** | *SPARAM.* |
| **Sistema(s) operacional(is):** | *Todos.* |
| **Versões/Release:** | *11.82.41* |

## Descrição

Criado parâmetro para permitir a visualização de disciplinas equivalentes reprovadas na análise curricular.

Com o parâmetro marcado, se o aluno for reprovado em uma disciplina equivalente, esta disciplina será visualizada abaixo da disciplina da grade.

Vale ressaltar que o status da disciplina da grade ficará como "Não concluída".

Com o parâmetro desmarcado(padrão), a disciplina equivalente reprovada não será visualizada na análise curricular.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *11.82.40.119* deste chamado.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **Configurador Educacional**, acesse **Educacional/Secretaria/Geral2/4**. Configure o(s) parâmetro(s) a seguir:

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| **Nome:** | *Exibir disciplinas equivalentes reprovadas na análise curricular* |
| **Tipo:** | *Booleano* |
| **Cont. Por.:** | *Falso* |
| **Descrição:** | *Permite habilitar/desabilitar a visualização das disciplinas equivalentes reprovadas na análise curricular.* |

## Procedimento para Utilização

**Exemplo:**

1.            No Educacional, acesse Parâmetros / Secretaria / Geral 2/4 /  e marque o parâmetro Exibir disciplinas equivalentes reprovadas na análise curricular.

2.            Acesse a visão de cadastro de alunos.

       3.            Selecione um aluno que tenha reprovado em uma ou mais disciplinas equivalentes.

       4.            Acesse o anexo de Curso/Habilitação do aluno.

Selecione uma habilitação que o aluno tenha matrículas em disciplinas equivalentes e estas estejam reprovadas.

       5.            Na visão do registro de Curso/Habilitação selecione "Análise Curricular".

       6.            Visualize a disciplina equivalente reprovada abaixo da disciplina da grade.

       7.            Esta informação também pode ser visualizada acessando o histórico no portal do aluno.
