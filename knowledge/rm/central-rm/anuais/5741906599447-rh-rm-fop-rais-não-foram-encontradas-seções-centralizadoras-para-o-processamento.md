---
article_id: 5741906599447
category: Anuais
content_hash: 236eaebb58173bd10dcf37192bfe5f463eee141d21dd04118451fc2e01baaccf
fetched_at: '2026-06-28T22:46:51.060304+00:00'
product: rm
section_id: 1500000861142
source: central-rm
title: 'RH - RM - FOP - RAIS: Não foram encontradas seções centralizadoras para o
  processamento'
type: support-article
updated_at: '2025-03-13T09:57:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5741906599447-RH-RM-FOP-RAIS-N%C3%A3o-foram-encontradas-se%C3%A7%C3%B5es-centralizadoras-para-o-processamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:45 min  
  
Dúvida**Como corrigir o erro: **Não foram encontradas seções centralizadoras para o processamento. Verifique se o Código de Quebra está correto.****Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para correção do erro, será necessário a validação da estrutura de máscaras utilizadas, a quebra de CNPJ e de seções:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5741660908439/mceclip0.png)  
  
Verifique em configurações| Parametrizador | Máscaras e Códigos de Quebra:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5741742951191/mceclip1.png)  
  
Na geração da RAIS, em Anuais, nos parâmetros da coligada, desmarcar a flag:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5741739109911/mceclip2.png)  
  
Dessa forma, gere o arquivo novamente e importe no validador.

***Informações gerais sobre a RAIS 2022****Foi publicado no* [*Portal da RAIS*](https://www.rais.gov.br/sitio/index.jsf) *no dia 15/03/2022 o Manual e o Leiaute relativos ao Ano Base 2021. A adequação é apenas no campo de identificação do trabalhador* ***PIS/PASEP/NIT****, passando a ser facultativo, de acordo com o Manual de Orientação da RAIS ano-base 2021. O Programa Validador da RAIS –* ***GDRAIS2022****, está disponível no portal para download, então já é possível preparar-se para a transmissão da RAIS, uma vez que* ***para a linha RM, não será necessária adequação do produto****. As versões que atenderão a rotina serão as mesmas que atenderam a DIRF 2022:*

* *12.1.32.241 ou superiores;*
* *12.1.33.178 ou superiores;*
* *12.1.34.100 ou superiores.*

*Ressaltamos que, a entrega da RAIS para os Grupos 1 e 2 já foram substituídas pelo envio mensal dos eventos de remuneração no eSocial desde 2019, e para estes grupos está bloqueado o envio através do GDRAIS.*
