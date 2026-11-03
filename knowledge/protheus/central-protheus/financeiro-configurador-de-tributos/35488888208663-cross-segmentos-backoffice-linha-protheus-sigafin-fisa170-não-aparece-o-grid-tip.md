---
article_id: 35488888208663
category: Financeiro - Configurador de Tributos
content_hash: 1cb9451c14850aa4fd7fbc8e376e507603725733eb4dbffabf57dd3ee0349bf5
fetched_at: '2026-06-28T22:37:46.047359+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FISA170 - Não aparece
  o grid Tipo de Retenção x Natureza no cadastro de natureza
type: support-article
updated_at: '2026-03-09T18:34:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35488888208663-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-N%C3%A3o-aparece-o-grid-Tipo-de-Reten%C3%A7%C3%A3o-x-Natureza-no-cadastro-de-natureza
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35488888189975) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Não consigo amarrar a regra financeira no cadastro de natureza porque não aparece o grid "tipo de retenção x natureza"?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2210  
  
**Solução**

As possíveis causas da **grid** do Cadastro de Natureza não aparecer são:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38912424295447)

1. Regra Financeira incompleta: O **grid** será exibido apenas quando houver **uma regra financeira completamente cadastrada**, ou seja, com **todos os cadastros concluídos no Configurador de Tributos**.
2. Cadastro da Natureza aberto: Outro possível motivo para a **não exibição do grid** é o fato de a **natureza ter sido criada**, mas o **cadastro permanecer aberto** enquanto eram efetuados os lançamentos de impostos no Configurador de Tributos. Nessa situação, **basta fechar o cadastro da natureza e acessá-lo novamente** para que o grid seja exibido corretamente.
3. Conteúdo em branco no campo **FKK\_CODIGO** da tabela **FKK**:

   Hoje no padrão do sistema todo registro gravado na tabela **FKK** terá que ter conteúdo no campo **FKK\_CODIGO** , caso algum registro tiver o conteúdo em branco no campo **FKK\_CODIGO**, o grid da parte de baixo deixará de ser exibido

**Saiba mais**

[Financeiro - Configurador de Tributos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/30946086151959-Financeiro-Configurador-de-Tributos)
