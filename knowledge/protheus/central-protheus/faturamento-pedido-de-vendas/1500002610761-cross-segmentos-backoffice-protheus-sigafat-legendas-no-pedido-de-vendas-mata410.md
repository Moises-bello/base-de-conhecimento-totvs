---
article_id: 1500002610761
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 5d9f034c4ac0cf865c6defae0227732a9147beb07ff661489ba174f9dd38184d
fetched_at: '2026-06-28T22:38:42.566030+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - BackOffice Protheus - SIGAFAT - Legendas no Pedido de Vendas
  (MATA410)
type: support-article
updated_at: '2025-11-26T13:47:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002610761-Cross-Segmentos-BackOffice-Protheus-SIGAFAT-Legendas-no-Pedido-de-Vendas-MATA410
---

**Dúvida**  
Qual o significado das legendas exibidas na rotina Pedidos de Venda (MATA410)?  
  
**Ambiente**  
Cross Segmentos - BackOffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Na rotina **Pedidos de Venda (MATA410)** os **Status disponíveis** são representados conforme as seguintes **legendas**:  
  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36596934597143)

![](https://tdn.totvs.com/download/thumbnails/244940135/image2018-4-23_11-40-9.png?version=1&modificationDate=1524494409000&api=v2)  
**Legenda cor vede**  
  
**Em Aberto**: Não foi submetido à liberação (**não possui registro na SC9**) - campo **(C5\_LIBEROK)** em branco;

![](https://tdn.totvs.com/download/thumbnails/244940135/image2018-4-23_11-40-50.png?version=1&modificationDate=1524494451000&api=v2):   
**Legenda cor Vermelho**  
  
**Encerrado**: **Já faturado 100% ou Eliminado resíduo** - possui conteúdo no (**C5\_NOTA**); Quando faturado 100% o (**C5\_NOTA**) recebe o número da última Nota Faturada. Quando Eliminado resíduo recebe o conteúdo XXXXXX (6 ou 9 dígitos)

![](https://tdn.totvs.com/download/thumbnails/244940135/image2018-4-23_11-41-49.png?version=1&modificationDate=1524494509000&api=v2):   
**Legenda cor Amarelo**  
  
**Liberado**: Já foi submetido à liberação do Pedido (**já gerou registro na SC9** independente se gerou com ou sem bloqueio de crédito/estoque), **mas não foi encerrado** (está pendente de faturamento) - campo (**C5\_LIBEROK**) com conteúdo "**S**" e campo (**C5\_NOTA**) em branco;

![](https://tdn.totvs.com/download/thumbnails/244940135/image2018-4-23_11-42-25.png?version=1&modificationDate=1524494546000&api=v2):  
**Legenda cor Azul**  
  
**Bloqueio de Regra**: Ocorre quando os **itens e o cabeçalho** do pedido de venda **não estão de acordo** com a definição do cadastro de Regras de Negócio. - (**C5\_BLQ**) com conteúdo "**1**";

![](https://tdn.totvs.com/download/thumbnails/244940135/image2018-4-23_11-42-50.png?version=1&modificationDate=1524494571000&api=v2)  
**Legenda cor Laranja**  
  
**Bloqueio de Verba**: Ocorre quando, na análise da verba, o Sistema verifica se o **desconto concedido** nos itens do pedido **é maior que o permitido** pela empresa. A diferença entre o permitido pela regra e o concedido no pedido de venda será abatido do saldo da verba de venda, caso possua saldo. Caso não tenha saldo suficiente, o pedido será bloqueado por verba. - (**C5\_BLQ**) com conteúdo "**2**".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36596934600599)    
  **Legenda cor Roxa:**  
  
**Bloqueio de Alçada:** Ocorre quando o pedido está bloqueado por qualquer tipo de alçada. Segue mais detalhes sobre o [**controle de alçada**](https://tdn.totvs.com/pages/viewpage.action?pageId=804802719)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36596934602391)  
  **Legenda X**  
  
**Pedido R****ejeitado**: Ocorre quando o pedido ficou bloqueado por alçada e foi rejeitado pelo aprovador no momento de liberar o documento.Segue mais detalhes sobre o [**controle de alçada**](https://tdn.totvs.com/pages/viewpage.action?pageId=804802719)

**Saiba mais:**   
[**FAT0121 Legendas Status do Pedido de Vendas**](https://tdn.totvs.com/display/PROT/FAT0121_Legendas_Status_do_Pedido_de_Vendas)

[**Pedidos de Venda (MATA410)**](https://tdn.totvs.com/pages/viewpage.action?pageId=789976267)

[**SIGAFAT - Ao faturar pedido de venda, legenda não ficou vermelha**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/24800545267479-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Ao-faturar-pedido-de-venda-legenda-do-pedido-de-venda-n%C3%A3o-ficou-vermelha)
