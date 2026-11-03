---
article_id: 35787034507031
category: RH - Lançamentos
content_hash: 776602e5456693a7465a92e5ea3c54a9ce3c98c2e454bf8571e16baeb15d6d1c
fetched_at: '2026-06-28T22:44:46.791435+00:00'
product: protheus
section_id: 32419271673111
source: central-protheus
title: RH - Linha Protheus - PON - Cálculo da Interjornada quando temos um dia de
  Feriado entre os dias que tiveram jornada trabalhada
type: support-article
updated_at: '2025-10-21T21:03:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35787034507031-RH-Linha-Protheus-PON-C%C3%A1lculo-da-Interjornada-quando-temos-um-dia-de-Feriado-entre-os-dias-que-tiveram-jornada-trabalhada
---

**Dúvida**  
Cálculo da interjornada quando temos um dia de Feriado entre os dias que tiveram jornada trabalhada  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
O **Feriado,** pode ser interpretado para alguns,assim como o **DSR** e a **Interjornada**, com o objetivo de realizar a manutenção da saúde do empregado através do período de descanso, sendo o **Feriado** consideradocom no mínimo **24 horas** de descanso e a **Interjornada** com no mínimo **11 horas** de descanso.  
  
Neste caso, o sistema de ponto está configurado para atender tanto à regra que exige um mínimo de 24 horas de descanso de interjornada no feriado, quanto para não aplicá-la, conforme a configuração do turno de trabalho do funcionário.

Se o turno estiver configurado para garantir as 24 horas de descanso no feriado, esse período será acumulado junto às 11 horas da interjornada, totalizando 35 horas contínuas de descanso a partir do horário de saída do funcionário no dia anterior ao feriado.  
  
Para o correto funcionamento deverá seguir as configurações abaixo:  
No turno de trabalho do funcionário os campos deverão serem configurados conforme abaixo:  
  
Hr.Inter.Jor- R6\_HRINTER->Informar o número de Horas que devem ser considerado para Descanso Entre Duas Jornadas de Trabalho na apuração de Horas Extras Inter-Jornada.  
Tp.Dia In.Jo-R6\_INTERNT->Informe os Tipos de Dias Para os quais deverão ser apontadas Horas Extras  
Inter-Jornadas.  
Hrs. FER HE-R6\_FERINTE->Este campo será responsável por armazenar a quantidade de horas que o funcionário deverá descansar em dias de feriados, caso não tenha preenchimento ou com valor "0" o descanso do funcionário serão geradas com base na interjornada de 11h. O conteúdo em que estiver preenchido no campo Hrs. FER HE será somado ao que estiver preenchido no campo Hr.Inter.Jor.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35787034495895)  
  
**Abaixo, segue um exemplo do cálculo feito pelo sistema:**  
- no dia 13.10 (dia trabalhado normal), o funcionário realizou seu trabalho no expediente normal saindo as 16h56;  
- no dia 14.10(Feriado), o funcionário entrou as 08h00 e saiu as 09h00, efetuando 01h de HE no Feriado.   
  
Com isso, o sistema calculou 35h00 de interjornada(11h da interjornada e 24h do Feriado), ficando assim:  
Descanso efetuado: das 16h56(13/10) Às 08h(14/10) igual à 15h04;  
Cálculo efetuando de 35h diminuindo 15h04 igual à 19h56 de HE INTERJORNADA  
  
**Importante** ressaltar que esta regra se aplica mesmo quando o dia que antecede o **Fériado** é um dia Trabalhado.  
  
Veja exemplo prático:   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35787034496663)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35787065201047)  
  
Caso o campo Hrs. FER HE-R6\_FERINTE do Turno de Trabalho estiver com 0,00 ou em branco, o sistema não irá considerar o descanso de 35h e sim somente as 11h definida no campo Hr.Inter.Jor- R6\_HRINTER.   
Veja abaixo que o campo Hrs. FER HE-R6\_FERINTE com conteúdo 0,00, ao reapontar o dia 13/10 não gerou mais as 19h56 de HE INTERJORNADA:   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35787034499351)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35787236227223)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35787191402391)  
  
**Saiba Mais:**  
[Apontando Horas Extras por Violação do Intervalo Interjornada em Jornada de 35h com Trabalho em Feriado](https://tdn.totvs.com/pages/releaseview.action?pageId=969135126)  
[RH - Linha Protheus - PON - Como gerar a Interjornada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014625691-RH-Linha-Protheus-PON-Como-gerar-a-hora-extra-interjornada)  
[Cálculo da Interjornada quando temos um dia de DSR entre os dias que tiveram jornada trabalhada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004089441-RH-Linha-Protheus-PON-C%C3%A1lculo-da-Interjornada-quando-temos-um-dia-de-DSR-entre-os-dias-que-tiveram-jornada-trabalhada)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
