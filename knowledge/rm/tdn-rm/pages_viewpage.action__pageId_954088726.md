---
content_hash: b4e1f575f86e7f450c2818c8fb0201e1ca439479444b2657b57a02dbf0e3ef05
fetched_at: '2026-06-29T00:12:13.350094+00:00'
page_id: '954088726'
product: rm
source: tdn-rm
title: FISCAL01-25685 - Evento Tributário - Violação de chave estrangeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=954088726
version: 2
---

## **01. DADOS GERAIS**

| Produto: | TOTVS |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | Evento Tributário |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-25685 |

## **02. SITUAÇÃO/REQUISITO**

Ao salvar um Evento Tributário que foi vinculado uma Conta Contábil na aba Centro de Custo, ocorre o erro abaixo:  
   
*Violação de chave estrangeira*  
*Possíveis causas:*  
*- exclusão de registro que possui outros registros associados*  
*- inclusão de registro detalhe sem um registro mestre associado*

## **03. SOLUÇÃO**

Pequeno ajuste em query para correta seleção do dados das contas contábeis e execução de script de banco de dados para correção do problema.  
O script realiza a alteração no relacionamento entre as tabelas  do evento tributário e Conta.

Disponível à partir da biblioteca 12.1.2410
