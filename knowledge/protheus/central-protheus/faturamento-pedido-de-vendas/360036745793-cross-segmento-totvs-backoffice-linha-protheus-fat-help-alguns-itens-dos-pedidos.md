---
article_id: 360036745793
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: ff350c5cf05d56ba04d7f90f3a09343c7759084679a80f504bccfbff059fef16
fetched_at: '2026-06-28T22:38:38.376655+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - FAT - Help:  Alguns itens
  dos pedidos não foram gerados pois a Qtd. Vendida e menor que a liberada ou existem
  divergências nos saldos de lote/endereço.'
type: support-article
updated_at: '2022-03-09T17:44:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036745793-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FAT-Help-Alguns-itens-dos-pedidos-n%C3%A3o-foram-gerados-pois-a-Qtd-Vendida-e-menor-que-a-liberada-ou-existem-diverg%C3%AAncias-nos-saldos-de-lote-endere%C3%A7o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:03:00 min**

**Ocorrência**

**Help:** *Alguns itens dos pedidos não foram gerados pois a Qtd. Vendida e menor que a liberada ou existem divergências nos saldos de lote/endereço. Como resolver?*

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048293873/mceclip0.png)  
 **Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento - A partir da versão 11.  
  
**Solução**

Para tratar o help, realize a analise dos campos:

* **C6\_QTDENT** - se esta preenchido com a quantidade superior ao total do pedido, se sim, ajuste o campo **C6\_QTDENT** para a quantidade correta a faturar do pedido;
* Verifique no campo **C9\_QTDLIB** se o item esta sendo faturado integralmente e se preencheu a mesma quantidade da **C6\_ITEM**;
* Verifique no campo **C9\_QTDLIB** se o item esta sendo faturado parcialmente e se preencheu a mesma quantidade da **C6\_ITEM**;
* Analise se os campos **C9\_NFISCAL**, **C9\_SERIENF**, **C9\_BLCRED** E **C9\_BLEST** estão preenchidos corretamente;
* Valide se a quantidade de casas decimais estão divergentes na comparação da **SC6** com a **SC9**, o que pode indicar um arredondamento errado apontando inconsistência na comparação das quantidades liberadas em comparação às faturadas.

Para auxiliar, disponibilizo abaixo a documentação a respeito da alteração de decimais no ambiente de faturamento, apontando as principais tabelas a serem consideradas na alteração de Decimais no Protheus para o módulo de faturamento.

**Saiba Mais: [MP-FAT- Casas decimais no Faturamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115001427308-MP-FAT-Casas-decimais-no-Faturamento?source=search)**
