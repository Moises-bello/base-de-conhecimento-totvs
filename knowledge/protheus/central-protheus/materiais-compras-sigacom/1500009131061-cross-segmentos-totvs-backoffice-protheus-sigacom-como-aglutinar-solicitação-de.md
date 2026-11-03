---
article_id: 1500009131061
category: Materiais - Compras (SIGACOM)
content_hash: 35b20fd1e8eb28d369985ca14433c3a6f825c34b833333ee501f3682b8dfb399
fetched_at: '2026-06-28T22:41:14.432600+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como Aglutinar Solicitação
  de Compras ?
type: support-article
updated_at: '2026-05-20T17:08:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009131061-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-Aglutinar-Solicita%C3%A7%C3%A3o-de-Compras
---

**Dúvida**  
Como Aglutinar Solicitação de Compras ?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Todas as versões  
  
**Solução**

A rotina de aglutinação de solicitações de compra permite juntar as solicitações de compra de um mesmo produto em uma única solicitação, respeitando a igualdade dos campos **Filial**, **Produto** e **Tipo de OP**.  
Para realizar a aglutinação de solicitações de compra no Protheus, pode ser utilizada a rotina **Aglutinar Solicitações** (MATA126), do módulo de Compras.  
As solicitações de compra são aglutinadas de acordo com o período definido pelo usuário.

* **Diário**: Agrupa as SCs cuja data prevista de entrega seja no mesmo dia.
* **Semanal**: Agrupa as SCs cuja data prevista de entrega esteja dentro de um intervalo de 7 dias, a partir da data mais próxima de entrega prevista.
* **Quinzenal**: Agrupa as SCs cuja data prevista de entrega esteja dentro de um período de 15 dias, a partir da data mais próxima de entrega prevista.
* **Mensal**: Agrupa as SCs cuja data prevista de entrega seja dentro do mesmo mês.
* **Trimestral**: Agrupa as SCs cuja data prevista de entrega caia dentro de um trimestre do ano (meses 1 a 3, 4 a 6, 7 a 9, ou 10 a 12).
* **Semestral**: Agrupa as SCs cuja data prevista de entrega esteja dentro do semestre do ano (meses 1 a 6 ou 7 a 12).

O sistema exibirá uma janela com os parâmetros a serem definidos para realizar a aglutinação das SCs.

Configure os parâmetros conforme necessário e clique em "Ok" para confirmar

***Obs.1:***

Ao efetivar a aglutinação, são geradas novas SCS aglutinadas, o campo observação é preenchido automaticamente com a informação: **SC CRIADA POR AGLUTINAÇÃO e as SCs antigas são excluídas, não havendo um processo de reversão da execução.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9213796623127)![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9213738840855)

***Obs.2:***

A rotina de Aglutinação não possui a funcionalidade de levar as Entidades Contábeis contidas nas SCs selecionadas para serem aglutinadas, para a SC gerada na aglutinação em forma de rateio de entidades contábeis.  
Por Padrão e característica da rotina, a nova SC gerada, fica sem as Entidades Contábeis que estavam contidas nas SCs selecionada para aglutinação.

A opção de Rateio de Centos de Custos da rotina de SC tem sua funcionalidade apenas na rotina de Solicitações de Compras em "Outras Ações" inserindo manualmente as entidades contábeis e os respectivos percentuais, não sendo realizado na rotina de Aglutinação de SCs este processo automático.

***Obs.3:***

Quais são os campos que o sistema valida para amarrar as SC's antigas as que serão Aglutinadas nas atuais?

**R:** O sistema verifica os campos abaixo:

C1\_OP  
C1\_NUM  
C1\_ITEM  
C1\_PRODUTO  
C1\_QUANT  
C1\_QTSEGUM  
C1\_DATPRF  
C1\_OBS  
C1\_SOLICIT  
C1\_EMISSAO" ,ddatabase})  
C1\_TPOP  
C1\_CC  
C1\_CONTA  
C1\_ITEMCTA  
C1\_CLVL  
 C1\_FORNECE  
C1\_LOJA

***Saiba Mais :***

[*Aglutinação de SC's(MATA126 - SIGACOM)*](https://tdn.totvs.com/pages/viewpage.action?pageId=306852172)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
