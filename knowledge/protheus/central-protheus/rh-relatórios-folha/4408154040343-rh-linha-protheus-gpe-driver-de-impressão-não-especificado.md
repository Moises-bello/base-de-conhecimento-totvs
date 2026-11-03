---
article_id: 4408154040343
category: RH - Relatórios Folha
content_hash: affcf78f9e5b76470a0116b17845afa5678f31ce3ac99a7ef28a10fcdeb62f51
fetched_at: '2026-06-28T22:43:17.398275+00:00'
product: protheus
section_id: 360010843854
source: central-protheus
title: RH - Linha Protheus - GPE -  Driver de Impressão não especificado
type: support-article
updated_at: '2024-08-21T21:11:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408154040343-RH-Linha-Protheus-GPE-Driver-de-Impress%C3%A3o-n%C3%A3o-especificado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25809262059159) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Ao confirmar a impressão de relatórios, sistema emite alerta: Driver de Impressão não especificado.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

Para corrigir esta situação, devem ser executados os procedimentos:

1. Acesse o **SIGACFG - Configurador > Ambiente > Cadastros > Parâmetros**, localizee configure o parâmetro **MV\_DRIVER** como **EPSON** nas 3 linhas da aba **Informações**, ou driver que utiliza para impressão dos relatórios;
2. Acesse o diretório **System** do **Protheus** e verifique se existe o arquivo **EPSON.DRV** ou relacionado ao driver especificado no passo **1.**;
3. Acesse o **SIGACFG** e configure o **Driver de Impressão;**
4. Após executar os procedimentos, reinicie o **Protheus.**

**Importante**

Caso o arquivo do driver de impressão não exista na pasta *System* do Protheus, deverá ser aberto um **ticket** para o **Framework**, solicitando o arquivo do **Driver de Impressão.**

Se o seu ambiente estiver em **Cloud** (banco de dados salvo na nuvem da Totvs), abra uma solicitação direcionada ao **Cloud Totvs** para atualização do diretório.

**Saiba Mais:**

[RH - Relatórios Folha](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010843854-RH-Relat%C3%B3rios-Folha)
