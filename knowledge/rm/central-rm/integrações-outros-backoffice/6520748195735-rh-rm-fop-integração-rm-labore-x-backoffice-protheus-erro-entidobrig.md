---
article_id: 6520748195735
category: Integrações Outros BackOffice
content_hash: f1a6725505994aca80f637d4dee4f5a34298d351370e05e723c95333b1bf40f7
fetched_at: '2026-06-28T22:46:42.142559+00:00'
product: rm
section_id: 4410716084503
source: central-rm
title: 'RH - RM - FOP - Integração RM Labore x BackOffice Protheus: Erro ENTIDOBRIG'
type: support-article
updated_at: '2025-02-10T12:12:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6520748195735-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Labore-x-BackOffice-Protheus-Erro-ENTIDOBRIG
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:04 min****Ocorrência**Ao realizar a integração do sistema **RM** com o **BackOffice do Protheus**, retorna o erro AJUDA: ENTIDOBRIG e posteriormente o nome da entidade.  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**  
Esse incidente ocorre, pois a parametrização do sistema **Protheus** está com campos obrigatórios que não são levados na integração com o **RM**. Na maioria dos casos o campo não existe no RM.  
  
**Solução**Para solucionar essa ocorrência o Usuário deverá verificar se o **RM** possui o campo para ser enviado no XML e caso não exista, deverá remover a obrigatoriedade do campo no **Protheus** para que seja possível integrar.  
Um exemplo é o campo **CT1\_NATCTA** referente à **Natureza da Conta**. O **RM** por padrão não leva esse campo na integração, caso seja marcada a obrigatoriedade no **Protheus** ele sempre esperará recebê-lo e retornará o erro de ENTIDOBRIG (Entidade obrigatória).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6520402182935/mceclip0.png)

Para identificar quais campos são levados, pode-se obter o **XML de Resposta** da transação que retornou o erro e identificar o campo através das orientações: [RH - RM - FOP - Integração RM Labore x BackOffice Protheus: Obtenção o XML mensagem de Resposta e Transformada no RM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036176914)  
Obtendo o **XML de Resposta** irá mencionar o campo que está ausente de preenchimento ou obrigatório no Protheus e não é levado na integração de forma padrão.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6520518867223/mceclip1.png)
