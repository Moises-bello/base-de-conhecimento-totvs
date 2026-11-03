---
article_id: 12928311594903
category: NFe - Nota Fiscal Eletrônica
content_hash: dba1d756fb5a4388b4c00ff0bda86481b045d9f83f3aa4dd47d6392aafddf307
fetched_at: '2026-06-28T22:40:07.082913+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota Técnica 2023.001
type: support-article
updated_at: '2025-10-06T18:23:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12928311594903-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Nota-T%C3%A9cnica-2023-001
---

**Dúvida**Quais serão as alterações da Nota Técnica 2023.001 ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.27

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Para a adequação à Nota Técnica **2023.001 Versão 1.00.**

**O prazo previsto para a Nota Técnica 2023.001 v1.00 é:**

Ambiente de Homologação (ambiente de teste das empresas): **13/02/2023**

**Ambiente de Produção: 13/03/2023**

Para a adequação à Nota Técnica **2023.001 Versão 1.30.**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Rejeição 769 - Obrigatório o preenchimento da Quantidade tributada retida anteriormente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22658426125847-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Rejei%C3%A7%C3%A3o-769-Obrigat%C3%B3rio-o-preenchimento-da-Quantidade-tributada-retida-anteriormente?source=search)

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 508 Rejeição CST incompatível na operação com Não Contribuinte](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018436411--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-508-Rejei%C3%A7%C3%A3o-CST-incompat%C3%ADvel-na-opera%C3%A7%C3%A3o-com-N%C3%A3o-Contribuinte?source=search)

Para a adequação à Nota Técnica **2023.001 Versão 1.40.**

**O prazo previsto para a Nota Técnica 2023.001 v1.40 é:**

* Ambiente de Homologação (ambiente de teste das empresas): **16/10/2023**
* **Ambiente de Produção: 30/10/2023**

**1. Atualização do ambiente TSS (repositório e schemas)**

Atualizar o **repositório** com o último pacote de**expedição continua do TSS** disponível no link:

[MP - TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981)

Atualizar a pasta **SCHEMAS** presente na estrutura do TSS através do link:  
[TSS - Atualização dos SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552)

**2. Atualização do ambiente Protheus:**

Aplicar o **Pacote Acumulado Documentos eletrônicos:**

[Clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=525010692)

Aplicar o **Pacote da escrituração fiscal:**

[Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/1039088)  

**Compilar RDMAKE NFESEFAZ, DANFEII e DANFEIII** (se emitir NF-e) presente no link abaixo:

[Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1152113)

* **Saiba mais:**

Lembrando que **RDMAKE não possui Release** sendo assim, pode ser aplicada em qualquer uma todos os pacotes.

 4. Criação **dos novos campos de forma Manual.**

[Clique Aqui](https://tdn.totvs.com/display/public/PROT/DSERTSS1-21006+DT+Protheus+NT+2023.001+Montagem+de+XML+Rdmake)

Criaçãodos **Campos** abaixo no dicionário de dados: Tabela CD6 - Complemento de Combustíveis

| **Campo** | CD6\_PBIO |
| --- | --- |
| **Tipo** | Numérico |
| **Tamanho** | 8 |
| **Decimal** | 4 |
| **Formato** | @E 999.9999 |
| **Validação** | Iif(M->CD6\_PBIO < 0 .Or. M->CD6\_PBIO > 100, .F., .T.) |
| **Título** | Perc. Biodie |
| **Descrição** | Perc. Biodiesel oleo dies |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Help** | Informar o percentual do índice de mistura do Biodiesel para o produto Óleo Diesel B.  Valores maiores que 0 e menores ou iguais a 100. Utilizado na geração da tag <pBio> do grupo <comb> |

| **Campo** | CD6\_PORIG |
| --- | --- |
| **Tipo** | Numérico |
| **Tamanho** | 8 |
| **Decimal** | 4 |
| **Formato** | @E 999.9999 |
| **Validação** | Iif(M->CD6\_PORIG < 0 .Or. M->CD6\_PORIG > 100, .F., .T.) |
| **Título** | P.Orig.UF |
| **Descrição** | Perc. Originario para UF |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Help** | Informar o percentual originário para a UF. Esse valor será obtido através dos Anexos de Combustíveis previstos em Ato Cotepe.  Valores maiores que 0 e menores ou iguais a 100. Utilizado na geração da tag <pOrig> do grupo <origComb> |

| **Campo** | CD6\_UFORIG |
| --- | --- |
| **Tipo** | Caracter |
| **Tamanho** | 2 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Validação** | Positivo() |
| **Título** | UF de Origem |
| **Descrição** | Código da UF Origem |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Help** | Sigla da UF de origem do produtor ou do importador. Utilizar a tabela do IBGE.  Utilizado na geração da tag <cUFOrig> do grupo <origComb> |

| **Campo** | CD6\_INDIMP |
| --- | --- |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Ind. Import. |
| **Descrição** | Indicador de importação |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Opções** | 0=Nacional; 1=Importado; |
| **Val. Sistema** | Pertence(" 01") |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Help** | Indicador de importação. Usado na geração da tag <indImport> do grupo <origComb> |

Criaçãodos novos **Código de CST**para configuração de TES:

No **Configurador (SIGACFG)**, acessar **Base de Dados \ Dicionários \ Base de Dados**. Selecionar a opção **Tabelas Genéricas** e **Pesquisar** pelo código "**S2**". Clicar em **Editar** para incluir os novos registros.

![](https://tdn.totvs.com/download/attachments/747330772/image2023-3-31_18-37-36.png?version=1&modificationDate=1680298656350&api=v2&effects=drop-shadow)

Posicionado no ultimo registro da opção **Itens**, pressione seta para baixo para incluir uma nova linha. Nesta linha informar os seguintes CST:

|  |  |
| --- | --- |
| **Chave** | **Descrição** |
| 2 | Tributação monofásica própria sobre combustíveis. |
| 15 | Tributação monofásica própria e com responsabilidade pela retenção sobre combustíveis. |
| 53 | Tributação monofásica sobre combustíveis com recolhimento diferido. |
| 61 | Tributação monofásica sobre combustíveis cobrada anteriormente. |

Conforme imagem abaixo. Log em seguida clicar em "**OK**".

![](https://tdn.totvs.com/download/attachments/747330772/image2023-3-31_18-38-49.png?version=1&modificationDate=1680298730117&api=v2&effects=drop-shadow)

Alíquota ad rem do ICMS, estabelecida na legislação para o produto.  
Tabela de códigos de combustíveis sujeitos à tributação monofásica de ICMS - Publicada em 19/04/2023

Cálculo de ICMS **Monofásico Convênio 15/2023:**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=765332384>

Obs: Para a gravação do conteúdo das novas tags

**adRemICMSRet e vICMSMonoRet**

Necessário que gera na tabela CD2 a linha CD2\_IMP = STMONO e seja preenchido os campos abaixo:  
 - **CD2\_ALIQ** -> <adRemICMSRet>**0**</adRemICMSRet>

 - **CD2\_VLTRIB** -> <vICMSMonoRet>**0**</vICMSMonoRet>

Para a adequação à Nota Técnica  
**2023.001 Versão 1.50** publicada em 01/11/2023 não haverá ajustes, essa NT muda apenas regras de validação da Sefaz.
