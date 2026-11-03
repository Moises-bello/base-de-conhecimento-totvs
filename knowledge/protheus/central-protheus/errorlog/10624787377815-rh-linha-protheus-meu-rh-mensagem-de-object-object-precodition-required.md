---
article_id: 10624787377815
category: ERRORLOG
content_hash: 096886bc2cd974aa1d050cf076ba4b29df0502b7f803b9c6aa23af7c8db06f58
fetched_at: '2026-06-28T22:44:39.435916+00:00'
product: protheus
section_id: 10299583475863
source: central-protheus
title: RH - Linha Protheus - MEU RH - Mensagem de [object Object] Precodition Required
type: support-article
updated_at: '2025-12-08T14:21:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10624787377815-RH-Linha-Protheus-MEU-RH-Mensagem-de-object-Object-Precodition-Required
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29117992713111) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Apresenta a mensagem de **[object Object]** e **Precodition Required** em alguma rotina do MEU RH  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – Todas as versões.  
  
**Causa**  
**Falta de atualização** entre os **arquivos do portal** MEU RH e o **RPO** utilizado.  
  
**Solução**  
Para correção desse problema é necessário **Atualizar** o acumulado do RH assim como os arquivos do portal MEU RH, pois essa inconsistência é gerada quando há diferença entre a versão usada nos arquivos do portal MEU RH com os fontes compilados no RPO. Para correção aplique ambas atualizações:

**1. Arquivos do Portal:**  
[RH - Linha Protheus - MEU RH - Onde baixo a versão mais recente e como atualizar os arquivos do Portal Meu RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729034)  
  
**2. Acumulado RH:**  
[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus#:~:text=Para%20fazer%20o%20download%20do,com%20seu%20release%20do%20Protheus.&text=Nesse%20pacote%2C%20n%C3%A3o%20temos%20dispon%C3%ADveis,segue%20abaixo%2C%20link%20para%20download.)  
  
**3. LIB mais recente, por conta das aplicações em REST**  
<https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/>   
  
Se após as atualizações, houver o mesmo cenário, uma das causas mais prováveis é **falta de licença disponível** para utilização do recurso.  
  
Para isso, acesse o *Monitor do License Server*, e verifique quais as licenças disponíveis.  
**A mais utilizada é a de ID 4001 - TOTVS I.**  
  
No exemplo abaixo, temos um LS com 05 licenças TOTVS I disponíveis, porém **todas sendo utilizadas.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29117992716567)  
  
Nesse caso, será necessário entrar em contato com o ESN - Gerente de Contas TOTVS, para que obtenham mais licenças na modalidade TOTVS I.   
  
**Saiba Mais**  
[**RH - Linha Protheus - MEU RH - Aprenda sobre o MEU RH e como fazer a implantação**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036164214)  
[**CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI para acessar a documentação de referência sobre o MEU RH**](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
