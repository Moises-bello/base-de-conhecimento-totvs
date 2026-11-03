---
article_id: 4410702141719
category: Manutenção de Ativos (SIGAMNT)
content_hash: 6d24d2d6ac9673366804427422ebdc6e5008b342c1d9317c23ad83f8ea463e87
fetched_at: '2026-06-28T22:42:34.318448+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Penhora - MNTA525
type: support-article
updated_at: '2021-10-18T19:24:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410702141719-Manufatura-Linha-Protheus-MNT-Penhora-MNTA525
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)* Tempo aproximado para leitura: **00:01:30 min****Dúvida**Para que serve a rotina **Penhora - MNTA525**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**A rotina **Penhora - MNTA525** permite efetuar o cadastro de uma **Penhora**, que será vinculado a um **Veículo** através da tabela **Bens - ST9** com status **Penhorado**.   
Esta necessidade pode ocorrer quando o **Veículo** é usado como garantia em alguma dívida da empresa. O **Veículo** penhorado não pode ser utilizado para fazer qualquer movimentação no Sistema. Nesta rotina serão apresentadas as informações de **Bem**, **Descrição do bem**, **Placa**, **Status** que pode ser **Penhorado** ou **Liberado de Penhora**, **Data de indicação do veículo**, **Data de entrada da ação**, **Nome do reclamante**, **Advogado**, **Processo**, **Valor do veículo**, **Tipo de ação** que pode ser **Cível**, **Trabalhista**, **Tributária** ou **Recuperação de crédito**, **Data de liberação**, **Valor da ação** e **Descrição**. Na confirmação o programa irá alterar o **Status** do bem para **Veículo Penhorado**.  
  
**Importante**Será necessária a configuração dos parâmetros **MV\_NGSTPHR - Penhora** e **MV\_NGSTLPH - Não penhora**, de acordo com dois s*tatus* cadastrados na rotina **Status - MNTA710**. Lembrando que os *status* poderão ser cadastrados com outros valores, esses são só exemplo:

* **01 - Penhorado**
* **02 - Não penhorado**

Em seguida configure os parâmetros:

1. **MV\_NGSTPHR = 01**
2. **MV\_NGSTLPH = 02**

**Saiba mais**Acesse a documentação completa no *link* [Penhora - MNTA525](https://tdn.totvs.com/pages/viewpage.action?pageId=636958286)*.*
