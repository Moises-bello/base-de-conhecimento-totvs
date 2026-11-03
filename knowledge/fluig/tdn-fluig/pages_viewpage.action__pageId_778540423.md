---
content_hash: 55bffc7fa359aa57b8ef6d11534ad9334b0870a28e051dea250059e5e119d8e9
fetched_at: '2026-06-28T21:35:29.939061+00:00'
page_id: '778540423'
product: fluig
source: tdn-fluig
title: hAPI.getCardValue (nova)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=778540423
version: 9
---

O método **getCardValue** da  retorna o valor de um campo no registro de formulário da solicitação atual.

# Nesta documentação

trueNesta doc.\*nonefalse

# Sintaxe

---

js

# Parâmetros

---

### **fieldname**

Uma string  com o nome do campo de formulário que será lido.

# Valor de retorno

---

Uma nova string contendo o valor do campo. Sempre é retornado uma string, não importando o tipo de campo no formulário

Caso o campo não exista no formulário ou a solicitação não tenha formulário ou esteja sendo executado em um ponto fora dos eventos de processo, será retornado o valor **null**.

# Exemplos de uso

---

## Validar o preenchimento de um campo

xmltrue

Código do usuário\*:    
Nome do usuário\*:
