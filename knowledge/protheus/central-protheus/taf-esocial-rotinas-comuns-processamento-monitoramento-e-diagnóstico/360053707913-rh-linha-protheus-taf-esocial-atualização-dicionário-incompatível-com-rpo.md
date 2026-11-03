---
article_id: 360053707913
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: f320067ec37140f6b6cf4ee33eaf89b28f534fdd803dfed39290e6ff74145de1
fetched_at: '2026-06-28T22:45:20.919786+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Atualização - Dicionário incompatível
  com RPO
type: support-article
updated_at: '2025-03-24T15:26:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053707913-RH-Linha-Protheus-TAF-eSocial-Atualiza%C3%A7%C3%A3o-Dicion%C3%A1rio-incompat%C3%ADvel-com-RPO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26470279736983) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**

Ao acessar o **SmartClient** ocorre erro: **DICIONÁRIO INCOMPATÍVEL COM RPO****Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF - Todas as versões.  
  
**Solução**

**1** - Acesse o link de downloads do TAF e baixe a versão correspondente a sua release:

* 12.1.2210 **com garantia estendida**: <https://suporte.totvs.com/portal/p/10098/download?e=1084563>
* 12.1.2310: <https://suporte.totvs.com/portal/p/10098/download?e=1126399>

**2** - Acesse a pasta de instalação do Protheus e faça o backup dos arquivos **sdfbra** e **sx2.unq** e em seguida coloque os arquivos **sdfbra** e **sx2.unq** que foram baixados da atualização disponível no portal de download na pasta **SYSTEMLOAD**;

**3** - Exclua os arquivos **\*.IDX e** **\*.DTC** da pasta **SYSTEMLOAD**

**4** - Exclua os arquivos **\*.LOG** da pasta **SYSTEM**

**5** - Execute o UPDDISTR e UPDTAF conforme link abaixo:

[TAF - ATUALIZAÇÃO - Executando UPDDISTR e UPDTAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034765854)  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e**pesquise**por "****Eventos****"*Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
