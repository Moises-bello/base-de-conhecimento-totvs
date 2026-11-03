---
content_hash: abbbe89882b6e812bff5cd301171fa794f8f16e1c6eff0991f826d58dac0830b
fetched_at: '2026-06-28T21:35:22.242302+00:00'
page_id: '235327464'
product: fluig
source: tdn-fluig
title: Configuração do Fluig Viewer
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235327464
version: 42
---

# Índice

objetivo

# Objetivo

---

O objetivo deste guia é demonstrar a configuração do TOTVS Fluig Plataforma para utilização do Fluig Viewer como visualizador interno.

precondicao

# Precondição

---

O servidor onde está instalado o TOTVS Fluig Plataforma deve ter acesso externo liberado, pois o visualizador deve acessar a URL [https://api.accusoft.com.br](http://api.accusoft.com.br). Portanto, devem ser feitos os devidos ajustes de rede para que seja possível que a plataforma acesse esse endereço.

Em casos onde existe um DNS na plataforma, recomendamos que a configuração seja feita seguindo a documentação [Considerações de DNS para a plataforma](http://tdn.totvs.com/pages/viewpage.action?pageId=213980466). Também é necessário configurar o proxy reverso de acordo com a documentação [Configuração de Proxy Reverso](http://tdn.totvs.com/pages/viewpage.action?pageId=257623455).

Importante

As URLs **[https://api.accusoft.com](https://api.accusoft.com/)** e **[http://api.accusoft.com.br](http://api.accusoft.com.br/)** foram descontinuadas.

Em versões anteriores a 1.6.0, o TOTVS Fluig Plataforma utiliza uma JDK anterior ao JDK 8 e por conta disso, não utiliza o TLSv1.2. Onde o Fluig Viewer não funcionará corretamente, para esses casos será necessário atualizar o TOTVS Fluig Plataforma para a versão mais recente.

oculto

Essas configurações estão duplicadas no artigo <https://centraldeatendimento.fluig.com/hc/pt-br/articles/360033257094> (Mensagem Connection failed and the session will be stopped)

Caso houver alteração aqui, lembrar de alterar esse artigo.

habilitando

# Habilitando o Fluig Viewer no TOTVS Fluig Plataforma

---

falsecloud viewerPasso 1

* Acesse a plataforma com o usuário **wcmadmin**.

Passo 2

* Acesse o **Painel de Controle** > **WCM** > **Empresas**.

Passo 3

* Edite o cadastro da sua empresa.

Passo 4

* Clique em **Cadastrar dados adicionais**.

Passo 5  

* Procure pelo parâmetro **internalVisualizerServer**.
  + Se ele existir, remova-o e cadastre-o novamente informando [https://api.accusoft.com.br](http://api.accusoft.com.br) no campo Valor.
  + Se ele não existir, cadastre-o com o valor citado.

* Procure pelo parâmetro **oldViewer**.
  + Se ele não existir não é necessário cadastrá-lo.
  + Se ele existir, remova-o.

* Salve as alterações na tela Dados adicionais.

* Salve as alterações na tela de cadastro da empresa.

proxy

# Por que configurar o proxy reverso?

---

O proxy reverso é um procedimento que padroniza as configurações de direcionamento da URL do TOTVS Fluig Plataforma. Para saber como configurá-lo acesse [Configuração de Proxy Reverso](http://tdn.totvs.com/pages/viewpage.action?pageId=257623455).

Geralmente quando o TOTVS Fluig Plataforma é instalado o endereço IP do servidor é utilizado (por exemplo, 172.188.95:8080). Porém, depois de algum tempo é muito comum que seja feito o redirecionamento desse endereço para um endereço nominal, como por exemplo, [fluig.totvs.com.br](http://fluig.totvs.com.br).

Como esse redirecionamento pode ser feito de várias formas - via switch, host do servidor, proxy - a configuração de proxy reverso padroniza a forma de redirecionamento da URL, pois nele é configurado o nome do servidor e o endereço externo.

A configuração de proxy reverso é indicada nos casos onde a plataforma não reconhece o endereço externo como se fosse seu endereço.

Um caso muito comum é quando os documentos não são visualizados pela plataforma, apresentando a mensagem "Erro ao gerar a visualização do arquivo. Caso possua permissão, utilize a opção de download do documento" em tela (figura 1). Além dessa mensagem, o arquivo de log também registra a seguinte informação:

**Figura 1 - Mensagem de erro ao visualizar documento**

O que acontece nesse caso é que o visualizador monta uma URL de stream do documento. O endereço dessa URL é o endereço de acesso - no caso, fluig.totvs.com.br:8080/stream/document...". O servidor recebe esse endereço e não o reconhece, pois para ele o endereço correto é 172.188.95. A configuração de proxy reverso faz com que o servidor entenda aquele prefixo na URL de stream como se fosse seu próprio endereço e permite a visualização dos documentos.

$("b:contains('oculto')").parent().parent().hide();
]]>
