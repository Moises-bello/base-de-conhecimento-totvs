---
article_id: 360052627734
category: Escrita Fiscal - Impostos - ICMS
content_hash: 8f295aaaacc875a84c526c4e1139bdbcfae4df1c44f8b905e28adabbc77bd808
fetched_at: '2026-06-28T22:39:25.857092+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- FISA080 - UF x UF
  Cadastro Para Cálculo do FECP
type: support-article
updated_at: '2021-12-23T14:51:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052627734-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA080-UF-x-UF-Cadastro-Para-C%C3%A1lculo-do-FECP
---

**Dúvida**Qual a documentação devo seguir para o correto cadastro e realizar cálculo do FECP utilizando a rotina UF x UF.  
  
**Ambiente**Protheus - Fiscal - A partir da versão 11.80  
  
**Solução**

Disponível a rotina de cadastro UF x UF, que tem por objetivo realizar cadastros de regras de tributação que variam em função da Unidade Federativa de Origem e da Unidade Federativa de Destino. Estas regras serão utilizadas nos cálculos e na escrituração dos documentos fiscais. 

**Procedimento para Configuração**

 

No **Configurador (SIGACFG)** acesse **Ambiente/ Cadastros/ Menus** e inclua, no *menu* do módulo **Livros Fiscais (SIGAFIS)**, conforme especificação a seguir:

 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Nome do Menu** | **Submenu** | **Nome da Rotina** | **Programa** | **Tabelas** |
| atualizações | Cadastros | UF x UF | FISA080 | CFC |

No **Configurador (SIGACFG)** acesse **Base de Dados / Dicionário / Base de Dados**, inclua/verifique os campos necessários:

* Tabela CFC – UF x UF:

 

|  |  |  |  |
| --- | --- | --- | --- |
| Chave | Nome | Modo | PYME |
| CFC | UFxUF | E | S |

| Campo | CFC\_PAUTFB |
| --- | --- |
| Tipo | Numérico |
| Tamanho | 9 |
| Decimal | 2 |
| Formato | @E 999,999.99 |
| Titulo | Pauta FOB |
| Descrição | Calcular Frete FOB |
| Nível | 1 |
| Usado | Não |
| Obrigatório | Não |
| Help | Indica se haverá cálculo do frete FOB. |

|  |  |
| --- | --- |
| Campo | CFC\_FILIAL |
| Tipo | Caracter |
| Tamanho | <definido pelo cliente> |
| Decimal | 0 |
| Formato | @! |
| Título | Filial |
| Descrição | Filial Corrente |
| Nível | 1 |
| Usado | Não |
| Obrigatório | Não |
| Help | Informe a Filial que utilizará o cadastro. |

| Campo | CFC\_UF |
| --- | --- |
| Tipo | Caracter |
| Tamanho | 2 |
| Decimal | 0 |
| Formato | @! |
| Titulo | UF |
| Descrição | Unidade Federativa |
| Obrigatório | Não |
| Help | Informe a Unidade Federativa que utilizará o cadastro. |

|  |  |
| --- | --- |
| Campo | CFC\_UFORIG |
| Tipo | Caracter |
| Tamanho | 2 |
| Decimal | 0 |
| Formato | @! |
| Título | UF Origem |
| Descrição | UF Origem |
| Usado | Sim |
| Obrigatório | Sim |
| Help | Preencha a unidade da federação de origem da operação. Este campo, junto ao campo CFC\_UFDEST, define a origem e destino da operação para preenchimento dos campos e regras dessa relação. |

|  |  |
| --- | --- |
| Campo | CFC\_UFDEST |
| Tipo | Caracter |
| Tamanho | 2 |
| Decimal | 0 |
| Formato | @! |
| Título | UF Destino |
| Descrição | UF Destino |
| Nível | 1 |
| Usado | Sim |
| Obrigatório | Sim |
| Help | Preencha a unidade da federação de destino da operação. Este campo, junto ao campo CFC\_UFORIG, define a origem e destino da operação para preenchimento dos campos e regras dessa relação. |

|  |  |
| --- | --- |
| Campo | CFC\_CODPRD |
| Tipo | Caracter |
| Tamanho | Tamanho definido através do grupo de campos de código de produto. |
| Formato | @! |
| Título | Cod. Prod. |
| Descrição | Código do Produto |
| Nível | 1 |
| Usado | Sim |
| Obrigatório | Não |
| Help | Quando um produto possuir uma regra diferente da regra cadastrada utilizando apenas Uf de Origem e Destino, preencha este campo com o código do produto que possui as regras específicas. |

