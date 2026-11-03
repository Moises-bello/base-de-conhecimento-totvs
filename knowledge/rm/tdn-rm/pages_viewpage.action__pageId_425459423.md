---
content_hash: 34f7467472c4fabda9d72c9d9987162f945e41d66b23244d3dc4ed1c517cf691
fetched_at: '2026-06-29T00:09:35.900077+00:00'
page_id: '425459423'
product: rm
source: tdn-rm
title: Cadastro Município
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459423
version: 2
---

**Cadastro Município**

---

Os Municípios são atualizados automaticamente na base RM.   
 Ao iniciar o RM ocorre uma verificação dos estados no site do IBGE, e quando é identificado uma mudança nos estados (um novo estado, por exemplo) os dados são atualizados na base RM.  
    
 A integração permite realizar o sincronismo dos estados existentes na base RM para o MS CRM, através do agendamento deste conceito "Cadastro\_Municipio\_RM\_CRM".  
    
 ***Observações:***

* Nenhuma inclusão e/ou alteração no cadastro de município realizadas no MS CRM serão sincronizadas para a Linha RM.
* O agendamento do conceito é realizado na configuração da integração.
* A sincronização deste cadastro ocorre em massa.

Para visualizar os cadastros de municípios no RM, acesse: BackOffice | Gestão de Estoques, Compras e Faturamento | Cadastros | Mais | Municípios  
 Para visualizar os municípios sincronizados para o MS CRM, acesse: MS CRM (4.0 ou 2011) | Integração | Municípios  
     
 **Dados Sincronizados**  
    
 Os dados sincronizados do RM para o MS CRM referentes a este cadastro são:

* Código do Município
* Código do Estado
* Nome do Município
