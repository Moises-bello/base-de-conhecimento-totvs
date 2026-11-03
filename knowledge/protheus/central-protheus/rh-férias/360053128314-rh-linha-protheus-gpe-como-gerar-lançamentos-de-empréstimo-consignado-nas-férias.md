---
article_id: 360053128314
category: RH - Férias
content_hash: e9b449847679b42ebe27a388a9dbbc713e09c98adbaeda3c5523236a1defbc96
fetched_at: '2026-06-28T22:43:58.143873+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Como gerar lançamentos de empréstimo consignado
  nas Férias
type: support-article
updated_at: '2025-08-06T12:25:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053128314-RH-Linha-Protheus-GPE-Como-gerar-lan%C3%A7amentos-de-empr%C3%A9stimo-consignado-nas-F%C3%A9rias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33983154765079)** Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Como gerar lançamentos de empréstimo consignado no cálculo de Férias?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE - Gestão de Pessoal - Todas as versões  
  
**Solução**

O processo para lançamento de descontos de **Empréstimo** do funcionário nas **férias** é o mesmo para folha de pagamento, porém deve ser observada a informações incluída no campo **Regra Desconto****.****ATENÇÃO**O processo descrito a seguir, referente ao desconto de empréstimo durante o período de férias, **NÃO está relacionado ao desconto do eConsignado/Crédito** Trabalhador (MP 1.292/2025). O programa do governo não prevê o desconto da parcela nas férias, apenas o seu provisionamento. Consulte materiais do eConsignado [aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/sections/32292829000215-eConsignado-Cr%C3%A9dito-do-Trabalhador)

Para realizá-lo, siga os passos conforme abaixo:

1. Acesse o cadastro de **verbas** através do menu **Atualizações > Definições de Cálculo > Verbas.**

2. Inclua uma nova verba sem id de cálculo vinculado

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11175678891159)

3. Acesse a rotina de Valores Futuros no menu **atualizações > lançamentos > valores futuros**.

4. Selecione o funcionário desejado. Clique em **incluir** caso ele não tenha nenhum lançamento fico anterior ou clique**alterar** para informar nova verba.

5. Preencha os campos de acordo com a necessidade, e informe no campo **Regra Desconto**a opção 2 - Férias.

**Exemplo**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11175842510487)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11175949542167)

6. Clique em salvar para gravar o lançamento

7. Calcule as férias do funcionário.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11176100831383)

**Campos importantes**

**Código de verba:** Informe o código da verba cadastrada para desconto do empréstimo consignado;

**Valor Principal:** Valor total do empréstimo concedido ao funcionário;

**Numero de parcelas:** Numero de parcelas a serem descontadas do funcionário para quitação do empréstimo;

**Num. parcelas pagas:** No fechamento do período da folha, este campo é atualizado automaticamente, porém, caso o empréstimo já esteja **em andamento** é necessário preencher este campo com o numero de parcelas já pagas;

**Data do próximo vencimento:** Este campo deve ser preenchido para que o sistema tenha uma base de **quando** iniciará o desconto em folha;

**Emp. Consig:** Este campo é preenchido de forma automática caso o campo **Emp. Consig.** do cadastro de verbas esteja preenchido. Caso não esteja, informe **SIm**.

Per. Inicio: É o período inicial do desconto, a folha em aberto.

Situação: Informa se aquele lançamento este ativo e deve ser calculado na folha.

**Regra de Desconto:** Neste campo é possível selecionar a regra de desconto para o empréstimo. Se **selecionado Folha ou deixar em branco** o sistema sempre descontará da folha de pagamento, portanto nos meses de férias, onde o funcionário não tenha saldo, o desconto ocorrerá e a verba saldo insuficiente será demonstrada no valor como provento e no próximo mês o sistema lança automaticamente essa verba como desconto (quando houver saldo).

Se **selecionado Férias**, o sistema irá descontar na folha de pagamento normalmente e quando houver Férias, **o sistema desconta das férias e não da folha**.

**Saiba Mais**[RH - Linha Protheus - GPE - Como efetuar os lançamentos Futuros](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwivfhbSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBhGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAwNjk3NTE1MS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1lZmV0dWFyLW9zLWxhbiVDMyVBN2FtZW50b3MtRnV0dXJvcwY7CFQ6DnNlYXJjaF9pZEkiKTMzMGMzZjM0LTZiNTQtNGVhYy1hYmFmLWI4YzdlOGM4N2VhMAY7CEY6CXJhbmtpDzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiFHZhbG9yZXMgZnV0dXJvcwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--ea3d17616cbf7cf270463496f3889ad31425f0fe)  
[RH - Linha Protheus - GPE - Como descontar empréstimo consignado na rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwitFD3TUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBlmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyNjI4MTEzMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1kZXNjb250YXItZW1wciVDMyVBOXN0aW1vLWNvbnNpZ25hZG8tbmEtcmVzY2lzJUMzJUEzbwY7CFQ6DnNlYXJjaF9pZEkiKTQ4ZWM5MmYwLTE5ZDktNDMzOC05NTViLTRjMDllNWE0ZTlmYwY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiGHByb3RoZXVzIGVtcHJlc3RpbW8GOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--f86e6cbfaa659fbf05075b930aa1f4abaceea7db)  
[RH - Linha Protheus - GPE - Como controlar as movimentações de Lançamentos Valores Futuros](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiQShDSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBqWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAwNjU2ODU5Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jb250cm9sYXItYXMtbW92aW1lbnRhJUMzJUE3JUMzJUI1ZXMtZGUtTGFuJUMzJUE3YW1lbnRvcy1WYWxvcmVzLUZ1dHVyb3MGOwhUOg5zZWFyY2hfaWRJIikzMzBjM2YzNC02YjU0LTRlYWMtYWJhZi1iOGM3ZThjODdlYTAGOwhGOglyYW5raQw6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhR2YWxvcmVzIGZ1dHVyb3MGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--8e01ec6bc8c240fed08a2cca996d3b8b3edd8186)  
[RH - Linha Protheus - GPE - Como gerar os lançamentos de empréstimo consignado na folha de pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016524552-RH-Linha-Protheus-GPE-Como-gerar-os-lan%C3%A7amentos-de-empr%C3%A9stimo-consignado-na-folha-de-pagamento?source=search)
