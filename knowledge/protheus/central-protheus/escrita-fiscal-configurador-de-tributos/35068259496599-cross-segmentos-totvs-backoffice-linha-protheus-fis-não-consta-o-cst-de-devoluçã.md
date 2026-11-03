---
article_id: 35068259496599
category: Escrita Fiscal - Configurador de Tributos
content_hash: 2001a6ce3e5a15efb51d82aaebe13d4dd4c01e34c2d2a2359a3dea19c1e2e314
fetched_at: '2026-06-28T22:39:18.491812+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – Não consta o CST
  de devolução dos impostos calculados pelo Configurador de Tributos.
type: support-article
updated_at: '2026-03-27T00:25:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35068259496599-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-N%C3%A3o-consta-o-CST-de-devolu%C3%A7%C3%A3o-dos-impostos-calculados-pelo-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35068259477527) Tempo aproximado para leitura: **00:10 min**  
  
**Ocorrência**  
A devolução de um documento, seja de entrada ou saída, cujo cálculo do documento original foi realizado pelo Configurador de Tributos, não esta considerando o CST de devolução informado na Regra Escrituração.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Causa**  
Nesse contexto, o sistema retorna ao documento original, analisa os cálculos efetuados, verifica a versão da regra de cálculo aplicada e realiza um novo cálculo, espelhando a operação original de forma inversa.

* **Devolução de documento de entrada:** O sistema gerará uma saída correspondente.
* **Devolução de documento de saída:** O sistema gerará uma entrada correspondente.

O cálculo utilizará a versão da regra vigente no momento da emissão ou lançamento do documento original, mantendo:

* Base de cálculo
* Alíquota
* Escrituração correspondente à data da operação original

**Solução**  
Caso seja necessário realizar ajustes na Regra de Escrituração:

1. Modificar a Regra de Escrituração conforme desejado.
2. Reprocessar o documento original.

Dessa forma, a versão será atualizada para refletir os parâmetros atuais de base de cálculo, alíquota e escrituração.

[Perguntas e Respostas - Configurador de Tributos](https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Perguntas+e+Respostas+-+Configurador+de+Tributos#CFGTRIBPerguntaseRespostasConfiguradordeTributos-13-ComoFuncionaaDevolu%C3%A7%C3%A3oquandoosc%C3%A1lculosdodocumentodeorigemforamexecutadospeloconfigurador?)
