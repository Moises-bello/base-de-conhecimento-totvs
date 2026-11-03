---
article_id: 33938434213271
category: TAF - eSocial - Configuração
content_hash: e27ca9afcdb8aa665118481592cc61ae4c8d71b40b690146e62c4ab7843e2d8b
fetched_at: '2026-06-28T22:45:14.435849+00:00'
product: protheus
section_id: 1500001536941
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial – Configurações  - Como criar um appserver
  exclusivo a partir da versão 12.1.2410
type: support-article
updated_at: '2026-06-26T11:19:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33938434213271-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%B5es-Como-criar-um-appserver-exclusivo-a-partir-da-vers%C3%A3o-12-1-2410
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33938434173079) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como criar um appserver exclusivo, separado do ambiente principal, onde os possíveis erros serão direcionados somente para um arquivo console.log? Facilitando a interpretação e detecção de mensagens de erros do sistema.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF - Á partir da versão 12.1.2410  
  
**Solução**

**Siga o passo a passo, descrito abaixo, para criar um appserver.ini exclusivo á partir da versão 12.1.2410 do Protheus.**  
  
**1° Copie e cole um appserver.ini  já existente no ambiente.**

**Exemplo:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33938419354135)

**2° Mude o nome do mesmo, para melhor exemplificar, deixamos o nome do mesmo como “EXCLUSIVO”.**

Exemplo, após mudar o nome:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33938419356311)

**3° Acesse a pasta nova e abra o arquivo appserver.ini, depois localize o ambiente que usamos para acessar o sistema e “RENOMEIE” o mesmo para o nome “EXCLUSIVO”.**

Exemplo

**ANTES:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33938434176023)

**DEPOIS:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33938434177047)

**4° Em seguida MUDE o número da porta TCP para qualquer número que desejar.**

Exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33938434177559)

**5° MUDE o NOME DO AMBIENTE na chave app\_environment localizada no grupo GENERAL,  mudando o nome para "Exclusivo"**

Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33938419360535)

**6° Como estamos na release 12.1.2410 e possuímos a grupo WEBAPP é necessário também ALTERAR a PORTA do Webapp.**

**Exemplo:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33938434187159)

**7° Como o objetivo do appserver exclusivo é GERAR UM CONSOLE preciso, é necessário ATIVAR as chaves TAFCONOUT e CONSOLELOG como no exemplo abaixo:**  
  
**Exemplo:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33938434187927)

**8° Após o appserver estar totalmente configurado deve subir o serviço em modo CONSOLE.**

**Para isso, deve:**

**a) Criar um atalho:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33938419368727)

b) Depois, acesse  “PROPRIEDADES" do atalho e acrescente – console

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33938419369751)

**Após, inicie o serviço pelo atalho criado como CONSOLE.**  
  
A janela abaixo será aberta, indicando que o serviço foi iniciado em modo CONSOLE.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33938419370647)

**9° Depois de subir o serviço, abra o navegador da internet e acesse o sistema colocando a porta do Webapp, que foi configurada anteriormente.**

**Exemplo:**  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/33938434192535)**

**10° Para validar se a configuração foi realizada corretamente, quando entrar no sistema o cabeçalho apresentará o ambiente “Exclusivo”.**

**Exemplo:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33938434193687)

**Saiba Mais**  
Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Para conhecimento dos eventos futuros, acessa a nossa página [**TOTVS Informa**](https://informa.totvs.com/) selecione em categorias a área e pesquise por "**Eventos**"  
  
Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
