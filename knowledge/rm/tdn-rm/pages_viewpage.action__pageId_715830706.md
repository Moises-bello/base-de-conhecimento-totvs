---
content_hash: 0def96ab616f0f03dc07fcc6ed6fadcf5819b3495b14b4e2881ad914eb5caff3
fetched_at: '2026-06-29T00:11:26.220029+00:00'
page_id: '715830706'
product: rm
source: tdn-rm
title: R-2050 - Comercialização da Produção por Produtor Rural PJ / Agroindústria
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=715830706
version: 29
---

![](https://tdn.totvs.com/download/thumbnails/715830650/Retornar.png)
]]>#f5f5f5#363636noneR-2050

## **Conteúdo**



## **01. Regras****1**

### Regras Específicas

* Para geração desse evento devem ser selecionados os lançamentos fiscais de saída que possuem o Tributo Funrural informado.
* O Evento deve agrupar todos os lançamentos do período por filial.

### Regras Gerais

## **02. Exemplo****2**

xmlExemplo R-2050


{...}
{...}

{...}
]]>ideContri

Utiliza um grupo **ideEstab** específico para este tipo

## **03. Origem dos Dados****3**

DadosevtComProdevtComProd

| Elemento | Elemento Pai | Nível | Descrição | Ocorrência | Elemento Chave | Origem RM |
| --- | --- | --- | --- | --- | --- | --- |
| ideEvento ]]> | evtComProd | 3 | Informações de identificação do evento | 1-1 |  |  |
| ideContri ]]> | evtComProd | 3 | Informações de identificação do contribuinte | 1-1 | tpInsc, nrInsc |  |
| infoComProd | evtComProd | 3 | Informação da Comercialização de Produção | 1-1 |  |  |
| ideEstab ]]> | infoComProd | 4 | Identificação do Estabelecimento/obra contratante dos Serviços | 1-1 | tpInscEstab,  nrInscEstab |  |
| tipoCom ]]> | ideEstab | 5 | Identificação do prestador de serviços mediante cessão de mão de obra ou empreitada. | 1-1 | cnpjPrestador |  |
| infoProc ]]> | ideEstab | 6 | Notas fiscais | 1-N | serie, numDocto |  |

ideEventoideEventoDados-ideEventoideContriideContriideEstabideEstabtipoComtipoCominfoProcinfoProc
