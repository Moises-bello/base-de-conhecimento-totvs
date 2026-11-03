---
content_hash: 22103502c7acef497431d523ee870e70dcd722a719a0575cc106f1f2aebf315f
fetched_at: '2026-06-29T00:11:56.685008+00:00'
page_id: '868233301'
product: rm
source: tdn-rm
title: DT - Integração RM x Feedz - Utiliza token por filial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=868233301
version: 7
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Integração RM x Feedz - Utiliza token por filial |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-11372](https://jiraproducao.totvs.com.br/browse/DRHROTRM-11372 "View this issue") |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2310.260
* 12.1.2402.232
* 12.1.2406.158 e superiores

## **03. SITUAÇÃO/REQUISITO**

Há a necessidade de permitir a utilização de mais de um token na mesma coligada, possibilitando a integração de várias bases Feedz para a mesma empresa no TOTVS Folha de Pagamento RM.

## **04. SOLUÇÃO**

Foi criado o parâmetro '**Utiliza token por filial'**. Com esse parâmetro, o TOTVS Folha de Pagamento RM transmitirá as informações dos funcionários conforme a filial cadastrada, direcionando os dados para o ambiente correspondente na Feedz, de acordo com o Token indicado. Ao marcar esse parâmetro, o sistema habilitará a aba **'Token X Filiais'**, permitindo a vinculação entre os tokens e as respectivas filiais.

Para as coligadas que não tiverem um token associado, o sistema utilizará o token padrão preenchido no campo **'Feedz | Token'**.

Passo 1 - Em Configurações | Parametrizador | Integrações | Feedz marque o parâmetro **'****Utiliza token por filial'**. 

Passo 2 -  Ao marcar o parâmetro acima, será habilitado a aba **'Token x Filiais'**, realize a vinculação

Passo 3 - Acesse o menu Administração de Pessoal | TOTVS RH Performance e Meta / Feedz e realize o envio das informações. 

Passo 4 - Demonstração de recebimento Feedz

Após realizar a integração dos funcionários e associação dos seus líderes, os dados foram enviados corretamente conforme a parametrização realizada no passo 2.

**ATENÇÃO****:** Na plataforma Feedz, por motivos estruturais, não é possível associar um líder de uma base de dados a um subordinado de outra base dados.

Por exemplo, o líder/chefe da filial 01 (RM), cadastrado na base 01 (Token 1 Feedz) não pode ser vinculado a um subordinado da filial 02 (RM), cadastrado na base 02 (Token 2 Feedz).

## **05. DEMAIS INFORMAÇÕES**

[Integração RM X Feedz](https://tdn.totvs.com.br/pages/releaseview.action?pageId=785614408)
