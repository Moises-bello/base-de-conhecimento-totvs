---
article_id: 360021618392
category: Integrações Outros BackOffice
content_hash: 0f9c7c34dba975c86f5406abe0bea23280a7922bd8b65ee84835a3da81be8aed
fetched_at: '2026-06-28T22:46:42.205127+00:00'
product: rm
section_id: 4410716084503
source: central-rm
title: 'RM - FOP - Integração RM Labore x BackOffice Protheus: Erro na ACCOUNTANTACCOUNT'
type: support-article
updated_at: '2025-02-10T18:43:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021618392-RM-FOP-Integra%C3%A7%C3%A3o-RM-Labore-x-BackOffice-Protheus-Erro-na-ACCOUNTANTACCOUNT
---

**Ocorrência**Ao realizar a integração do plano de contas entre o RM Folha de Pagamento e o Backoffice Protheus apresenta o seguinte erro: **A entidade 'ACCOUNTANTACCOUNT' não está mapeada para esta integração**.  
   
 **Ambiente**RM - Folha de Pagamento - Todas as versões  
   
 **Causa**O erro é causado quando o plano de contas e a entidade **ACCOUNTANTACCOUNT** estão com as versões diferentes.  
   
 **Solução**Para solucionar o caso, veja os passos a seguir: **01.** Acesse **Integração | Integração | Mensagem Única | Integrações** e selecione a integração do RM Folha de Pagamento x Backoffice Protheus. Depois vá em **Processos | Mapeamento de Entidades**.  
  
**02.** Procure a entidade **ACCOUNTANTACCOUNT** e verifique a versão da entidade. Atualmente é utilizada a versão 2.000.  
 **03.** Para validar se no Protheus consta com a mesma versão do RM, deverá acessar o configurador do Protheus e no castrado do EAI altere a versão do adapter **ACCOUNTANTACCOUNT** caso seja necessário.
