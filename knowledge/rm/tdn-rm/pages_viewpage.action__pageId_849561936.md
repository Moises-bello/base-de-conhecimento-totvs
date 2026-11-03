---
content_hash: 4108b57707c07b0e90d6ef4b1d4835b9608697dfe1e6b63276e9ce4c7f94baaa
fetched_at: '2026-06-29T00:11:53.679306+00:00'
page_id: '849561936'
product: rm
source: tdn-rm
title: DES - Bento Gonçalves
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=849561936
version: 50
---

# Conteúdo

2Conteúdo

# 1. Introdução

O objetivo deste documento é oferecer uma visão geral a respeito da Declaração Eletrônica de Serviços – DES e os processos necessários no sistema de Gestão Fiscal para geração do arquivo para posterior importação no programa da Prefeitura e apuração do ISSQN sendo considerados os lançamentos referente a serviços tomados.

Glossário de termos técnicos e siglas:

* **DES** - Declaração Eletrônica de Serviços.
* **ISSQN** - Imposto sobre Serviços de Qualquer Natureza.
* **NFS-e** - Nota Fiscal de Serviço Eletrônica.

# 2. Regras Gerais

A Prefeitura de Bento Gonçalves sancionou a lei complementar Nº 183, de 27 de dezembro de 2013, Art. 125 sobre a Secretária Municipal de Finanças notificar o contribuinte para fornecer a Declaração de Serviços.

Para cumprir com as obrigações acessórias perante o fisco municipal, as empresas precisam efetuar a declaração de serviços, onde a mesma deve declarar seus documentos fiscais para fins de apuração do ISSQN.

Devem ser informadas na DES as seguintes operações:

a) Todos os serviços tomados e acobertados por documentos fiscais e sujeitos à incidência do ISSQN, devido ou não ao Município de Bento Gonçalves;  
b) Os documentos fiscais Autorizados e Cancelados.

# 3. Geração do arquivo

A geração da DES deve ser executada a partir de Obrigações Acessórias | Gerador de Saídas. Sendo necessário obter o layout mais recente do arquivo "FISLAY0033-DMS-Bento-Gonçalves-RS.Totvsgen" pelo TOTVS Compartilhamento.

O arquivo é gravado no diretório selecionado na tela de geração.

Para a geração do arquivo, devem ser informados:

* Filial;
* Período: Data inicial e final dos lançamentos a serem considerados. Lembrando que se trata de uma rotina mensal;
* Classificações que serão utilizadas para codificação do Município e para o País;
* Gerar Centralizada: Ao marcar este parâmetro, o sistema irá considerar lançamentos de entrada das filiais que possuem a mesma Inscrição Municipal e o mesmo município da filial selecionada. Desmarcado, será gerado apenas informações da filial informada.

As guias de recolhimento do ISSQN deverão ser geradas e obtidas pelos contribuintes e responsáveis tributários por meio do software da DES.

# 4. Seleção de Lançamentos

Serão selecionados os Lançamentos Fiscais conforme regras abaixo.

* Lançamentos de Entrada.
* O Tipo de Documento não deve possuir Código Modelo Documento.
* Tributo ISS deve estar preenchido no Item ou na Situação Tributária.

A data para seleção dos Lançamentos Fiscais de Entrada irá considerar a definição dos parâmetros no TOTVS Gestão Fiscal (Processo 03.02 - "Apuração de Tributos" → 03.02.03 - "ISS" → "Apur. por Filial" **→** Datas Apuração do ISS). As opções são:

* Data de Emissão;
* Data de Entrada/Saída;
* Data de Pagamento/Vencimento.

Utilizando a opção "Data de Pagamento/Vencimento", o sistema se comportará da seguinte forma:

* Se existir integração com sistema de Gestão Financeira, serão selecionados os Lançamentos Fiscais cujo Lançamento Financeiro associado esteja baixado no período informado na tela da rotina (Data de Baixa);
* Se não existir integração com sistema de Gestão Financeira, serão selecionados os Lançamentos Fiscais cuja Data de Vencimento (aba "Dados Financeiros") esteja no período informado na tela da rotina

  **Importante:** A integração se refere ao menu Parâmetros | Integração de Sistemas caso exista integração com o Financeiro o Lançamento deve obrigatoriamente estar integrado e baixado no financeiro para ser considerado na rotina.

