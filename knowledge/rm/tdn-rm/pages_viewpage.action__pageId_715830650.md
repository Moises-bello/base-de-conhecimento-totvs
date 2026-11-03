---
content_hash: c32d36b78bceef49a90246d03970c1014c17288bf4b875c0fa7dae1163a830e8
fetched_at: '2026-06-29T00:11:26.184267+00:00'
page_id: '715830650'
product: rm
source: tdn-rm
title: R-2020 - Retenção Contribuição Previdenciária - Serviços Prestados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=715830650
version: 24
---

![](https://tdn.totvs.com/download/thumbnails/715830650/Retornar.png)
]]>#f5f5f5#363636noneR-2020

## **Conteúdo**



## **01. Regras****1**

### Regras Específicas

* Para geração desse evento devem ser selecionados os lançamentos fiscais de saída que possuem pelo menos um item com o Tributo INSS informado para retenção pelo contratante.
* O Evento deve agrupar todos os lançamentos do período por cliente fornecedor.
* Caso na Tag vlrRetencao ocorrer diferença de até R$0,05 quando comparado com a Base \* alíquota o sistema irá assumir o valor da Base \* alíquota, a fim de evitar rejeições indevidas ao consultar o evento. Este ajuste não acontecerá para valores menores que R$0,01 (Ex: R$0,0063)
* O processo irá agrupar os Eventos por CNO para todos os lançamentos que tem CNO preenchido, e por cliente fornecedor os casos onde o CNO não foi preenchido.

  Exemplo:

  Lan 1:  
  Cliente C0001  
  CNO 123

  Lan 2:  
  Cliente C0002  
  CNO 123

  Lan 3:  
  Cliente C0004  
  CNO em branco

  Lan 4:  
  Cliente C0005  
  CNO em branco

  Lan 5:  
  Cliente C0004  
  CNO em branco

  Lan 6:  
  Cliente C0005  
  CNO 123

  Como resultado:

  Evento 1 Agrupado pelo CNO 123 (Lan1, Lan2, Lan6)  
  Evento 2 Agrupado pelo Cliente C0004 (Lan3, Lan5)  
  Evento 3 Agrupado pelo Cliente C0005 (Lan4)

### Regras Gerais

## **02. Exemplo****2**

xmlR-2020


{...}
{...}

{...}
]]>

## **03. Origem dos Dados****3**

Origem-dos-DadostrueevtServPrestevtServPrest

| Elemento | Elemento Pai | Nível | Descrição | Ocorrência | Elemento Chave | Origem RM |
| --- | --- | --- | --- | --- | --- | --- |
|  | evtServPrest | 3 | Informações de identificação do evento | 1-1 |  |  |
|  | evtServPrest | 3 | Informações de identificação do contribuinte | 1-1 | tpInsc, nrInsc |  |
| infoServPrest | evtServPrest | 3 | Serviços Tomados — Cessão de Mão de Obra ou Empreitada | 1-1 |  |  |
|  | evtServPrest | 4 | Identificação do Estabelecimento/obra contratante dos Serviços | 1-1 | tpInscEstab,  nrInscEstab |  |
| idePrestServ | ideEstabObra | 5 | Identificação do prestador de serviços mediante cessão de mão de obra ou empreitada. | 1-1 | cnpjPrestador |  |
|  | idePrestServ | 6 | Notas fiscais | 1-N | serie, numDocto |  |
| infoTpServ | nfs | 7 | Informações sobre os tipos de Serviços constantes da NF | 1-9 | tpServico |  |
|  | idePrestServ | 6 | Informações de processo | 0-50 | tpProcRetPrinc,  nrProcRetPrinc,  codSuspPrinc | O (Se {vlrTotalNRetPrinc} > 0;  N (Nas demais situações). |
|  | idePrestServ | 6 | Informações de processo | 0-50 | tpProcRetPrinc,  nrProcRetPrinc,  codSuspPrinc | O (Se {vlrTotalNRetAdic} > 0);  N (Nas demais situações). |

ideEventoideEventoOrigem-dos-Dados-ideEventoideEstabPrestideEstabPrestOrigem-dos-Dados-ideEstabPrestinfoProcRetPrinfoProcRetPr

Origem-dos-Dados-infoProcRetPr

infoProcRetAdinfoProcRetAd

Origem-dos-Dados-infoProcRetAd

nfsnfs

Origem-dos-Dados-nfs

ideContriideContri

Origem-dos-Dados-ideContri
