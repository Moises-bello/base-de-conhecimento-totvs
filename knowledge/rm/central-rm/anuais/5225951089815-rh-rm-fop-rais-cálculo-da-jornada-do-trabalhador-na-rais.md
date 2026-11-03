---
article_id: 5225951089815
category: Anuais
content_hash: 249dbd306e5701349f1cad747f3f2ddd25b5b8b67da19edbcf4cbd849a55709d
fetched_at: '2026-06-28T22:46:51.073238+00:00'
product: rm
section_id: 1500000861142
source: central-rm
title: 'RH - RM - FOP - RAIS: Cálculo da jornada do trabalhador na RAIS'
type: support-article
updated_at: '2025-03-14T10:01:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5225951089815-RH-RM-FOP-RAIS-C%C3%A1lculo-da-jornada-do-trabalhador-na-RAIS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:35 min** **Dúvida**Como é feito o cálculo da jornada de trabalho na RAIS?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**O sistema se vale das informações cadastrais do funcionário para calcular sua jornada. O valor informado no campo **Jornada** será dividido por 5, pois precisa buscar o total de horas semanais:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5225012310167/mceclip0.png)  
  
No exemplo do funcionário acima, a jornada de 220 / 5 = 44:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5225119356439/mceclip1.png)  
  
Mesmo no caso de funcionários horistas, o sistema dividirá o valor do campo por 5.  
  
Para funcionários que possuem salário composto, deve-se atentar para que a soma das jornadas não ultrapasse as 44 horas semanais. Por exemplo:  
  
Salário de número 4 / Jornada 3240  
Salário de número 5 / Jornada 4590  
Salário de número 1 / Jornada 6720  
  
Soma das jornadas em minutos = 14550 / 60 = 242,5 horas mensais.  
  
242,5 / 5 = 48,5 jornada semanal.  
  
Ou seja, no exemplo acima, deve-se verificar qual dos salários está com seu histórico preenchido indevidamente.  
  
Em última instância, caso o usuário não concorde com o cálculo do sistema, é possível inserir uma fórmula durante a geração da RAIS para que o sistema exporte a informação da Jornada conforme o entendimento do usuário. Durante a geração da RAIS, nos parâmetros específicos da coligada, há o campo **Fórmula para cálculo de horas semanais**, onde poderá ser inserida esta fórmula. Importante ressaltar que a inclusão desta fórmula e mudança da lógica de cálculo é de responsabilidade do usuário:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5225859022103/mceclip2.png)

***Informações gerais sobre a RAIS 2022*** *Foi publicado no* [*Portal da RAIS*](https://www.rais.gov.br/sitio/index.jsf) *no dia 15/03/2022 o Manual e o Leiaute relativos ao Ano Base 2021. A adequação é apenas no campo de identificação do trabalhador* ***PIS/PASEP/NIT****, passando a ser facultativo, de acordo com o Manual de Orientação da RAIS ano-base 2021. O Programa Validador da RAIS –* ***GDRAIS2022****, está disponível no portal para download, então já é possível preparar-se para a transmissão da RAIS, uma vez que* ***para a linha RM, não será necessária adequação do produto****. As versões que atenderão a rotina serão as mesmas que atenderam a DIRF 2022:*

* *12.1.32.241 ou superiores;*
* *12.1.33.178 ou superiores;*
* *12.1.34.100 ou superiores.*

*Ressaltamos que, a entrega da RAIS para os Grupos 1 e 2 já foram substituídas pelo envio mensal dos eventos de remuneração no eSocial desde 2019, e para estes grupos está bloqueado o envio através do GDRAIS.*
