---
article_id: 360043042034
category: Comércio Exterior - Easy Import Control - Purchase - Order
content_hash: b6988737610736a40df28a0e1cddcdf73cbde539295839be725ac74e2787d93f
fetched_at: '2026-06-28T22:39:41.138512+00:00'
product: protheus
section_id: 1500001538481
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Definir Armazém
  Padrão Para os Pedidos de Compra Gerado pelo Módulo SIGAEIC
type: support-article
updated_at: '2022-02-04T19:11:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043042034-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Definir-Armaz%C3%A9m-Padr%C3%A3o-Para-os-Pedidos-de-Compra-Gerado-pelo-M%C3%B3dulo-SIGAEIC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como definir Armazém Padrão Para os Pedidos de Compra Gerado pelo Módulo SIGAEIC?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Easy Import Control – A partir da versão 11.80  
  
**Solução**A informação do Armazém ou Local Padrão não faz parte do módulo SIGAEIC, esta informação é do cadastro do produtos (SB1) ou da solicitação de compras (SC1).  
Cenário:  
1 - Quando o Purchase Order (SW2/SW3) criado referencia uma Solicitação de Importação (SW0/ SW1) que foi originada por uma solicitação de compras (SC1), ao gerar o pedido de compras (SC7) enviamos para o Local Padrão (C7\_LOCAL) a informação da Solicitação de Compras (C1\_LOCAL).  
2 - Quando o Purchase Order (SW2/SW3) criado referencia uma Solicitação de Importação (SW0/ SW1) que não foi originada por uma solicitação de compras (SC1), ao gerar o pedido de compras (SC7) enviamos para o Local Padrão (C7\_LOCAL) a informação do Cadastro de Produtos (B1\_LOCPAD).   
  
Observação: A rotina de cópia do PO se enquadra neste segundo cenário, pois a cópia no Purchase Order não gera cópia da Solicitação de Compras. Logo, todas as informações do Purchase Order são copiadas – só que o local padrão não faz parte do escopo das informações do nosso Purchase Order.
