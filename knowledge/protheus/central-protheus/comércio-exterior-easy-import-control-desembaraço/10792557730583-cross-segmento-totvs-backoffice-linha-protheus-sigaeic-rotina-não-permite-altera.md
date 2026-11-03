---
article_id: 10792557730583
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: dba05c36990ea54ccd2d6309433ac327eff98df3086875db986166383b5452d0
fetched_at: '2026-06-28T22:39:51.383382+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Rotina não permite
  alterar o Incoterm quando há mais de uma Invoice no Embarque
type: support-article
updated_at: '2022-12-12T19:16:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10792557730583-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Rotina-n%C3%A3o-permite-alterar-o-Incoterm-quando-h%C3%A1-mais-de-uma-Invoice-no-Embarque
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Rotina não permite alterar o *Incoterm* quando há mais de uma *Invoice* no Embarque, apresenta o Help:  
  
**Atenção!Neste processo há invoice com incoterm com negociação de seguro e invoice com incoterm sem negociação de seguro. Esta operação não é permitida pelo Siscomex.** ![](https://totvssuporte.zendesk.com/attachments/token/OG1cQnJXjb7L4sdijhuKHc1tP/?name=image.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**A mensagem apresentada é uma restrição decorrente de rateio das despesas entre os itens da adição.  
Atualmente o **SISCOMEX** só permite na mesma DI adições que possuam o mesmo método de valoração e cujo*Incoterms* pertençam ao mesmo grupo. Por grupo de *Incoterms* temos os que possuem seguro previsto (na *Invoice*) (C+I, DPU, CIF, CIP e DAP) e os que não possuem seguro (na *Invoice*) (EXW, FAS, FCA, FOB, C+F, CFR e CPT).  
Ao selecionar o primeiro método de valoração, o Siscomex apresentará a tela abaixo e o importador terá que preencher o seguinte campo:

* **Campo *Incoterm*:** Indicação do termo contratual que define as obrigações e direitos do comprador e do vendedor, em um contrato internacional de compra e venda de mercadoria, de acordo com a tabela *Incoterms*, administrada pela *SECEX* (vide Resolução *Camex* n° 16, de 02 de março de 2020).

***Atenção:***

Por limitação do sistema, na mesma Declaração de Importação *"DI"* não podem ser preenchidas adições com métodos de valoração diferentes, nem serem utilizados *Incoterms* pertencentes a grupos diferentes (vide abaixo a divisão dos grupos de *Incoterms* feita pelo sistema).  
Caso a importação abarque mercadorias com métodos de  valoração diferentes ou contenha faturas com *Incoterms* de grupos diferentes, o importador deverá solicitar o desdobramento do conhecimento de embarque para registrar duas ou mais DI, conforme necessário:  
***Incoterms do GRUPO 1***: EXW, FAS, FCA, FOB, C+F, CFR e CPT  
***Incoterms* do GRUPO 2:** C+I, DPU, CIF, CIP e DAP (possuem seguro embutido no valor negociado).

**Saiba mais**  
[Aba - Valor Aduaneiro](https://www.gov.br/receitafederal/pt-br/assuntos/aduana-e-comercio-exterior/manuais/despacho-de-importacao/sistemas/siscomex-importacao-web/declaracao-de-importacao/funcionalidades/elaborar-uma-nova-solicitacao-de-di/preenchimento-da-di-1/formularios-de-dados-especificos-da-adicao/aba-valor-aduaneiro-1#:~:text=Por%20limita%C3%A7%C3%A3o%20do%20sistema%2C%20na,de%20Incoterms%20feita%20pelo%20sistema)
