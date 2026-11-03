---
content_hash: cf199ee7d68a2452b5bc71f366619855ac3e08c691fd6af5a6189b8326ef7d70
fetched_at: '2026-06-29T00:09:35.865549+00:00'
page_id: '425459402'
product: rm
source: tdn-rm
title: Preenchendo o cadastro da Integração, Gerado Pelo Configurador de Integrações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459402
version: 8
---

**Preenchendo o cadastro da Integração, Gerado Pelo Configurador de Integrações**

---

O cadastro da integração é responsável por identificar o webservice e as regras empresariais utilizadas pelo Protheus.

**Pré-Condições:**

1- Ter executado o configurador da integração Backoffice TOTVS Protheus x TOTVS Incorporação

2- Ter definido a regra de empresas, filiais ou grupo de empresas que será utilizado, através do arquivo sigamat.emp do TOTVS Protheus.  
   
**Preenchendo o cadastro**

1- Acesse: Integração/ Integração/ Mensagem Única/ Integrações

2- Execute um filtro que retorne a integração desejada (identificador da integração = 1000)

3-Selecione o cadastro da integração e clique em \[Editar Integração\]

4- Preencha os campos e clique no botão \[Salvar\].Os campos são:

* **Nome da Integração:** Nome da Integração. Valor gerado pelo Configurador da integração
* **Nome Reduzido:** Nome reduzido da Integração. Valor gerado pelo Configurador da integração
* **Sistema Integrado:** Sistema qual o RM integrará
* **CheckBox Ativo?:** Identifica se a integração está ativa
* **URL do Webservice:** Url do webservice  do sistema Integrado. deverá ser informado conforme o exemplo:

Estrutura:{\*} [http://ServidorEAI:PortaEAI/eaiservice.apw?wsdl](http://ServidorEAIPortaEAI)

**Exemplo:**[{+}](http://localhost:83/eaiservice.apw?wsdl)<http://localhost:83/eaiservice.apw?wsdl+>

* **Usuário de Autenticação:** Usuário de autenticação do TOTVS Business Connect(mestre)
* **Senha de Autenticação:** Senha de autenticação do TOTVS Business Connect(totvs)
* **Significado de coligada:**

**- Company Groups:** Se o arquivo sigamat.emp protheus foi criado com a configuração de grupos de empresas

**- Company:** Se o arquivo sigamat.emp protheus foi criado com a configuração de Empresa e Filial

**-Business Unity**: Se o arquivo sigamat.emp protheus foi criado com a configuração de Unidade de Negócios
