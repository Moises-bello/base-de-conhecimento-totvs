---
article_id: 360025765411
category: ADVPL - Classe e Função
content_hash: 45cf6730785d7a05fc1afa5e074497d6215a4dc8b50b2be07c12fef91086bc7e
fetched_at: '2026-06-28T22:40:18.325703+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Erro ao Imprimir
  Browse
type: support-article
updated_at: '2025-04-15T14:14:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025765411-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-ao-Imprimir-Browse
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao solicitar a impressão do Browse, de uma determinada rotina gera o erro or log.

Exemplo:

Temos um campo customizado com uma user function que percorre uma tabela e retorno o conteúdo do campo, a user function é executada no inicializador do browse.

Na Rotina FINA040 gera o erro abaixo.

variable does not exist "E1\_PARCELA" on TRBREAK:EXECUTE(REPORT07.PRW)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024558651/mceclip0.png)  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Causa**Esse erro pode ocorre em qualquer rotina do padrão ou customização, quando é selecionado uma tabela em uma user function, desposicionando área de trabalho do *browse*.  
  
**Solução**Esse erro " *variable does not exist "E1\_PARCELA" on TRBREAK:EXECUTE(REPORT07.PRW)*" é só um exemplo, pois cada rotina é diferente, o sistema tenta acessar o campo "E1\_PARCELA" que na sua estrutura está na "SE1", mas como na *user function* está sendo utilizada "*DbSelectArea()"* para selecionar uma tabelaé necessário restaurar a área de trabalho, usando no inicio [GetArea()](http://tdn.totvs.com/pages/releaseview.action?pageId=6814876) e no final a [RestArea()](http://tdn.totvs.com/pages/releaseview.action?pageId=6814881)

```
#Include 'Protheus.ch'  
  
User Function INFO()  
Local aArea := GetArea() // Salva área atual para posterior restauração  
// sua customização  
DbSelectArea("TMP")  
  
("TMP")->(DbCloseArea())  
  
RestArea(aArea) // Restaura área atual  
  
Return 
```
