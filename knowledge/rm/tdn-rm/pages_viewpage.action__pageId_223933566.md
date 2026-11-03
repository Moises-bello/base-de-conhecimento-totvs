---
content_hash: 6a765ef8d268c8e32490f1a812d95e2a691aa1944ea31e3ed33d2e8b6bfeb644
fetched_at: '2026-06-29T00:06:23.177925+00:00'
page_id: '223933566'
product: rm
source: tdn-rm
title: ER_PCREQ_Modificação de horário planejado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223933566
version: 131
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### 

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | Automação de Ponto | **Módulo** | Cadastro de horário |
| **Segmento Executor** |  | | |
| **Projeto1** |  | **IRM1** |  |
| **Requisito1** |  | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.10 | **Réplica** |  |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 

 

**O cliente tem vários tipos de horários (Não limitando aos dois abaixo):**

 

**Exemplo 1 = 4 índices (2 dias de trabalho e 2 dias sem trabalho)**

 

**Exemplo 2 = 12 índices (6 dias de trabalho, 1 sem, depois 4 dias de trabalho e 1 sem)**

 

 

Proposta: O sistema deverá validar para que toda semana tenha somente um dia de descanso, nos dias sem trabalho. Abaixo exemplo do resultado esperado:

 

 

|  |  |  |  |
| --- | --- | --- | --- |
| **Data** | **Dia Semana** | **Horário/Índice** | **Descanso?** |
| 21/12/2015 | segunda-feira | Trabalho |  |
| 22/12/2015 | terça-feira | Trabalho |  |
| 23/12/2015 | quarta-feira | Dia sem trabalhos | SIM |
| 24/12/2015 | quinta-feira | Dia sem trabalhos |  |
| 25/12/2015 | sexta-feira | Trabalho |  |
| 26/12/2015 | sábado | Trabalho |  |
| 27/12/2015 | **domingo** | Dia sem trabalhos |  |
| 28/12/2015 | segunda-feira | Dia sem trabalhos | SIM |
| 29/12/2015 | terça-feira | Trabalho |  |
| 30/12/2015 | quarta-feira | Trabalho |  |
| 31/12/2015 | quinta-feira | Dia sem trabalhos |  |
| 01/01/2016 | sexta-feira | Dia sem trabalhos |  |
| 02/01/2016 | sábado | Trabalho |  |
| 03/01/2016 | **domingo** | Trabalho |  |
| 04/01/2016 | segunda-feira | Dia sem trabalhos | SIM |
| 05/01/2016 | terça-feira | Dia sem trabalhos |  |
| 06/01/2016 | quarta-feira | Trabalho |  |
| 07/01/2016 | quinta-feira | Trabalho |  |
| 08/01/2016 | sexta-feira | Dia sem trabalhos |  |
| 09/01/2016 | sábado | Dia sem trabalhos |  |
| 10/01/2016 | **domingo** | Trabalho |  |
| 11/01/2016 | segunda-feira | Trabalho |  |
| 12/01/2016 | terça-feira | Dia sem trabalhos | SIM |
| 13/01/2016 | quarta-feira | Dia sem trabalhos |  |
| 14/01/2016 | quinta-feira | Trabalho |  |
| 15/01/2016 | sexta-feira | Trabalho |  |
| 16/01/2016 | sábado | Dia sem trabalhos |  |
| 17/01/2016 | **domingo** | Dia sem trabalhos |  |

## Definição da Regra de Negócio

1)      Será criado um cadastro “Modificação de Horário Planejado” com as seguintes informações:

1. **Código:** Código da modificação.
2. **Início da definição**: Se a definição da modificação será realizada a partir do início da semana ou fim da semana.
3. **Tipo de ocorrência a considerar**: Tipo de ocorrência de presença que será definido. Exemplo: Descanso
4. **Horas na semana**: O total de horas para o tipo de ocorrência a considerar dentro da semana.
5. Tipo de ocorrência para substituição:  Tipo de ocorrência de presença que será trocado. Exemplo: Compensado  
   **Explicação referente ao comportamento dos três itens anteriores.**
   1. Caso o número de horas na montagem do horário do **Tipo de ocorrência a considerar** seja menor que as **horas na semana**:  
      Será verificado se existe o **tipo de ocorrência a considerar** na montagem de horário, dentro de cada semana.  
      Caso exista, irá aumentar as horas até atingir o total configurado.   
      Caso não exista, o **tipo de ocorrência a considerar** irá substituir o **tipo de ocorrência para substituição** até atingir as horas **na semana**. Caso o **tipo de ocorrência para substituição** não exista, nada será feito.
   2. Caso o número de horas na montagem do horário do **Tipo de ocorrência a considerar** seja igual as horas **na semana**:  
      Nada será feito.
   3. Caso o número de horas na montagem do horário do **Tipo de ocorrência a considerar** seja maior que as **horas na semana**:  
      O **tipo de ocorrência a considerar** será substituído pelo **tipo de ocorrência para substituição** até atingir as **horas na semana**.
