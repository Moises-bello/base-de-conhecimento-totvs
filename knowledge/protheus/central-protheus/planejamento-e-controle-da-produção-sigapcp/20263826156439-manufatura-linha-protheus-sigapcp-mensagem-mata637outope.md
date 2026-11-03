---
article_id: 20263826156439
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: ed946428f6c011d491aeced404b7040d8529dfd5e05c93ca02f9da059029a893
fetched_at: '2026-06-28T22:42:44.508979+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem MATA637OUTOPE
type: support-article
updated_at: '2024-01-02T18:05:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20263826156439-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-MATA637OUTOPE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20263811363991) Tempo aproximado para leitura: **00:01:31 min****Ocorrência**Ao tentar relacionar operação com componente na rotina **MATA637 - Operação x Componentes** ou através da rotina **PCPA200 - Cadastro de Estruturas** é apresentada a mensagem **MATA637OUTOPE -** **Componente já está sendo usado em outra operação**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**A mensagem **MATA637OUTOPE** ocorre quando o componente e sequência selecionado já está relacionado com uma operação e o usuário deseja vincular o mesmo componente com outra operação.  
  
**Solução**Para que consiga relacionar o componente com duas ou mais operações é necessário incluir o mesmo componente na estrutura com o campo **G1\_TRT - Sequencia** com o conteúdo diferente para cada registro, e depois relacionar cada um desses registros com a operação desejada.  
  
**Exemplo**Se for necessário relacionar o MP01 com três operações diferentes, deve ser feita a inclusão de três registros do MP01 na estrutura, conforme print abaixo, onde o campo **G1\_TRT - Sequência** deve possuir conteúdo diferente para cada registro

**![Imagem01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20263811365783)**Na sequência deve ser realizado o relacionamento de cada registro do MP01 na estrutura com a operação na qual deve ocorrer a sua requisição. **![](https://centraldeatendimento.totvs.com/hc/article_attachments/20263811367063)**
