---
article_id: 360017958992
category: NFe - Nota Fiscal Eletrônica
content_hash: 84695edb96ad1bb9a4bd5e852b50249804c3db611c6321ffba1f02070d380b6f
fetched_at: '2026-06-28T22:40:06.681054+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar apenas
  uma unidade de medida no xml e no Danfe para operações dentro do País ?
type: support-article
updated_at: '2025-11-28T20:50:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017958992-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-apenas-uma-unidade-de-medida-no-xml-e-no-Danfe-para-opera%C3%A7%C3%B5es-dentro-do-Pa%C3%ADs
---

**Dúvida**

Como gerar apenas uma unidade de medida no Danfe para operações dentro do País ?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

**Como criar o parâmetro MV\_NIMP2UM ?**

Para atender a nota técnica 2016.001 é necessário utilizar a tabela SB5 para utilização da segunda unidade de medida, ao realizar essa configuração é gerado para qualquer nota as duas unidades de medida no Danfe sem que haja a verificação do país de destino da nota, como o produto utilizado para fazer vendas nacionais e de exportação pode ser o mesmo, foi criado um parâmetro para que o XML e a Impressão de Danfe em operações nacionais seja opcional sair impresso com as duas unidades de medida

## Parâmetro:

Nome: MV\_NIMP2UM  
Descrição: Não imprime a 2ª. Unidade de Medida para operações dentro do País.  
Tipo: Lógico  
Conteúdo: .T. - Não Imprime ou .F. - Imprime (Default)

## Regra:

* Se o parâmetro estiver com o conteúdo .T. – será considerado “ATIVO”, ou seja, não será impresso a 2ª. Unidade de Medida para operações de dentro do País, com exceção dos CFOPS das operações vinculadas a exportação: 1501, 2501, 5501, 5502, 5504, 5505, 6501, 6502, 6504 ou 6505; e
* Se o parâmetro estiver com o conteúdo .F. – será considerado “INATIVO”, ou seja, será impresso a 2ª. Unidade de Medida para todas as operações (Default).

**Operações nacionais que não sejam dos CFOPs 1501, 2501, 5501, 5502, 5504, 5505, 6501, 6502, 6504 ou 6505; mesmo que haja cadastro do produto na SB5 será gerado com o parâmetro habilitado como .T.**
