---
article_id: 21373523807639
category: Financeiro
content_hash: 1d6cfbf11ce1e7934d41718fd4de91511403e986eee708f3c356b26e29072ab8
fetched_at: '2026-06-28T22:38:03.014107+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice linha Protheus - SIGAFIN - FINA381 - Qual são
  um dos motivos da rotina aglutinação de impostos IRRF, PIS, COFINS e CSLL não aglutinarem?
type: support-article
updated_at: '2024-02-15T15:05:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21373523807639-Cross-Segmentos-Backoffice-linha-Protheus-SIGAFIN-FINA381-Qual-s%C3%A3o-um-dos-motivos-da-rotina-aglutina%C3%A7%C3%A3o-de-impostos-IRRF-PIS-COFINS-e-CSLL-n%C3%A3o-aglutinarem
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21373544197911) Tempo aproximado para leitura: **00:15: min****Dúvida**Qual são um dos motivos da rotina aglutinação de impostos IRRF, PIS, COFINS e CSLL não aglutinarem?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões]  
  
**Cenário 1:** Título a pagar com IR e PCC parametrizados para gerar na emissão.

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/21373544200983)](https://centraldeatendimento.totvs.com/hc/article_attachments/21373544200983)

**1 ponto:**

É necessário verificar os parâmetros abaixo, pois se o título na base tenha um fornecedor ou natureza diferente do que está nos parâmetros,  a rotina pode deixar de não aglutinar

[MV\_UNIAO = Código do fornecedor dos impostos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052816113-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Utiliza%C3%A7%C3%A3o-do-par%C3%A2metro-MV-UNIAO)

[MV\_IRF = Código da natureza do IR (com aspas duplas)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115016051667-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-definir-a-natureza-utilizada-para-os-t%C3%ADtulos-de-IRRF)

**MV\_PISNAT** = Código da natureza do PIS

**MV\_COFINS** = Código da natureza do COFINS

**MV\_CSLL** = Código da natureza do CSLL

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/21373523776919)](https://centraldeatendimento.totvs.com/hc/article_attachments/21373523776919)

Caso eu tenha números cadastrados nos parâmetros, como devem ficar:

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/21373544209943)](https://centraldeatendimento.totvs.com/hc/article_attachments/21373544209943)

[**![](https://centraldeatendimento.totvs.com/hc/article_attachments/21373523784215)**](https://centraldeatendimento.totvs.com/hc/article_attachments/21373523784215)

**2 ponto:**

Pergunte parâmetro "Filial De" e "Filial Até"

O sistema irá pesquisar pelo campo E2\_FILORIG, veja se o campo foi gravado corretamente

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/21373523787799)](https://centraldeatendimento.totvs.com/hc/article_attachments/21373523787799)

Caso o pergunte esteja:

**"Modo Retenção = Emissão"** o sistema irá utilizar o campo E2\_EMISSAO para pesquisar

**"Modo Retenção = Baixa"** o sistema irá utilizar o campo E5\_BAIXA para pesquisar

**"Modo Retenção = Vencimento Real"** o sistema irá utilizar o campo E2\_VENCREA para pesquisar

O E2\_TIPO dos impostos devem ser do tipo TX ou TXA, caso contrário o sistema não irá encontrar dados.

O saldo do título de imposto, deve ser igual ao campo valor do imposto, caso contrário o sistema não irá encontrar dados.

O campo não pode ter o conteúdo E2\_NUMTIT = FINA381 ou E2\_NUMTIT = FINA378

O conteúdo do campo E2\_IDDARF deverá estar vazio

**3 ponto:** O campos E2\_TITPAI

O campo E2\_TITPAI dos títulos de impostos, faz o vinculo entre o titulo filho (título de impostos tipo TX) e o título pai (o título que originou o impostos, exemplo tipo NF)

E essa amarração é feita através do campo E2\_TITPAI que grava uma chave de identificação entre os registros

Essa chave E2\_TITPAI grava o conteúdo no título do impostos com o conteúdo Prefixo, Número do título, Parcela, Tipo, Fornecedor e Loja

Pode apresentar problemas,  quando é alterado o tamanho de algum campo que faz parte desta chave, e para mais informações sugiro a documentação abaixo

[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - CTBAFIN - Contabilização duplicando ou gerando gravação incorreta do campo da tabela Sequência de Baixa (E5\_SEQ)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18890795067927-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-CTBAFIN-Contabiliza%C3%A7%C3%A3o-duplicando-ou-gerando-grava%C3%A7%C3%A3o-incorreta-do-campo-da-tabela-Sequ%C3%AAncia-de-Baixa-E5-SEQ)

[Cross Segmento - Backoffice Linha Protheus - FINA050 - Desdobramento acima de 35 parcelas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021873891-Cross-Segmento-Backoffice-Linha-Protheus-FINA050-Desdobramento-acima-de-35-parcelas)
