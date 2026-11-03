---
article_id: 41248409476247
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 889b97ced8c81ab0990521c71831be7aae109fe49dd3c386c8f273682aab76a0
fetched_at: '2026-06-28T22:37:23.883112+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Mensagem "NOCLVL" na
  rotina de Medição CNTA121 ao selecionar a Planilha
type: support-article
updated_at: '2026-06-16T12:08:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41248409476247-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Mensagem-NOCLVL-na-rotina-de-Medi%C3%A7%C3%A3o-CNTA121-ao-selecionar-a-Planilha
---

A mensagem "NOCLVL" na rotina de Medição CNTA121 ocorre ao selecionar a planilha, indicando que o código da classe de valor está inválido ou não cadastrado corretamente. A solução envolve verificar se as classes de valor dos itens do contrato estão cadastradas e ativas no Cadastro de Classe de Valor, pois o erro ocorre quando o sistema não reconhece essa classe ao transferir dados do contrato para a planilha de medição.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41248409458967) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**  
Ocorrência da Mensagem "NOCLVL" na rotina de Medição CNTA121 ao selecionar a Planilha a ser medida.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41248409459351)

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**

Na rotina de medição, ao se clicar na flag de seleção de planilha da rotina, este é o momento em que o módulo "gatilha" as informações que estão nos itens da planilha cadastrada no contrato, para o item da planilha da medição.  
   
Dessa forma, como a mensagem reporta o help "NOCLVL" referente a:

 "Código de classe valor inválido ou não preenchido" - Verifique se a classe valor foi digitada corretamente ou existe no cadastro",

No caso, uma análise que pode-se realizar no ambiente e registros do contrato em questão, é se as informações de "classe de valor" informadas no cadastro do contrato, nos itens da planilha selecionada, existem corretamente cadastradas no cadastro de classe de valor, ou se caso existam possam estar bloqueadas, ou de alguma forma com o cadastro/registro corrompidos.

Visto que a ocorrência é devido ao sistema não estar reconhecendo no cadastro de Classe de Valor, o código da Classe de Valor em questão que está se tentando "gatilhar", ou seja, levar do item do contrato para o item da planilha.

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
