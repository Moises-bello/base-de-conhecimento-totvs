---
article_id: 15673083408279
category: Materiais - Compras (SIGACOM)
content_hash: a0c81a96216203818e34d69937e7e284ea1e25833d2aa62049a9a04ea0763d89
fetched_at: '2026-06-28T22:41:16.087251+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como utilizar mais
  de 350 campos na tabela SD1 do Documento de de Entrada ?
type: support-article
updated_at: '2024-05-13T13:28:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15673083408279-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-utilizar-mais-de-350-campos-na-tabela-SD1-do-Documento-de-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15673054815127) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como criar mais de 350 campos em uma tabela?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Compras - Versão 12  
  
**Solução**

Existe um limite máximo de campos por tabela na estrutura do Protheus que no caso é os 350 campos. Pensando nisso, foi disponibilizado uma tabela auxiliar da SD1 que será uma continuação da linha do grid conforme exemplo abaixo:

![](https://totvssuporte.zendesk.com/attachments/token/iTMmGl1iJk5W7MYdXslreGkZ9/?name=image.png)

Para criar campos na tabela DKD siga os procedimentos abaixo:

1-) No modulo configurador( SIGACFG), dar um incluir.     
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23442530012823)

 2-) incluir a tabela DKD.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23442524648727)

3-) Crie os campos na tabela conforme sua necessidade!

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23442530051351)

**Documentação:**  

DT Implementação de Tabela Complementar de itens de NF para facilitar usuário quando criar campos customizados: <https://tdn.totvs.com/pages/viewpage.action?pageId=699820173>  
   
**Importante:**

É necessário atualizar o pacote acumulado do módulo compras, inclusive com dicionário de dados (UPDDISTR), através do link abaixo:

<https://tdn.totvs.com/pages/viewpage.action?pageId=522011099>

**Obs:**

A tabela DKD é uma tabela complementar a SD1, somente campos Usados e Reais que são apresentados em tela, os campos Virtuais não serão apresentados em Tela.

***Saiba Mais:***

[DT Implementação de Tabela Complementar de itens de NF para facilitar usuário quando criar campos customizados](https://tdn.totvs.com/pages/releaseview.action?pageId=699820173)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