|  |  |
| --- | --- |
| Campo | CFC\_ALQFCP |
| Tipo | Numérico |
| Tamanho | 7 |
| Decimal | 4 |
| Formato | @E 99.9999 |
| Título | Alíq. FECP |
| Descrição | Alíquota do FECP |
| Nível | 1 |
| Usado | Sim |
| Obrigatório | Não |
| Help | Preencha o percentual do Fundo de Combate a Pobreza em relação à unidade da Federação de Destino. |

|  |  |
| --- | --- |
| Campo | CFC\_IDHIST |
| Tipo | Caracter |
| Tamanho | 20 |
| Decimal | 0 |
| Formato | @! |
| Título | Id Hist. |
| Descrição | ID Histórico |
| Nível | 1 |
| Usado | Não |
| Obrigatório | Não |

|  |  |
| --- | --- |
| Campo | CFC\_DESCR1 |
| Tipo | Caracter |
| Tamanho | 30 |
| Decimal | 0 |
| Formato | @! |
| Título | Desc. Prod. |
| Descrição | Descrição do Produto |
| Nível | 1 |
| Usado | Não |
| Obrigatório | Não |
| Help | Campo de descrição do produto. |

|  |  |
| --- | --- |
| Campo | CFC\_MGLQST |
| Tipo | Numérico |
| Tamanho | 6 |
| Decimal | 2 |
| Formato | @E 999.99 |
| Título | Mar. Liq. ST |
| Descrição | Margem Líquida ST |
| Nível | 1 |
| Usado | Não |
| Obrigatório | Não |
| Help | Preencha a Margem para cálculo de ICMS ST Líquida. |

|  |  |
| --- | --- |
| Campo | CFC\_ALQSTL |
| Tipo | Numérico |
| Tamanho | 7 |
| Decimal | 4 |
| Formato | @E 99.9999 |
| Título | Alíq. Liq. ST |
| Descrição | Alíquota ST Líquida |
| Nível | 1 |
| Usado | Não |
| Obrigatório | Não |
| Help | Preencha a alíquota para cálculo do ICMS ST Líquido. |

| Campo | CFC\_MVAES |
| --- | --- |
| Tipo | Caracter |
| Tamanho | 1 |
| Decimal | 0 |
| Formato | @! |
| Titulo | MVA Ent/Sai |
| Descrição | MVA na Entrada ou Saída |
| Help | MVA utilizado nas entradas e saídas. |

|  |  |
| --- | --- |
| Campo | CFC\_MARGEM |
| Tipo | Numérico |
| Tamanho | 5 |
| Decimal | 2 |
| Formato | @E 99.99 |
| Título | MVA |
| Descrição | Margem de Valor Agregado |
| Nível | 1 |
| Usado | Sim |
| Obrigatório | Não |
| Help | Informe o percentual de Margem de Valor Agregado. |

|  |  |
| --- | --- |
| Campo | CFC\_ALFCPO |
| Tipo | Numérico |
| Tamanho | 7 |
| Decimal | 4 |
| Formato | @E 99.9999 |
| Título | Alq.Fcp.Ori. |
| Descrição | Alíquota do Fecp da UF Or. |
| Nível | 1 |
| Usado | Sim |
| Obrigatório | Não |
| Help | Preencha o percentual do Fundo de Combate a Pobreza em relação à unidade da federação de Origem. |

|  |  |
| --- | --- |
| Campo | CFC\_FCPAUX |
| Tipo | Numérico |
| Tamanho | 7 |
| Decimal | 4 |
| Formato | @E 99.9999 |
| Título | Ind.Fcp.Aux. |
| Descrição | Índice Auxiliar do Fecp |
| Nível | 1 |
| Usado | Sim |
| Obrigatório | Não |
| Help | Preencha se necessário, o índice Auxiliar para cálculo do Fecp ICMS e/ ou ICMS ST. Utilizado no cálculo de algumas UF's de acordo com a Legislação. |

