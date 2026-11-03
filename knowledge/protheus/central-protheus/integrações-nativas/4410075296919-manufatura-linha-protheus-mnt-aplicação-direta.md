---
article_id: 4410075296919
category: Integrações Nativas
content_hash: 01d5febe3159cc5781003fd3b2cd053e80c582fcfdfa50ace4542073032ebe54
fetched_at: '2026-06-28T22:42:35.324355+00:00'
product: protheus
section_id: 360012117933
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Aplicação Direta
type: support-article
updated_at: '2021-10-29T11:37:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410075296919-Manufatura-Linha-Protheus-MNT-Aplica%C3%A7%C3%A3o-Direta
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:00:40 min** **Dúvida**Qual é o processo de aplicação direta no **Manutenção de Ativos - SIGAMNT?**  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integrações Nativas - Todas as versões  
  
**Solução**Ao incluir um documento de entrada relacionando a **Ordem de Serviço - O.S**, o Sistema não altera o **Estoque**. Toda saída de **Estoque** relacionada a uma **O.S.** de manutenção deverá ter o número da **O.S.** informado no campo **Ordem de Serviço -** **D3\_ORDEM**. Com esta providência o módulo **Estoque/ Custos - SIGAEST** irá gerar automaticamente um registro de consumo de **Insumo - STL** no módulo **Manutenção de Ativos** . Assim movimentação do produto é relacionada diretamente com a **O.S**, ou seja, o produto já é predestinado para a **O.S**.
