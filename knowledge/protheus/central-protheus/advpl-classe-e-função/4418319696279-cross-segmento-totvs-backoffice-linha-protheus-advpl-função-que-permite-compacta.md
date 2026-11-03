---
article_id: 4418319696279
category: ADVPL - Classe e Função
content_hash: 999239207ed4dab6cb9c0524d1a2f2501f902aa48e81dace6d039fb21c7fea8f
fetched_at: '2026-06-28T22:40:16.836454+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Função que permite
  compactar uma pasta ou diretório
type: support-article
updated_at: '2022-01-07T13:32:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418319696279-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-que-permite-compactar-uma-pasta-ou-diret%C3%B3rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**É possível compactar uma pasta ou um diretório?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus – ADVPL – A partir da versão 11.80  
  
**Solução**Para compactar um diretório, é necessário utilizar a função [FZip()](https://tdn.totvs.com/display/tec/FZip) que compacta arquivos, junto com a função [Directory()](https://tdn.totvs.com/display/tec/Directory) que busca os arquivos dentro de um diretório especificado.

Exemplo:

```
User Function fziptst ()  
  
    local nX := 1  
    local aFiles := {}, aFileFun := {}  
    Local cDir := "\imp\teste\"                        //Diretorio da pasta que deseja compactar  
  
    aFileFun := Directory( cDir + "*", "A")            //Busca todos os arquivos do diretorio passado  
  
    For nX = 1 to len(aFileFun)  
        aadd(aFiles, cDir + aFileFun[nX][1])           //Adiciona os arquivos e o diretorio no array aFiles  
    NEXT nX  
  
    nret := FZip("\imp\compactado.zip", aFiles, cDir)  //Compacta os arquivos sem copiar o diretorio  
  
    if nret!=0  
        conout("Não foi possível criar o arquivo zip")  
    else  
        conout("Arquivo zip criado com sucesso")  
    endif  
  
Return
```
