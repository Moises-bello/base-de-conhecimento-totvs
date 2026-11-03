---
content_hash: c53b52424e8167797986c3ef9cd94a45fe96cc6abb52a100cb707cfcaa920647
fetched_at: '2026-06-29T00:10:06.199718+00:00'
page_id: '452719313'
product: rm
source: tdn-rm
title: Cadastro de Índices da Jornada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719313
version: 14
---

**Parâmetros:**   
**Índice da Jornada**  
Índice da jornada que será associada ao dia para a execução do cálculo.  
**Tipo da Jornada**                  
Definirá o tipo da jornada associada ao dia. Existem três tipos de Jornada:  
1 – Trabalho (Define a jornada de trabalho do funcionário);  
2 – Compensado (Define a jornada de compensado do funcionário);  
3 – Descanso (Define a jornada de descanso do funcionário).  
**Número de horas da jornada**  
Número de horas que será considerado como jornada de cada dia.  
**Número de horas do intervalo de refeição**   
Número de horas que será considerado como intervalo de refeição da jornada.  
Observação: Só será habilitado este parâmetro quando utilizar o tipo da jornada de trabalho.  
**Número de Batidas**   
Número de horas que será considerado como intervalo de refeição da jornada.  
Observação: Como default o valor sempre será 2, caso exista número de horas de refeição o número de batidas deverá ser maior ou igual a 4 batidas.  
   
**Carência de Extras** Número de horas em que, até o valor definido, não será considerado como horas extras  
   
**Exemplo:**  
Jornada do funcionário = 08:00  
Tolerância para omissão de extras = 00:10  
   
**Horário Executado**

|  |  |  |  |
| --- | --- | --- | --- |
|  | **Entrada 1** | **Saída1** | **Entrada 2** |
|  |  |  |  |
| 1/8/2008 | 22:00 |  |  |
| 2/8/2008 |  | 06:08 | 22:00 |
| 3/8/2008 |  | 06:13 | 22:00 |
| 4/8/2008 |  | 05:00 |  |

No exemplo acima, o sistema irá calcular apenas 13 minutos de extra no dia 02/08 (o número de horas é lançado no dia de inicio da jornada), ignorando os 8 minutos da jornada do dia 01/08.  
   
**Abate carência de Extras** Caso este parâmetro esteja marcado, o sistema irá gerar apenas 3 minutos de extras, pois os 10 minutos do parâmetro acima ("Carência de extras") serão abatidos do valor total.  
**Carência para Atrasos** Número de horas em que, até o valor definido, não será considerado como horas extras.  
   
**Exemplo:**  
Jornada do funcionário = 08:00  
Tolerância para omissão de atrasos = 00:10  
   
**Horário Executado**

|  |  |  |  |
| --- | --- | --- | --- |
|  | **Entrada 1** | **Saída1** | **Entrada 2** |
| 1/8/2008 | 22:00 |  |  |
| 2/8/2008 |  | 05:52 | 22:00 |
| 3/8/2008 |  | 05:45 | 22:00 |
| 4/8/2008 |  | 05:00 |  |

No exemplo acima, o sistema irá calcular apenas 15 minutos de atraso no dia 02/08 (o número de horas é lançado no dia de inicio da jornada), ignorando os 8 minutos de atraso da jornada do dia 01/08.  
   
**Abate carência de Atrasos** Caso este parâmetro esteja marcado, o sistema irá gerar apenas 5 minutos de extras, pois os 10 minutos do parâmetro acima ("Carência de atrasos") serão abatidos do valor total.  
   
**Observação Carência Extra/Atraso:** Os parâmetros de Carência de Extras e Atrasos só serão habilitados quando o tipo da jornada for de Trabalho. **Fórmula para jornada de Trabalho**   
Será informada a fórmula que definirá o número de horas da jornada de Trabalho.  
Exemplo:  
SE DIASEM (PAR) = 'TRAB' ENTAO 480 - Se dia pesquisado = Trabalho então jornada de jornada 08:00  
Observação: Este parâmetro só será habilitado quando o tipo da jornada for de trabalho.  
   
**Ausência Planejada por Tempo**   
Ao informar o tempo executado para a ausência planejada, o cálculo irá aplicar o conceito de ausência por tempo.

*Exemplo de configuração:*

**Horas da Jornada:** 08:00

**Horas do Intervalo de Refeição:** 01:00

**Número de Batidas**: 4

**Utiliza Ausência Planejada por Tempo:** Sim

**Tempo Executado:** 06:00

Com essa configuração, ao completar 6 horas de trabalho, será aplicada uma ausência planejada de 1 hora. O horário planejado será ajustado de acordo com o horário executado.

Importante

* Não é gerada ocorrência para a ausência planejada.
* O sistema fará o cálculo com base no primeiro intervalo, caso este intervalo executado da jornada seja menor que o tempo cadastrado no parâmetro **"Tempo Executado"**, essa configuração será desconsiderada e o intervalo de refeição será aplicado no meio da jornada.

*Exemplos de cálculos das jornadas:*

* **Jornada completa:**

**Horário Executado:** 08:00E - 17:00S

**Horário Planejado:** 08:00E - 14:00S / 15:00E - 17:00S

**Ocorrências geradas:**

* + - 08:00 - 14:00: Trabalho (T)
    - 15:00 - 17:00: Trabalho (T)
* ****Jornada finalizada antes do tempo cadastrado no parâmetro "Tempo Executado":****

**Horário Executado:** 08:00E - 13:00S

**Horário Planejado:** 08:00E - 12:00S / 13:00E - 17:00S

**Ocorrências geradas:**

* + - 08:00 - 12:00: Trabalho (T)
    - 12:00 - 13:00: Extra Normal Compensada (ENC)
    - 13:00 - 14:00: Atraso Compensado (AC)
    - 14:00 - 17:00 Atraso (A)

* **Jornada finalizada durante o intervalo de ausência planejada:**

**Horário Executado:** 08:00E - 14:30S

**Horário Planejado:** 08:00E - 14:00S / 15:00E - 17:00S

**Ocorrências geradas:**

* + - 08:00 - 14:00: Trabalho (T)
    - 15:00 - 17:00 Atraso (A)

* **Jornada finalizada após o intervalo de ausência planejada:**

**Horário Executado:** 08:00E - 15:30S

**Horário Planejado:** 08:00E - 14:00S / 15:00E - 17:00S

**Ocorrências geradas:**

* + - 08:00 - 14:00: Trabalho (T)
    - 15:00 - 15:30: Trabalho (T)
    - 15:00 - 17:00: Saída Antecipada (SA)

* **Jornada com horas extras:**

**Horário Executado:** 08:00E - 18:00S

**Horário Planejado:** 08:00E - 14:00S / 15:00E - 17:00S

**Ocorrências geradas:**

* + - 08:00 - 14:00: Trabalho (T)
    - 15:00 - 17:00 Trabalho (T)
    - 17:00 - 18:00: Extra Normal (EA)

|  |  |
| --- | --- |
|  | Informações Complementares |

---

|  |  |
| --- | --- |
|  | Como Fazer |

---

|  |  |
| --- | --- |
|  | Recursos Adicionais |

---

|  |  |
| --- | --- |
|  | Veja Também |

---
