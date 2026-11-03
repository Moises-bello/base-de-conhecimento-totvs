---
article_id: 24650180931607
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 270dd4f241f6563ab8edb07d0ef21928481728b018a45c4f1985889bd8a32f91
fetched_at: '2026-06-28T22:39:56.236171+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Erro ao configurar
  E-mail na rotina FISA022: CRTTBLMAIL(AUTODISTMAIL.PRW)'
type: support-article
updated_at: '2024-07-04T17:59:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24650180931607-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Erro-ao-configurar-E-mail-na-rotina-FISA022-CRTTBLMAIL-AUTODISTMAIL-PRW
---

**Dúvida**No **wizard.config da rotina FISA022**, ao informar os dados do SMTP ocorre o error.log abaixo:  
  
[SQLITE] \*\*\* Check / Rebuild SQLITE Tables FAILED \*\*'.  
in file E:\build-dir\TP11-OF20320-TECXWIN64\lib\sqlite.cpp at line 6658  
on CRTTBLMAIL(AUTODISTMAIL.PRW) 15/04/2024 11:09:27 line : 167  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Para correção do erro é necessário **adicionar as chaves** no appserver.ini do Protheus, dentro da seção General, veja o exemplo:

[General]   
SQLITE\_RebuildTables=0  
SQLite\_CollateRTRIM=0  
SQLite\_TrailSpace=1

**Em seguida esse serviço deve ser reiniciado!**
