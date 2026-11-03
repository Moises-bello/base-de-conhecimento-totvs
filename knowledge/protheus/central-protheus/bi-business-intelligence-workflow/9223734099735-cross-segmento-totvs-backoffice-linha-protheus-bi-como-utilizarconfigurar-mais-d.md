---
article_id: 9223734099735
category: BI - Business- Intelligence - Workflow
content_hash: 98f9172f0280880afd6c1da9fcf7f922a8e1d87996b1989b0a50ad2ae1d2510f
fetched_at: '2026-06-28T22:37:03.100165+00:00'
product: protheus
section_id: 1500001550762
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Como utilizar/configurar
  mais de uma empresa ou filial no WorkFlow
type: support-article
updated_at: '2022-09-29T18:25:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9223734099735-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Como-utilizar-configurar-mais-de-uma-empresa-ou-filial-no-WorkFlow
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min****Dúvida**Há possibilidade do sistema trabalhar com mais de uma Empresa/Filial para disparo no WF?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Workflow – A partir da versão 11.80  
  
**Solução**É possível trabalhar com mais de uma empresa/filial para disparo do Workflow através de uma mesma caixa de e-mail. Para isto, a tabela de empresa/filial deve ser compartilhada e **não deve** ser utilizado, tanto no appserver.ini como em fonte customizado, a chave "***Prepare Environment/ PrepareIn***" pois como o nome sugere, está chave/comando irá preparar o ambiente para uma determinada empresa/filial o que acarretará em erro no caso de tentativa de disparo por uma empresa/filial não configurada no parâmetro.   
O produto Workflow possui configuração para através da informação de empresa/filial em que o usuário está logado, carregar estas informações para o disparo do e-mail sendo desnecessária sua configuração.  
Não é necessário a criação de nenhum job a mais, a não ser que se utilize o Schedule sendo neste caso a configuração do SchedulerWF.  
  
**Saiba mais**[Cross Segmento - TOTVS Backoffice Linha Protheus - WF - Configuração do ini WorKFlow](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020911512-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-WF-Configura%C3%A7%C3%A3o-do-ini-WorKFlow)
