---
content_hash: 37627c7ff07a1ef5d9efa2cf6b23c4a51126217450dce4aada9bfe0776b3aed2
fetched_at: '2026-06-29T00:11:23.023504+00:00'
page_id: '706142061'
product: rm
source: tdn-rm
title: Configuração do Smart View para integrar ao RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=706142061
version: 24
---

# Introdução

---

O objetivo dessa página é mostrar como configurar o **Smart View** para integrar com o RM.

A instalação do Smart View é demonstrada na página .

A integração com o Smart View está disponível no RM à partir da versão **12.1.2302.**

# Configurando o RM

---

Em ambientes do RM que **NÃO** são **MULTI-TENANT**, para permitir a integração com o Smart View é necessário configurar o Alias padrão conforme detalhado em .

Em ambientes **MULTI-TENANT** não é necessário nenhuma configuração adicional no RM.

O Smart View ainda **NÃO** disponibiliza uma integração **MULTI-TENANT**.

# Configurando o Agent

---

Após instalar o **Smart View**, o primeiro passo é configurar o sistema via Agent, conforme detalhado em .

Para integração com o RM, na etapa de configuração do **Provedor de Segurança**, os campos devem ser preenchidos conforme abaixo:

Provedor de SegurançatrueDescoberta AutomáticaDescoberta Automática

Utilizando a Descoberta Automática, a configuração deve ser feita conforme demonstrado abaixo:

| **Campo** | **Valor** |
| --- | --- |
| **Nome do provedor** | Nome a ser exibido no Smart View. (Ex.: CorporeRM) |
| **Endereço de descoberta** | http://{**endereçoHost**}:{**portaApi**}/api/.well-known/treports/security |

Em **Recuperar emissor**deve ser preenchido um usuário e senha cadastro no RM que servirá como **administrador** do Smart View.

Abaixo um exemplo de configuração do **Provedor de Segurança**onde o RM.Host está sendo executado no endereço 192.168.15.15 e a porta de Api é 8051:

Descoberta ManualDescoberta Manual

Devido à incompatibilidades de compartilhamento de recursos e validação de permissões do Smart View com o RM em relação à **Descoberta Manual**, essa foi descontinuada em integrações com o RM e não é recomendado fazê-la. Caso seu **Smart View** já esteja configurado para uso de **Descoberta Manual**, recomendamos atualizar suas informações de provedor de segurança para o uso da **Descoberta Automática.**

As demais etapas devem ser configurados conforme orientações em .

Concluídas as configurações do Agent, será possível acessar o **Smart View** utilizando os usuários cadastrados no RM.

  

# Configurando o Conector via Provedor Nativo do RM

---

Para concluir a integração com o RM, é necessário cadastrar o Conector para ter acesso aos Objetos de Negócio. Essa configuração é detalhada em . Essa configuração deve ser realizada pelo usuário administrador do Smart View, que corresponde ao mesmo usuário utilizado para recuperar o emissor na configuração do Agent.

Em Conectores, deve ser adicionado um conector do tipo Provedor Nativo apontando para o endereço:

* http://{**endereçoHost**}:{**portaApi**}/api/.well-known/treports/connector
* **Exemplo:** http://localhost:8051/api/.well-known/treports/connector

Seguindo o mesmo exemplo da etapa anterior, onde o RM.Host está sendo executado no endereço 192.168.0.50 e a porta de Api é 8051, a configuração seria:

Após validar a conexão via **Testar Conexão** e Salvar o conector, os Objetos de Negócios ficarão disponíveis para os usuários no Smart View, respeitando as políticas de segurança definidas para cada um.

Índicefalsefalse

**Produto:** Framework

false

**Versão:** 12.1.2302

false

**Processo:** Integração com o

falsefalseStatus

GreenCONCLUÍDO

falseAutores
