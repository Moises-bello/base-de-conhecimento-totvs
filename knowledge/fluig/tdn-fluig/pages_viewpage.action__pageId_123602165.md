---
content_hash: 9b967ba64d490843fe1698f45712a3c5ea3ce6528d48530119b36ba86e2ad16b
fetched_at: '2026-06-28T21:35:17.703517+00:00'
page_id: '123602165'
product: fluig
source: tdn-fluig
title: Integração de Módulos Customizados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=123602165
version: 12
---

# Índice

true.\*ndicenone

# Objetivo

---

O objetivo deste guia é sanar dúvidas referentes a integração de módulos customizados com o TOTVS Fluig Plataforma.

# Pré-requisitos

---

Para desenvolver a integração em .NET, PHP ou outra linguagem, é necessário ter o ambiente de desenvolvimento da respectiva linguagem instalado.

# Integração de Módulos Customizados

---

Acompanhe a seguir, dois exemplos de integrações desenvolvimentos em .NET e um de integração PHP.

* Exemplo    
  Este exemplo envia um determinado documento via protocolo FTP para a área de *upload* do usuário, e após concluído o envio, realiza a publicação de documento através do método *createDocument* do WebService *DocumentService* enviado uma segurança customizada.

* Exemplo   
  Este exemplo realiza a movimentação de um processo workflow e incluindo anexos através do método *saveAndSendTask* do WebService *WorkflowEngineService*.

Importante

Notem que em alguns campos além de informar o valor da variável, é necessário definir a variável como *Specified*, caso contrário o valor não é enviado pela requisição WebService.

* Exemplo   
  Este é um exemplo de integração da linguagem PHP com os WebServices do Fluig Plataforma.
