---
article_id: 360020797512
category: ADVPL - Classe e Função
content_hash: 61b33641b2ef8864e6f3bc4dd37b62dde0d0959ad58def5cf3d712550fda0d58
fetched_at: '2026-06-28T22:40:19.475190+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Funcionamento da
  guilhotina em impressora não fiscal
type: support-article
updated_at: '2022-01-10T22:23:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020797512-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Funcionamento-da-guilhotina-em-impressora-n%C3%A3o-fiscal
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**  
Funcionamento da guilhotina em impressora não fiscal  
  
**Ambiente**  
Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Solução**Verificar, em **SIGACFG > Dicionário de Dados > Dicionário de Dados (CFGX031),** se o parâmetro**MV\_FTTEFGU**estiver ativo. Assim, é ativado a guilhotina para impressão não fiscal.   
Para utilizar a guilhotina em um ponto especifico de suas customizações, verifique o manual do equipamento para validar se o mesmo comporta comandos do arquivo **DLL**, caso sim, utilize a função **ExecInDllRun**.  
  
**Saiba mais**[MV\_FTTEFGU](http://tdn.totvs.com.br/display/PROT/DT_MV_FTTEFGU)  
[ExecInDllRun](http://tdn.totvs.com/display/tec/ExecInDLLRun)
