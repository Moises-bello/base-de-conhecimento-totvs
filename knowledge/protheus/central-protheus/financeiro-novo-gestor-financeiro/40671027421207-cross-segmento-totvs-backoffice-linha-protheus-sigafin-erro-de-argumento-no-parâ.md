---
article_id: 40671027421207
category: Financeiro - Novo Gestor Financeiro
content_hash: 356e0d33d26283fa44beb97be2d3e7a061fa91b44616596f24c3cb9e0076a150
fetched_at: '2026-06-28T22:37:41.530193+00:00'
product: protheus
section_id: 33830415324183
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Erro de argumento
  no parâmetro cTitle previsto C para U na rotina FINA711
type: support-article
updated_at: '2026-05-22T20:38:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40671027421207-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-Erro-de-argumento-no-par%C3%A2metro-cTitle-previsto-C-para-U-na-rotina-FINA711
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40670981086871)** Tempo aproximado para leitura: **00:09:00 min**  
  
**Dúvida**  
Como corrigir a ocorrência do erro "argumento #07 , parâmetro cTitle erro, previsto C->U on BOPROTHEUSEVENTVIEWER:UPDEVENT(BOPROTHEUSEVENTVIEWER.PRW)" durante a tentativa de processamento da rotina FINA711?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Todas as releases  
  
**Solução**

Este comportamento está relacionado a conflitos entre as versões do Schedule (estrutura anterior versus nova estrutura), ocorrendo quando permanecem vestígios de dados de agendamentos anteriores no ambiente.

Para a resolução do problema, é necessária a eliminação do agendamento atual da rotina FINA711 e a sua posterior recriação dentro da nova estrutura do Schedule. Também é fundamental realizar a limpeza completa de tarefas residuais vinculadas ao agendamento anterior diretamente pela interface do Schedule (PO-UI), eliminando registros antigos pendentes para evitar novos conflitos de execução.

Passos:

1. Acessar o módulo correspondente e abrir a ferramenta do Schedule (interface PO-UI).
2. Localizar o agendamento atual configurado para a rotina FINA711 e realizar a sua exclusão.
3. Acessar a gerência de tarefas no Schedule e remover todos os registros residuais do agendamento anterior que apresentem os status Aguardando Execução e Executando.

Recriar o agendamento para a rotina FINA711 mantendo as configurações e parâmetros necessários, assegurando que o registro seja gerado sob a nova arquitetura do Schedule.
