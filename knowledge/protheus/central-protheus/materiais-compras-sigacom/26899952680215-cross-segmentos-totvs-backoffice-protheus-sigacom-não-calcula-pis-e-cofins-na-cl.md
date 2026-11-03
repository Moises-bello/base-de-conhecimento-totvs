---
article_id: 26899952680215
category: Materiais - Compras (SIGACOM)
content_hash: 335969dc279799b84944397353d11f96287e24f55d53e1d9624c1c9e2bf73636
fetched_at: '2026-06-28T22:41:13.031963+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM -  Não Calcula Pis e
  Cofins na Classificação da Nota Gerada Pelo Módulo SIGAEIC
type: support-article
updated_at: '2024-10-07T19:13:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26899952680215-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-N%C3%A3o-Calcula-Pis-e-Cofins-na-Classifica%C3%A7%C3%A3o-da-Nota-Gerada-Pelo-M%C3%B3dulo-SIGAEIC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26899938083351) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Não Calcula Pis e Cofins na Classificação da Nota Gerada Pelo Módulo SIGAEIC  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Compras - Todas as versões  
  
**Solução**

As informações foram preenchidas corretamente no módulo SIGAEIC e ao gerar a Pré-Nota foram gravado corretamente os impostos nos campos D1\_BASIMP5,D1\_BASIMP6,D1\_VALIMP5,D1\_VALIMP6 , porém , na Classificação do Documento de Entrada não Calcula os impostos.

Uma possibilidade existente dessa situação é a que segue abaixo (***Obs:*** Valide em ambiente de Homologação):

1- Verifique qual o número do pedido de compras que essa NF está amarrada   
   
2- No campo C7\_SEQUEN de uma olhada para verificar se tem alguma informação preenchida.  
   
3- Se o campo C7\_SEQUEN tiver em branco provavelmente esse é o problema.

Para corrigir:

* Marcar o campo C7\_SEQUEN como USADO, nÍvel 1, todos os módulos no configurador do sistema.
* Excluir a pré nota
* Excluir o pedido de compras
* Gerar todo processo Novamente.

***Saiba Mais:***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
