---
article_id: 5377190562199
category: Anuais
content_hash: 400bd6d99090fdedc41a3905e647898356a782a5eae773340726d263ec53e346
fetched_at: '2026-06-28T22:46:51.063789+00:00'
product: rm
section_id: 1500000861142
source: central-rm
title: 'RH - RM - FOP - RAIS: Erro 0010 - Quantidade de Horas Semanais é de preenchimento
  obrigatório'
type: support-article
updated_at: '2025-03-13T09:58:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5377190562199-RH-RM-FOP-RAIS-Erro-0010-Quantidade-de-Horas-Semanais-%C3%A9-de-preenchimento-obrigat%C3%B3rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Ao importar o arquivo da RAIS no validador, é apresentado o erro 0010 - Quantidade de Horas Semanais é de preenchimento obrigatório. Como resolver?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Este erro ocorre porque o campo Jornada no cadastro do funcionário está vazio por algum motivo ou porque há falta de Histórico Salarial para o funcionário.  
  
Para resolver, certifique-se do preenchimento do campo em **Administração de Pessoal | Funcionários |** selecione o **Funcionário | Editar | Salário / Jornada | Jornada**:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5376709047191/mceclip0.png)  
  
Verifique também se há pelo menos um registro de Histórico Salarial em **Históricos | Histórico Salarial**.

***Informações gerais sobre a RAIS 2022****Foi publicado no* [*Portal da RAIS*](https://www.rais.gov.br/sitio/index.jsf) *no dia 15/03/2022 o Manual e o Leiaute relativos ao Ano Base 2021. A adequação é apenas no campo de identificação do trabalhador* ***PIS/PASEP/NIT****, passando a ser facultativo, de acordo com o Manual de Orientação da RAIS ano-base 2021. O Programa Validador da RAIS –* ***GDRAIS2022****, está disponível no portal para download, então já é possível preparar-se para a transmissão da RAIS, uma vez que* ***para a linha RM, não será necessária adequação do produto****. As versões que atenderão a rotina serão as mesmas que atenderam a DIRF 2022:*

* *12.1.32.241 ou superiores;*
* *12.1.33.178 ou superiores;*
* *12.1.34.100 ou superiores.*

*Ressaltamos que, a entrega da RAIS para os Grupos 1 e 2 já foram substituídas pelo envio mensal dos eventos de remuneração no eSocial desde 2019, e para estes grupos está bloqueado o envio através do GDRAIS.*
