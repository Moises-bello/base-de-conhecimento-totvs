---
content_hash: a6200c8d7dc609df6d0a9aab6023910e7fd7852c1dc3fa32aed44e60d3c824d2
fetched_at: '2026-06-29T00:08:30.507305+00:00'
page_id: '272696404'
product: rm
source: tdn-rm
title: MDF-e Layout 3.0
type: documentation
url: https://tdn.totvs.com/display/LRM/MDF-e+Layout+3.0
version: 7
---

# MDF-e Layout 3.0

##### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | **RM** | | |
| **Segmento Executor:** | *Construção e Projetos* | | |
| **Módulo:** | *TOTVS Gestão de Estoque, Compras e Faturamento* | | |
| **Rotina:** | MDF-e | | |
| **Chamado/Ticket:** |  | | |
| **Requisito/Story/Issue:** | MATFATCMPCRM01-164 | | |
| **País:** | (Brasil | | |
| **Outros:** |  | | |

### Objetivo

De acordo com o Ato COTEPE/ICMS 29, de 23 de novembro de 2016, até 5 de junho de 2017 é permitida a utilização do MOC – MDF-e, na versão 1.00a para o cumprimento das obrigações previstas no Ajuste SINIEF 21/10. Dessa forma, a partir de 6 de junho de 2017 passa a vigorar o MOC – MDF-e na versão 3.00.

## Definição da Regra de Negócio

Para atender a essa demanda, serão realizadas as seguinte alterações nos parâmetros:

* Nos parâmetros fiscais da Filial (Parâmetros - Gestão de Estoque, Compras e Faturamento -> Integrações -> Fiscal -> Seleciona a Filial)

1. 1. Na Aba "Ambiente MDF-e", mudar o default para 3.00

Será criado um cadastro para seguradoras com os seguintes campos

* CNPJ da seguradora.
* Nome da Seguradora.

Também serão realizadas as seguinte alterações no Movimento.

* Na aba "CT-e", Habilitar o item "Seguro de Carga" para MDF-e.

1. 1. Não exibir o campo "Valor Mercadoria"
   2. Não exibir o campo "Seguradora"
   3. Exibir um lookup para selecionar uma seguradora do Cadastro de Seguradora.

* Na aba CTRC Saida. Será criada uma aba Carga Perigosa para MDF-e.

1. 1. Conterá todos os campos do CT-e exceto o campo "Ponto de Fulgor".
   2. Será possível incluir "n" registros para cada documento associado.

* Na aba CTRC Saida. Será criado um campo para o CIOT assim como para o CPF ou CNPJ do tomador do CT-e
* Na tela de edição do movimento de MDF-e, em Transporte | Identificação, esconder os campos esconder "Tipo de Frete", “Distância”, “Forma de Cálculo do Frete”, “Espécie”, “Natureza dos Volumes” e “Numeração dos Volumes”.
* Na tela de edição do movimento de MDF-e, em CTRC, não exibir as telas “Remetente e Destinatário” e “Outros Dados”.

Tabelas Utilizadas

* TSEGURADORA - Cadastro de Seguradoras. (Tabela nova)
* TMDFECARGAPERIGOSA - Carga Perigosa para documentos associados por MDF-e (Tabela Nova)
* TCTESEGURO - Seguro de Carga para o MDF-e (Tabela já existe)
* TCTECARGAPERIGOSA - Carga Perigosa, de acordo com a ONU, para o MDF-e (Tabela já existe)
* TCTRC - Para preencher o campo CIOT do CT-e vinculado ao MDF-e (Tabela já existe, mas campos CNPJCIOTCTE e CIOTCTE serão criados.

As seguintes Implementações/validações serão feitas na hora do envio do MDF-e

* Não incluir Municípios de Carregamento duplicados na tag infMunCarrega.
* Se o Tipo Emitente for igual a Prestador de Serviço de Transporte (tpEmit=1), será necessário informar o seguro da carga.
* Se o Tipo Emitente for igual a Prestador de Serviço de Transporte (tpEmit=1) e informado grupo de seguro da carga seguintes campos devem ser obrigatórios:

1. 1. CNPJ do Responsável se for pessoa jurídica
   2. Seguradora
   3. Averbação
   4. Número da Apólice

* Não pode existir CPF de condutor informado em duplicidade no grupo veículo tração

As tags que foram alteradas no Layout do XML e que possuem impacto no processo do *TOTVS Gestão de Estoque, Compras e Faturamento,* são as seguintes:

| Grupo infDoc | |
| --- | --- |
| Subgrupo infMunDescarga | |
| infCT | O subgrupo e todas as suas tags foi excluído |
| infNF | O subgrupo e todas as suas tags foi excluído |

OBS: Portanto, no envio do MDF-e, somente documentos de NF-e (Modelo 55) e CT-e (modelo 57) serão aceitos.

| Grupo PERI (grupo novo para Cargas perigosas) | |
| --- | --- |
| nONU | Deve ser informado o número ONU. Tamanho 4. |
| xNomeAE | Deve ser informado o nome para embarque do produto. Tamanho entre 1 e 150. |
| xClaRisco | Deve ser informado a classe e risco secundário. Tamanho entre 1 e 40. |
| grEmb | Deve ser informado o grupo de embalagem. Tamanho entre 1 e 6. |
| qTotProd | Deve ser informado a quantidade total por produto. Tamanho entre 1 e 20. |
| qVolTipo | Deve ser informado a quantidade e o tipo de volumes. Tamanho entre 1 e 60. |

OBS: Esse grupo está vinculado tanto a Notas Fiscais, quanto a CT-es vinculados ao MDF-e

| Grupo SEG (Grupo novo para Seguro de Carga | |
| --- | --- |
| nApol | Número da Apólice. Tamanho entre 1 e 20. |
| nAver | Número da Averbação. Tamanho entre 1 e 40 |
| SubGrupo infResp | |
| respSeg | Responsável pela contratação do serviço de transporte. Opções “Emitente do MDF-e” e “Responsável pela contratação do serviço de transporte (contratante)” |
| CNPJ ou CPF | CNPJ ou CPF do responsável pelo seguro. Obrigatória se o responsável pelo seguro for pessoa jurídica. |
| Subgrupo infSeg | |
| xSeg | Deve ser preenchida com o nome da seguradora. Tamanho entre 1 e 30 |
| CNPJ | Deve ser preenchida com o CNPJ da seguradora |

| Grupo tot(Totalizadores de notas vinculadas) | |
| --- | --- |
| qCT | A tag foi excluída |
| qNF | A tag foi excluída |

| Grupo infCIOT(CIOT de CT-e vinculados ao MDF-e) | |
| --- | --- |
| CIOT | Deve ser preenchido com o número do CIOT informado no CT-e |
| CNPJ ou CPF | Deve ser preenchido com o CNPJ/CPF do Tomador do CT-e. |

| Grupo valePed(Vale Pedágio de CT-e vinculados ao MDF-e) | |
| --- | --- |
| CNPJForn | CNPJ da empresa fornecedora do Vale-Pedágio |
| CNPJPg ou CPFPg | CNPJ do responsável pelo pagamento do Vale-Pedágio |
| nCompra | Número do comprovante de compra |
| vValePed | Valor do Vale Pedágio |
| tpValePed | Tipo do Vale Pedágio |
| categCombVeic | Categoria de Combinação Veicular |

## Procedimento para Utilização

Para utilização do MDF-e 3.0 será necessário parametrizar o sistema para versão 3.0 conforme feito na imagem abaixo:

Para Emitir um MDF-e no layout 3.0 será necessário informar o Seguro de Carga no Movimento, dentro da aba "CT-e -> Seguro de Carga"*.*

Sempre que um CT-e estiver vinculado ao Movimento de MDF-e, deverá ser informado as informações do CIOT.

Quando o documento (NF-e ou CT-e) possuir um produto classificado pela ONU como perigoso, o mesmo deve ser informado no MDF-e

Foi criada uma nova aba dentro da tela de Documentos Associados (CTRC Saida no Movimento) para que sejam informados os Produtos Perigosos.

Podem ser informados quantos produtos perigosos quanto forem necessários.

Quando o documento (CT-e) possuir Vale Pedágio

O processo de envio do MDF-e não sofreu qualquer alteração sendo da mesma forma como era feito na versão 1.0

Os eventos disponíveis (Cancelamento, Inclusão de Condutor e Encerramento) também não sofreram alterações em seus processos.
