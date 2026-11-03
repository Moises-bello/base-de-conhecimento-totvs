---
article_id: 35839512276503
category: PONTO ELETRÔNICO
content_hash: b2106063d7ab2d472ca3a2928ee7c5d23f2204448f32f987e59c079fe521ed4b
fetched_at: '2026-06-28T22:44:36.447566+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - Meu RH - Como limitar os motivos de inclusão de marcações
  na rotina Espelho de Ponto no App Meu RH
type: support-article
updated_at: '2026-06-19T19:02:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35839512276503-RH-Linha-Protheus-Meu-RH-Como-limitar-os-motivos-de-inclus%C3%A3o-de-marca%C3%A7%C3%B5es-na-rotina-Espelho-de-Ponto-no-App-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35839512229399) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como limitar os motivos de inclusão de marcações na rotina Espelho de Ponto no App Meu RH?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**  
Foi criado o **parâmetro MV\_MRHRFD** que, irá limitar os motivos de inclusão de marcação que serão demonstrados no App Meu RH, pelo rotina Espelho de Ponto.  
  
Configuração do parâmetro:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35839512233623)  
  
**Na rotina PONA430 - Motivos de Manutenção, pelo módulo SIGAPON,** temos os motivos de inclusão padrões do Sistema e os que é possível incluir com o Uso Livre.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35839503800087)  
  
**Se o parâmetro MV\_MRHRFD estiver como .T.** o Meu RH, demonstrará **todos os motivos com o tipo INCLUSÃO, os que são Uso pelo Sistema e os Uso livre.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35839512239255)  
  
**Se o parâmetro MV\_MRHRFD estiver como .F.** o Meu RH, **demonstrará todos os motivos com o tipo INCLUSÃO, porém somente os que estiver com o campo USO = Uso livre, ou seja, os criados pelo usuário.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35839503802519)  
  
**Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
