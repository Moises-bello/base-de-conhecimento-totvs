---
content_hash: 83e75a940b4d4598536d41216ee8effb4e1b85c9880da893da80df0663847f2a
fetched_at: '2026-06-29T00:09:34.561527+00:00'
page_id: '425459188'
product: rm
source: tdn-rm
title: Linha RM x Microsoft Dynamics CRM - Pré-Requisitos e Restrições da Integração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459188
version: 3
---

**Pré-Requisitos e Restrições da Integração**

---

Para o perfeito funcionamento da integração, é necessário atender ao pré-requisitos apresentados abaixo:  
    
 **Linha RM**

* Linha RM versão 11.80 (ou superior)

**Microsoft Dynamics CRM**

* Microsoft Dynamics CRM 4.0
* Microsoft Dynamics CRM 2011

**Banco de Dados**

* SQL Server 2005
* SQL Server 2008
* Oracle 10G

**Sistema Operacional**

* Windows 32 bits

**Outros**

* Arquivos de customização do MS CRM
* Microsoft .NET Framework 4.0

**Observações:**

* A TOTVS disponibiliza um backup da base de dados RM "vazia" que pode ser utilizada para novos clientes. Para clientes que já possuem versão anterior utilizar o Conversor RM para atualizar o banco de dados para a versão 11.80.
* Caso o cliente já possua base de dados implantada do RM será responsabilidade da equipe de implantação efetuar a carga inicial e/ou sincronismo dos cadastros. A integração irá efetuar o sincronismo de novos registros ou alterações posteriores à ativação da integração.
* Para obter os arquivos customizados referente a esta integração o Cliente deve entrar em contato com o Suporte da TOTVS-BH no produto Integração. Os arquivos correspondem as versões 4.0 e 2011 do MS CRM.
* Os clientes que já possuem seu MS CRM customizado, ao importar o arquivo customizado referente a integração Linha RM x MS CRM, os mesmos irão perder suas customizações.

**Instalação:**

Não entraremos em detalhes quanto às instalações de produtos da Linha RM ou do MS CRM. Iremos focar no TBC, ou seja, nas funções de integração do nosso EAI RM para este pacote de integração específico. Os procedimentos de instalação são realizados pelo implantador, responsável por instalar e configurar a integração. O atendimento aos pré-requisitos mencionados devem ser verificados junto ao Cliente.
