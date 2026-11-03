---
article_id: 360025645531
category: Gestão de Transportes (TMS)
content_hash: 514daabd4a0ce06c85a81eab2025aab5e9e6e37491f27d4b81382a36f02fbf89
fetched_at: '2026-06-28T22:45:32.551295+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Rejeição 213 - CNPJ - Base do Emitente difere
  do CNPJ-Base do Certificado digital
type: support-article
updated_at: '2022-06-15T11:29:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025645531-Log%C3%ADstica-Linha-Protheus-TMS-Rejei%C3%A7%C3%A3o-213-CNPJ-Base-do-Emitente-difere-do-CNPJ-Base-do-Certificado-digital
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)* Tempo aproximado para leitura: **00:00:40 min****Dúvida**Como resolver a **Rejeição 213** - **CNPJ** **- Base do Emitente difere do CNPJ** - Base do Certificado digital?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Deve-se verificar se o **CNPJ – Cadastro Nacional da Pessoa Jurídica** Base do emitente foi informado corretamente.  
  
Esta rejeição ocorre quando a **SEFAZ** **- Secretaria da Fazenda**, verifica que o **CNPJ** do emitente está diferente do **CNPJ** do certificado digital utilizado na **assinatura**.  
  
Através do navegador **IE - Internet Explorer**, acessar **Configurações/Opções da Internet/Conteúdo/Certificados**, será possível verificar **Nome da Empresa** e **CNPJ** que foi emitido o seu certificado.  
  
Avaliar se os dados acima são os mesmos registrados no aplicativo utilizado para Transmissão dos Documentos para **SEFAZ**.  
  
No arquivo **XML** do documento, o **CNPJ** é gravado nas ***tags*** em destaque abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024384652/mceclip0.png)

No **TSS – TOTVS Service SOA**, as informações ficam registradas na tabela **SPED001**.
