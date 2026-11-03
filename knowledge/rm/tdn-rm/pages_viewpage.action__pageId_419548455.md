---
content_hash: ada2d9dc1ef4c9162cde0dbebc7aeea4aa24f38ee460725f79394df4015beb9b
fetched_at: '2026-06-29T00:09:13.365473+00:00'
page_id: '419548455'
product: rm
source: tdn-rm
title: APIs de Framework - Módulo Serviços Globais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=419548455
version: 44
---

# Sumário

---

Sumário

# 1 - APIs de Framework e swagger

---

      O aplicativo RM.Host é responsável por hospedar e expor os serviços de APIs. Veja mais sobre a .

Abaixo estão listadas as APIs de Framework:

Listagem de APIs pelo Host - Swagger

Através do link [http://{dominio}:{porta}/api/swagger/](http://localhost:8099/api/swagger/) disponibilizado pelo RM.Host.exe, é possível listar todas as api's da linha RM, disponíveis. Nesse endereço é possível visualizar todos os métodos implementados, o formato ao ser utilizado nos dados de entrada, o formato dos dados de saída, entre outras informações sobre as api's desenvolvidas.

### Desabilitar o Swagger

Para desabilitar o acesso ao Swagger pelo link acima, é necessário adicionar a seguinte chave ao <*appSettings>* do *RM.Host.exe.config*:

**<add key="DisableSwagger" value="true" />**

O **FrameHTML** também possui um acesso ao Swagger pela URL [http://{dominio}:{porta}/swagger/](http://localhost:8080/swagger/); para desabilitá-lo, adicione a chave acima ao <*appSettings>* do *Web.config*, localizado na pasta *FrameHTML*.

Importante: Alteração na URL do Swagger

A partir da versão **12.1.2606**, o endereço de acesso ao Swagger mudou.

* **Nova estrutura:** `http://{dominio}:{porta}/swagger/index.html`
* **Exemplo:** `http://localhost:8051/swagger/index.html`

# 2 - Padrões

---

      Na API de Usuário é utilizado dois padrões:

* Guia de API Totvs
* SCIM

# 2.1 - Guia de API Totvs

---

      Este guia define os padrões que **devem** ser adotados durante a implementação de novas APIs publicas ou privadas na plataforma TOTVS incluindo:

* Definir práticas e padrões consistentes para todos os *endpoints* das APIs da TOTVS;
* Garantir a utilização mais próxima possível das boas práticas estipuladas pelos padrões REST/HTTP;
* Tornar os serviços da TOTVS acessíveis através de APIs facilmente compreendidas e documentadas para desenvolvedores e consumidores.

[Mais em "Guia de implementacao das APIs TOTVS"](https://tdn.totvs.com/pages/releaseview.action?pageId=274849083)

# 2.2 - SCIM

---

      O SCIM (*System for Cross-domain Identity Management* ou Sistema de Gerenciamento de Identidade de Domínio Cruzado) é um padrão aberto para automatizar a troca de informações de identidade do usuário entre domínios de identidade e aplicações.

[Mais em "SCIM"](http://www.simplecloud.info/)

# 3 - Métodos

---

      Na API de Usuários estão expostos os métodos:

* GET
* POST
* PUT
* DELETE

## Especificações

| Especificações | Título | Comentário |
| --- | --- | --- |
| [RFC 7231, sessão 4: Request methods](https://tools.ietf.org/html/rfc7231#section-4) | Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content | Especifica os métodos GET, HEAD, POST, PUT, DELETE, CONNECT, OPTIONS, TRACE. |
| [RFC 5789, sessão 2: Patch method](https://tools.ietf.org/html/rfc5789#section-2) | PATCH Method for HTTP | Especifica o método PATCH. |

# 3.1 - GET

---

      O Método GET solicita a representação de um recurso específico. Requisições utilizando o Método GET devem retornar apenas dados.HEAD O Método HEAD solicita uma resposta de forma idêntica ao método GET, porém sem conter o recurso "body"(corpo).

# 3.2 - POST

---

      O Método POST é utilizado para submeter uma entidade a um recurso específico, às vezes causando uma mudança no estado do recurso ou solicitando alterações ao servidor.

# 3.3 - PUT

---

      O Método PUT substitui todas as atuais representações de seu recurso alvo pela carga de dados da requisição.

# 3.4 - DELETE

---

      O Método DELETE remove um recurso específico.

# 4 - Lembretes

---

     Importante: Lembre-se que ao informar valores inteiros para propriedades, eles devem ser informados sem o 0 (zero) à esquerda. Caso seja enviado com o 0 (zero), o valor inteiro deve estar entre aspas duplas:

     Ex.: "day": 8   ou  "day": "08".

     Isso acontece porque ao utilizar um inteiro com um 0 a esquerda o C# entende que este inteiro é base Octal ( de 0 a 7) onde os caracteres 8 e 9 são inválidos.

# 5 - Solicitação usando Filter

---

     A Api tem suporte para realizar pesquisa usando operações básicas de comparação, cada valor deve ser informado como um parâmetro, veja os exemplos abaixo:

* Igual (=)

  pyRDark
* Maior e Menor (> e <)

  pyRDark :ID1 AND CODCOLIGADA < :ID2", 1, 7]]]>
* Contém ( in )  
  Neste exemplo esta sendo utilizado o filtro "**IN**", trazendo todos os registros que tenham o valor IDTURMADISC igual a 845 ou 846 ou 847.

  pyRDark

# 6 - Consumo de Licença pelo License Server

---

Importante

O consumo de Licença foi desativado para as seguintes APIs:

* Coligada
* Usuários
* Perfil
* JobExecution
* JobScheduler
* Parâmetros

A partir das versões e patchs listados abaixo:

* 12.1.2302, patch 121
* 12.1.2209, patch 195
* 12.1.2205, patch 246

Para demais versões anteriores o consumo permanece ativado.

##
