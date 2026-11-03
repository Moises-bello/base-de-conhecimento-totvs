---
article_id: 360056458533
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: bb8fdb77d638f98c2ec32b207ec8cc2cd98beb20e6a93a170f4eaad2c9ec38f0
fetched_at: '2026-06-28T22:39:50.047639+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Despesa Negativa
  na NF Complementar
type: support-article
updated_at: '2022-04-27T21:02:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056458533-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Despesa-Negativa-na-NF-Complementar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Despesa Negativa na NF Complementar não grava a tabela SD1.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – A partir da versão 12.  
  
**Solução**

O documento [Despesa Negativa na NF Complementar](https://tdn.totvs.com/display/public/mp/Despesa+Negativa+na+NF+Complementar), diz respeito à funcionalidade para cenários não integrados com o módulo de compras **(SIGACOM)** - parâmetro **MV\_EASY** desabilitado **.F.**.

Quando o parâmetro **MV\_EASY** está desabilitado **.F.**, o recebimento de importação grava apenas as tabelas SF1 e SWN - a capa, **SF1**, da nota fiscal é gravada sempre. Não havendo a tabela **SD1**, o documento de entrada não pode ser classificado.

Neste caso, com o valor negativo entre os itens não é aceito pela SEFAZ ao transmitir a nota, por este motivo não é possível gerar a **SD1**, apresentando a mensagem de bloqueio.
