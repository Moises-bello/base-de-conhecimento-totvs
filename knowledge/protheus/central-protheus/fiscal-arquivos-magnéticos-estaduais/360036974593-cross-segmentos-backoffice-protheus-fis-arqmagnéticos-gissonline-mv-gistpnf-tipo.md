---
article_id: 360036974593
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: c82dcbdc23518d9ee3f7a3ce2e1b7fa8e17780463a53c0d2f02668e9bd1ad4b3
fetched_at: '2026-06-28T22:42:11.668352+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - GISSONLINE -
  MV_GISTPNF Tipo da Nota Fiscal Tomador
type: support-article
updated_at: '2022-08-18T14:02:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036974593-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-GISSONLINE-MV-GISTPNF-Tipo-da-Nota-Fiscal-Tomador
---

**Dúvida**  
MV\_GISTPNF:

Relação dos tipos de notas de serviços tomados a serem consideradas para o arquivo da GISS Online

**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

O **MV\_GISTPNF** existe para identificar como deve ser preenchido o campo **TP\_DOC\_NF** da GISS online quando a escrituração for por tipo tomador de serviço e o atual comportamento do Protheus não atende a necessidade da geração do arquivo da GISS online.   
As opções disponíveis no leiaute da GISS online são:

Tipo da Nota Fiscal Tomador:  
1 - Não Retida  
2 - Cancelada  
3 - Anulada  
4 - Isenta  
5 - Retida  
6 - Pagamento pelo prestador  
7 - Imune  
8 - S. Judicial

Ocorre que algumas das opções são semelhantes dentro do Protheus, como por exemplo, "1 - Não Retida" e "6 - Pagamento pelo prestador". Para evitar que a escrituração em lote seja feita de forma incorreta foi criado o parâmetro para que ao identificar a necessidade, o cliente venha alterar o comportamento do Protheus ao gerar o arquivo.  
Assim, as posições do array representam as opções existentes no leiaute e os valores dispostos em cada posição, o novo conteúdo que deve ser adotado na geração do arquivo da GISS online . Caso o array possua suas posições sem conteúdo, indicará ao sistema que deve adotar o comportamento padrão do Protheus.  Caso alguma posição do array possua conteúdo, o sistema irá preencher conforme configuração daquela posição não afetando os outros tipos de notas. Assim temos alguns exemplos:

* Preenchimento na situação onde a opção **"1 - Não Retida"** será considerada pela Prefeitura como **"6 - Pagamento pelo Prestador"** e a opção **"2 - Cancelada"**, será considerada como **"3 - Anulada"** e as demais opções continuarão com seu comportamento padrão:  
  **{“6”,“3”,“”,“”,“”,“”,“”,“”}**
* Preenchimento na situação onde a opção **"1 - Não Retida"** será considerada pela Prefeitura como **"6 - Pagamento pelo Prestador"**e as demais opções continuarão com seu comportamento padrão.

**{“6”,“”,“”,“”,“”,“”,“”,“”}**

 As posições do array não devem ser preenchidas de forma diferente do exemplo acima, ou seja, devem sempre conter um número que referência uma opção do leiaute.

Procedimentos para criar o parâmetro:

**MV\_GISTPNF:**

**Tipo**: Caracter

**Conteúdo**: {“”,“”,“”,“”,“”,“”,“”,“”}

**Descrição**: Relação dos tipos de notas de serviços tomados a serem consideradas para o arquivo da GISS Online.

Link contendo informações sobre o parâmetro MV\_GISTPNF:

<https://tdn.totvs.com/pages/releaseview.action?pageId=185760779>
