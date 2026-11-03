---
article_id: 34880002888215
category: Meu RH - Ponto
content_hash: c7d82dd2607d41b70fef3bc45a9588a164ff4f77bf47bf68013f9e93ca0af399
fetched_at: '2026-06-28T22:47:30.264385+00:00'
product: rm
section_id: 1500000861782
source: central-rm
title: 'RH - RM - Meu RH - Erro ao incluir batida: Permitido inserir batidas apenas
  do inicio do período atual até o dia de hoje'
type: support-article
updated_at: '2026-01-13T18:48:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34880002888215-RH-RM-Meu-RH-Erro-ao-incluir-batida-Permitido-inserir-batidas-apenas-do-inicio-do-per%C3%ADodo-atual-at%C3%A9-o-dia-de-hoje
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34879966179223) Tempo aproximado para leitura:  **00:03:30 min**  
  
**Ocorrência**  
Ao incluir batida manual é apresentado o erro "Permitido inserir batidas apenas do inicio do período atual até o dia de hoje.".  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Causa**  
O erro ocorre devido a parametrização de batidas no módulo de automação de ponto, em Configurações **l** Parametrizador **l** Batidas que impede o lançamento de batidas em datas posteriores a atual ou fora do período.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35029817295511)

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/35029833506455)**  
  
**Solução**

De acordo com a parametrização, só é permitido inserir batidas em datas desde o início do período até a data atual. Inserções em datas futuras são bloqueadas. Para registrar batidas em dias posteriores, é necessário alterar a parametrização.
