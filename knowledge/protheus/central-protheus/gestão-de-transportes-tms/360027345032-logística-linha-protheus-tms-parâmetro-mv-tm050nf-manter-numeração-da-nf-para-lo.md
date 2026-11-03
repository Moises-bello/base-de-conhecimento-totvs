---
article_id: 360027345032
category: Gestão de Transportes (TMS)
content_hash: 0f8b2f5b9db36ce8e27b1b49cc571ac5ddca145ef325f9577ae227694e80f55f
fetched_at: '2026-06-28T22:45:29.494979+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Parâmetro MV_TM050NF - Manter numeração
  da NF para lotes diferentes
type: support-article
updated_at: '2023-11-21T12:45:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027345032-Log%C3%ADstica-Linha-Protheus-TMS-Par%C3%A2metro-MV-TM050NF-Manter-numera%C3%A7%C3%A3o-da-NF-para-lotes-diferentes
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:50 min****Dúvida**Como permitir a inclusão de documentos com o mesmo número de nota/série/produto em lotes diferentes?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões  
  
**Solução**No **Configurador - SIGACFG** acesse **Ambientes/Cadastros/Parâmetros CFGX017**.   
Caso o parâmetro **MV\_TM050NF** não exista, crie-o conforme imagem a seguir:

![MV_TM050NF.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360027106532/MV_TM050NF.PNG)

Configure com **.F.** para desativar a validação da digitação das notas dos clientes, **permitindo** informar o mesmo **número, série e produto em lotes diferentes**.  
Configure com **.T.**para que o Sistema valide a digitação das notas dos clientes, **não permitindo** informar o mesmo **numero, série e produto em lotes diferentes**. Validação também abrange **cliente remetente e chave da nota**.

1. No **Gestão de Transportes - SIGATMS**, acesse **Atualizações/ Recebimento/ Entrada.Dc.Cliente - TMSA050;**
2. Clique em **Incluir** e informe os dados conforme o *help*de cada campo;
3. Salve e repita o processo com os dados de **Documento/Série/produto.**
