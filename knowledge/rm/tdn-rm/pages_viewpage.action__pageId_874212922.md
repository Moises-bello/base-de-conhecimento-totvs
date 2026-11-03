---
content_hash: 0ef516a91916f05edde96ffe7f23294423ac01ec117d77b83afaf51a5e38d09f
fetched_at: '2026-06-29T00:11:59.623091+00:00'
page_id: '874212922'
product: rm
source: tdn-rm
title: DES - São José dos Campos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=874212922
version: 19
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

 A LEI Complementar Municipal Nº 272/03 de 18 de dezembro de 2023  dispõe sobre o Imposto Sobre Serviço de Qualquer Natureza - ISSQN, estabelece obrigações acessórias e dá outras providências.

Em substituição aos livros fiscais previstos na legislação vigente, todo prestador que emita nota fiscal de prestação de serviços e todo tomador de serviços ficam obrigados a escriturar eletronicamente, por meio do programa DSF , os fatos geradores do ISSQN, por meio do preenchimento dos seguintes livros fiscais:  
I – Livro de Registro de Prestação de Serviços; e  
II – Livro de Registro de Serviços Tomados de Pessoas Físicas e Jurídicas.

Neste processo de extração dos dados para a geração das informações a prefeitura iremos gerar eletronicamente as informações para atender ao  Livro de Registro de Serviços Tomados de Pessoas Físicas e Jurídicas.

3. Geração do arquivo

A geração da DES deve ser executada a partir de Obrigações Acessórias | Gerador de Saídas. Sendo necessário obter o layout mais recente do arquivo "FISLAY0037 - DES-São-José-Dos-Campos.TotvsGen" pelo TOTVS Compartilhamento.

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

Essa parametrização deve ser feita para operação de Entrada  e serão selecionados lançamentos cuja natureza é não fiscal e notas de serviços de tomadores de outros munícipios.

As informações de Alíquota, Tipo de Recolhimento, Base de Cálculo e Valor do Imposto serão preenchidos conforme os dados informados na aba "Outros Tributos" dos Itens do Lançamento Fiscal. 

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
