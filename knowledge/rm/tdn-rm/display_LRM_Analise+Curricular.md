---
content_hash: 022d7607a068c6d5de8691d92e646bef3ad8d56ce5a9a12ba98c5e88cb0946dc
fetched_at: '2026-06-29T00:10:35.461669+00:00'
page_id: '528921669'
product: rm
source: tdn-rm
title: Analise Curricular
type: documentation
url: https://tdn.totvs.com/display/LRM/Analise+Curricular
version: 44
---

Índice

## **01. Análise curricular**

Esta funcionalidade permitirá ao usuário ter uma visão do currículo do aluno mediante o seu curso, com informações de cada período da matriz curricular do aluno, indicando o cumprimento ou não de cada disciplina. As disciplinas são classificadas em legendas como Concluída, Pendente e Não concluída, da seguinte forma:  
   
***Concluída***: Disciplina que o aluno cursou em regime normal, cursou equivalente ou teve um aproveitamento de estudo. Para ser considerada concluída, a situação de matrícula deve indicar que não é "É uma disciplina em curso" e "Conta como créditos cursados ou em curso". Em caso de aproveitamento de estudos, além da situação de matrícula a carga horária lançada no aproveitamento deve ser maior ou igual à carga horária da disciplina.  
   
***Pendente***: Disciplina nunca cursada pelo aluno, nunca cursada equivalente ou indicada no aproveitamento de estudos.  
   
***Não concluída***: Disciplina que o aluno já foi matriculado, mas a situação de matrícula não indica a conclusão da disciplina. Tipicamente serão os status de Matriculado, Reprovado, Trancado, Cancelado, Transferido, etc. Indica que alguma vez o aluno já fez (ou está fazendo) a disciplina, mas não concluiu. Nestes casos a situação de matrícula deve estar parametrizada como "Conta como créditos cursados ou em curso" e "É uma disciplina em curso", indica que alguma vez o aluno já fez (ou está fazendo) a disciplina, mas não concluiu.  
   
Na Análise Curricular os itens como disciplinas da matriz, disciplinas equivalentes, disciplinas optativas/eletivas, componentes curriculares, disciplinas extras e TCC são apresentados separados por blocos de informações.

### 01.01. Aproveitamento de estudo

Caso uma disciplina seja concluída por aproveitamento de estudos, o sistema irá apresentar as disciplinas de origem logo abaixo da disciplina do aproveitamento de estudos, indicando que são as disciplinas de "Origem".

### 01.02. Disciplinas equivalentes

As disciplinas equivalentes cursadas pelo aluno e que eliminam alguma disciplina obrigatória também são exibidas na Análise Curricular.

Nos parâmetros do sistema (Ambiente | Parâmetros | Educacional | Secretaria | Geral 2/7), existem alguns parâmetros que orientam a forma de exibição das disciplinas equivalentes.

Disciplinas equivalentes reprovadas serão exibidas na análise dependendo da parametrização realizada.

As disciplinas equivalentes serão exibidas tanto embaixo da disciplina da matriz, quanto no grupo de disciplinas equivalentes.

### 01.03. Disciplinas extras

As disciplinas extras cursadas pelo aluno, que não fazem parte da matriz curricular também são apresentadas na Análise Curricular.

### 01.04. Disciplinas optativas/eletivas

A exibição das disciplinas optativas/eletivas na Análise Curricular dependerá da forma como o sistema estiver parametrizado.  
Se o sistema ***estiver parametrizado* para utilizar *grupos de disciplinas***, (parâmetro do sistema "Usa grupo de disciplinas optativas/eletivas", disponível em Ambiente | Parâmetros | Educacional | Secretaria | Geral 1/7 = marcado) as disciplinas optativas/eletivas cadastradas na matriz curricular devem ser associadas à *grupos de disciplinas* e estas serão apresentadas na Análise Curricular logo abaixo do período ao qual o grupo de disciplinas foi associado ou no final da Análise Curricular para os casos em que o *grupo de disciplinas* não esteja associado a nenhum período.  
A exibição das disciplinas optativas/eletivas na Análise Curricular ainda dependerá da opção "Exibe na análise curricular?" presente dentro do cadastro dos respectivos grupos de disciplinas ao qual estão associadas.  
Se o sistema ***não estiver parametrizado*** **para utilizar *grupos de disciplinas***(parâmetro do sistema "Usa grupo de disciplinas optativas/eletivas", disponível em Ambiente|Parâmetros|Educacional|Secretaria|Geral 1/7 = desmarcado), as disciplinas optativas/eletivas cadastradas na matriz curricular serão apresentadas no final da Análise Curricular em um único bloco (no Resumo da Análise Curricular).

