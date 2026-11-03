---
article_id: 4404184065687
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: afa04365d1bfabbd71b54e3336d0ccea9dd48f03ce31a46128b06137f2ef7b23
fetched_at: '2026-06-28T22:42:06.574007+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  Configuração para não gerar no arquivo txt operações de Entrada/ Aquisição sem direito
  a crédito
type: support-article
updated_at: '2022-11-22T18:31:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404184065687-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Configura%C3%A7%C3%A3o-para-n%C3%A3o-gerar-no-arquivo-txt-opera%C3%A7%C3%B5es-de-Entrada-Aquisi%C3%A7%C3%A3o-sem-direito-a-cr%C3%A9dito
---

**Dúvida**

Como configurar o sistema para não carregar nota de Entrada, "**Aquisição sem direito a crédito**" no arquivo **EFD Contribuições**?  
  
**Ambiente**  
Cross Segmento - Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
1. Para não levar as **Notas Fiscais** sem direito ao crédito **(Entrada/ Aquisição)** para o **EFD Contribuições**, configure os parâmetros conforme abaixo:

**MV\_SKPENC = .T.**  
**MV\_SPEDCSC = .F.**

![sem_cr_dito.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/8551429277975/sem_cr_dito.PNG)

2. Gere o documento de entrada com os campos abaixo do Cadastro de **TES** preenchido:

**PIS/COFINS "F4\_PISCOF"**= Não considera  
**Cred. PIS/COF "F4\_PISCRED"**= Não calcula  
**Sit. Trib, PIS "F4\_CSTPIS"**= 70  
**Sit. Trib. COF "F4\_CSTCOF"**= 70

3. Processe a apuração **Efd Contribuições**, na apuração vai trazer o valor no campo **"Aquisição sem direito a crédito";**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404189444375/mceclip0.png)

Na tabela **SFT** não pode haver base de cálculo e valores de **PIS** e **COFINS** e caso 1 (UM) item da nota tenha **crédito de PIS e COFINS**, então os demais itens (mesmo que não tenha crédito) deverão ser apresentados no **arquivo txt**.
