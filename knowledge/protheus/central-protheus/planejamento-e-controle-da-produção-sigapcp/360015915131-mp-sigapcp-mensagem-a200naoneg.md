---
article_id: 360015915131
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 2c00e3fb0f2ec2954b049e689fe44df2acba9b0806bad372a5888cb1ef5fb80b
fetched_at: '2026-06-28T22:42:47.236117+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: MP - SIGAPCP - Mensagem A200NAONEG
type: support-article
updated_at: '2020-09-24T18:34:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015915131-MP-SIGAPCP-Mensagem-A200NAONEG
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:00:35 min  
Ocorrência**Ao incluir um componente com quantidade negativa no **MATA200 - Estrutura** é apresentada a mensagem **A200NAONEG**.  
  
 **Ambiente**Microsiga Protheus - Planejamento e Controle da Produção - Versão 12  
  
**Causa**Essa situação ocorre pois o parâmetro **MV\_NEGESTR - Permite incluir itens negativos na estrutura, sendo que estes itens gerarão devoluções no arquivo de movimentos nos módulos de Estoque/PCP** está desativado.  
  
**Solução**  
Ativar o parâmetro **MV\_NEGESTR**, desta forma o sistema permite a inclusão de produtos negativos na estrutura.
