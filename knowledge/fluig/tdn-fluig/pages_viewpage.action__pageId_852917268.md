---
content_hash: ddb7f7eed3c7ce9dc83e4a1c9e022f0679ba418eb72d41c6f9f7ac45254987eb
fetched_at: '2026-06-28T21:35:30.430040+00:00'
page_id: '852917268'
product: fluig
source: tdn-fluig
title: Criação de templates de e-mail
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=852917268
version: 1
---

# Índice

true.\*ndicenone

# Introdução

O Fluig permite você  e envia-los através dos scripts de personalização pelo método .

Está documentação vai ensinar você como adicionar os seus parâmetros no template e como criar templates complexos de envio de e-mail.

# Template

Para a criação de templates de e-mails no TOTVS Fluig, utilizamos a linguagem de templates Freemarker. Ele permite a inserção de lógica em templates HTML, proporcionando uma grande flexibilidade na customização de e-mails. Com isso, você pode utilizar:

* **Variáveis**: Inserção de valores dinâmicos no conteúdo do e-mail.
* **Condicionais**: Criação de diferentes partes do template com base em condições específicas.
* **Loops**: Iteração sobre listas para gerar conteúdo repetitivo dinamicamente.

O Fluig 1.8.1 utiliza a versão 2.3.28 Freemarker.

# Exemplos de Template

## E-mail simples com uso de dois parâmetros, conforme

xml${descricao}.
Atenciosamente,
Equipe TOTVS
]]>

## E-mail simples com dados do formulário

xml- **Autor:** ${WDK\_DocumentAuthor}
- **Descrição:** ${WDK\_DocumentDescription}
- **Número do Formulário:** ${WDK\_DocumentNumber}
- **Data de Atualização:** ${WDK\_DocumentUpdatedDate}
- **Versão:** ${WDK\_DocumentVersion}
- **Acesse o Formulário:** [Clique aqui](${WDK_DocumentViewLink})
Atenciosamente,
Equipe TOTVS  ]]>

## Criando um e-mail sobre aprovação do pedido com comportamentos diferentes caso seja aprovado ou reprovado

xml
Seu pedido foi aprovado!
<#else>
Infelizmente seu pedido foi reprovado.
<#if observacao??>

Observação: ${observacao}

Atenciosamente,
Equipe TOTVS
]]>

## Utilizando um parâmetro que é uma lista de tarefas

xml
Você tem as seguintes tarefas pendentes:

<#list tarefas as tarefa>* ${tarefa}

<#else>
Você não tem tarefas pendentes.
Atenciosamente,
Equipe TOTVS]]>
