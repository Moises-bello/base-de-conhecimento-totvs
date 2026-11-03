---
article_id: 14944092570903
category: SIGAEST - CUSTOS
content_hash: 9017ba0de257c914e0566bc3da4b45ec63124289372bd9d1faf8f75eaceee5ef
fetched_at: '2026-06-28T22:39:02.234629+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330/MATA331 -
  Tela de lançamentos está sendo exibida mesmo marcando para não mostrar
type: support-article
updated_at: '2023-05-30T18:17:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14944092570903-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-MATA331-Tela-de-lan%C3%A7amentos-est%C3%A1-sendo-exibida-mesmo-marcando-para-n%C3%A3o-mostrar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:13 min** **Dúvida**Ao rodar o Recálculo do Custo Médio, mesmo optando pelo flag "Não" no campo "Mostrar lançamentos", ainda assim abre a janela de contabilização. Como fazer para omitir essa exibição?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**Esta tela abre neste cenário quando existe alguma inconsistência em algum lançamento, ignorando o flag "Não" da pergunta "Mostrar Lançamentos Contábeis".

Isso acontece porque ou parâmetro MV\_CT105MS ou o parâmetro MV\_ALTLCTO estão ativos no Sistema.

O parâmetro **MV\_CT105MS** é utilizado para indicar se serão exibidas mensagens de alerta ao encontrar inconsistências em lançamentos de integração, caso o o sistema estiver configurado para não permitir a alteração destes lançamentos no momento da contabilização (parâmetro **MV\_ALTLCTO**com conteúdo N)

**Conteúdo do parâmetro MV\_CT105MS:**

 **1** - **S** - Mostra mensagem.

 **2** - **N** - Não mostra mensagem.

Desta forma, ambos estiverem = N, tendo ou não inconsistência, o flag será respeitado e não abrirá a tela de lançamentos.

Vale lembrar que, caso tenha alguma inconsistência, pelo fato da rotina não mostrar mais devido a essa configuração (caso o usuário tenha feito), cabe a ele, posteriormente, via rotina CTBA350, ajustar os lançamentos manualmente.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
