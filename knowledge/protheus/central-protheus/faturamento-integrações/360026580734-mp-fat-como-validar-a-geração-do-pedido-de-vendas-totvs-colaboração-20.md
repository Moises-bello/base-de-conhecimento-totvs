---
article_id: 360026580734
category: Faturamento - Integrações
content_hash: ff621304ef2aefb8d9f525e5bc64ce6375ecd385de4f65e57414bfa475a08ca0
fetched_at: '2026-06-28T22:38:26.571999+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: MP - FAT - Como validar a geração do pedido de vendas TOTVS Colaboração 2.0
type: support-article
updated_at: '2021-04-28T15:15:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026580734-MP-FAT-Como-validar-a-gera%C3%A7%C3%A3o-do-pedido-de-vendas-TOTVS-Colabora%C3%A7%C3%A3o-2-0
---

**Dúvida**

Como validar a geração do pedido de vendas TOTVS Colaboração 2.0?  
  
**Ambiente**

Microsiga Protheus -  a partir da versão 12.  
  
**Solução**

1. Confira nos arquivos de logs contidos na pasta XML dentro do start path do Protheus;

2. Verifique no SIGAFAT se o pedido realmente foi gerado;

3. Acesse a APSDU, abra a tabela CKOCOL;

 4. Verifique se o campo CKO\_FLAG contém ‘1’. Se sim, significa que o arquivo foi processado com sucesso e o pedido foi gerado;

5. Abra a tabela SC6;

 6. Filtre pelo pedido gerado e verifique se o campo C6\_PEDCLI condiz com o numéro contido no XML conforme tag \_OrderID;

7. Abra a tabela SC5;

 8. Verifique se o campo C5\_ORIGEM contem a informação MATA411.

Para visualização das telas, acesse a FAQ no TDN: **[FAT0221\_Como\_Validar\_A\_Geracao\_Do\_Pedido\_De\_Vendas\_Totvs\_Colaboracao\_2.0](%C2%A0http://tdn.totvs.com/display/public/PROT/FAT0221_Como_Validar_A_Geracao_Do_Pedido_De_Vendas_Totvs_Colaboracao_2.0)**

**SAIBA MAIS:**  
  
1 - Orientações gerais sobre o TOTVS Colaboração 2.0 podem ser obtidas no link abaixo :

**<http://tdn.totvs.com/pages/releaseview.action?pageId=240976575>**

2 - Pre Requisitos de cadastro Protheus para Totvs Colaboração 2.0 :

**<http://tdn.totvs.com/pages/viewpage.action?pageId=283401659>**
