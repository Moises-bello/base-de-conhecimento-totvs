---
article_id: 14124444612887
category: RH - Benefícios
content_hash: 432fb07915352684020488a7a73bf1071d2e9d0ed5d699963f84de01855e0885
fetched_at: '2026-06-28T22:44:03.857764+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Como preencher a Rede de Recarga no arquivo de
  Integração VB Serviços
type: support-article
updated_at: '2025-08-28T02:53:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14124444612887-RH-Linha-Protheus-GPE-Como-preencher-a-Rede-de-Recarga-no-arquivo-de-Integra%C3%A7%C3%A3o-VB-Servi%C3%A7os
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34503210034711) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como preencher a **Rede de Recarga no arquivo de Integração VB Serviços?**  
  
**Ambiente**

TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - Todas as versões

**Solução**  
Para preencher a rede de recarga no arquivo VB, realize os seguintes passos:  
  
**1.**Cadastre os Meios de Transporte através do menu **Atualizações > Benefícios > Vt /Vr /Va > Meios de Transporte,** informe o tipo de benefício e **preencha** o campo **Rede Recarga** na aba VB Serviços;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14123087249943)

**2.** Acesse o arquivo **VB.INI** na pasta **System** e configure a rede de recarga no Identificador **D05ID\_REDECA\_RCG; Essa configuração pode ser realizada de duas formas.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14123191750679)

**1ª Opção:** Chumbar o código da rede de recarga para que sempre seja preenchido com essa rede na geração dos arquivos de integração, exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14123282802583)

**2ª Opção:** Configurar uma fórmula para que o sistema busque a rede de recarga cadastrada no Meio de Transporte, no campo **Rede Recarga** que fica na **tabela RFP, campo RFP\_VBRECA,** exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14123292844567)

**3**. Após configurar o VB.INI com uma das opções acima, gere o arquivo de Integração e abra-o, onde a rede de recarga será apresentada no TXT na linha que inicia com o identificador **5 - Itens Funcionários**, com **inicio na coluna 157.**

**No exemplo abaixo utilizamos a configuração criando a formula no VB.INI**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14126024266903)

**Saiba Mais:**

[RH - Linha Protheus - GPE - Arquivo de Benefícios - BENEFARQ para customizações](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412579856151-RH-Linha-Protheus-GPE-Arquivo-de-Benef%C3%ADcios-BENEFARQ-para-customiza%C3%A7%C3%B5es?source=search)

[RH - Linha Protheus - GPE - Como gerar arquivo de integração de benefícios utilizando a rotina BENEFARQ](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015541491-RH-Linha-Protheus-GPE-Como-gerar-arquivo-de-integra%C3%A7%C3%A3o-de-benef%C3%ADcios-utilizando-a-rotina-BENEFARQ?source=search)
