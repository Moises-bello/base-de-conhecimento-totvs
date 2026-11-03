---
article_id: 360052211974
category: RH - Integração de Titulo
content_hash: 069dc447125dc8385c5b0abc7f5ad8e7e231610bc04e7bfc89f2c6d6127da575
fetched_at: '2026-06-28T22:43:36.494235+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Chave de busca de duplicidade de títulos
type: support-article
updated_at: '2025-07-18T14:04:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052211974-RH-Linha-Protheus-GPE-Chave-de-busca-de-duplicidade-de-t%C3%ADtulos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33558642080919)**Tempo aproximado para leitura: 00:03:00 min

**Dúvida**Chave de busca de duplicidade de títulos  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão Pessoal -  A partir da Versão 12.1.17.  
  
**Solução**A funcionalidade da consistência de duplicidade de títulos, não considera a data de vencimento **(RC1\_VENCTO)** na chave de busca de títulos duplicados (A validação ocorre pelas seguintes chaves: Filial/Agrupamento/Prefixo do título/Tipo/Competência), não possibilitando a geração de títulos diversos para a mesma competência e fornecedor, que é uma necessidade de quem trabalha com o pagamento de semanalistas, por exemplo.  
  
Criado o  parâmetro **MV\_CHAVDUP** para permitir a inclusão da data de vencimento do título, **(RC1\_VENCTO)** na chave de busca de títulos para consistência de duplicidade.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084153234)

1. A funcionalidade do parâmetro **MV\_CHAVDUP** está diretamente ligada a do **MV\_CONDUPL,** sendo que só haverá diferença de comportamento entre as opções "1" e "2" se o conteúdo do **MV\_CONDUPL** estiver como **".T."**;
2. O parâmetro será disponibilizado a partir do release 12.1.28. Para utilizar a implementação em algum release inferior, o parâmetro **MV\_CHAVDUP** deverá ser criado manualmente pelo configurador.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084156054)

## **ASSUNTOS RELACIONADOS**

 Consistir Duplicidade de Títulos - <https://tdn.totvs.com/pages/viewpage.action?pageId=204966712>

Como incluir um novo parâmetro pelo configurador - <https://tdn.totvs.com/pages/viewpage.action?pageId=306855076>  
  
**Saiba Mais**  
[Artigos sobre Integração de Títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
