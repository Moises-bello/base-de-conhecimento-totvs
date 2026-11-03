---
content_hash: 169ba731483dca59b75d40910d01e5e203f48c766c88ec2da686ade1e246e61d
fetched_at: '2026-06-29T00:09:35.335862+00:00'
page_id: '425459315'
product: rm
source: tdn-rm
title: Conteúdo Geral Backoffice Protheus - De-Para Mensagem Única - Company e Branch
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459315
version: 5
---

**De-Para Mensagem Única - Company e Branch**

---

Em integrações com o Protheus, cuja arquitetura seja Mensagem Única, o De-Para das mensagens Company e Branch devem ser configurados manualmente.   
    
 Para realizar o cadastro do De-Para no RM acesse: RM.exe | módulo Integração | Mensagem Única | De-Para.

Inclua os registros conforme orientação abaixo:  
    
 **De-Para de Empresa (Company)**

| **Campo** | **Valor** |
| --- | --- |
| Tabela RM | GCOLIGADA |
| Chave Primária RM | CODCOLIGADA |
| Valor Chave Primária RM[ | [Código da coligada no RM] |
| Sistema Integrado | PROTHEUS |
| Valor Chave Integração | [Código da coligada no RM] |

****Notas**:**

* O cadastro de De-Para de empresas **em integrações com o Protheus** será feito de forma particular, relacionando tanto o campo referente à chave no RM quanto o campo de valor externo, com o código da coligada no RM.
* Para integração com outros sistemas, que não o Protheus, no campo "Valor Chave Integração" deve ser adicionado o valor referente ao campo CompanyId do sistema de destino.
* Os campos destacados entre colchetes devem ser preenchidos com os dados referentes à descrição dada. Os outros campos devem ter o valor fixo.

**De-Para de Filial (Branch)**

| **Campo** | **Valor** |
| --- | --- |
| Tabela RM | GFILIAL |
| Chave Primária RM | CODCOLIGADA CODFILIAL |
| Valor Chave Primária RM | [Código da coligada + Código da Filial] |
| Sistema Integrado | PROTHEUS |
| Valor Chave Integração | [Dado referente ao CompanyInternalId no Protheus] |

****Notas:****

* O separador '|' informado na chave primária RM deve ser adicionado entre o código da coligada e o código da filial sem espaços. Ex: 1|1 -> Onde a coligada possui código '1' e a filial possui código '1'.
* O campo CompanyInternalId do Protheus pode ser obtido por observação de alguma mensagem que possua este campo ou através da concatenação dos campos CompanyId e BranchId, separados pelo caractere '|'.
* Os campos destacados entre colchetes devem ser preenchidos com os dados referentes à descrição dada. Os outros campos devem ter o valor fixo.
