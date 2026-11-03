---
article_id: 115013300368
category: ADVPL - Classe e Função
content_hash: c143959db2ad406797c4c90b84df0100b56e732af13ac3ebac66fe1a6afd07b8
fetched_at: '2026-06-28T22:40:19.267648+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Erros Integração
  Excel Ap5_Excel_8 e MsExcel não Instalado
type: support-article
updated_at: '2022-01-10T15:12:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115013300368-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erros-Integra%C3%A7%C3%A3o-Excel-Ap5-Excel-8-e-MsExcel-n%C3%A3o-Instalado
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**Após atualizar o Office ocorreu o seguinte erro: Ap5\_Excel\_8, como resolver?  
Ao realizar a integração excel está mensagem é exibida: **Erro de compilação de modulo oculto: Ap5\_excel\_8 Geralmente esse erro ocorre quando o código é incompatível com a versão, a plataforma ou a arquitetura deste aplicativo. Clique em "Ajuda" para obter informações sobre como corrigir o erro.**

![image2017-8-25 11:41:33.png](http://tdn.totvs.com/download/attachments/286502575/image2017-8-25%2011%3A41%3A33.png?version=1&modificationDate=1503672791000&api=v2)

Na integração aparece a mensagem: **MsExcel nao instalado**  
    ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023621551/mceclip0.png)  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Causa**Erro ocorre devido a versões do Office não homologadas.  
  
**Solução****- Para o erro " Ap5\_Excel\_8 "**Faça um bkp da pasta**c:\apexcel** e excluir a pasta apexcel da estação.  
Exclua o arquivo dll da estação, pois o sistema recria automaticamente.  
Executar a Integração Excel novamente

**- Para o erro " MsExcel não Instalado "**Neste caso verifique a versão do Office, pois essa mensagem ocorre com versões não homologadas.

**[SmartClient Office](http://tdn.totvs.com/display/tec/SmartClient+-+Office)****Saiba mais**[Office suites](http://tdn.totvs.com/display/tec/Office+suites)  
[Office 365](http://tdn.totvs.com/display/tec/Office+365)  
[Disponibilização do binário SmartClient e dependências em arquitetura 64-bit.](http://tdn.totvs.com.br/pages/viewpage.action?pageId=272161372)
