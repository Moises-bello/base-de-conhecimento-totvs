---
content_hash: 39efc975f6e8791a1feda7b8e124530b2059bc9ff9fe437c9bcb9086b96536de
fetched_at: '2026-06-29T00:10:16.607131+00:00'
page_id: '476745678'
product: rm
source: tdn-rm
title: FISCAL01-7868 DT Layout ECF - Alterações Y672
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=476745678
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Estrutura do Registro Y672 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-7868 |

## **02. SITUAÇÃO/REQUISITO**

Criar uma nova estrutura para o Registro Y672 que contemple a exclusão dos campos 18 - VL\_FOLHA e 19 -  VL\_ALIQ\_RED. Fazer a alteração no layout, mantendo a compatibilidade para períodos anteriores

## **03. SOLUÇÃO**

Layout da ECF foram realizadas as seguintes alterações, de acordo com o [Manual ECF 2019](http://sped.rfb.gov.br/estatico/84/62D84C440E97164D123ABE283B1308D53BC17A/Manual_de_Orienta%C3%A7%C3%A3o_da_ECF_Fevereiro_2019.pdf):

**- Registro Y672 foram removido os campos:**

* 18 - VL\_FOLHA
* 19 - VL\_ALIQ\_RED

## **04. DEMAIS INFORMAÇÕES**

* Para gerar o Layout atualizado deve-se selecionar no *Processo do Gerador de Saídas* a versão 005 (ou mais atual).
* A estrutura do XML foi alterada no Contábil. O novo XML está publicado em Objetos Gerenciais.
