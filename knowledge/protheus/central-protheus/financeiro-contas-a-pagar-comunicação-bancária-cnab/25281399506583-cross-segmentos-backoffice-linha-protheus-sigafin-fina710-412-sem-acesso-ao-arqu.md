---
article_id: 25281399506583
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: b096e82235e20443d4933ec1118cc3a7db8ccafea00b823053e9fae9388d13bc
fetched_at: '2026-06-28T22:37:56.280671+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710 - 412 - Sem
  acesso ao arquivo PDF no Comprovante de Pagamentos
type: support-article
updated_at: '2024-07-30T18:33:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25281399506583-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA710-412-Sem-acesso-ao-arquivo-PDF-no-Comprovante-de-Pagamentos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25281430033303) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**

No módulo **Financeiro**, ao tentar realizar o download do **Comprovante de Pagamentos** na rotina **FINA710,**ocorre a mensagem de erro **"412 - Sem acesso ao arquivo PDF"**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25281399469079)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2210  
  
**Causa**Esse incidente ocorre, pois a ausência do arquivo **Printer.exe** na pasta do **Appserver** no Servidor.

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse a pasta do **SmartClient** e copie o arquivo **Printer.exe**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25281627535639)**

2. Cole o arquivo **Printer.exe** dentro da pasta do **Appserver**

3. Realize novamente a baixa do Comprovante via **FINA710 - Novo Gestor Financeiro**

**Importante**  
Não é preciso sair da rotina ou reiniciar ambiente

**Saiba mais**

[TOTVS Printer](https://tdn.totvs.com/display/tec/TOTVS+Printer)  
[Bradesco - Configuração Boletos - FINA710](https://tdn.totvs.com/pages/releaseview.action?pageId=638386427)
