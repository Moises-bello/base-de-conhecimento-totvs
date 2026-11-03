---
article_id: 360056164374
category: Financeiro - Contas a Receber
content_hash: 24758d2893b486f5ee524b5ad0e90dc1aedda8d453b3b350defab017ed4fa737
fetched_at: '2026-06-28T22:38:15.010320+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: MP - SIGAFIN - FINA070 - Cálculo variação monetária
type: support-article
updated_at: '2021-04-28T15:16:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056164374-MP-SIGAFIN-FINA070-C%C3%A1lculo-varia%C3%A7%C3%A3o-monet%C3%A1ria
---

**Dúvida**Na rotina **Baixa a Receber** (FINA070), no momento da baixa, habilitamos o campo "**+corr. monetaria**", porém ao adicionar valor no campo, o mesmo não soma ao total do valor do título a ser baixado?  
  
  
**Ambiente**Microsiga Protheus - Financeiro - FINA070 - A partir Versão 12.1.17  
  
**Solução**Para que o sistema calcule a variação monetária pelo valor original e o não o valor total (valor líquido), será  necessário o preenchido do parâmetro **MV\_TIPOCM** = com o conteúdo **O** (**Original**).  
  
Segue a documentação com explicação do parâmetro com cálculo efetuado  
com conteúdo O (Original) e com conteúdo T (Total).  
<https://tdn.totvs.com/pages/releaseview.action?pageId=532024035>
