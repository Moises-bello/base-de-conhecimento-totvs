---
article_id: 17470232115095
category: ACOMPANHA CUSTOS - JORNADA DE FECHAMENTO (NOVO)
content_hash: 5880618df415e01c0f92ff8e6b4334502a586f6b99b2c78fdfd4cdf0b5f36927
fetched_at: '2026-06-28T22:38:48.100887+00:00'
product: protheus
section_id: 5367899706647
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Internal Server Erro
  ao alterar os parametros das perguntas da rotina Acompanha Custo
type: support-article
updated_at: '2026-06-16T13:47:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17470232115095-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Internal-Server-Erro-ao-alterar-os-parametros-das-perguntas-da-rotina-Acompanha-Custo
---

O erro "Internal Server Error" ao alterar parâmetros da rotina Acompanha Custos no TOTVS Protheus ocorre quando faltam grupos de perguntas nas tabelas SX1, referentes às etapas Custo Médio e Virada de Saldos. A correção envolve validar e garantir que todos os parâmetros estejam presentes e não deletados na base de dados. **AC.CONFIG.PROFILE.REPOSITORY.ACPROFREPOSITORY:FIXANDUPDATEPARAMETERSPROPERTY**

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17470241333783) Tempo aproximado para leitura: **00:01:10 min**  
  
**Ocorrência**  
Ao alterar os parametros das perguntas da rotina Acompanha Custo é apresentado o erro de "**Internal Server Error**", como corrigir?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da release 12.1.33

**Causa**  
Ao fazer uma alteração de perguntas nos parametros da rotina Acompanha Custos e apresentar o erro de **"Internal Server Error",** é necessário fazer o seguinte procedimento:

Internal Server Erro.

**AC.CONFIG.PROFILE.REPOSITORY.ACPROFREPOSITORY:FIXANDUPDATEPARAMETERSPROPERTY(ACPROFREPOSITORY.TLPP)**

Segue imagem de exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17470035340439)

   
**Solução**  
Para correção desse errorlog, precisa validar se possui todos os grupos de perguntas das rotinas Custo Médio e Virada de Saldos na tabela SX1 conforme exemplo abaixo:

**Parametros estapa Custo Médio/Contabilização offline:**

![](https://totvssuporte.zendesk.com/attachments/token/ONyDPE2jMV23Zbc3KnrufdEpI/?name=image.png)**Parametros etapa - Virada de Saldos:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17470130535191)

Pois esse erro ocorre quando a base de dados não possui ou consta como deletado algum desses parametros, sendo necessário validar internamente.

**Saiba Mais**

[*Clique aqui e veja mais artigos sobre o Acompanha Custos*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/5367899706647-MONITOR-DE-CUSTOS)
