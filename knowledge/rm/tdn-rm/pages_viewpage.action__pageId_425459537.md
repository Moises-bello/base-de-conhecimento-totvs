---
content_hash: 769bb7c3294df1279edb086d878b68674fd43c2b9df96e8f0c73243489552292
fetched_at: '2026-06-29T00:09:36.874350+00:00'
page_id: '425459537'
product: rm
source: tdn-rm
title: Arquiteturas - Mensagem Única
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459537
version: 6
---

**Mensagem Única**

---

As primeiras integrações entre produtos TOTVS de origens diferentes utilizaram-se de diferentes técnicas de integração, como o uso de triggers de banco ou exportação de arquivos texto, por exemplo.   
 Com o objetivo de padronizar as integrações com os produtos TOTVS, foi definida uma nova diretriz para os projetos de integração: a de que todos os produtos TOTVS devam trabalhar com uma mensagem XML únicas evitando, desta forma, o processo de transformação de mensagens.   
 Neste cenário, qualquer produto TOTVS trabalhará com o mesmo XML para uma mesma entidade, ou seja, supondo que suporte o recebimento desta entidade. Uma vez que os vários produtos TOTVS terão um "idioma" comum as integrações entre estes produtos não exigirão mais que as mensagens sejam transformadas de um formato para outro. Com isto, será possível conectar diretamente dois produtos, sem a necessidade do TOTVS ESB, como no diagrama abaixo:  
   
 A mensagem única também torna uniforme o tratamento destas mensagens XML pelos aplicativos, principalmente no que diz respeito à capacidade de rastreamento. Ela estabelece alguns padrões que devem ser seguidos por todos os aplicativos que participem da integração. Estes padrões estabelecem alguns tipos de mensagens suportadas bem como informações obrigatórias que devem fazer parte do seu conteúdo.  
    
    
 **Fórmula Visual**  
    
 Visando facilitar a sincronização de dados em massa entre o RM e sistemas integrados via Mensagem Única TOTVS, foi desenvolvida uma atividade de fórmula visual que se responsabiliza por, a partir de alguns parâmetros, obter os dados necessários e solicitar o envio da Mensagem Única TOTVS para o sistema de destino.  
 Clique no link para mais informações: **Sincronização de Registros via atividade de Fórmula Visual**  
    
 **Integrações que utilizam esta arquitetura:**

* TOTVS Educacional x TOTVS Learning Management System
* Backoffice RM x Protheus SigaMNT
* TOTVS Incorporação x Backoffice Protheus
* TOTVS Folha de pagamento x BackOffice Logix
