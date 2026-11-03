---
article_id: 34099317388183
category: Inspeção de Entradas (SIGAQIE)
content_hash: 7d1e91c1923ff6a40a7b71da303e8937b0bcee15a23f6a9251d09b321e8065d6
fetched_at: '2026-06-28T22:42:27.084959+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Módulo não está implantado - Erro "Usuário
  Inválido!" ao acessar sessões de Inspeção no App Minha Produção
type: support-article
updated_at: '2026-01-20T20:29:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34099317388183-Manufatura-Linha-Protheus-SIGAQIE-M%C3%B3dulo-n%C3%A3o-est%C3%A1-implantado-Erro-Usu%C3%A1rio-Inv%C3%A1lido-ao-acessar-sess%C3%B5es-de-Inspe%C3%A7%C3%A3o-no-App-Minha-Produ%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34099317358359) Tempo aproximado para leitura: **00:04:43 min**  
  
**Ocorrência**  
Ao tentar acessar, pela primeira vez, a sessão do **Inspeção de Entradas - SIGAQIE** no aplicativo **Minha Produção TOTVS**, é exibida a seguinte mensagem: **Usuário Inválido! Revise o relacionamento deste login no módulo QIE do Protheus**.  
  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Causa**  
Esse erro ocorre quando há **inconsistências** no relacionamento do **login do usuário** com o módulo **SIGAQIE,** quando existem configurações **incorretas da sessão REST** utilizada pelo aplicativo ou quando utilizada a **validação de usuário via integração de AD - Active Directory** (**APP Minha Produção** não tem integração com AD).   
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
**1. Revisar Premissas Básicas**:

Certifique-se de que todos os seguintes requisitos estão atendidos:

* O módulo **SIGAQIE** está corretamente implantado no Protheus;
* A **sessão REST (geralmente [HTTPURI])** está configurada no AppServer.ini, com a **chave PrepareIN=Empresa,Filial**;
* O **login do usuário está vinculado** corretamente a algum cadastro de usuário na empresa e filial definidas no **PrepareIN da sessão REST**;
* O campo **Nível Usr. (QAA\_NIVEL)** está preenchido no cadastro do usuário;
* A sessão de Inspeção de Processos está com o **back-end do Protheus atualizado** e o **dicionário diferencial aplicado**.

**2. Verificar a Opção de Conexão Utilizada pelo Aplicativo**:

**A) Acesso via Mingle**

* Identificar os dados de **Servidor, Porta e Instância (URL da sessão [HTTPURI])** que serão utilizados no ambiente (Desenvolvimento, Homologação ou Produção);
* Abrir chamado com o time **TOTVS Framework Mingle** solicitando a criação de um novo Alias apontando para essas informações.

**Observação:** no contexto do **Mingle, “Instância” e “Endpoint”** referem-se à URL configurada no Alias.

* No app Minha Produção, configurar a conexão via Mingle, utilizando o Alias recém-criado.

**B) Acesso Direto (sem Mingle)**

* Atualizar o **RPO com a última LIB** publicada;
* Configurar a **sessão REST** no **AppServer.ini (geralmente [HTTPURI])** com os parâmetros abaixo:

Stateless=1  
; Realiza o consumo da licença sob demanda

Module=10  
; Indica o uso de licença APP (código 3016)

* No app Minha Produção, utilizar a opção Acesso Direto, informando corretamente a URL, Porta e Instância, conforme configuração do AppServer.ini.

**3. Cuidados Especiais para Clientes TOTVS CLOUD**

* Em ambiente **Cloud**, cada servidor possui um **ID e uma URL de acesso exclusivos**.
* Certifique-se de que o aplicativo está apontando para o **Servidor, Porta e Instância REST corretos** conforme o ambiente (Desenvolvimento, Homologação ou Produção).
* Após a migração entre ambientes, como de Homologação para Produção, é fundamental repetir todas as configurações no novo ambiente. Situações em que configurações são feitas apenas em Homologação e não replicadas na Produção podem causar falhas.

**Após a migração para Produção, siga os passos:**

* Configurar a **sessão REST ([HTTPURI]) no AppServer.ini**, conforme modelo do ambiente anterior;
* Validar se a chave **PrepareIN=Empresa,Filial** está corretamente ajustada;
* Se o acesso for via Mingle, solicitar um novo alias ao time TOTVS Framework Mingle, apontando para o servidor de produção;
* No app, configurar a **conexão via Mingle ou Acesso Direto**, conforme os dados (**Servidor, Porta e Instância**) do ambiente de produção.

**Conclusão**  
A mensagem **"Usuário Inválido!"** está relacionada à correta c**onfiguração da sessão REST no Protheus**, ao vínculo do usuário com o **módulo SIGAQIP** e à forma de conexão utilizada no **aplicativo Minha Produção**.  
Seguir as etapas descritas neste documento garante o funcionamento adequado das sessões de Inspeção no app.

**Documentações relacionadas**

[Tudo sobre configuração - Guia de Uso - Aplicativo Minha Produção](https://tdn.totvs.com/pages/releaseview.action?pageId=606095034#tudo-sobre-Configuracao)  
[Guia de Uso - Aplicativo Minha Produção - Funcionalidades Inspeção da Qualidade Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=606095034#tudo-sobre-inspecao_de_processos-protheus)  
[Pacotes - APP Inspeção de Entradas P12](https://tdn.totvs.com/pages/releaseview.action?pageId=904036510%20)
