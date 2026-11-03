---
content_hash: c328616edf3ddf0a74037803861c3ed2d965a68b36343e64b63072dbff466d97
fetched_at: '2026-06-29T00:09:11.356550+00:00'
page_id: '403746926'
product: rm
source: tdn-rm
title: Preferências de Anexos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=403746926
version: 9
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

As preferências de anexos permitem que você configure a exibição dos anexos presentes nas telas .Net (também chamada de Actions). Estas preferências podem desde obrigar a inserção de dados no anexo, durante a inclusão de um registro na tela principal até carregar o anexo prontamente com a visão da tela .Net.

## **02. EXEMPLO DE UTILIZAÇÃO**

Uma vez o anexo definido como um anexo preferencial, ele será apresentado na edição da tela .Net, como se fosse uma pasta.  
Você pode incluir quantos anexos desejar, selecionando qual a tela .Net e os anexos correspondentes. Para todos os tipos de permissões, você poderá controlar os anexos com os parâmetros abaixo:

**Obrigatório:** No momento da inclusão de um novo registro na tela principal, será obrigada a inclusão de pelo menos um registro no anexo escolhido. Se marcado, ele desativará o parâmetro abaixo, "Carregar Automaticamente".

false

**Observação:**  
A inclusão obrigatória de um registro no anexo NÃO valerá para as situações:

* Telas de exibição, ou seja, não são telas de cadastro
* Quando uma tela for Extended Action (veja a explicação no fim da página)

**Carregar Automaticamente:**Carrega automaticamente o anexo escolhido assim que você entrar na tela .NET, como você o tivesse aberto na visão da tela .Net.

## **TELA EXTENDED ACTION**

Extended Action é um anexo que NÃO é exibido como uma pasta, e sim como uma tela adicional que aparecerá sobre a tela .NET.  
Todas as telas Extended Action serão apresentadas como links, listados em uma nova pasta Informações Adicionais, exibida na edição de uma tela .NET. Uma vez clicado no link, a tela Extended Action aparecerá sobre a tela .Net, permitindo suas configurações adicionais.  
   
Oriente-se pelas configurações das permissões:

**Permissões Gerais:**

Todos os anexos aqui incluídos serão visualizados para todos os usuários nas telas .Net. Basta selecionar qual a tela desejada, seu anexo correspondente e parametrizar da maneira desejada.

false

**Observação:**  
As permissões gerais são as últimas a serem consideradas e, portanto as que têm menor prioridade na questão da segurança.

**Permissões por Perfil:**

Os anexos incluídos aqui serão visualizados para os usuários que pertencerem ao perfil definido para as telas .Net. Basta selecionar o perfil desejado, qual a tela e seu anexo correspondente e parametrizar da maneira conveniente.

false

**Observação:**  
As permissões por perfil estão entre as Permissões de Usuário e Permissões Gerais na questão da segurança, onde a primeira tem maior prioridade e a segunda uma prioridade menor.

**Permissões por Usuário:**

Os anexos incluídos aqui serão visualizados para os usuários que pertencerem ao perfil definido para as telas .Net.   
Basta selecionar o perfil desejado, qual a tela e seu anexo correspondente e parametrizar da maneira conveniente.

false

**Observação:**  
As permissões por usuário são as primeiras a serem consideradas e, portanto as que têm maior prioridade na questão da segurança. Se esta permissão de usuário estiver definida para "Carregar Automaticamente" um o anexo em uma tela, e estiver parametrizado nas Permissões Gerais que este mesmo anexo é "Obrigatório", então valerá as configurações definidas em "Permissões de Usuário", ou seja, o anexo será aberto automaticamente.

O mesmo vale para as Permissões por Perfil, que será considerada depois das Permissões por Usuário.

Importante

A partir da versão 12.1.2209 ao marcar o campo "**Obrigatório**", é validado se o tipo de dados dos campos chaves entre as actions Mestre/Detalhe são do mesmo tipo, caso não seja será gerada a mensagem abaixo:

Se após atualizar a versão, aparecer uma mensagem de erro ao abrir a tela de uma action principal, será necessário conferir se a mesma possui um anexo onde os campos das tabelas possuem tipos diferentes, e desmarcar a opção "Obrigatório".

false

**Versão:** 12.01.XX
