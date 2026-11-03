---
content_hash: 5101e257913152fd94c6b34d0aa287ca61438c692e96689f6db484077fce50e8
fetched_at: '2026-06-29T00:11:45.037988+00:00'
page_id: '819051699'
product: rm
source: tdn-rm
title: DT - Integração RM x Benefícios Flexíveis Swile - De/Para benefícios terceiros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=819051699
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Gestão de Pessoas (VITAE) |
| Função: | Integração RM x Swile |
| País: | Brasil |
| Story | [DRHCALCRM-5853](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-5853) |

## **02. SITUAÇÃO/REQUISITO**

No RM é possível cadastrar vários benefícios com a mesma finalidade como valores, descrição, eventos de lançamento para folha, entre outros que podem customizados pelo usuário. Estes benefícios são vinculados aos colaboradores e seus dependentes, podendo cada colaborador e/ou dependente ter benefícios específicos vinculados conforme a necessidade do cliente. Porém na integração com a Swile só é possível vincular um benefício RM a um benefício Swile, impossibilitando que o usuário tenha essa flexibilidade de utilizar vários benefícios no módulo Gestão de Pessoas.

## **03. SOLUÇÃO**

Foi alterado o cadastro De/Para de benefícios de terceiros para permitir vincular mais de um benefício RM a um mesmo benefício Swile. Com isto também foi tratado o envio dos pedidos para acumular todos os valores dos benefícios associados ao mesmo código de Benefício Swile na mesma integração, de forma que o usuário possa enviar todos os benefícios em uma única requisição caso haja a necessidade do mesmo.

## **04. DEMAIS INFORMAÇÕES**

**Para que seja possível fazer a associação de N Códigos de Benefícios RM a um mesmo Código de Benefício Swile é necessário executar o atualizador após a aplicação do patch que a solução foi disponiblizada.IMPORTANTE!**

## **05. ASSUNTOS RELACIONADOS**

[Integração TOTVS RM X Benefício Flexíveis Swile](https://tdn.totvs.com/pages/releaseview.action?pageId=737546308)
