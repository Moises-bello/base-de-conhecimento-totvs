---
article_id: 360041858674
category: RH - Férias
content_hash: 0ab8edd9d2bac02645d6a79d5332a63f270c8fa3cd6d67bf34db0ea37b5b74b0
fetched_at: '2026-06-28T22:43:58.329228+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - O que analisar quando o Relatório de Médias de
  Férias apresenta valor diferente do Cálculo das Férias
type: support-article
updated_at: '2025-08-05T19:09:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041858674-RH-Linha-Protheus-GPE-O-que-analisar-quando-o-Relat%C3%B3rio-de-M%C3%A9dias-de-F%C3%A9rias-apresenta-valor-diferente-do-C%C3%A1lculo-das-F%C3%A9rias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24594854690967) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**O que analisar quando o relatório de médias de férias apresenta **valor diferente** do Cálculo das Férias?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

Em alguns casos o sistema pode apresentar um valor diferente no cálculo das Férias em comparação com o **Relatório de Médias (GPER080)** por conta da **parametrização** informada para geração do relatório. Assim, é indicado que a conferência seja realizada gerando o relatório de médias **dentro do cálculo de férias (DEM\_MED),** conforme passo 1.

Em outros casos, o valor das médias no cálculo das Férias, refere-se à coluna **Valor Original**, e não ao **Valor Atual.**Este incidente ocorre quando há divergências nas configurações das **Verbas,** portanto, para solucionar esse incidente, realize os seguintes passos:

**1.** Emitir o Relatório de Médias na rotina de **Cálculo das Férias.**  
Para emissão do Relatório, preencha os dados das Férias e calcule.   
Antes de clicar em Confirmar, clique em **Outras Ações > Relatório de Médias:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/11283489315223)

**2.** É necessário avaliar se o funcionário possui algum adicional que **incorpora ao salário,** como: **Insalubridade, Periculosidade, Adicionais Por Tempo de Serviço** e etc.  
Se as verbas de adicionais da folha estiverem com o campo **Incorpora Salário = Sim** (RV\_INCORP), as verbas de adicionais de Férias **também devem incorporar salário**. Caso não estejam, realize a alteração:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24594854696983)  
  
  
  
**3.** Todas as verbas de **Horas** que compõem o cálculo das Médias (Horas Extras, Adicional Noturno, DSR.) devem estar com o campo **Hora Extra** (RV\_HE) preenchido com **Sim.**  
Caso esteja preenchido com Não, o sistema considera os valores desta verba **como Valor, e com isto, não paga as médias com base no Valor Original**, pois as **verbas em Valor não sofrem reajuste:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24595556508311)  
  
  
  
**4.** A verba de **DSR** deve estar com o campo **Base Cálculo** (RV\_BASCAL) preenchido com **2 - Salário Incorporado**, assim como as demais verbas que compõem as Médias de Férias:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24595556515223)  
  
  
**Saiba Mais**[RH - Linha Protheus - GPE - Cálculo de médias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgKFbLUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSJ8aHR0cHM6Ly9jZW50cmFsZGVhdGVuZGltZW50by50b3R2cy5jb20vaGMvcHQtYnIvYXJ0aWNsZXMvMzYwMDUwNzI2MTU0LVJILUxpbmhhLVByb3RoZXVzLUdQRS1DJUMzJUExbGN1bG8tZGUtbSVDMyVBOWRpYXMGOwhUOg5zZWFyY2hfaWRJIilhMDlmMGUxZC0xYjM4LTQxYjctYjA2MC0yNWExYTllODIwNzMGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhhjw6FsY3VsbyBkZSBtw6lkaWFzBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--f71caa12ac89c0f1318da459f28f7724df7e0583)  
[RH - Linha Protheus - GPE - Como gerar o demonstrativo de Médias para Férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXLXHuBgc6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBl2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzc3MjYzNTE1OTI4NTUtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tZ2VyYXItby1kZW1vbnN0cmF0aXZvLWRlLU0lQzMlQTlkaWFzLXBhcmEtRiVDMyVBOXJpYXMGOwhUOg5zZWFyY2hfaWRJIiljOWI5NmRhMS1kMWJmLTRkZTUtOTZiMy1hYzU1NzgwZWFkZDgGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIlNSSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gQ29tbyBnZXJhciBvIGRlbW9uc3RyYXRpdm8gZGUgTcOpZGlhcyBwYXJhIEbDqXJpYXMGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--d214b9cb72716a9e9623f433d7364b6f72b27879)  
[RH - Linha Protheus - GPE - Coluna Valor Original e Valor Atual Demonstrativo de Médias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiihSPTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBnGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyNDYwNjExNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29sdW5hLVZhbG9yLU9yaWdpbmFsLWUtVmFsb3ItQXR1YWwtRGVtb25zdHJhdGl2by1kZS1NJUMzJUE5ZGlhcwY7CFQ6DnNlYXJjaF9pZEkiKWM5Yjk2ZGExLWQxYmYtNGRlNS05NmIzLWFjNTU3ODBlYWRkOAY7CEY6CXJhbmtpBzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiU1JIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBDb21vIGdlcmFyIG8gZGVtb25zdHJhdGl2byBkZSBNw6lkaWFzIHBhcmEgRsOpcmlhcwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--3282134ad218c6e5bdafc1e57c4bf3244117de17)  
[RH - Linha Protheus - GPE - Como demonstrar o salário Incorporado no Relatório de Médias de Férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgRyX4%2FXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBt2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE1MDAwMDg4NTk5MjEtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tZGVtb25zdHJhci1vLXNhbCVDMyVBMXJpby1JbmNvcnBvcmFkby1uby1SZWxhdCVDMyVCM3Jpby1kZS1NJUMzJUE5ZGlhcy1kZS1GJUMzJUE5cmlhcwY7CFQ6DnNlYXJjaF9pZEkiKTM0N2ZiZmYyLWU0MjYtNDc3My05NjkxLWJhNjYwMjdhYzUzYgY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkia1JIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBDb21vIGRlbW9uc3RyYXIgbyBzYWzDoXJpbyBJbmNvcnBvcmFkbyBubyBSZWxhdMOzcmlvIGRlIE3DqWRpYXMgZGUgRsOpcmlhcwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--18a6a05cc0bba3bcc020a29aa956e03a0dad2962)
