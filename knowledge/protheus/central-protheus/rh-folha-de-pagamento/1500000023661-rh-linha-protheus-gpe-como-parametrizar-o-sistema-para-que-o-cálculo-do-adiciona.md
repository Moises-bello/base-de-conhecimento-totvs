---
article_id: 1500000023661
category: RH - Folha de Pagamento
content_hash: 76e684254dcce87d95830440f7013a22cbb79d1c0ce16f93b05d7f5aa1aeef9b
fetched_at: '2026-06-28T22:44:11.831424+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE -  Como parametrizar o sistema para que o cálculo
  do Adicional por Tempo de Serviço (ATS) seja sobre salário base mais verbas
type: support-article
updated_at: '2025-08-06T20:18:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000023661-RH-Linha-Protheus-GPE-Como-parametrizar-o-sistema-para-que-o-c%C3%A1lculo-do-Adicional-por-Tempo-de-Servi%C3%A7o-ATS-seja-sobre-sal%C3%A1rio-base-mais-verbas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26355532075031) Tempo aproximado para leitura: 00:04:00 min**  
**Dúvida**Como parametrizar o sistema para que o cálculo do Adicional por Tempo de Serviço seja sobre salário mais verbas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para que o cálculo do ATS seja sobre salário base mais verbas, deve ser feita a parametrização conforme abaixo:  
**IMPORTANTE: Esta alteração deve ser feita com a Data Base do sistema no primeiro dia do mês do inicio do cálculo vigente!**  
  
1. Entre na rotina **Sindicato** (Atualização >Cadastros >Sindicato) posicione no Sindicato em questão e clique em Alterar:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098907814)  
  
Para que as verbas que deverão fazer base para do ATS (adicional por tempo de serviço) (por exemplo verba de falta, atraso, HE, entre outras), entre no cadastro da verba na**rotina Verbas** e na aba **Incidência**, deixe o campo **Adic.T.Serv** com **SIM**:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000028081)  
  
Nesse calculo o sistema buscará as verbas com SIM para ATS e fará a base calculo. Portanto o adicional não entrará para base de calculo de uma hora extra por exemplo.

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
