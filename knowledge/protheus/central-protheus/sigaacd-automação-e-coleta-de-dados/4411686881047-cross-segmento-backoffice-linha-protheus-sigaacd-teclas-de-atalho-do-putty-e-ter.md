---
article_id: 4411686881047
category: SIGAACD - Automação e Coleta de Dados
content_hash: 024d9a20a9ede148a06abce5eabd25a42a16337ad9171ee1a21f6045d4471f6a
fetched_at: '2026-06-28T22:39:11.145351+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD -  Teclas de atalho
  do Putty e TeraTerm não Funciona. Como corrigir?
type: support-article
updated_at: '2021-10-29T11:53:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411686881047-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Teclas-de-atalho-do-Putty-e-TeraTerm-n%C3%A3o-Funciona-Como-corrigir
---

**Dúvida**Qual a configuração correta para as Teclas de Atalho do Putty e do TeraTerm funcionar corretamente? Pois quando dou seta para baixo ocorre do coletor fica dessa forma: ^B ^C .

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.

**Solução**Para as Teclas de Atalho funcionar corretamente via Putty, basta efetuar a seguinte configuração:

Na opção de **Terminal**, selecione o "Local echo" e "Local Line Editing" marcando a opção **Force Off** conforme a imagem abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411686870295/mceclip0.png)

Para o TeraTerm, basta efetuar as mesmas configurações ajustando no arquivo TERATERM.ini as tags EnableLineMode=off e LocalEcho=off.

**Saiba Mais:**

*[Clique aqui e veja mais artigos sobre Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)*
