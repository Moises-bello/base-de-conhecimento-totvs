---
article_id: 360016631111
category: Materiais - Compras (SIGACOM)
content_hash: ddf9e6208b58e1a77a40bba7aa2cd3d7d32585154fbc0d6546375c1765b330ee
fetched_at: '2026-06-28T22:41:09.056326+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Não permite preencher
  Natureza na aba Duplicatas no Documento de Entrada
type: support-article
updated_at: '2022-05-13T11:41:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016631111-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-N%C3%A3o-permite-preencher-Natureza-na-aba-Duplicatas-no-Documento-de-Entrada
---

**Dúvida**

Ao digitar o Documento de Entrada o sistema não permite preencher Natureza na aba Duplicatas no Documento de Entrada  
  
**Ambiente**

Protheus – Compras – A partir da versão 11.80  
  
  
**Solução**

O sistema realiza validação a partir da TES informada no campo D1\_TES no Documento de Entrada.

Se a TES estiver com o campo F4\_DUPLIC = **NÃO**, o sistema não permite digitar a Natureza, pois a Duplicata está relacionada à Natureza, desta forma se não há Duplicata não há Natureza.

Caso o campo esteja com **SIM**, e mesmo assim não seja possível preencher a Condição de Pagamento e a Natureza, é necessário revisar os Gatilhos padrões da tabela **SD1** conforme abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014889151/mceclip0.png)

Verificar também se na TES utilizada as opções do campos "Classe Valor" alterando para "Classe Valor = Não". Caso necessite da utilização de outras opções que não permitam o preenchimento da Natureza e Cond. Pagto na NF, verificar o conceito juntamente ao suporte ao Módulo Fiscal.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
