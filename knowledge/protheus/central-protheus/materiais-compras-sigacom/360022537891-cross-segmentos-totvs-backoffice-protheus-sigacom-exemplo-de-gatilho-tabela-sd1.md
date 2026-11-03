---
article_id: 360022537891
category: Materiais - Compras (SIGACOM)
content_hash: d74af637fd01ff9e8292d5a66442e80e24847e5e62b411ca6784a9a6409a85d5
fetched_at: '2026-06-28T22:41:08.868192+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Exemplo de gatilho
  tabela SD1 para carregar campo D1_TOTAL
type: support-article
updated_at: '2026-06-24T19:37:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022537891-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Exemplo-de-gatilho-tabela-SD1-para-carregar-campo-D1-TOTAL
---

**Dúvida**Exemplo de gatilho tabela SD1 para carregar campo D1\_TOTAL

**Ambiente**Protheus – Compras – A partir da versão 12  
  
**Solução**

É possível criar gatilho para o campo D1\_TOTAL para ser carregado automaticamente quando informado a quantidade e o valor no Documento de Entrada?

Não é indicado alterar as tabelas do ambiente padrão, contudo caso necessário criar gatilho para carregar o campo D1\_TOTAL constam exemplos abaixo que é necessário experiência em manutenção de ambiente para tal alteração:

**Gatilhos padrões:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019548891/mceclip0.png)**

**Exemplo de gatilho para campo D1\_TOTAL:**

CAMPO: D1\_VUNIT  
SEQUENCIA: 001  
CNT. DOMINIO: D1\_TOTAL  
TIPO: PRIMARIO  
REGRA: NoRound(M->D1\_VUNIT\*M->D1\_QUANT,2)   
POSICIONA: NAO  
ORDEM: 0

CAMPO: D1\_VUNIT  
SEQUENCIA: 002  
CNT. DOMINIO: D1\_TOTAL  
TIPO: PRIMARIO  
REGRA: If(A103Trigger("D1\_TOTAL"),M->D1\_TOTAL,CriaVar("D1\_TOTAL"))  
POSICIONA: NAO  
ORDEM: 0

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019670612/mceclip1.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019549351/mceclip2.png)

**OBSERVAÇÃO:** Para que o gatilho do campo funcione devem ser criadas as duas sequências citadas acima.

Caso tenha dúvidas quanto ao funcionamento ou ocorrências, verifique com a pessoa com experiência em manutenção de ambiente e valide sempre com o Dicionário de Dados padrão conforme disponível no Portal do Cliente para download.
