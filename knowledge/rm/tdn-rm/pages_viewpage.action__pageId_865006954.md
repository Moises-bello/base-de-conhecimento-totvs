---
content_hash: bc8f9c5a617e5d789ba2f2e845b8b70f0ddbbccd993bcc5470fd606c5699d378
fetched_at: '2026-06-29T00:11:55.979367+00:00'
page_id: '865006954'
product: rm
source: tdn-rm
title: DT - Integração com TOTVS RH Orçamento - Requisição de Alteração de Dados Funcionais
  (Campos)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=865006954
version: 2
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Gestão de Pessoas |
| Função: | Integração com TOTVS RH Orçamento |
| País: | Brasil |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHHCM-13054](https://jiraproducao.totvs.com.br/browse/DRHHCM-13054) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2410

## **03. SITUAÇÃO/REQUISITO**

      

       Na criação ou edição da requisição de alteração de dados funcionais será verificado se o [parâmetro que habilita a integração](https://tdn.totvs.com/pages/viewpage.action?pageId=864350982) está marcado.

       Se não estiver marcado:

* + A aba "TOTVS RH Orçamento" não será exibida

       Se estiver marcado:

* + A aba "TOTVS RH Orçamento" será exibida e terá os campos abaixo:
    - Centro de custo
    - Item contábil
    - Classe de valor

## **04. SOLUÇÃO**

       Foi criada uma nova aba no cadastro da requisição de alteração de dados funcionais contendo os dados acima informados.

       Para essa integração, quando a mesma estiver habilitada a aba estiver visível, o campo Centro de Custos estará visível e obrigatório.  
       Os demais campos (Item Contábil e Classe de Valor) serão visíveis conforme regra já constante hoje na folha de paramento para os mesmos campos no cadastro do funcionário.

* Visibilidade dos campos Item Contábil e Classe de Valor:
  + No sistema de Folha de Pagamento (Configurações | Parametrizador | Integrações | Outros BackOffice) é necessário habilitar o parâmetro "Usa integração outros backOffice".

* Habilitar os campos Item Contábil e Classe de Valor:  
  + No sistema de Folha de Pagamento (Configurações | Parametrizador | Folha de Pagamento | Folha Normal | Contabilização) é necessário habilitar o parâmetro "Item Contábil" e/ou "Classe de Valor".
  + No sistema de Folha de Pagamento (Configurações | Parametrizador | Folha de Pagamento | Folha Normal | Lancto Financeiro) é necessário habilitar o parâmetro "Item Contábil" e/ou "Classe de Valor".

## **05. DEMAIS INFORMAÇÕES**

* Quando não estiver habilitada a integração, não deverá ser habilitada a aba contendo os dados de Centro de Custo, Item Contábil e Classe de Valor
* O campo "Permite Exceção" nunca será habilitado pois irá refletir o retorno do TOTVS RH Orçamento, onde somente será marcado, caso no TOTVS RH Orçamento esteja habilitada a possibilidade de Exceção quando de uma negativa.
