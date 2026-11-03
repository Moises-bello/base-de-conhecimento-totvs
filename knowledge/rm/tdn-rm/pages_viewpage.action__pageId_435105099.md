---
content_hash: 40ba488fe395555f7be16d71b9a13d75a8efbfea0eaef74aab9fbd78d672ef5b
fetched_at: '2026-06-29T00:09:47.915504+00:00'
page_id: '435105099'
product: rm
source: tdn-rm
title: Solicitação de Atendimento integrada ao Agilis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105099
version: 2
---

**Solicitação de Atendimento integrada ao Agilis**    
 Existe a possibilidade de realizar o fluxo de Atendimento da Garantia, utilizando os processos do Agilis. Onde toda a Solicitação de Atendimento cadastrada, criará um Atendimento no Agilis.  
 **Pré-Condições**  
 Para a utilização dos processos Agilis na execução do fluxo de Atendimento da Garantia, é necessários alguns cadastros e parametrizações prévias:   
 *Cadastros:*

* Coberturas
* Modelos
* Responsáveis
* Etapa
* Associar o modelo ao empreendimento.
* Gerar uma venda que possui a cobertura.
* Grupo de Atendimento (*Agilis*)
* Tipo de Atendimento (Agilis)
* Etapa Agilis, vinculada a Etapa do TIN

*Parâmetros:*

* Nos parâmetros da Garantia: *Parâmetros SGI >> Contratos >> Garantia >> Etapa 2 - Integração com Agilis*, maque o campo "Criar automaticamente um Atendimento no Agilis ao criar uma Solicitação".
* Ao marcar o parâmetro acima, serão habilitados os seguintes campos:
  + **Coligada do Agilis:** Indica qual a coligada que será criado os atendimentos do Agilis *(Campo obrigatório);*
  + **Grupo de Atendimento:** Indica qual o Grupo de atendimento será utilizado para a criação do atendimento, será exibido somente os Grupos de Atendimento da Coligada selecionada *(Campo obrigatório);*
  + **Tipo de Atendimento:** Indica qual o Tipo de Atendimento será utilizado para a criação do atendimento, será exibido somente os Tipos de Atendimento do Grupo de Atendimento selecionado *(Campo obrigatório);*

Após realizar os cadastros e parametrizações necessárias, ao criar uma Solicitação de Atendimento, automaticamente será criado um Atendimento no Agilis. Assim ao executar o processo de "Avançar Etapa", será executado o processo do Agilis, utilizando o fluxo de atendimento contido no Tipo de Atendimento parametrizado.

|  |  |
| --- | --- |
|  | Veja Também |

---

Para maiores informações sobre os Parâmetros da Garantia, acesse o link abaixo:   
    
 Parâmetros da Garantia  
    
 Para maiores informações sobre o Grupo de Atendimento, acesse o link abaixo:  
 Grupo de Atendimento  
 Para maiores informações sobre o Tipo de Atendimento, acesse o link abaixo:  
 Tipo de Atendimento  
 Para maiores informações sobre o vínculo da Etapa do TIN com a Etapa do Agilis, acesse o link abaixo:   
 Etapa Agilis
