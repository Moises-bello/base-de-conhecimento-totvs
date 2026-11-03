---
article_id: 1500012564741
category: Faturamento - Integrações
content_hash: dc62aa8eff534e69ffae16b45e4f5bfe6be737f5c1a17aa81ec9ee9b82a63db3
fetched_at: '2026-06-28T22:38:26.621616+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Invoice  Espelho
  da Nota
type: support-article
updated_at: '2021-05-28T13:57:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012564741-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Invoice-Espelho-da-Nota
---

**Dúvida**Processo de geração do invoce - espelho da nota no faturamento.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**

**Invoice** é processo de envio do espelho da nota.

É possível enviar o Invoice por meio da Neogrid, para isso, é necessário possuir o ***client* da Neogrid instalado.**

Os XML's emitidos após a trnasmissão da nota ficam na pasta **OUT (MV\_NGOUT)** e o ***job da Neogrid*** faz a leitura e a importação do Invoice.

É possível enviar o Invoice também via **TSS.**

**Configurações:**

* **Parâmetros envolvidos:**
  + **MV\_COLESP****:** Exemplo: .T.  
    **[MV\_NGOUT](http://tdn.totvs.com.br/pages/viewpage.action?pageId=184780483)**: Exemplo:\NEOGRID\BIN\OUT
  + MV\_SPEDURL :  [http://LocalHost:8090/](http://spod2757:8080/)
  + **MV\_SPEDCOL**: Exemplo: N
  + **MV\_ESPECIE**: Exemplo: UNI=NF; 1=SPED
  + **MV\_TCNEW:** Documentos que utilizam o novo modelo TOTVS Colab. Onde:**0-todos,1-NFE,2-CTE,3-NFS,4-MDe,5-MDfe,6-Recebimento.**  
    Exemplo: 0.

Obs - Para o Totvs Colaboração 1.0 é necessário configurar o serviço do TSS.

**Utilização**

1. É necessário faturar o pedido emitido por meio do TOTVS Colaboração, acesse: **Atualizações / Pedidos / Pedido de Vendas** > Selecione o pedido, clique em **Ações Relacionadas / Preparar Documento de Saída;**
2. Selecione a Série da nota e confirme;

***Obs: É necessário transmitir a nota:***

![](https://tdn.totvs.com/download/attachments/240976575/image2016-7-1%2014%3A25%3A46.png?version=1&modificationDate=1467390382000&api=v2)

Se a transmissão for bem sucedida, é gerado o arquivo com extensão .XML com a Invoice (Espelho da nota):

![](https://tdn.totvs.com/download/attachments/240976575/image2016-7-1%2014%3A26%3A57.png?version=1&modificationDate=1467390452000&api=v2)

Em anexo, encontra-se o fonte **NFEEspNeo** necessário para tratar o espelho da nota e um modelo de XML do Invoice - Espelho da Nota.

Saiba mais:

**[DI\_Integração\_TOTVS\_Colaboração\_2\_0\_EDI\_de\_Vendas](https://tdn.totvs.com/pages/viewpage.action?pageId=240976575)**
