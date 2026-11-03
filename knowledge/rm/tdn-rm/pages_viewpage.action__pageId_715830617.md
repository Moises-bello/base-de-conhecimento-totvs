---
content_hash: 3f47eedd60ac9861b64ea2ee162e6b405723e861d1639e2aef00c313c2b34762
fetched_at: '2026-06-29T00:11:26.173030+00:00'
page_id: '715830617'
product: rm
source: tdn-rm
title: R-2010 - Retenção Contribuição Previdenciária - Serviços Tomados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=715830617
version: 31
---

![](https://tdn.totvs.com/download/thumbnails/715830650/Retornar.png)
]]>#f5f5f5#363636noneR-2010

## **Conteúdo**



## **01. Regras****1**

### **Regras Específicas**

* Para geração desse evento, devem ser selecionados os lançamentos fiscais de entrada que possuem pelo menos um item com INSS informado nos Tributos.
* Caso na Tag vlrRetencao ocorrer diferença de até R$0,05 quando comparado com a Base \* Alíquota o sistema irá assumir o valor da Base \* Alíquota, a fim de evitar rejeições indevidas ao consultar o evento. Este ajuste não acontecerá para valores menores que R$0,01 (Ex: R$0,0063)

falseAgrupamentos

**O Evento R-2010 é agrupado das seguintes formas:**

* Por CNO e CNPJ do Cliente Fornecedor quando o Projeto for Total\Parcial e de Terceiro.
* Por CNO e CNPJ do projeto (**filial** ou **empresa / construtora**responsável pelo CNO).
* Por CNPJ do Cliente Fornecedor quando **não** estiver Projeto associado ao Lançamento Fiscal **ou** quando Campo Indicador de Prestação de Serviço do Projeto for igual a “Não se Aplica” **ou** “em branco” **ou** “Não é obra de construção civil **ou** não está sujeita a matrícula de obra” **ou** o CNO estiver vazio.

Exemplo de Lançamentos Fiscais para o Evento R-2010 (cada exemplo se trata de um caso isolado):

Indicador: Nulo ou Branco ou Não se Aplica ou Não é Obra de Construção Civil...

|  |  |  |
| --- | --- | --- |
| **Projeto: 001**  **CNO: 900003244870 CNPJ Projeto: 44.444.444/0001-91 CNPJ Filial do Movimento: 55.555.555/0001-91** | | |
| **Lanc 1:** Cliente: 11.111.111/0001-91 | **Lan 2:** **Cliente: 22.222.222/0001-91** | **Lan 3:** **Cliente: 33.333.333/0001-91** |

Resultado:

| Evento 1  Lan1  nrInscEstab: 55.555.555/0001-91 cnpjPrestador: 11.111.111/0001-91 |
| --- |
| **Evento 2**  **nrInscEstab: 55.555.555/0001-91** **cnpjPrestador: 22.222.222/0001-91** |
| **Evento 3**  **nrInscEstab: 55.555.555/0001-91** **cnpjPrestador: 33.333.333/0001-91** |

Indicador: Empreitada Parcial ou Total - Tipo de Projeto: Próprio

|  |  |  |
| --- | --- | --- |
| **Projeto: 003**  **CNO: 900003244870 CNPJ Projeto: 44.444.444/0001-91 CNPJ Filial do Movimento: 55.555.555/0001-91** | | |
| **Lanc 1:** Cliente: 11.111.111/0001-91 | **Lan 2:** **Cliente: 22.222.222/0001-91** | **Lan 3:** **Cliente: 33.333.333/0001-91** |

Resultado:

| Evento 1  Lanc 1, Lanc 2 e Lanc 3 Agrupados  nrInscEstab: 900003244870 cnpjPrestador: 44.444.444/0001-91 |
| --- |

|  |  |  |
| --- | --- | --- |
| **Projeto: 004**  **CNO: 900003244870 CNPJ Projeto: VAZIO CNPJ Filial do Movimento: 55.555.555/0001-91** | | |
| **Lanc 1:** Cliente: 11.111.111/0001-91 | **Lan 2:** **Cliente: 22.222.222/0001-91** | **Lan 3:** **Cliente: 33.333.333/0001-91** |

