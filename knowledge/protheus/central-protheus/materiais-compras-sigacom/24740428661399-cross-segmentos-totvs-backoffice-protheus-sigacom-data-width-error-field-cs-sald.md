---
article_id: 24740428661399
category: Materiais - Compras (SIGACOM)
content_hash: f5bb8ce59b8485a65a14e0eee29e3fae2790b1430190852268df14e16d48bfce
fetched_at: '2026-06-28T22:41:17.118377+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Data width error -
  Field: CS_SALDO Value: 222222222222.222222 on MAALCDOC(MATXALC.PRX)'
type: support-article
updated_at: '2024-07-09T12:57:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24740428661399-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Data-width-error-Field-CS-SALDO-Value-222222222222-222222-on-MAALCDOC-MATXALC-PRX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24740428634007) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ao tentar eliminar resíduo de pedido de compra está sendo gerado o erorrlog abaixo:

*Data width error - Field: CS\_SALDO Value: 222222222222.222222 on MAALCDOC(MATXALC.PRX)*  
**Ambiente**Protheus – Compras – A partir da versão 12.1.33  
  
**Solução**

O errorlog em questão estaá acusando um estouro de campo, no campo CS\_SALDO, informando que o valor que esta sendo passado por ele não é suportado. O erro *"data width error"* está relacionado ao tamanho/decimais do campo no ambiente.  
  
No errorlog o valor que está passando é de 12 casas antes da virgula e 6 casa após a virgula, porém como pode ver abaixo o campo CS\_SALDO no produto padrão possui 2 casas após a virgula e tamanho 14.

![](https://totvssuporte.zendesk.com/attachments/token/01W8eArxjsHoRwvlZc5YzKQlu/?name=image.png)

Muito possivelmente houve alteração de estrutura, teoricamente para que esse erro não ocorra o campo CS\_SALDO deveria contemplar as características do padrão do print.  
  
IMPORTANTE: Implementar teste primeiramente em ambiente teste homolog observar/ validar os resultados.

O Protheus permite alteração de diversos campos via Configurador no que se refere à tamanho e decimais, de modo a atender a particularidade de cada cliente e sua regra de negócio. No entanto, não há um mapeamento técnico de relacionamento e impacto do aumento para todos os campos do sistema. Para alguns mais usuais e de maior demanda, o Protheus fornece a funcionalidade de [Grupo de Campos](https://centraldeatendimento.totvs.com/hc/article_attachments/24754078702871) que é disponibilizada como facilitadora para rastreamento e alteração em massa pelo Configurador (Em alguns casos também, o relacionamento entre os campos está explícito na SX9).  
  
[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Alteração de Tamanho ou Decimais em campos do Módulo COMPRAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407536919575-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Altera%C3%A7%C3%A3o-de-Tamanho-ou-Decimais-em-campos-do-M%C3%B3dulo-COMPRAS?source=search)

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
* <https://tdn.totvs.com/display/public/framework/MenuDef>
* <https://tdn.totvs.com/pages/releaseview.action?pageId=745762400>
