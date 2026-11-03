---
article_id: 360007450231
category: Espelho
content_hash: 002bc22b3b17a6917f113fa694baa3f7a844406402ee7b27a1d9c0a959506f00
fetched_at: '2026-06-28T22:46:31.315269+00:00'
product: rm
section_id: 6045459696023
source: central-rm
title: RH - RM - PTO - Comportamento quando houver ausência de marcação
type: support-article
updated_at: '2025-08-19T19:14:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007450231-RH-RM-PTO-Comportamento-quando-houver-aus%C3%AAncia-de-marca%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19409201115927)** **Tempo aproximado para leitura: 00:01:00 min****Dúvida**

Qual o comportamento do produto quando o funcionário esquece de efetuar uma batida no ponto?  
  
**Ambiente**

TOTVS RH - Linha RM - TOTVS Automação de Ponto - Todas as versões.  
  
**Solução**A validação da batidas é realizada por pares (por exemplo: 4 batidas: entrada jornada, saída refeição, volta refeição, saída jornada). Caso tenha uma batida ausente, o produto irá procurar a próxima batida realizada para completar o seu par e, dessa forma, podem ser geradas extras ou atrasos, conforme parametrização do sindicato.

Acesse **Configurações > Parametrizador**, ao abrir o assistente, clique em avançar, selecione a opção **Sindicato** e avance:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13809027521303)   
  
Selecione o sindicado que deseja alterar e clique na opção **Parametrizar**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13809028161431)

No Sindicato, acesse a **Etapa 4 -** **Atrasos e Faltas**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25771234313111)

**Considera ausência quando existir batida sem par:**

Com esse parâmetro habilitado, o sistema irá calcular falta quando não existir uma batida de saída para uma batida de entrada. Caso não esteja habilitado, quando existir uma batida de entrada sem uma batida de saída correspondente, o sistema irá calcular extra.

Quando houver batidas ímpares no dia, ou seja, uma batida ausente, a empresa pode inserir essa batida manualmente com a devida justificativa:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34299330837527)  
  
**Saiba Mais  
[Perguntas e Respostas - Portaria n° 671/2021](https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/inspecao-do-trabalho/fiscalizacao-do-trabalho/Perguntas%20e%20Respostas%20REP)**
