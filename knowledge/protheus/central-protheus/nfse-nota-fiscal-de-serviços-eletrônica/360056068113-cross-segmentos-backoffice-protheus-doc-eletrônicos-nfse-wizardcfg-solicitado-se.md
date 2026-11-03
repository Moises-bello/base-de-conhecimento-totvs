---
article_id: 360056068113
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 7b706dba97f14bbda91476906da6e2bd6b7fae42059e3394e2f7c703489e3adb
fetched_at: '2026-06-28T22:39:58.639364+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Wizard.cfg
  solicitado sempre ao acessar a rotina
type: support-article
updated_at: '2025-05-21T12:15:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056068113-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Wizard-cfg-solicitado-sempre-ao-acessar-a-rotina
---

**Ocorrência**Ao acessar a rotina **FISA022**o Wizard.cfg está aparecendo e sendo solicitado para configuração novamente.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Causa**Esse incidente ocorre por dois principais motivos:  
  
1. Algum dado não está sendo informado nas telas de configuração do Wizard.cfg;  
2. Rotina FISA022 desatualizada.  
  
**Solução**Isso ocorre por falta de preenchimento de algum campo (Usuário, Senha, Token, entre outros).  
  
Exemplo abaixo da prefeitura de Florianópolis, **porém vale lembrar que a disponibilização dos campos ou não, varia de prefeitura para prefeitura.**  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18056565561495)  
  
Portanto, para correção deverão ser preenchidos TODOS os campos dentro do Wizard.cfg, **incluindo o Certificado Digital e Senha.**  
Todos os dados de credenciais deverão ser disponibilizados pela própria prefeitura.  
  
Abaixo a atualização da rotina FISA022 caso necessário:  
- [Protheus 12.1.2310](https://suporte.totvs.com/portal/p/10098/download#detail/1124963)  
- [Protheus 12.1.2410](https://suporte.totvs.com/portal/p/10098/download#detail/1171486)
