---
article_id: 360024933113
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 9ad2eb25a1e26bd586c7c0bf09314afd3ac61d9563459d7f8eeafc716467fb86
fetched_at: '2026-06-28T22:42:43.238484+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Filtros dos produtos no MRP
type: support-article
updated_at: '2024-05-27T13:39:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024933113-Manufatura-Linha-Protheus-SIGAPCP-Filtros-dos-produtos-no-MRP
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23763401670935)***Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**Como é possível filtrar os produtos para o cálculo do **MRP - Manufacturing Resources Planning** na rotina **PCPA712 - MRP Memória**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
Para o cálculo do **MRP** é possível filtrar os produtos por:

1. **Grupo de produtos** - selecionando os grupos de produtos para os quais deseja calcular a necessidade;
2. **Tipo de produto** - selecionando os tipos de produtos para os quais deseja calcular a necessidade;
3. Avaliando se o conteúdo do campo **B1\_MRP - Entra MRP,** do **Produto** no **MATA010 - Cadastro de Produto**, está igual a **S - Sim**;
4. Customizando o filtro através do uso do ponto de entrada [P712SQL](https://tdn.totvs.com/pages/releaseview.action?pageId=654300935).

**Importante**Não é possível filtrar os produtos definindo um código inicial e final de produtos.
