---
article_id: 13781767107735
category: SIGAEST - CUSTOS
content_hash: ea7082c5b1d6efbef631f6eabd110b6c8bc49e29264b6e92c1b5e1a98bc96b36
fetched_at: '2026-06-28T22:39:02.013668+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA038 - Acompanha
  Custos não abre/botão "Novo Fechamento" não habilita
type: support-article
updated_at: '2025-10-27T11:29:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13781767107735-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA038-Acompanha-Custos-n%C3%A3o-abre-bot%C3%A3o-Novo-Fechamento-n%C3%A3o-habilita
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35903771860247) Tempo aproximado para leitura: **00:03:30 min**  
  
**Ocorrência**

A rotina Acompanha Custos (MATA038) não está mais abrindo, ficando com tela branca ou com o botão "Novo Fechamento" inativo.

Tela branca:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13781437535127)

Botão novo fechamento indisponível:

![botao novo fechamento inativo.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35903755787287)

Carregando eternamente:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13781540156439)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**

Esse incidente ocorre normalmente por falta de atualização de Componentes, onde rotinas PO-UI requisitam bastante da manutenção (atualização) periódica dos artefatos como: LIB, Binários e Dbaccess. O próprio código-fonte do da "Acompanha Custos" (MATA038) também é importante, porém normalmente são os artefatos que, conforme ficam obsoletos, podem enfrentar esse tipo de colateral.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

**1.** Atualizar os artefatos de Framework:

* LIB: <https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/LIB_LABEL>
* Binário

* AppServer: <https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/appserver>

  Smartclient: <https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/smartclient>

* DBACcess:

  Linux: <https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/DBAccess_Linux>

  Windows: <https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/DBAccess_Windows>

**Observação:** sempre aplicar pacotes primeiramente em ambiente de homologação com backup prévio do RPO.

**2.** Em caso de atualizações porém insucesso (permanência do problema), será necessário avaliar via Logs (gere e encaminhe ao Suporte Técnico:

**Habilitação de TraceStack e geração de logs:**  
  
2.1. Habilite TraceStack no arquivo appserver.ini em um ambiente isolado, conforme a documentação: <https://tdn.totvs.com/display/tec/TraceStack>

2.2. Após habilitar a chave TraceStack, faça um backup do arquivo console.log (com outro nome) e o arquivo original **console.log**, limpe todo seu conteúdo. Este arquivo está contido no diretório do appserver. Em seguida reinicie o Sistema.  
  
2.3. Depois de reiniciar o sistema, acesse à rotina "Acompanha Custos" e aguarde por cerca de 5 minutos.  
  
2.4. Durante este período, o arquivo console.log será alimentado. Caso não tenha conhecimento/habilidade de análise de log, colete-o e encaminhe ao Suporte Técnico por meio de um ticket.

2.5. Encaminhar também os dados de ambiente via Central de Diagnósticos. Veja neste artigo como enviar através do atalho SHIFT + F6: [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como enviar dados pela Central de Diagnóstico?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33711098138007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-enviar-dados-pela-Central-de-Diagn%C3%B3stico)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