Caso o parâmetro exibir disciplinas optativas/eletivas pendentes na análise curricular, disponível em Ambiente | Parâmetros |Educacional | Secretaria | Geral 2/6, esteja desmarcado. O Sistema exibe somente as disciplinas optativas/eletivas que o aluno está cursando ou já concluiu. Após a definição deste parâmetro a visualização desta disciplina pelo executável, portal, book de relatórios e EducaMobile passa a seguir a regra definida pelo usuário.

Para permitir que uma disciplina seja optativa/eletiva e equivalente na analise curricular .

### 01.05. Componentes curriculares

Os Componentes curriculares são agrupados também pela modalidade, além da exibição dos valores mínimo e concluído por componente e mínimo e máximo por modalidade.

 As informações exibidas são agrupadas em três níveis.

* No primeiro nível é exibido o valor mínimo relacionado ao componente curricular e o total concluído pelo aluno;
* No próximo nível é exibido o valor mínimo e máximo relacionado à modalidade;
* No último nível são exibidas as atividades com os seus respectivos status, Concluída ou Pendente, assim como o valor dos créditos, a carga horária aproveitada e o total concluído pelo aluno em cada modalidade.

### 01.06. Disciplinas de TCC

As disciplinas cadastradas como disciplinas de TCC e cujas matrículas foram associadas ao TCC do aluno, serão mostradas no grupo TCC.

### 01.07. Atividades de Extensão

As atividades de extensão tem por objetivo atender a legislação que tange a . Quando existirem atividades de extensão será apresentada a coluna **CH Extensão** e o resumo de extensão. Atividades de extensão podem ser disciplinas com carga horária de extensão informada ou componentes curriculares de extensão.

Se alguma disciplina possuir carga horária de extensão, será mostrado o valor da carga horária na coluna **CH Extensão**.

Se algum componente curricular for de extensão, ele virá marcado como sendo de extensão e a carga horária irá aparecer na coluna **CH Extensão**.

### 01.08. Resumo

No final da Análise Curricular é apresentado o *Resumo*, onde são exibidos totalizadores para as disciplinas e componentes. A exibição ou não deste Resumo está vinculada ao parâmetro do sistema "Exibir resumo de disciplinas na análise curricular (inclusive no portal)", disponível em Ambiente | Parâmetros | Educacional | Secretaria | Geral 2/7.

Extensão

O resumo das atividades de extensão só será apresentado se existir alguma disciplina com carga horária de extensão ou algum componente de extensão na matriz curricular. A carga horária de extensão a ser cursada será 10% da carga horária da matriz curricular, conforme resolução nº7 do Conselho Nacional de Educação (CNE)/Câmara de Educação Superior (CES). Caso não seja informada a carga horária da matriz curricular, este valor será 0 (zero).

Componentes curriculares

O resumo dos componentes curriculares mostra na linha Concluídas a quantidade de horas integralizadas que foram aproveitadas, esse valor pode divergir do valor exibido anteriormente (01.05) no caso de ter algum componente com carga horária integralizada com valor superior ao limite do item curricular do componente

### 01.09. Integralização da Carga Horária

Na área de apresentação de dados da *Matriz curricular* e *TCC*, é exibida a coluna da carga horária integralizada com o respectivo valor de carga horária para as disciplinas que foram concluídas, conforme exemplificado abaixo:

São exibidos totais da carga horária integralizada por período, para o grupo de optativas quando não associadas a um período específico, para o grupo de disciplinas equivalentes e também por modalidade de atividades curriculares:

