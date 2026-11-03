---
article_id: 360031705093
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 09827cb3bac69bd5738069d50d4c910b2af9ab2caa961acf24cc7e67180f741e
fetched_at: '2026-06-28T22:38:44.024825+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Compensação automática na
  devolução de compras e vendas
type: support-article
updated_at: '2024-10-29T13:07:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360031705093-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Compensa%C3%A7%C3%A3o-autom%C3%A1tica-na-devolu%C3%A7%C3%A3o-de-compras-e-vendas
---

**Dúvida**Compensação automática na devolução de compras e vendas  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da versão 12.

**Solução**Para que ocorra a compensação automática, seja pela nota de devolução de compra (**MATA461**) ou pela nota de devolução de venda (**MATA103**) é necessário que:

**1** - Se for devolução de compra: o parâmetro **MV\_CMPDEVC**esteja igual a **T**;  
**2** - Se for devolução de venda: o parâmetro **MV\_CMPDEVV** esteja igual **T**;  
**3** - O parâmetro **MV\_CHECKNF** esteja igual a **F**;  
**4** - O título não pode estar em borderô. Se houve a transferência para borderô, a compensação deve ser feita de forma manual.  
**5 -** O TES (**MATA080**) deve estar configurado como "Gera duplicata=SIM".  
**6** - A Devolução de Compras (**MATA461**) trata a Compensação Automática do título da devolução parcial ou total. Já para Devolução de Vendas (**MATA103**), foi implementada uma melhoria para tratar de devolução de vendas parcial, maiores detalhes acesse a documentação da equipe de desenvolvimento: **<https://tdn.totvs.com/pages/releaseview.action?pageId=271404820>**

Segue descrição dos parâmetros:

**MV\_CMPDEVC** - Indica se serão compensados automaticamente os títulos do tipo "**NDF** - Nota de          Débito ao Fornecedor" (devolução de compras);

**MV\_CMPDEVV**- Indica se serão compensados automaticamente os títulos do tipo "**NCC** - Nota de          Crédito ao Cliente" (devolução de vendas);

**MV\_CHECKNF** - Descrição: Verificar a situação do título (se foi transferido ou não), antes de efetuar          a compensação automática.

Obs. A compensação automática, em situações onde há mais de um título (parcelas) gerado pela nota de origem, o sistema sempre irá iniciar a baixa do NDF/ NCC a partir da primeira parcela, baixando-a integralmente e seguindo para baixas posteriores conforme houver saldo.
