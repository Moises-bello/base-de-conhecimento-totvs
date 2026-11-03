---
article_id: 360021883451
category: ADVPL - Ponto de Entrada
content_hash: ddc4e1e876478d8e1e19b173f602bc368767229dcc3fe645fc8980a27f721366
fetched_at: '2026-06-28T22:40:11.691037+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Gatilho Mata103
  não executado na importação de pedido
type: support-article
updated_at: '2021-12-27T20:35:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021883451-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Gatilho-Mata103-n%C3%A3o-executado-na-importa%C3%A7%C3%A3o-de-pedido
---

**Ocorrência**Criamos um gatilho para trazer uma informação em um campo customizado da MATA103, porém quando eu clica em Outras Ações/Pedido para realizar a importação do Pedido de Venda já realizado a um fornecedor, o gatilho não é executado, desta forma, não preenchendo o campo customizado.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL – A partir da versão 11.80  
  
**Causa**Este comportamento ocorre devido ao preenchimento das linhas ser realizado diretamente na variável aCols, deste modo, não passando pelas funções de validação de linha da classe MsGetDados().  
  
**Solução**Utilizar o ponto de entrada **MT103FRE** que é chamando após a execução da função Processa() (ao clicar em Salvar na tela seleção de pedido de compras) e antes de retornar o controle para o usuário na tela da rotina de Documento de Entrada (MATA103).  
  
Exemplo  
No exemplo abaixo é realizado o preenchimento de um campo de descrição com base no código do produto informado na variável aCols:

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch"  
  
// FUNÇÃO PRINCIPAL  
User Function MT103FRE()  
    Local aParam   := PARAMIXB  // RATEIO DE FRETE  
    Local aAreaTOT := GetArea() // TABELA POSICIONADA NO MOMENTO  
    Local aAreaSB1 := {}        // POSICIONAMENTO DA TABELA A SER MANIPULADA  
    Local nPosDesc := 0         // ARMAZENA A POSIÇÃO DO CAMPO CUSTOMIZADO D1_XPDDESC (DESTINO)  
    Local nPosProd := 0         // ARMAZENA A POSIÇÃO DO CAMPO PADRÃO D1_COD (ORIGEM)  
    Local nX       := 0         // CONTROLADOR DO LAÇO DE REPETIÇÃO  
  
    // ARMAZENA O ESTADO DA ÁREA CORRENTE DA TABELA SB1  
    DbSelectArea("SB1")  
    aAreaSB1 := SB1->(GetArea())  
  
    // ARMAZENA AS POSIÇÕES DOS CAMPOS D1_COD E D1_XPDDESC COM BASE NA AHEADER  
    nPosDesc := AScan(aHeader, {|x| AllTrim(x[2]) == "D1_XPDDESC"})  
    nPosProd := AScan(aHeader, {|x| AllTrim(x[2]) == "D1_COD"})  
  
    // LAÇO DE REPETIÇÃO PREENCHENDO O CAMPO CUSTOMIZADO COM O CONTEÚDO DO POSICIONE EM B1_DESC  
    For nX :=1 To Len(aCols)  
        aCols[nX][nPosDesc] := Posicione("SB1", 1, FwXFilial("SB1") + aCols[nX][nPosProd], "B1_DESC")  
    Next nX  
  
    // RESTAURAÇÃO DA ÁREA DE SB1 E DA ÁREA ANTERIOR  
    RestArea(aAreaSB1)  
    RestArea(aAreaTOT)  
Return (aParam)
```

**Saiba mais**  
[MT103FRE - Ponto de Entrada para Manipulação do Frete no Documento de Entrada](http://tdn.totvs.com/pages/viewpage.action?pageId=286007787)
