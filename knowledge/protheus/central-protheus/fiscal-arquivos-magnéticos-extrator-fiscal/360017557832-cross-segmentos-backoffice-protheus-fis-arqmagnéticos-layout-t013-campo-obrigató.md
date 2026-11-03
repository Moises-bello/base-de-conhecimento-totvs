---
article_id: 360017557832
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: e8a19e02ce539c4321c8ce73367f359e2396bf70ada28f0b3fa084728f5abd5d
fetched_at: '2026-06-28T22:42:07.861401+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Layout T013
  Campo obrigatório não informado: C28_INDCAR'
type: support-article
updated_at: '2022-08-18T17:39:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017557832-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Layout-T013-Campo-obrigat%C3%B3rio-n%C3%A3o-informado-C28-INDCAR
---

**Ocorrência**Erro 1 - Linha: 3 - Coluna: 2   
Campo obrigatório não informado: **(C28\_INDCAR)**  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Causa 1:**

O TAF espera receber o conteúdo do campo **CDF\_TPTRAN** do **Complemento de Coleta e Entrega**, porém este campo não foi preenchido.

**Solução 1:**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse Livros Fiscais -> Atualizações -> Movimentos -> NF Manual de Saída;  
2. Posicione o cursor sobre a nota que o complemento será ajustado;   
3. Acesse Outras Ações -> Complementos -> Locais de Coleta e Entrega;  
4. Preencha o campo **Tp. transp. (CDF\_TPTRAN)**e confirme;  
5. Efetue a extração dos dados e o processamento desta nota para o TAF.

**Causa 2:**Trata-se de uma nota de serviço, porém o **Complemento de Coleta e Entrega**foi preenchido e este conteúdo esta sendo validado pelo TAF.

**Solução 2:**

1. Preencha o campo **B1\_CODISS** para que os campos **FT/F3\_CODISS** sejam gravados, após a escrituração da nota;  
2. Escriture a nota com o cálculo de ISS para que os campos **FT/F3\_TIPO** sejam gravados, após escrituração da nota;  
3. Efetue a extração e processamento dos dados novamente para o TAF.
