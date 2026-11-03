---
content_hash: c38b56603435a1fb408fe943380adad441ad278b24cb3954893d40e17c1c5ca4
fetched_at: '2026-06-29T00:11:45.765991+00:00'
page_id: '821572000'
product: rm
source: tdn-rm
title: DT - eSocial - Nota Técnica S-1.2 Nº 02/2024 - Item 3.1
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=821572000
version: 10
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento - eSocial |
| Função: | Nota Técnica 02/2024 - Item 3.1 |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-8671](https://jiraproducao.totvs.com.br/browse/DRHROTRM-8671) |

## **02.** **VERSÕES**

* 12.1.2302.257
* 12.1.2306.216
* 12.1.2310.148  ou superiores

## **03.****SITUAÇÃO/REQUISITO**

Adequar o produto para atender as alterações descritas na [Nota Técnica 02/2024](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-2-02-2024.pdf) do eSocial publicada em 10/01/2024.

## **04. SOLUÇÃO**

Considerando o cronograma divulgado pelo governo nesta NT, as primeiras alterações a serem liberadas serão aquelas relacionadas aos itens **3.1.**Diante disso, liberamos as adequações no produto TOTVS Folha de Pagamento conforme descrito abaixo:

**3.1** Alterações previstas para serem implantadas nas seguintes datas: 

* Ambiente de produção restrita: 01/02/2024
* Ambiente de produção: 01/02/2024

**ALTERAÇÕES NO PRODUTO:**

No cadastro das "Informações do Empregador", no campo "Indicativo de Desoneração da Folha", foram realizadas as seguintes alterações:

1. Ajuste na descrição do valor "1", que anteriormente era "Empresa enquadrada nos arts. 7º a 9º da Lei 12.546/2011", foi alterado para "Empresa enquadrada nos critérios da legislação vigente".
2. Inclusão do valor "2 - Município enquadrado nos critérios da legislação vigente" e implementação da validação correspondente. Sendo a validação: "Pode ser igual a [1] apenas se classTrib = [02, 03, 99]. Pode ser igual a [2] apenas para as naturezas jurídicas iguais a [103-1, 106-6, 124-4, 133-3]. Nos demais casos, deve ser igual a [0]".
3. Tratamento da geração da tag <indDesFolha> no evento S-1000.

**ATENÇÃO:** Em breve, forneceremos informações sobre a previsão de liberação dos itens **3.2** nas linhas de produtos de folha de pagamento, fique ligado nas noticias publicadas no nosso [RH Informa](https://informa.totvs.com/rh/).

## **05. DEMAIS INFORMAÇÕES**
