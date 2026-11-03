---
article_id: 360047217294
category: Manutenção de Ativos (SIGAMNT)
content_hash: 2eae676cb65e5b698aea9885409b9d99841714a15af1b3a04934a3913e05acb4
fetched_at: '2026-06-28T22:42:34.090670+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Help Placa no cadastro do bem
type: support-article
updated_at: '2021-07-06T17:01:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047217294-Manufatura-Linha-Protheus-MNT-Help-Placa-no-cadastro-do-bem
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**Ao incluir um **bem** no módulo de **Manutenção de Ativos** está apresentando o *help* **Placa**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069867453/mceclip0.png)

**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Causa**O *help* é apresentado quando o usuário está incluindo um **veículo** com uma **placa** já existente na tabela **ST9 - Cadastro de bens**.   
  
**Solução**Por conceito do Sistema, o *help* sempre será apresentado quando na **inclusão** de um veículo, **em qualquer filial**, for informado uma placa de outro cadastro já existente.   
  
Quando é efetuado a transferência do **veículo**, o mesmo fica como inativo na filial de origem, desta forma, por se tratar de transferência o Sistema irá permitir que existam dois registros para a mesma placa.  
  
Não é permitido pois é possível efetuar o abastecimento do **veículo** em qualquer filial, e no abastecimento manual, pode ser informado a placa como busca do veículo, onde irá gerar o conflito de cadastros.  
  
Desta forma, caso queira que veículo fique cadastrado em várias filiais, recomenda-se que o compartilhamento da tabela **ST9** fique como **Compartilhado**.