6. Considera intervalos programados: Se deve considerar os intervalos programados para a modificação. Os intervalos considerados são de abono, sem ponto, afastamento, férias e descanso (grupo descanso). Caso o parâmetro esteja desmarcado, a modificação será realizada antes de aplicar os intervalos programados. Caso contrário, a modificação será aplicada após aplicar os intervalos programados, dando prioridade a eles. (Ver exemplo 5 no final do deste documento)  
     
   **Obs: A parametrização acima será realizada para o cadastro de Modificação de Horário Planejado. Uma mesma configuração poderá ser associada a N horários.**

2)      Será criado um lookup dentro do cadastro de horário por intervalo e horário por jornada para vincular o **cadastro da modificação aos horário planejado**:

1. Horário por intervalo
2. Horário por jornada

3)      **Detalhes internos da evolução do cálculo:** A leitura do horário no cálculo será evoluída para aplicar as configurações da modificação de horário. A modificação terá os seguintes comportamentos:

1. Será aplicada com uma periodicidade semanal.
2. Será considerado somente se a data de mudança do horário for no início da semana. Como a periodicidade é semanal, devemos garantir a integridade da aplicação da modificação.  
     
     
   Ex:

   |  |  |  |
   | --- | --- | --- |
   | **Semana** | **Índice** | **Descrição** |
   | Segunda-feira | 4 | Troca de Horário 2 x 2 Índice 4 |
   | Terça-feira | 1 | T |
   | Quarta-feira | 2 | T |
   | Quinta-feira | 4 | Troca de Horário 6 x 1 e 4 x 1 Índice 4 |
   | Sexta-feira | 4 | Compensa |
   | Sábado | 1 | T |
   | Domingo | 2 | T |

   No exemplo acima, temos duas trocas de horário dentro da semana.

   Horário 2 x 2 (Segunda-feira)

   Horário 6 x 1 e 4 x 1 (Segunda-feira)

   Considerando que tenha modificação de horário para os dois planejados:

   Horário 2 x 2: **Modificação MOD1**

   Horário 6 x 1 e 4 x 1: **Modificação MOD2**

   Apenas o primeiro (MOD1) será aplicado, pois a troca foi realizada no começo da semana. O segundo (MOD2) será desconsiderado, pois a troca foi no meio da semana (quinta-feira):

   Horário 2 x 2: **Modificação MOD1 (CONSIDERADO)**

   Horário 6 x 1 e 4 x 1: **Modificação MOD2 (DESCONSIDERADO)**
3. A modificação também deverá respeitar as horas de interjornada.
4. A modificação será realizada somente para presença no horário, não sendo aplicada nos casos de ausência.
5. A memória de cálculo será evoluída para contemplar essa aplicação.

4)      Será criado aviso calculado para o caso do funcionário não tiver 24 horas de descanso na semana.

5)      Será disponibilizada  a visão de avisos calculados no portal para os gestores.

Considerações em relação a periodicidade:

Seguem exemplos de como será considerado para horários noturnos:

1. Semanal:
   1. A semana será definida conforme configuração de DSR no sindicato. Caso a jornada comece em um dia e termine em outro, ela será computada conforme o tipo do horário:
      1. Semana 1: 01/01 a 07/01  
         Horário contíguo: 07/01 22:00 a 08/01 05:00. Nesse caso serão consideradas as 07:00 para a semana 1.
      2. Semana 1: 01/01 a 07/01  
         Horário de quebra: 07/01 22:00 a 08/01 05:00. Nesse caso serão consideradas as 02:00 para a semana 1 e 05:00 para a semana 2.

### Itens não contemplados:

* Apesar de poder fazer trocas de horário no meio da semana livremente, não há definição de modificação de horário no meio da semana. A modificação de horário planejado considerado sempre será do horário definido no primeiro dia da semana.
* Proposta para **V12.1**
* Não há validação no histórico de horário, ou seja, se o cliente colocar todas os dias da semana como trabalho não será barrado, mas irá ser gerado um aviso calculado informando da inconsistência.

# Exemplos de Aplicação

Exemplos de aplicação para a CCR:

### 1)  Horário sem descanso na semana

Horário planejado:

2x2

1 – TRAB (08:00)

2 – TRAB (08:00)

**3 – DESC (24:00)**

4 – COMP(24:00)

Horário no período:

