---
article_id: 4439312281879
category: DEMONSTRATIVOS
content_hash: a2e5065f99515648808b518d27eea9efe8a5a525bf186486a761b7e47907ee14
fetched_at: '2026-06-28T22:44:38.401518+00:00'
product: protheus
section_id: 10299629664279
source: central-protheus
title: 'RH - Linha Protheus - MEU RH - Ao baixar o demonstrativo de pagamento em ambiente
  Linux apresenta erro Fontconfig error: Cannot load default config file'
type: support-article
updated_at: '2026-06-23T21:02:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4439312281879-RH-Linha-Protheus-MEU-RH-Ao-baixar-o-demonstrativo-de-pagamento-em-ambiente-Linux-apresenta-erro-Fontconfig-error-Cannot-load-default-config-file
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24769109226775) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Ao baixar o demonstrativo de pagamento em ambiente Linux apresenta erro *Fontconfig error: Cannot load default config file* **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - MEU RH - Todas as versões **Solução**Se o appserver está sendo executado em LINUX que não possui um X *SERVER* (modo gráfico), a geração de relatório via *JOB* não ocorrerá e a mensagem ***"Fontconfig error: Cannot load default config file"*** será exibida no console.log conforme exemplo abaixo.  
  
Ou seja, o arquivo .PDF só é gerado com o LINUX em **modo gráfico**.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4439246733463)  
  
No appserver.ini onde está configurado o ambiente do MEU RH na *tag* ***StartPath*** a system deve estar conforme exemplo ***StartPath=/system/*  
![](https://totvssuporte.zendesk.com/attachments/token/9S0qRqx68xE0uViDNP5DjIrcH/?name=inline1736443400.png)**São necessários arquivos de binário de impressão diferentes para cada sistema operacional. Esses arquivos devem estar na mesma pasta do appserver e podem ser baixados na central de downloads: **Protheus - TOTVSTEC-FRAMEWORK - SMARTCLIENT**

Para **Linux****:** Utilize o executável PDFPRINTER

x32: <https://suporte.totvs.com/portal/p/10098/download?e=693159>  
x64: <https://suporte.totvs.com/portal/p/10098/download?e=693160>  
  
Para que o pdf seja gerado é necessário que o Totvs Printer esteja na pasta appserver e smartclient do MEU RH e que a impressão seja "setada" para server. 

Importante: 

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24769139123735)  
Segue abaixo documentações de referência sobre configurações adicionais em Linux:  
[TOTVS Printer](https://tdn.totvs.com/display/tec/TOTVS+Printer)  
[Agente TOTVS Printer](https://tdn.totvs.com/display/tec/Agente+TOTVS+Printer)  
[Agente TOTVS Printer para Linux sem GUI](https://tdn.totvs.com/display/tec/Agente+TOTVS+Printer+para+Linux+sem+GUI)  
  
**Saiba Mais  
[RH - Linha Protheus - MEU RH - Qual a regra para exibir os Demonstrativos de Pagamento (recibos/holerites)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044237214)  
[RH - Linha Protheus - MEU RH - O que fazer quando download de demonstrativo apresenta "Falha ao carregar documento PDF"](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042996014)  
[RH - Linha Protheus - MEU RH - É possível visualizar o Demonstrativo de Pagamento somente do mês atual](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044764053)**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
