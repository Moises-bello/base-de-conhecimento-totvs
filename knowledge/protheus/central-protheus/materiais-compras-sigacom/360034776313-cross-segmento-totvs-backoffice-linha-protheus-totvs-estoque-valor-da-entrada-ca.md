---
article_id: 360034776313
category: Materiais - Compras (SIGACOM)
content_hash: 6d9348f921651a5897ca4b2a6e2bbe9eec2268c2fb11b28cc16588416574e4a6
fetched_at: '2026-06-28T22:41:11.802529+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS ESTOQUE - Valor
  da entrada Campo B1_UPRC e BZ_UPRC
type: support-article
updated_at: '2024-12-27T12:55:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034776313-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-ESTOQUE-Valor-da-entrada-Campo-B1-UPRC-e-BZ-UPRC
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28807917717783)** Tempo aproximado para leitura: **00:02 min**  
**Ocorrência**

Documento de Entrada, consulta do valor da última entrada está do campo **B1\_UPRC** e não do campo **BZ\_UPRC**

**Ambiente**

Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Todas as versões

**Causa**

Esse incidente ocorre, pois a parametrização do sistema não está conforme se deseja.  
  
**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

**1. Acessar o configurador;**

**2. No parâmetro** **MV\_ARQPROD**, informar conforme a necessidade, onde este parâmetro configura se os dados de indicadores de produto serão considerados pela tabela "*SB1*" ou "*SBZ*". Neste exemplo o correto é informar SBZ.

**3. No parâmetro****MV\_CADPRO** devera estar preenchido desta forma *"|SA5|SBZ|SB5|DH5|SGI*" ou conforme necessidade. Tem como objetivo informar quais cadastros complementares devem ser apresentados no cadastro de produtos.

**Gravação do campo B1\_UPRC ou BZ\_UPRC deduzindo o valor do desconto;**

Os campos serão atualizados somente se o Documento de Entrada for do tipo Normal ou Complemento de Preço/Frete e o campo F4\_UPRC (Atualiza Preço de Compra) no cadastro da TES estiver configurado para permitir a atualização.

**Dica 1:** Utilize o ponto de Entrada MT103UPC para customizar a gravação dos campos B1\_UPRC/BZ\_UPRC.

**Dica 2:** Utilize essa opção em conjunto com a pergunta 11, (F12) da rotina MATA103.

Pergunta 11. Atualiza ultimo preço por?

Ao atualizar o último preço de compra considerar o preço por data de recebimento ou por data de emissão.

Opção utilizada na gravação dos campos B1\_UCOM/BZ\_UCOM (Data da última compra).

Caso o usuário opite por considerar a data de recebimento, será gravado o conteúdo do campo D1\_DTDIGIT (Data de Digitação), caso o usuário opite por considerar a data de emissão, será gravado o conteúdo do campo D1\_Emissão (Data de Emissão). 

***Saiba Mais :***

* [MP - SIGAEST - Utilidade e configuração do parâmetro MV\_CADPROD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016068032-MP-SIGAEST-Utilidade-e-configura%C3%A7%C3%A3o-do-par%C3%A2metro-MV-CADPROD)
* [Gravação do campo B1\_UPRC ou BZ\_UPRC deduzindo o valor do desconto.](https://tdn.totvs.com/x/cP04E)
