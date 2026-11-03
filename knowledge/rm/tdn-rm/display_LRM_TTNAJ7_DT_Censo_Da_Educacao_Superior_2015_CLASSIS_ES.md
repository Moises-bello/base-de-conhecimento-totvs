---
content_hash: 23ca4f552c915d057d64bfb8e69c4dd7071a50824f0867e02f590e82ae47e50c
fetched_at: '2026-06-29T00:06:24.295626+00:00'
page_id: '224116097'
product: rm
source: tdn-rm
title: TTNAJ7_DT_Censo_Da_Educacao_Superior_2015_CLASSIS_ES
type: documentation
url: https://tdn.totvs.com/display/LRM/TTNAJ7_DT_Censo_Da_Educacao_Superior_2015_CLASSIS_ES
version: 119
---

# CENSO DA EDUCAÇÃO SUPERIOR 2015 (CLASSIS\_ES)

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | **RM** |
| **Segmento:** | ****Educacional**** |
| **Módulo:** | *****Totvs Gestão Educacional***** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | **Censo da Educação Superior** | **Censo da Educação Superior** |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | ****Geração de Dados do Censo**** | ***Geração de Dados do Censo*** | |  |  | |
| **Cadastros Iniciais:** | *Cadastro de Carga Horária da Grade dos alunos*  **Cadastro de Carga Horária das Disciplinas dos alunos** |
| **Parâmetro(s):** | **N/A** |
| **Ponto de Entrada:** | **N/A** |
| **Chamados Relacionados** | *TUCX92* |
| **Requisito (ISSUE):** | **N/A** |
| **País(es):** | ***Brasil*** |
| **Banco(s) de Dados:** | **SQL Server e Oracle** |
| **Tabelas Utilizadas:** | **UALUNOCURSOMEC** |
| **Sistema(s) Operacional(is):** | **Windows 7** |

## Descrição

Foram feitas as alterações para o Censo da Educação Superior 2015, conforme leiaute disponibilizado pelo INEP.

O INEP agora quer que sejam enviadas (no arquivo do Censo) as seguintes informações de carga horária:

**Carga horária total do curso por aluno:** Somatório do total da carga horária dos componentes curriculares que fazem parte da matriz do curso. Cada aluno poderá possuir uma carga horária total a depender do currículo que ele deva integralizar.

**Carga horária integralizada pelo aluno:** Somatório da carga horária dos componentes curriculares que o aluno tenha aproveitado e que fazem parte da matriz do curso.

Para que seja possível pegar essas informações corretamente, é necessário que elas estejam cadastradas no sistema.

Então, a Carga Horária de todas as disciplinas dos cursos que sairão no Censo devem ser informadas:

Caso fique faltando alguma informação de carga horária para algum aluno que sairá no Censo, será mostrado isso em um dos passos da tela de preparação dos dados para o censo superior:

Não será permitido avançar no assistente sem informar todas as cargas horárias que estão faltando.

Ao prosseguir na tela de preparação dos dados do censo e mandar gerar, será feito o cálculo de carga horária integralizada para cada aluno. Essa informação sairá no arquivo gerado pelo relatório do Censo, junto com a carga horária do curso, conforme leiaute do INEP:

[edu\_superior\_migracao\_arquivo\_aluno.xls](http://tdn.totvs.com/download/attachments/223916728/edu_superior_migracao_arquivo_aluno.xls?version=3&modificationDate=1452792579000&api=v2)

divs
