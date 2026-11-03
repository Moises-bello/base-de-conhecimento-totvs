---
article_id: 1500004089441
category: RH - Lançamentos
content_hash: 5c60f775d6be5c9aebe964ffce134c513c97580103cefa1c40aea22f0911b3e2
fetched_at: '2026-06-28T22:44:46.785463+00:00'
product: protheus
section_id: 32419271673111
source: central-protheus
title: RH - Linha Protheus - PON - Cálculo da Interjornada quando temos um dia de
  DSR entre os dias que tiveram jornada trabalhada
type: support-article
updated_at: '2025-10-21T21:01:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004089441-RH-Linha-Protheus-PON-C%C3%A1lculo-da-Interjornada-quando-temos-um-dia-de-DSR-entre-os-dias-que-tiveram-jornada-trabalhada
---

**Dúvida**Cálculo da interjornada quando temos um dia de DSR entre os dias que tiveram jornada trabalhada  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**O **Descanso Semanal Remunerado** (DSR)**,** assim como a **Interjornada**, possuem o objetivo de realizar a manutenção da saúde do empregado através do período de descanso, sendo o **DSR** com no mínimo **24 horas** e a Interjornada com no mínimo **11 horas** de descanso.  
  
Neste caso, entende-se que, nos dias que antecedem o **DSR**, os períodos de descanso devem ser acumulados, totalizando 35 horas contínuas de descanso a partir do horário de saída do funcionário no dia anterior ao **DSR.**Para o correto funcionamento deverá seguir as configurações da documentação: [Como apontar a Interjornada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014625691-RH-Linha-Protheus-PON-Como-apontar-a-Interjornada)Além da configuração citada na documentação, é válido destacar que no turno de trabalho do funcionário os campos deverão serem configurados conforme abaixo:  
  
Hr.Inter.Jor- R6\_HRINTER->Informar o número de Horas que devem ser considerado para Descanso Entre Duas Jornadas de Trabalho na apuração de Horas Extras Inter-Jornada.  
Tp.Dia In.Jo-R6\_INTERNT->Informe os Tipos de Dias Para os quais deverão ser apontadas Horas Extras  
Inter-Jornadas.  
Hrs. DSR HE-R6\_DSRINTE->Por padrão o sistema irá considerar 24 horas para o descanso do DSR, caso o campo estiver em branco ou com valor "0" o sistema acatará 24horas. Só será permitido alterando a quantidade igual ou maior que 01minuto.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35791294857751)  
  
  
**Abaixo, segue um exemplo do cálculo feito pelo sistema:**  
- no dia 02.12 (dia Compensado pela Tabela de Horário Padrão), o funcionário realizou Hora Extra das 12h às 23h;  
- no dia 03.12 (dia de DSR pela Tabela de Horário Padrão), o funcionário realizou Hora Extra das 08h às 12h;  
- além das Horas Extras dos dois dias, foi apontado um total de 26h de Interjornada, pois:  
-> a partir do horário de saída do funcionário no dia que antecede o DSR (neste caso, o dia 02), é iniciada a contagem das 35h de descanso que devem ser contínuas, ou seja, o funcionário só poderia ter iniciado a jornada no dia 04 a partir das 10h00;  
-> neste caso, como o funcionário interrompeu este descanso iniciando uma jornada no dia 03 às 08h, o sistema contabiliza quantas horas ele efetivamente descansou, ou seja: das 23h00 do dia 02 até às 08h do dia 03 = 09h descansadas;  
-> por fim, é feito o cálculo das horas previstas a serem descansadas menos as horas efetivamente descansadas, ou seja: 35h - 09h = 26h que ele deixou de descansar, portanto, estas horas são apontadas como Interjornada. Para efeito de visualização das marcações e apontamentos, acesse em **Atualizações-Lançamentos-Marcações**, filtre o funcionário e entre como alterar.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20194155212695)  
  
**Importante** ressaltar que esta regra se aplica mesmo quando o dia que antecede o **DSR** é um dia Trabalhado.   
  
Para mais detalhes, o time de **Consultoria Jurídica da TOTVS** disponibilizou uma documentação com maiores informações, que pode ser acessada e consultada na documentação no item [3.1 DSR - Interjornada  e DSR - Coincidência dos Períodos](https://tdn.totvs.com.br/pages/releaseview.action?pageId=144412479#Orienta%C3%A7%C3%B5esConsultoriadeSegmentosInterjornadaPer%C3%ADodom%C3%ADnimode11horasconsecutivasparadescanso.-3.1DSR-InterjornadaeDSR-Coincid%C3%AAnciadosPer%C3%ADodos)   
  
**Saiba Mais:**[RH - Linha Protheus - PON - Como gerar a Interjornada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014625691-RH-Linha-Protheus-PON-Como-gerar-a-hora-extra-interjornada)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
