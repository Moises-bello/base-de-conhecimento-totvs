---
article_id: 360017466452
category: Materiais - Compras (SIGACOM)
content_hash: 8bc86d949e26c0630a91aeb5c1444b2efb30dd6e581d18ff592d77b31a724d52
fetched_at: '2026-06-28T22:41:08.878693+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Fornecedor Bloqueado
  ao Analisar Cotação
type: support-article
updated_at: '2023-02-06T19:36:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017466452-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Fornecedor-Bloqueado-ao-Analisar-Cota%C3%A7%C3%A3o
---

**Ocorrência**

Fornecedor Bloqueado ao Analisar Cotação

**Ambiente**

Protheus - Compras - A partir da versão 12.1.17  
  
**Causa**

No módulo **Compras**, ao Analisar Cotação, caso no Cadastro do Fornecedor caso esteja o campo A2\_MSBLQL em Branco, apresenta a mensagem: "Impossível analisar a cotação, todos os fornecedores listados estão bloqueados, por favor execute o desbloqueio de algum fornecedor para executar esta operação".

Esse incidente ocorre, pois o campo A2\_MSBLQL na rotina MATA020 - Cadastro de Fornecedor,  está em branco, ao Analisar a Cotação apresenta a mensagem.  
  
**Solução**

Acessa a rotina MATA020 - Cadastro de Fornecedor.

Selecione o Fornecedor que foi gerado a Analise de Cotação e clique na opção Alterar e insira o valor no campo Bloqueio (A2\_MSBLQL) para a opção 2- Não.

Após modificar, Acessar a rotina Analise de Cotação, faça o procedimento.
