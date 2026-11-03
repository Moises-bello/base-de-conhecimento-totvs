---
content_hash: 0db540b8846155273e7667caf80b494d4ab567b3bd21ec01077909f31a714884
fetched_at: '2026-06-28T21:35:16.843548+00:00'
page_id: '1003463739'
product: fluig
source: tdn-fluig
title: Lidando com numéricos (int) no Rhino
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1003463739
version: 2
---

---

false

Esta página não tem como objetivo ser um guia de como programar com Rhino ou mesmo como um "aprenda a programar", mas sim para listar algumas características interessantes que serão referenciadas em outros pontos da documentação. Se você ainda não tem experiência com o desenvolvimento no Rhino, recomendamos que deixe essa documentação para o futuro.

Em vários momentos da personalização lidamos com variáveis numéricas o que chamamos de **int**, ou **integer**.

No , assim como em qualquer motor javascript, as variáveis numéricas são **double** (ou seja, aceitam casas decimais). Quando um método ou objeto está explícito que o objeto esperado é um int o próprio Rhino faz a conversão, mas quando o objeto esperado é genérico (Object por exemplo) o objeto usado é um Double. Isso é normalmente transparente para o usuário e não tem impacto, mas podem acontecer alguns estranhamentos principalmente em logs.

# Exemplos de logs

jstrue
