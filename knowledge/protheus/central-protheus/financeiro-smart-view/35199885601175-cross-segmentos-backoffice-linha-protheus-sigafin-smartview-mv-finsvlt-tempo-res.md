---
article_id: 35199885601175
category: Financeiro - Smart View
content_hash: be044b86dd6e0e91cbfe714af051997b874423cf1e34755b5c80837daa9f4382
fetched_at: '2026-06-28T22:37:44.809238+00:00'
product: protheus
section_id: 32632656432151
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - SmartView - MV_FINSVLT
  - Tempo resposta relatórios Smartview
type: support-article
updated_at: '2026-01-15T16:30:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35199885601175-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-SmartView-MV-FINSVLT-Tempo-resposta-relat%C3%B3rios-Smartview
---

![relogio_tempo_leitura_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35199885569815) Tempo aproximado para leitura: 00:03 min  
  
**Dúvida**  
Relatórios SmartView não correspondem aos dados presentes no sistema.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - 12.1.2210  
  
**Solução**  
Esse parâmetro define o tempo de cache das consultas realizadas pelo sistema. Durante o período configurado, o sistema mantém em memória (cache) tanto o resultado da consulta (dados apresentados ao usuário) quanto os parâmetros utilizados, evitando que uma nova pesquisa seja executada diretamente no banco de dados enquanto não houver alteração nesses parâmetros gerando uma melhor performance.

Dessa forma, dentro do tempo de validade do cache definido pelo **MV\_FINSVLT**, o sistema retornará as mesmas informações previamente consultadas, com o objetivo de otimizar a performance e reduzir acessos desnecessários ao banco de dados.

Uma nova consulta ao banco somente ocorrerá quando:

* Os parâmetros da consulta forem alterados; ou
* O tempo de cache configurado for expirado.

Caso o parâmetro não esteja criado no ambiente ou esteja com o conteúdo igual a **0**, o sistema interpreta o valor como **nulo**, aplicando automaticamente o valor padrão de **300(segundos)**.

O tempo de processamento informado no parâmetro é configurável e pode ser reduzido em relação ao valor padrão. Assim, quando o tempo atingir o valor definido no parâmetro, os dados serão atualizados.

Da mesma forma, quando houver uma consulta com parâmetros diferentes dos anteriormente utilizados, o sistema entenderá como uma nova busca de dados, realizando um novo *select* no banco e retornando as informações atualizadas.

**Saiba mais**

[Smart View - Financeiro](https://tdn.totvs.com/display/public/PROT/Smart+View+-+Financeiro)

[DT Criação de parâmetro para alteração de tempo de cache](https://tdn.totvs.com/pages/releaseview.action?pageId=907928700)
