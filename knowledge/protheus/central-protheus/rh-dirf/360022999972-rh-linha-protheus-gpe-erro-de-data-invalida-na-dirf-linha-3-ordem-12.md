---
article_id: 360022999972
category: RH – DIRF
content_hash: a79efe5696f36d31c9012d7165f5aee4cdbc1e6347edb5342a876834b72a53d4
fetched_at: '2026-06-28T22:44:06.984372+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Erro de data invalida na DIRF, linha 3 ordem 12
type: support-article
updated_at: '2025-08-19T20:48:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022999972-RH-Linha-Protheus-GPE-Erro-de-data-invalida-na-DIRF-linha-3-ordem-12
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34302296816151)**Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**Erro no validador Data Invalida na linha 3 e ordem 12.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360021023811)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**O erro ocorre quando nos parâmetros da geração do arquivo magnético (GPEM590) a pergunta **Situação da Declaração** for informado o conteúdo **2-Ext/Enc.espol** e a data do evento ficou em branco.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360021024091)  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

Entre na rotina de Arquivo Magnético pelo caminho **>Miscelânea >Dirf >Arquivo Magnético**, e faça os ajustes conforme abaixo:  
Caso a DIRF seja realmente uma extinção/Encerramento por espólio, a **data do evento** deve ser preenchida;  
Porém se a DIRF não for esse motivo, deve-se alterar o a pergunta **Situação da Declarção para conteúdo 1-Normal.**  
  
Confirme os parâmetros e gere o arquivo magnético, após isso, importe para o PGD (Programa Gerador DIRF).  
  
**Saiba mais**  
[RH - Linha Protheus - GPE - Passo a Passo para geração do Arquivo magnético da DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022076092)