| Campo | CFC\_FCPINT |
| --- | --- |
| Tipo | Caracter |
| Tamanho | 1 |
| Decimal | 0 |
| Formato | @! |
| Titulo | Op.Int./Imp |
| Descrição | Calc. FECP Oper.Int/Imp. |
| Help | Preencha 1=Sim;2=Não |

|  |  |
| --- | --- |
| Campo | CFC\_FCPXDA |
| Tipo | Caracter |
| Tamanho | 1 |
| Decimal | 0 |
| Formato |  |
| Título | Calc.Dif.Alq |
| Descrição | Cálculo do Fecp – Diferen. Aliq. |
| Nível | 1 |
| Usado | Sim |
| Obrigatório | Não |
| Help | Indica se haverá majoração do FECP na Alíquota do ICMS Diferencial de Alíquotas. |

| Campo | CFC\_NUMCON |
| --- | --- |
| Tipo | Caracter |
| Tamanho | 30 |
| Decimal | 0 |
| Formato | @! |
| Titulo | N.Convênio |
| Descrição | Numero do Convênio |
| Help | informar o numero do convênio |

|  |  |
| --- | --- |
| Campo | CFC\_PRECST |
| Tipo | Caracter |
| Tamanho | 01 |
| Decimal | 0 |
| Formato | @! |
| Título | Pz Rec ST |
| Descrição | Prazo Rec. ST |
| Nível | 1 |
| Usado | Sim |
| Obrigatório | Não |
| Opções | 1=Nao;2=Sim |
| Val. Sistema | Pertence('12') |
| Help | Indica se o Produto faz parte do Decreto Nº 59.967. |

|  |  |
| --- | --- |
| Campo | CFC\_RDCTIM |
| Tipo | Numérico |
| Tamanho | 7 |
| Decimal | 4 |
| Formato | @E 99.9999 |
| Título | % Carg Imp |
| Descrição | % de Carga Trib ICMS |
| Nível | 1 |
| Help | Preencha o percentual de Carga Tributária do ICMS para Importação. Decreto 34.560/2010 |

|  |  |
| --- | --- |
| Campo | CFC\_ADICST |
| Tipo | Numérico |
| Tamanho | 6 |
| Decimal | 2 |
| Formato | @E 999.99 |
| Título | % Adic ST |
| Descrição | Perc. Adic. ST |
| Nível | 1 |
| Help | Informar percentual adicional para estabelecimentos optantes pelo Simples Nacional para Carga Líquida ST. |

 

| Campo | CFC\_VLICMP |
| --- | --- |
| Tipo | Numérico |
| Tamanho | 9 |
| Decimal | 2 |
| Formato | @E 999,999.99 |
| Titulo | ICMS P.Pauta |
| Descrição | Valor ICMS Prop. de Pauta |
| Help | Informar o ICMS próprio de pauta |

 

| Campo | CFC\_VL\_ICM |
| --- | --- |
| Tipo | Numerico |
| Tamanho | 9 |
| Decimal | 2 |
| Formato | @E 999,999.99 |
| Titulo | ICMS Pauta |
| Descrição | Valor do ICMS de Pauta |
| Help | Informar o valor do ICMS de pauta |

|  |  |
| --- | --- |
| Campo | CFC\_PICM |
| Tipo | Numérico |
| Tamanho | 6 |
| Decimal | 2 |
| Formato | @E 999.99 |
| Título | Aliq. ICM. Dest |
| Descrição | Alíquota ICMS de Destino |
| Nível | 1 |
| Help | Informe a alíquota do ICMS de destino |

|  |  |
| --- | --- |
| **Campo** | CFC\_ALFEEF |
| **Tipo** | Numérico |
| **Tamanho** | 5 |
| **Decimal** | 2 |
| **Formato** | @E 99.99 |
| **Título** | Aliq. FEEF |
| **Descrição** | Alíquota FEEF |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| Nível | 1 |
| **Help** | Informe a Alíquota do FEEF. |

