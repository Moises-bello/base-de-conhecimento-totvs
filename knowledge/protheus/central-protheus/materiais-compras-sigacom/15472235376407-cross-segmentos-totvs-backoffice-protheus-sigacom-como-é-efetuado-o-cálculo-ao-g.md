---
article_id: 15472235376407
category: Materiais - Compras (SIGACOM)
content_hash: d57b0e82bb21fbb253eef7ae879bde4ef7d47f213204c8d849566bb58e78fb47
fetched_at: '2026-06-28T22:41:15.784324+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como é efetuado o cálculo
  ao gerar NF de Despesa de importação pela rotina MATA119?
type: support-article
updated_at: '2023-06-21T15:02:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15472235376407-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-%C3%A9-efetuado-o-c%C3%A1lculo-ao-gerar-NF-de-Despesa-de-importa%C3%A7%C3%A3o-pela-rotina-MATA119
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15472214973591) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Como é efetuado o cálculo ao gerar NF de Despesa de importação pela rotina MATA119?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Compras - Todas as versões  
  
**Solução**

Nesta documentação estão descritas as regras para o rateio de despesa de importação.

O rateio ou distribuição do valor de despesa entre os itens do  documento é definido pela configuração do parâmetro **MV\_RATDESP**. Os valores de despesa podem ser rateados por valor ou por peso.

Visto que os itens do documento podem possuir configurações fiscais diferentes, a distribuição dos valores de despesa pode afetar o cálculo dos impostos no documento de entrada. 

Abaixo o cálculo que o sistema efetua para rateio de valor de despesa nos itens da nota fiscal.

***((Valor Despesa / Total das Mercadorias) \* Valor Total Item))        → (valor de despesa dividido pelo total das mercadorias, multiplicado pelo total do item)***

*Item       Qtd       Valor Unit       Valor Total        Valor Despesa*  
**001**10             4,50                45,00               37,50  
**002**10            7,50                75,00               62,50

***Valor Despesa**= 100,00 (valor lançado nos perguntes da rotina MATA119 - despesa de importação)*

***(valor de despesa dividido pelo total das mercadorias, multiplicado pelo total do item)***  
100,00        /    120,00                \*     45,00  
100,00        /    120,00                \*     75,00

***Saiba Mais :***

* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual a finalidade do parâmetro MV\_RATDESP ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024655932-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-a-finalidade-do-par%C3%A2metro-MV-RATDESP-?source=search)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
