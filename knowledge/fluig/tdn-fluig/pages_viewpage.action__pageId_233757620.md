---
content_hash: cb6bdf6f2ab7cf6071faeb34688aeb528e3dfa8462a8c94051f782cac6984e7c
fetched_at: '2026-06-28T21:35:20.050083+00:00'
page_id: '233757620'
product: fluig
source: tdn-fluig
title: ARQ - Como alterar o endereço do servidor de licenças?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=233757620
version: 10
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

**Versão:** 1.5.6 ou superior

# Ocorrência

Realizamos a instalação da plataforma e após iniciar os serviços e tentar acessar com o usuário wcmadmin, está ocorrendo o erro: ERROR: 4012. Como faço para alterar o endereço do servidor de licenças?

**Figura 1 - Mensagem apresentada na versão 1.6.0 e anteriores**

**Figura 2 - Mensagem apresentada na versão 1.6.1 e superiores**

# Causa

Esta mensagem de erro é exibida quando a plataforma não consegue localizar o slot 4012 no servidor de licenças que foi configurado na instalação.

# Solução

1. Execute os passos da página  Se os procedimentos realizados não corrigirem a inconsistência de endereço, siga os passos abaixo.  
   1. Neste caso, será necessário acessar o diretório [diretório\_instalação]\repository\wcmdir\config e verificar se existe o arquivo **configuration.properties**.
   2. Se existir, abra o mesmo com um editor de textos e localize os parâmetros webdesk/LSHost e webdesk/LSPort, verifique se os valores atribuídos estão corretos.
   3. Caso o arquivo não exista, será necessário criá-lo manualmente. Crie um arquivo com o nome configuration e salve com a extensão .properties
   4. Em seguida, abra o mesmo com um editor de textos e adicione as seguintes linhas:

javaconfiguration.properties
webdesk/LSPort=]]>

Por exemplo, se o endereço do servidor de licenças fosse 172.168.0.1 e a porta 5555, o arquivo ficaria da seguinte forma:

javaconfiguration.properties

Em seguida, será preciso reiniciar os serviços do Fluig. Não se preocupe se o arquivo for deletado, pois a plataforma faz a leitura do mesmo, atualiza a tabela fdn\_paramgeral e em seguida, remove o arquivo automaticamente.
