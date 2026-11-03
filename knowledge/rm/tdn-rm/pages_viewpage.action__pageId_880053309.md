---
content_hash: afc4b4d82e401dd1c5a435577f9ce366311c97e2ea8e60432e4cd160ebd19a4c
fetched_at: '2026-06-29T00:12:00.073556+00:00'
page_id: '880053309'
product: rm
source: tdn-rm
title: Guia de Visão Geral
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=880053309
version: 34
---

# Conteúdo:

1Conteúdo:

# 1. Sobre

A guia de Visão Geral oferece uma visão consolidada de toda a operação da empresa, a carga tributária incidente e detalhamentos, tanto por participantes, como por produtos e serviços envolvidos.

Os dados necessários para a geração da Visão Geral são provenientes dos Lançamentos Fiscais. São selecionados todos os Lançamentos Fiscais das Coligadas, Filiais e Período filtrados, que não estejam Cancelados ou Estornados.

# 2. Quadros disponíveis na guia

Esta guia apresenta, separadamente as opções de entrada e saída. Para mudar a seleção entre uma e outra, utilize os botões disponíveis na guia.

CardsSimulação

Esta ferramenta permite visualizar o impacto da reforma tributária nas operações da empresa. O objetivo é comparar a carga tributária atual com a futura, após o período de transição.

Fórmula do cálculo:

**Débitos:**

(Valor operacional (Débitos) - Carga tributária atual( Débitos)) \*( Alíquota informada \* (1- Percentual de  Redução))

**Créditos:**

(Valor operacional (Créditos) - Carga tributária atual( Créditos)) \*( Alíquota informada )

O cálculo considera os filtros aplicados.

No primeiro campo digite a alíquota para calcular o Cenário Pós Reforma que serão apresentados com base nos valores do Cenário Atual.

No segundo campo digite o Percentual de redução, este percentual será executado considerando o IVA e  então apresentado no Débito (IBS/CBS) no quadro Cenário Pós Reforma.

Após a seleção da alíquota e do Percentual de Redução será executado o cálculo  conforme fórmula do cálculo listada acima para Débitos e Créditos, e  apresentado no Cenário Pós Reforma.

.

Quadros de valores

Quadro de Entradas (Créditos)

Quadro de Saídas (Débitos)

* **Valor Operacional**: Somatório do Valor de Mercadoria dos Itens dos Lançamentos Fiscais de Entrada ou Saída.

* **Total dos Impostos:**

* + **ICMS:** Somatório do Valor de ICMS, Valor de Diferencial de Alíquota e Valor de ICMS-ST dos Itens dos Lançamentos Fiscais de Entrada ou Saída.

* + **ISS**:Somatório do Valor dos tributos do tipo ISS dos Itens dos Lançamentos Fiscais de Entrada ou Saída.

* + **IPI:** Somatório do Valor de IPI dos Itens dos Lançamentos Fiscais de Entrada ou Saída.

* + **PIS**:Somatório do Valor dos tributos do tipo PIS dos Itens dos Lançamentos Fiscais de Entrada ou Saída.

* + **COFINS**:Somatório do Valor dos tributos do tipo COFINS dos Itens dos Lançamentos Fiscais de Entrada ou Saída.
Mapa Logístico

Através do **Mapa Logístico** é possível visualizar, de forma fácil, onde estão os estabelecimentos da empresa e como estes se localizam em relação aos clientes e fornecedores, permitindo uma análise otimizada da rede de distribuição da empresa.

Na visualização das operações de entrada, as operações serão totalizadas pelo município do Fornecedor (remetente/emitente). Já nas saídas, os valores operacionais serão totalizados pelo município do Cliente (destinatário/adquirente) participante da operação. O valor operacional será sinalizado pelo ícone  *.*Além disso, as filiais envolvidas nas operações serão identificadas através do ícone.

Utilize o scroll do mouse, os botões de + e - disponíveis no próprio mapa ou, ainda, clique nos points para para aumentar ou diminuir o zoom.

