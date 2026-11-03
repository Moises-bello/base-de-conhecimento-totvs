---
article_id: 4415922787607
category: TAF - eSocial - Instalação
content_hash: 8e60411c32b9b69632a425de9d3e04a51e91c387bcab2b7e6b78b1b6d7068809
fetched_at: '2026-06-28T22:45:11.016799+00:00'
product: protheus
section_id: 1500001536881
source: central-protheus
title: 'RH (LINHA PROTHEUS) - eSocial - TAF eSocial -TSS - Alerta ao acessar rotinas
  do TAF: TOKEN de autenticação obrigatório TAF X TSS - Esta Filial não tem permissão
  para acessar o servidor TSS'
type: support-article
updated_at: '2025-04-11T17:54:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415922787607-RH-LINHA-PROTHEUS-eSocial-TAF-eSocial-TSS-Alerta-ao-acessar-rotinas-do-TAF-TOKEN-de-autentica%C3%A7%C3%A3o-obrigat%C3%B3rio-TAF-X-TSS-Esta-Filial-n%C3%A3o-tem-permiss%C3%A3o-para-acessar-o-servidor-TSS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31349676543895) Tempo aproximado para leitura: **05:00:00 min****Dúvida**Quando acesso o monitor para transmissão de eventos pelo TAF, ou, acesso a tela de diagnóstico do TAF, é apresentado o alerta:

***"CONEXÃO TSS - Totvs Service SOA***

*Mensagem Token inválido*

*TOKEN de autenticação obrigatório TAF X TSS: descrição do Erro:*

*Esta Filial não tem permissão para acessar o servidor TSS. (...)"*

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415891551511)  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - TSS -  Todas as versões

**Solução**

1 - Configurar o TSSINTERFACE, caso não tenha configurado:  
[MP - TSS - Como acessar as interfaces gráficas do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049308093-MP-TSS-Como-acessar-as-interfaces-gr%C3%A1ficas-do-TSS)  
   
2 - Após acessar a Interface Gráfica do TSS, é necessário gerar o TOKEN de autenticação:  
[Configurando TSS com autenticação](https://tdn.totvs.com.br/pages/releaseview.action?pageId=593238229#conf_cred_tss-gerar)  
   
Obs.: Copie os dados referente ao ao CLIENT ID e CLIENT SECRET:  
![](https://totvssuporte.zendesk.com/attachments/token/APqW7swagQ98tW2gU6BKH8ulE/?name=inlineImage.png)  
   
3 - Verifique se o parâmetro MV\_TAFSURL foi preenchido corretamente, contendo a URL do TSS.  
**Observe se a URL está completa, incluindo o http://:**  
[Automação Fiscal - CONFIGURADOR - Como acessar os parâmetros do sistema?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036109233)  
   
4 - Acesse o Programa SIGATAF e a rotina Configurações Gerais TSS. Acesso á rotina "Conf. Gerais TSS": Miscelanea > Rotinas TSS > Conf. Gerais TSS:  
![](https://totvssuporte.zendesk.com/attachments/token/mRPLIzVVU0alZS02VnoVmThv0/?name=inlineImage.png)  
   
5 - Selecione a empresa que foi gerado TOKEN e insira os TOKENS gerados na aba credencial TSS:  
![](https://totvssuporte.zendesk.com/attachments/token/85RgcQkYOeMC7ijsfMPB6j8Q1/?name=inlineImage.png)  
   
6 - Insira a URL do TSS:  
![](https://totvssuporte.zendesk.com/attachments/token/1nlXwUtwaDBprWmsgXhX5VRXD/?name=inlineImage.png)  
   
7 - Informe o certificado digital:  
![](https://totvssuporte.zendesk.com/attachments/token/b33rMcsiL6vR0nqPvEViRzJJW/?name=inlineImage.png)  
   
8 - Após preencher todas as abas, clique em salvar para que as informações sejam inseridas no ambiente.
