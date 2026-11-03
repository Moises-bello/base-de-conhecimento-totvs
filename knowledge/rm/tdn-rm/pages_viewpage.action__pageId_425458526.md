---
content_hash: 4ff894248d0cbe2c2c9d5daceab3c37b0c45a2122d90d959242a2b2fb439a74d
fetched_at: '2026-06-29T00:09:30.795774+00:00'
page_id: '425458526'
product: rm
source: tdn-rm
title: Corrigir questões fechadas da prova
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458526
version: 3
---

Por este  processo é possível realizar a correção de questões dos tipos **Exclusiva** ou **Múltiplas** executadas pelos candidatos em uma prova.

O objetivo da correção é determinar o índice de acerto e a nota obtida.

Os índices de acerto possíveis são: **Correta**, **Parcialmente correta** e **Incorreta**.

A nota obtida na questão é determinada a partir do peso dela na prova.

**Correção de provas do tipo Avaliação de conhecimento**

**Questões do tipo Exclusiva**

Se o candidato escolheu a opção correta, o índice de acerto será **Correta** e a nota obtida será igual ao peso da questão.

Se o candidato escolheu uma opção incorreta, o índice de acerto será **Incorreta** e a nota obtida será **ZERO**.

**Questões do tipo Múltiplas**

**a)** Para questões **sem compensação**:

* Se o candidato acertou todas as opções, o índice de acerto será definido como **Correta** e a nota obtida será igual ao peso da questão na prova.
* Se o candidato errou uma ou mais opções, o índice de acerto será definido como **Incorreta** e a nota obtida será **ZERO**.

**b)** Para questões **com compensação**:

Internamente é calculado o **APROVEITAMENTO** na questão que é dado por:   
**Soma do % de pontos das opções marcadas corretamente - Soma do % de pontos das opções marcadas erroneamente**.

* Se **APROVEITAMENTO >= 100**, então a nota é igual ao valor da questão e o índice de acerto é **Correta**.
* Se **APROVEITAMENTO <= 0**, então a nota é igual a **ZERO** e o índice de acerto é **Incorreta**.
* Se **APROVEITAMENTO > 0 e < 100**, então a nota será:  
  **APROVEITAMENTO \* VALOR DA QUESTÃO / 100**.  
    
  **Correção de provas do tipo Pesquisa de opinião**
  + - O sistema calcula o **SOMATÓRIO** do percentual de pontos de cada opção que o entrevistado marcou.
* Se o **SOMATÓRIO** calculado for:  
  **>= 100**, então o índice de acerto será **Correta** e a nota obtida será igual ao peso da questão.  
  **<= 0**, então o índice de acerto será **Incorreta** e a nota obtida será igual a **ZERO**.  
  **> 0 e <100**, então o índice de acerto será **Parcialmente correta** e a nota será proporcional ao peso da questão (**SOMATÓRIO \* Peso /100**).
