---
article_id: 14679089526423
category: ADVPL - Classe e Função
content_hash: 15dfc174e7a94395d04129494b066a7156df39035ecceca1d14507f02e2875b5
fetched_at: '2026-06-28T22:40:17.065436+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Operador XOR
type: support-article
updated_at: '2025-01-20T17:32:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14679089526423-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Operador-XOR
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Existe o operador XOR no AdvPL?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12  
  
**Solução**No Protheus, não existe um operador XOR nativo.

No entanto, é possível simular o comportamento do operador XOR usando outras construções da linguagem. Uma maneira comum de simular o operador XOR em ADVPL é mediante uma expressão condicional utilizando os operadores lógicos AND e OR, juntamente com o operador de negação NOT.

Aqui está um exemplo de como você pode implementar o operador XOR em ADVPL:

```
User Function XOR(lValueA, lValueB)   
  
Return (lValueA .and. .not. lValueB) .or. (lValueB .and. .not. lValueA)
```

Neste exemplo, a função XOR recebe dois valores booleanos lValueA e lValueB como parâmetros.

Ela retorna o resultado do operador XOR simulado usando expressões condicionais com os operadores AND, OR e NOT. Você pode usar essa função XOR em seu código ADVPL sempre que precisar realizar uma operação lógica XOR entre dois valores booleanos.

**Saiba Mais**

[Operadores AdvPL](https://tdn.totvs.com/display/tec/Operadores+Comuns)
