---
article_id: 11482254247063
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 7dcb0e4d2e910bb0defddc478a5c95d530ca254511cc11e814fddf3e98426d9d
fetched_at: '2026-06-28T22:42:02.474215+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Valor incorreto no campo 5 do G125 quando a quantidade do item na nota é maior
  que 1
type: support-article
updated_at: '2023-01-06T13:36:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11482254247063-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Valor-incorreto-no-campo-5-do-G125-quando-a-quantidade-do-item-na-nota-%C3%A9-maior-que-1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao gerar o Sped Fiscal com B**loco G**, no **campo 05 do G125**, o valor apresentado não condiz com o valor de **ICMS Próprio** apresentado na **Manutenção CIAP**.   
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Causa**  
Esse incidente ocorre, pois a parametrização do sistema está incorreta quanto à configuração do campo **Desm. IT. ATF -F4\_BENSATF** no cadastro de **TES** utilizado na escrituração da nota que acobertou a entrada do bem.

**Solução**

O campo **Desm. IT. ATF -F4\_BENSATF** é utilizado para desmembrar os itens constantes na nota fiscal de entrada.

**Exemplo:**

Item 001 – Quantidade: 03

Se o campo for configurado como **SIM**, são criados **3 ativos referentes** a esta NF cada qual com o valor proporcional do ICMS.

Caso configure como **NÃO,** será lançado somente **1 ativo** com valor total de ICMS.

Quando este campo é alterado, ocorre problema na geração do **Bloco G**. É preciso ter um cadastro de **TES** específico para os casos em que **Não Desmembra o Ativo** e outra para quando deve ser Desmembrado. 

O que explica a diferença de valores é alteração do campo em questão após escrituração da nota.

Abaixo um exemplo em que o valor estava incorreto devido a alteração no cadastro:

Veja que o valor que consta no **campo 05 do G125** é justamente a multiplicação da quantidade pelo valor do **ICMS.**

226 x 15.140,84 = 2.774.701,44

![](https://totvssuporte.zendesk.com/attachments/token/ZHcscoHrmaXZJKpBjIAD9w031/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/qCj8uVFEtojyzdGGcfCd4iUEf/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/cFFQiCkYDx8ZPLjtNjk5Z5iOg/?name=image.png)

Fazendo alteração do campo para 2 (da forma que provavelmente estava quando do momento da escrituração)

![](https://totvssuporte.zendesk.com/attachments/token/Do48VyUfQHIe8wWuRmLy5vxTn/?name=image.png)

Foi gerado corretamente conforme abaixo:

![](https://totvssuporte.zendesk.com/attachments/token/lM24Z5htKrheMzpjNZn7nFOsy/?name=image.png)
