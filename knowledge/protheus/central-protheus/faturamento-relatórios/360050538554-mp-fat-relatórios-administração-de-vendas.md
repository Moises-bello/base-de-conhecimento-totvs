---
article_id: 360050538554
category: FATURAMENTO - RELATÓRIOS
content_hash: 8d3631c45a3b9dac827526ec70c487a49552cf5a4b55e3fbb17cec423cda04a7
fetched_at: '2026-06-28T22:38:23.025639+00:00'
product: protheus
section_id: 1500001539381
source: central-protheus
title: MP-FAT- Relatórios Administração de Vendas
type: support-article
updated_at: '2021-04-28T15:15:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050538554-MP-FAT-Relat%C3%B3rios-Administra%C3%A7%C3%A3o-de-Vendas
---

**Dúvida**

Quais filtros e informações são impressas nos relatórios do administração de vendas no módulo Faturamento.  
  
 **Ambiente**

Microsiga Protheus - Versão 12

**Solução**

Filtros e informações que são impressa relatórios do administração de vendas:

**FATR010 - Oportunidades**  
Este relatório relaciona as oportunidades apresentando informações tais como: descrição, vendedor, razão social do prospect, processo, estagio, receita, moeda e status. Nos parâmetros é possível filtrar por prospect, representante(vendedores), processo, etapa(estagio), produto e status da oportunidade.

* O parâmetro de prospect de vazio á "ZZZZZ" irá relacionar todas as oportunidades inclusive de cliente, porem, não exibirá os dados do cliente.

**FATR020 - Processos de Venda**  
Este relatório relaciona as processos de vendas apresentando informações tais como: processo, descrição, estagio e contribui. Nos parâmetros é possível filtrar por processos.

**FATR030 - Contrato de Parceria**  
Este relatório relaciona os contratos de parceiras apresentando informações tais como: status do contrato, numero do contrato, emissão, cliente, produto, quantidade, preço. Nos parâmetros é possível filtrar por cliente, loja, produto, moeda,  
 produto e status do contrato. A impressão de pode ser analítica ou sintética.

* O numero de pedido de venda gerado pelo contrato é apresentado na impressão analítica.

**FATR050 - Metas x Realizado / Relação de Metas de Vendas X Vendas realizadas**  
Possibilita que seja feito um comparativo, por região, entre as metas de vendas e as vendas que de fato foram realizadas.  
 O sistema relaciona, por produto, as quantidades e valores definidos nas metas e as quantidades e valores vendidos, apresentando a diferença entre eles.  
 A impressão deste relatório considera as informações respeitando a posição do Vendedor na Estrutura de Negócio.

**FATR070 - Propostas Comercial**  
Este relatório relaciona as propostas com possibilidade de filtrar por data, vendedor, produto, segmento, entidade(ambos, cliente ou prospect). A impressão é possível configurar a quebra por entidade, produto, vendedor e segmento e se analítico ou sintético.

* Informações impressa na analítica: a quebra definida(entidade, produto, vendedor e segmento), proposta, oportunidade, tabela de preço cliente, produto, preço unitário e tabela.
* Informações impressa no sintético: a quebra definida(entidade, produto, vendedor e segmento), total geral de todas proposta por item e valor.

**FATR060 - Oportunidades X Processos de Vendas**  
Este relatório relaciona as oportunidade por processo de venda com possibilidade de filtrar por data, processo, vendedor, considerar oportunidade(todas, aberta, perdido, suspenso e encerrado),  desconsiderar oportunidades(nenhum, aberta, perdido, suspenso e encerrado) e moeda. Informações apresentadas na impressão é processo, estagio, código oportunidade, receita, revisão, cliente, data inclusão, vendedor.

**Saiba mais: [relatórios no módulo Faturamento](https://tdn.totvs.com/x/4xP3Fw)**
