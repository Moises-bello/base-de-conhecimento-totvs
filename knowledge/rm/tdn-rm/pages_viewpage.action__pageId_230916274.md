---
content_hash: 607745b8a55b9f767d4d93446b0edd726771845827faf2943c7b3729dfd1b196
fetched_at: '2026-06-29T00:06:27.124056+00:00'
page_id: '230916274'
product: rm
source: tdn-rm
title: DT_ModificaçãoHorárioPlanejado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=230916274
version: 152
---

# Modificação de horário planejado

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Automação de Ponto** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Modificação de Horário Planejado* | *Modificação de Horário Planejado* | |
| **Cadastros Iniciais:** |  |
| **Parâmetro(s):** |  |
| **Ponto de Entrada:** |  |
| **Chamados Relacionados** |  |
| **Requisito (ISSUE):** |  |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** |  |
| **Tabelas Utilizadas:** |  |
| **Sistema(s) Operacional(is):** |  |
| **Versões/Release:** | *12.1.10* |
| **Versão Expedida:** | *12.1.10* |

## Descrição

Essa implementação tem por objetivo adicionar novas funcionalidades ao TOTVS Automação de Ponto, para garantir que toda semana tenha somente um dia de descanso.

Abaixo exemplo do resultado esperado:

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

# Cadastro Modificação de Horário Planejado

Foi disponibilizado o Cadastro de Modificação de Horário Planejado através do menu "*Cadastros | Horários planejados | Modificação de horário*" com as seguintes informações:

1. **Código:** Código da modificação.
2. **Descrição:** Descrição da modificação.
3. **Início da definição**: Se a definição da modificação será realizada a partir do início da semana ou fim da semana.
4. **Horas na semana**: O total de horas para o tipo de ocorrência a considerar dentro da semana.
5. **Tipo de ocorrência a considerar**: Tipo de ocorrência de presença que será definido. Exemplo: Descanso
6. **Tipo de ocorrência para substituição:**  Tipo de ocorrência de presença que será trocado. Exemplo: Compensado  
   **Explicação referente ao comportamento dos três itens anteriores.**
   1. Caso o número de horas na montagem do horário do **Tipo de ocorrência a considerar** seja menor que as **horas na semana**:  
      Será verificado se existe o **tipo de ocorrência a considerar** na montagem de horário, dentro de cada semana.  
      Caso exista, irá aumentar as horas até atingir o total configurado.   
      Caso não exista, o **tipo de ocorrência a considerar** irá substituir o **tipo de ocorrência para substituição** até atingir as horas**na semana**. Caso o **tipo de ocorrência para substituição** não exista, nada será feito.
   2. Caso o número de horas na montagem do horário do **Tipo de ocorrência a considerar** seja igual as horas**na semana**:  
      Nada será feito.
   3. Caso o número de horas na montagem do horário do **Tipo de ocorrência a considerar** seja maior que as **horas na semana**:  
      O **tipo de ocorrência a considerar** será substituído pelo **tipo de ocorrência para substituição** até atingir as **horas na semana**.
7. **Considera intervalos programados:** Se deve considerar os intervalos programados para a modificação. Os intervalos considerados são de abono, sem ponto, afastamento, férias e descanso (grupo descanso). Caso o parâmetro esteja desmarcado, a modificação será realizada antes de aplicar os intervalos programados. Caso contrário, a modificação será aplicada após aplicar os intervalos programados, dando prioridade a eles. (Ver exemplo 5 no final do deste documento)

**Validações:**

* Os campos "Código", "Início para definição", "Tipo de ocorrência a considerar" e "Horas na semana" são de preenchimento obrigatório.
* O campo "Horas na semana" não aceitará um valor superior a 168:00
* Os tipos de ocorrência não podem ser iguais.

# Associar modificação de horário planejado ao Cadastro de Horário por Intervalo e por Jornada

Foi disponibilizado um lookup dentro do cadastro de horário por intervalo e horário por Jornada par avincular o cadastro de modificação de horário planejado.

* Horário por intervalo:

* Horário por Jornada:

**Validações:**

* Caso seja vinculadas modificações que possuam o mesmo tipo de ocorrência a considerar o cadastro de horário não será salvo.z'

