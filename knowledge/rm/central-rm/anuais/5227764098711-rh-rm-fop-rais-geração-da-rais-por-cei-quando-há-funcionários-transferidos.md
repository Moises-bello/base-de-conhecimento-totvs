---
article_id: 5227764098711
category: Anuais
content_hash: 897a3bb0b87c1761a120ef42db6b1d6eb681e4512c47a6324ce0658da196c250
fetched_at: '2026-06-28T22:46:51.068794+00:00'
product: rm
section_id: 1500000861142
source: central-rm
title: 'RH - RM - FOP - RAIS: Geração da RAIS por CEI quando há funcionários transferidos'
type: support-article
updated_at: '2025-03-14T10:00:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5227764098711-RH-RM-FOP-RAIS-Gera%C3%A7%C3%A3o-da-RAIS-por-CEI-quando-h%C3%A1-funcion%C3%A1rios-transferidos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:15 min** **Dúvida**Como parametrizo o arquivo da RAIS para que informe o registro de funcionários transferidos para a alteração de CEI?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Na primeira tela da geração da RAIS em **Anuais | RAIS,** há a flag **Gera registro para alteração de CEI**. Esta flag também está presente em algumas etapas posteriores, nos parâmetros específicos da coligada, caso utilize:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5226729147287/mceclip0.png)  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5226723294615/mceclip1.png)  
  
Marcando este parâmetro, o sistema irá verificar em **Cadastros | Funcionários | Históricos | Hist. Seção** as mudanças de seções identificadas por CEI ocorridas no ano base da RAIS. A data de mudança no histórico de seção representará a data de demissão no CEI antigo e a admissão no novo CEI. Para casos de mudança de CEI, a demissão será tipo 4 - sem ônus na seção antiga, e a admissão tipo 31 - sem ônus na nova seção.  
  
**Importante**  
- Se o funcionário não possuir histórico de seção, este funcionário não sairá na RAIS;  
- O sistema irá verificar os meses nos quais o funcionário trabalhou em cada quebra de CEI. Nos meses onde houve a mudança, a movimentação vai para o mês onde o funcionário trabalhou mais dias.

***Informações gerais sobre a RAIS 2022*** *Foi publicado no* [*Portal da RAIS*](https://www.rais.gov.br/sitio/index.jsf) *no dia 15/03/2022 o Manual e o Leiaute relativos ao Ano Base 2021. A adequação é apenas no campo de identificação do trabalhador* ***PIS/PASEP/NIT****, passando a ser facultativo, de acordo com o Manual de Orientação da RAIS ano-base 2021. O Programa Validador da RAIS –* ***GDRAIS2022****, está disponível no portal para download, então já é possível preparar-se para a transmissão da RAIS, uma vez que* ***para a linha RM, não será necessária adequação do produto****. As versões que atenderão a rotina serão as mesmas que atenderam a DIRF 2022:*

* *12.1.32.241 ou superiores;*
* *12.1.33.178 ou superiores;*
* *12.1.34.100 ou superiores.*

*Ressaltamos que, a entrega da RAIS para os Grupos 1 e 2 já foram substituídas pelo envio mensal dos eventos de remuneração no eSocial desde 2019, e para estes grupos está bloqueado o envio através do GDRAIS.*
