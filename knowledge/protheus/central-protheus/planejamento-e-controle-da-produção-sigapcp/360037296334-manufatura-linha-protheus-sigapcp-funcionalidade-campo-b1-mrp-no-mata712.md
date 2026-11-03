---
article_id: 360037296334
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 7c21b35a468e8b9a7efc3e2cbc68c211f8c734e77423009ce76ea94e8ac242d4
fetched_at: '2026-06-28T22:42:43.284138+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Funcionalidade campo B1_MRP no MATA712
type: support-article
updated_at: '2024-08-02T14:39:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037296334-Manufatura-Linha-Protheus-SIGAPCP-Funcionalidade-campo-B1-MRP-no-MATA712
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25364112118295)**Tempo aproximado para leitura: **00:01:21 min****Dúvida**Como funciona o campo **B1\_MRP - Entra MRP?** do **MATA010 - Produtos** no **MATA712 - MRP**?  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**Se utilizar a opção para **Sim** no campo **B1\_MRP**, o produto será calculado pelo **MRP -  Material Requirement Planning**. Logo, se tiver necessidade será gerado empenho desse produto.  
Se utilizar a opção para **Não** no campo **B1\_MRP**, além do produto não ser calculado pelo **MRP** o empenho também não será gerado se algum **PA - Produto Acabado** desse produto gerar **OP** **- Ordem de Produção**.   
  
Se utilizar a opção **Especial** no campo **B1\_MRP**, o **MRP** não irá calcular as necessidades desse produto, como por exemplo estoque de segurança, plano mestre de produção, previsão de vendas, ponto de pedido, entre outras. E o produto não será mostrado no **MRP**. Mas se ele for filho de algum **PA** que gerará uma **OP**, ele será empenhado.   
  
**Saiba mais**  
Segue também o documento sobre a implementação da opção [Especial](http://tdn.totvs.com/x/Ns-yE).