Essa parametrização deve ser feita para operação de Entrada.

***Importante!*** Se a Filial estiver parametrizada para utilizar município por item, as informações de Alíquota, Tipo de Recolhimento, Base de Cálculo e Valor do Imposto serão preenchidos conforme os dados informados na aba "Outros Tributos" dos Itens do Lançamento Fiscal. Se a Filial for parametrizada para não usar o município por item, esses campos serão preenchidos conforme os dados informados na aba "Outros Tributos" do Lançamento Fiscal.

# 5. Registros

A geração dos demais Registros da DES será realizada conforme layout da ABASE Sistemas e Soluções. Neste layout temos dois registros especificamente o registro de Identificação do Documento Fiscal NFS e o registro SER - Identificação do Serviço relacionado ao Documento Fiscal.

registrosregistro-NFSRegistro NFS2

Registro NFS -Registro de Identificação do documento fiscal NFS

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Ordem** | **Tipo** | **Tamanho** | **Obrigação** | **Origem dos dados** |
| 001 | S | - | Sim | Valor Fixo - (NFS) |
| 002 | N | 4 | Sim | Ano de Exercício Data definida nos parâmetros do relatório no Gerador |
| 003 | N | 4 | Sim | Código do modelo do lançamento fiscal no tipo de documento fiscal |
| 004 | N | 4 | Sim | Código de Série do lançamento fiscal |
| 005 | S | 14 | Sim | CPF ou CNPJ do Prestador do Serviço |
| 006 | DT | 20 | Sim | Data de Emissão do Doc. Fiscal no lançamento |
| 007 | N | 15 | Sim | Número do Documento |
| 008 | D | 10,2 | Sim | Valor Contábil do Documento |
| 009 | S | 2 | Sim | Mês de Competência |
| 010 | N | 1 | Sim | Fixar 1 - Serviços contratados |
| 011 | S | 14 | Sim | CPF ou CNPJ do Tomador de Serviço no caso da Filial |
| 012 | N | 1 | Sim | **Fixar 1- Emitido** |
| 013 | S | 300 | Não | **Observação** da Situação tributária - Situação Tributária | Informações Adicionais | Outros Dados | Observação |
| 014 | N | 1 | Sim | Se o campo "Optante pelo Simples" estiver marcado, no menu Tributos do Cadastro do Cliente/Fornecedor, receberá valor "**S - Sim**", senão recebe "**N - Não**". |
| 015 | D | 10,2 | Sim | Valor do ISS |
| 016 | D | 10,2 | Sim | Valor Tributável |
| 017 | D | 10,2 | Sim | Valor das Deduções |
| 018 | D | 10,2 | Sim | Valor dos Descontos |
| 019 | N | 2 | Sim | Código da Situação Tributária da Declaração do Serviço obedecendo legenda do Manual e verificando o tipo de recolhimento do tributo e regime de iss do clifor. |

registro-SER Registro SER2

Registro SER - Identificação do Serviço Relacionado ao Documento Fiscal

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Ordem** | **Tipo** | **Tamanho** | **Obrig.** | **Origem dos Dados** |
| 001 | S | - | Sim | Descrição dos Dados Importados (NFS) |
| 002 | S | 14 | Sim | CPF ou CNPJ do Prestador do Serviço |
| 003 | N | 15 | Sim | Número do Documento do lançamento Fiscal |
| 004 | S | 8 | Sim | .Local de prestação do Serviço |
| 005 | N | 11 | Sim | Código do Item da Lista de Serviços da Lei Complementar 116 |
| 006 | N | 11 | Sim | Código da Atividade (Subserviço) |
| 007 | D | 10.2 | Sim | Alíquota |
| 008 | D | 10.2 | Sim | Valor do Serviço |
| 009 | S | 2 | Sim | Mês de competência  definido nos parâmetros do relatório no Gerador |
| 010 | N | 4 | Sim | Ano de Exercício Data definida nos parâmetros do relatório no Gerador |

estrutura\_registrosExemplo do Arquivo

NFS;2024;1;0;CNPJPRESTADOR;2024-06-13 09:50:24;8989;818.50;9;1;CNPJTOMADOR;1;ISS RETIDO 06/2024;1;34.79;818.50;0.00;0.00;1;

SER;CNPJPRESTADOR;8989;92420030;10;2;4.25;818.50;9;2024;
