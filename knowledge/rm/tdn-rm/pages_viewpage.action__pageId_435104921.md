---
content_hash: 018a1284fa971f10b68965029ee4627edd9a6e275ea819bb261e897646c76e7f
fetched_at: '2026-06-29T00:09:47.097989+00:00'
page_id: '435104921'
product: rm
source: tdn-rm
title: Efetivar Contrato Vendas e Aluguéis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435104921
version: 2
---

**Efetivar Contrato**   
 A partir da versão 11.20 a efetivação de Vendas e Aluguéis será executada através da opção de Processos | Efetivar Contrato que se localiza na tela de Vendas/Aluguéis.  
    
 Em versões anteriores este processo é realizado através botão de efetivação.  
    
 Efetivar a venda significa que o cliente concordou com as condições e confirmou a compra. Com isso, o RM Fluxus já estará apto para administrar os recebíveis das Vendas e Aluguéis.  
    
 Ao selecionar uma venda ou aluguel que já tenha gerado o seu plano de financiamento e clicar nesta opção, a venda é efetivada e a situação da sub-unidade passará para "Vendido" para o caso das vendas e "Alugado" para o caso dos aluguéis, desde que esta venda não tenha nenhuma pendência.  
    
 **Observações:**  
  1 - Se o parâmetro "**Efetivar venda e gerar lançamentos no RMFluxus**", localizado em Menu Opções | Parâmetros | RM SGI | Integração Financeira | Integração Fin. Param. Colig 4/4, estiver marcado, ao efetivar a venda, o sistema irá gerar lançamentos para o TOTVS Gestão Financeira automaticamente.  
 2 - Ao efetivar a venda, o sistema irá verificar no parâmetro "**Consistir na efetivação as seguintes condições**", através do Menu Opções | Parâmetros | RM SGI | Contrato | Efetivação | , o que irá consistir as condições para a efetivação da venda.  
 O sistema poderá impedir, alertar ou não fazer consistência sobre as seguintes opções:

* Consistir na efetivação se existe parcelas;
* Consistir na efetivação se existe lote;
* Consiste na efetivação se existe endereço do cliente;
* Consiste na efetivação se a contabilização é obrigatória;
* Consistir se foi gerado movimento para a(s) comissão(ões) cadastrada(s);
