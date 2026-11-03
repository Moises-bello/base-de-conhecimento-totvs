---
article_id: 360060595513
category: Encargos
content_hash: e45d9520bdba6e64223fc577a3c3b7d2765a3d274b9badc296ac7a1d37c65718
fetched_at: '2026-06-28T22:46:53.280296+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: 'RH - RM - FOP - SEFIP: PIS/PASEP/CI Inválido'
type: support-article
updated_at: '2022-07-25T17:51:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060595513-RH-RM-FOP-SEFIP-PIS-PASEP-CI-Inv%C3%A1lido
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:01:20 min  
  
Ocorrência**Após gerar o arquivo **SEFIP** e importar para o aplicativo, é apresentada a  mensagem de erro: **PIS/PASEP/CI Inválido**. **Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
**Causa**Esse incidente ocorre quando, no cadastro do funcionário, o número **PIS/PASEP** está incorreto, ou quando antes do processo de geração da **SEFIP** não foi realizada a rotina **Liberação de Flags de FGTS.** Deve-se lembrar que a Liberação de Flags de FGTS tem o intuito de validar alterações cadastrais apresentadas na rotina antes de emitir a SEFIP.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. No cadastro do funcionário confira o número do **PIS/PASEP**;2. Acesse **Encargos | Liberação de Flags FGTS**;  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000297062/mceclip0.png)  
  
3. Realize a geração da **SEFIP** novamente e importe para o aplicativo.
