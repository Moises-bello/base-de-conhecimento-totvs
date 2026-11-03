---
article_id: 16301704231831
category: Materiais - Compras (SIGACOM)
content_hash: ce85191aa58c67e528f714ca6dd63d574b0c38c7bea4ff1d61105ee26ef256f3
fetched_at: '2026-06-28T22:41:20.021564+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Lentidão na Contabilização
  da rotina CTBANFE
type: support-article
updated_at: '2023-08-25T10:53:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16301704231831-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Lentid%C3%A3o-na-Contabiliza%C3%A7%C3%A3o-da-rotina-CTBANFE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16301726357527) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Lentidão na Contabilização da rotina CTBANFE

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras Fiscal - Todas as versões

**Solução**Referente a Lentidão na contabilização da CTBANFE abaixo alguns pontos que podem ser verificados e adequados no ambiente em questão, com as devidas validações em em ambiente de homologação:  
   
1 - Primeiramente, pode-se verificar e realizar em um ambiente de homologação uma limpeza nas tabelas de Contraprova CTK e CV3 da Contabilização (que são apenas de contraprova, podendo apenas guardar backup para caso de necessidade) Aqui artigo que menciona as tabelas: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012532692-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTK-CONTABILIZA%C3%87%C3%83O->  
   
   
2 - Outro ponto orientamos a verificação do cadastros de LPs na CT5, verificando se possui alguma customização/fonte customizado no LP ou regra em ADVPL e se tiver realizar um teste com o LP de forma padrão sem customizações e sem regras em ADVPL conforme o exemplo do artigo abaixo de Contabilização:  
[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Contabilização Compras - Quais Lançamentos Padrões e como funciona ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027616491-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Contabiliza%C3%A7%C3%A3o-Compras-Quais-Lan%C3%A7amentos-Padr%C3%B5es-e-como-funciona-?source=search)  
   
   
3 - Caso ainda persista, pode ser verificado o artigo abaixo da Contabilização do Faturamento, com pontos a serem verificado sobre lentidão:  
   
<https://tdn.totvs.com/pages/releaseview.action?pageId=268825968>  
   
Sendo que no caso da CTBANFE do Compras, utilizar as informações:  
 

* No Método 1: o parâmetro **MV\_CNFETHR, no caso da CTBANFE**

 

* No Método 2: usar o parâmetro **MV\_OPTNFE** como ativado, e utilizar o "apelido" das tabelas mencionado como "CTBANFE" e não "CTBANFS" como do Faturamento;

   
   
   
4 - Caso após essas verificações ainda assim persista a lentidão a orientação é realizar o teste em Homologação com os pacotes e artefatos atualizados, dos links abaixo verificando se ainda persiste:  
   
COM: <https://tdn.totvs.com/pages/viewpage.action?pageId=522011099>  
CTB: <https://tdn.totvs.com/pages/releaseview.action?pageId=334342777>  
- LIB Atual -[Logo Guará](https://suporte.totvs.com/portal/p/10098/download?e=989259) | [Harpia](https://suporte.totvs.com/portal/p/10098/download?e=1050526)  
- Appserver - [Lobo Guará](https://suporte.totvs.com/portal/p/10098/download#detail/947528) | [Harpia R.33](https://suporte.totvs.com/portal/p/10098/download#detail/1031460)  
- Smartclient - [Lobo Guará](https://suporte.totvs.com/portal/p/10098/download#detail/947510) | [Harpia R.33](https://suporte.totvs.com/portal/p/10098/download#detail/1032341)

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
