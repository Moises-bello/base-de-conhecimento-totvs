---
article_id: 8899599519383
category: Materiais - Compras (SIGACOM)
content_hash: e9d825e6f4f14bcdc9403c55a4b0058d7773d690bba6d956086cb41add997151
fetched_at: '2026-06-28T22:41:11.565130+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Ao incluir uma
  Nota do tipo Devolução é apresentado o Help A410UNIDIF
type: support-article
updated_at: '2023-08-04T11:42:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8899599519383-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Ao-incluir-uma-Nota-do-tipo-Devolu%C3%A7%C3%A3o-%C3%A9-apresentado-o-Help-A410UNIDIF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16529033563799) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Ao incluir uma Nota do tipo Devolução é apresentado o Help A410UNIDIF

![imagem2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8899031854871)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12  
  
**Solução**O help em questão pode estar relacionado a condição de casas decimais dos campos envolvidos no processo.

Por se tratar de uma relação de Compras x Vendas caso haja qualquer campo com quantidade de casas decimais divergentes no processo realizado, o help será apresentado.

Por exemplo, os campos D1\_QUANT, D2\_QUANT estão com o tamanho 6, porém o D1\_QTDPED está com tamanho 2. Bem como os campos das tabelas de NF de Saída da NF que está sendo Devolvida.

Dessa forma recomenda-se a checagem se  se os campos de **quantidade** e **valor** das tabelas **SC6, SD2**, **SD1** e **SB6** estão com a quantidade de **tamanho e decimais iguais**, conforme a documentação: **[FAT0068\_Aumento\_de\_Casas\_Decimais\_no\_ambiente\_Faturamento\_SIGAFAT](https://tdn.totvs.com/x/twEmDg)**

Todos os campos de Quantidade e Valor devem possuir mesmo tamanho / máscara.   
Com exceção de campos de **Valor Total**, esses campos não podem ser alterados e devem permanecer com 2 casas decimais (evitando inclusive erros em arquivos fiscais).

Documentação Complementar:

[MP-FAT-Ajuste de casas decimais e tamanho de campo para campos de percentual de comissão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059174994-MP-FAT-Ajuste-de-casas-decimais-e-tamanho-de-campo-para-campos-de-percentual-de-comiss%C3%A3o?source=search)

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
