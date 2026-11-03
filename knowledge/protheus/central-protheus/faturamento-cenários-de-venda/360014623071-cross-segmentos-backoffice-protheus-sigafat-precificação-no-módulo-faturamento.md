---
article_id: 360014623071
category: Faturamento - Cenários de Venda
content_hash: 32793945a959502bd89c74229db040c6d69c471fe78ee2601086495ca96e7225
fetched_at: '2026-06-28T22:38:34.101017+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Precificação no módulo Faturamento
type: support-article
updated_at: '2024-03-26T21:14:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014623071-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Precifica%C3%A7%C3%A3o-no-m%C3%B3dulo-Faturamento
---

**Dúvida**Como trabalhar os preços de Venda no módulo Faturamento? Quais as funcionalidades disponíveis?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.  
  
  
**Solução**

É possível realizar pré-configurações / cadastros para que o preço de venda seja automaticamente sugerido no Pedido de Vendas na rotina (MATA410) no campo "Prc Lista" (C6\_PRUNIT).  
  
As opções são:

* Preço de Venda POR PRODUTO MATA010: "Preço Venda" (B1\_PRV1)   
  *(OBS: Campos de Preço da SB5 - (Complemento de Produtos) não são utilizados no módulo Faturamento. Veja tratamento [pelo Compras](https://tdn.totvs.com/pages/viewpage.action?pageId=284884712) ou [pelo Varejo](https://tdn.totvs.com/pages/viewpage.action?pageId=301171610)).*Demais dúvidas sobre campos entrar em contato com equipe de **Estoque/ Custos.**
* Preço de Venda POR TABELA de Preço OMSA010: Registrar no campo "Preco Venda" (DA1\_PRCVEN)  
  (Necessário que a Tabela esteja **Ativa** e a **Vigência** no Item seja anterior ou igual à data base)
* Preço de Venda POR CLIENTE: Registrar no Cadastro de Cliente (CRMA980) a tabela de preço padrão para esse Cliente -"Tabela Preco" (DA1\_TABELA) através do campo "Tabela Preco" (A1\_TABELA).
* Preço de Venda POR LOTE: Registrar no campo "Preco Lote" (B8\_PRCLOT) (Necessário que a data base seja inferior ou igual à B8\_DTVALID). Detalhes em: [Conceito\_preco\_por\_lote](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/mata410_conceito_preco_por_lote.htm)

OBS: O uso de Moedas no Pedido de Vendas podem interferir no Preço de Venda padrão conforme a taxa do dia. Detalhes em: [FAT0096\_Uso\_Moeda\_Modulo\_Faturamento](http://tdn.totvs.com/display/PROT/FAT0096_Uso_Moeda_Modulo_Faturamento)

Além disso, há diversas funcionalidades disponíveis para tratamento do preço de venda; de modo a compor os valores de acordo com vários fatores comerciais envolvidos. Conheça todas as ferramentas disponibilizadas na documentação técnica de Precificação  
  
  
Saiba mais:  
[Precificação no módulo Faturamento](https://tdn.totvs.com/pages/releaseview.action?pageId=393364250)   
[Tabelas de Preços (OMSA010 - SIGAFAT)](https://tdn.totvs.com/pages/viewpage.action?pageId=357601934)

#
