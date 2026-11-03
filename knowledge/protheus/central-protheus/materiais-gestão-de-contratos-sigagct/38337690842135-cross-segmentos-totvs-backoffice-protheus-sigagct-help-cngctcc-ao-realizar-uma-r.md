---
article_id: 38337690842135
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 0a5d5593de5268d9928a215e8c72db7c47d552520a8fa184c48261e8f6c10ff0
fetched_at: '2026-06-28T22:37:22.909821+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Help CNGCTCC ao realizar
  uma Revisão ou Medição de Contratos
type: support-article
updated_at: '2026-02-12T13:09:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38337690842135-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Help-CNGCTCC-ao-realizar-uma-Revis%C3%A3o-ou-Medi%C3%A7%C3%A3o-de-Contratos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38337768110871) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**

O que avaliar na ocorrência do Help CNGCTCC ao se realizar uma Revisão ou Medição de Contratos ?

**Ambiente**

Microsiga – Gestão de Contratos – A partir da versão P12.1.17

**Solução**

A ocorrência da mensagem CNGCTCC está relacionada ao se fazer uma revisão ou uma medição, em haver  nos registros informações de entidade contábil ou centro de custo, **ao mesmo tempo** na aba de "Rateio Contábil por Item" (tabela **CNZ**) da Medição/Contrato e também no Item da planilha (tabela **CNE** na Medição ou **CNB** no Contrato), ambos possuindo ao mesmo tempo a informação (tanto em item de uma planilha já existente anteriormente como também em uma nova que se está incluindo no caso da revisão), sendo que o sistema permite apenas existir entidade contábil ou na aba de rateio ou no item da medição/contrato em seu padrão.  
   
Assim uma analise e verificação no ambiente que pode-se verificar ao se realizar a revisão ou medição, é se possui informação de entidade contábeis tanto na aba de rateio (CNZ), como também no item da planilha do contrato/Medição (CNE ou CNB), e assim havendo, fazer a exclusão/manutenção do registro do item ou da aba de rateio pra que não exista em ambos os lugares (tanto em item de uma planilha já existente anteriormente como também em uma nova que se está incluindo).

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
