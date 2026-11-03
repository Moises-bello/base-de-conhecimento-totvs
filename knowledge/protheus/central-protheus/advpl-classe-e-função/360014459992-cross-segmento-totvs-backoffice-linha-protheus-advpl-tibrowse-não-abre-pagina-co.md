---
article_id: 360014459992
category: ADVPL - Classe e Função
content_hash: be27c1b81c49b7db832c7254451d0f2eb07c864952a0fff9f0f74378f9ff645c
fetched_at: '2026-06-28T22:40:18.093786+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - TIBrowse não abre
  Pagina Corretamente
type: support-article
updated_at: '2022-06-13T21:43:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014459992-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-TIBrowse-n%C3%A3o-abre-Pagina-Corretamente
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:05:00 min  
  
Dúvida**Após alteração da URL por parte do prefeitura de Curitiba, não é mais possível carregar a URL pela TIBrowser. No Internet Explorer funciona normalmente

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009813112/mceclip8.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão P1217  
  
**Solução**

Executar o programa de exemplo disponível no final deste documento.  
Por padrão o componente TIBrowser utiliza sempre o Internet Explorer no modo de compatibilidade do IE7. A única maneira de mudar isso é alterar o registro do *Windows* (<https://msdn.microsoft.com/en-us/library/ee330730.aspx#browser_emulation> seguir procedimento da seção ***Browser Emulation***).

Conforme o documento do MSDN citado acima descreve, o administrador da estação deve seguir os seguintes passos para alterar para a versão 11 do Internet Explorer usado em “Browser Emulation”:

1. Abra o registro do *Windows* (tecla de atalho “*Windows*” + R, digite regedit e tecle <Enter>)![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009812852/mceclip0.png)
2. Navegue até a chave **HKEY\_CURRENT\_USER\Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE\_BROWSER\_EMULATION** ou **HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE\_BROWSER\_EMULATION** (durante os testes, em algumas situações, somente a alteração na chave a partir de **HKEY\_CURRENT\_USER** surtiu efeito, então é importante testar nas duas **HKEY\_CURRENT\_USER** e **HKEY\_LOCAL\_MACHINE**)![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009824331/mceclip1.png)
3. Clique no menu Editar > Novo > Valor DWORD (32-bits)![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009824371/mceclip2.png)
4. Digite o valor **exe** e tecle <Enter>![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009812952/mceclip3.png)
5. Clique com o botão direito sobre o valor smartclient.exe e selecione **..**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009824471/mceclip4.png)
6. Em **Base** selecione **Decimal** e em **Dados do valor** digite **11000** e clique em **OK**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009813012/mceclip5.png)
7. O resultado final deverá ficar como na imagem a seguir:![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009824591/mceclip6.png)
8. Se necessário repita a operação para a chave **HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE\_BROWSER\_EMULATION**
9. Teste o componente TIBrowse, agora ele deverá estar emulando com Internet Explorer 11.![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009813092/mceclip7.png)
10. ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009824691/mceclip9.png)

Exemplo utilizado na customização:

```
#include 'protheus.ch'  
#include 'parmtype.ch'  
#include "totvs.ch"  
  
User Function TiBrowseHTTPS()  
  
DEFINE DIALOG oDlg TITLE "Visualizador de NFS-e" FROM 0,0 TO 768,1024 PIXEL  
  
oTIBrowser := TIBrowser():New(0,0,515,385,"https://isscuritiba.curitiba.pr.gov.br/NotaCuritibana/NotaRPS/AutenticidadeNota/Default.aspx?doc=XXXXXXXXX&num=XXXXXX&cod=XXXXXXX",oDlg )  
  
ACTIVATE DIALOG oDlg CENTERED  
  
Return
```

**Saiba mais:**  
**[Classe TIBrowser](https://tdn.totvs.com/display/tec/TIBrowser)**
