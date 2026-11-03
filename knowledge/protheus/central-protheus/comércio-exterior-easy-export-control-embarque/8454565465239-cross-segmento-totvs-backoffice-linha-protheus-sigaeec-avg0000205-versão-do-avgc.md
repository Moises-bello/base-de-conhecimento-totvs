---
article_id: 8454565465239
category: Comércio Exterior - Easy Export Control - Embarque
content_hash: 933804d6924735bc4e7096d4c766a538900607426730e9cc641626ca44499262
fetched_at: '2026-06-28T22:36:39.096068+00:00'
product: protheus
section_id: 1500001549322
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - AVG0000205  Versão
  do AvgCrw32.exe Inferior a 10/10/2000 '
type: support-article
updated_at: '2022-08-26T20:20:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8454565465239-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-AVG0000205-Vers%C3%A3o-do-AvgCrw32-exe-Inferior-a-10-10-2000
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **HH:MM:SS min** **Dúvida**Ao efetuar a tentative de geração do relatório do crystal no **SIGAEEC** esta sendo exibida uma mensagem de "**Help - AVG0000205 Problema: Versão do AvgCrw32.exe inferior a 10/10/2000, Atualizar Versão**". Como faço para gerar o relatório sem que seja exibida esta mensagem?

![AVG0000205.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/8453179055383/AVG0000205.PNG)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões  
  
**Solução**Para atualizar a versão **AVGCRW32.EXE** será necessário:

1) Fazer o donwload o pacote da expedição conitnua do comex através dos link: <https://tdn.totvs.com/pages/releaseview.action?pageId=526987588>

2) Selecione o release desejado e clique na opção clique **aqui** para efetuar o download. ![clique_aqui.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/8454067355287/clique_aqui.PNG)

3) Descompacte o arquivo **Config.zip** .

4)  Depois descompacte o arquivo ***CrystalDLLs.zip***.

5) Pegar o conteúdo das  dlls da pasta crystal  e copiar o seu conteudo dentro pasta *Smartclient* .

Efetuado esta procedimento o relatório estará funcionando.
