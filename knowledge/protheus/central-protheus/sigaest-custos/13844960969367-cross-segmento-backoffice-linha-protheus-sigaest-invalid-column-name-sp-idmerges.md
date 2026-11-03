---
article_id: 13844960969367
category: SIGAEST - CUSTOS
content_hash: 888bff9755f3d7f5f3eef5903cf582ba4994759dfe45a2f3d5584205b24993d9
fetched_at: '2026-06-28T22:39:01.994623+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Invalid column name
  'SP_IDMERGE'.'SP_CFGXSIG'
type: support-article
updated_at: '2025-03-12T12:20:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13844960969367-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Invalid-column-name-SP-IDMERGE-SP-CFGXSIG
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00**:**02:00 min**Ocorrência**

Ao executar o Custo Médio ou a rotina de Contabilização é gerado o seguinte errorlog na procedure:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13844714460311)

Error : 207 (S0022) (RC=-1) - [Microsoft][SQL Server Native Client 11.0][SQL Server]Invalid column name 'SP\_IDMERGE'. Error : 207 (S0022) (RC=-1) - [Microsoft][SQL Server Native Client 11.0][SQL Server]Invalid column name 'SP\_CFGXSIG'.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**Após a atualização do fonte **23-04-04-LIB\_LABEL\_03042023\_P12\_HARPIA** é gerado o errorlog acima ao executar as rotinas de Custo Médio/Contabilização.

Ocorre por conta da nova configuração das procedures.  
  
**Solução**

Para correção desse errorlog, será necessário desinstalar e reinstalar a procedure 19.

Caso não seja possível a instalação, avaliar se o ambiente e central se encontram atualizados:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Procedure 19 "Recálculo do Custo médio" Desatualizada | Não Conclui a Instalação | Status "Não instalada"](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13765345109271)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
