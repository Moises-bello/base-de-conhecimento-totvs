---
article_id: 360022029352
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 869128a04e70a5ad811d7d3b3c02d891c25a96f0a2f33d3d966817300b332aa2
fetched_at: '2026-06-28T22:42:43.280010+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Função CalcPrazo
type: support-article
updated_at: '2024-05-20T17:20:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022029352-Manufatura-Linha-Protheus-SIGAPCP-Fun%C3%A7%C3%A3o-CalcPrazo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:35 min  
  
Dúvida**Qual a origem e finalidade da função **CalcPrazo**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12.1.17  
  
**Solução**Essa rotina calcula o prazo de entrega do produto com base no roteiro de operações ou do cadastro de produtos e pode ser visível no relatório **MATR110 - Pedidos de Compra**, para isso ele valida o parâmetro **MV\_PEOPERA - O prazo de entrega dos produtos fabricados deve ser calculado pelo roteiro de operações?**.  
Quando o parâmetro **MV\_PEOPERA** estiver como **T**, indica que o cálculo será pelo roteiro de operações, onde a rotina levará em consideração informações de **calendário**, **Lote Padrão - G2\_LOTEPAD**, **Tipo de Operação - G2\_TPOPER** e **Tempo Padrão - G2\_TEMPAD**, além da **Fórmula Setup -** **G2\_FORMSTP** ou **Setup (Hs) - G2\_SETUP** e **Tempo Fim -** **G2\_TEMPEND** da operação. Se no **Cadastro do Produto - MATA010** ou na **Ordem de Produção - MATA650** não estiverem com o roteiro informado, será considerado o **roteiro padrão 01**.  
Caso esteja indicado para calcular pelo cadastro de produto, ou seja, quando o parâmetro está **em branco** ou como **F**, as informações consideradas são **Prazo de Entrega -** **B1\_PE** e **Tipo Prazo - B1\_TIPE** ou a **Fórmula Prazo -** **B1\_FORPRZ** cadastrada**.**
