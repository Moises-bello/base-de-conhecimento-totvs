---
content_hash: 21ba7822138e0bc569464deb7e343ba119696dc0f546f58bd710ab3c42421a00
fetched_at: '2026-06-29T00:06:06.947039+00:00'
page_id: '201733556'
product: rm
source: tdn-rm
title: DT_Plano_Atividade_Etapas_Estagio
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Plano_Atividade_Etapas_Estagio
version: 10
---

# Plano de atividade e etapas do plano de atividade

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Totvs Educacional |
| **Módulo:** | Educacional |

## Descrição

O fluxo do processo de aprovação do plano de atividade e suas etapas foi alterado para que se tenha a opção de solicitar a aprovação do Supervisor do estágio (funcionário da empresa). Com isso foram criadas duas novas situações (Pendente Supervisor e Pendente Orientador)

**Solicitar aprovação do plano de atividade ao Supervisor:**

Foi criado um novo parâmetro (vide parâmetro 1), que define se quando o orientador realizar a aprovação do plano de atividade e etapas do aluno, o supervisor do estágio também deverá realizar a aprovação.

O processo de aprovação deverá seguir o seguinte fluxo:

* Parâmetro desmarcado: Depois que o aluno solicitar a aprovação do plano, o professor orientador tem a opção aprovar/reprovar, voltando a solicitação para o aluno.
* Parâmetro marcado: Depois que o aluno solicitar a aprovação do plano, o professor orientador tem a opção de aprovar/reprovar. Caso ele realiza a aprovação, o plano é direcionado para o supervisor realizar aprovação/reprovação. Mas caso o professor orientador reprove, o fluxo deve retornar para o aluno realizar os ajustes necessários.

O Supervisor do estágio aprova/reprova o plano de atividade e suas etapas, através do portal no menu Administração | Estágio/Emprego | Plano de atividade.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **Totvs Educacional**, acesse **Configurações/Parâmetros/Estágio (Estágio 5/7)**.

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| **Nome:** | Solicitar aprovação do plano de atividade e etapas ao supervisor. |
| **Tipo:** | Booleano (True/False) |
| **Cont. Por.:** | False |
| **Descrição:** | Esse parâmetro definirá se será necessário o plano de atividade e suas etapas, passar por uma aprovação do Supervisor (funcionário da empresa). |
