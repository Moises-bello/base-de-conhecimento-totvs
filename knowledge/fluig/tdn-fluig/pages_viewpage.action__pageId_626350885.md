---
content_hash: e4352bb36abd323bac60b19ac3f0e884947b36c3cf4980134650717b99a68677
fetched_at: '2026-06-28T21:35:28.256392+00:00'
page_id: '626350885'
product: fluig
source: tdn-fluig
title: Ocultar informações no cabeçalho HTTP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=626350885
version: 21
---

4true.\*ndicenone

# Objetivo

---

O objetivo deste guia é alertar quanto ao problema de expor informações nos cabeçalhos HTTP, bem como apresentar o procedimento para ocultar essas informações nos balanceadores de carga homologados para uso no TOTVS Fluig Plataforma.

# Exposição de informações

---

A aplicação retorna informações nos cabeçalhos HTTP que podem ser aproveitadas em tentativas de invasão. Um aspecto importante do desenvolvimento de aplicações seguras é evitar o vazamento de informações: cabeçalhos HTTP podem fornecer a um atacante o conhecimento sobre o funcionamento interno de uma aplicação. 

0.5falsebalanceadoresfadetrue1Apache2Nginx3NLB

 

# Como ocultar as informações

---

Para evitar essa exposição, sugerimos realizar o tratamento de informações de saída. O procedimento para ocultar as informações depende do *load balancer* utilizado no ambiente: Apache, NGINX ou Microsoft NLB.

## Apache

---

Para remover por completo a informação, acompanhe os passos a seguir:

**01.** Instalar o módulo mod- security.

**02.** Adicionar o módulo do Apache.

**03.** Editar o arquivo de configuração de segurança:

**04.** Adicionar a opção:

* SecServerSignature " "

  Nota:

  É possível alterar o conteúdo para qualquer informação. Em vez de adicionar**SecServerSignature " "**, adicionar o texto desejado. Exemplo:

  + SecServerSignature Fluig

  Com isso, a opção Server passa a apresentar:

**05**. Alterar os dois parâmetros para ocultar a informação do **Server**:

* ServerSignature Off
* ServerTokens Prod

**06**. Incluir os dois parâmetros para ocultar a informação do  **X-Powered-By**:

* Header always unset "X-Powered-By"
* Header unset "X-Powered-By"

**07**. Reiniciar o Apache.

Com isso, a opção Server passa a não apresentar nenhuma informação:

## Nginx

---

Importante!

Somente é possível utilizar o Nginx **até a versão** **1.22** por conta da compatibilidade com o módulo nginx-stick-module-ng.

Para remover por completo a informação, acompanhe os passos a seguir:

**01**. Instalar o módulo ngx\_headers\_more. A instalação depende de cada sistema operacional. No Debian basta executar o comando abaixo:

Debian

**02**. Editar o arquivo de configuração onde está configurado o *proxy* reverso e adicionar as opções abaixo na sessão **location**:

**03**. Reiniciar o NGINX.

Esta configuração limpa mais informações do cabeçalho HTTP. Neste caso irá remover as informações **Server** e **X-Powered-By**.

## Microsoft NLB

---

Nesse caso, a solução é um pouco diferente, sendo necessário incluir regras de saída utilizando a reescrita de URL. Acompanhe os passos a seguir:

0.5falseNLBfadetrue0Conceito

Existem várias configurações de balanceamento de carga e *proxy* reverso. Diante disto, será necessário avaliar cada caso para identificar o melhor local para configuração. O ideal é criar a regra no servidor de saída que geralmente será o *proxy* reverso. Caso exista apenas o balanceamento de carga sem o *proxy* reverso, será necessário criar a regra em cada servidor IIS que faz parte do cluster.

Neste caso, deverá ser configurado nos dois servidores, pois não existe um servidor único com *proxy* reverso.

Já neste segundo caso, basta configurar uma regra de saída no servidor *proxy* reverso.

1Passo 1

* Para realizar a configuração, é necessário criar uma regra de saída na opção URL Rewrite do *site*.

2Passo 2

* Visualizar variáveis do servidor:

3Passo 3

 

* Adicionar variável:

4Passo 4

* Adicione a varável **RESPONSE\_SERVER****:**

5Passo 5

* Adicione a variável **RESPONSE\_X-POWERED-BY:**

6Passo 6

* Adicione uma nova regra de saída:

7Passo 7

* Em regras de saída escolha regra em branco:

8Passo 8

* Escolha um nome para a regra, em correspondência escolha a opção **variável** e no nome da varável preencha com **RESPONSE\_SERVER** conforme cadastrado anteriormente.

9Passo 9

* A ação deve ser **reescrita** e o valor deve ser deixado em branco por padrão. Caso escreva algum outro valor, este será apresentado no cabeçalho HTTP.

* Acione **Aplicar**.

10Passo 10

* Para o cabeçalho X-Powered-By deverá seguir os mesmos passos trocando apenas o nome da varável para **RESPONSE\_X-POWERED-BY:**

11Passo 11

* Ao final teremos duas regras de saída:

12Resultado

O resultado esperado aparecerá nos cabeçalhos HTTP:

A regra do cabeçalho **Server** foi criada porque pode ou não aparecer, dependendo da forma que estão configurados os serviços de *proxy* reverso e balanceamento de carga.
