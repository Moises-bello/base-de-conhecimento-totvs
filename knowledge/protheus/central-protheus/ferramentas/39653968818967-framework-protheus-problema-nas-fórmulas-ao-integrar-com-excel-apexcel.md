---
article_id: 39653968818967
category: Ferramentas
content_hash: ff487bd88902edcea6a14da2d2c1f464d4c7aad52d19a145456c0451d7e82954
fetched_at: '2026-06-28T22:42:18.082327+00:00'
product: protheus
section_id: 360000075448
source: central-protheus
title: Framework – Protheus – Problema nas fórmulas ao integrar com Excel (Apexcel)
type: support-article
updated_at: '2026-05-07T13:02:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39653968818967-Framework-Protheus-Problema-nas-f%C3%B3rmulas-ao-integrar-com-Excel-Apexcel
---

⏱ Tempo aproximado para leitura: 00:00:46 min

**Ocorrência**  
Na rotina Miscelânea > Integrações, ao gerar uma planilha Excel, as fórmulas ficam desconfiguradas

**Ambiente**  
Integrações - Planilha Excel (Apexcel)

**Causa**  
Este cenário ocorre devido a uma mudança na LIB de março/2026 (20260302), onde a busca do arquivo apexcel80.xla foi alterada de "C:\apexcel" para a pasta web-agent, que fica no perfil do usuário

**Solução**  
Para solucionar este cenário, é necessário realizar os seguintes passos:

1. Certificar de que o Web-Agent está em execução no computador do usuário
2. Na fórmula, retire a informação 'C:\ApExcel\apexcel80.xla'!, que está apontando para o antigo caminho do arquivo apexcel80.xla. Com o Web Agent em execução, o arquivo será localizado automaticamente no perfil do usário, dentro da pasta web-agent (C:\"Usuário"\AppData\Local\Programs\web-agent)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39653955797911)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39653955799063)

**Obs.:** Com a ferramenta localizar do Excel, pode ser utilizada a opção "Substituir tudo" para limpar o caminho 'C:\ApExcel\apexcel80.xla'! de todas as fórmulas da planilha

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39653968806167)