|  |  |  |  |
| --- | --- | --- | --- |
|  | **Semana** | **Índice** | **Descrição** |
| **SEMANA 1** | Segunda-feira | 4 | Troca de Horário 2 x 2 Índice 4 |
| Terça-feira | 1 | T |
| Quarta-feira | 2 | T |
| Quinta-feira | 4 | Troca de Horário 2 x 2 Índice 4 |
| Sexta-feira | 4 | Compensa |
| Sábado | 1 | T |
| Domingo | 2 | T |
| **SEMANA 2** | Segunda-feira | 3 | DESCANSO |
| Terça-feira | 4 | Compensa |
| Quarta-feira | 1 | T |
| Quinta-feira | 2 | T |
| Sexta-feira | 3 | DESCANSO |
| Sábado | 4 | Compensa |
| Domingo | 1 | T |
| **SEMANA 3** | Segunda-feira | 2 | T |
| Terça-feira | 3 | DESCANSO |
| Quarta-feira | 4 | Compensa |
| Quinta-feira | 1 | T |
| Sexta-feira | 2 | T |
| Sábado | 3 | DESCANSO |
| Domingo | 4 | Compensa |
| **SEMANA 4** | Segunda-feira | 1 | T |
| Terça-feira | 2 | T |
| Quarta-feira | 3 | DESCANSO |
| Quinta-feira | 4 | Compensa |
| Sexta-feira | 1 | T |
| Sábado | 2 | T |
| Domingo | 3 | DESCANSO |

1. Cadastro modificação de horário planejado:  
   Periodicidade: Semanal  
   Início da definição: Início do período  
   Tipo de ocorrência a considerar: DESCANSO  
   Total de horas: 24:00  
   Tipo de ocorrência para substituição: COMPENSADO  
   Considera intervalos programados desmarcado

Horário após aplicação do cadastro:

|  |  |  |  |
| --- | --- | --- | --- |
|  | **Semana** | **Índice** | **Descrição** |
| **SEMANA 1** | Segunda-feira | 4 | DESCANSO |
| Terça-feira | 1 | T |
| Quarta-feira | 2 | T |
| Quinta-feira | 4 | Troca de Horário 2 x 2 Índice 4 |
| Sexta-feira | 4 | Compensa |
| Sábado | 1 | T |
| Domingo | 2 | T |
| **SEMANA 2** | Segunda-feira | 3 | DESCANSO |
| Terça-feira | 4 | Compensa |
| Quarta-feira | 1 | T |
| Quinta-feira | 2 | T |
| Sexta-feira | 3 | Compensa |
| Sábado | 4 | Compensa |
| Domingo | 1 | T |
| **SEMANA 3** | Segunda-feira | 2 | T |
| Terça-feira | 3 | DESCANSO |
| Quarta-feira | 4 | Compensa |
| Quinta-feira | 1 | T |
| Sexta-feira | 2 | T |
| Sábado | 3 | Compensa |
| Domingo | 4 | Compensa |
| **SEMANA 4** | Segunda-feira | 1 | T |
| Terça-feira | 2 | T |
| Quarta-feira | 3 | DESCANSO |
| Quinta-feira | 4 | Compensa |
| Sexta-feira | 1 | T |
| Sábado | 2 | T |
| Domingo | 3 | Compensa |

1. Cadastro Tabela de horário:  
   Periodicidade: Semanal  
   Início da definição: Fim do período  
   Tipo de ocorrência a considerar: DESCANSO  
   Total de horas: 24:00  
   Tipo de ocorrência para substituição: COMPENSADO  
   Considera intervalos programados desmarcado

Horário após aplicação do cadastro:

|  |  |  |  |
| --- | --- | --- | --- |
|  | **Semana** | **Índice** | **Descrição** |
| **SEMANA 1** | Segunda-feira | 4 | Compensa |
| Terça-feira | 1 | T |
| Quarta-feira | 2 | T |
| Quinta-feira | 4 | Troca de Horário 2 x 2 Índice 4 |
| Sexta-feira | 4 | DESCANSO |
| Sábado | 1 | T |
| Domingo | 2 | T |
| **SEMANA 2** | Segunda-feira | 3 | Compensa |
| Terça-feira | 4 | Compensa |
| Quarta-feira | 1 | T |
| Quinta-feira | 2 | T |
| Sexta-feira | 3 | Compensa |
| Sábado | 4 | DESCANSO |
| Domingo | 1 | T |
| **SEMANA 3** | Segunda-feira | 2 | T |
| Terça-feira | 3 | Compensa |
| Quarta-feira | 4 | Compensa |
| Quinta-feira | 1 | T |
| Sexta-feira | 2 | T |
| Sábado | 3 | Compensa |
| Domingo | 4 | DESCANSO |
| **SEMANA 4** | Segunda-feira | 1 | T |
| Terça-feira | 2 | T |
| Quarta-feira | 3 | Compensa |
| Quinta-feira | 4 | Compensa |
| Sexta-feira | 1 | T |
| Sábado | 2 | T |
| Domingo | 3 | DESCANSO |

