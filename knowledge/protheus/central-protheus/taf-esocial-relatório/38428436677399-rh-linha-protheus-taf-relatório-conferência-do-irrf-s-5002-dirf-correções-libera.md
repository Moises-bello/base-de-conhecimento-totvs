---
article_id: 38428436677399
category: TAF - eSocial - Relatório
content_hash: b265e5654bbc4e671d4b9331dd95ace80b974a67b4165d785b3fd2b6d03bc498
fetched_at: '2026-06-28T22:45:20.027667+00:00'
product: protheus
section_id: 1500001536821
source: central-protheus
title: RH - Linha Protheus - TAF - Relatório  - Conferência do IRRF S-5002 (DIRF)
  - Correções liberadas
type: support-article
updated_at: '2026-06-24T18:45:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38428436677399-RH-Linha-Protheus-TAF-Relat%C3%B3rio-Confer%C3%AAncia-do-IRRF-S-5002-DIRF-Corre%C3%A7%C3%B5es-liberadas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38428456861207) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Relatório para conferência do IRRF S-5002 (DIRF) não apresenta registro, não gera, ou apresenta registro com valores errados.  
  
**Ambiente**  
RH - Linha Protheus - TAF - Relatório  - Conferência do IRRF S-5002 (DIRF) - Correções liberadas - Todas as versões  
  
**Solução**

1.Verifique se seu ambiente está com a última expedição contínua do TAF , deve estar com atualização a partir de 01/2026.

Para conferir sua atualização, acesse a tela de diagnostico do TAF:  
[RH - Linha Protheus - TAF - eSocial - Rotinas Comuns - Como acessar a tela de diagnóstico no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17988545143063)

2. Aplique as patcht´s de correções abaixo listadas, no RPO do PROTHEUS:  
  
A)

12.1.2310:<https://r.totvs.io/p/1238449>

12.1.2410:<https://r.totvs.io/p/1238450>

12.1.2510:<https://r.totvs.io/p/1238451>

B)

12.1.2310:<https://r.totvs.io/p/1237891>   
12.1.2410:<https://r.totvs.io/p/1237892>   
12.1.2510:<https://r.totvs.io/p/1237893>

C)  
12.1.2310:<https://r.totvs.io/p/1238379> ;   
12.1.2410:<https://r.totvs.io/p/1238380> ;   
12.1.2510:<https://r.totvs.io/p/1238381>

3. Após aplicar a patch, realize o reprocessamento seguindo as orientações da documentação abaixo:

<https://tdn.totvs.com/display/public/TAF/Reprocessamento+DIRF+-+TafRepDIRF>

\*Clicar na opção: Forcar Reprocessamento(Sobrescreve dados na T8R)

**Saiba Mais**

Para saber mais consulte os links abaixo:

[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)

[Centralizadora TAF](https://tdn.totvs.com/display/public/TAF/Centralizadora+TAF)

[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)

[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)

*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e pesquise por "**Eventos**"*

Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
