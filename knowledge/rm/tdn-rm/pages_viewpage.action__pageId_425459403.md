---
content_hash: 91d5f8f670040caf1d6ca98ea0f1ea7633babca247e2929af6c328d7ebf99c24
fetched_at: '2026-06-29T00:09:35.868654+00:00'
page_id: '425459403'
product: rm
source: tdn-rm
title: Duas Integrações Ativas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459403
version: 2
---

**Duas Integrações Ativas**

---

**1. Integrações TOTVS Incorporação (TIN) x BackOffice Protheus e TOTVS Obras e Projetos (TOP) x BackOffice Protheus**   
    
 As integrações TOTVS Obras e Projetos (TOP) x BackOffice Protheus e TOTVS Incorporação (TIN) x BackOffice Protheus possuem cadastros integrados que são comuns entre as duas.  
    
 Quando se utiliza a integração TOP x Protheus com arquitetura Stored Procedure, e na mesma base é ativada a integração TIN x Protheus com arquitetura Mensagem Única os cadastros que são comuns nas duas integrações só poderão ser executados na integração com Mensagem Única.  
    
 Neste caso, os cadastros sincronizados nas integrações são:

|  |  |  |
| --- | --- | --- |
| **Cadastros da integração TOP x Protheus** |  | **Cadastros da integração TIN x Protheus** |
| Empresa\*   Filial\*   Condição de Pagamento   Unidade de Medida   Produto   Cliente/Fornecedor   Moeda e Cotação   Centro de Custos   Projeto, Obra, Tarefa |  | Empresa\*   Filial\*   Condição de Pagamento\*   Moeda\*   Produto\*   Cliente/Fornecedor   Centro de Custos   Banco   Natureza Financeira |

*\* São Cadastros Manuais*  
    
    
 Quando as duas integrações estão ativas (considerando o cenário TIN x Protheus com mensagem única e TOP x Protheus com Stored Procedure) os cadastros em comum são sincronizados apenas pela integração TIN x Protheus, por meio de mensagem única. Estando dessa forma desativados, por meio de configurações no perfil de segurança, o sincronismo dos mesmos na integração TOP x Protheus.
