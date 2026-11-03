---
article_id: 30875676663319
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: c08a6da70283584255bfef5376f1c26db0bcb59153d28070c4289ae4732f0a9b
fetched_at: '2026-06-28T22:39:08.012359+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - AGRA045 - Como excluir
  um armazem com dados históricos?
type: support-article
updated_at: '2025-03-24T13:46:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30875676663319-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-AGRA045-Como-excluir-um-armazem-com-dados-hist%C3%B3ricos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30875703327383) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como posso efetuar a exclusão de um armazem, que ja teve movimentos ou saldos, e agora esta zerado?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Estoque/Cusots - Todas as versões  
  
**Solução**

**Como excluir um armazem que ja teve dados gravados?**

**Não há essa possibilidade**, devido a registro histórico no local, você não podera excluir, pois isso ira afetar por exemplo, uma relação de movimentos que ocorreram nesse armazem, se você viesse a consultar em um relatorio de movimentos, portanto o sistema não permite.

![Screenshot_18.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30875676650263)

**Mas eu não quero mais que ninguem movimente nada nesse armazem:**

Você pode realizar o bloqueio do armazem, a exclusão não sera possivel devido integridade do sistema.

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - AGRA045 - Como bloquear armazém para movimentações?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022132132-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-AGRA045-Como-bloquear-armaz%C3%A9m-para-movimenta%C3%A7%C3%B5es)

**Ja para locais que foram criados, e nunca tiveram nada veiculados ao mesmo:**

o processo de exclusão é o seuginte: voce pode ir na rotina **"Locais de Estoque - AGRA045"(SIGAEST>Atualizações > Cadastros > Produto > Locais de Estoque)**, selecionar o "armazem" desejado, e clicar em **"Outras Ações > Excluir"**

![Screenshot_16.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30875676647959)

Sera aberto uma tela, basta clicar em **Confirmar**, e ele sera excluido.

![Screenshot_17.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30875676649111)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
