---
article_id: 20761026008727
category: RH – DIRF
content_hash: 2a333e06111a63bf31c889ea138e8b2ab97fcd6fd8064f0cd0b505eb145d16d0
fetched_at: '2026-06-28T22:44:07.038412+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: 'RH - Linha Protheus - GPE - Log de Confirmação de Envio de Informe de Rendimento
  por Email '
type: support-article
updated_at: '2024-01-23T10:59:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20761026008727-RH-Linha-Protheus-GPE-Log-de-Confirma%C3%A7%C3%A3o-de-Envio-de-Informe-de-Rendimento-por-Email
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20761025938071) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como emitir o Log de Confirmação de Envio de Informe e Rendimento por Email?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - À partir do Release 12.1.33  
  
**Solução**Implementado as seguintes melhorias no processo de envio do Informe de Rendimento po Email:

1. Troca do assunto do email para "Informe de Renfimento referente ao ano de <ano de referência>":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20761025941527)  
  
  
2. Geração de Log de Confirmação de Envio de Email com relação de:  
  
A) Quantidade de matriculas cujo email foi enviado e quantidade de matriculas cujo email não foi enviado.  
B) Dados (Filial/Matricula/Nome) dos funcionários cujo Informe de Rendimentos foi enviado com sucesso.  
C) Dados (Filial/Matricula/Nome) dos funcionários cujo Informe de Rendimentos não foi enviado e o motivo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20761025944855)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20761034638871)

No Log de Confirmação de Envio de Email são verificados os seguintes motivos de falha no envio:

**Falha no envio de E-mail - Verifique o E-mail (RA\_EMAIL) do funcionário.**![](https://centraldeatendimento.totvs.com/hc/article_attachments/20761025951383)

**Falha de Anexo do Arquivo - Verifique as configurações de Permissão do caminho indicado no parâmetro MV\_RELT.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20761034647319)

**Falha na Autenticação no Envio do E-mail - Verifique o conteúdo dos parâmetros MV\_RELACNT e MV\_RELPSW.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20761034653975)

**Falha na Configuração de Servidor de Email - Verifique a configuração de servidor de email no módulo SIGACFG e parâmetros.**![](https://centraldeatendimento.totvs.com/hc/article_attachments/20761025964183)  
  
**O servidor de SMTP (o parâmetro MV\_RELSERV) não foi configurado:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20761025966743)

**A conta de email (parâmetro MV\_EMCONTA) não foi configurada.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20761025969943)  
  
**Senha da conta de email (parâmetro MV\_EMSENHA) não foi configurada.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20761025975191)

**Saiba Mais:**[Informe de Rendimentos Log de Confirmação de Envio de Email](https://tdn.totvs.com/pages/releaseview.action?pageId=820180754)   
[RH - Linha Protheus - GPE - Como Enviar Informe de Rendimento por E-mail](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9990125136919-RH-Linha-Protheus-GPE-Como-Enviar-Informe-de-Rendimento-por-E-mail)   
[RH - DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
