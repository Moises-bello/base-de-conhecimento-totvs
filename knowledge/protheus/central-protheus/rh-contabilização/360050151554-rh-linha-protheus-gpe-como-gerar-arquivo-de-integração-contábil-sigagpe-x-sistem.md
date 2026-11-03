---
article_id: 360050151554
category: RH - Contabilização
content_hash: 43388497b3d2e4847464e1c797080777b701e1b3ddc9ee384715f944a5c29aee
fetched_at: '2026-06-28T22:43:45.829712+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Como gerar arquivo de Integração contábil SIGAGPE
  X Sistema Externo
type: support-article
updated_at: '2025-07-21T18:26:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050151554-RH-Linha-Protheus-GPE-Como-gerar-arquivo-de-Integra%C3%A7%C3%A3o-cont%C3%A1bil-SIGAGPE-X-Sistema-Externo
---

**Dúvida**Como gerar arquivo de Integração contábil SIGAGPE X Sistema Externo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Passos para a efetiva contabilização com sistema Externo arquivo TXT (extensão CON)  
Configure os parâmetros:

MV\_RHCONEX conteúdo .T.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076303274)  
  
Conteúdo MV\_PASCON = (selecionar a pasta que será gravado o arquivo).   
Observação: Essa configuração é opcional. A rotina apresentará uma opção de gravação na pasta desejada.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076304374)

2. Gere o processo de contabilização através da rotina GPEM110 (Miscelânea /Fechamentos/Contabilização).  
Os lançamentos contábeis serão apresentados em tela. Selecione "Salvar":

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077522933)  
  
3. Após selecionar para salvar os lançamentos contábeis será apresentada a tela, para geração do arquivo  txt de integração contábil.   
Veja que conforme configuramos no parâmetro MV\_PASCON, a pasta destino da gravação já está definida. Selecione "Salvar":  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077523493)  
  
4. Aviso que o arquivo foi gerado com sucesso:  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076380554)  
  
5. Acesse a pasta selecionada para gravar o arquivo e conferir o arquivo gerado:   
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076380614)

**Saiba Mais:**  
[Página Centralizadora da Contabilização](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109092-RH-Contabiliza%C3%A7%C3%A3o)
