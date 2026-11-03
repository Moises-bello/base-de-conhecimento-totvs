---
content_hash: cdc6b6ed3679e3c8b1fa073445e31f06b33056e5cf65a6b1df3581e65686e16e
fetched_at: '2026-06-29T00:10:37.309006+00:00'
page_id: '539530122'
product: rm
source: tdn-rm
title: DT Informações específicas dos parâmetros do Pergamum
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=539530122
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS Gestão Educacional |
| Função: | Integrações - Pergamum |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | EDUCACIONAL01-11361 |

## **02. SITUAÇÃO/REQUISITO**

Para a integração entre o TOTVS Educacional e o Pergamum funcionar era necessário efetuarmos um acesso direto a base do Pergamum para obtermos algumas informações sobre parâmetros, o que não era recomendado pela equipe do software pois poderia comprometer a segurança.

## **03. SOLUÇÃO**

A equipe do Pergamum disponibilizou um método para ser consumido através do webservice para realizar estas consultas, assim não precisamos mais efetuar acesso direto a base de dados e com isto, removemos da tela de parâmetrização do TOTVS Educacional todos os itens relacionados a base de dados do Pergamum, como esta informação não é mais relevante não há necessidade de mostrá-la na tela.

O funcionamento do sistema não terá nenhuma alteração nem será necessário nenhuma ação do usuário.

Para mais informações sobre os parâmetros 

Observações

Esta alteração está disponível à partir das versões:

* 12.1.24.285
* 12.1.25.238
* 12.1.26.187
* 12.1.27.130
