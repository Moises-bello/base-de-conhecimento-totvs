---
content_hash: 983759fdfebd01372901064c816e6ce1ccbb445c7ddb1ac41a9e9a8906bcad89
fetched_at: '2026-06-28T21:35:30.421063+00:00'
page_id: '852912430'
product: fluig
source: tdn-fluig
title: Interceptando e personalizando o e-mail padrão (onNotify)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=852912430
version: 2
---

# Índice

true.\*ndicenone

# Introdução

Diversos e-mails são disparados no Fluig, variando de notificações simples a alertas urgentes. O **onNotify** é um  do Fluig que pode ser criado para interceptar notificações padrão do Fluig, permitindo alterações ou a geração de logs.

# Sintaxe

jsEclipse

# Parâmetros

## subject

Uma lista de string que, quando adicionada algum item, modifica o assunto do e-mail para todos os destinatários. Apesar de ser uma lista, apenas o primeiro item da lista será considerado. Então, caso sejam adicionados dois assuntos, somente o primeiro item será usado.

## receivers

Uma lista de Strings com os e-mails dos destinatários. Também é possível adicionar outros e-mails, de usuários do sistema ou mesmo e-mails externos, caso seja necessário notificar uma pessoa que não tenho acesso ao sistema.

## template

Uma String contendo o código do template (ou tipo) de e-mail que está sendo enviado, permitindo que seja alterado apenas um tipo específico de e-mail. É recomendável que sempre seja verificado o código do template, para evitar que ocorram alterações em outros tipos de e-mail, que não necessitariam de personalização. Este parâmetro é fixo e alterações nele não mudaram o tipo de template a ser utilizado.

## params

É um mapa de dados que permite alterar/incluir parâmetros para que sejam apresentados no e-mail. O nome dos parâmetros informados nesse mapa devem ser os mesmos que são utilizados dentro do arquivo de template.

# Exemplos

## Alterando o Assunto quando o e-mail for do tipo "Tarefa sob sua responsabilidade em atraso"

javascriptEclipse1true

## Adicionando um destinatário quando o e-mail for do tipo "Notificação de nova atividade sob sua gerência"

javascriptEclipse1true

## Adicionando um parâmetro o e-mail for do tipo "Solicitação cancelada"

javascriptEclipse1true
