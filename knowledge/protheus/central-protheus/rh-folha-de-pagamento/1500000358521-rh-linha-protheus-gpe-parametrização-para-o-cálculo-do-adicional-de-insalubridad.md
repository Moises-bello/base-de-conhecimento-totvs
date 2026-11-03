---
article_id: 1500000358521
category: RH - Folha de Pagamento
content_hash: 0aeb3ce489666a28e51b5ca564f8a487414420fb73a3d4cd38ec3767700f7ca0
fetched_at: '2026-06-28T22:44:16.138973+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Parametrização para o cálculo do Adicional de insalubridade
  sobre salário base mais verbas
type: support-article
updated_at: '2024-09-10T16:43:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000358521-RH-Linha-Protheus-GPE-Parametriza%C3%A7%C3%A3o-para-o-c%C3%A1lculo-do-Adicional-de-insalubridade-sobre-sal%C3%A1rio-base-mais-verbas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26273527462167)** Tempo aproximado para leitura**: 00:02:00 min**  
**Dúvida**Como parametrizar o sistema para que o cálculo do Adicional insalubridade seja sobre salário base mais verbas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para que o cálculo da insalubridade  seja sobre salário base mais verbas, deve ser feita a parametrização conforme abaixo:  
**IMPORTANTE: Esta alteração deve ser feita com a Data Base do sistema no primeiro dia do mês do inicio do cálculo vigente!**  
  
1. Entre na rotina **Sindicato** (Atualização >Cadastros >Sindicato) posicione no Sindicato em questão e clique em Alterar;   
  
2. Clique na aba Perc/Insal;  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101499253)  
  
3. Para as verbas que fazem base para a Insalubridade (por exemplo verba de falta, atraso, hora extra, entre outras), entre no cadastro da verba na**rotina Verbas** e na aba **Incidência**, deixe o campo **Insalubrid.** com **SIM;**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000405181)  
  
Nesse cálculo o sistema buscará as verbas com **SIM** para **Insalubridade** e fará a base calculo. Portanto o adicional não entrará para base de calculo de uma hora extra por exemplo.

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Alteração no cadastro do Sindicato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052464393-RH-Linha-Protheus-GPE-Altera%C3%A7%C3%A3o-no-cadastro-do-Sindicato)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