### 2)  Horário com descanso de menos de 24:00 na semana.

Horário planejado:

6x1 e 4x1

1 – TRAB (08:00)

2 – TRAB (08:00)

3 – TRAB (08:00)

4 – TRAB (08:00)

5 – TRAB (08:00)

6 – TRAB (08:00)

7 – DESC (04:00 a +02:00)

8 – TRAB (08:00)

9 – TRAB (08:00)

10 – TRAB (08:00)

11 – TRAB (08:00)

12 – DESC (22:00)

13 - DESC (02:00)

Horário da semana:

SEG - 1

TER - 2

QUA - 3

QUI - 4

SEX - 5

SAB - 6

DOM – 7 **(04:00 a +02:00)**

1. Cadastro Tabela de horário:  
   Periodicidade: Semanal  
   Início da definição: Início do período  
   Tipo de ocorrência a considerar: DESCANSO  
   Total de horas: 24:00  
   Tipo de ocorrência para substituição: COMPENSADO  
   Considera intervalos programados desmarcado  
     
     
     
   Horário após aplicação do cadastro:

             SEG - 1

             TER - 2

             QUA - 3

             QUI - 4

             SEX - 5

             SAB - 6

             **DOM – 7 DESCANSO (02:00 a +02:00) (24:00)**

### 3)  Horário com descanso de 24:00 na semana.

Horário planejado:

2x2

1 – TRAB (08:00)

2 – TRAB (08:00)

3 – COMP (24:00)

**4 – DESC** (24:00)

Horário da semana:

SEG - 1

TER - 2

QUA - 3

QUI – 4 DESCANSO

SEX - 1

SAB - 2

DOM - 3

1. Cadastro Tabela de horário:  
   Periodicidade: Semanal  
   Início da definição: Início do período  
   Tipo de ocorrência a considerar: DESCANSO  
   Total de horas: 24:00  
   Tipo de ocorrência para substituição: COMPENSADO  
   Considera intervalos programados desmarcado  
     
     
     
   Horário após aplicação do cadastro, continuará o mesmo:

             SEG - 1

             TER - 2

             QUA - 3

             QUI – 4 DESCANSO

             SEX - 1

             SAB - 2

             DOM - 3

### 4)  Horário com descanso maior que 24:00.

Horário planejado:

2x2

1 – TRAB (08:00)

2 – TRAB (08:00)

3 – COMP (24:00)

**4 – DESC** (24:00)

Horário da semana:

SEG - 3

TER – 4 DESCANSO

QUA - 1

QUI - 2

SEX - 3

SAB – 4 DESCANSO

DOM - 1

1. Cadastro Tabela de horário:  
   Periodicidade: Semanal  
   Início da definição: Início do período  
   Tipo de ocorrência a considerar: DESCANSO  
   Total de horas: 24:00  
   Tipo de ocorrência para substituição: COMPENSADO  
   Considera intervalos programados desmarcado  
     
     

   Horário após aplicação do cadastro:

   SEG - 3

   TER – 4 DESCANSO

   QUA - 1

   QUI - 2

   SEX - 3

   **SAB – 4 COMPENSADO**

   DOM - 1
2. Cadastro Tabela de horário:  
   Periodicidade: Semanal  
   Início da definição: Fim do período  
   Tipo de ocorrência a considerar: DESCANSO  
   Total de horas: 24:00  
   Tipo de ocorrência para substituição: COMPENSADO  
   Considera intervalos programados desmarcado  
     
     
   Horário após aplicação do cadastro:

             SEG - 3

             **TER – 4 COMPENSADO**

             QUA - 1

             QUI - 2

             SEX - 3

             SAB – 4 DESCANSO

             DOM - 1

### 5)  Considerando intervalo programado

Horário planejado:

2x2

1 – TRAB (08:00)

2 – TRAB (08:00)

3 – COMP (24:00)

**4 – DESC** (24:00)

Horário da semana:

SEG - 3

TER – 4 DESCANSO (GRUPO DESCANSO)

QUA - 1

QUI - 2

SEX - 3

SAB – 4 DESCANSO

DOM - 1

1. Cadastro Tabela de horário:  
   Periodicidade: Semanal  
   Início da definição: Fim do período  
   Tipo de ocorrência a considerar: DESCANSO  
   Total de horas: 24:00  
   Tipo de ocorrência para substituição: COMPENSADO  
   Considera intervalos programados marcado  
     
     
   Horário após aplicação do cadastro:  
     
   SEG - 3

TER – 4 DESCANSO (GRUPO DESCANSO)

            QUA - 1

            QUI - 2

            SEX - 3

**SAB – 4 COMPENSADO**

            DOM - 1

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
