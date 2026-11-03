---
article_id: 12499053894935
category: Call Center - Help Desk
content_hash: 9397bc0d3122ec7071a1a28554d957b03dcbb1cf77a752a0d88bcce5f1d27b52
fetched_at: '2026-06-28T22:41:27.680081+00:00'
product: protheus
section_id: 1500001537181
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGATMK - Campos "Cod.
  Chamado" (ADF_CODIGO) e "Filial" (ADF_FILIAL) não são preenchidos ao finalizar o
  Teleatendimento (TMKA503A)
type: support-article
updated_at: '2023-02-17T19:43:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12499053894935-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Campos-Cod-Chamado-ADF-CODIGO-e-Filial-ADF-FILIAL-n%C3%A3o-s%C3%A3o-preenchidos-ao-finalizar-o-Teleatendimento-TMKA503A
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**

Campos (ADF\_CODIGO) e (ADF\_FILIAL) não são preenchidos ao finalizar o Teleatendimento (TMKA503A)

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGATMK - Todas as versões  
  
**Causa**Esse incidente ocorre, pois a parametrização do cadastro do "Modelo de Atendimento" (CFGX503B) não está configurada com os campos "Cod. Chamado" (ADF\_CODIGO) e "Filial" (ADF\_FILIAL).  
  
**Solução**Para solucionar esse problema, acesse o "Configurador" (SIGACFG) e siga os seguintes passos:  
  
1-No "Configurador" (SIGACFG), siga o menu "Ambiente>Cadastro>Modelo de atendimento".  
2-No cadastro de "Modelos de atendimento" (CFGX503B) acesse a opção "Alterar" no respectivo código da tabela ADE e ADF conforme imagem abaixo:  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12498785946263)  
OBS: Esse cadastro é criado automaticamente ao realizar um atendimento dentro da rotina TMKA503A

3- Selecione a opção Avançar.  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12498168259863)

4-Selecione novamente a opção Avançar.  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12498259714967)  
  
5-Dentro da tela de "Relacionamentos existentes" as configurações "Campo na tabela do cabeçalho" e "Campo na tabela de Itens", devem estar preenchidos com o relacionamento do campo, caso o registro esteja em branco, preencha os campos:

* "Filial" (ADE\_FILIAL) e "Filial" (ADF\_FILIAL)
* "Codigo" (ADE\_CODIGO) e "Cod. Chamado" (ADF\_CODIGO)

Conforme imagem abaixo:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12498386261911)

6- Avance as próximas 3 opções e Finalize a operação.

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12498665277207)

**Saiba mais**: [Modelo de Atendimento (CFGX503b - SIGACFG)](https://tdn.totvs.com/pages/releaseview.action?pageId=306855363)
