---
article_id: 360027681571
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: f16b47933749361fe57e76ef19144b5b97cb7de6b8328c1e6359164a5839a2fb
fetched_at: '2026-06-28T22:42:43.387601+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Impedir abertura de OP para produto
  sem estrutura
type: support-article
updated_at: '2021-07-29T16:02:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027681571-Manufatura-Linha-Protheus-SIGAPCP-Impedir-abertura-de-OP-para-produto-sem-estrutura
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:00:50 min****Dúvida**É possível impedir a abertura de uma **OP - Ordem de Produção** para um produto sem estrutura?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - A partir da versão 11.80  
  
**Solução**Não existe parametrização na rotina **MATA650 - Ordens de Produção** para impedir a abertura de uma **OP** para um produto que não tenha estrutura cadastrada na rotina **MATA200 - Estruturas**. Porém, existe o **PE - Ponto de entrada** **MA650TOK - Permite executar a validação do usuário ao confirmar a OP** que permite implementação desta validação.  
  
**Saiba mais**  
Para consultar a documentação deste **PE** consulte o *link* [MA650TOK - Válida Usuário](http://tdn.totvs.com/pages/viewpage.action?pageId=322148838)
