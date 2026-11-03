---
article_id: 360006894472
category: Materiais - Compras (SIGACOM)
content_hash: 0876e011cde01784109ccbacd855c242833aeb65614214675b7c17d59c5a9ab7
fetched_at: '2026-06-28T22:41:10.121865+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ocorrência do Help
  A100VALDUP ao incluir NF de Entrada
type: support-article
updated_at: '2022-05-13T11:43:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006894472-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ocorr%C3%AAncia-do-Help-A100VALDUP-ao-incluir-NF-de-Entrada
---

**Dúvida**Ocorrência do Help A100VALDUP ao incluir NF de Entrada  
   
**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
**Solução**

Para que o sistema considere o valor de tolerância entre o total da nota e valor das duplicatas e não permita a inclusão da nota fiscal quando houver divergências, os parâmetros abaixo devem estar configurados:

- **MV\_LIMPAG** = Valor de tolerância permitido entre o Total da Nota Fiscal e as Duplicatas

- **MV\_CONFDUP** = Parâmetro que irá indicar se poderá haver interação do usuários com os valores de duplicatas recalculados.   
Configurar com valor igual 1, para permitir a interação.

- **MV\_LIMREC** = Mesmo que não haja diferença entre o valor da nota e a tolerância o sistema deve recalcular o valor das duplicatas.   
Configurar com valor igual a 2.

Ao confirmar a nota, se o valor das duplicatas estiver maior que o valor da nota, porém dentro da tolerância, o sistema irá permitir a inclusão. Caso contrário, se o valor das duplicatas for maior que a nota e maior que a tolerância permitida, o sistema irá recalcular as parcelas e não irá confirmar a inclusão da nota.
