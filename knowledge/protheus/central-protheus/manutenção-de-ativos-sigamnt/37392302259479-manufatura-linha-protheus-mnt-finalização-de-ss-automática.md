---
article_id: 37392302259479
category: Manutenção de Ativos (SIGAMNT)
content_hash: c2c7fdf55d35e573c42fd72dcb3257d6b1354e651237f9e236c38fcfaa51d2a5
fetched_at: '2026-06-28T22:42:33.197094+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Finalização de S.S automática
type: support-article
updated_at: '2026-01-02T13:21:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37392302259479-Manufatura-Linha-Protheus-MNT-Finaliza%C3%A7%C3%A3o-de-S-S-autom%C3%A1tica
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37392302246551)*** Tempo aproximado para leitura: **00:01:14 min**  
  
**Dúvida**  
É possível finalizar a S.S automáticamente ao finalizar uma **Ordem de serviço - O.S** relacionada a **Solicitação de serviço - S.S**?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**  
Ao gerar uma **O.S** a partir da **S.S**,**a S.S não é transformada em uma O.S, tanto a S.S quanto a O.S são itens individuais** o que é gerado é um relacionamento entre a **S.S** e a **O.S**. Onde uma **S.S** pode possuir múltiplas **O.S** gerdas a partir da **S.S**.  
  
Com isso não existe nenhum processo ou parâmetrização para que a **S.S** seja finalizada automaticamente, os usuários do processo precisam ativamente realizar o processo de finalização da **S.S** para finalização da mesma. Ao finalizar uma **O.S** que tem relação com uma **O.S** é possível realizar os processos em conjunto.
