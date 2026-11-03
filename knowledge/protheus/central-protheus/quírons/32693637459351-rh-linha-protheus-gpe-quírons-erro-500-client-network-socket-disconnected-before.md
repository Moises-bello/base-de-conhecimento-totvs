---
article_id: 32693637459351
category: Quírons
content_hash: afddb48bff37ea7eb605fda8191e8505f92cffe9a9788207101ffe0a889d6a50
fetched_at: '2026-06-28T22:42:52.110236+00:00'
product: protheus
section_id: 9033517492119
source: central-protheus
title: RH - Linha Protheus - GPE - Quírons - Erro 500 Client network socket disconnected
  before secure TLS connection was established
type: support-article
updated_at: '2025-06-09T18:11:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32693637459351-RH-Linha-Protheus-GPE-Qu%C3%ADrons-Erro-500-Client-network-socket-disconnected-before-secure-TLS-connection-was-established
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32693670262167) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao tentar realizar integração do Quírons para o Protheus, ou durante tentativa de consumo de dados das APIs do Protheus, é gerado **Erro 500: Erro Inesperado.**  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**O problema ocorre quando a configuração do protocolo de segurança **TLS não está na versão 1.3**, que é a **exigida** para o correto funcionamento entre as integrações Quírons - Protheus.  
  
**Solução**Para solucionar este problema, é necessário fazer as validações abaixo:  
  
**1 -** Verifique se o **Certificado Digital de SSL/TLS** está instalado, e o local de instalação e senha (se houver) estão devidamente informados em seu **appserver.ini** do serviço REST nas seções **HTTPREST** e **SSLConfigure:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32693670264343)  
  
  
**2 -** Em seu appserver.ini do serviço REST, certifique-se que as chaves **SSL2** e **SSL3** estão **desabilitadas**, pois tratam-se de protocolos defasados que foram substituídos pelo TLS:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32693670266007)  
  
  
**3 -** Por fim, configure no appserver.ini do serviço REST o protocolo **TLS 1.3**, que se trata do mais atual/seguro, e é **obrigatório** por parte do Quírons que **não aceita protocolos inferiores:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32693637409559)**Sugerimos que após as configurações acima, seja feito um teste utilizando a ferramenta **Postman** para verificar se o protocolo **TLS 1.3** foi configurado com sucesso. Para isso, basta seguir os passos abaixo:  
  
**>** No Postman, clique na **engrenagem** e em **Settings:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32693637410455)  
  
  
>** Clique em **Certificates** e **informe o local do seu Certificado Digital** para habilitá-lo no teste: **![](https://centraldeatendimento.totvs.com/hc/article_attachments/32693637412247)  
  
  
>** Com a aba da sua requisição aberta, clique em **Settings** e **habilite a opção Enable SSL certificate verifications:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32693670275607)  
  
  
>** Em **Authorization,** selecione em **Auth Type** a opção **Basic Auth,** e ao lado informe o **usuário e senha de acesso ao seu REST Protheus:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32693637414551)  
  
  
  
>** Neste teste, usaremos o método **GET** na API de **Centro de Custo (payrollcostcenter).** Após preencher os parâmetros obrigatórios, que são: **Código da Filial (branchId) e Código do Grupo de Empresas (companyId),** clique em **Send** para obter o resultado do teste:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32693670282007)  
  
  
O resultado acima mostra que as **configurações do protocolo TLS 1.3 estão corretas/ativas,** portanto, a integração entre Quírons e Protheus está pronta para ser utilizada.  
  
Em casos de **erros relacionados ao protocolo TLS ou Certificado Digital** (conforme exemplo abaixo), reveja com seu TI as configurações do ambiente. **![](https://centraldeatendimento.totvs.com/hc/article_attachments/32693637421847)  
  
  
  
Saiba Mais:**  
[REST - Framework](https://tdn.totvs.com.br/pages/releaseview.action?pageId=185747842)
