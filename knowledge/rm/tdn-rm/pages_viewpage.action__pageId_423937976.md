---
content_hash: d75a1ffd53f53775a9c36d4a9055f09581a7877d80c21ae600f46d05fc142e71
fetched_at: '2026-06-29T00:09:24.634533+00:00'
page_id: '423937976'
product: rm
source: tdn-rm
title: Integrações Fiscal (NF-e)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937976
version: 12
---

Através deste anexo, é possível alterar os valores dos campos Número do Pedido de Compra e Item do Pedido de Compra.  
Através da visão do Item de movimento → Integrações → Fiscal, em movimentos que não geram escrituração.   
Para tal, é preciso parametrizar as informações, apenas para movimentos dos tipos "1.1" e "2.1".   
O parâmetro pode ser acessado em "Etapa 62 - Fiscal - Dados Fiscais", campo "Editar Número do Pedido" que deve ter a opção de ser definido como Não Edita, Mostra, Edita.  
Quando parametrizado como "Edita", os valores devem ser preenchidos manualmente e serão persistidos/enviados para estes mesmos campos no movimento de Escrituração (NF-e) no processo de faturamento.  
Isso se deve ao fato de que os movimentos do tipo 1.1 e 2.1 são a origem das Notas, trazendo assim, maior transparência e consistência das informações.  
***Observações***: Os campos serão apresentados na visão dos itens de movimento e no XML da Nota Fiscal, terão as seguintes nomenclaturas e tipos:  
Campo Número do Pedido de Compra → XPED → Tipo Alfanumérico.  
Campo Item do Pedido de Compra → NITEMPED → Tipo Inteiro.
