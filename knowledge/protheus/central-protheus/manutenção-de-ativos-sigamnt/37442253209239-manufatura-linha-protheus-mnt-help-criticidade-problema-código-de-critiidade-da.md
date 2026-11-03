---
article_id: 37442253209239
category: Manutenção de Ativos (SIGAMNT)
content_hash: 922b4968e873492d37cf9b62099a8276bef16ced4b2797585d602f5015ed28ac
fetched_at: '2026-06-28T22:42:34.093892+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: 'Manufatura - Linha Protheus - MNT - HELP: Criticidade Problema: Código de
  critiidade da peça de reposição'
type: support-article
updated_at: '2026-01-05T16:39:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37442253209239-Manufatura-Linha-Protheus-MNT-HELP-Criticidade-Problema-C%C3%B3digo-de-critiidade-da-pe%C3%A7a-de-reposi%C3%A7%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37442253206551)*** Tempo aproximado para leitura: **00:01:06 min**  
  
**Ocorrência**  
Ao tentar realizar o processo de **Incluir ou alterar um bem para informar peças de reposição** é apresentado a mensagem **HELP: NAOBEMPADR Problema: Código da família padrão não cadastrado**  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Causa**  
A situação pode estar acontecendo devido ao campo **TPY\_CRITIC - Criticidade da Peça** da tabela **TPY - Peças de Reposição do Bem** estar configurado com um tamanho diferente de 1.  
  
**Solução**  
Considerando que o campo é uma lista o tamanho do campo **deve ser tamanho 1**. Nesse sentido será necessário ajustar / atualizar o tamanho do campo no dicionário de dados no SIGACFG.

**Saiba Mais**  
Para informações complementares a respeito da atualização do tamanho de campos no Protheus, verifique o artigo:  
[Framework - Linha Protheus - Como alterar o tamanho de um campo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000583568)
