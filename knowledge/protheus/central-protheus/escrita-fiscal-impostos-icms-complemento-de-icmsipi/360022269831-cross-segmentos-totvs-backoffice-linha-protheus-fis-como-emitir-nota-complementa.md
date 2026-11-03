---
article_id: 360022269831
category: Escrita Fiscal - Impostos - ICMS - Complemento de ICMS/IPI
content_hash: 6875e7f064ffaa462b2115619265fb885bf0d2633e93c460f556bda6eada237b
fetched_at: '2026-06-28T22:39:21.300714+00:00'
product: protheus
section_id: 1500001538701
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como emitir nota
  Complementar de ICMS e ICMS-ST com base de cálculo?
type: support-article
updated_at: '2024-06-20T15:04:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022269831-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-emitir-nota-Complementar-de-ICMS-e-ICMS-ST-com-base-de-c%C3%A1lculo
---

**Dúvida**Como emitir nota Complementar de ICMS e ICMS-ST com base de cálculo?  
   
 **Ambiente**  
Protheus – Fiscal – A partir da versão 11.80  
  
   
**Solução**

O complemento de ICMS com base de cálculo não será gerado através de um pedido de venda, mas sim através da rotina de inclusão de **Notas Manuais de Saída** (MATA920) pois esta rotina permite a digitação, além da base de cálculo, de outras informações que não estão disponíveis no pedido.

Desta forma, a inclusão de um complemento deverá ser efetuada seguindo os passos abaixo:

1) Acessar a rotina de inclusão de notas fiscais manuais de saída:**Módulo Livros Fiscais -> Atualizações -> Movimentos -> NF Manual Saída.**

2) Selecionar o tipo **"Compl. ICMS"** no combobox de seleção de tipo de documento.

3) Preencher as demais informações do cabeçalho do documento.

4) Informar o produto da NF original (que está sendo complementada), o TES a ser utilizado na operação e os demais dados pertinentes ao item. É necessário que o TES utilizado possua o cálculos de ICMS devidamente configurado.

5) Para vincular o complemento ao documento de origem: Ao editar o campo **"N.F. Original"**, pressione a tecla **<F4>** para que sejam listadas as notas que podem ser complementadas.

6) Após selecionar a nota que será complementada os campos **"N.F. Original"**, **"Serie Orig."** e **"It.Doc. Orig"**. serão preenchidos automaticamente. Estes campos também podem ser informados manualmente.

7) Preencher os valores a serem complementados nos respectivos campos, sendo para o ICMS próprio o campo "**Base ICMS"**e para o ICMS-ST os campos **"Ret. ICMS"**e **"ICMS Solid".**

8) Confirmar a inclusão do documento e efetuar os procedimentos de transmissão à SEFAZ normalmente.

Importante

Este procedimento é obrigatório apenas nos casos em que for necessário informar a base de cálculo. Caso contrário o complemento poderá ser emitido normalmente, através do pedido de venda.

* **Recebendo um Complemento**

No recebimento não houve nenhuma mudança. O complemento deverá ser registrado normalmente, vinculado ao respectivo documento de origem, e a base de cálculo deverá ser informada no campo **"Base ICMS"** (D1\_BASEICM).
