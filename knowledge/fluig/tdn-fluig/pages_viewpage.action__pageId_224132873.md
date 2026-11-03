---
content_hash: 87df9b2309f70ba1e6c8b04788627cccca02909f690094345f44f42300fb7735
fetched_at: '2026-06-28T21:35:19.923013+00:00'
page_id: '224132873'
product: fluig
source: tdn-fluig
title: IDE - Mensagem "Ocorreu um erro ao tentar conectar ao servidor do Identity."
  Como corrigir?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224132873
version: 15
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**TOTVS Fluig Plataforma integrado ao TOTVS Identity

**Versão:** 1.5.5

# Ocorrência

Ao tentar integrar a plataforma ao Identity seguindo a documentação de  e testar a conexão antes de salvar, a plataforma exibe a mensagem "Ocorreu um erro ao tentar conectar ao servidor do Identity. Verifique se as informações estão corretas". Além disso, o log registra a mensagem abaixo:

falseerroImagemLogjava

# Causa

O erro "*Connection timed out*" indica que o tempo de conexão entre a plataforma e o Identity expirou. Isso pode acontecer devido a configuração de *proxy*, por exemplo.

# Solução

Verifique se o servidor da plataforma Fluig utiliza *proxy*. Se utilizar, desabilite o *proxy* e faça um novo teste de conexão. Se conseguir se conectar no Identity e finalizar a integração, uma mensagem de sucesso será exibida. Entre em contato com o administrador da rede para verificar a configuração do *proxy*.
