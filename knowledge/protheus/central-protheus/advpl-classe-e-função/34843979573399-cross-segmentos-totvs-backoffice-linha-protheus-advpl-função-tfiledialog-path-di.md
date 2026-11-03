---
article_id: 34843979573399
category: ADVPL - Classe e Função
content_hash: 1a685360e0201a356b2b7bc19238ddfabfeca32cb9960f68abdc6728a4fb3f01
fetched_at: '2026-06-28T22:40:21.673401+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL- Função tFileDialog
  - Path diferente a partir da versão 10.1.3 do WebApp
type: support-article
updated_at: '2025-09-23T19:35:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34843979573399-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-tFileDialog-Path-diferente-a-partir-da-vers%C3%A3o-10-1-3-do-WebApp
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34843979542679) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Após atualização do WebApp para a versão 10.1.3 ou superior, o path retornado pela função tFileDialog está diferente. Como ajustar?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - À partir da versão 12.1.2410  
  
**Solução**  
Caminho da função **tFileDialog** alterado após atualização do **WebApp para 10.1.3 ou superior**  
Se você atualizou seu **WebApp** para a **versão 10.1.3** ou superior e notou que o caminho retornado pela função **tFileDialog** está diferente, saiba que essa mudança é intencional e faz parte do novo comportamento da aplicação.

**O que mudou?**  
A partir da **versão 10.1.3**, quando o parâmetro **lSalvar** é definido como **.F. (falso)**, o **WebApp** não retorna mais o caminho local do arquivo no computador do usuário. Em vez disso, ele realiza um upload do arquivo para uma pasta temporária no servidor de aplicação (o **AppServer**).

O caminho retornado por **tFileDialog** é agora o caminho completo para essa pasta temporária no servidor, e é exatamente esse caminho que deve ser usado para acessar o arquivo.

**Como ajustar?**  
Não é necessário fazer ajustes no seu código. As funções de acesso a arquivos, como **fOpen**, **fRead** e outras, já foram preparadas para lidar com esse novo caminho. Basta passar o caminho completo (o **cRet** da função **tFileDialog**) diretamente para essas funções.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35070559389719)

Exemplo:

```
User Function FLDGTST()

local targetDir := ""
Local nHandle 
Local cString := ""
 
  DEFINE DIALOG oDlg TITLE "Exemplo TFileDialog" FROM 0,0 TO 100,200 PIXEL    
    oBtnFIle := TButton():New( 002, 002, "Abre TFileDialog",oDlg,;
      {||;
        targetDir := tFileDialog( "", 'Selecao de Arquivos',, tmp, .F., ), ;
        msgAlert(targetDir);
      }, 50,10,,,.F.,.T.,.F.,,.F.,,,.F. )
      
  ACTIVATE DIALOG oDlg CENTERED

  nHandle := fopen(targetDir , FO_READWRITE + FO_SHARED )
  cTeste := fRead(nHandle, cString, 100) 

return
```

Essa mudança garante que a manipulação do arquivo ocorra de forma segura e eficiente no ambiente do servidor, sem depender do acesso direto ao disco do cliente.

**Importante:**

Chamada da função **tFileDialog** em ambiente web.  
Por questões de segurança, os navegadores não permitem que uma janela de seleção de arquivos seja aberta sem a interação direta do usuário, como o clique em um botão. Por esse motivo, não é possível chamar a função **tFileDialog** diretamente a partir de uma tela de parâmetros do **WebApp**.

Para que a função funcione corretamente, ela deve ser chamada a partir de uma ação do usuário, como o clique em um botão na sua rotina.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/35070559393431)**

**Saiba mais:**  
[**tFileDialog**](https://tdn.totvs.com/display/tec/tFileDialog)
