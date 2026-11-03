---
content_hash: 3d6a8e7a4cac34cae6c288b164b75a54874b2b955d84cf6dafa25de7b605c03b
fetched_at: '2026-06-29T00:09:30.321972+00:00'
page_id: '425458428'
product: rm
source: tdn-rm
title: Pesquisa de satisfação - Parâmetros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458428
version: 2
---

**Pesquisa de satisfação**

**Endereço para Pesquisa de Satisfação**   
    
 O fluxo normal de um atendimento é: abertura do atendimento, interpretar a solicitação, encontrar uma solução, informá-la ao cliente (aguardar um ok do cliente), encerrar o atendimento. Ao passar a informação ao cliente (concluído respondido) o sistema gera um registro de pesquisa de satisfação e envia um e-mail ao cliente com um link para que ele possa responder tal pesquisa. Este link na verdade é um endereço web composto de um "site", um complemento indicando diretório, a página da pesquisa de satisfação e um código criptografado que identifica o atendimento:   
    
 *(href=<site>corpore.net/Source/CRM/RM.CRM.Servicos/CRMPesquisaSatisfacaoRedirect.html?Codigo=<código criptografado>)*  
    
 Este parâmetro serve para valorar qual é o site onde o serviço de pesquisa de satisfação se encontra disponível. Este serviço só está disponível caso o cliente possua o portal da linha RM.   
    
    
 **Caixa Postal para resposta do cliente em caso de não concordar com a solução do atendimento**  
    
 Este parâmetro é utilizado em duas situações: a partir do e-mail de conclusão de atendimento que é enviado ao cliente e também ao e-mail enviado ao cliente sobre a pesquisa de satisfação respondida. O e-mail de conclusão de atendimento é enviado ao cliente OU o e-mail enviado ao cliente sobre a pesquisa de satisfação pode ter alguma resposta por parte do cliente, esta resposta deve ser armazenada em uma caixa postal, e posteriormente deve ser lida e analisada por alguém da empresa. Este parâmetro é utilizado para indicar onde as respostas serão armazenadas para posteriormente serem lidas e analisadas.  
    
 **Observação**  
    
 O preenchimento desta caixa postal é obrigatório para o envio de e-mail de conclusão de atendimento enviado ao cliente.  
    
    
 **Texto complementar (Ex:. Agradecimento) pela resposta da pesquisa de satisfação**   
    
 Sempre que uma pesquisa de satisfação é respondida um e-mail é enviado ao cliente (e a uma caixa postal da empresa) contendo informações do atendimento e outras informações sobre o que foi citado na pesquisa de satisfação. Este parâmetro é um texto livre que será incorporado ao e-mail citado acima e enviado ao cliente.
