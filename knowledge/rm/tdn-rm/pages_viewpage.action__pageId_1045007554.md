---
content_hash: 14a9ac825400e160e3b246cc5f8ea84ff86974ebc65c7e7dde8ee10e28bcd212
fetched_at: '2026-06-29T00:05:50.898141+00:00'
page_id: '1045007554'
product: rm
source: tdn-rm
title: DT - Integração RM x Feedz - Utiliza token por Seção do Funcionário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1045007554
version: 12
---

## **1. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Integração RM x Feedz - Utiliza token por Seção do Funcionário |
| País: | Brasil |
| Épico: | [DRHROTRM-14774](https://jiraproducao.totvs.com.br/browse/DRHROTRM-14774) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2506.268
* 12.1.2510.187
* 12.1.2602.111 e superiores

## **03. SITUAÇÃO/REQUISITO**

Atualmente, o sistema permite utilizar mais de um token na mesma coligada, realizando a parametrização por filial. No entanto, há a necessidade de que essa parametrização seja realizadapor seção a nível de funcionário, em vez de por filial, possibilitando a integração de várias bases Feedz para a mesma empresa no TOTVS Folha de Pagamento (RM).

## **04. SOLUÇÃO**

Foi criado o parâmetro '**Utiliza token por Seção'**. Com esse parâmetro, o TOTVS Folha de Pagamento RM transmitirá as informações dos funcionários conforme a seção cadastrada, direcionando os dados para o ambiente correspondente na Feedz, de acordo com o Token indicado. Ao marcar esse parâmetro, o sistema habilitará a aba **Token X Seção**, permitindo a vinculação entre os tokens e as respectivas seções.

Para as seções que não tiverem um token associado, o sistema utilizará o token padrão preenchido no campo **'Feedz | Token'**.

Passo 1 - Em Configurações | Parametrizador | Integrações | Feedz marque o parâmetro **'****Utiliza token por Seção'**. 

Passo 2 -  Ao marcar o parâmetro acima, será habilitado a aba **'Token x Seção'**, realize a vinculação

**Atenção:** Serão apresentadas somente as seções referentes ao **nível de funcionário**, conforme aquebra mestre informada em Configurações | Parametrizador | 06.04 - RH - Máscaras e Quebras.

Passo 3 - Acesse o menu Administração de Pessoal | TOTVS RH Performance e Meta / Feedz e realize o envio das informações. 

Passo 4 - Demonstração de recebimento Feedz.

Após realizar a integração dos funcionários e associação dos seus líderes, os dados foram enviados corretamente conforme a parametrização realizada no passo 2.

**ATENÇÃO****:** Na plataforma Feedz, por motivos estruturais, não é possível associar um líder de uma base de dados a um subordinado de outra base dados.

Por exemplo, o líder/chefe da seção 01.01 (RM), cadastrado na base 01 (Token 1 Feedz) não pode ser vinculado a um subordinado da seção 02.02 (RM), cadastrado na base 02 (Token 2 Feedz).

## **05. DEMAIS INFORMAÇÕES**

[Integração RM X Feedz](https://tdn.totvs.com.br/pages/releaseview.action?pageId=785614408)
