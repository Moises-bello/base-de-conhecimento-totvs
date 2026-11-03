---
article_id: 26292542235159
category: Materiais - Compras (SIGACOM)
content_hash: 43fc3c4088a3033ce8faea26b68e36b1fb039c78ee20c255c4adae9e851302be
fetched_at: '2026-06-28T22:41:24.297854+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual o comportamento
  para gravação do campo C8_OBSM no Processo de Cotação ?
type: support-article
updated_at: '2024-09-11T11:46:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26292542235159-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-o-comportamento-para-grava%C3%A7%C3%A3o-do-campo-C8-OBSM-no-Processo-de-Cota%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26292574650391) Tempo aproximado para leitura: **00:03:00** **Dúvida**Qual o comportamento para gravação do campo ***C8\_OBSM*** (Observação)  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de COmpras - Versão 12

**Solução**

Passo a Passo :

Na geração da cotação, é avaliado o parâmetro ***MV\_SELFOR***

* **MV\_SELFOR = "N"**
  + Observação é composta pela observação informada na solicitação de compras (***C1\_OBS***)
* **MV\_SELFOR = "S"**
  + Observação (***C8\_OBSM***) é composta pela observação informada na solicitação de compras (***C1\_OBS***)
  + Ao inserir um **novo fornecedor**, ao gerar a cotação a observação (***C8\_OBS***), será preenchida com a observação do item da solicitação de compras (***C1\_OBS***) + observação informada por fornecedor
  + Ao utilizar a opção de **replicar**, será perguntado se **"Deseja replicar a observação?"**
    - Se **"Sim"**,  a observação  da cotação do item (***C8\_OBS***) selecionado na replicação será replicado para os demais.
    - Se **"Não"**, será avaliado o parâmetro ***MV\_OBSC1C*** para definir se observação se manterá o já existente no ***C1\_OBS*** de cada produto ou se ficara em branco.
      * Parâmetro: ***MV\_OBSC1C*** (Default = T)
        + T = Usara a observação do campo ***C1\_OBS*** para montar a observação do fornecedor
        + F = Não usara o campo ***C1\_OBS*** para montar a observação do fornecedor deixando em branco.

**Exemplo:**Geração de Cotação com solicitação de compra contendo 3 itens e com os parametro ***MV\_SELFOR = "S"*** e ***MV\_OBSC1C = "T"***.

![](https://tdn.totvs.com.br/download/attachments/836061382/Gif_OBS_2%20%281%29.gif?version=1&modificationDate=1722378356697&api=v2)

***Saiba Mais:***

[Campo Observação C8\_OBSM](https://tdn.totvs.com.br/pages/releaseview.action?pageId=836061382)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
