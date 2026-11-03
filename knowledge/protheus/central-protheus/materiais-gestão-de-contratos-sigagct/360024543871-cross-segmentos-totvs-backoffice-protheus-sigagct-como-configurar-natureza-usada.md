---
article_id: 360024543871
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: ccfae87fd15c6abed940a5387d0e5e7b6fc93478f36e1ddaf53ce9a24870c36e
fetched_at: '2026-06-28T22:37:19.789436+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como configurar Natureza
  usada na Medição de Contrato de Vendas ?
type: support-article
updated_at: '2025-11-27T20:04:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024543871-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-configurar-Natureza-usada-na-Medi%C3%A7%C3%A3o-de-Contrato-de-Vendas
---

**Dúvida**  
Como configurar Natureza no Encerramento de Medição em Contrato de Vendas ?  
  
**Ambiente**  
Microsiga Protheus – Gestão de Contratos – A partir da versão 12.17  
  
  
**Solução**  
Para pedidos de vendas gerados através do Gestão de Contratos, o parâmetro ***MV\_1DUPNAT*** deverá estar configurado para que a natureza seja considerada do cadastro do cliente ***(Conteúdo SA1->A1\_NATUREZ)***, uma vez que como o pedido ainda não foi gerado, não há conteúdo no campo ***C5\_NATUREZ***.  
  
Por padrão, a natureza do cadastro do cliente não será levada ao campo ***C5\_NATUREZ***. Ela somente será carregada ao título financeiro que será gerado quando o pedido for faturado.  
O parâmetro ***MV\_1DUPNAT*** permite a inclusão de validação, para que quando o pedido for gerado pelo Gestão de Contratos, seja considerado o conteúdo ***SA1->A1\_NATUREZ*** e quando o pedido for incluso manualmente pelo pedido de vendas, considere o conteúdo ***SC5->C5\_NATUREZ***.

**Obs:**Se o campo **CN9\_NATURE** estiver preenchido no cabeçalho do Contrato a natureza do **Pedido de vendas** será preenchida com a Natureza do campo **CN9\_NATURE**,se o campo CN9\_NATURE tiver em branco, será considerado conforme instruções acima.

***Saiba Mais:***  
[Natureza no encerramento de medição de vendas](http://tdn.totvs.com/pages/viewpage.action?pageId=271172868)
