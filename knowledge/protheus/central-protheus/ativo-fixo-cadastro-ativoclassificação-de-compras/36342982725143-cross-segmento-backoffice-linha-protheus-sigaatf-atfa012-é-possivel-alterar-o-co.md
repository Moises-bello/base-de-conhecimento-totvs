---
article_id: 36342982725143
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: 866a3f6dab1ab56dcd1f225d5b8324f1dba861cce36f79999994ed03d05ae753
fetched_at: '2026-06-28T22:41:48.351218+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA012 - É possivel
  alterar o conteudo do campo: Dt de aquis ori (N3_AQUISIC)'
type: support-article
updated_at: '2025-11-17T12:07:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36342982725143-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA012-%C3%89-possivel-alterar-o-conteudo-do-campo-Dt-de-aquis-ori-N3-AQUISIC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36342982705687) Tempo aproximado para leitura: 00**:05 min**  
  
**Dúvida**

É possível alterar o campo: "**Dt de Aquis Ori**" (N3\_AQUISIC), no momento da classificação ou aquisição.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Ativo Fixo -  A partir da versão 12.1.2410

**Solução**

Os campos "**Dt de Aquis**" Ori (N3\_AQUISIC) e "**Dt.Aquisicao**" (N1\_AQUISIC) não podem ser alterados, pois estavam gerando lançamentos inconsistentes na tabela Movimentos (SN4).  
   
Documentação sobre a correção e bloqueio do campo:   
[https://tdn.totvs.com/pages/viewpage.action?pageId=9100248](https://tdn.totvs.com/pages/viewpage.action?pageId=910024881)

Neste caso será necessário, realizar os passos abaixo com a informação correta do Bem:

**1°** Realizar a baixa do bem através da rotina Baixa De Ativo (ATFA036)

**2°** Realizar a inclusão do bem novamente via rotina Documento de entrada (MATA103) ou Inclusão Manual pela rotina Cadastro de Ativos Imobilizados (ATFA012)

Documentações para auxílio:

Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA036 - BAIXA DE ATIVO

[Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA240 - Aquisição de imobilizado e classificação de compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012521571-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA240-Aquisi%C3%A7%C3%A3o-de-imobilizado-e-classifica%C3%A7%C3%A3o-de-compras)
