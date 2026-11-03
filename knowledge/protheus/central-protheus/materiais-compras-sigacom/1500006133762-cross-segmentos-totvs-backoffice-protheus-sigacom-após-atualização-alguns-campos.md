---
article_id: 1500006133762
category: Materiais - Compras (SIGACOM)
content_hash: 43208bf0af63ebe150b1f47200212ac5441388b1a851a5baad92d75a6acc6e0f
fetched_at: '2026-06-28T22:41:14.180265+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Após atualização alguns
  campos não aparecem na tela de SC
type: support-article
updated_at: '2022-05-16T21:15:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006133762-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ap%C3%B3s-atualiza%C3%A7%C3%A3o-alguns-campos-n%C3%A3o-aparecem-na-tela-de-SC
---

**Dúvida**Após a aplicação do pacote acumulado de compras alguns campos não aparecem na tela de SC

- Tipo doc.  
- Desc. Tipo doc.  
- Requisitante SC  
- Centro de Custo  
- Num. Contrato  
- Revisão Ct.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras  
  
**Solução**Foi retirada a função ValidaCNI() do MATA110, e passa a valer o parâmetro SX6 MV\_SCLCNI para habilitar tela,e funcionalidades utilizadas na CNI e demais federações.  
O MV\_SCLCNI é logico, quando .T. (ativa funcionalidades da CNI e Federações), .F. não altera. Caso não o possua no seu ambiente por gentileza crie conforme abaixo:  
  
![](https://totvssuporte.zendesk.com/attachments/token/WjspxqHZsF48JWeCFAyc3V4AK/?name=inline1056881669.png)  
  
ref. <https://tdn.totvs.com/pages/releaseview.action?pageId=577907968>
