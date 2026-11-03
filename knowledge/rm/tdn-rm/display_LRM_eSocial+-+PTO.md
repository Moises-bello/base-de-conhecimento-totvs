---
content_hash: 492c589599eab408c8edb34e69a1d3b358dfcfad429b06bfcac0159c2ed7ca5a
fetched_at: '2026-06-29T00:10:07.792244+00:00'
page_id: '452719438'
product: rm
source: tdn-rm
title: eSocial - PTO
type: documentation
url: https://tdn.totvs.com/display/LRM/eSocial+-+PTO
version: 1
---

**eSocial**

---

**Cadastro de Horários:**

* **Horários por Intervalo:**

Nesta aba é possível definir as informações relacionadas ao eSocial:   
**Tipo de Jornada e-Social**  
O parâmetro possui o objetivo de representar qual o tipo da jornada que será considerado para o e-Social. Existirá como opção de escolha os seguintes itens: - Jornada com horário diário e folga fixos; - Jornada 12 x 36 (12 horas de trabalho seguidas de 36 horas ininterruptas de descanso); - Jornada com horário diário fixo e folga variável; - Demais tipos de jornada.  
A informação acima será considerado no leiaute do eSocial  nos eventos  "S-2200 - Evento Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador" e "S-2206 -Alteração de Contrato de Trabalho".  
**Atenção:**  
Para atender ao eSocial, quando a jornada for semanal, o usuário poderá incluir horário padrão por dia da semana, e folga fixa. Exemplo:

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Data | Índice | Letra | ID Jornada | Dia | Entrada 1 | Saída 1 | Entrada 2 | Saída 2 |
| 16/02/2016 | 1 |  | 1 | TER | 08:00 | 12:00 | 14:00 | 18:00 |
| 17/02/2016 | 2 |  | 1 | QUA | 08:00 | 12:00 | 14:00 | 18:00 |
| 18/02/2016 | 3 | A | 1 | QUI | 08:00 | 12:00 | 14:00 | 18:00 |
| 19/02/2016 | 4 |  | 1 | SEX | 08:00 | 12:00 | 14:00 | 18:00 |
| 20/02/2016 | 5 |  | 1 | SÁB | 08:00 | 12:00 | 14:00 | 18:00 |
| 21/02/2016 | 6 |  | 1 | DOM | 08:00 | 12:00 | 14:00 | 18:00 |
| 22/02/2016 | 7 |  | 1 | SEG | 00:00 | 00:00 |  |  |

**Horas Reduzidas noturnas:**  
Esse campo foi criado para atender ao eSocial evento S-1050 - Tabela de Horários/Turnos de Trabalho   TAG durJornada.  
   
   
**Atenção:**  
O usuário deverá informar na hora nos campos  horário início e horário fim conforme necessidade.  
Por default o campo virá com valor 22:00-05:00.
