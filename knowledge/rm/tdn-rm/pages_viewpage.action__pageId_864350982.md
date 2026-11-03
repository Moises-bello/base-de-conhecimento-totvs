---
content_hash: 5bded7ad7ee7e5d6bb365c27ba506ed1bf6da44d5e88739d5f909360af284065
fetched_at: '2026-06-29T00:11:55.881870+00:00'
page_id: '864350982'
product: rm
source: tdn-rm
title: DT - Integração com TOTVS RH Orçamento - Parametrizador
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=864350982
version: 3
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
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHHCM-13050](https://jiraproducao.totvs.com.br/browse/DRHHCM-13050) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2410

## **03. SITUAÇÃO/REQUISITO**

      Na tela "Parametrizador" criar um novo processo "TOTVS RH Orçamento". Ao selecionar esse processo e clicar em Avançar, será exibido o campo "Habilitar integração". Por padrão esse campo virá desmarcado.

## **04. SOLUÇÃO**

Foi criado um item no parametrizador do sistema de Gestão de Pessoas para definição da Integração com o TOTVS RH Orçamento.

Este parâmetro poderá ser manipulado apenas quando não houver requisições de Aumento de Quadro, Substituição, e Alteração de Dados Funcionais com status "Suspensa" ou "Em andamento".

Ao tentar manipular o parâmetro, a mensagem abaixo deverá ser exibida.

## **04. DEMAIS INFORMAÇÕES**

Ao persistir essa opção, será possível identificar em Banco de Dados, através da tabela VPARAMADICIONAIS onde na coluna NOMECOLUNA esteja identificado como INTEGRACOMTOTVSORCAMENTO.  
Caso esteja habilitada a integração, o valor da coluna VALORINT será 1, caso não esteja habilitada o valor será 0.

O parâmetro **"Habilitar Integração com TOTVS RH Orçamento"**não poderá ser manipulado enquanto houver registros de requisições na base de dados com os status "Suspensa" ou "Em andamento".
