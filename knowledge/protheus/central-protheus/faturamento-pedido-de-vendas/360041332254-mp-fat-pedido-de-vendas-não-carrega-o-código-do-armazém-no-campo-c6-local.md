---
article_id: 360041332254
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: b5e07936357cf9a0418fed3d54204b3e2abc9d99f0e1748f9c85aee33a02db86
fetched_at: '2026-06-28T22:38:42.796465+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: 'MP - FAT - PEDIDO DE VENDAS NÃO CARREGA O CÓDIGO DO ARMAZÉM NO CAMPO: C6_LOCAL '
type: support-article
updated_at: '2021-04-28T15:50:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041332254-MP-FAT-PEDIDO-DE-VENDAS-N%C3%83O-CARREGA-O-C%C3%93DIGO-DO-ARMAZ%C3%89M-NO-CAMPO-C6-LOCAL
---

**Dúvida**

Pedido de vendas não carrega o código do armazém no campo: C6\_LOCAL.  
   
 **Ambiente**  
Protheus – Faturamento – A partir da versão 12.  
  
**Solução**

Verificar primeiro se existe o armazém configurado no cadastro de produto que é a tabela SB1, caso já exista, valide como esta configurado os parâmetros abaixo:

MV\_ARQPROP = F  
MV\_ARQPROD = SBZ

Obs: Estes parâmetros são utilizados para o modulo de Oficina e Veículos. 

Devido o parâmetro esta considerando a tabela SBZ ou invés da SB1, ao informa o produto no pedido de vendas o sistema não preenche o armazém no C6\_LOCAL, porque não existe o registro na tabela SBZ, e a rotina responsável é MATA018. 

Para que seja considerado através da SBZ deverá cadastrar o mesmo produto na rotina: MATA018 (Indicador de Produtos).