[NF-e Implementação da versão 4.00](https://tdn.totvs.com/pages/viewpage.action?pageId=318604074).

 

|  |  |
| --- | --- |
| **Campo** | CFC\_BFCPST |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Bs.FCP ST |
| **Descrição** | Base do FCP - ST |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Opções** | #cBoxBsST() |
| **Help** | Base de cálculo do FCP - ST |

| Campo | CFC\_VL\_ANT |
| --- | --- |
| Tipo | Numérico |
| Tamanho | 9 |
| Decimal | 2 |
| Formato | @E 999,999.99 |
| Titulo | ICMS A. Pauta |
| Descrição | Pauta do ICMS Antecipação |
| Help | Pauta do ICMS Antecipação |

|  |  |
| --- | --- |
| **Campo** | CFC\_BFCPCM |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Bs.FCP Comp. |
| **Descrição** | Base do FCP Complementar |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Opções** | #cBoxBsCMP() |
| **Help** | Base de cálculo do FCP Complementar |

| Campo | CFC\_BFCPPR |
| --- | --- |
| Tipo | Caracter |
| Tamanho | 1 |
| Decimal | 0 |
| Formato | @! |
| Titulo | Bs.FCP Prop. |
| Descrição | Base do FCP - Próprio |
| Help | Informar a base do FCP - Próprio |

|  |  |
| --- | --- |
| **Campo** | CFC\_AFCPST |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Alq.FCP-ST |
| **Descrição** | Alq. do FCP-ST |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Opções** | 1=UfxUf;2=Cliente |
| **Help** | Indica a origem da alíquota do FCP-ST. Opções:  1 = UfxUf (Padrão): Cadastro UfxUf  2 = Cliente: Alíquota informada no campo A1\_PERFECP. Utilizado quando a alíquota variar por CNAE. |

 

* **SS9 – UFxUF**

|  |  |  |  |
| --- | --- | --- | --- |
| Chave | Nome | Modo | PYME |
| SS9 | UFxUF | E | S |

|  |  |
| --- | --- |
| Campo | S9\_FILIAL |
| Tipo | Caracter |
| Tamanho | <definido pelo cliente> |
| Decimal | 0 |
| Formato | @! |
| Título | Filial |
| Descrição | Filial |
| Nível | 1 |
| Usado | Não |
| Obrigatório | Não |

|  |  |
| --- | --- |
| Campo | S9\_UFORIG |
| Tipo | Caracter |
| Tamanho | 2 |
| Decimal | 0 |
| Formato | @! |
| Título | UF Origem |
| Descrição | UF Origem |
| Usado | Sim |
| Obrigatório | Sim |

|  |  |
| --- | --- |
| Campo | S9\_UFDEST |
| Tipo | Caracter |
| Tamanho | 2 |
| Decimal | 0 |
| Formato | @! |
| Título | UF Destino |
| Descrição | UF Destino |
| Nível | 1 |
| Usado | Sim |
| Obrigatório | Sim |

|  |  |
| --- | --- |
| Campo | S9\_CODPRD |
| Tipo | Caracter |
| Tamanho | Tamanho definido através do grupo de campos de código de produto |
| Formato | @! |
| Título | Cod. Prod. |
| Descrição | Código do Produto |
| Nível | 1 |
| Usado | Sim |
| Obrigatório | Não |

|  |  |
| --- | --- |
| Campo | S9\_ALQFCP |
| Tipo | Numérico |
| Tamanho | 7 |
| Decimal | 4 |
| Formato | @E 99.9999 |
| Título | Alíq. FECP |
| Descrição | Alíquota do FECP |
| Nível | 1 |
| Usado | Sim |
| Obrigatório | Não |

 

|  |  |
| --- | --- |
| Campo | S9\_MGLQST |
| Tipo | Numérico |
| Tamanho | 06 |
| Decimal | 2 |
| Formato | @E 999.99 |
| Título | Mar. Liq. ST |
| Descrição | Margem Líquida ST |
| Nível | 1 |
| Usado | Não |
| Obrigatório | Não |

|  |  |
| --- | --- |
| Campo | S9\_ALQSTL |
| Tipo | Numérico |
| Tamanho | 06 |
| Decimal | 2 |
| Formato | @E 99.9999 |
| Título | Alíq. Liq. ST |
| Descrição | Alíquota ST Líquida |
| Nível | 1 |
| Usado | Não |
| Obrigatório | Não |

|  |  |
| --- | --- |
| Campo | S9\_MARGEM |
| Tipo | Numérico |
| Tamanho | 5 |
| Decimal | 2 |
| Formato | @E 99.99 |
| Título | MVA |
| Descrição | Margem de Valor Agregado |
| Nível | 1 |
| Usado | Sim |
| Obrigatório | Não |

|  |  |
| --- | --- |
| Campo | S9\_ALFCPO |
| Tipo | Numérico |
| Tamanho | 7 |
| Decimal | 2 |
| Formato | @E 99.9999 |
| Título | Alq.Fcp.Ori. |
| Descrição | Alíquota do Fecp da UF Or. |
| Nível | 1 |
| Usado | Sim |
| Obrigatório | Não |

|  |  |
| --- | --- |
| Campo | S9\_FCPAUX |
| Tipo | Numérico |
| Tamanho | 7 |
| Decimal | 2 |
| Formato | @E 99.9999 |
| Título | Ind.Fcp.Aux. |
| Descrição | Índice Auxiliar do Fecp |
| Nível | 1 |
| Usado | Sim |
| Obrigatório | Não |

|  |  |
| --- | --- |
| Campo | S9\_FCPXDA |
| Tipo | Caracter |
| Tamanho | 1 |
| Decimal | 0 |
| Formato | @! |
| Título | Calc.Dif.Alq |
| Descrição | Cálculo do Fecp – Diferen. |
| Nível | 1 |
| Usado | Sim |
| Obrigatório | Não |

|  |  |
| --- | --- |
| Campo | S9\_FCPINT |
| Tipo | Caracter |
| Tamanho | 1 |
| Decimal | 0 |
| Formato | @! |
| Título | Oper.Interna |
| Descrição | Cálculo do Fecp - Interna |
| Nível | 1 |
| Usado | Sim |
| Obrigatório | Não |

 

|  |  |
| --- | --- |
| Campo | S9\_PRECST |
| Tipo | Caracter |
| Tamanho | 01 |
| Decimal | 0 |
| Formato | @! |
| Título | Pz Rec ST |
| Descrição | Prazo Rec. ST |
| Nível | 1 |
| Usado | Sim |
| Obrigatório | Não |

|  |  |
| --- | --- |
| Campo | S9\_RDCTIM |
| Tipo | Numérico |
| Tamanho | 7 |
| Decimal | 4 |
| Formato | @E 99.9999 |
| Título | % Carg Imp |
| Descrição | % de Carga Trib ICMS |
| Nível | 1 |
| Help | Preencha o percentual de Carga Tributária do ICMS para mportação.  Decreto 34.560/2010 |

|  |  |
| --- | --- |
| Campo | S9\_ADICST |
| Tipo | Numérico |
| Tamanho | 6 |
| Decimal | 2 |
| Formato | @E 999.99 |
| Título | % Adic ST |
| Descrição | Perc. Adic. ST |
| Nível | 1 |
| Help | Informar percentual adicional para  estabelecimentos optantes pelo Simples Nacional para Carga Líquida ST. |

 

|  |  |
| --- | --- |
| Campo | SS9\_PICM |
| Tipo | Numérico |
| Tamanho | 6 |
| Decimal | 2 |
| Formato | @E 999.99 |
| Título | Perc.ICM |
| Descrição | [Perc.do](http://perc.do/) ICMS |
| Nível | 1 |
| Help | Informe o percentual do ICMS para Operações internas |

|  |  |
| --- | --- |
| **Tabela** | SS9 |
| **Campo** | SS9\_ALFEEF |
| **Tipo** | Numérico |
| **Tamanho** | 5 |
| **Decimal** | 2 |
| **Formato** | @E 99.99 |
| **Título** | Aliq. FEEF |
| **Descrição** | Alíquota FEEF |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Help** | Informe a Alíquota do FEEF. |

 

Criação de **Gatilhos** no arquivo **SX7 – Gatilhos**:

* Tabela CFC UFx UF:

|  |  |
| --- | --- |
| **Campo** | CFC\_CODPRD |
| **Sequência** | 001 |
| **Conteúdo** | SB1->B1\_DESC |
| **Campo   Destino** | CFC\_DESCR1 |

Criação de **Perguntas** no arquivo **SX1 – Cadastro de Perguntes**:

|  |  |
| --- | --- |
| **Pergunta** | UF Origem |
| **Rotina** | FISA080 |
| **Tipo** | Caracter |

|  |  |
| --- | --- |
| **Pergunta** | UF Destino |
| **Rotina** | FISA080 |
| **Tipo** | Caracter |

|  |  |
| --- | --- |
| **Pergunta** | NCM De: |
| **Rotina** | FISA080 |
| **Tipo** | Caracter |

|  |  |
| --- | --- |
| **Pergunta** | NCM Até: |
| **Rotina** | FISA080 |
| **Tipo** | Caracter |

|  |  |
| --- | --- |
| **Pergunta** | Grupo De: |
| **Rotina** | FISA080 |
| **Tipo** | Caracter |

|  |  |
| --- | --- |
| **Pergunta** | Grupo Até: |
| **Rotina** | FISA080 |
| **Tipo** | Caracter |

|  |  |
| --- | --- |
| **Pergunta** | Produto De: |
| **Rotina** | FISA080 |
| **Tipo** | Caracter |

|  |  |
| --- | --- |
| **Pergunta** | Produto Até: |
| **Rotina** | FISA080 |
| **Tipo** | Caracter |

|  |  |
| --- | --- |
| **Pergunta** | Edita? |
| **Rotina** | FISA080 |
| **Tipo** | Caracter |

|  |  |
| --- | --- |
| **Pergunta** | Origem Produto? |
| **Rotina** | FISA080 |
| **Tipo** | Caracter |

## **Procedimentos para Utilização**

  

**Detalhamento dos campos disponíveis na tela de cadastro:** 

 

* **UF Origem (CFC\_UFORIG):** Informe a Unidade Federativa de origem da operação.

* **UF Destino (CFC\_UFDEST):**Informe a Unidade Federativa de destino da operação.

* **Cod.Prod. (CFC\_CODPRD)**: Informe o código do produto da operação.

* **Alíq. FECP (CFC\_ALQFCP):**Informe a alíquota do FECP.

* **Desc. Prod. (CFC\_DESCR1):** Este campo exibirá a descrição do produto selecionado
* **Mar.Liq.ST  (CFC\_MGLQST):**Neste campo deve ser informado a Margem para cálculo de de ICMS ST Líquida. O campo Calc.ST Liq.(F4\_STLIQ) precisa estar definido como 1-Sim.
* **% Adic ST (CFC\_ADICST):**Deve ser informado a alíquota para carga líquida de ST apenas para estabelecimentos optante pelo simples nacional. Desta forma a sua utilização vai ocorrer apenas para fornecedores/clientes optante pelo simples. O campo Calc.ST Liq.(F4\_STLIQ) precisa estar definido como 1-Sim e o Mar.Liq.ST  (CFC\_MGLQST) precisa estar preenchido com valor da margem.
* **Perc.ICM  (CFC\_PICM:**Neste campo deve ser informado a Alíquota nas operações de saída

* **Aliq. FEEF:** Neste campo deve ser informado a alíquota do FEEF a ser utilizado para cálculo conforme legislação de cada Estado.

 

Na escrituração do documento fiscal será feita uma consulta na tabela UFxUF (CFC), considerando a UF de origem do documento fiscal, a UF de destino do documento fiscal e o produto utilizado no item do documento. Encontrando um lançamento nesta tabela, as informações disponíveis aqui serão consideradas para o cálculo e escrituração do documento fiscal.

 

O código de produto é opcional neste cadastro, assim, caso exista um lançamento com UF de Origem e UF de Destino sem código de produto, as informações da tabela UFxUF serão válidas para todas as notas fiscais que se enquadrarem nesta combinação de UFs.

![](https://tdn.totvs.com/download/attachments/237372680/image2018-1-19_15-21-6.png?version=1&modificationDate=1516382467000&api=v2)

![](https://tdn.totvs.com/download/attachments/237372680/image2018-1-19_15-21-23.png?version=1&modificationDate=1516382484000&api=v2)

 

As informações poderão ser cadastradas manualmente, registro por registro, ou via processamento em lote, realizado através do facilitador.

**Facilitador** 

Com objetivo de agilizar o cadastro na rotina UFxUF, foi desenvolvido um Facilitador, disponível na opção “**Ações Relacionadas**” desta rotina.  Este facilitador realizará o processamento de cadastro em lote, considerando o filtro e os valores informados pelo usuário por meio das perguntas desta rotina. Abaixo seguem detalhes de preenchimento destas perguntas: 

**UF Origem:** Informe a UF de origem que será gravada.

**UF Destino:** Informe a UF de destino que será gravada.

   

 **Importante**

 Para considerar todas as UFs como destino, basta informar “\*\*” na pergunta **UF Destino**.

 

 **NCM De:**  Informe a NCM inicial que deseja realizar o processamento;

**NCM Até:** Informe a NCM final que deseja realizar o processamento;

 

 **Importante**

Para considerar todas NCMs, basta deixar a pergunta **NCM De** com conteúdo vazio e a pergunta **NCM Até** toda preenchida com letra “Z”.

 

 **Grupo De:** Informe o Grupo de Tributação inicial para o qual deseja realizar o processamento;

 

 **Grupo Até:** Informe o Grupo de Tributação final para o qual deseja realizar o processamento;

 

**Importante**

Para considetar todos os Grupos de Tributação basta deixar a pergunta **Grupo De** com conteúdo vazio e a pergunta **Grupo Até** toda preenchida com letra “Z”.

 

**Produto De:** Informe o código de produto inicial que deverá ser considerado no processamento;

**Produto Até:**Informe o código do produto final que deverá ser considerado no processamento;

**Importante**

Para considerar todos os Códigos de Produto, basta deixar a pergunta **Produto De** com conteúdo vazio e a pergunta **Produto Até** toda preenchida com letra “Z”.

 

 **Edita?**: Por meio desta pergunta será indicado se o processamento do facilitador irá editar ou não um registro, caso ele já exista. Informe as opções disponíveis:

 

**Sim:** Irá editar registro;

**Não:** Não irá editar registro.

**Origem Produto?:**Por meio desta pergunta será validado qual origem do produto deve ser processado.

Após a confirmação destas perguntas, será exibida uma tela com o seguinte campo:

**- Alíquota do FECP**

Neste campo deverá ser informado o valor da alíquota do FECP, que deverá ser gravado na tabela UFxUF para UF destino/origem, NCM, Grupo de Tributação e Produtos informados nas perguntas anteriores.

Exemplos de processamento do Facilitador:

**Exemplo 1**: - Cadastrar alíquota de FECP 2,0000 para operações com origem em SE e destino em RJ, considerando os produtos com códigos entre 1 e 10:

 

Perguntas:

 

|  |  |
| --- | --- |
| UF Origem | SE |
| UF Destino | RJ |
| NCM Até | ZZZZZZZZZZ |
| Grupo Até | ZZZZZZ |
| Produto De | 1 |
| Produto Até | 10 |
| Altera? | 1-SIM |

 

 

Tela com campos disponíveis:

|  |
| --- |
| Alíquota do  FECP |
| 2,0000 |

  

 

 **Exemplo 2:** - Cadastrar alíquota de FECP 3,0000 para operações com origem em TO e destino em CE para todos os códigos de Produtos:

 

Perguntas:

 

|  |  |
| --- | --- |
| UF Origem | TO |
| UF Destino | CE |
| NCM Até | ZZZZZZZZZZ |
| Grupo Até | ZZZZZZ |
| Produto Até | ZZZZZZZZZZZZZZZ |
| Altera? | 1-SIM |

 

 

Tela com campos disponíveis:

 

|  |
| --- |
| Alíquota do FECP |
| 3,0000 |

 

 

 

**Exemplo 3:** - Cadastrar alíquota de FECP 1,0000 para operações com origem na BA e destino para qualquer estado, considerando NCM entre os códigos 27050000 e 27079100:

 

Perguntas:

 

|  |  |
| --- | --- |
| UF Origem | BA |
| UF Destino | \*\* |
| NCM De | 27050000 |
| NCM Até | 27079100 |
| Grupo Até | ZZZZZZ |
| Produto Até | ZZZZZZZZZZZZZZZ |
| Altera? | 1-SIM |

 

 

 Tela com campos disponíveis:

|  |
| --- |
| Alíquota do FECP |
| 1,0000 |

 

 

 **Importante**

 Não será permitida a execução do Facilitador em mais de uma instância.

## **Informações Técnicas**

|  |  |
| --- | --- |
| **Tabelas Utilizadas** | CFC – UF x UF  SS9 – Histórico UF x UF |
| **Rotinas Envolvidas** | FISA080 – UF x UF |
| **Sistemas Operacionais** | Windows®/Linux® |

Link para acesso da documentação completa:   
  
<https://tdn.totvs.com/display/public/PROT/CADUF+-+UFxUF>
