---
article_id: 28273993434263
category: Materiais - Compras (SIGACOM)
content_hash: 397f325026bbf4481139ab63aa3588852f64693f63e573f79ae539993894a0c4
fetched_at: '2026-06-28T22:41:16.131831+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Protheus - SIGACOM - Conceitos sobre o Processo
  Encomendante - Documento de Entrada
type: support-article
updated_at: '2024-12-04T17:00:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28273993434263-Cross-Segmentos-TOTVS-Backoffice-Protheus-SIGACOM-Conceitos-sobre-o-Processo-Encomendante-Documento-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28273993401239) Tempo aproximado para leitura: **00:02:SS min** **Dúvida**

Conceitos sobre o Processo como Encomendante - Documento de Entrada  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - VERSAO 12  
  
**Solução**

1 - Recebe o Documento de Entrada do fornecedor. Este documento deve utilizar um TES que atualize o estoque (F4\_ESTOQUE = S), sem controlar poder de terceiros (F4\_PODER3 = N).

***Obs.:*** O TES informado nessa etapa, deve conter o campo "Tes Rem. Sim." (Tes Remessa Simbólica - F4\_TESE3) configurado com uma TES de saída, que será a TES utilizada na emissão do documento de Cobertura, esta deve atualizar o estoque (F4\_ESTOQUE = S) e controlar poder de terceiros como remessa (F4\_PODER3 = R). O campo F4\_TESE3 deve ser habilitado, como "Usado", por meio do ambiente Configurador.

2- Vincula o documento recebido do fornecedor com o documento emitido pelo fornecedor para o industrializador, por meio da opção Documento Vinculado > Vínculo > Alterar. No campo "Operação" deve ser selecionado "Encomendante"  
(DH\_OPER = 2). É necessário informar o Industrializador no campo "Cliente" (DH\_CLIENTE) e o número do documento emitido ao industrializador, através dos campos DH\_DOC e DH\_SERIE.

3- Emite Documento de Saída de Cobertura para o industrializador, por meio da opção Documento Vinculado > Cobertura > Documento de Saída. A TES será preenchida automaticamente, conforme a configuração do campo "Tes Rem. Sim.".

4- Recebe o Documento de Entrada do industrializador. Este documento deve utilizar um TES que atualize o estoque (F4\_ESTOQUE = S), e controle poder de terceiros como Devolução (F4\_PODER3 = D).

***Saiba Mais :***

[Industrialização por encomenda](https://tdn.totvs.com/pages/releaseview.action?pageId=440846500)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
