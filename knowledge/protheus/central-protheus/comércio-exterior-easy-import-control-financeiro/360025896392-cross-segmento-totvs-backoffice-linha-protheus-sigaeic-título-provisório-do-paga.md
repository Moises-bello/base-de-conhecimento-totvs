---
article_id: 360025896392
category: Comércio Exterior - Easy Import Control - Financeiro
content_hash: 9e5d28b8c849798363a7c00e186a8b8f2efadfdbef17d0cedf1e89c39cd89805
fetched_at: '2026-06-28T22:39:44.430290+00:00'
product: protheus
section_id: 1500001549642
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Título Provisório
  do Pagamento Antecipado
type: support-article
updated_at: '2025-05-05T17:27:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025896392-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-T%C3%ADtulo-Provis%C3%B3rio-do-Pagamento-Antecipado
---

**Dúvida**Qual a configuração para que o título provisório "PR" referente ao pagamento antecipado não seja excluído ao liquidar a parcela do câmbio antecipado.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.   
  
**Solução**1. Acesse o módulo SIGACFG em Ambiente/Cadastros/ Parâmetros.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025326371/mceclip0.png)

2. Selecione Visualizar ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025523332/mceclip1.png)

3. No campo **Procurar por:**, informe o parâmetro MV\_EIC0003 e selecione Buscar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025305772/mceclip2.png)

4. Selecione  Editar  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025537771/mceclip0.png)

5. Altere o conteúdo do campo **Cont. Port** = 1 e selecione Salvar.![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025328931/mceclip0.png)

Para que o Protheus efetue a leitura da nova configuração, deve-se fechar o Protheus e acessar o módulo novamente.

Saiba mais: **[MP - SIGAEIC - Tipo de Títulos SIGAEIC x SIGAFIN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115010175987)**
