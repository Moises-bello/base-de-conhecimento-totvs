---
article_id: 360033930194
category: CRM - Dúvidas Gerais
content_hash: 2f7ef92a6622887a12ca1f0de2c38bcaacef3d58448fbb7a194646021295fe5f
fetched_at: '2026-06-28T22:40:27.569030+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: 'MP-CRM-HELP: TK340INVHC'
type: support-article
updated_at: '2021-04-28T14:49:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033930194-MP-CRM-HELP-TK340INVHC
---

**Dúvida**

Ao informar a hora inicial e final na grade do evento (**TMKA340**), ocorre o help: **TK340INVHC**

![tk340invhc.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360044627273/tk340invhc.jpg)  
 **Ambiente**

Microsiga Protheus - a partir da versão 12.  
  
**Solução**A mensagem ocorre quando o sistema valida os campos de data e hora do cabeçalho do evento( tabela **ACD)** com os campos de data e hora da grade de eventos (tabela **ACE)**, onde, se não for informado as informações hora inicial e final , o sistema ficará validando e solicitando a informação do cabeçalho.

![evento.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360044627633/evento.jpg)

Caso o ambiente não possua todos os campos do cabeçalho, conforme a imagem acima, é indicado efetuar o download do dicionário de dados brasil completo  para a versão e release em que se encontra e rodar o **Upddistr** para atualização das tabelas.

**Obs...Para atualização de dicionários, requer conhecimentos de estrutura Protheus, em caso de dúvida no procedimento, acione a equipe de Frame Work.**
