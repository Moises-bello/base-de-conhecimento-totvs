---
article_id: 23155232257047
category: ADVPL - Classe e Função
content_hash: dd330bfb62cc13bd7cd763f108735ecf154d6c17c075c31f971c6e7deecc1167
fetched_at: '2026-06-28T22:40:20.715816+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Erro: variable
  does not exist CEMPANT on RETSQLNAME(APLIB070.PRW) '
type: support-article
updated_at: '2024-04-30T14:09:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23155232257047-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-variable-does-not-exist-CEMPANT-on-RETSQLNAME-APLIB070-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23155232220311)Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**Ao executar uma rotina customizada é apresentado o erro: variable does not exist CEMPANT on RETSQLNAME(APLIB070.PRW).  
  
**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Causa**O erro reportado "variable does not exist CEMPANT on RETSQLNAME(APLIB070.PRW)" significa que o ambiente não está aberto no momento da execução de sua customização ou por algum motivo foi fechado.

**Solução**

Para realizar a abertura de ambiente utilize a função RPCSETENV() ou Prepare Environment, no qual irá inicializar o ambiente.

**Saiba mais**

[RPCSETENV](https://tdn.totvs.com.br/pages/releaseview.action?pageId=6814927)

[Prepare Environment](https://tdn.totvs.com.br/display/public/framework/Prepare+Environment)
