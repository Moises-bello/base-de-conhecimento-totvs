---
article_id: 360057357633
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 50644e6ed7505d00b30b9cb0e05f6781bba7e3d154d0e5fd06a5ddf836da9122
fetched_at: '2026-06-28T22:39:57.564005+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Não foi possível
  salvar o arquivo em diretório local
type: support-article
updated_at: '2025-06-25T21:21:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057357633-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-N%C3%A3o-foi-poss%C3%ADvel-salvar-o-arquivo-em-diret%C3%B3rio-local
---

**Ocorrência**Ao realizar a transmissão de uma nota pela rotina **FISA022** é apresentado a mensagem abaixo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093863694)  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Causa**Esse erro pode ocorrer pelo lado dos dois produtos (Protheus ou TSS).  
A ordem desse processo de forma resumida é a seguinte abaixo:  
  
*- TSS grava o arquivo na pasta FTP/ARQGER/CodigoMunicipio/Arquivo.txt;*  
*- Protheus transfere esse arquivo para a pasta Local (caso tenha sido habilitada no Wizard.cfg).*  
  
**Solução**Caso o arquivo tenha sido salvo na pasta (FTP/ARQGER...), o TSS fez o seu papel e o problema está no Protheus.  
Caso o arquivo não tenha sido gerado na pasta (FTP/ARQGER...) o problema está já no TSS.  
  
Principais pontos à serem checados:  
Se o **problema já estiver no TSS**, verificar:  
- Algum erro no Console.log;  
- Checar se o ambiente está atualizado: [MP - TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-MP-TSS-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS?source=search)  
- Verificar se a seção FTP no appserver.ini está habilitada e configurada.  
  
**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093865454)**  
  
Se o **problema estiver no Protheus**, verificar:  
- Parâmetro **MV\_TSSFTPP** (deverá possuir o mesmo conteúdo da seção [FTP] **do appserver.ini do TSS;**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096126653)  
  
- Checar se está com a última LIB e Appserver (binário);  
- Checar se a pasta local que está sendo escolhida possui permissões para gravações/alterações.
