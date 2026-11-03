---
content_hash: 0084b9faaa86418e6e4e99ae202107ecdbc22de37cd4d55135997349a4b2573d
fetched_at: '2026-06-29T00:10:53.199018+00:00'
page_id: '577913258'
product: rm
source: tdn-rm
title: Soma dos Créditos Acadêmicos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=577913258
version: 4
---

## Descrição

Crédito acadêmico é uma unidade de medida utilizada para medir o avanço do estudante ao longo do curso. Os cursos determinam um mínimo e um máximo de créditos para que o estudante possa se graduar. Cada disciplina (obrigatória, optativa e/ou eletiva) pode oferecer um número diferente de créditos, de acordo com a carga horária. Esta unidade está presente apenas no **Ensino Superior**.

As regras descritas abaixo passam a valer a partir das versões: 12.1.27.314, 12.1.28.222, 12.1.29.153 e 12.1.31.

## Ensino Superior

No ensino superior o número de créditos vai ser somado ao total daquela período letivo se a disciplina matriculada possuir em sua situação de matrícula **marcado** o parâmetro **conta como crédito cursados ou em curso**. Caso esteja adicionando uma disciplina pela sugestão de disciplinas, esta disciplina sempre será somada ao total de créditos do período letivo.

### **Matrícula on-line no ensino superior - Portal do Aluno**

No portal do aluno também deverá ter na situação de matrícula o parâmetro **conta como crédito cursados ou em curso**marcado, mas é necessário atenção ao parâmetro **não altera a situação de matrícula na disciplina (apenas para matrícula on-line)**, pois se ele estiver **marcado** a situação de matrícula a ser considerada da disciplina será a de entrada, ou seja, a situação de matrícula atual da disciplina, caso o aluno já esteja matriculado na disciplina. Caso ele não esteja matriculado irá ocorre a soma dos créditos. Entretanto se este parâmetro estiver **desmarcado** a situação de matrícula a ser considerada, será a de saída, ou seja, a situação de matrícula parametrizada nos parâmetros em Configurações | Parâmetros |  RM Portal - Matrícula | Primeira aba.
