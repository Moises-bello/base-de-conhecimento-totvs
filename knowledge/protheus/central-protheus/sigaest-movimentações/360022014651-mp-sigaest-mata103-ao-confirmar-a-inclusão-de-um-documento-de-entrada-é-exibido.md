---
article_id: 360022014651
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 5afac3d345932f021153bb864ad835990198106e373be71e369b56176653b013
fetched_at: '2026-06-28T22:38:54.174524+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: MP - SIGAEST -  MATA103 - Ao confirmar a inclusão de um Documento de Entrada
  é exibido o alerta "O Armazém informado é Invalido"
type: support-article
updated_at: '2021-04-28T15:45:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022014651-MP-SIGAEST-MATA103-Ao-confirmar-a-inclus%C3%A3o-de-um-Documento-de-Entrada-%C3%A9-exibido-o-alerta-O-Armaz%C3%A9m-informado-%C3%A9-Invalido
---

**Ocorrência**

Ao confirmar a inclusão de um documento de entrada é exibido o alerta "O Armazém informado é Inválido, o campo será ajustando com o armazém padrão do cadastro de produtos"  
  
**Ambiente**

Microsiga Protheus – Estoque– A partir da versão 11.80  
  
**Causa**

Esse incidente ocorre devido à parametrização do sistema estar configurada para considerar a tabela SBZ (**MV\_ARQPROD**) e o campo **BZ\_LOCPAD** estar em branco, com isso ao digitar o código do produto no documento de entrada, o campo armazém (D1\_LOCAL) fica em branco ocasionando o alerta.  
  
**Solução**

Para solucionar essa ocorrência, realize a manutenção do produto na rotina Indicador de Produtos (MATA018 ou MATA019), informando o campo BZ\_LOCPAD. Assim, ao fazer um Documento de Entrada para o produto em questão não aparecerá mais este Help.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
