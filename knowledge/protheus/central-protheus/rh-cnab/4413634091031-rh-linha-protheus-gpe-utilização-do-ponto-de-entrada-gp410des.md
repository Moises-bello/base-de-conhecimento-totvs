---
article_id: 4413634091031
category: RH - CNAB
content_hash: a85504eb0d6e669fcd221a4b35580729d0b28e0a1b62b62b4657a2c584054cc7
fetched_at: '2026-06-28T22:43:39.353852+00:00'
product: protheus
section_id: 360004833653
source: central-protheus
title: RH - Linha Protheus - GPE - Utilização do Ponto de Entrada GP410DES
type: support-article
updated_at: '2025-06-17T19:03:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413634091031-RH-Linha-Protheus-GPE-Utiliza%C3%A7%C3%A3o-do-Ponto-de-Entrada-GP410DES
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32878793201431) Tempo aproximado para leitura: **01:00:00 min** **Dúvida**Utilização do Ponto de Entrada **GP410DES .**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.

**Solução**Ponto-de-Entrada: **GP410DES - Líquido de Funcionários.**

**Descrição:**

Geração de Líquido de funcionários. Este ponto de entrada esta localizado após consistência de funcionários. Caso o Rdmake retorne falso (.F.) o funcionário posicionado será desprezado.

**Programa Fonte**

```
GPEM410.PRX
```

**Sintaxe**

GP410DES - Líquido de Funcionários ( ) --> URET

Retorno

**URET**(logico)  
          .T. ou .F. (Verdadeiro ou Falso).

**Saiba Mais**

[Artigos CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833653-RH-CNAB)
