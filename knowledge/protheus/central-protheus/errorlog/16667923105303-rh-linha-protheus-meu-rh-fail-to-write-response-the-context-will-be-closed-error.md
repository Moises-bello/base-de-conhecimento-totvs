---
article_id: 16667923105303
category: ERRORLOG
content_hash: 5ecda721ad39be7083130391573ff1af2942d896ab9d0974c87ddc86a4434ab0
fetched_at: '2026-06-28T22:44:39.427272+00:00'
product: protheus
section_id: 10299583475863
source: central-protheus
title: RH - Linha Protheus - MEU RH - Fail to write response the context will be closed.
  Error:-100
type: support-article
updated_at: '2026-06-18T19:29:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16667923105303-RH-Linha-Protheus-MEU-RH-Fail-to-write-response-the-context-will-be-closed-Error-100
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16667878817431) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Ao tentar realizar o *login* através do Portal **Meu RH** inserindo o usuário e senha a página carrega realizando o *logout* em seguida. Ao analisar o console é apresentada a mensagem: ***"Fail to write response the context will be closed. Error:-100"***  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - MEU RH - Todas as versões  
  
**Causa**  
Geralmente este erro ocorre quando os serviços (***API's***) e *threads* de requisição são finalizadas e possui solicitações em execução.  
  
**Solução**  
A mensagem "***Fail to write response the context will be closed. Error:-100***" pode ser apresentada no console do serviço REST utilizado pelo Meu RH, ao realizar o acesso **via*****web*** quando é realizada a atualização dos **pacotes acumulados** do RH e não é feita a atualização dos **arquivos do Portal Meu RH**ou vice e versa.  
  
Deste modo é preciso realizar as atualizações em conjunto:  
**1. Baixar** e **aplicar** o pacote de **Expedição Contínua do RH** mais recente no Repositório do serviço **REST**:  
[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854)  
  
**2. Baixar**e **atualizar** os **Arquivos do Portal** para a última versão mais recente:  
[RH - Linha Protheus - MEU RH - Onde baixo a versão mais recente e como atualizar os arquivos do Portal Meu RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729034)  
  
**3. Se depois de atualizar tudo ainda persistir aplica os procedimentos do link abaixo:**  
[**Erro - Invalid return of selector - Fail to write response, the context will be closed. Error: -100**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30488238936343-RH-Linha-Protheus-Meu-RH-Erro-Invalid-return-of-selector-Fail-to-write-response-the-context-will-be-closed-Error-100)  
  
**Saiba Mais**  
[**RH - Linha Protheus - MEU RH - Aprenda sobre o MEU RH e como fazer a implantação**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036164214)  
[**CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI para acessar a documentação de referência sobre o MEU RH**](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
