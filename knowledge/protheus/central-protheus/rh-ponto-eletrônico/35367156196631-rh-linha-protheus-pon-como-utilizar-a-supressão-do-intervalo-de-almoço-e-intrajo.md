---
article_id: 35367156196631
category: RH - Ponto Eletrônico
content_hash: 69a5909623972ea0415628bc163f481af6c54ae2802e5ef0af2db5876fe718b3
fetched_at: '2026-06-28T22:44:58.240436+00:00'
product: protheus
section_id: 206956208
source: central-protheus
title: RH - Linha Protheus - PON - Como utilizar a Supressão do intervalo de almoço
  e intrajornada da Sumula 437
type: support-article
updated_at: '2025-11-21T18:56:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35367156196631-RH-Linha-Protheus-PON-Como-utilizar-a-Supress%C3%A3o-do-intervalo-de-almo%C3%A7o-e-intrajornada-da-Sumula-437
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35367156129175) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**  
Como utilizar a Supressão do intervalo de almoço e intrajornada da Sumula 437?  
  
**Ambiente**  
TOTVS RH - TOTVS RH ( Linha Protheus ) Ponto Eletrônico - Todas as versões  
  
**Solução**  
Para atender a **Súmula 437** - Intervalo da intrajornada para repouso e alimentação, será necessário além de gerar o evento de hora extra no intervalo gerar o evento indenizatório com a quantidade total de horas do intervalo ou apenas com o excedente realizado no intervalo, conforme a consultoria jurídica abaixo:  
[Orientações Consultoria de Segmentos - Interjornada - 3.2 Supressão do Intervalo do Almoço](https://tdn.totvs.com/pages/releaseview.action?pageId=144412479#Orienta%C3%A7%C3%B5esConsultoriadeSegmentosInterjornadaPer%C3%ADodom%C3%ADnimode11horasconsecutivasparadescanso.-3.2Supress%C3%A3odoIntervalodoAlmo%C3%A7o)  
  
Como foi disponibilizado na regra de apontamento os campos:**Pg. Int. Tot**(PA\_PGINTOT),**Inden. Sumul(**PA\_INDESUM),**Tol. Súmula** (PA\_TOLSUML) e **Limite Suml** (Limite Suml ), bem como o ID do Ponto 048A (INDENIZAÇÃO SÚMULA 437). Se tem por requisito a aplicação da atualização liberada no pacote de expedição do módulo RH a partir de **19/08/2024**e da execução do **UPDDISTR** com o dicionário diferencial.  
  
**Cadastro da Regra de Apontamento:**  
Acessando módulo 16-**SIGAPON, Em atualizações-Cadastro do Ponto-Regra de Apontamento, Aba Súmula 437**  
Temos os campos abaixo:  
**Pg. Int. Tot**(PA\_PGINTOT)->Informe se no intervalo deve ser pago apenas os minutos realizados de Hora Extra ou o período completo conforme súmula 437.  
**Inden. Sumul(**PA\_INDESUM)->Quando o Campo Inden. Sumul estiver com **Sim**, o campo **Tol. Súmula**será liberado para edição e o valor preenchido nele, será a tolerância que o sistema utilizará para verificar se deve gerar o evento indenizatório da Súmula.  
**Tol. Súmula** (PA\_TOLSUML)->Informe a quantidade de Tolerância para que seja gerado o evento indenizatório da Súmula 437. A tolerância só será utilizada se o campo Inden. Sumul (PA\_INDESUM) estiver com Sim.  
**Limite Suml** (PA\_LIMSUML)->Limite do intervalo que será considerado para a geração da Súmula 437, sendo o valor máximo da indenização.  
  
**Exemplo prático:**  
Quando o Campo **Inden. Sumul** estiver com **Sim**, o campo **Tol. Súmula**será liberado para edição e o valor preenchido nele, será a tolerância que o sistema utilizará para verificar se deve gerar o evento indenizatório da Súmula.

Quando o Campo **Inden. Sumul** estiver com **Não**, como não será gerado qualquer evento indenizatório a tolerância da indenização será desativada e não será utilizado no apontamento das marcações.

Configuração da regra de apontamento utilizando a tolerância da indenização.   
Quando possui uma tolerância de HE 0,10 no dia do expediente e 0,01 minuto de tolerância para a indenização da intrajornada/Sumula 437:  
  
**Cadastro de** **Eventos(SIGAPON-atualizações-cadastro do ponto-eventos), efetue o cadastro do evento ID 048A (INDENIZAÇÃO SÚMULA 437):**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35380064150807)  
  
**Regra de Apontamento/Aba Súmula 437(em SIGAPON-Atualizações-cadastro do ponto-Regra de apontamento):**  
Informe os campos de acordo com a necessidade de sua regra.  
O exemplo abaixo aplicará 0,01 minuto de tolerância e o limite da intrajornada é de 01:00.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35380064153111)  
  
**Tabela de horário Padrão(SIGAPON-Atualizações-cadastro do ponto-Tabela de horário padrão).**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/35380064154007)**

**Apontamentos do funcionário(SIGAPON-Atualizações-lançamentos-integrados):**

No exemplo abaixo a hora extra de intervalo ultrapassou por conta do intervalo seria 01:30 na tabela de horário e foi descansado 00:58 minutos, por isso gerou 00:32 de HE INTERVALO e 00:02 de INDEN INTRAJORNADA SUMULA 437:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35382539541911)

No exemplo abaixo a tolerância do dia para indenização da intrajornada não foi ultrapassada gerando assim somente as horas extras do intervalo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35382556360471)

As tolerâncias do expediente no dia foi ultrapassada, com isso foram geradas todas as horas extras realizada no dia e a tolerância da indenização também foi ultrapassada, com isso será gerado o evento indenizatório.  
  
HORAS EXTRAS referente a saída das 18:00 as 18:10=00:10 HE   
HORAS EXTRAS intervalo das 12:50 as 13:30=00:40 HE INTERVALO  
INDENIZAÇÃO DA SUMULA 437 das 12:50 as 13:00=00:10 INDEN INTRAJORNADA DA SUM 437

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35382539544855)

Quanto a utilização do campo **Limite Suml** (PA\_LIMSUML) estiver preenchido com 1,00 mesmo que na tabela de horário, por exemplo, estiver com 01:30 de intervalo, o sistema limitará 01:00 para validação da violação da intrajornada. Veja exemplo prático:  
Com a mesma regra Gera somente 0,30 minutos de horas extras no intervalo, mas não gera a Sumula 437:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35380064156055)  
  
Se descansar 00:30 minutos de intervalo gera 01:00 de horas extras no intervalo e 0,30min da Inden da Sumula 437(ID: 048a), veja:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35380064156951)  
  
Saiba mais,  
[Supressão do intervalo de almoço / intrajornada](https://tdn.totvs.com/pages/releaseview.action?pageId=861550459)  
[Supressão do intervalo de almoço intrajornada Sumula 437](https://tdn.totvs.com/pages/releaseview.action?pageId=849086512)  
[Aplicação da tolerância das horas de supressão intrajornada](https://tdn.totvs.com/pages/releaseview.action?pageId=867160430)  
[Manual do Ponto](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Atualização da Expedição Continua do RH](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/rh_expedicao)
