---
article_id: 1500006910061
category: FÉRIAS
content_hash: 122b62e3f4e42cdaeeed1d5db0e92a6ff3bd03d89bccf8bc488247f154db8efe
fetched_at: '2026-06-28T22:44:34.578505+00:00'
product: protheus
section_id: 10299705719575
source: central-protheus
title: RH - Linha Protheus - MEU RH - Erro ao solicitar férias - Não existe período
  de férias no cadastro de Programação de Férias
type: support-article
updated_at: '2026-06-16T18:10:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006910061-RH-Linha-Protheus-MEU-RH-Erro-ao-solicitar-f%C3%A9rias-N%C3%A3o-existe-per%C3%ADodo-de-f%C3%A9rias-no-cadastro-de-Programa%C3%A7%C3%A3o-de-F%C3%A9rias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24768628898455)Tempo aproximado para leitura: 00:02:00 min**  
  
**Ocorrência**  
Ao tentar solicitar férias pelo Meu RH, apresenta a seguinte mensagem de erro "Erro ao solicitar férias - Não existe período de férias no cadastro de Programação de Férias!"

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500009100162)  
  
**Causa**  
Este erro ocorre quando no parâmetro MV\_REFTRAB não está com 'F' em seu conteúdo.  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**  
Inclua 'F' no conteúdo do parâmetro, ele deve ficar como 'FSRI' (sem aspas), reinicie o serviço do Meu RH e faça a solicitação de férias novamente.  
  
**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500009107842)**  
  
**Saiba Mais**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI**para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
