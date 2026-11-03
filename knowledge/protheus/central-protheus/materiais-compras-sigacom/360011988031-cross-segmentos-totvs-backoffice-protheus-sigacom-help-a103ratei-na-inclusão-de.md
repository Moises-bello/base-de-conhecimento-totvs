---
article_id: 360011988031
category: Materiais - Compras (SIGACOM)
content_hash: 0f8faf60bc7529b1037731683be691a8cfbc741c36c58e68f33556df19e5d270
fetched_at: '2026-06-28T22:41:08.911643+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help A103RATEI na
  Inclusão de Documento de Entrada '
type: support-article
updated_at: '2024-03-07T20:36:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011988031-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-A103RATEI-na-Inclus%C3%A3o-de-Documento-de-Entrada
---

**Dúvida**

Help A103RATEI na Inclusão / Classificação de Documento de Entrada MATA103

Por que o assistente A103RATEI é apresentado na inclusão / classificação da nota ?

**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
**Solução**

O Help é apresentado quando é informado o Rateio das Entidades Contabeis (**Centros de custo, Conta Contábil, Item Conta e Classe Valor**) em **Outras > Ações >Rateio** do Documento de entrada **(SDE)** e Também tenta informar as entidades contábeis na Linha do Item com o parâmetro **MV\_M103LRA**habilitado.

Caso queira manter as Entidades Comtábeis tanto na linha do item (SD1) quanto em Outras Ações>Rateio (SDE) do Documento de entrada desabilite o parâmetro **MV\_M103LRA = .F.**

Documentação do Parâmetro **MV\_M103LRA**

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como configurar para Apagar ou Não as Entidades Contábeis nos itens do Documento de Entrada ao Informar o Rateio ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061906214-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-configurar-para-Apagar-ou-N%C3%A3o-as-Entidades-Cont%C3%A1beis-nos-itens-do-Documento-de-Entrada-ao-Informar-o-Rateio-?source=search)

Obs: Importante estar com o ambiente atualizado, com data igual OU SUPERIOR nos fontes que trata a validação deste parâmetro (validar em ambiente teste):

<https://suporte.totvs.com/portal/p/10098/download?e=1120996> /  <https://suporte.totvs.com/portal/p/10098/download?e=1119834>  
(Patch possui ajuste quando o cliente utilizava Execauto ou P.E. com uso do parâmetro MV\_M103LRA no processo)

Outra possibilidade da mensagem de erro:

Verifique se os Campos (**Centros de custo, Conta Contábil, Item Conta e Classe Valor)** não constam como obrigatórios no configurador do sistema e caso estejam, verifique se os mesmos estão preenchidos na linha do item ou em Outras Ações >Rateio.

Quando o parâmetro **MV\_M103LRA = .T.**, o sistema não permite que seja declarado rateio na linha do item e no Rateio CC de outras ações. Quando o parâmetro está habilitado, se preenchemos o rateio CC de outras ações e depois preenchemos as entidades contábeis da linha do item, ele gera o help A103RATEI. Se primeiro preenchemos as entidades contábeis da linha do item e, depois, preenchemos o Rateio CC de outras ações, o sistema apaga as entidades contábeis digitadas na linha do item.

***Saiba Mais :***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - MATA103 - A conta contábil informada no pedido de compras é apagada após atualizar (dar enter) o campo D1\_CONTA do documento de entrada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16105701559191-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-MATA103-A-conta-cont%C3%A1bil-informada-no-pedido-de-compras-%C3%A9-apagada-ap%C3%B3s-atualizar-dar-enter-o-campo-D1-CONTA-do-documento-de-entrada?source=search)

[Implementar parâmetro para que ao informar rateio de centro de custo, as informações das entidades contábeis no grid do itens não sejam apagados.](https://tdn.totvs.com/pages/releaseview.action?pageId=592061244)

[MT103LRAT - Rateio de Centro de Custo - Campos do Acols](https://tdn.totvs.com/display/public/PROT/MT103LRAT+-+Rateio+de+Centro+de+Custo+-+Campos+do+Acols)

[MT100GE2 - Complementa a Gravação dos Títulos Financeiros a Pagar](https://tdn.totvs.com/pages/releaseview.action?pageId=6085781)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
