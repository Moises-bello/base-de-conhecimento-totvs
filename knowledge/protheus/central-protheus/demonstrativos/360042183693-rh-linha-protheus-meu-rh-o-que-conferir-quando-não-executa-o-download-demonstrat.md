---
article_id: 360042183693
category: DEMONSTRATIVOS
content_hash: 93bc194c57d5ca1f57b0e36a3838a16e07a9db88dc0a48ae570992bc4253bbdc
fetched_at: '2026-06-28T22:44:38.470924+00:00'
product: protheus
section_id: 10299629664279
source: central-protheus
title: RH - Linha Protheus - MEU RH - O que conferir quando não executa o download
  demonstrativo de pagamento no App Meu RH
type: support-article
updated_at: '2025-12-10T14:40:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042183693-RH-Linha-Protheus-MEU-RH-O-que-conferir-quando-n%C3%A3o-executa-o-download-demonstrativo-de-pagamento-no-App-Meu-RH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24442676779159) Tempo aproximado para leitura: 00:05:00 min**  
  
**Dúvida**  
O que conferir quando não executa o *download* do demonstrativo de pagamento no App Meu RH  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH - todas as versões  
  
**Solução**  
1° No arquivo appsever.ini onde está configurado o ambiente do MEU RH, na *tag **StartPath*** a *system* deve estar com barra invertida no começo e no final conforme exemplo ***StartPath=\system\***  
  
2° São necessários arquivos de binário de impressão diferentes para cada sistema operacional. Esses arquivos devem estar na mesma pasta do appserver e podem ser baixados na sessão abaixo:  
[Central de download - Protheus - TOTVSTEC-FRAMEWORK](https://suporte.totvs.com/portal/p/10098/download#000006/368/)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5741987150359)  
  
Para **Windows:** Utilize o executávelPRINTER.exe:  
x32: <https://suporte.totvs.com/portal/p/10098/download#detail/693163>  
x64: <https://suporte.totvs.com/portal/p/10098/download#detail/693168>  
  
Para **Linux:** Utilize o executável PDFPRINTER:  
x32: <https://suporte.totvs.com/portal/p/10098/download#detail/693159>  
x64: <https://suporte.totvs.com/portal/p/10098/download#detail/693160>  
  
Para **Mac:** Utilize o executável PRINTER:  
<https://suporte.totvs.com/portal/p/10098/download#detail/693162>

**Obs.:** Em ambientes LINUX caso ocorra o erro "***Fontconfig error: Cannot load default config file*****",** seguir o passo a passo da documentação abaixo para a correção.  
[RH - Linha Protheus - MEU RH - Ao baixar o demonstrativo de pagamento em ambiente Linux apresenta erro Fontconfig error: Cannot load default config file](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4439312281879)

**Importante**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5741723637655)  
  
**Documentação de referência:** [**Demonstrativo de Pagamento**](https://tdn.totvs.com/display/NPR/6.0++Demonstrativo+de+Pagamento)  
  
Caso tenha erro por conta da vinculação de participante com as matrículas de funcionários, orientamos conferir o vínculo conforme o artigo a seguir:  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024677334>   
  
**Saiba Mais**  
[**RH - Linha Protheus - MEU RH - Qual a regra para exibir os Demonstrativos de Pagamento (recibos/holerites)**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044237214)  
[**RH - Linha Protheus - MEU RH - É possível visualizar o Demonstrativo de Pagamento somente do mês atual**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044764053)  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
