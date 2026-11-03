---
article_id: 360050633394
category: RH - Provisão
content_hash: 30afe27ee40df93b0c4b9c785bf73e41091e524aa91977288eaaa0d56180b7c4
fetched_at: '2026-06-28T22:43:56.873411+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de Provisão de Recesso Antecipado para
  Estagiário
type: support-article
updated_at: '2022-05-11T13:02:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050633394-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-Provis%C3%A3o-de-Recesso-Antecipado-para-Estagi%C3%A1rio
---

**Dúvida**Como Calcular a Provisão com Recesso Antecipado para os Estagiários?  
  
**Ambiente**

 TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**O Cálculo do Recesso de Estagiário, é Realizado pela Rotina Lançamento de Ausências e Folha de Pagamento, não tendo relação com a rotina Controle de Dias de Direito (GPEA050).  
Porém para cálculo das Provisões, o sistema apresenta os Períodos Aquisitivos, portanto é necessário ajustar o Período Aquisitivo de forma manual, para que o sistema calcule corretamente os dias de Recesso Antecipados para os estagiários.  
  
Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Realize o Lançamento do Recesso do Estagiário e Processo da Folha. Para saber como realizar o Cálculo de Recesso Estagiário [Clique Aqui;](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018551291-MP-GPE-Como-calcular-recesso-de-estagi%C3%A1rio-)  
  
2. Acesse: Atualizações / Definições de Cálculo / Verbas , e verifique se os identificadores de Cálculo de Recesso de Estagiário na provisão estão cadastrados:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077873614/mceclip0.png)  
  
3. Acesse: Atualizações / Funcionários / Controle de Dias de Direito / Localize o Estagiário e clique em "+ Manutenção" e preencha o campo "**Dias Pagos**" (RF\_DFERANT) com a quantidade de dias de Recesso que foram antecipados e clique em Confirmar. No exemplo abaixo, o Estagiário teve 20 dias de Recesso Antecipado, enquanto tinha somente 15 dias de Direito:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079020513/mceclip2.png)  
  
4. Acesse: Miscelanea / Provisões / Provisões de Férias/13ºSalário / Outras Ações / Cálculo e Preencha os parâmetros para cálculo das provisões.  
  
5. Desta forma o sistema calcula as Baixas do Recesso do Estagiário, e preenche o campo "Dias Ferias Antecip" com os dias antecipados.  
Os dias de Recesso serão zerados, pois foram antecipados mais dias, o que o funcionário tem direito:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079020433/mceclip1.png)

**Saiba mais  
[RH - Linha Protheus - GPE - Como realizar cadastro de Estagiário](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgoxKjSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBhWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxNjU2MTE5Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1yZWFsaXphci1jYWRhc3Ryby1kZS1Fc3RhZ2klQzMlQTFyaW8GOwhUOg5zZWFyY2hfaWRJIik5YTA5ZWYyYy1kZjkwLTRmZTUtYmMxOC1mZGMxZDYzMDMzM2QGOwhGOglyYW5raQ86C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhdyZWNlc3NvIGVzdGFnaWFyaW8GOwhUOhJyZXN1bHRzX2NvdW50aQHD--5f53637d38d38bb123f81b098394301c135042f0)**
