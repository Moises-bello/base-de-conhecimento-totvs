---
content_hash: e09505021cf261096a1db795874d0c956d59bea92e5cd617f4fb84c5121a944a
fetched_at: '2026-06-29T00:08:44.902103+00:00'
page_id: '309406432'
product: rm
source: tdn-rm
title: 'DT Widget: Limite de Faltas (Novo portal do aluno)'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=309406432
version: 5
---

# LIMITE DE FALTAS (Novo Portal do aluno)

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Gestão Educacional |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Widgets | Widgets Limite de Faltas |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Digitação de faltas através da etapa;  Digitação da Frequência diária. | Digitação de Faltas;  Digitação da Frequência diária | |  |  | |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [PORTALMOBILE01-657](http://jiraproducao.totvs.com.br/browse/PORTALMOBILE01-657) |
| **País(es):** | BRA |
| **Banco(s) de Dados:** | SQL e Oracle |
| **Tabelas Utilizadas:** | SWIDGETS |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Este *Widgets* tem como objetivo exibir se o aluno está no limite de faltas por disciplina em que o mesmo esteja matriculado.

O *Widgets* será exibido apenas nos menus: Falta e Notas do aluno. Através dele, o aluno/responsável irá  visualizar um gráfico com o limite de faltas (porcentagem). Se limite NÃO excedido a cor deve ser azul e se limite excedido a cor deve ser vermelho, além disso será listado as disciplinas que o aluno está matriculado seguindo a mesma regra dos outros *Widgets*e listas de disciplinas do aluno no portal.

Ao selecionar uma disciplina, o gráfico e os dados serão atualizados automaticamente conforme a seleção da disciplina devem ser atualizados.

O cálculo a ser utilizado é o mesmo já utilizado no Totvs Educa Mobile (Resumo de disciplinas).

**‰**Percentual de faltas = (QTDE FALTAS / CARGA HORARIA) X 100.

Onde:

1. Quantidade de faltas pode ser a quantidade preenchida na etapa final ou a soma das etapas caso não tenha se preenchido a etapa final.
2. Carga horária pode ser da disciplina na grade (ensino básico) ou da disciplina (ensino superior).

## Importante

Para a exibição correta do gráfico, definir o percentual de faltas nos parâmetros do sistema em: Totvs Gestão Educacional | Configurações | Parâmetros | Secretaria | Geral 4/7.

## Procedimento para Utilização

Após a parametrização para a exibição do Widgts, acessar o Novo portal do aluno.

* **Faltas dentro do Limite**

* **Faltas fora do limite**
