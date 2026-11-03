---
article_id: 26653213835031
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 0312ffab200b3288ded61eeb49b7ff7de7152a5daeb920f0f945542c54278334
fetched_at: '2026-06-28T22:38:55.796972+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA185 - Ao emitir
  o Termo de Retirada de uma S.A, sai os dados de outra. O que fazer?
type: support-article
updated_at: '2024-09-26T19:38:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26653213835031-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA185-Ao-emitir-o-Termo-de-Retirada-de-uma-S-A-sai-os-dados-de-outra-O-que-fazer
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26653255846423) Tempo aproximado para leitura: **00:03:12 min** **Dúvida**Ao emitir o Termo de Retirada na rotina Baixa de Pré-Requisição (MATA185), é exibido o Termo de outra Solicitação ao Armazém diferente da que selecionei. O que fazer?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**O Termo de Retirada na rotina de Baixa de Pré-Requisição é um recurso que chama um relatório. Para evitar este tipo de problema, considere as informações abaixo:

1 - Clique em cima da S.A que deseja gerar o Termo de Retirada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26653213808151)

2 - Clique em Outras Ações -> Termo de Retirada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26653255848471)

3 - Será aberta a tela da chamada do Relatório do Termo. É **imprescindível** clicar em Outras Ações -> Parâmetros:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26653213813783)

4 - Neste caso, note que a S.A que marcamos anteriormente para emitir o termo é a de número **000018,** no entanto, conforme imagem abaixo, já estava parametrizada a S.A de número **000002.** Se o usuário não alterar para a S.A que ele deseja emitir o Termo, ele vai considerar a S.A (neste exemplo) de número **000002**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26653213816471)

5 - Altere a S.A para a desejada (neste caso, a 00018). Atente-se também às perguntas "Data Solicitação De" e "Data Solicitação Até". Se a S.A 000018, neste exemplo, estiver fora do período de 01/01/2000 até 04/03/2024, não será gerado o Termo de Retirada dele.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26653255854615)

6 - Após inserir a S.A correta e o período de data correto, a impressão do Termo será da S.A desejada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26653255855383)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
