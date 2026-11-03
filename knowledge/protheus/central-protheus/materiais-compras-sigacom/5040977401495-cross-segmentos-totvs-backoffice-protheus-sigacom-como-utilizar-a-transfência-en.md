---
article_id: 5040977401495
category: Materiais - Compras (SIGACOM)
content_hash: 4c572bdb8142e065cbe6d0b350cd67dab18b2bb4aa93862325953bbcae229684
fetched_at: '2026-06-28T22:41:16.082343+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como utilizar a transfência
  entre filiais na Rotina Central de Compras
type: support-article
updated_at: '2022-10-26T13:57:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5040977401495-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-utilizar-a-transf%C3%AAncia-entre-filiais-na-Rotina-Central-de-Compras
---

**Dúvida**Como utilizar a Transferência entre filiais na Rotina Central de Compras (MATA179)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões

**Solução**Quando o campo **Tp. Sugestão** for "Transferência" nos parâmetros da Central de Compras, a Rotina irá analisar a Necessidade de Reposição das Filiais abastecidas, e sugerir a transferência dos produtos pela filial Distribuidora;

**Requisitos:**

- Cadastrar Matriz de Abastecimento:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5040766730519/mceclip0.png)

**Na Filial Distribuira:**

1) - Cadastre um Cliente utilizando o mesmo **CNPJ** e **Inscrição Estadual** informado no **SIGAMAT** referente a Filial 02 (Ou seja, esse cliente irá representar a Filial 02)

**IMPORTANTE**: Informar uma **Cond. Pagto** na aba **Vendas**;

2) - Cadastre um Fornecedor utilizando o mesmo **CNPJ** e **Inscrição Estadual** informado no **SIGAMAT** referente a Filial 02 (Ou seja, esse cliente irá representar a Filial 02);

**IMPORTANTE**: Informar uma **Cond. Pagto** na aba **Adm/Fin**;

Utilizando o tipo tranferência, ao efetivar uma sugestão gerado pela Central de Compras, o sistema irá gerar automaticamente um Pedido de Venda na Filial distribuidora para o Cliente Representante da Filial 02.

Apos Faturar a NF pela distribuidora, a filial abastecida poderá fazer a entrada da NF emitida.

**Para saber mais sobre Central de Compras acesse nossa pagina no YouTube:**

[How To | MP - SIGACOM - Central de Compras - Metodo de Previsão de Vendas](https://youtu.be/c6yl7zgAZu4)

[How To | MP - SIGACOM - Central de Compras - Método Media de Vendas](https://youtu.be/XwfWQ5Rfw8s)

[How To | MP - SIGACOM - Central de Compras - Médodo Demanda Gerada](https://youtu.be/qm8qJEus_YU)

[How To | MP - SIGACOM - Central de Compras - Transferencia entre filiais](https://www.youtube.com/watch?v=xbL8WIt6nhg)

***Saiba Mais:***

* [Funcionalidde da Central de Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021601092)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
* [HELP MTA179PRD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029046751)
* [MATA295](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053860653-MP-SIGACOM-Como-utilizar-a-rotina-de-Gerar-Demanda-MATA295-)
* [MATA700](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=555278384)
