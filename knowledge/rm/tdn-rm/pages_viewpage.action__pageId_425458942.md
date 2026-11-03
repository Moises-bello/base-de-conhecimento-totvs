---
content_hash: 3dd2e2cf1f022a25e74d1c8235769a4d3352c2d7a4b7c088cd4a1f406b8546dd
fetched_at: '2026-06-29T00:09:33.242336+00:00'
page_id: '425458942'
product: rm
source: tdn-rm
title: Choque de horários na matrícula
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458942
version: 8
---

## Descrição

O choque de horário sempre deverá ocorrer quando um horário de uma disciplina estiver dentro de um intervalo de horário de uma outra disciplina, termo de compromisso de estágio e atividades curriculares.

As regras descritas abaixo passam a valer a partir das versões: 12.1.27.314, 12.1.28.222, 12.1.29.153 e 12.1.31.

## Ensino Básico

No ensino básico o choque vai acontecer se a disciplina matriculada possuir em sua situação de matrícula **marcado** o parâmetro **conta como aluno matriculado na turma**. Na alteração de situação de matrícula somente será validado o choque se a situação de matrícula atual estiver **desmarcado**o parâmetro **conta como aluno matriculado na turma**e na situação nova o mesmo estiver **marcado**.

### **Rematrícula no ensino básico - Novo Portal do Aluno**

No portal do aluno também deverá ter na situação de matrícula o parâmetro **conta como aluno matriculado na turma**marcado, mas é necessário atenção ao parâmetro **não altera a situação de matrícula na disciplina (apenas para matrícula on-line)**, pois se ele estiver **marcado** a situação de matrícula a ser considerada da disciplina será a de entrada, ou seja, a situação de matrícula atual da disciplina, caso o aluno já esteja matriculado na disciplina. Entretanto se este parâmetro estiver **desmarcado** a situação de matrícula a ser considerada, será a de saída, ou seja, a situação de matrícula parametrizada nos parâmetros em Configurações | Parâmetros |  RM Portal - Matrícula | Primeira aba.

## Ensino Superior

No ensino superior o choque vai acontecer se a disciplina matriculada possuir em sua situação de matrícula **marcado** o parâmetro **conta como aluno matriculado na turma**ou **é uma disciplina em curso**. Na alteração de situação de matrícula somente será validado o choque se a situação de matrícula atual estiverem **desmarcados**os parâmetros **conta como aluno matriculado na turma** e **é uma disciplina em curso**e na situação nova estiver **marcado**um dos parâmetros citados marcado.

### **Matrícula on-line no ensino superior - Novo Portal do Aluno**

No portal do aluno também deverá ter na situação de matrícula o parâmetro **conta como aluno matriculado na turma**ou **é uma disciplina em curso**marcado, mas é necessário atenção ao parâmetro **não altera a situação de matrícula na disciplina (apenas para matrícula on-line)**, pois se ele estiver **marcado** a situação de matrícula a ser considerada da disciplina será a de entrada, ou seja, a situação de matrícula atual da disciplina, caso o aluno já esteja matriculado na disciplina. Entretanto se este parâmetro estiver **desmarcado** a situação de matrícula a ser considerada, será a de saída, ou seja, a situação de matrícula parametrizada nos parâmetros em Configurações | Parâmetros |  RM Portal - Matrícula | Primeira aba.

## Algumas situações no RM.exe

Nível de ensino: **Graduação**

Turma/Disciplina: 1 (Direito Penal I)

|  |  |
| --- | --- |
| **Dia** | **Horário** |
| Segunda | 19:00 - 20:40 |
| Quarta | 19:00 - 20:40 |

Turma/Disciplina: 2 (Gestão de Processos)

|  |  |
| --- | --- |
| **Dia** | **Horário** |
| Quarta | 19:00 - 20:40 |
| Sexta | 19:00 - 20:40 |

Pode existir interseção de horários, usando o exemplo acima.

| Dia | Horário | Disciplina |
| --- | --- | --- |
| Segunda-Feira | 07:00 - 07:40 | Direito Penal I |
| Segunda-Feira | 07:10 - 07:50 | Gestão de Processos |

Se o usuário optar por utilizar a **sugestão de disciplina** no processo de matricular aluno no RM, será informado as situações onde as disciplinas possuem choque de horário, pitando as disciplinas de vermelho.

Nos parâmetros do sistema existe um parâmetro que indica *"Matricula em disciplina com conflito de horário".* Nos parâmetros educacionais do perfil de usuário do RM existe outro parâmetro: *"Matricular alunos com choque de horário".*

* **Situação 1**: aluno realiza matrícula pelo Portal.

 - Não possui permissão via perfil para matricular com choque de horários.  
 - Parâmetro ***"Matricula em disciplina com conflito de horário"* desmarcado.**  
   
Aluno irá realizar a matricula nas duas turmas/disciplinas acima: *Direito Penal* I e *Gestão de Processos*.  
   
**Resultado:** sistema não irá permitir a matricula por que há conflito de horários entre as disciplinas:  
   
Turma/Disciplina: 1 (Direito Penal I)

|  |  |
| --- | --- |
| **Dia** | **Horário** |
| Quarta | 19:00 - 20:40 |
| Sexta | 19:00 - 20:40 |

Turma/Disciplina: 2 (Gestão de Processos)

|  |  |
| --- | --- |
| **Dia** | **Horário** |
| Segunda | 19:00 - 20:40 |
| Quarta | 19:00 - 20:40 |

