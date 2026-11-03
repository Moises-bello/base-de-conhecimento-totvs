---
article_id: 4402836482199
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: eba7a79f94fed61fd9b6e88c85fef50910e13b5ae6d1aee22a0793cf0a298fba
fetched_at: '2026-06-28T22:42:44.517493+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem não existe nenhum produto
  a ser criado com o conteúdo selecionado
type: support-article
updated_at: '2021-06-18T10:54:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402836482199-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-n%C3%A3o-existe-nenhum-produto-a-ser-criado-com-o-conte%C3%BAdo-selecionado
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:45 min**  
**Ocorrência**No **MATA093 - Configurador de Produtos**, ao utilizar a opção **Gera Automático** surge a mensagem não **Não existe nenhum produto a ser criado com o conteúdo selecionado**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**Essa mensagem surge quando o Sistema já encontra na tabela **SB1 - Descrição Genérica de Produto** todos os produtos que poderiam ser gerados através desta família  
  
**Solução**Inclua no **MATA093** uma família de produtos e características e no **MATA098 - Codificação** determine as opções de cada característica de modo que o resultado dos códigos de produtos gerados não existam previamente na tabela **SB1.**
