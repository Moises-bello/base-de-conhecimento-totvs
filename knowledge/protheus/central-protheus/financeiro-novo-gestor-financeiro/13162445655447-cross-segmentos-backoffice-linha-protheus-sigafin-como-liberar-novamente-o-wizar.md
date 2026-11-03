---
article_id: 13162445655447
category: Financeiro - Novo Gestor Financeiro
content_hash: 7e6355c3cc2cb084ed7792e01e2a5a7903784b98ce33b4b84b97b6df4bc8c07b
fetched_at: '2026-06-28T22:37:41.445505+00:00'
product: protheus
section_id: 33830415324183
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Como liberar novamente
  o WIZARD FINA710
type: support-article
updated_at: '2026-03-30T16:47:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13162445655447-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-liberar-novamente-o-WIZARD-FINA710
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39393089756951) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Como liberar novamente o WIZARD inicial de configuração da FINA710?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Para que o sistema volte a exibir o **Wizard de configuração da FINA710**, será necessário excluir o cadastro gerado na primeira execução do assistente, localizado nos cadastros de rotinas do **Schedule**.

![](https://tdn.totvs.com/download/attachments/271167961/worddav3e2f739e06107ccddc8d4294bce33d7d.png?version=1&modificationDate=1556799043960&api=v2)

Assim, ao abrir a **FINA710** pelo menu, o sistema voltará a exibir a tela inicial do *Schedule.*

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39393085801239)

Caso esteja utilizando a rotina com **PO UI** em conjunto com as portas multiprotocolo ativadas, o comportamento do sistema passa a ser diferenciado.

**Passos para habilitar a Porta Multiprotocolo (MPP):**

1. Edite o arquivo **appserver.ini**.
2. Na seção **[DRIVERS]**, configure:
   * `MultiProtocolPort=1`
   * `MultiProtocolPortSecure=0` (caso não utilize SSL)
3. Na seção **[GENERAL]**, informe:
   * `App_Environment=NomeDoAmbiente`
4. Reinicie o **AppServer** para aplicar as alterações.

Deverá remover o job da FINA711('01'). Acessar a rotina do novo Painel Gestor, será apresentado um assistente (wizard), conforme os passos descritos a seguir:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39393085802519)

A partir desse processo, acesse o **Configurador > Ambiente > Schedule** >**Schedule** e  realize a ativação do agendador.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39393089770135)

Observe que existem duas opções disponíveis: **Smart Scheduler** e **Schedule**.

* Em ambiente **cloud**, recomenda-se utilizar a opção **Schedule**.
* Em ambiente **local**, é possível utilizar qualquer uma das opções.

**Diferença entre as opções:**

* **Smart Scheduler:** [Schedule Protheus - Frameworksp - TDN](https://tdn.totvs.com/display/public/framework/Schedule+Protheus)
* **Schedule:** [Schedule - Como agendar a execução de rotinas - Frameworksp - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=271167961)

**Saiba Mais**  
[Schedule - Como agendar a execução de rotinas](https://tdn.totvs.com/pages/releaseview.action?pageId=271167961)
