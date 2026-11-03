---
content_hash: e839a385c2a66cb5a2def159ad0201144e2245490398f081d661108658266de7
fetched_at: '2026-06-29T00:08:34.796099+00:00'
page_id: '274842097'
product: rm
source: tdn-rm
title: EDUCACIONAL01-948 Censo da Educação Básica 2017
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274842097
version: 104
---

# CENSO DA EDUCAÇÃO BÁSICA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | *****Educacional***** |
| **Módulo:** | *****Totvs Educacional***** |
| **Função:** | Censo da Educação Básica |
| **Situação/Requisito:** | Conforme testes realizados, foi identificado que o sistema está solicitando que o cliente crie campos complementares e mobilidade acadêmica indevidamente. Tabém que a colsulta SQL encontra-se incorreta e o processo de atualização de dados do censo está dando referencia de objeto.      * O erro relacionado à matricula no período letivo do Aluno, ocorre a partir da versão 12.1.13 enquanto o erro relacionado ao professor, ocorre a partir da versão 12.1.14       * O sistema está validando o campo CONSIDERADOCENSO como Null e S da tabela SMATRICPLCOMPL sendo que deveria apenas considerar S da Tabela SMATRICPLMEC do Campo Consideradocenso       * Na tela de dados do MEC da matricula no período letivo do aluno, o sistema obriga na primeira vez o cliente a “cadastrar” o campo Mobilidade acadêmica , Tipo de mobilidade e País destino.       * Verificar o processo de atualização de dados do MEC e SISTEC ao chamar a funcionalidade ocorre erro "Referência de objeto" |
| **Solução/Implementação:** | Foram feitas correções de nomenclatura para o campo CONSIDERADOCENSO. Retirada do campo complementar da consulta. Retirada de mensagem pedindo para cadastrar o campo complementar. Retirada da obrigatoriedade do campo Mobilidade acadêmica na tela de dados do MEC da matricula no período letivo do aluno. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
