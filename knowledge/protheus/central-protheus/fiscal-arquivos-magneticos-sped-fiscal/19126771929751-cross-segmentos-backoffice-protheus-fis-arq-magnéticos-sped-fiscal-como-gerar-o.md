---
article_id: 19126771929751
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 28d923997e107e1a00b3955cefd0d2dab712909d76d3cfd36ec756f8e5c258ff
fetched_at: '2026-06-28T22:42:01.150083+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Como gerar o campo 07 do G125?
type: support-article
updated_at: '2025-03-19T17:53:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19126771929751-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-gerar-o-campo-07-do-G125
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19126816446231) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como gerar o campo 07 do G125 no Sped Fiscal?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Solução**

Conforme validação do Guia Prático, o campo 07 do G125 somente deve ser apresentado caso possua amarração com CTE, caracterizando o frete como **Tipo = FOB**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19126788448791)

**Parâmetros**:

**MV\_FTCIAP** = S

**MV\_F9SKPNF** = .F. (Busca da SFT/SF3)

**MV\_F9SKPNF** = .T. (Busca da SF9)

**1** - Efetue amarração de uma nota com a **TES** configurada conforme abaixo:

**Credita ICMS** = Sim

**Atu. Ativo** = Sim – Caso haja integração com o módulo Ativo Fixo, o registro gerado na SF9 gera um registro também na SN1.

**Desm. IT. ATF** = Sim/Não – Parâmetro utilizado para desmembrar os itens constantes na nota fiscal de entrada. Por exemplo: Item 001 – Quantidade: 03 – Se campo for configurado como SIM, são criados 3 registros referentes a esta NF. Caso configure como NÃO, será lançado somente um ativo com valor total de ICMS.

**Calcula ICMS** = Sim

**Livro Fiscal de ICMS** = Outros

**Material de Consumo** = Sim

**Livro Fiscal CIAP** =Sim

**Modelo** = **SPED** (55)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19126794760599)

**2** - Após, acesse a rotina **MATA116** e inclua o **CTE** amarrando a nota efetuada na **MATA113**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19126808209943)

**3-** Amarre a nota e gera o **Conhecimento de Transporte:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19126788455575)

**4** - Alimente o tipo do frete na aba **"Informações DANFE**":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19126794773143)

**5** - Consulte os valores da **SF9** pela **MATA906** e aproprie:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19126808219543)

Neste cenário, os campos abaixo gerará:

**ICMS Frete =** Com o valor do frete

**Valor ICMS =** Valor do ICMS + ICMS Frete

**ICMS Próprio =** Valor do ICMS Próprio

**6** - Gere o **Sped Fiscal:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19126803342743)
