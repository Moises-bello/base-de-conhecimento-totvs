---
article_id: 360007547411
category: Gestão de Transportes (TMS)
content_hash: 1dee300aa115e91b8413c18104a2ff8c59491ecc9481672ff749a36108ef87af
fetched_at: '2026-06-28T22:45:32.510779+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Quebra de manifesto
type: support-article
updated_at: '2021-08-31T11:35:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007547411-Log%C3%ADstica-Linha-Protheus-TMS-Quebra-de-manifesto
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:01:30 min****Dúvida**Quais configurações o Sistema considera para efetuar a **quebra de manifesto**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O Sistema pode gerar vários manifestos para uma mesma viagem, separando por exemplo, por filial de origem ou estado.  
  
Para acessar os parâmetros em questão, é necessário seguir os seguintes passos:

* No **SIGATMS - Gestão de Transportes**, acesse **Atualizações/ Viagens/ Rodoviário Entrega/ Viagens modelo 2 - TMSA144D**;
* Selecionar uma viagem;
* Clique em **Outras Ações/ Manutenção/ Manifesto/ Manifestar**;
* Será apresentada uma tela para que seja informado o **Tipo do Manifesto**. Informar o tipo **Normal** e clicar em **OK**;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044437993/mceclip0.png)

* Após, será apresentada uma segunda tela, onde devem ser configurados os tipos de separação. Estes tipos de separação serão considerados na geração dos manifestos, conforme imagens abaixo. Ajuste conforme necessidade da empresa.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044437173/mceclip0.png)  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043586674/mceclip1.png)

**Importante**Esta ação é necessária para efetuar a alteração da configuração, visto que o tipo de **manifesto normal** e **eletrônico** usam as mesmas configurações porém somente o tipo **normal** está habilitado para apresentar as parametrizações.  
  
Como será gerado um **manifesto normal**, é necessário **estornar/excluir** o mesmo e manifestar novamente colocando como **Tipo do manifesto** igual a **Eletrônico**.  
  
Lembrando que, independente da configuração, sempre haverá a quebra do **MDF-e** por **estado de descarga**, para cumprimento da legislação conforme citado no artigo [Logística - Linha Protheus - TMS - Resumo referente a legislação do MDF-e](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025105632-MP-TMS-Resumo-referente-a-legisla%C3%A7%C3%A3o-do-MDF-e-)
