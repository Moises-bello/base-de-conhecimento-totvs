---
content_hash: c95f256635f39c7eb0ecab222cc8010448f1c516c5999b11f67ecac1ada326b7
fetched_at: '2026-06-29T00:09:34.477829+00:00'
page_id: '425459165'
product: rm
source: tdn-rm
title: TOTVS Obras e Projetos x BackOffice Protheus - Pré-Requisitos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459165
version: 3
---

**Pré-Requisitos**

---

**Aplicativos**

* Protheus versão 10 release 1.3
  + Patch específico da integração
* RM versão 11.20 (ou superior)

**Banco de Dados**

* SQL Server 2005
* SQL Server 2008
* Oracle 10G

**Sistema Operacional**

* Windows 32 bits

**Outros**

* Microsoft .NET Framework 4.0
* Biblioteca RM 11.20 (ou superior)

**Observações:**

* A TOTVS disponibiliza um backup da base de dados RM "vazia" que pode ser utilizada para novos clientes. Para clientes que já possuem versão anterior utilizar o Conversor RM para atualizar o banco de dados para a versão 11.20.
* Tanto o TOTVS Obras e Projetos quanto o BackOffice Protheus utilizam o modelo de licenciamento TOTVS padrão (Licence Server). Sendo que os Web Services do Protheus exigem uma licença específica (Master I ou Protheus I - utilização de Web Service). As licenças (hard lock) devem ser providenciadas junto a TOTVS com a devida antecedência.
* Se o cliente já possui base de dados implantada do RM ou do Protheus, **será de responsabilidade da equipe de implantação efetuar a carga inicial e/ou sincronismo dos cadastros**. A integração irá efetuar o sincronismo automático de novos registros ou alterações posteriores à ativação da integração.

**Instalação**  
    
 Não entraremos em detalhes quanto às instalações do TOP e Protheus. Iremos focar no TBC, ou seja, nas funções de integração do nosso EAI RM para este pacote de integração específico. Estes procedimentos são realizados pelo implantador, responsável por instalar e configurar a integração. O atendimento aos pré-requisitos mencionados devem ser verificados junto ao Cliente.

---

**Recursos Adicionais**

[TDN - Manual Técnico da Integração TOTVS Obras e Projetos x BackOffice Protheus](http://tdn.totvs.com/download/attachments/4810777/ManualTecnicoTOPxProtheus2012-03-16.rar?version=1&modificationDate=1337523012203)
