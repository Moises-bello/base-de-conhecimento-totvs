---
article_id: 360059007914
category: RH - Lançamentos
content_hash: 865bcbf711bb8c6ab337a973a4e7a9f4deb3a3bc317d6cbdb7011569012e7806
fetched_at: '2026-06-28T22:43:31.299730+00:00'
product: protheus
section_id: 360010781734
source: central-protheus
title: RH - Linha Protheus - GPE - Informada verba incorreta nos Lançamentos Futuros
type: support-article
updated_at: '2025-07-23T17:36:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059007914-RH-Linha-Protheus-GPE-Informada-verba-incorreta-nos-Lan%C3%A7amentos-Futuros
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26297701742615)  Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**Feito lançamento de uma verba **incorreta** em **Valores Futuros,** mas quando tentamos ajustar informando o código correto, Sistema emite **alerta: A verba não pode ser alterada após sua inclusão!**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101669193)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**A rotina possui uma **trava de segurança** para alterações, afim de manter **histórico das manutenções,** bem como **histórico de cálculo** dos funcionários.  
  
**Solução**  
Para **corrigir** o código da verba informada, acesse a rotina **Valores Futuros em Atualizações > Lançamentos > Valores Futuros (GPEA110)**, e **exclua** a linha de sua referência**.**  
Após este processo, basta **incluir uma nova linha** com o **código correto** desejado e **salvar** as alterações.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000573582)

Esta ação só será possível caso **não** tenha sido feito nenhum **cálculo** após sua inclusão. Caso tenha sido feito, será necessário **cancelar** o **cálculo** realizado **antes** de realizar a manutenção na rotina de Valores Futuros, conforme orientado acima.  
  
**Saber mais**

[RH - Linha Protheus - GPE - Como suspender valores lançados na rotina de Valores Futuros](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017555452-MP-GPE-Como-cancelar-valores-lan%C3%A7ados-na-rotina-de-Valores-Futuros?source=search)

[RH - Linha Protheus - GPE - Impressão de relatório de Valores Futuros GPER570](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052070034-MP-GPE-Impress%C3%A3o-de-relat%C3%B3rio-de-Valore-Futuros-GPER570?source=search)

[RH - Linha Protheus - GPE - Relatório Valores Futuros em planilha (GPER570)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053605673-MP-GPE-Relat%C3%B3rio-Valores-Futuros-em-planilha-GPER570-?source=search)

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[Artigos Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)
