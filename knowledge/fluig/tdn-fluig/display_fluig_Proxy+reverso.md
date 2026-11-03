---
content_hash: 31c6d1fa72e11a51ddf654aa07ef8861be95358e0cca169a295d53fe373bf833
fetched_at: '2026-06-28T21:35:23.644852+00:00'
page_id: '257623455'
product: fluig
source: tdn-fluig
title: Proxy reverso
type: documentation
url: https://tdn.totvs.com/display/fluig/Proxy+reverso
version: 45
---

Nota:

Esta página foi revisada para considerar as configurações de *server* do TOTVS Fluig Plataforma a partir da atualização 1.6.

4.\*ndice

# Objetivo

---

O objetivo deste guia é descrever os procedimentos para a configuração de um servidor de *proxy* reverso em uma instalação da plataforma.

Dicas

Após a configuração do *proxy* reverso, não esqueça de alterar a URL de acesso ao portal nas Configurações do sistema da plataforma. [Clique aqui](http://tdn.totvs.com/x/EO4KDg) e saiba como fazer.

Importante!

Salientamos que, ao utilizar um *proxy* reverso, uma prática de segurança recomendada para a plataforma é não expor o servidor de aplicação diretamente na Internet.

e veja outras boas práticas de segurança recomendadas para o seu ambiente.

# Visão geral

---

Um *proxy* reverso é um servidor que repassa o tráfego de rede recebido para um ou mais servidores. Ele fica na frente dos servidores Web e encaminha as solicitações do cliente – o navegador Web, por exemplo – para esses servidores Web, agindo como uma camada de controle, ajudando a aumentar a segurança, a confiabilidade e o desempenho.

Em uma instalação da plataforma, este tipo de servidor é usado para habilitar uma topologia de arquitetura chamada [DMZ](http://tdn.totvs.com/display/fluig/Topologia+DMZ).

# Funcionamento

---

O *proxy* reverso intercepta as solicitações dos clientes antes que elas cheguem aos servidores Web. Isso permite aplicar balanceamento de carga – um dos seus usos mais comuns – como também cache de conteúdo, criptografia SSL, compressão de dados, além de permitir aumentar a segurança das aplicações Web e a proteção contra ataques.

Dessa forma, o *proxy* reverso garante que nenhum cliente se comunique diretamente com os servidores Web.

# Por que utilizar um *proxy* reverso?

---

Alguns dos benefícios obtidos ao utilizar um *proxy* reverso são:

* melhora no desempenho de aplicações Web, diminuindo o tempo de resposta e otimizando o processamento, pois ele facilita o balanceamento de carga e o cache de conteúdo;

* aumento da confiabilidade e da segurança contra ataques, visto que ele permite proteger os servidores implementando várias medidas de segurança e proteção;

* facilidade na aplicação de políticas de segurança, de autenticação e de autorização, por permitir centralizar o controle de tráfego;

* redução da carga de trabalho dos servidores *back-end*, pois ele gerencia a criptografia e a descriptografia do tráfego SSL.

# Configuração de *proxy* reverso / DMZ

---

No exemplo abaixo, a implementação da DMZ na plataforma foi realizada com o uso do Apache™ HTTP *Server*, que é um servidor *Web* de código livre, desenvolvido e mantido pela Apache *Software Foundation*.

A figura a seguir apresenta as topologias DMZ + SSL suportadas pela plataforma TOTVS Fluig.

Nota:

Destacamos que a topologia considerada ideal e recomendada é a número **2**: **(DMZ + SSL) → Fluig**.

Importante!

Não é possível utilizar as notificações em tempo real quando utilizado *proxy* reverso com HTTPS.

Se o seu ambiente utiliza HTTPS e , a [configuração de HTTPS](https://tdn.totvs.com/pages/viewpage.action?pageId=354472893#Configura%C3%A7%C3%A3oHTTPSdaplataforma-Configura%C3%A7%C3%A3odeHTTPSmanual) deve ser replicada manualmente para todos os servidores do Fluig.

## *Proxy* reverso com Apache

---

Consulte os procedimentos para a configuração e alguns exemplos em Configuração de *proxy* reverso Apache.

## *Proxy* reverso com NGINX

---

Consulte os procedimentos para a configuração e alguns exemplos em Configuração de *proxy* reverso NGINX com HTTPS.

Importante!

Somente é possível utilizar o NGINX **até a versão** **1.22** por conta da compatibilidade com o módulo nginx-stick-module-ng.

## *Proxy* reverso com NLB ou Big IP

---

Para configurar *proxy* reverso utilizando o NLB, Big IP ou outros servidores homologados na nossa , consulte a documentação dos próprios fornecedores ou fabricantes.

Mas, é importante se atentar à prevenção de vulnerabilidades, para que informações não fiquem expostas no cabeçalho HTTP. [Clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=626350885) e saiba como ocultá-las no NLB.

## Gerenciamento de vazão e restrição de acessos (Rate Limit)

---

Implementação de controles de admissão para assegurar a estabilidade da infraestrutura, prevenindo a exaustão de recursos por requisições automatizadas ou volumétricas de uma mesma origem.

**Proteção de Camada de Aplicação no Apache (mod\_evasive)**

Configuração de limites de frequência por objeto e por site, utilizando tabelas de hash em memória para detecção e bloqueio temporário (HTTP 403) de IPs com comportamento anômalo.

Saiba mais

Confira as instruções detalhadas para configurar o **Rate Limit** de requisições no Apache **[aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=877162376#Configura%C3%A7%C3%A3odeproxyreversoApache-ConfigurarRateLimitderequisi%C3%A7%C3%B5es)**.

**Controle de Fluxo e Escalonamento no NGINX (limit\_req)**

Utilização do algoritmo *leaky bucket* para padronizar a taxa de processamento de requisições, permitindo a gestão de picos de tráfego (burst) e respostas semânticas personalizadas (HTTP 429).

Saiba mais

Confira as instruções detalhadas para configurar o **Rate Limit** de requisições no NGINX **[aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=736971727#Configura%C3%A7%C3%A3odeproxyreversoNGINXcomHTTPS-Funcionamentodocontroledetaxa(RateLimit))**.