Detalhamento das Operações por Participante

Nesta visão, os dados selecionados através do filtro são organizados conforme a localização do participante envolvido, agrupadas por Coligada, Filial e Participante, cliente ou fornecedor, além da carga tributária incidente sobre elas.

O objetivo é facilitar a análise da rede de distribuição e suprimentos da empresa.

Ao abrir a visualização no Smart View, é possível reconfigurar os dados, alterando os agrupamentos, reordenando ou removendo colunas, para criar novas análises e perspectivas. Use sem moderação!

Colunas disponíveis:

* **Coligada:** Código e nome da Coligada da Operação;

* **Filial:** Código e nome da Filial da Operação;

* **País:** Nome do País do Participante da Operação;

* **UF:** Nome do Estado do Participante da Operação;

* **Cidade:** Nome da Cidade do Participante da Operação;

* **Participante:** Código e nome do Participante da Operação, podendo ser um Cliente\Fornecedor ou uma Filial (no caso de transferências, por exemplo);

* **S.N.:** Indicativo se o Participante é inscrito no Simples Nacional;

* **Valor Operacional:** Somatório do Valor de Mercadoria dos Itens dos Lançamentos Fiscais deste Participante para a combinação de Coligada e Filial;

* **ICMS:** Somatório do Valor de ICMS, Valor de Diferencial de Alíquota e Valor de ICMS-ST dos Itens dos Lançamentos Fiscais deste Participante para a combinação de Coligada e Filial;

* **ISS:** Somatório do Valor dos tributos do tipo ISS dos Itens dos Lançamentos Fiscais deste Participante para a combinação de Coligada e Filial;

* **IPI:** Somatório do Valor de IPI dos Itens dos Lançamentos Fiscais deste Participante para a combinação de Coligada e Filial;

* **PIS:** Somatório do Valor dos tributos do tipo PIS dos Itens dos Lançamentos Fiscais deste Participante para a combinação de Coligada e Filial;

* **COFINS:** Somatório do Valor dos tributos do tipo COFINS dos Itens dos Lançamentos Fiscais deste Participante para a combinação de Coligada e Filial;
Detalhamento das Operações por NCM/NBS

Esta visão apresenta os dados selecionados através do filtro agrupados por Coligada, NCM (Nomenclatura Comum do Mercosul), NBS (Nomenclatura Brasileira de Serviços) e Código do Produto/Serviço.

Seu objetivo é fornecer uma visão clara da carga tributária atual para cada produto e serviço comercializado pela empresa.

Colunas disponíveis:

* **Coligada:** Código e nome da Coligada da Operação;

* **NCM/NBS:** Indicativo se o Produto possui NCM (Produto) ou NBS (Serviço);

* **Código:** Código do NCM ou NBS;

* **Código do Produto:** Código do Produto ou Serviço;

* **Valor Operacional:** Somatório do Valor de Mercadoria dos Itens dos Lançamentos Fiscais envolvendo esse Produto para a Coligada em questão;

* **ICMS:** Somatório do Valor de ICMS, Valor de Diferencial de Alíquota e Valor de ICMS-ST dos Itens dos Lançamentos Fiscais envolvendo esse Produto para a Coligada em questão;

* **ISS:** Somatório do Valor dos tributos do tipo ISS dos Itens dos Lançamentos Fiscais envolvendo esse Produto para a Coligada em questão;

* **IPI:** Somatório do Valor de IPI dos Itens dos Lançamentos Fiscais envolvendo esse Produto para a Coligada em questão;

* **PIS:** Somatório do Valor dos tributos do tipo PIS dos Itens dos Lançamentos Fiscais envolvendo esse Produto para a Coligada em questão;
* **COFINS:** Somatório do Valor dos tributos do tipo COFINS dos Itens dos Lançamentos Fiscais envolvendo esse Produto para a Coligada em questão;
0solid

#### [Voltar para o Menu Principal](https://tdn.totvs.com/pages/viewpage.action?pageId=880053215)