Também é exibida a informação do total de carga horária integralizada pelo aluno no curso na área de *Resumo*:

#### 01.09.01.  Cálculo da Integralização da Carga Horária

A carga horária integralizada de uma disciplina corresponde à carga horária da respectiva disciplina que foi **concluída**.

Para disciplina concluída por aproveitamento de estudo, a carga horária integralizada será a carga horária informada no campo "Carga horária" do seu respectivo aproveitamento de estudo.

Para disciplina concluída por equivalência de disciplinas, a carga horária integralizada será a carga horária da disciplina da matriz que foi concluída por equivalência e não a carga horária da disciplina efetivamente cursada.

Para atividade curricular, a carga horária integralizada será a carga horária informada no campo "CH aproveitada" da respectiva atividade.

**Não são contabilizadas na integralização de carga horária**:  a carga horária das disciplinas extras, a carga horária de disciplinas filhas, e a carga horária de atividades curriculares cujo componente curricular não está associado à matriz aplicada do aluno ou cujo componente associado não possua Item curricular cadastrado.

Caso a configuração "Utilizar carga horária de disciplinas de origem na integralização de carga horária " esteja marcada em Configurações|Parâmetros|Secretaria|Geral 2/7, o cálculo da integralização de carga horária e sua apresentação na Análise curricular terá as seguintes mudanças:

* Para disciplina concluída por equivalência de disciplinas, a carga horária integralizada será a carga horária da disciplina efetivamente cursada e não a carga horária da disciplina da matriz que foi concluída por equivalência. Na análise curricular a coluna de CH Integr. ficará vazia para ambas as disciplinas no respectivo período da disciplina concluída, e na área de disciplinas equivalentes, a coluna CH Integr. será preenchida com a carga horária da respectiva disciplina equivalente concluída:

* Para disciplina de TCC concluída por equivalência cujos dados de TCC estão associados à matricula do aluno na disciplina, na análise curricular, a coluna de CH Integralizada ficará preenchida com a carga horária da respectiva disciplina equivalente concluída na área de TCC. A disciplina de TCC equivalente concluída não será apresentada na área de disciplinas equivalentes pois o seu detalhamento é feito na área de dados do TCC.

* Para disciplina concluída por aproveitamento de estudos, a carga horária integralizada será a carga horária da disciplina de origem do aproveitamento de estudo, caso ela tenha sido cadastrada. Na análise curricular a coluna CH Integr. da disciplina da matriz concluída por aproveitamento de estudos ficará vazia, e na linha da disciplina de origem do aproveitamento de estudo será exibida na coluna  CH Integr. o valor da carga horária da disciplina de origem do aproveitamento de estudo:

* Caso o aproveitamento de estudo não tenha disciplina de origem cadastrada, a carga horária integralizada será a carga horária do respectivo aproveitamento de estudo da disciplina. Na análise curricular a coluna CH Integr. da disciplina da matriz exibirá o valor da carga horária do respectivo aproveitamento de estudo da disciplina:

### 01.10. Análise Curricular através do portal

Ao consultar a Análise Curricular tanto pelo portal quando pelo sistema, é possível que o usuário veja as informações a respeito do ENADE para cada período letivo de matrícula do aluno. A exibição ou não desta informação está vinculada ao parâmetro do sistema "Exibir informações do ENADE na análise curricular do ensino superior (inclusive no Portal)", disponível em Ambiente|Parâmetros|Educacional|Secretaria|Geral 2/7.

### 01.11. Relatório

Dentro de Análise Curricular existe a opção de *Impressão de relatório*.

## **02. Documentos relacionados**

[Aproveitamento de Estudos](https://tdn.totvs.com/x/mftbGQ)

[Disciplinas Extras](https://tdn.totvs.com/x/QvxbGQ)

[Atividades de Extensão](https://tdn.totvs.com/x/PTbuJg)

[Equivalência de Disciplinas](https://tdn.totvs.com/x/xvxbGQ)

[Relatório utilizando provedor de dados Análise Curricular](https://tdn.totvs.com/x/lmpKE)

]]>
