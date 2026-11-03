---
article_id: 40048159460631
category: TAF - eSocial - Relatório
content_hash: 4903c4596609b7cee01aaf82316d66dcc30140c292d3b75a8169fc84aec71bfe
fetched_at: '2026-06-28T22:45:20.040956+00:00'
product: protheus
section_id: 1500001536821
source: central-protheus
title: RH - Linha Protheus - TAF - Relatório -Travam no percentual de 1% durante a
  geração pelo Painel do eSocial.
type: support-article
updated_at: '2026-05-04T14:12:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40048159460631-RH-Linha-Protheus-TAF-Relat%C3%B3rio-Travam-no-percentual-de-1-durante-a-gera%C3%A7%C3%A3o-pelo-Painel-do-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40048159440279) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
  
Os relatórios do TAF travam no percentual de 1% durante a geração pelo Painel do eSocial.  
**Obs.:** O travamento pode ocorrer, em qualquer um dos relatórios disponíveis no Painel do eSocial: **INSS, FGTS ou IRRF,** ocorre em clientes Protheus e segregados.

Exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40048205553687)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Relatório - (TAFA552A) - Todas as versões  
  
**Solução**  
Para resolver, siga as instruções:

1. Confirme se seu ambiente tem a Expedição Contínua de 03/2026.

Confira a data de atualização na tela de diagnóstico do TAF.

[RH - Linha Protheus - TAF - eSocial - Rotinas Comuns - Como acessar a tela de diagnóstico no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17988545143063)

**2.** Se sua atualização for de 03/2026, aplique o patch de correção conforme a versão do Protheus/TAF:

12.1.2310:<https://r.totvs.io/p/1243819>

12.1.2410:<https://r.totvs.io/p/1243820>

12.1.2510:<https://r.totvs.io/p/1243821>

**3. IMPORTANTE:** após aplicar a patch, pare e reinicie os serviços do PROTHEUS para que a correção tenha efeito!

**4.** Se sua atualização for antes de 03/2026, deve:

A) Atualizar o TAF com Expedição Contínua:

[RH - Linha Protheus - TAF  - ATUALIZAÇÃO - Como atualizar o TAF E-social (Expedição Contínua)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18972648169239)

B) Aplicar a patch de correção do item 2 deste documento.

C) Reiniciar os serviços do PROTHEUS para ativar a correção.  
  
**5.** Gere o relatório novamente no Painel do eSocial.

**Saiba Mais**

Para saber mais consulte os links abaixo:

[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)

[Centralizadora TAF](https://tdn.totvs.com/display/public/TAF/Centralizadora+TAF)

[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)

[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)

*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e pesquise por "**Eventos**"*

Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
