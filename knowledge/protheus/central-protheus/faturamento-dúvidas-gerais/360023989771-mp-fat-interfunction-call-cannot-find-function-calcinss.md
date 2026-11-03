---
article_id: 360023989771
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 8407e9d99164c3e930c0cc7a306ec9dbf2894625799e6052aea49dea98060e9c
fetched_at: '2026-06-28T22:38:31.238502+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'MP-FAT-Interfunction call: cannot find function CALCINSS '
type: support-article
updated_at: '2021-04-28T15:54:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023989771-MP-FAT-Interfunction-call-cannot-find-function-CALCINSS
---

**Ocorrência**

Ao gerar o documento de saída (**MATA461**), gera a mensagem: **Interfunction call: cannot find function CALCINSS**.

**Ambiente**

Microsiga Protheus - a partir da release 12.1.17.

**Causa**

A mensagem ocorre, em razão da função **CALCINSS** não ter sido encontrada no RPO.  
   
 **Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:  
 1. Efetue o download do **FINA040** (Fonte detentor da função) mais atual: [**https://suporte.totvs.com/portal/p/10098/download?e=734555**](https://suporte.totvs.com/portal/p/10098/download?e=734555) ;  
 2. Aplique o pacote via TDS ou antigo IDE para atualização do RPO;  
 3. Reinicie o Smartclient  e refaça o processo de geração do documento de saída.

**Obs: Para aplicação do pacote é necessário que o analista tenha conhecimentos em estrutura Protheus, em caso de dúvidas no processe, acione a equipe de atendimento de Frame Work.**

**Sempre efetue a aplicação do pacote em ambiente de homologação para validar a atualização, e posteriormente aplique em ambiente de produção.**
