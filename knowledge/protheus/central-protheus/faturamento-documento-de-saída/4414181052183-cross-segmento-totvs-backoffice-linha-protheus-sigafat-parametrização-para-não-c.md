---
article_id: 4414181052183
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 6dcb48ebb4ca4c4a455825aa13e2d8bf986168cbd838a2224dea042985f783b6
fetched_at: '2026-06-28T22:38:43.902406+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Parametrização
  para não contabilizar a nota de saída
type: support-article
updated_at: '2022-10-25T11:46:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414181052183-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Parametriza%C3%A7%C3%A3o-para-n%C3%A3o-contabilizar-a-nota-de-sa%C3%ADda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como parametrizar para a nota fiscal de saída não ser contabilizada?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**

Existem duas formas de se contabilizar (**CTBANFS**) a nota de saída (**MATA461**):

* **On line**, através dos parâmetros de geração da nota fiscal;
* **Off line**, via miscelâneas, fechamento, contabilização dos documentos de saída;

Para parametrizar para não contabilizar a nota de saída:

* On line:  Desabilite as pergunta Contabiliza On line, deixando conforme o modelo abaixo. Aproveite e também já desabilite as demais perguntas relacionadas a contabilização:![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414180321431/mceclip0.png)
  + Os parâmetros são acionados ao clicar em **prep.docs** do browse do **MATA460A**;
* Off line: Só será contabilizado, se o usuário acionar a rotina, parametrizá-la e clicar em Ok, caso contrário, o sistema não efetua a contabilização off line:![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414180952983/mceclip1.png)  
    
  **\* Importante**  
    
  Por padrão a janela de lançamentos contábeis será apresentada sempre que houver algum problema nos lançamentos da LP que está sendo contabilizada, independente da pergunta "Mostra Lança. Contab.?" estar como não, e que no seu caso está apresentando a mensagem de que as contas de débito e crédito não estão batendo.   
    
  Existem configurações específicas para contornar essa situação, peço que entre em contato com o atendimento do módulo da Contabilidade Gerencial para maiores detalhes.

Para mais informações sobre contabilização, acesse: **[Integração Faturamento X SigaCtb (SIGAFAT)](https://tdn.totvs.com/x/W2nXIQ)**
