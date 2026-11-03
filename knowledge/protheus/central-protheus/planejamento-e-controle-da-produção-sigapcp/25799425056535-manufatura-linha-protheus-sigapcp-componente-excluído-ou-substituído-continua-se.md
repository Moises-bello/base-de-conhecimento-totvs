---
article_id: 25799425056535
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 5dd607433870f60ef0650e9277404d095385460e99f0112a7ea4e037c4e2ab46
fetched_at: '2026-06-28T22:42:42.066214+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Componente excluído  ou substituído
  continua sendo listado no browse
type: support-article
updated_at: '2024-08-22T19:01:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25799425056535-Manufatura-Linha-Protheus-SIGAPCP-Componente-exclu%C3%ADdo-ou-substitu%C3%ADdo-continua-sendo-listado-no-browse
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25799425044631) Tempo aproximado para leitura: **00:01:19 min** **Dúvida**Por que ao excluir um componente da estrutura no **PCPA200**, ou usar o processo de substituição para substituí-lo por outro , o mesmo continua sendo listado no *browse*, mas ao consultar a estrutura ele não é listado?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Esse comportamento é normal quando o parâmetro **MV\_REVAUT** tem o conteúdo **T** , nesta situação ao excluir ou substituir o componente da estrutura o Sistema gera uma nova revisão com o novo cenário da estrutura, mas não exclui o componente substituído ou excluído da tabela **SG1**, deixando somente restrito à revisão anterior com o objetivo de manter o histórico das manutenções realizadas.  
Sendo assim, como o *browse* lista os registros da tabela **SG1**, o componente substituído ou excluído que está numa revisão anterior a atual continua sendo listado  
  
**Glossário  
PCPA200** - Cadastro de estrutura **MV\_REVAUT** - Indica se o controle de revisões será controlado automaticamente   
**SG1** - Estruturas dos produtos
