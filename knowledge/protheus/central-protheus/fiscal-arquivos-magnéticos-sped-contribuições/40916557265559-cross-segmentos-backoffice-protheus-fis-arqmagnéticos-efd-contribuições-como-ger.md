---
article_id: 40916557265559
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 8fa39b5ca74e5990e8a08a61dec1639903f18cfa054ef7f1f9eeaf6857ea0d2b
fetched_at: '2026-06-28T22:42:05.128605+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Como gerar os Tributos Genéricos da LC 224/2025 (NT 012/2026) de forma manual,
  quando há débitos apurados no período
type: support-article
updated_at: '2026-06-02T20:56:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40916557265559-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Como-gerar-os-Tributos-Gen%C3%A9ricos-da-LC-224-2025-NT-012-2026-de-forma-manual-quando-h%C3%A1-d%C3%A9bitos-apurados-no-per%C3%ADodo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40916557216791) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como gerar os Tributos Genéricos da LC 224/2025 (NT 012/2026) de forma manual, quando há débitos de **CST 01** apurados no período  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - A partir da versão 2310  
  
**Solução**  
Para inclusão do ajuste, siga os seguintes passos:  
  
**1.** Acesse a **Rotina de Apuração** (FISA001), depois acesse a Sub-rotina de **Ajuste de PIS/COFINS e CPRB** (FISA042) e clique em **Incluir**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40916570750103)  
  
**1.1** Para a geração dos registros é obrigatório o preenchimento dos campos **Ind Ajuste**, **Ajuste**, **Valor Ajuste**, **Cod. Ajuste**, **Data Refe.**, **CST**, **Cod. Contrib** e **Créd/Débito**. Os demais campos são opcionais com base na Nota ou Título que será referenciado no ajuste.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40916570752279)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40916557225111)  
  
**2.** **Processe a Apuração** considerando o período/mês dos registros criados  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40916570754199)  
  
**2.1** Verifique se na aba **Composição dos Débitos**, os valores dos ajustes foram apresentados corretamente e **Confirme** a apuração  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40916557230615)  
  
**3. Gere o Arquivo** também considerando o período/mês dos registros criados  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40916570757015)  
  
**3.1** Ao gerar o arquivo, os registros **M220 e M620** serão apresentados  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/40916570757783)**  
  
**Saiba mais**  
[**Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições - Como gerar os Tributos Genéricos da LC 224/2025 (NT 012/2026)**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/40783586426647-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Como-gerar-os-Tributos-Gen%C3%A9ricos-da-LC-224-2025-NT-012-2026)
