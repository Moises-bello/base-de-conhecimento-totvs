---
article_id: 8743505709335
category: Meu RH - Pagamento
content_hash: 07aa1aab98228e9209b31368de620b58478d35d77acc47ef7c8565f836e4f0f6
fetched_at: '2026-06-28T22:47:33.871167+00:00'
product: rm
section_id: 1500000835221
source: central-rm
title: 'RH - RM - Meu RH - Lentidão para realizar download do envelope de pagamento
  no Meu RH '
type: support-article
updated_at: '2025-02-03T17:50:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8743505709335-RH-RM-Meu-RH-Lentid%C3%A3o-para-realizar-download-do-envelope-de-pagamento-no-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:44 min****Ocorrência**No Meu RH, ao tentar realizar o download do envelope de pagamento a tela fica somente carregando apresentando lentidão excessiva.

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) – Meu RH – Todas as versões  
  
**Causa**  
Esse incidente ocorre, pois a Logotipo da coligada possui o formato muito grande ou está corrompida.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse: **Configurações | Parametrizador | RM Portal** e Edite o grupo do quiosque utilizado pelo usuário. Na aba **Demonstrativo de Pagamento**, desmarque a Flag **"Mostra Logotipo".**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8743481952535/mceclip1.png)**

2. Acesse o menu "Executar" do RM e pesquise pela rotina "Manutenção do Cadastro de Seções".

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8744809771799/mceclip2.png)

3. Selecione a rotina de manutenção do cadastro de seções e confira se sua execução foi realizada com sucesso.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8744873016087/mceclip3.png)

**Importante**

A rotina "Manutenção de Seção" **não causa nenhum impacto negativo**, poderá ser sempre executada caso suspeite de instabilidades no Meu RH e preferencialmente sempre executá-la caso houver inclusão / alteração / exclusão de seções no cadastro de seções da Folha de Pagamento.

**Saiba mais**

[Clique aqui para mais informações sobre Demonstrativo de Pagamento](https://tdn.totvs.com/display/public/NPR/6.0++Demonstrativo+de+Pagamento)

[Clique aqui para informações de como disponibilizar envelopes de pagamento no Meu RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024567074-RH-RM-Meu-RH-Como-disponibilizar-envelopes-de-pagamento-no-Meu-RH)
