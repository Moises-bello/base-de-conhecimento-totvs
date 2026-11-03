---
article_id: 9188624787863
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: db5361cf743101a261328958e797d7d588e0539710f91bcd49b33af1dd09870d
fetched_at: '2026-06-28T22:37:23.904072+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Mensagem FWNOLIST para
  campo Competência na rotina de Medição CNTA121
type: support-article
updated_at: '2023-09-20T15:16:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9188624787863-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Mensagem-FWNOLIST-para-campo-Compet%C3%AAncia-na-rotina-de-Medi%C3%A7%C3%A3o-CNTA121
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17682478812951) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Ao realizar uma medição ocorre a Mensagem FWNOLIST para campo Competência na rotina de Medição CNTA121:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9188423073815)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Causa**Esta ocorrência é comumente causada por inconsistências no Dicionário de Dados. Alterações não adequadas em Tabelas que envolvem o Contrato.

Por exemplo, alterada ordem de campos que funcionam com sequência lógica, alterado tamanho de modo incompatível, alterada a marcação de "usado" dos campos, dentre outras alterações indevidas.

**Solução**

1. A causa mais recorrente é a alteração na ordem (X3\_ORDEM) de campos como: CND\_NUMMED, CND\_CONTRA, CND\_COMPET e CND\_REVISA

Verifique se os campos estão nesta ordem em seu dicionário e, se necessário, corrija.

2. Tendo validado a ordem, caso persista, confira que os campos estão devidamente marcados como "Usado" e visíveis para o módulo / para os usuários (não há retrições de acessos / níveis).

3. Caso ainda assim persista, é recomendado em ambiente/base teste recriar os dicionários, de acordo com o dicinonário padrão disponibilizado pelo produto no Portal do cliente, para certificar que, com o dicionário padrão, a ocorrência não é apresentada.

Segue para validação a **ordem de todos os campos** da **tabela CND** conforme o padrão nas imagens abaixo, e caso não esteja, realizar o teste com os campos na ordenação padrão do Dicionário de dados.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9188231253271)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9188234999191)

***Obs:***  
Deve-se analisar na base de dados as ordens/tamanhos de campos ***tanto no Dicionário de Dados como também no Banco de Dados***, os quais devem estar compatíveis.

Caso necessário, orienta-se o apoio de um analista especialista em loco para a analise da base de dados.

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
