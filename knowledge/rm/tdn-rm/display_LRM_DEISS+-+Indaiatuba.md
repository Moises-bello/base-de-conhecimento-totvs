---
content_hash: 5dd0ad51efe41e45e615599ce3d1b1ef17c3c088565c2655e437051d0aa1692d
fetched_at: '2026-06-29T00:09:21.360630+00:00'
page_id: '422545868'
product: rm
source: tdn-rm
title: DEISS - Indaiatuba
type: documentation
url: https://tdn.totvs.com/display/LRM/DEISS+-+Indaiatuba
version: 9
---

## **01. Geração da Rotina**

A rotina municipal Declaração Eletrônica de ISS (DEISS) é gerada através do gerador de saídas. A rotina tem um único registro que será gerado com os dados dos serviços tomados no arquivo "Tomados.txt".  
Para a geração do arquivo, devem ser informados:

* Filial;
* Data inicial e final dos lançamentos a serem considerados. Lembrando que se trata de uma rotina mensal;
* Devem ser informadas, também, as Classificações que serão utilizadas para codificação do Município e para o País;

## **02. Seleção de Lançamentos**

São considerados Lançamentos Fiscais de Entrada onde a filial:

* Estiver parametrizada para utilizar município por item, as informações de Alíquota, Tipo de Recolhimento, Base de Cálculo e Valor do Imposto serão preenchidos conforme os dados informados na aba "Outros Tributos" dos Itens do Lançamento Fiscal.
  + Se a Filial for parametrizada para não usar o município por item, esses campos serão preenchidos conforme os dados informados na aba "Outros Tributos" do Lançamento Fiscal.

Não são considerados:

* Lançamentos Estornados e para o Estado.
* Lançamentos de Serviço tomados cujo prestador é do município de Indaiatuba - SP, conforme regras do layout.

## **03. Parâmetros**

A seleção dos Lançamentos Fiscais de Entrada será feita conforme os parâmetros informados nos parâmetros do TOTVS Gestão Fiscal em: Assistente | Parâmetros | TOTVS Gestão Fiscal | 03.02 - Apuração de Tributos | 03.02.03 - Etapa "Apur. ISS por Filial" - Datas Apuração do ISS.

Essa parametrização deve ser feita para cada tipo de operação:

* Lançamentos de Entrada;
* Lançamentos de Saída - Entidade Privada;
* Lançamentos de Saída - Entidade Pública.

As opções são:

* Data de Emissão;
* Data de Entrada/Saída;
* Data de Pagamento/Vencimento.

Utilizando a opção "Data de Pagamento/Vencimento", o sistema se comportará da seguinte forma:

* Se existir integração com sistema TOTVS Gestão Financeira, serão selecionados os Lançamentos Fiscais cujo Lançamento Financeiro associado esteja baixado no período informado na tela da rotina (Data de Baixa);
* Se não existir integração com sistema TOTVS Gestão Financeira, serão selecionados os Lançamentos Fiscais cuja Data de Vencimento (aba "Dados Financeiros") esteja no período informado na tela da rotina.

Layout da rotina disponível no link: <https://deiss.indaiatuba.sp.gov.br/Deiss/recursos/leiautes/leiaute_escrituracao_2_0_0_3.pdf>
