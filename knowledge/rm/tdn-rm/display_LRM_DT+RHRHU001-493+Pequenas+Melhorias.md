---
content_hash: 3f9405ab35661902495f5bf917a9554db27e73c820fdf0283c11586cad3b3bf3
fetched_at: '2026-06-29T00:08:27.222836+00:00'
page_id: '271400520'
product: rm
source: tdn-rm
title: DT RHRHU001-493 Pequenas Melhorias
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+RHRHU001-493+Pequenas+Melhorias
version: 4
---

# PEQUENAS MELHORIAS / RHRHU001-493

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM | | |
| **Segmento Executor:** | Construção e Projetos | | |
| **Módulo:** | Gestão de Pessoas | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Banco de Talentos |  | | Cursos | RhuCursosAction | | Tabela Salarial | RhuTabSalariaisAction | | Avaliação de Qualidade | RhuAvaliacaoQualidadeAction | | Turmas | RhuTurmasAction | | | |
| **Chamado:** | n/a | | |
| **Requisito (ISSUE):** | RHRHU001-493 | | |
| **País:** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros:** | n/a | | |

### Objetivo

 Aplicar pequenas melhorias e correções em alguns módulos do sistema TOTVS Gestão de Pessoas.

 

* Links para vaga do Banco de Talentos

* Aumentar tamanho do campo Nome do Professor no cadastro de Turmas

* Lançamento em Lote de notas de Avaliação de Qualidade

* Melhorar o anexo de histórico da Tabela Salarial

* Melhorar funcionamento do cadastro de Curso e-learning

## Definição da Regra de Negócio

## Banco de Talentos:

* Aplicado ajuste afim de que seja possível acessar uma vaga publicada no Banco de Talentos através da aplicação direta da url no browser.
* Garantido que caso o usuário já encontre-se logado, ao acessar a url não será exigida nova autenticação.

**Cursos:**

* Quando não existir integração entre TOTVS Gestão de Pessoas X E-Learning:
  + Ao informar o código do E-Learning manualmente, será emitido um alerta e desmarcada a opção automaticamente.
  + Ao editar um curso já cadastrado, não será possível alterar o parâmetro E-Learning.

**Tabela Salarial:**

* Acertada a visualização do Histórico da Tabela Salarial

**Avaliação de Qualidade:**

* Disponibilizado o lançamento de itens de qualidade para vários participantes de uma só vez.

**Obs.:** Somente será possível realizar o Lançamento em Lote da Avaliação de Qualidade quando for para o mesmo item.

**Turmas:**

* Adequação no cadastro de Turmas para que o campo referente ao nome do Professor permita digitação de até 200 caracteres.
