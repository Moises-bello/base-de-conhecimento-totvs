---
article_id: 30142005662231
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 9f23e7d737c9c62cdfd33ec669cbc1dbe846e288d0c0c18c3213dd0f149f385e
fetched_at: '2026-06-28T22:38:54.352376+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como alterar a ordem
  dos campos na tela de inclusão da MATA241
type: support-article
updated_at: '2025-03-12T12:26:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30142005662231-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-alterar-a-ordem-dos-campos-na-tela-de-inclus%C3%A3o-da-MATA241
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30141945703703) Tempo aproximado para leitura: **00:01:35min** **Dúvida**Na tela de inclusão da MATA241 quero alterar a ordenação dos campos para facilitar o preenchimento, é possível ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**A ordenação na tela de inclusão pode ser efetuada diretamente via configurador, apenas para campos de status verde (que podem ter sua ordenação alterada).

**1 -** Para esse ajuste, deve acessar o SIGACFG > Base de Dados > Dicionário > Base de Dados:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30141945704087)

**2 -** Após isso deve acessar o dicionário de dados e pesquisar pela tabela SD3:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30141945704599)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30141945705879)

**3 -** Após localizar a tabela deve abrir os campos e localizar os campos que pretende alterar a ordenação, neste exemplo alteramos os campos D3\_DESCRI e D3\_OBSERVA para que sejam apresentados entre os primeiros campos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30142005648663)

**4 -** Após alterar a ordenação deve clicar em sair e depois em salvar:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30141945707415)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30141945707671)

**5 -** Após salvar, ao abrir a rotina MATA241 a ordenação será respeitada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30141945708055)

**Observação:** Caso esse tipo de ajuste não atenda a necessidade temos também o ponto de entrada [**M240BROW**](https://tdn.totvs.com/pages/releaseview.action?pageId=236593296)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
