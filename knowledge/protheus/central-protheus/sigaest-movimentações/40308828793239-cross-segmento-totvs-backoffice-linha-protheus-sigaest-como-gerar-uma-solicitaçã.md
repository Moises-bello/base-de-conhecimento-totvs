---
article_id: 40308828793239
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 1ed666f49f8c62f179fc2c80d797d1a667705eaa469f809a56082066a0d64bfe
fetched_at: '2026-06-28T22:38:58.476659+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Como gerar uma
  Solicitação de Compra a partir de uma Solicitação ao Armazém
type: support-article
updated_at: '2026-05-07T19:17:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40308828793239-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEST-Como-gerar-uma-Solicita%C3%A7%C3%A3o-de-Compra-a-partir-de-uma-Solicita%C3%A7%C3%A3o-ao-Armaz%C3%A9m
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40308843869847) Tempo aproximado para leitura: 00**:**01:00 **min**  
  
**Dúvida**  
Como realizar o processo de geração de uma Solicitação de Compra (MATA110) utilizando como origem uma Solicitação ao Armazém (MATA105) no módulo de Estoque e Custos?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Todas as versões  
  
**Solução**  
Para gerar uma Solicitação de Compra (SC) através de uma Solicitação ao Armazém (SA), o sistema utiliza a rotina de Baixa da Pré Requisição. Este processo é indicado quando não há saldo em estoque para atender a requisição interna, disparando assim a necessidade de compra de forma vinculada.

1. Acesse o módulo Estoque e Custos (SIGAEST).

2. Vá em **Atualizações / Movimentações / Internas / Solicitação ao Armazém (MATA105)** e realize a inclusão da SA para o produto desejado.

![Captura de tela 2026-05-07 153455.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40308843876503)

3. Acesse a rotina **Atualizações / Movimentações / Internas / Gerar Pré-Requis. (MATA185)**.

3.1 Pressione a tecla **F12** do teclado para abrir os parâmetros da rotina.

3.2 Localize a pergunta **Gera Sol.Compras/Aut.Entrega?** e configure como **Sim**. Confirme o parâmetro.

![Captura de tela 2026-05-07 153217.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40308828780311)

3.3  Na tela de processamento, selecione a Solicitação ao Armazém (SA) desejada através do checkbox e clique no botão **Gera**.

![Captura de tela 2026-05-07 153701.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40308843878807)

4. O sistema processará a informação e gerará automaticamente o registro na rotina de Solicitação de Compras.

5. Para conferir, acesse o módulo Compras (SIGACOM) em Atualizações / Solicitações / Solicitação de Compras (MATA110) e verifique a SC gerada com a origem vinculada à SA.

![Captura de tela 2026-05-07 154430.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40308843882263)

**Saiba mais:**  
[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
