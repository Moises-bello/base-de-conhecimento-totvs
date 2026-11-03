---
article_id: 360004878272
category: Materiais - Compras (SIGACOM)
content_hash: 7301d308c6a3c862eca186d466b1d130ff9c8af95d585a52fe6f9cc519d54439
fetched_at: '2026-06-28T22:41:18.656341+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Falha autenticação
  do M-Messenger - Authentication Failed
type: support-article
updated_at: '2022-11-03T23:44:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004878272-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Falha-autentica%C3%A7%C3%A3o-do-M-Messenger-Authentication-Failed
---

**Dúvida**Ao executar rotinas que enviam e-mail configurado pelo M Messenger, está retornando mensagem de "Authentication failed"

![Capturar2.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360006336451/Capturar2.JPG)  
  
**Ambiente**Protheus – Compras – A partir da versão 12.1.17  
  
**Solução**Para solucionar o problema no envio de e-mail via Messenger, favor verificar configuração do parâmetro MV\_RELAUSR conforme a conta configurada na tela de "configuração do servidor de e-mail" do módulo Configurador do Protheus.

Exemplo:  
Se na tela "Configuração do Servidor de  E-mail" o campo "Conta a ser utilizada para autenticação SMTP" estiver preenchido com : "user@totvs.com", então o parâmetro MV\_RELAUSR deverá ser preenchido com "user@totvs.com", ou seja é o mesmo que informado no parâmetro MV\_RELACNT.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075984914/mceclip0.png)![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075985014/mceclip1.png)

Procedimento:

1. Entre no configurador e acesse o menu Cadastro - Parâmetros

2. Pesquise pelo parâmetro MV\_RELAUSR

3. Informe o email, cuja informação é o mesmo do parâmetro MV\_RELACNT

OBS: Em casos de utilização de e-mail do GMAIL, verificar a liberação conforme nosso documento: [GMAIL nova config. para utilização com o Workflow Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=689063841)

***Saiba Mais :***

* [MP - SIGACOM - Exemplo de configuração Messenger](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011724292-MP-SIGACOM-Exemplo-de-configura%C3%A7%C3%A3o-Messenger)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
