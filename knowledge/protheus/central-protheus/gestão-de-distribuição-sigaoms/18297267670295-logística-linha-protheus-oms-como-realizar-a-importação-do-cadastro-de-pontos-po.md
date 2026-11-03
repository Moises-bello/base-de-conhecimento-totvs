---
article_id: 18297267670295
category: Gestão de Distribuição (SIGAOMS)
content_hash: ccfe8aaffaeaa2ba5e7caf91cfa2b6299baf0f9aea4f152e3cc34ac5de6ba1e6
fetched_at: '2026-06-28T22:45:49.739183+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Como realizar a importação do Cadastro de
  Pontos por Zona e Setor - OMSA090 utilizando o MILE
type: support-article
updated_at: '2025-05-22T19:32:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18297267670295-Log%C3%ADstica-Linha-Protheus-OMS-Como-realizar-a-importa%C3%A7%C3%A3o-do-Cadastro-de-Pontos-por-Zona-e-Setor-OMSA090-utilizando-o-MILE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18297221120407) Tempo aproximado para leitura: **00:01:18 min** **Dúvida**Como realizar a importação do **Cadastro de Pontos por Zona e Setor - OMSA090** utilizando o **MILE**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões.  
  
**Solução**Realize os seguintes passos:

* No **SIGACFG**abra o programa **Manutenção *Layouts* MILE - CFGA600** localizado em **Ambiente > Aceleradores > Mile/*Layouts***;
* No botão **Incluir** selecione a opção **Importação**, a fim de criar o *layout* para importação de registros para o **Cadastro de Pontos por Zona e Setor** no módulo **SIGAOMS**;
* Observe os campos em destaque na imagem abaixo, esse é um modelo de *Layout*:

![omsa090 sigacfg.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18299455771415)

* Em seguida, acesse **Outras Ações >** **Criar de MVC**e informe o código do programa **OMSA090**no campo **Fonte MVC para carga**;
* Será gerado o *layout;*
* Salve o *layout*e acesse o módulo **SIGAOMS**;
* Acione o programa **Cadastro de Pontos por Zona e Setor**, clique no botão **Outras Ações > Outros > Importar**. No botão Arquivo informe o arquivo de Importação, clique em **Importar;**

**![omsa090.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/18299455784343)**

As regiões serão importadas para o **Cadastro de Pontos por Zona e Setor** do módulo **SIGAOMS.****Saiba mais**Para mais informações acesse os *links*abaixo: [MILE - Model Integrator Layout Engine](https://tdn.totvs.com/display/framework/MILE+-+Model+Integrator+Layout+Engine)  
[Cadastro de Pontos Por Setor - OMSA090](https://tdn.totvs.com/pages/viewpage.action?pageId=464948826)  
  
**Glossário**  
**MILE**- *Model Integrator Layout Engine*  
**SIGACFG**- Configurador Protheus  
**SIGAOMS**- Gestão de Distribuição  
  
**Anexo**  
Segue modelo de arquivo de importação para servir como base de utilização dessa funcionalidade:
