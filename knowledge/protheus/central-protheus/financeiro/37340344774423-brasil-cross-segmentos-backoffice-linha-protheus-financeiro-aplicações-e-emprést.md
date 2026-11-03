---
article_id: 37340344774423
category: Financeiro
content_hash: a78065d7c6fbe2bd8b511d4308caa435ccd98b02ccfee032aaf309a4de719724
fetched_at: '2026-06-28T22:38:01.027539+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Brasil - Cross Segmentos - Backoffice (Linha Protheus) - Financeiro - Aplicações
  e empréstimos - Erro A171DELETA - Não foi possível excluir o contrato
type: support-article
updated_at: '2025-12-31T11:00:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37340344774423-Brasil-Cross-Segmentos-Backoffice-Linha-Protheus-Financeiro-Aplica%C3%A7%C3%B5es-e-empr%C3%A9stimos-Erro-A171DELETA-N%C3%A3o-foi-poss%C3%ADvel-excluir-o-contrato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37340336566807) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Por que ocorre o erro 500 - Não foi possível excluir o contrato (A171DELETA) ao tentar excluir uma Aplicação ou Empréstimo no módulo Financeiro?  
  
  
**Solução**  
Uma das causas do help **A171DELETA** ocorre quando o sistema identifica que o contrato de aplicação ou empréstimo possui marcas de processamento que impedem sua exclusão. Esse bloqueio é acionado quando o campo **EH\_ULTAPR** está preenchido.  
  
Quando esse campo contém informação, o Protheus entende que já houve movimentação de juros ou apropriação para o contrato. Nessa situação, a exclusão é bloqueada de forma nativa pela rotina, com o objetivo de preservar a integridade dos saldos e dos dados financeiros.  
  
Dessa forma, **quando o campo EH\_ULTAPR estiver vazio, o que indica que não existe movimentação de juros ou apropriação, a mensagem não ocorrerá**, permitindo a exclusão do contrato pela rotina padrão do sistema.  
  
Recomenda-se validar se o ambiente está com **dicionário e binários atualizados**. Permanecendo o cenário em ambiente atualizado, não havendo movimentações e campo preenchido, será necessário coletar evidências detalhadas de todo o ciclo do contrato para análise pelo suporte.

**Saiba mais:** [**Aplicações e empréstimos - FINA716 - Financeiro P12**](https://tdn.totvs.com/pages/viewpage.action?pageId=680254799)
