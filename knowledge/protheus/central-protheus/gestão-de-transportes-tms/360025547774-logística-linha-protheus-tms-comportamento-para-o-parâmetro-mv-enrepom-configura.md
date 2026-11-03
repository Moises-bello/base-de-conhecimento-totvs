---
article_id: 360025547774
category: Gestão de Transportes (TMS)
content_hash: b3bd8b780f595a0d0d38885d0c9874e2663f713d629f172d601fa4e858c62ea4
fetched_at: '2026-06-28T22:45:27.529973+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Comportamento para o parâmetro MV_ENREPOM
  configurado com o valor 3
type: support-article
updated_at: '2022-05-31T19:57:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025547774-Log%C3%ADstica-Linha-Protheus-TMS-Comportamento-para-o-par%C3%A2metro-MV-ENREPOM-configurado-com-o-valor-3
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como o Sistema se comporta quando o parâmetro **MV\_ENREPOM** esta configurado com o valor **3 - Quitação conf. MV\_LIBCTC**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Quando o contrato de carreteiro for gerado, ele calculará a diferença entre o valor previsto enviado no fechamento de viagem e o total do frete, considerando valor com ou sem impostos, de acordo com o parâmetro **MV\_IMPCTC**, atualizando o **valor do contrato Repom** por meio do método **IncluiMovimento**.  
  
De acordo com a parametrização de geração do título, parâmetros **MV\_LIBCTC** e **DUJ\_TITFRE**, **o contrato será quitado**.  
  
Existe a possibilidade de autorizar o pagamento pela rotina **Pagamento de Saldo**, alterando o parâmetro **MV\_ENREPOM = 4 - Quitação Pagto Saldo.****Saiba Mais**Mais informações poderão ser acessadas no*link*: [ER Integração Repom.](http://tdn.totvs.com/pages/viewpage.action?pageId=273983106)
