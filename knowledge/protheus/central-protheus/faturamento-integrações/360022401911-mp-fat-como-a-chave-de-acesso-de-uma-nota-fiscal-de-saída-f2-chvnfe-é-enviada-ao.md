---
article_id: 360022401911
category: Faturamento - Integrações
content_hash: 13c3b2fc7d4bcab7ee861b7138ac3b2bc911e64d0cfc074be08c9f4192ae670e
fetched_at: '2026-06-28T22:38:26.565066+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: MP - FAT - Como a chave de acesso de uma nota fiscal de saída, F2_CHVNFE, é
  enviada ao SIGAGFE para alimentar o campo GW1_DANFE - Chave NF-e do Documento de
  Carga
type: support-article
updated_at: '2021-04-28T15:15:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022401911-MP-FAT-Como-a-chave-de-acesso-de-uma-nota-fiscal-de-sa%C3%ADda-F2-CHVNFE-%C3%A9-enviada-ao-SIGAGFE-para-alimentar-o-campo-GW1-DANFE-Chave-NF-e-do-Documento-de-Carga
---

**Dúvida**Como a chave de acesso de uma nota fiscal de saída, **F2\_CHVNFE**, é enviada ao SIGAGFE para alimentar o campo **GW1\_DANFE** - Chave NF-e do Documento de Carga?

**Ambiente**Microsiga Protheus - Faturamento - Todas as Versões  
  
**Solução**Para que haja a integração é necessário o parâmetro MV\_INTGFE = .T.

Quando geramos uma nota fiscal de saída no faturamento é gerado um documento de Carga no SIGAGFE com o campo GW1\_DANFE em branco  
  
Este campo é preenchido conforme conteúdo do F2\_CHVNFE quando efetuamos o monitoramento da nota, rotina **AUTONFEBUSINESS**, ou emitimos a Danfe, rotinas **DANFEII** ou **DANFEIII**.

O campo **GW1\_AUTSEF** - Autorização Sefaz também é atualizado neste processo conforme tabela abaixo:

|  |  |
| --- | --- |
| **Campo no ERP - F2\_FIMP** | **Campo no GFE GW1\_AUTSEF** |
| "T" - Transmitida | "0" - Não informado |
| "S" - NF Autorizada | "1" - Autorizado |
| "D" - NF Uso Denegado | "2" - Não autorizado |
| "N" - NF Não-autorizada | "2" - Não autorizado |

Para mais detalhes da Integração, conheça nossa FAQ Faturamento X GFE no Link abaixo

**<http://tdn.totvs.com/pages/viewpage.action?pageId=337359685>**
