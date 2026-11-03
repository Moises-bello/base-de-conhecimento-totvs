---
content_hash: 8cff5cb954b4f519e8e863b754ca127e92da5b96b8fd61058a0dd3468388f07b
fetched_at: '2026-06-29T00:08:17.555005+00:00'
page_id: '255756427'
product: rm
source: tdn-rm
title: DT_Analise_Curricular_Disciplinas_OptativaEletivas
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Analise_Curricular_Disciplinas_OptativaEletivas
version: 5
---

# Analise Curricular / Disciplinas Optativas/Eletivas

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | *RM* | | |
| ****Segmento Executor:**** | *Educacional* | | |
| **Módulo:** | ***TOTVS Educacional*** | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Análise Curricular* | *Análise Curricular* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Analise Curricular / Grupo de Disciplinas Optativas/Eletivas* | Ocultar disciplinas Optativas/Eletivas pendentes na Analise Curricular | |  |  | | | |
| **Requisito (ISSUE):** | EDUEDU001-369/EDUEDU001-356 | | |
| **País:** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

 Permite que o usuário exiba ou não as disciplinas optativas/eletivas pendentes na análise curricular.

## Definição da Regra de Negócio

A analise curricular até a versão 12.1.12 exibe todas as disciplinas optativas/eletivas independente do status, desta forma são listadas as disciplinas em andamento, concluídas e pendentes. Tal situação para algumas instituições de ensino passou a representar um problema, pois a informação apresentada para o aluno exibia uma conjunto grande de disciplinas.

Com base nesta percepção foi definido nos parâmetros do TOTVS Educacional em **Configurações | Parâmetros | Secretária**a possibilidade do cliente estabelecer se na análise curricular deve-se listar as disciplinas optativas/eletivas pendentes ou ocultá-las. O parâmetro criado tem a seguinte descrição "**Exibir disciplinas optativas/eletivas pendentes na análise curricular**".

A partir da definição deste parâmetro a análise curricular que pode ser chamada pelo executável, portal, book de relatórios e EducaMobile passam a seguir a regra definida pelo cliente. Abaixo um exemplo da utilização deste parâmetro no executável

* Sistema parametrizado para exibir disciplinas optativas/eletivas pendentes na Análise Curricular:

* Executar análise Curricular:

* Todas as disciplinas optativas/eletivas são exibidas inclusive as pendentes

* Sistema parametrizado para ocultar disciplinas optativas/eletivas pendentes na Análise Curricular:

* Executar a análise curricular:

* São ocultas todas disciplinas optativas/eletivas pendentes:
