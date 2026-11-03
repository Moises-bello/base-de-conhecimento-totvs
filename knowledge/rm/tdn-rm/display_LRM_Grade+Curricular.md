---
content_hash: f792051c6f5fe9295cd75c24fec3c72ddc9e22038f15b8607cf617ac27d1db3a
fetched_at: '2026-06-29T00:08:37.591393+00:00'
page_id: '284880193'
product: rm
source: tdn-rm
title: Grade Curricular
type: documentation
url: https://tdn.totvs.com/display/LRM/Grade+Curricular
version: 17
---

Este Menu está disponível apenas para o contexto ENSINO SUPERIOR.

Através do menu Grade Curricular, o aluno poderá acompanhar o andamento do curso e a situação de cada disciplina ou componentes curriculares.

## **Classificação das disciplinas**

As disciplinas serão classificadas com sinal conforme seu status.

Concluída (sinal verde): Disciplina que o aluno cursou, cursou equivalente ou teve um aproveitamento de estudo. Para ser considerada concluída, a situação de matrícula deve indicar que, não é uma disciplina em curso, indica como resultado final, indica Status na disciplina, e conta como créditos cursados ou em curso.

Pendente (Ícone vermelho): Disciplina nunca cursada pelo aluno, nunca cursada equivalência ou indicada no aproveitamento de estudos.

Não concluída (Ícone amarelo): Disciplina que o aluno já foi matriculado mas a situação de matrícula não indica a conclusão da disciplina. Tipicamente são os status de Matriculado, Reprovado, Trancado, Cancelado, Transferido, etc. Indica que alguma vez o aluno já fez (ou esta fazendo) a disciplina mas não concluiu

Equivalente (ícone azul): Caso a disciplina seja concluída por aproveitamento de estudos. As disciplinas de origem são apresentadas logo abaixo da disciplina do aproveitamento de estudos, indicando que são as disciplina de "Origem" e equivalente.

Para melhor visualização, o portal irá apresentar essas informações em abas e sub-abas, conforme descrito abaixo:

## **Aba Todos**

* Todas  
  Serão apresentadas todas as disciplinas da grade curricular do aluno (obrigatórias, eletivas/optativas, equivalentes e componentes curriculares). Independente do status.
* Obrigatórias:  
  Serão exibidas todas as disciplinas da grade curricular do aluno obrigatórias de serem cursadas. Independente do status.
* Eletivas/Optativas:  
  Serão exibidas todas as disciplinas da grade curricular do aluno que são eletivas ou optativas. Independente do status.
* Disciplinas Equivalentes:  
  Serão exibidas todas as disciplinas da grade curricular do aluno que são equivalentes. Independente do status.
* Componentes Curriculares:  
  Serão exibidas todos os componentes curriculares vinculados ao aluno. Independente do status.

## **Aba Em curso**

* Todas  
  Serão apresentadas todas as disciplinas da grade curricular do aluno (obrigatórias, eletivas/optativas, equivalentes e componentes curriculares). Que estão sendo cursadas.
* Obrigatórias  
  Serão exibidas todas as disciplinas da grade curricular do aluno obrigatórias, que estão sendo cursadas
* Eletivas/Optativas  
  Serão exibidas todas as disciplinas da grade curricular do aluno que são eletivas ou optativas, que estão sendo cursadas
* Disciplinas Equivalentes  
  Serão exibidas todas as disciplinas da grade curricular do aluno que são equivalentes, cursadas que eliminaram alguma disciplina obrigatória
* Componentes Curriculares  
  Serão exibidas todos os componentes curriculares vinculados ao aluno que estão em curso.

## **Aba Pendentes**

* Todas  
  Serão apresentadas todas as disciplinas da grade curricular do aluno (obrigatórias, eletivas/optativas, equivalentes e componentes curriculares). Que estão pendentes para serem cursadas.
* Obrigatórias  
  Serão exibidas todas as disciplinas da grade curricular do aluno obrigatórias, que estão sendo pendentes de serem cursadas
* Eletivas/Optativas  
  Serão exibidas todas as disciplinas da grade curricular do aluno que são eletivas ou optativas, que estão pendentes de serrem cursadas
* Componentes Curriculares  
  Serão exibidas todos os componentes curriculares vinculados ao aluno que estão pendentes para serem cursados.

## **Aba Concluídos**

* Todas  
  Serão apresentadas todas as disciplinas da grade curricular do aluno (obrigatórias, eletivas/optativas, equivalentes e componentes curriculares). Que estão já foram finalizadas.
* Obrigatórias  
  Serão exibidas todas as disciplinas da grade curricular do aluno obrigatórias, que estão já se encontram concluídas.
* Eletivas/Optativas  
  Serão exibidas todas as disciplinas da grade curricular do aluno que são eletivas ou optativas, já concluídas
* Disciplinas Equivalentes  
  Serão exibidas todas as disciplinas da grade curricular do aluno que são equivalentes, que já foram concluídas
* Componentes Curriculares  
  Serão exibidas todos os componentes curriculares vinculados ao aluno que já foram finalizados.

Observações:

Existe a possibilidade ocultar as disciplinas optativas/eletivas não cursadas na grade curricular do aluno, basta desmarcar o parâmetro "Exibir disciplinas optativas/eletivas pendentes na análise curricular" (**Configurações |Parâmetros | Secretária | Geral 2/7**)

 -As disciplinas equivalentes em que o aluno foi reprovado, não são exibidas na análise curricular. Nesta situação, a disciplina da grade permanece com seu status de Pendente.

-Caso uma disciplina possua mais de um grupo de equivalência e caso o aluno esteja "em curso" nas disciplinas dos dois grupos, a análise curricular irá exibir, logo abaixo da disciplina da matriz, as disciplinas do grupo de equivalência que tiverem a menor data de matrícula, ou seja, a matrícula mais antiga.

-Caso uma disciplina Optativa/Eletiva seja equivalente a uma disciplina da grade do aluno, para fins de cálculo de carga horária, créditos ou número de disciplinas, o sistema considera somente a disciplina da Grade.

Exemplo:

Disciplina Optativa X é equivalente à disciplina D da grade do aluno.

Conforme as regras de equivalência, se o aluno estiver aprovado em X terá concluído a D por equivalência. Contudo, o total de disciplinas Optativas concluídas continuará com 0 (zero), pois X é equivalente a D.

## **Resumo**

O usuário poderá parametrizar para que seja exibido o resumo na analise curricular para o aluno, basta marcar o parâmetro do Educacional chamado "Exibir resumo de disciplinas na análise curricular (inclusive no portal)". Este parâmetro está localizado em **Configurações | Parâmetros | Secretaria | Geral 2/7.**

Optando por essa parametrização, o portal exibirá o resumo dos grupos (Disciplinas e Componentes).

A partir da versão 12.1.29 também será possível parametrizar a exibição das informações sobre a integralização mínima do curso do aluno, para isso deve-se marcar o parâmetro "Habilita a integralização de curso" localizado em Configurações | Parâmetros | Secretária | Geral 6/6.

Com essa opção parametrizada será exibido mais um quadro informativo na parte de resumo da grade curricular.

A partir das versões 12.1.31.276, 12.1.32.224, 12.1.33.152 e 12.1.34, com todos os scripts executados, se alguma disciplina possuir carga horária de extensão e/ou algum componente curricular se de extensão o resumo terá mais um quadro contendo o totalizador de extensão.

## **Disciplinas Obrigatórias**

O resumo da disciplinas obrigatórias apresentará a quantidade de disciplinas obrigatórias de serem cursadas, quantas já foram concluídas e quantas ainda estão pendentes.

## **Disciplinas Optativas**

O resumo das disciplinas optativas será exibido conforme parametrização do Educacional **Currículo e Oferta | Matrizes Curriculares |Tipo de avaliação das disciplinas optativas.**Podendo ser por carga horária, crédito ou quantidade.

## **Disciplinas Eletivas**

O resumo das disciplinas eletivas também será exibido conforme parametrização do Educacional **Currículo e Oferta | Matrizes Curriculares |Tipo de avaliação das disciplinas eletivas.**Podendo ser por carga horária, crédito ou quantidade.

## **Componentes Curriculares**

O resumo dos componentes curriculares também será apresentado conforme parametrização do Educacional  **Currículo e Oferta | Matrizes Curriculares |Tipo de avaliação das atividades curriculares.**Podendo ser por carga horária ou crédito.

## **Extensão**

A carga horária de extensão a ser cursada será 10% da carga horária da matriz curricular, conforme resolução nº7 do Conselho Nacional de Educação (CNE)/Câmara de Educação Superior (CES). Caso não seja informada a carga horária da matriz curricular, este valor será 0 (zero).

A partir das versões 12.1.31.276, 12.1.32.224, 12.1.33.152 e 12.1.34, com todos os scripts executados, quando existirem atividades de extensão será apresentada a coluna **CH Extensão** e o resumo de extensão.

Atividades de extensão serão disciplinas com carga horária de extensão informada ou componentes curriculares de extensão.

Se alguma disciplina possuir carga horária de extensão, será mostrado o valor da carga horária na coluna **CH Extensão**.

Se algum componente curricular for de extensão, ele virá marcado como sendo de extensão e a carga horária irá aparecer na coluna **CH Extensão**.

## **Integralização da Carga Horária**

Na área de apresentação de dados da *Matriz curricular* e *TCC*, é exibida a coluna da carga horária integralizada com o respectivo valor de carga horária para as disciplinas que foram concluídas, conforme exemplificado abaixo:

São exibidos totais da carga horária integralizada por período, para o grupo de optativas quando não associadas a um período específico, para o grupo de disciplinas equivalentes e também por modalidade de atividades curriculares:

Também é exibida a informação do total de carga horária integralizada pelo aluno no curso na área de *Resumo*:

### Cálculo da Integralização da Carga Horária

Os detalhes do cálculo da integralização da carga horária e a parametrização que interfere neste cálculo estão descritos em: [Cálculo da Integralização da Carga Horária](https://tdn.totvs.com/display/public/LRM/Analise+Curricular#AnaliseCurricular-01.09.01.C%C3%A1lculodaIntegraliza%C3%A7%C3%A3odaCargaHor%C3%A1ria)
