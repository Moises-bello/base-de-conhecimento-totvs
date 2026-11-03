---
article_id: 360022521191
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: f0a62fd1b53f096c6f91c50c102bc51a9066a8f645ec6ab5f570dd151d007653
fetched_at: '2026-06-28T22:38:41.242158+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: MP - FAT - Nota de Devolução de Poder de Terceiro - Nota de Retorno
type: support-article
updated_at: '2026-05-15T20:20:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022521191-MP-FAT-Nota-de-Devolu%C3%A7%C3%A3o-de-Poder-de-Terceiro-Nota-de-Retorno
---

**Dúvida**Como emitir nota de devolução de poder de terceiro?   
  
**Ambiente**Microsiga Protheus –  A partir da versão 11.80  
  
**Solução**

Para emitir um Documento de Devolução no módulo Faturamento, por meio da emissão de um Pedido e respectivo Documento de saída, é necessário que sejam informados os itens:

* Nota Fiscal;
* Série;
* Item de origem.

De forma a estabelecer relacionamento com o Documento Original a ser devolvido.

Isto porque, a possibilidade de se realizar tal operação sem o devido relacionamento anula a integridade de dados no sistema.  
Inclusive, o **SEFAZ** rejeita o documento transmitido sem os devidos relacionamentos.

**Obs**: O indicado é que, se houver grande demanda de tal operação em seu negócio, e se for considerado inviável pela própria instituição incluir a Nota Fiscal de Origem no sistema apenas quando houver necessidade de devolve-lá (ajustando internamente as interferências na regra de negócio como estoque/custos).  
Então, que se alimente previamente o volume de dados (determinado período de registros de Documentos de Entrada/ Saída) na ocasião de implantação do módulo, reduzindo impactos quando se fizer necessário registrar operações relacionadas.

Veja mais detalhes na documentação abaixo.

**Saiba Mais:  
[Nota de Devolução de Poder de Terceiro / Nota de Retorno](http://tdn.totvs.com/pages/releaseview.action?pageId=236431772)**
