---
content_hash: 1d88b7685dbce00ec8754a473e88ae39bda4bce1609d491d682b86e39a3cf203
fetched_at: '2026-06-29T00:10:56.117222+00:00'
page_id: '590628080'
product: rm
source: tdn-rm
title: Turma Livre e Curriculo Individual - Calculo por crédito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=590628080
version: 77
---

---

CalculoporcreditoturmalivreTurma Livre

Na matricula do aluno no período letivo em disciplinas de uma Turma Livre os créditos considerados para cobrança serão os valores informados no campo Créditos para cobrança da turma/disciplina.

Após realizar a matricula o valor dos créditos considerados no contrato serão o da Turma Livre.

Créditos da Matriz do Aluno

Funcionamento dos parâmetros: **Usar número de créditos financeiros da matriz curricular do aluno /****Usar valor do créditos financeiros da matriz curricular do aluno / Usar nº créditos e valor do crédito da disciplina da matriz curricular do aluno em caso de equivalência múltipla**

*Acesse: Configurações / Parâmetros / Integração / Financeiro / Fin – Geral 1/2*

Disciplina da Turma Livre ofertada na Matriz Curricular

* **Usar número de créditos financeiros da matriz curricular do aluno**

Se o sistema estiver com este parâmetro marcado, e se a disciplina matriculada for da Turma Livre e também estiver ofertada na matriz curricular do aluno deverão ser considerados o número de créditos da disciplina matriz do aluno.

* **Usar valor do créditos financeiros da matriz curricular do aluno**

Se o sistema estiver com este parâmetro marcado, e se a disciplina matriculada for da Turma Livre e também estiver ofertada na matriz curricular do aluno deverão ser considerados o valor do créditos da disciplina matriz do aluno.

Exemplo:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Disciplina Matriz do aluno** | **Nº Crédito x Valor do Crédito** |  | **Mesma Disciplina (Turma Livre)** | **Nº Crédito x Valor do Crédito** |
| Introdução a Ciência do Direito | 5  \*  100 = 500 | Introdução a Ciência do Direito | 4  \*  150 = 600 |

Nesse exemplo, quando o aluno estiver matriculado na mesma disciplina da sua matriz, mas essa disciplina pertence a Turma Livre.  
  
Com os parâmetros marcados o número de crédito e valor de crédito considerado para o aluno será da própria matriz   
**5 (Nº de Créditos por disciplina) x R$100 = RS500**Sem os parâmetros marcados o número de crédito e valor de crédito considerado para o aluno será da Turma Livre  
**4 (Nº de Créditos por disciplina) x R$150 = RS600**

Disciplinas Optativas / Eletivas

O mesmo comportamento relatado anteriormente também será aplicado caso o aluno esteja matriculado em uma turma livre que a disciplina é ofertada como optativa/eletiva na matriz curricular do aluno.

Disciplinas diferentes com equivalência

* **Usar número de créditos financeiros da matriz curricular do aluno**

Se o sistema estiver parametrizado marcado, e se a disciplina for ofertada na Turma Livre e equivaler alguma disciplina na matriz curricular do aluno, deverão ser considerados o número de créditos da disciplina matriz do aluno.

* **Usar valor do créditos financeiros da matriz curricular do aluno**

Se o sistema estiver parametrizado marcado, e se a disciplina for ofertada na Turma Livre e equivaler alguma disciplina na matriz curricular do aluno, deverão ser considerados o valor do créditos da disciplina matriz do aluno.

Exemplo:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Disciplina Matriz do aluno** | **Nº Crédito x Valor do Crédito** |  | **Disciplinas equivalentes (Turma Livre)** | **Nº Crédito x Valor do Crédito** |
| Introdução a Ciência do Direito | 5  \*  100 = 500 | Teoria Geral do Direito | 3  \*  150 = 450 |

Nesse exemplo, quando o aluno estiver matriculado na disciplina da Turma Livre que possui equivalência cadastrada com a disciplina da matriz da sua grade.

Com os parâmetros marcados o número de crédito e valor de crédito considerado para o aluno será da própria matriz   
**5 (Nº de Créditos por disciplina) x R$100 = RS500**Sem os parâmetros marcados o número de crédito e valor de crédito considerado para o aluno será da Turma Livre  
**3 (Nº de Créditos por disciplina) x R$150 = RS450**

Disciplinas diferentes com equivalência múltipla

Se o parâmetro "**Usar nº créditos e valor do crédito da disciplina da matriz curricular do aluno em caso de equivalência múltipla**", o comportamento do sistema deve ser o conforme descrito abaixo:

1. Matricula tem duas disciplinas da Turma Livre com equivalência para uma da matriz: o sistema sempre irá considerar o número de crédito e valor do crédito da disciplina da matriz. 

   |  |  |  |  |  |  |
   | --- | --- | --- | --- | --- | --- |
   | **Disciplina Matriz do aluno** | **Nº Crédito x Valor do Crédito** |  | **Disciplinas equivalentes (Turma Livre)** | **Nº Crédito x Valor do Crédito** |  |
   | Português | 5  \*  100 | Redação | 5  \*  100 = 500 | Número de créditos e valor do crédito da disciplina de português |
   |  |  | Comunicação | 0 | A segunda disciplina ficará zerada, pois o valor foi considerado na primeira disciplina equivalente. |
2. Matricula em duas disciplinas da matriz do aluno com equivalência para uma disciplinas da Turma Livre: o sistema sempre irá considerar a disciplina com maior número de crédito e a disciplina com maior valor do crédito da matriz do aluno.

   |  |  |  |  |  |  |
   | --- | --- | --- | --- | --- | --- |
   | **Disciplinas Matriz do aluno** | **Nº Crédito x Valor do Crédito** |  | **Disciplinas equivalentes (Turma Livre)** | **Nº Crédito x Valor do Crédito** |  |
   | Redação | 5  \* 500 | Português | 6 \* 500 = 3.000 | Vai prevalecer o maior valor de crédito e o maior número de crédito de cada disciplina equivalente |
   | Comunicação | 6 \* 150 |

Quando os parâmetros para considerar o **n° de crédito e valor de crédito da matriz curricular do aluno** estiver marcado e o sistema não encontre a mesma disciplina na matriz curricular do aluno, ou se o valor da disciplina na matriz do aluno não estiver preenchido, o sistema irá considerar o valor da disciplina matriculada 

Exemplo:

| **Disciplinas Matriz do aluno** | **Nº Crédito x Valor do Crédito** | **Disciplinas equivalentes (Turma Livre)** | **Nº Crédito x Valor do Crédito** |  |
| --- | --- | --- | --- | --- |
| Português | 0 | Comunicação | 4 \* 100 = 400 | Mesmo com os parâmetros para considerar o **n° de crédito e valor de crédito da matriz curricular do aluno**, no momento da matrícula, será considerado o valor da disciplina "Comunicação", já que a disciplina "Português" está zerada. |

Quando o aluno está matriculado em uma Turma Livre e possui Currículo Individual será tratado da seguinte forma:

Currículo Individual x Turma Livre

* **Usar número de créditos financeiros da matriz curricular do aluno**

Se o sistema estiver com este parâmetro marcado, e se a disciplina matriculada for da Turma Livre e também estiver ofertada no Currículo Individual do aluno deverão ser considerados o número de créditos da disciplina do Currículo Individual.

* **Usar valor do créditos financeiros da matriz curricular do aluno**

Se o sistema estiver com este parâmetro marcado, e se a disciplina matriculada for da Turma Livre e também estiver ofertada no Currículo Individual do aluno deverão ser considerados o valor do créditos da disciplina do Currículo Individual.

Exemplo:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Disciplina Matriz do aluno** | **Nº Crédito x Valor do Crédito** |  | **Mesma Disciplina (Turma Livre)** | **Nº Crédito x Valor do Crédito** |
| Introdução a Ciência do Direito | 5  \*  100 = 500 | Introdução a Ciência do Direito | 4  \*  150 = 600 |

Nesse exemplo, quando o aluno estiver matriculado na mesma disciplina do seu Currículo Individual, mas essa disciplina pertence a Turma Livre.  
  
Com os parâmetros marcados o número de crédito e valor de crédito considerado para o aluno será do próprio Currículo Individual.    
**5 (Nº de Créditos por disciplina) x R$100 = RS500**Sem os parâmetros marcados o número de crédito e valor de crédito considerado para o aluno será da Turma Livre  
**4 (Nº de Créditos por disciplina) x R$150 = RS600**

Faixa de Crédito

Funcionamento do parâmetro **Utilizar Faixa de Crédito e  **Utilizar Faixa de Crédito |**Usar número de créditos financeiros da matriz curricular do aluno**

Acesse: Configurações / Parâmetros / Integração / Financeiro / Fin – Geral 1/2

**Utilizar Faixa de Crédito**

**Utilizar Faixa de Crédito | Usar número de créditos financeiros da matriz curricular do aluno**

Disciplina da Turma Livre ofertada na Matriz Curricular

* **Usar número de créditos financeiros da matriz curricular do aluno**

Se o sistema estiver com este parâmetro marcado, e se a disciplina matriculada for da Turma Livre e também estiver ofertada na matriz curricular do aluno deverão ser considerados o número de créditos da disciplina matriz do aluno.

Exemplo:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Disciplina Matriz do aluno** | **Nº Crédito x Valor da Faixa de Crédito** |  | **Mesma Disciplina (Turma Livre)** | **Nº Crédito x Valor do Crédito** |
| Introdução a Ciência do Direito | 1  \*  500 = 500 | Introdução a Ciência do Direito | 3  \*  200 = 600 |

Nesse exemplo, quando o aluno estiver matriculado na mesma disciplina da sua matriz, mas essa disciplina pertence a Turma Livre.  
  
Com os parâmetros marcados o número de crédito e valor de crédito considerado para o aluno será da própria matriz   
**1 (Nº de Créditos por disciplina) x R$500 (Valor de Crédito da Faixa de Crédito = RS500**

Sem os parâmetros marcados o número de crédito e valor de crédito considerado para o aluno será da Turma Livre  
**3 (Nº de Créditos por disciplina) x R$200 = RS600**

Disciplinas diferentes com equivalência

* **Usar número de créditos financeiros da matriz curricular do aluno**

Se o sistema estiver parametrizado marcado, e se a disciplina for ofertada na Turma Livre e equivaler alguma disciplina na matriz curricular do aluno, deverão ser considerados o número de créditos da disciplina matriz do aluno.

Exemplo:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Disciplina Matriz do aluno** | **Nº Crédito x Valor da Faixa de Crédito** |  | **Disciplinas equivalentes (Turma Livre)** | **Nº Crédito x Valor do Crédito** |
| Introdução a Ciência do Direito | 1  \*  500 = 500 | Teoria Geral do Direito | 4  \*  150 = 600 |

Nesse exemplo, quando o aluno estiver matriculado na disciplina da Turma Livre que possui equivalência cadastrada com a disciplina da matriz da sua grade.

Com os parâmetros marcados o número de crédito e valor de crédito considerado para o aluno será da própria matriz   
**1 (Nº de Créditos por disciplina) x R$500 (Valor de Crédito da Faixa de Crédito = RS500**

Sem os parâmetros marcados o número de crédito e valor de crédito considerado para o aluno será da Turma Livre  
**4 (Nº de Créditos por disciplina) x R$150 = RS600**

Para mais informações sobre o cadastro de Faixa de Crédito, [clique aqui.](http://tdn.totvs.com)

currículoindividualCurrículo Individual

No **currículo individual (CI)**a Instituição de Ensino Superior (IES) pode personalizar um modelo de matriz curricular específico para cada aluno, onde será determinado varias informações da matriz curricular.

Um dos campos que podem ser preenchidos são créditos financeiros e valor do crédito para cobrança que terão o mesmo comportamento dos campos que existe na matriz curricular do aluno. 

Quando um aluno possui Currículo Individual esse será considerado a matriz oficial do aluno, então para que os valores de créditos e números de créditos busquem do Currículo Individual os parâmetros **Usar número de créditos financeiros da matriz curricular do aluno e****Usar valor do créditos financeiros da matriz curricular do aluno** precisam estar marcados, caso ao contrario serão considerados os valores de créditos e números de créditos da matriz curricular do Curso/Habilitação do aluno.

Parâmetro Créditos da Matriz do Aluno

Funcionamento dos parâmetros: **Usar número de créditos financeiros da matriz curricular do aluno /****Usar valor do créditos financeiros da matriz curricular do aluno / Usar nº créditos e valor do crédito da disciplina da matriz curricular do aluno em caso de equivalência múltipla**

*Acesse: Configurações / Parâmetros / Integração / Financeiro / Fin – Geral 1/2*

Mesma disciplina em matriz diferente

* **Usar número de créditos financeiros da matriz curricular do aluno**

Se o sistema estiver com este parâmetro marcado, e a disciplina matriculada for de outra grade e também estiver ofertada no Currículo Individual (matriz do aluno) do aluno, deverão ser considerados o número de créditos da disciplina do Currículo Individual.

* **Usar valor do créditos financeiros da matriz curricular do aluno**

Se o sistema estiver com este parâmetro marcado, e a disciplina matriculada for de outra grade e também estiver ofertada no Currículo Individual (matriz do aluno) do aluno, deverão ser considerados o valor do créditos da disciplina do Currículo Individual.

Exemplo:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Disciplina Matriz do aluno (Currículo Individual)** | **Nº Crédito x Valor do Crédito** |  | **Mesma Disciplina (fora da grade do aluno)** | **Nº Crédito x Valor do Crédito** |
| Introdução a Ciência do Direito | 5  \*  100 = 500 | Introdução a Ciência do Direito | 4  \*  150 = 600 |

Nesse exemplo, quando o aluno estiver matriculado na mesma disciplina da outra grade, mas essa disciplina pertence também a seu Currículo Individual (matriz do aluno)  
  
Com os parâmetros marcados o número de crédito e valor de crédito considerado para o aluno será do Currículo Individual.   
**5 (Nº de Créditos por disciplina) x R$100 = RS500**Sem os parâmetros marcados o número de crédito e valor de crédito considerado para o aluno será da outra grade   
**4 (Nº de Créditos por disciplina) x R$150 = RS600**

Quando o aluno está matriculado em uma Turma Livre e possui Currículo Individual será tratado da seguinte forma:

Currículo Individual x Turma Livre

* **Usar número de créditos financeiros da matriz curricular do aluno**

Se o sistema estiver com este parâmetro marcado, e se a disciplina matriculada for da Turma Livre e também estiver ofertada no Currículo Individual (matriz do aluno) deverão ser considerados o número de créditos da disciplina do Currículo Individual.

* **Usar valor do créditos financeiros da matriz curricular do aluno**

Se o sistema estiver com este parâmetro marcado, e se a disciplina matriculada for da Turma Livre e também estiver ofertada no Currículo Individual (matriz do aluno) deverão ser considerados o valor do créditos da disciplina do Currículo Individual.

Exemplo:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Disciplina Matriz do aluno (Currículo Individual)** | **Nº Crédito x Valor do Crédito** |  | **Mesma Disciplina (Turma Livre)** | **Nº Crédito x Valor do Crédito** |
| Introdução a Ciência do Direito | 5  \*  100 = 500 | Introdução a Ciência do Direito | 4  \*  150 = 600 |

Nesse exemplo, quando o aluno estiver matriculado na mesma disciplina do seu Currículo Individual, mas essa disciplina pertence a Turma Livre.  
  
Com os parâmetros marcados o número de crédito e valor de crédito considerado para o aluno será do próprio Currículo Individual.    
**5 (Nº de Créditos por disciplina) x R$100 = RS500**Sem os parâmetros marcados o número de crédito e valor de crédito considerado para o aluno será da Turma Livre  
**4 (Nº de Créditos por disciplina) x R$150 = RS600**
