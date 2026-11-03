---
article_id: 4409758704663
category: esocial - Periódicos
content_hash: 0c89d5a00d7316d5997cd9a7884e3285ba6c9ffb6780251e499f0eb792c9638c
fetched_at: '2026-06-28T22:47:09.268064+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 163 ao transmitir S-1299: Trabalhador sem vinculo
  consta na base do eSocial mas não foi informada sua remuneração'
type: support-article
updated_at: '2024-12-30T12:31:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409758704663-RH-RM-FOP-eSocial-Erro-163-ao-transmitir-S-1299-Trabalhador-sem-vinculo-consta-na-base-do-eSocial-mas-n%C3%A3o-foi-informada-sua-remunera%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24454907632791) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao realizar a transmissão do S-1299 referente ao período de apuração mensal para o governo é retornado a inconsistência **O Trabalhador sem vinculo com Nome : X, CPF : XXXXXXXXXXX, NIS : XXXXXXXXXXX e Categoria : XXX consta na base de dados do Ambiente Nacional do eSocial, mas não foi informada sua remuneração. Ação Sugerida: Verificar se a falta de informação e decorrente de dificuldades operacionais ou se e possível efetuar a regularização.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28859547446551)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**A inconsistência apresentada indica que existem Trabalhadores Sem Vínculo, porém não foram enviados os eventos de remuneração (**S-1200**) para o ambiente do eSocial.   
  
**Solução**Para solucionar essa ocorrência, efetue as seguintes validações:

• **Avisos** retornados RETConforme descrito na tabela de regras do eSocial existindo um ou mais trabalhadores sem vínculo **ativos** no período de apuração da folha de pagamento e que não enviado o evento de remuneração (**S-1200**), o evento de fechamento é aceito como válido, no entanto, são gerados Avisos.

![33333.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409772048663)  
Regras de validação **REGRA\_VALIDA\_FECHAMENTO\_FOPAG**

• **Falta** do registro de **Remuneração**  
Para casos em que há obrigação do envio do evento **S-2300,** é necessário o envio de um evento de remuneração (**S-1200**), com exceção dos Trabalhadores em determinadas situação de afastamento preestabelecidas no [Leiaute](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica) do **eSocial.**  
  
**Saiba Mais**Para mais informações acesse: 

* [Utilização do evento S-2300 - Trabalhador Sem Vínculo do Emprego / Estatutário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015286312-RM-eSocial-Utiliza%C3%A7%C3%A3o-do-evento-S-2300-Trabalhador-Sem-V%C3%ADnculo-do-Emprego-Estatut%C3%A1rio-In%C3%ADcio?source=search)
* [Gerar XML Periódicos](https://tdn.totvs.com/pages/releaseview.action?pageId=452719232)
* [Evento S-1200 para autônomos cuja categoria não demandam o envio do evento S-2300](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015427792-RH-RM-FOP-eSocial-Evento-S-1200-para-aut%C3%B4nomos-cuja-categoria-n%C3%A3o-demandam-o-envio-do-evento-S-2300?source=search)
