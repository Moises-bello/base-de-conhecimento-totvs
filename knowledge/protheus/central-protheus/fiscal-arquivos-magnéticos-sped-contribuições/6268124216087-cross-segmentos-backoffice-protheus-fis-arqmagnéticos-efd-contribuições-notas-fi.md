---
article_id: 6268124216087
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 6c9523b586a094ba7db5f097ba5c215e542b3dd6de5ff7b0cb3c815a926c567d
fetched_at: '2026-06-28T22:42:05.225383+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Notas Fiscais de Saída modelo 55 do Distrito Federal estão escriturando no registro
  A100 ao invés do registro C100
type: support-article
updated_at: '2022-08-31T12:49:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6268124216087-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Notas-Fiscais-de-Sa%C3%ADda-modelo-55-do-Distrito-Federal-est%C3%A3o-escriturando-no-registro-A100-ao-inv%C3%A9s-do-registro-C100
---

**Dúvida**

Notas Fiscais de Saída modelo 55 do Distrito Federal estão escriturando no registro A100 ao invés do registro C100

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - Todas as versões  
  
**Solução**

Para que as Notas Fiscais de Saídas modelo 55 no Distrito Federal sejam consideradas no registro C100 se faz necessário configurar o parâmetro  **MV\_DFSRVAC**=.T.

Criação do parâmetro e adaptação da rotina para respeitar esta nova condição.

Parâmetro : MV\_DFSRVAC

Tipo : Lógico

Conteúdo padrão : .F.

Descrição: Define se as notas de serviço eletrônica do Distrito federal serão levadas no bloco A100  (.F.) ou C100 (.T.)

Assuntos relacionados:

* [Arquivo EFD Contribuições](https://tdn.totvs.com/pages/viewpage.action?pageId=185760365)