# Evolução do cálculo do Ponto

A leitura do horário no cálculo foi evoluída para aplicar as configurações da modificação de horário. A modificação terá os seguintes comportamentos:

1. Será aplicada com uma periodicidade semanal.
2. A modificação também deverá respeitar as horas de interjornada. Caso não respeite, será gerado aviso calculado.
3. A modificação será realizada somente para presença no horário, não sendo aplicada nos casos de ausência.
4. A memória de cálculo será evoluída para contemplar essa aplicação.
5. A aplicação da modificação deverá respeitar o comportamento do horário: contíguo/quebra por dia.
6. A semana será definida conforme configuração de DSR no sindicato. Caso a jornada comece em um dia e termine em outro, ela será computada conforme o tipo do horário:   
   Semana 1: 01/01 a 07/01   
   Horário Contíguo: 07/01 22:00 a 08/01 05:00. Nesse caso serão consideradas as 07:00 para a semana 1.  
   Horário de quebra: 07/01 22:00 a 08/01 05:00. Nesse caso serão consideradas as 02:00 para a semana 1 e 05:00 para a semana 2.
7. A alteração é possível a qualquer dia da semana, porém respeita o horário cadastrado no histórico do primeiro dia da semana. Como a periodicidade é semanal, devemos garantir a integridade da aplicação da modificação. Caso a modificação do próximo horário tenha o Tipo de Ocorrência a considerar igual ao primeiro, esta será desconsiderada.  
   Ex.:

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

   Horário 2 x 2: Modificação MOD1 - Tipo Ocorrência a considerar: EDN  
   Horário 6 x 1 e 4 x 1: Modificação MOD2 - Tipo Ocorrência a considerar: EDN

   Apenas o primeiro (MOD1) será aplicado, pois a troca foi realizada no começo da semana. O segundo (MOD2) será desconsiderado, pois a troca foi no meio da semana (quinta-feira):  
   Horário 2 x 2: Modificação MOD1 (CONSIDERADO)  
   Horário 6 x 1 e 4 x 1: Modificação MOD2 (DESCONSIDERADO)
8. A modificação será realizada da seguinte maneira:  

   i. Caso o número de horas na montagem do horário do Tipo de ocorrência a considerar seja menor que as horas na semana:

   Será verificado se existe o tipo de ocorrência a considerar na montagem de horário, dentro de cada semana.

   Caso exista, irá aumentar as horas até atingir o total configurado. Caso não exista, o tipo de ocorrência a considerar irá substituir o tipo de ocorrência para substituição até atingir as horas na semana. Caso o tipo de ocorrência para substituição não exista, nada será feito.

   ii. Caso o número de horas na montagem do horário do Tipo de ocorrência a considerar seja igual as horas na semana:

   Nada será feito.

   iii. Caso o número de horas na montagem do horário do Tipo de ocorrência a considerar seja maior que as horas na semana:

   O tipo de ocorrência a considerar será substituído pelo tipo de ocorrência para substituição até atingir as horas na semana. Caso o tipo de ocorrência para substituição não exista, as horas a mais serão apenar retiradas, sem substituição.
9. A modificação será realizada somente para presença no horário, não sendo aplicada nos casos de ausência.
10. Deverá considerar o parâmetro "Considera intervalos programados", e definir qual terá prioridade.
11. Os intervalos programados considerados são os descansos vinculados ao grupo de descanso. Caso o parâmetro esteja desmarcado, a modificação será realizada antes de aplicar os intervalos programados. Caso contrário, a modificação será aplicada após aplicar os intervalos programados, dando prioridade a eles.  
    Ex.:  

    Horário planejado:  
    2x2  
    1 – TRAB (08:00)  
    2 – TRAB (08:00)  
    3 – COMP (24:00)  
    4 – DESC (24:00)

    Horário da semana:  
    SEG - 3   
    TER – 4 DESCANSO (GRUPO DESCANSO)  
    QUA - 1   
    QUI - 2  
    SEX - 3  
    SAB – 4 DESCANSO  
    DOM - 1

    a. Cadastro Modificação de horário planejado:  
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
    SAB – 4 COMPENSADO  
    DOM - 1

