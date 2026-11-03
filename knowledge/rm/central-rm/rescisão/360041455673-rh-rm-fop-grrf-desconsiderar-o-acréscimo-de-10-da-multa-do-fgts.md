---
article_id: 360041455673
category: Rescisão
content_hash: 56b169a89dd59dd4b7e518b82ebd2f0d8b44967ec0c74467c50523cd9f08f5d3
fetched_at: '2026-06-28T22:46:55.310268+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - GRRF: Desconsiderar o acréscimo de 10% da multa do FGTS'
type: support-article
updated_at: '2025-03-12T19:53:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041455673-RH-RM-FOP-GRRF-Desconsiderar-o-acr%C3%A9scimo-de-10-da-multa-do-FGTS
---

**Dúvida**Conforme Medida Provisória nº 905/2019, como desconsiderar o acréscimo de 10% da multa do FGTS na geração da GRRF?  
  
**Ambiente**RM - Totvs Folha de Pagamento - A partir da versão 12.1  
  
**Solução**Foi liberado pela Caixa no dia 02/01/2020, um novo instalador do aplicativo GRRF para atender as alterações provenientes da MP 905/2019, portanto, **através do novo aplicativo, a própria GRRF fará a desconsideração da multa dos 10%**, não sendo necessário a atualização por parte do TOTVS RM.  
  
Link da Caixa para download: <http://www.caixa.gov.br/site/paginas/downloads.aspx>- Print da GRRF novo instalador, mostrando a desconsideração da multa:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055224173)

**Observação:**Será desconsiderado somente para rescisões a partir de 01/01/2020.

- Por parte do TOTVS RM, temos na geração da GRRF, o parâmetro chamado "**Desconsiderar o acréscimo de 10% da multa do FGTS**":  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30602147433367)  
  
O parâmetro deverá ser marcado e tem a funcionalidade exclusiva de não levar a multa dos 10% do FGTS para o **Lançamento Financeiro** que será criado a partir da GRRF.  
  
Maiores informações, segue o TDN: <https://tdn.totvs.com/pages/releaseview.action?pageId=527841168>
