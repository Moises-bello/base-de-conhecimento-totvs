---
article_id: 38601071149719
category: SIGAACD - Automação e Coleta de Dados
content_hash: 88e6a38a82e0f637ab65197fa4343d91998cf018e720c1e50abf3c354a093d74
fetched_at: '2026-06-28T22:39:12.706688+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Erro ao Excluir Lançamento
  de Inventário EOF Stack em MSRLOCK
type: support-article
updated_at: '2026-02-24T16:36:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38601071149719-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Erro-ao-Excluir-Lan%C3%A7amento-de-Invent%C3%A1rio-EOF-Stack-em-MSRLOCK
---

O erro "EOF Stack em MSRLOCK" no Protheus ocorre quando a rotina tenta manipular um registro não localizado, indicando quebra de integridade. Recomenda-se consultar o link fornecido para procedimentos detalhados de análise e solução do problema.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38601066671895) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Erro ao excluir o lançamento de inventário pelo SIGAACD, apresenta a mensagem "**EOF Stack em MSRLOCK**" como corrigir?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.

**Solução**  
A mensagem "EOF Stack em MSRLOCK" indica que a rotina tentou reservar um registro para ser manipulado no processamento; mas o ponteiro da tabela estava em FIM DE ARQUIVO (MODO EOF) pois não localizou o dado procurado na Tabela.

Ou seja, algum dado (relacionado a este registro que está sendo processado) está inválido / não foi localizado, apresentando quebra de integridade.  
   
Desenvolvemos a documentação [EOF Stack de chamadas em MSRLOCK.eof Controle de transaçoes Habilitado](https://tdn.totvs.com/pages/releaseview.action?pageId=235575485) onde no **tópico 3 (PROCEDIMENTOS)**, sugerimos uma série de avaliações a serem feitas, bem como explicamos com mais detalhes este erro. Peço gentilmente que valide.

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