**Obs: A modificação não irá ser considerada no caso de tolerâncias de presença antes/após intervalos de trabalho. Não será possível portanto entender intervalos de trabalho que possuam tolerância de presença.**

# Exemplos de Aplicação

### 1) Horário sem descanso na semana

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

**Cadastro modificação de horário planejado:**

**Periodicidade:** Semanal  
**Início da definição:** Início do período  
**Tipo de ocorrência a considerar:** DESCANSO  
**Total de horas:** 24:00  
**Tipo de ocorrência para substituição:** COMPENSADO  
**Considera intervalos programados:** Desmarcado

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

**2) Horário com descanso de menos de 24:00 na semana**

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

|  |  |  |  |
| --- | --- | --- | --- |
|  | **Semana** | **Índice** | **Descrição** |
| **SEMANA 1** | Segunda-feira | 1 | T |
| Terça-feira | 2 | T |
| Quarta-feira | 3 | T |
| Quinta-feira | 4 | T |
| Sexta-feira | 5 | T |
| Sábado | 6 | T |
| Domingo | 7 | DESC (04:00 a +02:00) |

**Cadastro Tabela de horário:**

**Periodicidade:** Semanal  
**Início da definição:** Início do período  
**Tipo de ocorrência a considerar:** DESCANSO  
**Total de horas:** 24:00  
**Tipo de ocorrência para substituição:** COMPENSADO  
**Considera intervalos programados:** Desmarcado

Horário após aplicação do cadastro:

|  |  |  |  |
| --- | --- | --- | --- |
|  | **Semana** | **Índice** | **Descrição** |
| **SEMANA 1** | Segunda-feira | 1 | T |
| Terça-feira | 2 | T |
| Quarta-feira | 3 | T |
| Quinta-feira | 4 | T |
| Sexta-feira | 5 | T |
| Sábado | 6 | T |
| Domingo | 7 | DESC (04:00 a +04:00) (24:00) |

**3) Horário com descanso de 24:00 na semana**

Horário planejado:

2x2

1 – TRAB (08:00)

2 – TRAB (08:00)

3 – COMP (24:00)

**4 – DESC**(24:00)

Horário da semana:

|  |  |  |  |
| --- | --- | --- | --- |
|  | **Semana** | **Índice** | **Descrição** |
| **SEMANA 1** | Segunda-feira | 1 | T |
| Terça-feira | 2 | T |
| Quarta-feira | 3 | COMP |
| Quinta-feira | 4 | DESC |
| Sexta-feira | 1 | T |
| Sábado | 2 | T |
| Domingo | 3 | COMP |

**Cadastro Tabela de horário:**

**Periodicidade:** Semanal  
**Início da definição:** Início do período  
**Tipo de ocorrência a considerar:** DESCANSO  
**Total de horas:** 24:00  
**Tipo de ocorrência para substituição:** COMPENSADO  
**Considera intervalos programados:** Desmarcado

Horário após aplicação do cadastro, continuará o mesmo:

|  |  |  |  |
| --- | --- | --- | --- |
|  | **Semana** | **Índice** | **Descrição** |
| **SEMANA 1** | Segunda-feira | 1 | T |
| Terça-feira | 2 | T |
| Quarta-feira | 3 | COMP |
| Quinta-feira | 4 | DESC |
| Sexta-feira | 1 | T |
| Sábado | 2 | T |
| Domingo | 3 | COMP |

**4) Horário com descanso maior que 24:00**

Horário planejado:

2x2

1 – TRAB (08:00)

2 – TRAB (08:00)

3 – COMP (24:00)

**4 – DESC**(24:00)

Horário da semana:

|  |  |  |  |
| --- | --- | --- | --- |
|  | **Semana** | **Índice** | **Descrição** |
| **SEMANA 1** | Segunda-feira | 3 | COMP |
| Terça-feira | 4 | DESC |
| Quarta-feira | 1 | T |
| Quinta-feira | 2 | T |
| Sexta-feira | 3 | COMP |
| Sábado | 4 | DESC |
| Domingo | 1 | T |

**Cadastro Tabela de horário:**

**Periodicidade:** Semanal  
**Início da definição:** Início do período  
**Tipo de ocorrência a considerar:** DESCANSO  
**Total de horas:** 24:00  
**Tipo de ocorrência para substituição:** COMPENSADO  
**Considera intervalos programados:** Desmarcado

