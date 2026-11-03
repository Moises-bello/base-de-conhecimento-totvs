---
article_id: 37499153399063
category: Meu RH - Assinatura Eletrônica
content_hash: 30183cea4b7655d8bf9ef8cb0de7d8183791ffcd4589b861f71c9ff1d767c8a6
fetched_at: '2026-06-28T22:47:28.736212+00:00'
product: rm
section_id: 19399655101335
source: central-rm
title: RH - RM - Meu RH - Documento da assinatura eletrônica exibido em branco no
  Meu RH
type: support-article
updated_at: '2026-01-14T15:48:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37499153399063-RH-RM-Meu-RH-Documento-da-assinatura-eletr%C3%B4nica-exibido-em-branco-no-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37499153391767) Tempo aproximado para leitura: **00:01:27 min**  
  
**Ocorrência**  
Ao acessar no Meu RH a página de visualização do documento / relatório e inserir o código de acesso, não é exibido nenhuma informação no documento. Em vez disso, é apresentada apenas uma tela em branco no local onde o conteúdo deveria ser carregado.

![image-2025-4-8_15-53-17.png](https://tdn.totvs.com/download/attachments/931598344/image-2025-4-8_15-53-17.png?version=1&modificationDate=1744201616137&api=v2)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir da versão 12.1.2406  
  
**Causa**  
O problema ocorre pois o navegador está tentando carregar um arquivo JavaScript como um module script (type="module"), mas o servidor está retornando o MIME type incorreto (application/octet-stream) ao invés de application/javascript ou text/javascript. Isso quebra a execução do módulo e impede a renderização do PDF.

**Solução**  
É necessário garantir que o IIS esteja configurado para servir arquivos .mjs e .ftl com o MIME type correto. Acesse o diretório C*:\TOTVS\CorporeRM\FrameHTML,* edite o arquivo **Web.config** e adicione as seguintes tags no <staticContent>:

```
<mimeMap fileExtension=".mjs" mimeType="text/javascript" />
<mimeMap fileExtension=".ftl" mimeType="text/plain" />
```

![](https://tdn.totvs.com/download/attachments/931598344/image-2025-4-9_9-29-23.png?version=1&modificationDate=1744201763370&api=v2)

**Saiba mais**

[Integração Meu RH x TAE - RM](https://tdn.totvs.com/pages/viewpage.action?pageId=733186927)
