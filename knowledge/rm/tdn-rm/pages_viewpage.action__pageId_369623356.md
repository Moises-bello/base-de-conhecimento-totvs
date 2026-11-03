---
content_hash: 871bb12837dcf691d71f388fd3f31fb652706807263d90c7b97034364be9ca7d
fetched_at: '2026-06-29T00:09:00.516830+00:00'
page_id: '369623356'
product: rm
source: tdn-rm
title: EDU0006 - Compartilhamento por grupo de empresas - Integração 1021
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=369623356
version: 90
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | BackOffice Protheus - TOTVS Educacional |
| **Versões:** | 12 |
| **Ocorrência:** |  |
| **Ambiente:** |  |
| **Passo a passo:** | Caso o Protheus esteja parametrizado para utilizar o compartilhamento das tabelas por grupo de empresas, é necessário realizar a parametrização abaixo, para que os registros compartilhados entre as empresas do grupo sejam corretamente compartilhados entre as coligadas do RM.    Após a configuração da integração no ambiente RM, informar o significado da coligada na integração com o Protheus.   1. Acessar o cadastro de integração (Módulo Integração | Mensagem única | Integrações ) 2. Para que exista a gestão por grupo de empresas na integração o significado da coligada deve ser marcada como "Company" ou "Bussines Unity" 3. Acessar o cadastro de coligada no RM (Módulo Serviços Globais | Coligadas) 4. Informar quais as coligadas fazem parte do grupo de empresa. Isso é feito através do código externo existente no cadastro de coligada.  No exemplo abaixo a Coligada 1, no RM, faz parte do grupo de empresas GP1, do Protheus.         [Retornar](http://wikihelp.totvs.com.br/WikiHelp/EDU/EDU.totvsEducacional.aspx) |

## Artigos relacionados

false5LRMfalsemodifiedtruepagelabel = "kb-how-to-article" and type = "page" and space = "LRM"kb-how-to-article
