---
article_id: 18694324704919
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: ece3c6f1504f818cd7ac5ce4b14fa3a7a6a73b6efc2630e74f4ac35440dd3d84
fetched_at: '2026-06-28T22:37:56.353333+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA717 - Erro ao transmitir
  - Falha na comunicação com o Banco do Brasil
type: support-article
updated_at: '2025-05-28T17:34:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18694324704919-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA717-Erro-ao-transmitir-Falha-na-comunica%C3%A7%C3%A3o-com-o-Banco-do-Brasil
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18694336879511) Tempo aproximado para leitura: **00:1****0:00 min****Ocorrência**No módulo Financeiro, ao tentar realizar a transmissão de pagamentos via API - FINA717, ocorre a mensagem de erro **"Falha na comunicação com o Banco do Brasil, verifique com o banco se o serviço de "Pagamentos em lote" está funcionando corretamente"**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18694324685079)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2210  
  
**Causa**A falha mais comum neste caso, será problemas de certificado, como falha na leitura abaixo

Exemplo abaixo

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18694341055639)**

Caso a visualização de seu console.log esteja com a mensagem abaixo ou no retorno do Suporte, deve realizar algumas ações para novos testes e correção

**CFGX060 Wizard de Conversão de Certificado**

Realizar a conversão do **certificado .PFX** seguindo a documentação abaixo

#### **[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Não foi possível gerar os arquivos corretamente Erro ao extrair o Certificado de Autorização no CFGX060 Wizard de Conversão de Certificado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10621741400087)**

Será gerado os arquivos **\*.CERT.PEM e \*.KEY.PEM**Então os arquivos devem ser renomeados suas extensões para  **De .CERT.PEM para  CERT.CRT  
De .KEY.PEM para .KEY.KEY**

Após conversão e adicionados a pasta **Protheus\_data/Cert/NGF**, adicione os certificados na **FINA710 - Configuração de Contas** para o Banco que irá realizar a transmissão de pagamentos

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18694336882839)

Posteriormente realize uma nova transmissão ou transmitir os títulos rejeitados.

**Saiba mais:**

#### **[Contas a pagar (Comunicação bancária online)](https://tdn.totvs.com/pages/viewpage.action?pageId=734394071)**
