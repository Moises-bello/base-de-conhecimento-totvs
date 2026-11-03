---
article_id: 25827164020759
category: Financeiro - Cadastros
content_hash: ef9258fe04fa81f6b4008c7552ad2fbea7ccc2fd9b6e4402e002e8ddda49a5b8
fetched_at: '2026-06-28T22:37:53.191500+00:00'
product: protheus
section_id: 1500001550722
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - Banco não
  aparece para configuração da conta
type: support-article
updated_at: '2024-09-06T11:01:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25827164020759-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Banco-n%C3%A3o-aparece-para-configura%C3%A7%C3%A3o-da-conta
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25827173244183) Tempo aproximado para leitura: **00****:03:00 min** **Dúvida**Porque o banco não aparece para configurar a conta?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**O requisito para que o banco apareça na seleção, é o preenchimento do campo **A6\_BCOOFI** na rotina de **Cadastro de Bancos MATA070.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25827164004631)**

Caso esteja com o banco oficial preenchido e mesmo assim não apareça, deve verificar se está selecionando a filial do banco que quer realizar o cadastro no botão do print a seguir:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26168982494871)**

**Importante:**O campo ****A6\_BLOCKED**** deve estar igual a 2**.**
