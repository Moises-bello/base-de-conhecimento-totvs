---
article_id: 39309703576855
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: 5f5c75df6b407316311dee28978c490a9a00df5b62947850c393e5b601aed8fd
fetched_at: '2026-06-28T22:45:21.042187+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Rotinas Comuns - Eventos Aguardando retorno
  RET do e-Social TAFA552A
type: support-article
updated_at: '2026-04-27T19:51:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39309703576855-RH-Linha-Protheus-TAF-eSocial-Rotinas-Comuns-Eventos-Aguardando-retorno-RET-do-e-Social-TAFA552A
---

**Dúvida**  
Eventos com status aguardando retorno RET no Painel do eSocial (monitor).  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Rotinas Comuns - Painel eSocial (TAFA552A) - Todas as versões.  
  
  
**Solução**  
Segue orientações para a dúvida "Eventos aguardando retorno RET":

1. Clica em atualizar status no evento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39309831759511)

Persistindo o problema, siga com as orientações abaixo:  
  
2. Para cliente Protheus, é necessário criar um AppServer exclusivo para esse cenário.

* Caso o ambiente seja segregado **(linha RM/Datasul)**, desconsiderar esta orientação..

[RH - Linha Protheus - TAF - eSocial – Configurações - Como criar um appserver exclusivo a partir da versão 12.1.2410](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33938434213271-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%B5es-Como-criar-um-appserver-exclusivo-a-partir-da-vers%C3%A3o-12-1-2410)

3. Em seguida, por gentileza, envie o arquivo console.log das pastas abaixo.

* TAF\bin\app  (para ambiente segregado – linha RM ou Datasul)
* TAF\bin\appserver (clientes Protheus)

4. Envie o console.log da pasta APPSERVER TSS.

* Totvssped\BIN\appserver
* Enviar appserver.ini do TSS.

\*\*Acima foram informadas as pastas criadas por padrão.

5. Print diagnostico do TAF.

* [RH - Linha Protheus - TAF - eSocial - Rotinas Comuns - Como acessar a tela de diagnóstico no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17988545143063-RH-Linha-Protheus-TAF-eSocial-Rotinas-Comuns-Como-acessar-a-tela-de-diagn%C3%B3stico-no-TAF)

**Saiba Mais**

Para saber mais consulte os links abaixo:

[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)

[Centralizadora TAF](https://tdn.totvs.com/display/public/TAF/Centralizadora+TAF)

[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)

[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)

Para conhecimento dos eventos futuros, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/) selecione em categorias a área e pesquise por "Eventos"

Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
