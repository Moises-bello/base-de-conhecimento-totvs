---
article_id: 35789452003607
category: eSocial
content_hash: 90079daab48992b28fcbaca7faf63bf66bad2a41d550adc7efb4c98c333cb15b
fetched_at: '2026-06-28T22:47:15.278511+00:00'
product: rm
section_id: 11645725240471
source: central-rm
title: 'RH - RM - RHU - eSocial - S-2501 - Erro código 632: Ja existe no evento um
  grupo com mesma chave de identificacao'
type: support-article
updated_at: '2025-10-23T13:27:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35789452003607-RH-RM-RHU-eSocial-S-2501-Erro-c%C3%B3digo-632-Ja-existe-no-evento-um-grupo-com-mesma-chave-de-identificacao
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35789451960215) Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**  
Ao gerar o XML do evento S-2501, está sendo apresentada a seguinte mensagem de erro:

***- Erro código 632: Ja existe no evento um grupo com mesma chave de identificacao.***

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35789451961367)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **12.1.2209.155 e superiores.**

**Causa**  
Este erro na transmissão do evento ocorre quando há códigos de receita duplicados no XML do evento e este campo não pode se repetir para o mesmo período.   
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Verifique se os códigos de receita gerados para os períodos presentes no evento S-2501 não foram repetidos para um mesmo período de pagamento;
2. Caso identifique a repetição do código, faça os ajustes necessários no sistema para que este código não se repita para o mesmo período;
3. Após a correção, gere novamente o XML do evento;
4. Realize o envio do evento novamente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35814881623575)

**Saiba Mais**  
Para maiores informações, acesse:

- [RH - RM - RHU - Dúvidas frequentes: geração dos eventos de Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17623656599575)
