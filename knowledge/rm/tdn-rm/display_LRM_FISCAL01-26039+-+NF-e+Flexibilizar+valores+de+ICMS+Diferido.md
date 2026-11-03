---
content_hash: 3893f2afa69d9536ba9ed362ef7aaa187c7f4e0e69181155a1b40d81c27357ea
fetched_at: '2026-06-29T00:12:13.483564+00:00'
page_id: '960021370'
product: rm
source: tdn-rm
title: FISCAL01-26039 - NF-e Flexibilizar valores de ICMS Diferido
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-26039+-+NF-e+Flexibilizar+valores+de+ICMS+Diferido
version: 2
---

## **01. DADOS GERAIS**

| Produto: | TOTVS |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | BackOffice |
| Módulo: | Gestão de Estoque, Compras e Faturamento |
| Função: | Envio NF-e |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-26039 |

## **02. SITUAÇÃO/REQUISITO**

Ao emitir NF-e com diferimento total de ICMS (100%), os campos do grupo de ICMS (CST 51) estão sendo preenchidos no XML, comportamento que não ocorria anteriormente.  
   
Anteriormente, em operações com diferimento total, os campos relacionados ao ICMS permaneciam zerados no XML, conforme orientação da legislação vigente.  
   
O problema surgiu após a implementação da ISSUE [~~FISCAL01-25652~~](https://jiraproducao.totvs.com.br/browse/FISCAL01-25652 "NFE - Diferimento de ICMS"), onde foi solicitada uma adequação do sistema\* somente para o estado do Ceará,\* solicitando que mesmo quando o diferimento fosse de 100%, esses campos seriam preenchidos, porém, esta mudança foi aplicada **para todos os estados** , e gerou transtorno para os demais cliente de outros estados **(exceto Ceará e Rio de Janeiro)** , no qual informaram que de acordo com a legislação\* Orientação de Preenchimento da NF-e - versão 2.02 (leiaute NF-e 3.10) – 04/02/2015\* o comportamento de preencher os campos está incorreto.

## **03. SOLUÇÃO**

Criar um novo anexo global denominado **"Dados Fiscais do Estado"**, vinculado ao cadastro de Estados (UF). Esse anexo deve conter um campo booleano (sim/não) com o rótulo:  
**"Gerar dados de diferimento do ICMS na NF-e?"**  
O campo será utilizado para indicar se os campos do grupo ICMS51 devem ser gerados no XML da NF-e, conforme a UF emitente.

Quando o parâmetro **"Gerar dados de diferimento do ICMS na NF-e?"** estiver marcado o grupo ICMS51 será gerado contendo os seus respectivos valores, se não o grupo será gerado com valor 0.00 nas tags do diferimento, apenas quando for 100% diferido, ou seja, a tag não influencia nos valores do grupo quando for parcialmente diferido.
