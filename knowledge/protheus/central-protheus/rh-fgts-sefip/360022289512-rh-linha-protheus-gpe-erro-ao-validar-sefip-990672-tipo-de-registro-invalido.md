---
article_id: 360022289512
category: RH - FGTS / SEFIP
content_hash: b8e8316d174924156f590430b121e923f03eef8ffb2cc4431c89c5d1e6bbc9e3
fetched_at: '2026-06-28T22:43:41.251494+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: 'RH - Linha Protheus - GPE - Erro ao validar SEFIP: 990672 - Tipo de Registro
  Invalido'
type: support-article
updated_at: '2025-09-04T14:50:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022289512-RH-Linha-Protheus-GPE-Erro-ao-validar-SEFIP-990672-Tipo-de-Registro-Invalido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34697675724311) Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**Ao realizar a validação do arquivo **SEFIP** no sistema da **Caixa Econômica Federal**, gerado pela rotina**GPEM610**, pode retornar o erro "**990672 - TIPO DE REGISTRO INVÁLIDO.**", como no exemplo abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360066332434)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Causa**   
Este erro pode ocorrer caso o arquivo **SEFIP** gerado esteja com espaços em branco em seu leiaute, causando assim o deslocamento das posições no arquivo. Estes espaços em branco em meio ao arquivo gerado são derivados de algum campo de **cadastro do funcionário** estar incorreto, com espaços em branco à mais.  
  
**Solução** **1.** Abra seu arquivo **SEFIP** com o erro;  
**2.** Acesse a linha explicitada pelo validador aqui:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019400891)  
  
**3.** Verifique as posições que estiverem com espaço em branco, fora do leiaute padrão, como no exemplo abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019533652)  
  
**4.** Confira com o leiaute da **SEFIP**, em que posição que o espaço incorreto está inserido e isso demonstrará qual campo está incorreto no cadastro de funcionário;  
**5.** Corrija o campo no módulo de **GPE**;  
**6.** Gere o arquivo da **SEFIP** novamente e será gerado corretamente.

**Saiba Mais:**

[FGTS](https://tdn.totvs.com/display/public/PROT/FGTS) 

[RH - FGTS/SEFIP](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003115651-RH-FGTS-SEFIP)
