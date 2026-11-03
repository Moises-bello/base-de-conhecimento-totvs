---
article_id: 4403168749207
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 88600641e69b3c21a915cda81f5be5bbf0c7ea7581e7ed1c4adbe577435538ac
fetched_at: '2026-06-28T22:38:39.838889+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - HELP NFXIDENTB6
type: support-article
updated_at: '2026-02-26T17:56:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403168749207-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-HELP-NFXIDENTB6
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38665960175511)** **Tempo aproximado para leitura:****00:01:00 min**

**Dúvida**  
Como corrigir o Help NFXIDENTB6 ao realizar uma devolução de Poder de Terceiros?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

O erro ocorre devido a uma falha na amarração entre as tabelas de Compras (SD1), Saldo de Terceiros (SB6) e Pedido de Venda (SC6).

Para resolver, valide os seguintes pontos:

1. **Campo C6\_ITEMORI:** Verifique se foi preenchido corretamente via rotina automática.
2. **Campo B6\_IDENT vs D1\_NUMSEQ:** O conteúdo destes campos deve ser idêntico no momento da devolução.
3. **Atualização:** Certifique-se de que a rotina **MATV410A** está atualizada com o último pacote da expedição contínua do SIGAFAT.

> **Observação:** Se o campo **D1\_IDENTB6** estiver em branco ou diferente do **B6\_IDENT**, poderá gerar também o erro *Variable does not exist C5\_TIPO*.

Saiba mais: [Relacionamentos das notas de Remessa/Devolução no sistema (Tabela SB6)](https://tdn.totvs.com/pages/releaseview.action?pageId=446701767#)
