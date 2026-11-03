---
article_id: 19125068671767
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 9be48aa8637cad81e4559b0e5644ce782942407e9c2b10bb59be5b057615e6cf
fetched_at: '2026-06-28T22:42:02.299254+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Como gerar valor de ICMS Frete no campo 05 do G125?
type: support-article
updated_at: '2023-11-17T19:06:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19125068671767-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-gerar-valor-de-ICMS-Frete-no-campo-05-do-G125
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19125057786903) Tempo aproximado para leitura: **00:02:30 min****Dúvida**Como gerar valor de ICMS Frete no campo 05 do G125?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Solução:**

Conforme determinação do Guia Prático o campo **05** do **G125** deve ser alimentado com o valor de **ICMS** Próprio:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19125073946263)

Porém, para **Frete** tipo = **CIF**, com o valor de frete destacado na nota faz parte da base de cálculo do **ICMS**, dessa forma é necessário aglutinar o **ICMS Frete** junto ao Próprio no campo **05** do **G125**.

Para essa questão ocorrer devidamente, aplique o patch abaixo:

12.1.2210:<https://r.totvs.io/p/1124610> ;

12.1.2310:<https://r.totvs.io/p/1124613> ;

Parâmetro:

**MV\_FTCIAP** = S

**MV\_F9SKPNF** = .F. (Busca da SFT/SF3)

**MV\_F9SKPNF** = .T. (Busca da SF9)

Após, isso efetue o processo:

**1** - Gere uma nota de entrada com a **TES** configurada conforme abaixo:

**Credita ICMS** = Sim

**Atu. Ativo** = Sim – Caso haja integração com o módulo Ativo Fixo, o registro gerado na SF9 gera um registro também na SN1.

**Desm. IT. ATF** = Sim/Não – Parâmetro utilizado para desmembrar os itens constantes na nota fiscal de entrada. Por exemplo: Item 001 – Quantidade: 03 – Se campo for configurado como SIM, são criados 3 registros referentes a esta NF. Caso configure como NÃO, será lançado somente um ativo com valor total de ICMS.

**Calcula ICMS** = Sim

**Livro Fiscal de ICMS** = Outros

**Material de Consumo** = Sim

**Livro Fiscal CIAP** =Sim

**Desp Ac ICMS** = Sim (Para o frete fazer parte da base de cálculo do ICMS)

**2** - Após, na aba "**Desconto/Frete/Despesas"** alimente o valor do **Frete**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19125068633111)

**3** - Caso esteja com o campo **Atu. Ativo = Sim** na TES utilizada, acesse a rotina de classificação do ativo

antes de apropria-lo.

**4** - Acesse a rotina **MATA906** para apropriar o **BEM** e consultar os valores gerados na **SF9**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19125057791511)

No padrão, os campos da **SF9** gerará desta forma:

**Valor ICMS (F9\_VALICMS)** = Gerará com o próprio + 2x o ICMS Frete

**ICMS Próprio (F9\_VALICMP)** = Gerará com o próprio + ICMS Frete

**ICMS Frete (F9\_VALFRET)** = Com o valor do ICMS Frete

**5** - Gere o **Sped Fiscal**, segue apresentação:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19125073952919)
