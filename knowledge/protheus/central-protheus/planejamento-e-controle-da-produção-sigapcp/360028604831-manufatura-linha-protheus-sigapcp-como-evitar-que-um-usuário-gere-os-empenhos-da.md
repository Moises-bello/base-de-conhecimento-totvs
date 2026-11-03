---
article_id: 360028604831
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: a79ff807f84d04532411a1e4eff60303356934500dcaf34de2c41648ec129f8b
fetched_at: '2026-06-28T22:42:41.098035+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Como evitar que um usuário gere os
  empenhos da OP cadastrada por outro usuário
type: support-article
updated_at: '2021-05-26T11:34:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028604831-Manufatura-Linha-Protheus-SIGAPCP-Como-evitar-que-um-usu%C3%A1rio-gere-os-empenhos-da-OP-cadastrada-por-outro-usu%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:50min****Dúvida**Como evitar que um usuário gere os empenhos da **OP - Ordem de Produção** cadastrada por outro usuário?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
Para que cada usuário gere os empenhos somente das **OPs** cadastradas por ele, não gerando os empenhos de **OPs** de outro usuário, é necessário alterar o conteúdo do parâmetro **MV\_EXPLOPU - Se o parâmetro estiver com o conteúdo igual a S será gerada OPs intermediarias/SC, somente para o usuário corrente**para **S - Sim**. Desta forma, o Sistema faz com que cada usuário inicie o processo de geração de empenhos somente das **OPs** cadastradas pelo usuário logado, ficando as demais em aberto, aguardando a execução do processo pelo usuário que a gerou.
