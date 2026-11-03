---
article_id: 360004252711
category: RH - Lançamentos
content_hash: 2ca13cd73d084488582746679edf5d79a93b40ed15af55bc1e9ca9e3541ac2ae
fetched_at: '2026-06-28T22:44:46.820013+00:00'
product: protheus
section_id: 32419271673111
source: central-protheus
title: RH - Linha Protheus - PON - Como gerar o Adicional Noturno e o Adicional Noturno
  sobre Horas Extras
type: support-article
updated_at: '2026-01-19T18:01:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004252711-RH-Linha-Protheus-PON-Como-gerar-o-Adicional-Noturno-e-o-Adicional-Noturno-sobre-Horas-Extras
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34204194054807) Tempo aproximado para leitura: 00:01:30 min******Dúvida**Como gerar apontamento de **Adicional Noturno** e de **Adicional Noturno sobre Horas Extras**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**O Protheus trabalha com o pagamento de **dois tipos de Adicional Noturno:**  
**1.** **Adicional noturno:**  o campo **PA\_ADNOT,** na aba Apontamentos da **Regra de Apontamento (Atualizações>Cadastro do Ponto>Regra de Apontamento)** corresponde aos IDs de Ponto **003N e 004A:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32039229529367)  
  
**2.** **Adicional noturno sobre horas extras:**  o campo **PA\_ADNOTEX,**  na Aba Apontamentos da **Regra de Apontamento** corresponde aos IDs de Ponto **027N e 028A:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32039243415831)

No **primeiro caso**, o evento será gerado apenas para os turnos que possuem horas noturnas normais, exemplo: 22:00 - 05:00 ou 23:00 - 06:00.

No **segundo caso**, será gerado quando um funcionário estiver alocado em turno diurno e estender sua jornada até o horário noturno ou quando ocorrer prorrogação da hora noturna. Exemplo: o turno do funcionário é das 19:00 às 07:00, porém, em um dia ele saiu às 08:00; a empresa prorroga o adicional noturno, fazendo com que seja gerado o evento de hora extra noturna juntamente com o adicional noturno sobre horas extras.

Esses campos não existem para indicar se o Adicional Noturno e o Adicional Noturno sobre Horas Extras serão gerados ou não, e sim para determinar:

* Se os campos estiverem como **SIM**, os IDs gerados serão **004A** e **028A**;
* Se os campos estiverem como **NÃO**, os IDs gerados serão **003N** e **027N**.

**3.** Para o correto apontamento do evento de Adicional Noturno sobre Horas Extras, é necessário que o **cadastro dos [Tipos de Horas Extras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060489314-RH-Linha-Protheus-PON-Regras-importantes-para-o-cadastro-dos-Tipos-de-Horas-Extras) (Atualizações>Cadastro do Ponto>Tipos Horas Extras)** esteja correto, conforme exemplo abaixo:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000026282)  
  
**4.** [**Turno de Trabalho**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410322419095-RH-Linha-Protheus-PON-Como-cadastrar-um-Turno-de-Trabalho) **(atualizações>Cadastros Gerais>Turnos de Trabalho)**: neste cadastro, definimos a **hora inicial/final** e o **valor da hora noturna** através dos **campos Ini. Hora Not., Fim Hora Not. e Min. Hora Not.**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32039229533463)  
  
**5.** Os campos **Con. H. N. Tab. e Con. H. N. Tb. I.** são responsáveis por fazer a conversão das horas de trabalhado cadastradas na Tabela de Horário Padrão em hora noturna, portanto, sempre deverão estar como **SIM**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32039229534487)  
  
**6.** **[Tabela de Horário Padrão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047920293-RH-Linha-Protheus-PON-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o) (Atualizações>Cadastro do Ponto>Tabela e Horário Padrão)**: além de cadastrar corretamente os horários que serão praticados pelo funcionário, é necessário **apontar quais serão os tipos de horas extras apontados em cada um dos dias, para quando ocorrer hora extra noturna e for gerado o adicional noturno sobre horas extras**, conforme exemplo abaixo:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098906894)  
  
**Saiba Mais**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[MP - PON - Como funciona a troca de turno dos funcionários?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015528671-MP-PON-Como-funciona-a-troca-de-turno-dos-funcion%C3%A1rios-?source=search)  
[MP - PON - Como efetuar o cadastro do Relógio Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004209412-MP-PON-Como-efetuar-o-cadastro-do-Rel%C3%B3gio-Ponto?source=search)  
[MP - PON - Como funciona a troca de turno dos funcionários?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015528671-MP-PON-Como-funciona-a-troca-de-turno-dos-funcion%C3%A1rios-?source=search)  
[MP - PON - Tabela de Horário Padrão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047920293-MP-PON-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o-?source=search)   
[MP - PON - Como gerar os Apontamentos no SIGAPON?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052257014-MP-PON-Como-gerar-os-Apontamentos-no-SIGAPON-?source=search)
