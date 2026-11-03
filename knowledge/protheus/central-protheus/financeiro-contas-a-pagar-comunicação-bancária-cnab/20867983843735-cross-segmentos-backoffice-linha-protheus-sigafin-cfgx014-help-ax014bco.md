---
article_id: 20867983843735
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: dcf0e7e10919b4af4fed8575dafbeb9e6abfe088780170f60406539e3b97a5c4
fetched_at: '2026-06-28T22:37:55.312436+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CFGX014 - HELP: AX014BCO '
type: support-article
updated_at: '2024-01-29T12:54:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20867983843735-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CFGX014-HELP-AX014BCO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20867969108247) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No módulo Configurador, ao tentar realizar a restauração do arquivo de configuração CNAB, ocorre a mensagem de **HELP: AX014BCO - Erro recuperando arquivo de comunicação bancária.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20867969112343)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Esse incidente ocorre, pois o arquivo usado na restauração é um **Modelo 2 - 240 posições**

**Solução**Para correção, deve usar um arquivo de modelo de configuração em **400 posições**, para saber se o arquivo de configuração é de **400 posições**, abra o arquivo em um bloco de notas, localize a função **Incremental()** e verifique a posição final

Exe.. 395 a 400, significa que o arquivo é 400 posições

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20867983806103)

Exemplo de um arquivo Modelo 2 - 240 posições

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20867969122327)

**Para saber sobres as extensões, verifique abaixo**  
[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Extensão cnab](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016606051-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Extens%C3%A3o-cnab)

**Saiba mais**  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Principais configurações e dúvidas para uso do CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7778595184407-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Principais-configura%C3%A7%C3%B5es-e-d%C3%BAvidas-para-uso-do-CNAB)
