---
content_hash: bea1aaa6d896150d258009fba6acb8cbd03c2188b93712249af910cce16daf4f
fetched_at: '2026-06-28T21:35:30.426298+00:00'
page_id: '852915615'
product: fluig
source: tdn-fluig
title: Envio de e-mails personalizados (notifier.notify)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=852915615
version: 5
---

# Índice

true.\*ndicenone

# Introdução

Além dos diversos e-mails são disparados no Fluig, você pode  e envia-los através dos scripts de personalização pelo método **notifier.notify**

Para estes e-mails funcionarem, é necessário que tenha sido feita a [configuração de envio de e-mail](http://tdn.totvs.com/x/CAZbDw).

# Sintaxe

jsEclipse

# Parâmetros

## sender

Uma string contendo a matrícula (código do usuário) do usuário que será usado como remetente do e-mail caso não tenha sido configurado o remetente padrão na configuração de e-mail. Caso tenha sido configurado o remetente padrão, essa parâmetro será ignorado.

## cardId

O código do registro de formulário vinculado à este e-mail. Informar o código do formulário adiciona alguns parâmetros adicionais que podem ser usados nos templates de e-mail:

| Parâmetro | Descrição |
| --- | --- |
| WDK\_CardContent | Conteúdo HTML do formulário (simula a visualização) |
| WDK\_DocumentAuthor | Nome do Autor |
| WDK\_DocumentComments | Comentário adicional |
| WDK\_DocumentDescription | Descrição do formulário |
| WDK\_DocumentIconImage | Imagem do ícone do formulário |
| WDK\_DocumentNumber | Número do formulário |
| WDK\_DocumentUpdatedDate | Data de atualização do formulário |
| WDK\_DocumentVersion | Versão do formulário |
| WDK\_DocumentViewLink | Link para acesso ao formulário |

## template

Uma string informando o código do template de e-mail que está sendo enviado. É o código usado no cadastro de template de e-mail.

## params

É um mapa de dados que permite incluir parâmetros para que sejam apresentados no e-mail. O nome dos parâmetros informados nesse mapa devem ser os mesmos que são utilizados dentro do arquivo de template.

Além dos parâmetros de uso no template, também pode ser adicionado a chave "subject" que será usado como assunto do e-mail. Caso não seja informado nada, o assunto do e-mail será "Fluig"

Por padrão, são adicionados dois parâmetros em todas as notificações e eles podem ser usados no template de e-mail:

| Parâmetro | Descrição |
| --- | --- |
| WDK\_VirtualDir | Diretório Virtual |
| WDK\_AdviceUser | Nome do colaborador remetente |

## receivers

Uma lista de strings com os códigos dos usuários para quem o e-mail será enviado ou os e-mails dos destinatários. Essa lista pode conter códigos de usuários e e-mails externos simultaneamente.

## mimeType

Uma string que especifica o tipo de mídia do conteúdo do e-mail. Normalmente, usa-se "text/html" mas existe também a opção "text/plain".

# Exemplos

## Envio de e-mail configurando alguns parâmetros

javascriptEclipse1true

## Envio de e-mail informando um formulário

javascriptEclipse1true

# Pontos de atenção

## Envio de mensagens para e-mails externos

Para que o envio de e-mails externos seja concluído corretamente o servidor SMTP responsável deve estar habilitado para enviar e-mails para fora da intranet do seu servidor.

## Envio de dados de um formulário via solicitação

Pode-se usam os eventos de personalização do processo para envio de e-mails.

Porém, quando tenta enviar os dados de um formulário na primeira atividade do processo, você deve chamar a notificação no método beforeStateEntry ou afterStateEntry. Caso contrário, com o formulário ainda não foi criado na tabela de dados, esse envio não irá funcionar.
