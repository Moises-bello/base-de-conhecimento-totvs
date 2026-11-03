---
article_id: 19839869158679
category: Financeiro - Contas a Receber - Comunicação Bancária Online
content_hash: c47017992d20980398d48b4cf0e2a11843e7e16a8db40784b3287b372e7128d7
fetched_at: '2026-06-28T22:37:49.249986+00:00'
product: protheus
section_id: 26656227629847
source: central-protheus
title: Cross Segmentos - TOTVS BackOffice (Linha Protheus) - FINA713 - Santander -
  Como enviar o IDCNAB via XML para recepcionar no FINA200 a baixa.
type: support-article
updated_at: '2025-06-12T12:43:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19839869158679-Cross-Segmentos-TOTVS-BackOffice-Linha-Protheus-FINA713-Santander-Como-enviar-o-IDCNAB-via-XML-para-recepcionar-no-FINA200-a-baixa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19839853487895) Tempo aproximado para leitura: **00:10:00 min****Dúvida**Como enviar o **IDCNAB** via **FINA713 - Boleto Online - XML** para recepcionar no **FINA200** a baixa e receber mensagem de **"TITULO OK"** no **FINR650 - Retorno de Cobranças** para pré-validar a baixa via **FINA200 - Retorno de Cobranças**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - a partir da release 12.1.33  
  
**Solução**Por padrão, o **Santander** só aceita uma posição de **SEU NÚMERO. *(Essa é uma limitação do Banco Santander.)***

Então só é possível enviar o **Número do Título** ou o **IDCNAB**, ou seja, o Protheus para usar a recepção via **CNAB - FINA200**, é necessário informar no layout da **FINA710 - Configuração de Contas** a informação de **E1\_IDCNAB**, para que no momento do **Download** no BankLine venha a informação de **IDCNAB** para recepção do arquivo de retorno.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19839836625943)

**Saiba mais**

#### **[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Pontos de entrada FINA200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9199530257303-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Pontos-de-entrada-FINA200)** **[Santander - Configuração Boletos - FINA710](https://tdn.totvs.com/pages/releaseview.action?pageId=653588365)**
