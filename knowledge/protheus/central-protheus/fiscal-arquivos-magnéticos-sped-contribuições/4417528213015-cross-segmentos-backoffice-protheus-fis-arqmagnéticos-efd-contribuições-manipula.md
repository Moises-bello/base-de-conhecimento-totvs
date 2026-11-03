---
article_id: 4417528213015
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 3abe84df5847a904e24168e46214443d4effc078c92e8acf05945b6b0dd9ca48
fetched_at: '2026-06-28T22:42:05.216593+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Manipulação dos títulos gerados na apuração da EFD Contribuições
type: support-article
updated_at: '2023-01-04T17:24:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417528213015-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Manipula%C3%A7%C3%A3o-dos-t%C3%ADtulos-gerados-na-apura%C3%A7%C3%A3o-da-EFD-Contribui%C3%A7%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **3****min** **Dúvida**Qual Ponto de Entrada permite a manipulação dos dados na tabela SE2 ao gerar o título através da apuração da EFD Contribuições/FISA001 ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIS - Todas as versões  
  
**Solução**

O ponto de entrada **CPCpoAdc** é utilizado para gravar/alterar a tabela SE2.

O mesmo é chamado na rotina **FISA001 Apuração da EFD Contribuições**  no exato momento em que a tabela **SE2 Títulos a Pagar** está aberta em modo de edição pelo sistema.

**Programa Fonte**

FISX001.PRX

**Sintaxe:**

CPCPOADC - Manipula a tabela SE2 no momento em que está aberta pelo sistema, sendo possível incluir ou alterar informações ( [ ExpC1] )

**Parâmetros:**

|  | Nome | Tipo | Descrição | Tamanho | Default |
| --- | --- | --- | --- | --- | --- |
|  | ExpC1 | Caractere | Alias SE2 Contas a Pagar processado no momento | 1 | "SE2" |

**Retorno:**

Nill

**Exemplo**:

![](https://tdn.totvs.com/download/attachments/258277419/image2016-9-21%2015%3A9%3A28.png?version=1&modificationDate=1474481425000&api=v2)

Documentação do Ponto de entrada:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=258277419>