Resultado:

| Evento 1  Não será gerado. |
| --- |

Indicador: Empreitada Parcial ou Total - Tipo de Projeto: Terceiros

|  |  |  |
| --- | --- | --- |
| **Projeto: 003**  **CNO: 512337096978 CNPJ Projeto: 44.444.444/0001-91 CNPJ Filial do Movimento: 55.555.555/0001-91** | | |
| **Lanc 1:** Cliente: 11.111.111/0001-91 | **Lan 2:** **Cliente: 22.222.222/0001-91** | **Lan 3:** **Cliente: 33.333.333/0001-91** |

Resultado:

| Evento 1  Lan1  nrInscEstab: 512337096978 cnpjPrestador: 11.111.111/0001-91 |
| --- |
| **Evento 2**  **nrInscEstab: 512337096978** **cnpjPrestador: 22.222.222/0001-91** |
| **Evento 3**  **nrInscEstab: 512337096978** **cnpjPrestador: 33.333.333/0001-91** |

### **Regras Gerais**

## **02. Exemplo****2**

xmlR-2010


{...}
{...}

{...}
]]>

## **03. Origem dos Dados****3**

Origem-dos-DadostrueevtServTomevtServTom

| Elemento | Elemento Pai | Nível | Descrição | Ocorrência | Elemento Chave | Origem RM |
| --- | --- | --- | --- | --- | --- | --- |
|  | evtServTom | 3 | Informações de identificação do evento | 1-1 |  |  |
|  | evtServTom | 3 | Informações de identificação do contribuinte | 1-1 | tpInsc, nrInsc |  |
| infoServTom | evtServTom | 3 | Serviços Tomados — Cessão de Mão de Obra ou Empreitada | 1-1 |  |  |
|  | evtServTom | 4 | Identificação do Estabelecimento/obra contratante dos Serviços | 1-1 | tpInscEstab,  nrInscEstab | Informações da Filial que efetuou a retenção. |
| idePrestServ | ideEstabObra | 5 | Identificação do prestador de serviços mediante cessão de mão de obra ou empreitada. | 1-1 | cnpjPrestador | Dados do Cliente/Fornecedor associado ao lançamento fiscal da retenção e do próprio lançamento. Este grupo totaliza os valores das notas fiscais informadas no Grupo {nfs} por CNPJ/CNO do prestador. |
|  | idePrestServ | 6 | Notas fiscais | 1-N | serie, numDocto |  |
| infoTpServ | nfs | 7 | Informações sobre os tipos de Serviços constantes da NF | 1-9 | tpServico |  |
|  | idePrestServ | 6 | Informações de processo | 0-50 | tpProcRetPrinc,  nrProcRetPrinc,  codSuspPrinc | Gerar um registro para cada Processo Jud/Admin associado aos lançamentos fiscais do cli/for relacionado no registro anterior que esteja sendo discutido o valor principal do tributo ou ambos, conforme especificação (2.1.2, "f", iii). |
|  | idePrestServ | 6 | Informações de processo | 0-50 | tpProcRetPrinc,  nrProcRetPrinc,  codSuspPrinc | Dados do Cliente/Fornecedor associado ao lançamento fiscal da retenção e do próprio lançamento. Este grupo totaliza os valores das notas fiscais informadas no Grupo {nfs} por CNPJ/CNO do prestador.  Gerar um registro para cada Processo Jud/Admin associado aos lançamentos fiscais do cli/for relacionado no registro anterior que esteja sendo discutido o valor adicional do tributo ou ambos, conforme especificação (2.1.2, "g", iii). |

ideEventoideEventoOrigem-dos-Dados-ideEventoideEstabObraideEstabObraOrigem-dos-Dados-ideEstabObraidePrestServidePrestServOrigem-dos-Dados-idePrestServinfoProcRetPrinfoProcRetPr

Origem-dos-Dados-infoProcRetPr

infoProcRetAdinfoProcRetAd

Origem-dos-Dados-infoProcRetAd

nfsnfs

Origem-dos-Dados-nfs

ideContriideContri

Origem-dos-Dados-ideContri
