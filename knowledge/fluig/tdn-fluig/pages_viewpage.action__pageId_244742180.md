---
content_hash: 833dfe7cab2287c5de2ea9ef5f94504a0858a16beaea854b0ad248ea52bde25d
fetched_at: '2026-06-28T21:35:23.336004+00:00'
page_id: '244742180'
product: fluig
source: tdn-fluig
title: BPM 085 - Como solucionar o erro gerado ao exportar projetos do Studio para
  fluig integrado com Identity?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244742180
version: 16
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig Studio + fluig Identity

# Ocorrência

ocorrenciaslideOcorrência 1

* Ao efetuar a exportação de um projeto para o fluig que se encontra integrado ao Identity é exibida a mensagem de erro abaixo impedindo que a exportação seja concluída.

* Já no ss\_service.log do SmartSync é exibida a mensagem de que a autenticação ocorreu com sucesso.

Ocorrência 2  

* Ao exportar um processo para o fluig é exibido o erro 'Read timed out':

# Causa

Quando um projeto é exportado do Studio para o fluig integrado com o Identity, o usuário cadastrado na conexão com o servidor sofre uma série de tentativas de autenticação com a senha do AD.

No SmartSync, é exibido que a autenticação ocorre com êxito, isto se deve porque apenas uma autenticação, de uma sequência, é realizada não efetuando as demais tentativas e assim o fluig Studio exibe o erro apresentado acima.

# Solução

Para que este erro não ocorra, deve-se configurar a conexão do Studio com o servidor do fluig e senha pessoal do Identity, assim a autenticação não precisará passar pelo AD, melhorando a performance e evitando erros de autenticação.

Caso a senha pessoal tenha sido desabilitada pelo(s) administrador(es) da empresa no fluig Identity, é possível aumentar o tempo de espera de retorno do servidor (*timeout*) nas configurações do plugin fluig Studio, conforme demonstrado . O tempo de espera padrão é de 10 segundos, mas esse valor pode ser incrementado conforme a necessidade da rede do cliente.
