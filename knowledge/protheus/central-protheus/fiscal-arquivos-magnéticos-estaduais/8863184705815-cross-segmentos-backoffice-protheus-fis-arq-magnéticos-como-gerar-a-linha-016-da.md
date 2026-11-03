---
article_id: 8863184705815
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: fa216f5b2ec98acd1290c65809fe69754b0991291eeb675b8619166fb3cb7bbb
fetched_at: '2026-06-28T22:42:08.917058+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 016 da DAPIMG? '
type: support-article
updated_at: '2022-09-14T12:10:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8863184705815-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-016-da-DAPIMG
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) empo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar a **linha 016** - Compras da **DAPIMG**?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Livros Fiscais – A partir da versão 12  
  
**Solução**

A **Linha 16- Compras** da **DAPI MG** é gerada com base nos valores totais das operações do período  lançadas no **livro Registro de Entradas**.  
  
Para que o valor de um documento fiscal componha os valores da **Linha 16**, o lançamento deve atender as condições abaixo:  
  
**1.** Campo **CFOP** do documento de entrada  **Cod. Fiscal - D1\_CF** deve conter  uma das **CFOPS** abaixo: 1101/1102/1111/1113/1116/1117/1118/1120/1121/1122/1124/1125/1126/1401/1403/1501/1651/1652  
  
**2.** Se no campo **Cod. Fiscal - D1\_CF**  for informada a **CFOP 1653** e cadastro da **TES** o Campo **Credita ICMS -** (**F4\_CREDICM**) estiver diferente de **Não.****3.** Se no campo **Cod. Fiscal - D1\_CF** for informado a CFOP **1949** e o campo **Tipo Docto -** **D1\_TIPO** for **Complemento de ICMS.****4.** Se no cadastro da **TES** o Campo **Material de consumo** (**F4\_CONSUMO**) diferente de **Sim.**
