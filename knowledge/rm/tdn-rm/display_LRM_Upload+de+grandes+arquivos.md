---
content_hash: e8a6c16d4aa035760e114f705ec19591ad056205a4dd4fac573961ce2d4563ac
fetched_at: '2026-06-29T00:10:31.281125+00:00'
page_id: '521137961'
product: rm
source: tdn-rm
title: Upload de grandes arquivos
type: documentation
url: https://tdn.totvs.com/display/LRM/Upload+de+grandes+arquivos
version: 3
---

## Problema

Quando o candidato envia pelo portal um arquivo/documento muito grande (geralmente acima de 30 MB), é apresentado a mensagem de erro: "Envio de arquivos erro server side".

## Solução

Este erro ocorre por uma medida de segurança do servidor Web que define o tamanho máximo de uma requisição.

O IIS 10 por exemplo define por padrão 30 MB.

#fffApesar de não recomendado, você pode aumentar o tamanho máximo de requisição que seu servidor Web receberá.

1. No IIS com o FrameHTML selecionado, abra o menu Filtragem de solicitações.
2. De dentro do menu Filtragem de solicitações, selecione nas opções listadas a direita o item Editar configurações de recurso.
3. Na tela que será aberta ao realizar o passo anterior, dentro do agrupamento Limites da Solicitação defina o campo Tamanho máximo de conteúdo permitido (Bytes) com o tamanho máximo que deseja receber requisições.
4. No arquivo web.config que fica localizado dentro da pasta FrameHTML, encontre a tag httpRuntime e adicione o atributo maxRequestLength também com o valor máximo (Bytes) que deseja receber requisições.
   1. Exemplo<httpRuntime targetFramework="4.5" maxRequestLength="204800" />.

Obs. Os passos acima tiveram como base a versão 10 do IIS, pode haver divergência de caminhos e nomeclaturas em versões diferentes.

Importante

Conforme citado anteriormente, a configuração de tamanho máximo de uma requisição é uma medida de segurança para o servidor Web.

Sendo assim, não é recomendado que se permita requisições com tamanho muito grande. Em caso de ataques como por exemplo o de negação de serviço, o envio de requisições grandes facilitaria para pessoas má intecionadas deixando o servidor vulnerável.
