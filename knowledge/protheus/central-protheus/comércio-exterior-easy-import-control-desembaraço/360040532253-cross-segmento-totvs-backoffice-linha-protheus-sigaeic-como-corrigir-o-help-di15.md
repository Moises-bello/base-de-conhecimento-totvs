---
article_id: 360040532253
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: c6d18f9f638ddf291ad48b895a58d1070afb7bc00f5fd3ff0ba7a5bf4a5293b0
fetched_at: '2026-06-28T22:39:50.008559+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Como corrigir
  o help "DI154DESP" na Nota complementar?
type: support-article
updated_at: '2022-04-27T20:45:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040532253-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Como-corrigir-o-help-DI154DESP-na-Nota-complementar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como corrigir o help "DI154DESP" na Nota complementar?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – A partir da versão 11.80  
  
**Solução**A mensagem apresentada informa que não foram incluídas despesas para geração da nota fiscal complementar.   
A nota complementar contém todas as despesas base de custo que não fizeram parte da primeira nota. As despesas devem ter a seguinte configuração :

* Base de custo = SIM
* Base de imposto = NÃO
* Base de ICMS = NÃO

Se a despesa for complemento de ICMS, cadastrar da seguinte forma:

* Base de custo = SIM
* Base de imposto = NÃO
* Base de ICMS = SIM
* ICMS na NFC = SIM e informar o UF na aba ICMS UF.

Existe um parâmetro que define se será calculado ICMS na nota complementar, o mesmo deve estar habilitado: MV\_ICMSNFC.  
Para gerar a nota complementar, realizar o seguinte procedimento:  
1 - Acessar a rotina desembaraço -> Manutenção -> Posicionar no processo a ser gerada a nota complementar, clicar em ações relacionadas -> Despesa, informar a despesa base de custo e confirmar.  
2 - Acessar a rotina de Desembaraço -> Recebimento de Importação, posicionar no processo -> Clicar em ações relacionadas -> Complementar.
