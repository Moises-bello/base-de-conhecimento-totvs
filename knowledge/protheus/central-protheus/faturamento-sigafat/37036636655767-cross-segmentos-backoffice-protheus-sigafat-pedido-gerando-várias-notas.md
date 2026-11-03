---
article_id: 37036636655767
category: Faturamento (SIGAFAT)
content_hash: 3a5d72a56612a3febdc6a65ef4a6f7bea25e16b350441c453856cb6a594598f2
fetched_at: '2026-06-28T22:36:27.130873+00:00'
product: protheus
section_id: 1500001545362
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Pedido gerando várias notas
type: support-article
updated_at: '2026-01-27T12:17:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37036636655767-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Pedido-gerando-v%C3%A1rias-notas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37036636635799) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Ao preparar um documento de saída pela rotina "Documentos de Saída (**MATA460A**)" são geradas várias notas para o mesmo pedido.  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Devido a nova tag **<**`dPrevEntrega`**>** — que representa a **data prevista de entrega** no cabeçalho da Nota Fiscal Eletrônica (NF-e) — introduzida pela Reforma Tributária (**Nota Técnica "NT 2025.002**"), o sistema passou a validar a **data de entrega** para a geração do documento de saídaquando o campo "**Tipo Frete (C5\_TPFRETE)**" no Pedido de Vendas está preenchido como:

* **C - CIF**
* **T - Por conta terceiros**
* **R - Por conta remetente**

Ao preparar o documento de saída pela rotina "**Documentos de Saída (MATA460A)**" temos 2 opções:

* **1 -** **Parâmetro "Data de Entrega?" em branco**: Sistema irá considerar o campo **"C6\_ENTREG"** para a geração do documento de saída e preenchimento do campo"**F2\_DTENTR**".  
      **>** Campo **"C6\_ENTREG"** **iguais**: É gerada uma **única nota**, essa data é levada para o campo "**F2\_DTENTR**".  
       **>** Campo **"C6\_ENTREG"** **diferentes**: É gerada **uma nota para cada** "**C6\_ENTREG**", essa data é levada para o campo "**F2\_DTENTR**".
* **2 -** **Parâmetro "Data de Entrega?" preenchido:** Ao preencher o parâmetro "**Data de Entrega?**" no momento de preparar o documento de saída é gerada **uma única nota**, essa data é levada para o campo "**F2\_DTENTR**".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37115013204119)

**Observação:**

Para habilitar ou desabilitar o tratamento da data de entrega prevista na NF utilize o parâmetro [**MV\_LDTENTR**](https://tdn.totvs.com/x/STO_PQ).  
Esse parâmetro estará disponível na próxima **Expedição Contínua do Backoffice com previsão para FEV/26.**

**Dica:**

Existe um ponto de entrada executado na rotina **Documentos de Saída (MATA461)** e no **Pedido de Vendas (MATA410),**permitindo definir a data de entrega no momento de preparar o **Documento de Saída**, conforme documento técnico: [PE MT46DTEN Definir data de entrega nos Documentos de Saída](https://tdn.totvs.com/x/FyaFPQ). Este ponto de entrada foi criado no dia 13/01/2026, por este motivo, é necessário aplicar o pacote a partir dessa data de corte para o ponto funcionar:

O pacote pode ser acessado no endereço:

12.1.2210:<https://r.totvs.io/p/1233690> ;   
12.1.2310:<https://r.totvs.io/p/1233691> ;  
12.1.2410:<https://r.totvs.io/p/1233688> ;   
12.1.2510:<https://r.totvs.io/p/1233689> ;

**Importante validar se há algum pacote disponível com data de corte posterior à 13/01/2026:** [Pacotes de Atualização - Faturamento](https://tdn.totvs.com/x/Iw4dHw)

**Saiba Mais:**

* [**Data prevista de entrega**](https://tdn.totvs.com/x/flCZP)
* [**Cross Segmentos - Backoffice Protheus - SIGAFAT - Help SEMDATA**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37027164084503-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Help-SEMDATA)
