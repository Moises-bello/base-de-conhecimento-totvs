---
content_hash: 53caa95d777b592b95ea67e68cc92ab14584249036d7c526cd572886138e90e6
fetched_at: '2026-06-28T21:35:24.016487+00:00'
page_id: '268596664'
product: fluig
source: tdn-fluig
title: ARQ - Por que o erro "Failed to create Solr core" está ocorrendo após utilizar
  a busca da plataforma?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268596664
version: 10
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

# Ocorrência

Por que ao tentar utilizar a busca da barra superior da plataforma aparece o erro abaixo no log?

xmlEclipse1024Arquivo de logtrue
(...)
Caused by: java.lang.IllegalArgumentException: Illegal character in path at index 29: http://172.0.0.1:8080/indexer /admin/cores?action=STATUS&core=1&indexInfo=true&wt=javabin&version=2
(...)
Caused by: java.net.URISyntaxException: Illegal character in path at index 29: http://172.0.0.1:8080/indexer /admin/cores?action=STATUS&core=1&indexInfo=true&wt=javabin&version=2 ]]>

# Causa

Ao cadastrar a URL de acesso ao Solr nos Parâmetros da plataforma (wcmadmin), foi salvo com um caractere espaço ' ' no final (ex.: "http://172.0.0.1:8080/indexer ").

# Solução

Corrigir a **URL de acesso ao Solr**, removendo o espaço ao fim do parâmetro e reinicializar a plataforma a seguir. Para isso, siga os passos a seguir:

0.5falseSamplefadetrue1Passo 1

* Faça login na plataforma com o usuário **wcmadmin**. Lembrando que os clientes Cloud TOTVS deverão abrir um ticket solicitando esta alteração.
* Acesse o menu **Painel de controle** e acione o recurso **Configurações do sistema**.

Em atualizações anteriores à **Liquid - 1.6.5**, esse recurso está localizado na aba **WCM** do **Painel de controle**.

2Passo 2

1. Em **Configurações do Sistema** clique na Aba **Parâmetros da Plataforma**.
2. Verifique se no campo **URL de acesso ao Solr** contém uma caractere espaço no final da URL. Caso tenha, apague o espaço e salve as configurações.
3. Será necessário **reiniciar os serviços do fluig** para salvar a edição.
