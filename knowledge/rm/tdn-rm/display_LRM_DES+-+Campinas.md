---
content_hash: 1380d968d1e35178d0ef356720dd6cdfe0ed7fe9cb9824b3244001f03c692436
fetched_at: '2026-06-29T00:12:02.249135+00:00'
page_id: '899211970'
product: rm
source: tdn-rm
title: DES - Campinas
type: documentation
url: https://tdn.totvs.com/display/LRM/DES+-+Campinas
version: 4
---

# Conteúdo

2Conteúdo

# 1. Introdução

 A DES é uma rotina municipal cujo objetivo é informar à prefeitura o registro dos serviços prestado e contratados pelas pessoas jurídicas para que possam gerenciar, de forma eficaz, o recolhimento do Imposto sobre Serviços de Qualquer Natureza – ISSQN. Neste documento iremos demonstrar o processo para a extração das informações no Gestão Fiscal para a geração do arquivo e importação no portal da prefeitura de São José dos Campos.

Neste processo o foco é a geração das informações dos serviços tomados e acobertados por documentos fiscais e sujeitos à incidência do ISSQN.

Glossário de termos técnicos e siglas:

* **DES** - Declaração Eletrônica de Serviços.
* **ISSQN** - Imposto sobre Serviços de Qualquer Natureza.
* **NFS-e** - Nota Fiscal de Serviço Eletrônica.

# 2. Regras Gerais

A prefeitura municipal de Campinas através do  DECRETO Nº 15.356 DE 26 DE DEZEMBRO DE 2005 Regulamenta a Lei 12.392, de 20/10/2005, que "Dispõe sobre o Imposto sobre Serviços de Qualquer Natureza - ISSQN e dá outras providências".

Para cumprir as obrigações acessórias conforme o  DECRETO Nº 15.356 DE 26 DE DEZEMBRO DE 2005, CAPÍTULO VII - DAS OBRIGAÇÕES ACESSÓRIAS , § 2º Os contribuintes e responsáveis obrigados ao credenciamento nos sistemas de gestão do ISSQN, nos prazos estabelecidos pela Administração Tributária, deverão emitir e escriturar os documentos fiscais conforme estabelecido nos atos normativos que regulam referidos sistemas, o IMA - Informática de Municípios Associados disponibilizou um layout para importação de lançamentos dos serviços tomados.

O processo é feito através dos lançamentos fiscais de entrada que se encontra no Totvs. Estes lançamentos  serão extraídos utilizando a ferramenta gerador de saídas.  Será gerado um arquivo texto para ser importado no sistema  da prefeitura.

# 3. Geração do arquivo

A geração da DES deve ser executada a partir de Obrigações Acessórias | Gerador de Saídas. Sendo necessário obter o layout mais recente do arquivo "FISLAY0038 - DES-Campinas.TotvsGen" pelo TOTVS Compartilhamento.

O arquivo é gravado no diretório selecionado na tela de geração.

Para a geração do arquivo, devem ser informados:

* Filial;
* Período: Data inicial e final dos lançamentos a serem considerados. Lembrando que se trata de uma rotina mensal;
* Classificações que serão utilizadas para codificação do Município e para o País.

As guias de recolhimento do ISSQN deverão ser geradas e obtidas pelos contribuintes e responsáveis tributários por meio do software da DES.

# 4. Seleção de Lançamentos

A seleção dos Lançamentos Fiscais de Entrada serão feitos conforme os parâmetros informados no TOTVS Gestão Fiscal (Processo 03.02 - "Apuração de Tributos" → 03.02.03 - "ISS" → "Apur. por Filial" **→** Datas Apuração do ISS). As opções são:

* Data de Emissão;
* Data de Entrada/Saída;
* Data de Pagamento/Vencimento.

Utilizando a opção "Data de Pagamento/Vencimento", o sistema se comportará da seguinte forma:

* Se existir integração com sistema de Gestão Financeira, serão selecionados os Lançamentos Fiscais cujo Lançamento Financeiro associado esteja baixado no período informado na tela da rotina (Data de Baixa);
* Se não existir integração com sistema de Gestão Financeira, serão selecionados os Lançamentos Fiscais cuja Data de Vencimento (aba "Dados Financeiros") esteja no período informado na tela da rotina.

Essa parametrização deve ser feita para operação de Entrada, para natureza não fiscal e notas de serviço de outro município.

As informações de Alíquota, Tipo de Recolhimento, Base de Cálculo e Valor do Imposto serão preenchidos conforme os dados informados na aba "Outros Tributos" dos Itens do Lançamento Fiscal .

# 5. Registros

Os demais registros serão gerados de acordo com as regras detalhadas abaixo.

registrosregistro-10Cabeçalho2

### Header

|  |  |  |
| --- | --- | --- |
| **Posição** | **Campo** | **Origem dos Dados** |
| 01 | Identificador do registro | Valor fixo 'H' |
| 02 | Inscrição para indicar empresa | Número da Inscrição Municipal da Filial, GFILIAL.INSCMUN |

registro-tRegistro T2

### Registro T - Serviços Tomados
