---
content_hash: fe4f436d76c5017009d366eb850ee02b2060d4ad447d4ce5fda350f5e970ae32
fetched_at: '2026-06-29T00:05:56.024560+00:00'
page_id: '149881272'
product: rm
source: tdn-rm
title: Utilizando a atividade "Aplicar Expressão Regular"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=149881272
version: 3
---

# Sumário

---

Sumário

# Objetivo

---

     Esse documento tem por objetivo demonstrar como utilizar atividade de expressão regular.

# Introdução

---

A finalidade da atividade "**Executar Expressão Regular**" é executar a partir de uma entrada de dados, a validação da Máscara definida, a fim de se obter o retorno se a entrada de dados esta conforme a máscara esperada.       
  
**Inserir atividade "Aplicar Expressão Regular"**

* A propriedade "CaseSensitive" serve para definir maiúsculas e minúsculas são tratadas como caracteres diferentes.
* A propriedade "Entrada" refere ao dado String para ser realizada a validação.
* A propriedade "Mascara" diz a respeito mascara a ser verificada pela atividade.
* A propriedade "Valido" determina se o valor inicial da atividade estará como (True/False).

Para o exemplo de utilização, realizaremos a validação de um E-mail, para verificar se ele esta conforme a Máscara determinada.

**Case Sensitive:** será False para esta validação.  
**Como entrada de dados, será utilizado o seguinte e-mail abaixo:** [Teste@totvs.com.br](mailto:Teste@totvs.com.br)  
**Utilizaremos a seguinte Máscara, que valida se um e-mail é valido:** ^([a-zA-Z0-9\_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})$  
**Valido:** Será iniciado já como False, para caso esteja correto o altere para True.  
  
  
  
Agora utilizemos a atividade de**"Expressão"** para obter o retorno da propriedade **"Valido"** da atividade de **"Expressão Regular"** em seu valor calculado, da seguinte forma:  
  
  
  
Agora para obter visualmente este retorno, utilizaremos a atividade de **"Gerar Exceção" para retornar a "Expressão".**

Agora ao **"Salvar e Executar"** a Fórmula Visual, conseguimos obter o retorno se o dado de Entrada esta conforme a Máscara esperada **(True)**:  
  
  
  
Ao preencher novamente um E-mail incorretamente (Teste@AAAA), para a validação ser realizada, se obtém o seguinte retorno **(False)**:  
  
  
  
Lembrando que a configuração da Máscara deve estar correta, para que a validação de dados seja realizada corretamente.   
  
Segue abaixo documentação oficial da Microsoft com a linguagem de expressão regular:  
**[Linguagem de expressões regulares - Microsoft](https://learn.microsoft.com/pt-br/dotnet/standard/base-types/regular-expression-language-quick-reference)**
