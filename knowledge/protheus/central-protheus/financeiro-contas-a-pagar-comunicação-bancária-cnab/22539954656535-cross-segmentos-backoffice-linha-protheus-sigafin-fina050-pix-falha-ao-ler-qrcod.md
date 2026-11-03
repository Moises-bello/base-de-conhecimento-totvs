---
article_id: 22539954656535
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 5421acde1e241056383245ce4d746180528eb1e530ac87dc7fd6e2487f42f8d2
fetched_at: '2026-06-28T22:37:55.394895+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA050 - PIX - Falha
  ao ler QRCODE, o Programa Barcode_Scan não foi localizado
type: support-article
updated_at: '2024-11-18T18:03:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22539954656535-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA050-PIX-Falha-ao-ler-QRCODE-o-Programa-Barcode-Scan-n%C3%A3o-foi-localizado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22539954633239) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No módulo Financeiro, ao tentar realizar a leitura do QRCODE do PIX para gravar as informações na aba PIX do complemento do título, ocorre a mensagem **"Falha ao ler QRCODE, o Programa Barcode\_Scan não foi localizado na pasta onde fica o client da aplicação. Favor Verificar"  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22539964787991)**  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Esse incidente ocorre, pois o "**Barcode\_Scan.exe**" não está pasta do Smartclient, onde é necessário o Software para leitura do **QRCODE** em tela  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o <https://suporte.totvs.com/> e buscar por **"BARCODE"**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22539964789271)  
2. Efetue o download conforme versão do sistema operacional  
3. Cole o Software na pasta do ***Smarclient*** na máquina de execução ou servidor, que é apontado o atalho na máquina   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22539964789783)

4. Posteriormente clicar no ícone para ler o *QRCODE* novamente.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22539964790679)

5 -Esse erro ocorre quando há um espaço no nome de alguma pasta no caminho até o executável. Por exemplo, se uma pasta no caminho se chama **'QRcode Banco'**. No entanto, se não houver espaço nos nomes das pastas, o problema pode estar no nome do usuário criado na máquina até a pasta do Smartclient conforme exemplo abaixo:

"C:\Users\Usuario Protheus\Desktop\SmartClient\_1212210\_Smartclinet\".

***Obs: O Barcode\_Scan, deve ser usado localmente na máquina do agente, atalhos de uso de drives, sharepoint ou pastas de redes externas, afetam diretamente a chamada do Software gerando no Smartclient***

**Saiba mais:**

[Pagamentos instantâneos - PIX](https://tdn.totvs.com/pages/releaseview.action?pageId=569478747)

[Barcode scan](https://tdn.totvs.com/display/tec/Barcode+scan)
