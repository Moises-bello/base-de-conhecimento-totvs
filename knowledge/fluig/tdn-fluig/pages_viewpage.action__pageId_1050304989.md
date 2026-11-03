---
content_hash: e941970a41c138f99f33d756b06b3873bbeceb4b68a6b87b4c278eb80cfedd30
fetched_at: '2026-06-28T21:35:17.367756+00:00'
page_id: '1050304989'
product: fluig
source: tdn-fluig
title: 'Configurações de segurança para prevenção de ataques de força bruta: BFA (Brute
  Force Attack)'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1050304989
version: 2
---

---

Em ambientes corporativos publicados na web, é essencial implementar medidas de proteção contra ataques de força bruta, incluindo variantes sofisticadas como o uso de endereços IP rotativos, ataques do tipo *low and slow* e tentativas de preenchimento de credenciais. Para mitigar esses riscos, recomenda-se a adoção da estratégia de defesa em profundidade, que combina múltiplas camadas de segurança e aumenta a resiliência da aplicação frente a diferentes vetores de ataque.

Nesse contexto, torna-se necessário fortalecer a segurança em todas as camadas envolvidas: Firewall/WAF, proxy reverso e a própria aplicação, essa utilizando o TOTVS Identity, que disponibiliza recursos de autenticação multifator (MFA), ampliando a proteção contra acessos não autorizados.

## Camada de Firewall e WAF (Web Application Firewall)

---

Recomenda-se que a aplicação seja publicada sob de uma camada de **Firewall e/ou Web Application Firewall (WAF)**. Essa camada atua como o primeiro nível de proteção entre a internet e a infraestrutura da aplicação, sendo responsável por filtrar e monitorar o tráfego antes que ele alcance o proxy reverso ou o servidor de aplicação.

O uso dessa camada é uma prática amplamente adotada em aplicações corporativas, pois permite reduzir significativamente a exposição direta da aplicação a tráfego malicioso ou automatizado.

Entre os principais objetivos dessa camada estão:

* **Bloqueio de tráfego malicioso conhecido**, utilizando listas de reputação de IP ou regras de segurança previamente definidas;
* **Mitigação de ataques automatizados**, como tentativas de autenticação em massa *(brute force)* ou varreduras automatizadas;
* **Filtragem de requisições suspeitas**, incluindo padrões de ataque comuns a aplicações web;
* **Limitação de taxa de requisições (rate limiting)** em determinados cenários, reduzindo o impacto de ataques de alta frequência;
* **Registro e monitoramento de eventos de segurança**, permitindo auditoria e identificação de comportamentos anômalos.

Independentemente da tecnologia adotada, recomenda-se que essa camada seja posicionada **antes do proxy reverso e/ou do servidor de aplicação**, de forma a atuar como a primeira barreira de proteção da arquitetura.

## Camada de Proxy Reverso

---

Recomenda-se que a aplicação seja publicada por meio de um [**proxy reverso**](https://tdn.totvs.com/display/fluig/Proxy+reverso), responsável por intermediar a comunicação entre os clientes externos e o servidor de aplicação. Essa camada atua como um ponto adicional de controle e proteção, permitindo aplicar políticas de segurança antes que as requisições sejam encaminhadas ao servidor de aplicação.

A configuração de medidas contra ataques de força bruta dependerá do proxy adotado. Abaixo estão as documentações do NGINX e do Apache HTTP Server, que fornecem orientações e parametrizações para mitigar possíveis ataques.

* [**NGINX – Brute Force Attack Policies**](https://docs.nginx.com/waf/policies/brute-force-attacks)

* [**Apache – Security Tips**](https://httpd.apache.org/docs/2.4/misc/security_tips.html)

## Camada de aplicação

---

Já na camada de aplicação **é recomendada** a utilização do [**TOTVS Identity**](https://tdn.totvs.com/display/fluig/TOTVS+IDENTITY) que possui integração nativa com o **TOTVS Fluig**. Além de centralizar e simplificar a gestão de credenciais, o TOTVS Identity disponibiliza o [**recurso de autenticação multifator (MFA)**](https://tdn.totvs.com/display/fluig/Identity+%7C+Login#Identity%7CLogin-Fazerlogincomautentica%C3%A7%C3%A3omultifator(MFA)), ampliando significativamente a segurança no acesso à plataforma e reduzindo o risco de comprometimento por ataques de força bruta ou uso indevido de credenciais.
