---
article_id: 6296180603159
category: Configurações
content_hash: 7bb46fa049e212be7f2f4cdd2b21c3d172de30113222834e0cbfa32335bed389
fetched_at: '2026-06-28T22:46:29.889130+00:00'
product: rm
section_id: 1500000835121
source: central-rm
title: RH - RM - PTO - Parâmetros do adicional noturno
type: support-article
updated_at: '2026-03-17T18:42:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6296180603159-RH-RM-PTO-Par%C3%A2metros-do-adicional-noturno
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16980759639063)**Tempo aproximado para leitura: 00:01:30 min**  
  
**Dúvida**  
Qual a funcionalidade dos parâmetros do adicional noturno?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - Todas as versões  
  
**Solução**  
Segue abaixo as informações dos parâmetros:

**Início, Fim e Tolerância diária:** Defina em qual período o sistema irá calcular Adicional Noturno, e se haverá uma tolerância.  
Exemplo:

Início: 22:00 - Fim: 05:00 - Tolerância: 01:00

**Abate tolerância de adicional noturno** Habilitando esse parâmetro as horas de tolerância de adicional noturno serão abatidas no adiciona noturno realizado pelo funcionário.  
**Calcula adicional noturno para o intervalo de refeição** Habilitando esse parâmetro caso o funcionário tenha uma Ausência Planejada (Intervalo de Refeição) cadastrado em seu horário o sistema irá inserir as horas do intervalo no cálculo de adicional noturno.  
  
**Observação:** Para funcionários que utilizam Horário por Jornada, o intervalo de refeição será calculado caso:

* O campo 'Tempo de Refeição' no cadastro do índice da jornada seja maior que 00:00;
* Deverá ter interseção com o adicional noturno conforme configuração do Parâmetro do sindicato;
* Como o horário por jornada não possui intervalo de refeição, será considerado o primeiro intervalo do horário executado, independente se existir mais de um intervalo no horário.

**Considera percentual de adicional noturno** Habilitando esse parâmetro o sistema irá calcular o adicional noturno considerando o seu percentual, para cada 00:52.5 equivale a sessenta minutos.  
  
**Considera 1 hora de nona hora a cada 7 horas de adicional noturno** Habilitando esse parâmetro o sistema irá adicionar 00:08 ao evento de nona hora a cada 7 horas realizadas dentro do período de adicional noturno. Caso não trabalhe as 07:00 horas de adicional noturno o sistema fará o cálculo normal de nona hora.  
  
**Considera extras que foram compensadas** Habilitando esse parâmetro o sistema não vai pagar Extra de Adicional Noturno quando a hora extra efetuada no intervalo noturno for compensada com o atraso. O sistema pagará apenas adicional noturno normal.  
  
**Considera executado efetivo no adicional noturno** Habilitando esse parâmetro o sistema irá considerar o executado efetivo após a aplicação da tolerância de batidas caso tenha cadastrado tolerância no horário do funcionário.  
  
**Paga adicional noturno sobre extra não autorizada** Habilitando esse parâmetro o sistema irá pagar extra de adicional noturno para o funcionário mesmo se a extra não estiver sido autorizada.  
  
**Paga nona hora considerando percentual** Habilitando esse parâmetro o sistema irá considerar 14,29% de nona hora para cada hora de adicional noturno.   
  
**Acrescenta a nona hora às horas extras** Ao marcar esse parâmetro o sistema irá adicionar as horas extras de nona hora às horas extras realizadas durante o período de adicional noturno.  
  
**Considera adicional noturno até o fim da jornada** Ao marcar este parâmetro o sistema irá estender o adicional noturno até o fim da jornada do funcionário. E necessário que as horas de trabalho noturno a tenha interseção com o adicional noturno cadastrado nos parâmetros Hora início e Hora fim.  
  
**Para Jornadas iniciadas até [xx : xx] horas** Este parâmetro estipula o horário máximo permitido que a jornada seja iniciada para obtenção do adicional noturno estendido. Somente será editável se o parâmetro "Considera adicional noturno até o fim da jornada" estiver marcado.

Será considerado adicional noturno o intervalo de 22:00 - 07:00 - 09 horas de adicional noturno.  
  
**Importante:** O parâmetro "Para Jornadas iniciadas até [xx : xx] horas" deve ser preenchido com valor de hora que esteja dentro do limite estipulado para cálculo de adicional noturno.

**Obs:** A partir da versão **12.1.2506.122** o parâmetro "**Para Jornadas iniciadas até [xx : xx]**" foi alterado para "**Para jornadas iniciadas entre xx:xx até xx:xx**"  
  
**Para jornadas iniciadas entre xx:xx até xx:xx**: Neste parâmetro, é definido o intervalo de horário em que as jornadas iniciadas dentro desse período terão direito ao adicional noturno estendido.  
A edição deste campo só será possível caso o parâmetro "Considera adicional noturno até o fim da jornada" esteja marcado.

**Saiba Mais**  
Para mais informações acesse o link [Adicional Noturno](https://tdn.totvs.com/display/public/LRM/Adicional+Noturno)
