---
content_hash: 0976296642027294745ad6fa3d5e002c3a6869f6638eed953bafe864c9a10257
fetched_at: '2026-06-29T00:11:28.324703+00:00'
page_id: '73074650'
product: rm
source: tdn-rm
title: Configuração Exchange - Relay
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=73074650
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Envio de E-mail                     **Versão:**11.00 |
| **Processo** | **:** | E-mail |
| **Subprocesso** | **:** | Configuração Exchange - Relay |
| **Data da publicação** | **:** | 26/07/2013 |

**As** **configurações** **de** **"Relaying"** **no** **Exchange** **deverão** **permitir** **que** **usuários** **anônimos "não** **autenticados"** **tenham** **permissão** **de** **envio** **de** **mensagens** **para** **outros** **domínios.** **As telas** **abaixo** **são** **utilizadas** **para** **estas** **definições.**

**Access:** **Acesso** **às propriedades** **do** **SMTP**

**Authentication:** **Define as** **regras de** **autenticação** **para** **acesso ao** **servidor** **SMTP. Podendo** **permitir** **acesso** **anônimo** **ou** **não ao** **serviço** **de** **mensagens. As aplicações** **RM Corpore** **permitem** **a** **utilização** **com** **ambos** **os** **métodos.**

**Relay:** **Habilita** **o envio** **de** **mensagens** **a** **outros** **domínios** **que** **o seu.**

**Relay** **Autenticado: permite** **que** **seus** **usuários** **internos** **enviem** **email** **para** **áreas** **fora da** **sua** **organização,** **mas** **requer** **autenticação antes** **do** **correio** **eletrônico** **ser** **enviado.** **Por padrão,** **o Exchange** **permite** **apenas** **"Relay"** **autenticado.**

**Relay** **Anônimo: permite** **que** **qualquer** **usuário** **se** **conecte** **ao** **seu** **servidor** **Exchange e usá-lo** **para** **enviar** **email** **fora** **de** **sua** **organização.**

**Exemplos:**

**Um** **usuário** **anônimo** **conecta** **ao** **servidor** **SMTP** **e** **tenta** **entregar** **um** **mail** **para** **o usuário** **interno na** **organização.** **Nesta** **situação,** **o** **servidor** **SMTP** **aceita** **a** **mensagem** **porque** **ela** **é destinada** **a** **um** **domínio** **interno** **e** **porque** **existe** **o** **usuário** **no** **Active** **Directory.**

**Um** **usuário** **anônimo** **conecta** **ao** **servidor** **SMTP** **e** **tenta** **entregar** **um** **mail** **para** **o usuário** **externo, em** **um** **domínio** **externo.** **Nesta** **situação,** **o** **servidor SMTP** **rejeita** **o** **correio eletrônico, uma** **vez** **que** **é** **destinado** **a** **um** **domínio** **externo para** **o** **qual** **o** **servidor** **Exchange não** **é** **responsável.** **Uma** **vez** **que** **o** **usuário** **não** **seja** **autenticado,** **o** **servidor** **SMTP** **não "Relay"** **este** **mail** **fora** **da** **organização.**

**Um** **usuário** **se** **conecta** **ao** **servidor** **SMTP** **usando** **POP** **ou** **IMAP,** **autentica e,** **em seguida,** **tenta** **enviar uma** **mensagem** **a** **um** **usuário em** **um** **domínio** **externo.** **Nesta** **situação, o** **cliente** **de** **email** **(aplicativo) conecta** **diretamente** **ao** **servidor** **SMTP** **e** **autentica** **o** **usuário. Apesar** **da** **mensagem** **ser** **destinada** **a** **um** **domínio remoto,** **o** **servidor** **SMTP** **aceita e** **"Relay" este** **mail** **porque** **o usuário** **está** **autenticado.**
