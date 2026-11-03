---
article_id: 360028341832
category: Meu RH - Instalação, configuração, qrcode, permissões e erros
content_hash: ae7aee86ade7f5bd1e1449577a07842beb72a3e2b6a048265bd07bd15a1af116
fetched_at: '2026-06-28T22:47:29.577683+00:00'
product: rm
section_id: 1500000961062
source: central-rm
title: RH - RM - Meu RH - Como criar o arquivo index html
type: support-article
updated_at: '2025-02-10T18:28:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028341832-RH-RM-Meu-RH-Como-criar-o-arquivo-index-html
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24081668485015) Tempo aproximado para leitura: 00:01:15 min  
  
Dúvida**Como criar o arquivo index.html e o que deve ter em seu conteúdo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir da versão 12.1.24  
  
**Solução**O arquivo index.html deverá ser criado para o redirecionamento correto da página de login do Meu RH.  
  
Para criá-lo, siga os passos.  
  
**01.** Aperte o botão **Windows + R**no teclado, digite **notepad** e clique em **OK**.  
**02.** Ao abrir o bloco de notas, insira o seguinte texto:

```
<!DOCTYPE html>  
 <html lang="en">  
 <head>  
 <meta charset="UTF-8">  
 <meta name="viewport" content="width=device-width, initial-scale=1.0">  
 <meta http-equiv="X-UA-Compatible" content="ie=edge">  
 <title>Document</title>  
 </head>  
 <body>  
 <script>  
 window.location.href = "web/app/RH/PortalMeuRH/#/login"  
 </script>  
 </body>  
</html>
```

**03.** Após inserir o texto, clique em **Arquivo | Salvar Como...**;  
**04.** Vá até o caminho: **c:\totvs\CorporeRM\FrameHTML**e salve o arquivo com o nome "index.html" (sem as aspas);  
**05.** Reinicie o IIS.