Horário após aplicação do cadastro:

|  |  |  |  |
| --- | --- | --- | --- |
|  | **Semana** | **Índice** | **Descrição** |
| **SEMANA 1** | Segunda-feira | 3 | COMP |
| Terça-feira | 4 | DESC |
| Quarta-feira | 1 | T |
| Quinta-feira | 2 | T |
| Sexta-feira | 3 | COMP |
| Sábado | 4 | COMP |
| Domingo | 1 | T |

**Cadastro Tabela de horário:**

**Periodicidade:** Semanal  
**Início da definição:** Fim do período  
**Tipo de ocorrência a considerar:** DESCANSO  
**Total de horas:** 24:00  
**Tipo de ocorrência para substituição:** COMPENSADO  
**Considera intervalos programados:** Desmarcado

Horário após aplicação do cadastro:

|  |  |  |  |
| --- | --- | --- | --- |
|  | **Semana** | **Índice** | **Descrição** |
| **SEMANA 1** | Segunda-feira | 3 | COMP |
| Terça-feira | 4 | COMP |
| Quarta-feira | 1 | T |
| Quinta-feira | 2 | T |
| Sexta-feira | 3 | COMP |
| Sábado | 4 | DESC |
| Domingo | 1 | T |

**5) Considerando intervalo programado**

Horário planejado:

2x2

1 – TRAB (08:00)

2 – TRAB (08:00)

3 – COMP (24:00)

**4 – DESC**(24:00)

Horário da semana:

|  |  |  |  |
| --- | --- | --- | --- |
|  | **Semana** | **Índice** | **Descrição** |
| **SEMANA 1** | Segunda-feira | 3 | COMP |
| Terça-feira | 4 | DESC (GRUPO DESCANSO) |
| Quarta-feira | 1 | T |
| Quinta-feira | 2 | T |
| Sexta-feira | 3 | COMP |
| Sábado | 4 | DESC |
| Domingo | 1 | T |

**Cadastro Tabela de horário:**

**Periodicidade:** Semanal  
**Início da definição:** Fim do período  
**Tipo de ocorrência a considerar:** DESCANSO  
**Total de horas:** 24:00  
**Tipo de ocorrência para substituição:** COMPENSADO  
**Considera intervalos programados:** Marcado

Horário após aplicação do cadastro:

|  |  |  |  |
| --- | --- | --- | --- |
|  | **Semana** | **Índice** | **Descrição** |
| **SEMANA 1** | Segunda-feira | 3 | COMP |
| Terça-feira | 4 | DESC (GRUPO DESCANSO) |
| Quarta-feira | 1 | T |
| Quinta-feira | 2 | T |
| Sexta-feira | 3 | COMP |
| Sábado | 4 | COMP |
| Domingo | 1 | T |

# Aviso calculado para menos de 24 horas contínuas de descanso na semana

Foi disponibilizado uma evolução no cálculo do ponto para gerar aviso calculado quando o funcionário tiver menos de 24 horas contínuas de descanso na semana.

Como parte da solução, foi adicionado um novo registro no cadastro "Tipo de Aviso Calculado" e a janela de informações do Aviso recebeu duas novas colunas indicando a data início e fim da semana.

**Observação**: Os demais avisos, não sofreram alterações e continuam sendo calculados e apresentados diariamente.

**Possíveis condições em que serão gerados os avisos calculados:**

* Caso o horário planejado possua menos de 24 horas de descanso na semana
* Caso o horário planejado possua 24 horas não continuas de descanso na semana
* Caso o horário planejado possua mais de 24 horas não continuas de descanso na semana

**Possíveis condições em que NÃO serão gerados os avisos calculados:**

* Caso o horário planejado possua 24 horas continuas de descanso na semana
* Caso o horário planejado possua mais de 24 horas continuas de descanso na semana

# Aviso calculado no Portal

Foi disponibilizado no Portal, dois novos menus contendo uma visão com os avisos calculados dos subordinados.

* Menu interno da equipe:
* Anexo do espelho na visão de subordinados:

Essa visão possui a opção de filtro para subordinados diretos além dos mesmos filtros disponíveis no winforms.

divs
