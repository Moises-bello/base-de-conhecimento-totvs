---
content_hash: cf0f17b4d4917f90d602b4edf0fc5f401bc50654912015538cc67f2eb38c9db4
fetched_at: '2026-06-28T21:35:23.176697+00:00'
page_id: '244425259'
product: fluig
source: tdn-fluig
title: BPM 057 - Como solucionar o erro SocketTimeOutException ao exportar processos
  pelo fluig Studio?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244425259
version: 6
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig Studio

**Versão:** 1.5.9 ou anterior

# Ocorrência

Ao tentar exportar um processo ou formulário para o servidor fluig através do plugin fluig Studio, é exibido o erro SocketTimeOutException.

# Causa

Este problema costuma ocorrer devido a problemas na rede do servidor ou configuração de proxy.

# Solução

Primeiramente, verifique as configurações de *proxy* definidas no TDS/Eclipse através do procedimento descrito em .

Caso o problema persista, atualize o servidor fluig e o *plugin* fluig Studio para a .

Esta atualização conta com uma nova opção nas configurações do *plugin* para definir o **Tempo de espera de retorno do servidor (segundos)**, conforme a imagem abaixo:

Acesse o menu ***Window*** → ***Preferences*** → **Fluig** para visualizar a tela de configuração

Para evitar que problemas de intermitência ou lentidão na rede causem problemas no procedimento de exportação, aumente o tempo de espera de retorno do servidor e realize um novo teste.
