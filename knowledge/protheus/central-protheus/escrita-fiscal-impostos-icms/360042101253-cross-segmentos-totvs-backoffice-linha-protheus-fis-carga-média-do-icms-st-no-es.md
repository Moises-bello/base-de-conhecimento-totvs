---
article_id: 360042101253
category: Escrita Fiscal - Impostos - ICMS
content_hash: a079e6f8efd784b21b4ab2327cefc04628c966b4a0817789d9291f01267b1cd0
fetched_at: '2026-06-28T22:39:24.140444+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Carga média do ICMS-ST
  no estado de Mato Grosso a partir de Janeiro 2020
type: support-article
updated_at: '2021-07-28T03:18:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042101253-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Carga-m%C3%A9dia-do-ICMS-ST-no-estado-de-Mato-Grosso-a-partir-de-Janeiro-2020
---

**Dúvida**

Até 31 de Dezembro de 2019, o ICMS - ST  no estado do mato Grosso ocorria por Carga Média, atrelado ao CNAE do cliente.

A partir de 01 de Janeiro de 2020 mudou este cenário, onde passa ser como os demais estados do Brasil, no entanto, No entanto existe algumas particularidades, para alguns clientes onde o MVA do mesmo produto poderá ser diferente para clientes revendedores dependendo se o cliente for optante ou não de beneficio fiscais.

**Ambiente**Protheus - Fiscal - A partir da versão 12.1.23  
  
**Solução**

Devera realizar as configurações abaixo:

Parâmetro "SIGACFG"

 O parâmetro **MV\_REGESIM** deve estar como ***.F.***

Cadastro de cliente "SA1"

O campo **Rg. Simp. MT** (A1\_REGESIM)  deve estar como ***NÃO***

O campo **P. Carga Med** (A1\_PERCATM) deve estar como ***0,00***

Cadastro de Fornecedor "SA2"

O campo **Rg. Simp. MT** (A2\_REGESIM) deve estar como ***NÃO***

Cadastro de Produto "SB1"

O campo Rg. Simp. MT (B1\_REGESIM) = ***NÃO***

Para calcular o ICMS ST devera seguir orientação disponível no link abaixo:

# ***[MP - FIS - Qual a configuração Padrão para o cálculo do ICMS-ST, Margem de Lucro no produto ou exceção fiscal?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026224194-MP-FIS-Qual-a-configura%C3%A7%C3%A3o-Padr%C3%A3o-para-o-c%C3%A1lculo-do-ICMS-ST-Margem-de-Lucro-no-produto-ou-exce%C3%A7%C3%A3o-fiscal-?source=search)***
