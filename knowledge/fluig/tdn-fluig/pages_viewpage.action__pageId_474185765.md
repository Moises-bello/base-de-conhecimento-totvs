---
content_hash: e7a19d08f1ca27a11b5b59e06a7a3b1aae6490e69873ec6bc118375e6ad720db
fetched_at: '2026-06-28T21:35:27.087680+00:00'
page_id: '474185765'
product: fluig
source: tdn-fluig
title: ARQ - Mensagem de erro após o login
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=474185765
version: 5
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** Fluig

**Versão:** 1.6.5 e superiores

# Ocorrência

Após efetuar o *login* é exibida a seguinte mensagem ao invés da página inicial: *{"code":"Internal Server Error","success":false,"message":"java.lang.NullPointerException"}*.

No *log* é possível detectar a seguinte mensagem:

java

# Causa

O módulo de *login* não está configurado corretamente, pois o parâmetro **principalClass** não está presente.

# Solução

falseVersão1A partir da 2.0

Edite o arquivo **standalone.xml**, na seção onde são declarados os módulos de *login*, customizados ou padrão e verifique se a propriedade **principalClass** está presente:

java
...
...
]]>21.6.5 até 1.8.2

Edite o arquivo **domain.xml**, na seção onde são declarados os módulos de *login*, customizados ou padrão e verifique se a propriedade **principalClass** está presente:

java
...
...
]]>
