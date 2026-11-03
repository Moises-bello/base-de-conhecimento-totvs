---
content_hash: cba77eb9c7b9f30120a2384523d18b944cf37804b998d7e230b6bdae6bfec44b
fetched_at: '2026-06-29T00:06:22.416145+00:00'
page_id: '223916728'
product: rm
source: tdn-rm
title: TTIN22_DT_Censo_Da_Educacao_Superior_2015
type: documentation
url: https://tdn.totvs.com/display/LRM/TTIN22_DT_Censo_Da_Educacao_Superior_2015
version: 127
---

# CENSO DA EDUCAÇÃO SUPERIOR 2015

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | ***Educacional*** |
| **Módulo:** | ***Totvs Gestão Educacional*** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Censo da Educação Superior* | **Censo da Educação Superior** |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Geração de Dados do Censo** | **Geração de Dados do Censo** | | **Geração de Arquivo do Censo** | Geração de Arquivo do Censo | |
| **Cadastros Iniciais:** | *Cadastro de Carga Horária da Grade dos alunos*  *Cadastro de Carga Horária das Disciplinas dos alunos* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | *TTZLRW, TTPJV9* |
| **Requisito (ISSUE):** | *N/A* |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Tabelas Utilizadas:** | *SALUNOCURSOMEC* |
| **Sistema(s) Operacional(is):** | *Windows 7* |
| **Versões/Release:** | *12.1.9, 11.83.55, 11.82.43, 11.82.42* |
| **Versão Corrigida:** | *N/A* |
| **Versão Expedida:** | *N/A* |

## Descrição

Foram feitas as alterações para o Censo da Educação Superior 2015, conforme leiaute disponibilizado pelo INEP.

O INEP agora quer que sejam enviadas (no arquivo do Censo) as seguintes informações de carga horária:

**Carga horária total do curso por aluno:** Somatório do total da carga horária dos componentes curriculares que fazem parte da matriz do curso. Cada aluno poderá possuir uma carga horária total a depender do currículo que ele deva integralizar.

**Carga horária integralizada pelo aluno:** Somatório da carga horária dos componentes curriculares que o aluno tenha aproveitado e que fazem parte da matriz do curso.

Para que seja possível pegar essas informações corretamente, é necessário que elas estejam cadastradas no sistema.

Então, a Carga Horária da Matriz Curricular do aluno deve estar informada:

A Carga Horária das disciplinas que compõem a grade do aluno também devem estar informadas:

Caso fique faltando alguma informação de carga horária para algum aluno que sairá no Censo, será mostrado isso em um dos passos da tela de preparação dos dados para o censo superior:

Não será permitido avançar no assistente sem informar todas as cargas horárias que estão faltando.

Para facilitar o ajuste das informações, foi criado um botão na frente de cada registro da tela, que irá direcionar para o lugar correto onde deve ser colocado a carga horária.

Ao prosseguir na tela de preparação dos dados do censo e mandar gerar, será feito o cálculo de carga horária integralizada para cada aluno. Essa informação sairá no arquivo gerado pelo relatório do Censo, junto com a carga horária do curso, conforme leiaute do INEP:

divs
