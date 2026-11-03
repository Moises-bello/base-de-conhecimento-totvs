---
article_id: 360053290493
category: Comércio Exterior - Easy Export Control - Pedido - Export
content_hash: cb921aaeaa47e689a802a0a1580b744545dc8df15b3898996c79aaab1ba459a7
fetched_at: '2026-06-28T22:36:59.011908+00:00'
product: protheus
section_id: 1500001538181
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Fluxo da integração:
  Pedido de Exportação para ERP Logix'
type: support-article
updated_at: '2022-06-14T20:43:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053290493-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Fluxo-da-integra%C3%A7%C3%A3o-Pedido-de-Exporta%C3%A7%C3%A3o-para-ERP-Logix
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura:**00:04:00 min  
  
Dúvida**Realizada a inclusão do Pedido de Exportação porém este não é integrado ao Logix, como corrigir?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões  
  
**Solução**A integração do Pedido de Exportação para o Logix, adapter  SALESORDER, será encaminha apenas após a aprovação da proforma, conforme documento: <https://tdn.totvs.com/pages/releaseview.action?pageId=237386803> , além das parametrizações.

**Cenário 2 – fluxo de integração Easy Export Control ->ERP**  
O segundo fluxo de integração possibilita que o pedido tenha origem no Easy Export Control. Para este cenário de integração, o pedido de exportação terá uma nova etapa a ser realizada: aprovação da proforma.  
Uma vez confirmada a sua gravação no Easy Export Control, será criado o processo de proforma que pode ser concluído por etapas sem que a integração seja iniciada. Isso possibilita que o preenchimento dos dados sejam realizados em momentos diferentes. Uma vez concluído a construção do pedido de exportação (ou proforma) o usuário poderá preencher a data de solicitação de aprovação disponível na pasta cadastrais do processo, campo Dt.Sol.Ap.Pr.(EE7\_DTSLAP).  
Uma vez que esteja com a data de solicitação de aprovação preenchido, em Ações Relacionadas o usuário poderá acessar a rotina **Aprov. Proforma**que possibilitará informar a data de aprovação do processo de exportação. Uma vez aprovado, o Easy Export iniciará a integração com o ERP através do envio da mensagem SALESORDER para a criação do pedido de venda.
