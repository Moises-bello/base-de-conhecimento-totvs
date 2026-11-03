---
article_id: 22813720816535
category: RH - Férias
content_hash: e4f2661effde5e83a7426c179c274230112eb9e8aa9679ee642d7bad6a3e5f54
fetched_at: '2026-06-28T22:43:59.148477+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Postergar pagamento do 1/3 (um terço) em caso de
  Férias antecipadas (Lei 14.457/2022)
type: support-article
updated_at: '2025-08-06T14:46:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22813720816535-RH-Linha-Protheus-GPE-Postergar-pagamento-do-1-3-um-ter%C3%A7o-em-caso-de-F%C3%A9rias-antecipadas-Lei-14-457-2022
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22813763052311) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Implementada a possibilidade de **postergar o pagamento do 1/3 (um terço) de Férias** em caso de **antecipação de Férias** para empregados enquadrados na regra da Lei 14.457/2022.

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.2210  
  
**Solução**De acordo com a Lei 14.457/2022, o funcionário que possui dependente de até 2 anos (nascimento de filho/enteado, adoção ou guarda judicial), poderá ter suas Férias antecipadas e o **empregador poderá optar** por efetuar o pagamento do **adicional de 1/3 (um terço) de Férias após a sua concessão.**  
As rotinas de calculo de Férias foram atualizadas para validar se o funcionário possui Férias a vencer e dependentes de **até 2 anos** para realizar a postergação. Veja abaixo como é feito:   
  
**→ Funcionário com dois dependentes menores de 2 anos:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33987181781015)

**→ GPEM030 - Férias individuais:**É gerado um *help* em tela, questionando se deseja postergar o pagamento do 1/3 ao calcular antecipação de Férias:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33987181783447)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33987181783959)  
  
**→** Após o calculo, é gravada a informação que o 1/3 foi **postergado:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33987219645079)

**→ GPEM060 - Férias programadas:**Nos parâmetros existe a pergunta **Posterga pagamento 1/3**, desta forma o sistema irá validar se existem empregados enquadrados na regra para prosseguir com a postergação:  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/33987219646487)**

**→** As verbas de 1/3 serão gravadas na rotina de **Valores Futuros** com data de 20/12. Caso seja necessário **antecipar o pagamento para outra data**, a alteração deve ser feita **manualmente** com a data de pagamento escolhida:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33987219647639)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33987181787543)

**OBS:** **NÃO será efetuada a postergação do Abono Pecuniário**, pois na Lei não existe previsão legal para a postergação desse valor como havia no artigo 8 da MP 1.046/2021.

**Saiba Mais:**[Lei 14.457/2022 (Programa Emprega + Mulheres)](https://tdn.totvs.com/pages/releaseview.action?pageId=781211063)   
[RH - Linha Protheus - GPE - Como cancelar cálculo de férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhWrrPUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBhWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MDgzMDkzNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jYW5jZWxhci1jJUMzJUExbGN1bG8tZGUtZiVDMyVBOXJpYXMGOwhUOg5zZWFyY2hfaWRJIillNmRiZjU3OS1iMjNlLTQ0MTItYjVlNi0zODk4YTk2OTEwNWQGOwhGOglyYW5raQg6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhhjw6FsY3VsbyBkZSBmw6lyaWFzBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--505bedfa92604acd2aabd6c1dd43265099fc98b3)  
[RH - Linha Protheus - GPE - Como visualizar histórico de férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXqHR5bxM6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBi2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzIxMzY5NDk5OTg2MDcxLVJILUxpbmhhLVByb3RoZXVzLUdQRS1Db21vLXZpc3VhbGl6YXItaGlzdCVDMyVCM3JpY28tZGUtZiVDMyVBOXJpYXMGOwhUOg5zZWFyY2hfaWRJIiliMTg4ODYyNy04MzYxLTQ1NzktOGIzMi0wODE2MWVkOTk1MDcGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhloaXN0b3JpY28gZGUgZsOpcmlhcwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--b104b8c490241216dc5c6bc51552c2636608fcba)  
[RH - Linha Protheus - GPE - Como gerar o demonstrativo de Médias para Férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXLXHuBgc6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBl2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzc3MjYzNTE1OTI4NTUtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tZ2VyYXItby1kZW1vbnN0cmF0aXZvLWRlLU0lQzMlQTlkaWFzLXBhcmEtRiVDMyVBOXJpYXMGOwhUOg5zZWFyY2hfaWRJIiliNWQwMzhkOS04MDc1LTRjYTgtODI4MC05NDg2ODcyZWU3YjIGOwhGOglyYW5raQg6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhtkZW1vbnN0cmF0aXZvIGRlIG1lZGlhBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--4949881bbbad506bbf23d077b4abbd32a42d43a8)
