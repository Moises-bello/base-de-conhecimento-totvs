---
content_hash: b11aec43e1805915acb440a1b5c733a8ed06a4391b93ac31e4bb4decbfb9b28a
fetched_at: '2026-06-29T00:05:49.075485+00:00'
page_id: '1036766765'
product: rm
source: tdn-rm
title: Serviço de alíquotas vigentes dos tributos de uma regra tributária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1036766765
version: 1
---

# **Conteúdo**

2

## 1.**O que é**

É um serviço que disponibiliza as alíquotas dos tributos de uma regra tributária vigente.

O valor das alíquotas é o resultado do cálculo obtido a partir das regras aplicadas aos tipos de tributos das regras tributárias.

## 2.**Informações necessárias para requisição das alíquotas vigentes**

O serviço espera receber 05 informações que serão utilizadas para encontrar as alíquotas e retorná-las para juntamente a uma lista de tributos:

* CODCOLIGADA: Código da coligada onde a regra tributária está cadastrada.
* IDREGRATRIBUTARIA: Identificador da regra tributária que será utilizada para obtermos os tributos que serão retornados com suas respectivas alíquotas.
* DATAOPERACAO: A data de operação que será utilizada para identificar a regra tributária e as alíquotas vigentes.
* CODETD: Código do estado da operação.
* CODMUNICIPIO: Código do município da operação.

Importante que todas as informações sejam passadas, pois elas são obrigatórias para resgates das alíquotas.

## 3. **Disponibilização do serviço**

O serviço foi disponibilizado pelo module **FisVigenciaAliquotaMod**, através da interface **IFisVigenciaAliquotaMod**.

A requisição retorna uma lista de tributos, que é obtida através da regra tributária informada pelos parâmetros de entrada de coligada e do identificador da regra tributária, respectivamente: CODCOLIGADA e IDREGRATRIBUTARIA.

## 4. **Objeto de retorno do serviço**

O serviço retornará uma lista de tributos, representados pelo objeto **FisAliquotaTributoPar**.

Esse objeto irá conter as seguintes informações:

* CODCOLIGADA: Código da coligada da regra tributária.
* IDREGRA: Identificador da regra tributária dos tributos.
* CODTRIBUTO: Código do tributo
* ALIQUOTACHEIA: Valor da alíquota vigente, sem o percentual de redução.
* ALIQUOTAEFETIVA: Valor da alíquota efetiva, considerando o percentual de redução cadastrado junto ao tributo.
* CODETD: Código do estado de operação da alíquota.
* CODMUNICIPIO: Código do município de operação da alíquota.
* DATAINICIAL: Data inicial de vigência da alíquota.
* DATAFINAL: Data final de vigência da alíquota.

## 5.**Regra tributária**

Para utilização de uma regra tributária, será necessária que ela esteja **ativa** e que a data de operação informada **esteja dentro de seu período vigente**.

Para as regras tributárias que não possuem uma data final de vigência, será considerada, somente, a data de início para a verificação de seu período de vigência.

## 6.**Validações consideradas pelo serviço**

1. A data de operação precisa ser uma data válida e maior que o valor de data mínina disponibilizada pelo Datetime.
2. A regra de tributação informada precisa existir na base e estar ativa.
3. A data de operação precisa estar dentro do período vigente da regra tributária e da vigência da alíquota.
4. O local de operação é obrigatório, por isso é necessária a informação do estado e do município de operação.

## 7.**Tipos tributáveis dos tributos**

Os seguintes tipos de tributos não serão tributáveis:

* Não incidência - P
* Isento - I
* Suspenso - U
* Imune - T

Os demais tributos serão tributados e entrarão na regra de cálculo:

* Tributado - N
* Diferido - F

Os tributos que estiverem com a classificação de um tipo de tributo não tributável será retornado com os valores de alíquota cheia e efetiva zerados.

## 8.**Cálculo da alíquota efetiva**

O cálculo da alíquota é baseado no valor da alíquota definida no cadastro de vigências de alíquotas.

O valor da alíquota pode ser obtido por uma alíquota de referência ou por uma específica por estado ou por município.

A alíquota de referência será sempre retornada quando não houver uma alíquota específica por estado ou por município. Caso não haja nenhuma alíquota de referência cadastrada, será retornado um valor zerado.

O valor efetivo da alíquota será o resultado do valor cheio menos a redução definida no tributo.

**Exemplo:**

27 = 30 - 10%

*Valor efetivo = Valor cheio - % Redução de alíquota*

## 8.**Versões disponíveis**

Versões disponibilizadas:

* 12.1.2502.264
* 12.1.2506.224
* 12.1.2510.154
* 12.1.2602