* **Situação 2**: aluno realiza matrícula pelo Portal.

 - Não possui permissão via perfil para matricular com choque de horários.  
 - Parâmetro ***"Matricula em disciplina com conflito de horário"* marcado.**  
   
Aluno irá realizar a matricula nas duas turmas/disciplinas acima: *Direito Penal* I e *Gestão de Processos*.  
   
**Resultado:** sistema irá permitir a matricula do aluno mesmo com o conflito de horários. Ele será notificado de que as disciplinas selecionadas possuem conflito de horários.  
   
Turma/Disciplina: 1 (Direito Penal I)

|  |  |
| --- | --- |
| **Dia** | **Horário** |
| Quarta | 19:00 - 20:40 |
| Sexta | 19:00 - 20:40 |

Turma/Disciplina: 2 (Gestão de Processos)

|  |  |
| --- | --- |
| **Dia** | **Horário** |
| Segunda | 19:00 - 20:40 |
| Quarta | 19:00 - 20:40 |

* **Situação 3**: aluno realiza matrícula pela secretaria da instituição**.**

 - Usuário logado no sistema que irá realizar a matricula do aluno possui permissão via perfil para matricular com choque de horários.  
 - Parâmetro ***"Matricula em disciplina com conflito de horário"* desmarcado.**  
   
A matrícula será realizada nas duas turmas/disciplinas acima: *Direito Penal I* e *Gestão de Processos*.  
   
**Resultado:** sistema irá permitir a matrícula do aluno, entretanto, irá informar ao usuário de que ele irá matricular o aluno em turmas/disciplinas com conflito de horários. Uma confirmação será solicitada para dar continuidade.  
   
Vamos supor agora, que haverá um outro nível de ensino com as seguintes disciplinas:  
   
Nível de ensino: **Pós- Graduação Lato Sensu**  
Turma/Disciplina: 3 (Inovação e Tomada de Decisão)

|  |  |
| --- | --- |
| **Dia** | **Horário** |
| Segunda | 19:00 - 20:40 |
| Terça | 19:00 - 20:40 |

Turma/Disciplina: 4 (Negociação e Comunicação)

|  |  |
| --- | --- |
| **Dia** | **Horário** |
| Quinta | 19:00 - 20:40 |
| Sábado | 09:00 - 12:30 |

Além do parâmetro *"Matricula em disciplina com conflito de horário",* existe ainda outro parâmetro: *"Considerar conflito de horário de disciplinas em diferentes níveis de ensino".*

* **Situação 4**: aluno realiza matrícula pelo Portal.

 - Não possui permissão via perfil para matricular com choque de horários.  
 - Parâmetro ***"Matricula em disciplina com conflito de horário"*** desmarcado**.**  
**-** Parâmetro **"*Considerar conflito de horário de disciplinas em diferentes níveis de ensino*"** marcado.  
   
Aluno irá realizar a matricula nas duas turmas/disciplinas: '*Inovação e Tomada de Decisão'*e '*Negociação e Comunicação'* no nível de ensino Pós- Graduação Lato Senso*.* Considere que ele já tenha matrícula nas disciplinas de '*Direito Penal I'* e '*Gestão de Processos' do* nível de ensino Graduação.  
   
**Resultado:** sistema não irá permitir a matricula por que irá indicar conflito das seguintes disciplinas em seus respectivos níveis:  
   
Nível de ensino: **Graduação**  
Turma/Disciplina: 1 (Direito Penal I)

|  |  |
| --- | --- |
| **Dia** | **Horário** |
| Segunda | 19:00 - 20:40 |
| Quarta | 19:00 - 20:40 |

Nível de ensino: **Pós- Graduação Lato Sensu**

Turma/Disciplina: 3 (Inovação e Tomada de Decisão)

|  |  |
| --- | --- |
| **Dia** | **Horário** |
| Segunda | 19:00 - 20:40 |
| Terça | 19:00 - 20:40 |

* **Situação 5**: aluno realiza matrícula pelo Portal.

 - Não possui permissão via perfil para matricular com choque de horários.  
 - Parâmetro ***"Matricula em disciplina com conflito de horário"*** marcado**.**  
**-** Parâmetro **"*Considerar conflito de horário de disciplinas em diferentes níveis de ensino*"** marcado.  
   
Aluno irá realizar a matricula nas duas turmas/disciplinas: '*Inovação e Tomada de Decisão'*e '*Negociação e Comunicação'* no nível de ensino Pós- Graduação Lato Senso*.* Considere que ele já tenha matrícula nas disciplinas de '*Direito Penal I'* e '*Gestão de Processos' do* nível de ensino Graduação.  
   
**Resultado:** sistema irá permitir a matricula mas ao final do processo irá indicar conflito das seguintes disciplinas em seus respectivos níveis:  
   
Nível de ensino: **Graduação**  
Turma/Disciplina: 1 (Direito Penal I)

|  |  |
| --- | --- |
| **Dia** | **Horário** |
| Segunda | 19:00 - 20:40 |
| Quarta | 19:00 - 20:40 |

Nível de ensino: **Pós- Graduação Lato Sensu**

Turma/Disciplina: 3 (Inovação e Tomada de Decisão)

|  |  |
| --- | --- |
| **Dia** | **Horário** |
| Segunda | 19:00 - 20:40 |
| Terça | 19:00 - 20:40 |
