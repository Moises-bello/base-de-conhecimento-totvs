---
article_id: 360020299932
category: ADVPL - Ponto de Entrada
content_hash: ca17baa96cfdfedb39b727496f3fabea78e2498bfb02823f384bcb8b975c1821
fetched_at: '2026-06-28T22:40:12.913374+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Validar o desconto
  no Loja701 (Lj7001)
type: support-article
updated_at: '2022-04-04T11:02:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020299932-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Validar-o-desconto-no-Loja701-Lj7001
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Como validar o total de desconto aplicado por meio de uma (ou mais) NCC (nota de crédito-cliente) utilizando o ponto de entrada LJ7001?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Solução**Será necessária a utilização das seguintes variáveis:

* aNCCItens: Contém todas as notas de crédito-cliente que são apresentadas na tela de seleção de NCC (posição [3][1] indica se a NCC está sendo utilizada):   
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360016427912/mceclip0.png)
* nNCCUsada: Armazena o valor total de desconto por meio de NCCs:  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360016428052/mceclip1.png)
* aTotais: Exibe os valores que compõem a venda:  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360016428252/mceclip2.png)

**EXEMPLO**

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch"  
  
// PONTO DE ENTRADA  
User Function LJ7001()  
    Local nX     := 0        // AUXILIAR PARA LAÇO DE REPETIÇÃO  
    Local nCount := 0        // CONTADOR PARA A QUANTIDADE DE NCCS  
    Local lValid := .T.      // VARIÁVEL DE CONTROLE DE TRANSAÇÃO  
    Local aParam := PARAMIXB // CONTEÚDOS ENVIADOS PELO PONTO  
  
    // (SIMULAÇÃO 01)  
    // PERCORRE O VETOR DE NCCS DO CLIENTE  
    For nX := 1 To aNCCItens  
        // CONTADOR AVALIANDO QUANTAS NCCS FORAM SELECIONADAS  
        If (aNCCItens[nX][1])  
            ++nCount  
        EndIf  
    Next nX  
  
    // (SIMULAÇÃO 01)  
    // CASO SEJA SELECIONADA MAIS DE UMA NCC, EXIBIR MENSAGEM DE ERRO  
    If (nCount > 1)  
        MsgInfo("Não é permitido o uso de mais de uma nota de crédito-cliente por venda", "NCC Error")  
        lValid := .F.  
    EndIf  
  
    // (SIMULAÇÃO 02)  
    // CASO O VALOR TOTAL ABATIDO POR MEIO DAS NCCS SEJA MAIOR QUE 20%   
    // DO VALOR TOTAL DA VENDA, EXIBIR MENSAGEM DE ERRO  
    If (nNCCUsada > (aTotais[4][2] * 0.2))  
        MsgInfo("Valor máximo de abatimento por meio de NCCs excedido", "NCC Error")  
        lValid := .F.  
    EndIf  
Return (lValid)
```

**Observação**  
Por meio do ponto de entrada LJ7001 é possível enxergar cerca de 350 variáveis privadas que representam atributos das tabelas utilizadas e mais outras 60 variáveis (também privadas) contendo informações da rotina (desde tamanho dos campos à dados de pagamento):  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360016430112/mceclip3.png)  
  
Todas essas variáveis podem ser enxergadas por meio da visão de variáveis (*Variables*) do IDE (*Integrated Developmente Environment*) TOTVS Developer Studio.  
  
**Saiba mais**  
[DEPURAÇÃO UTILIZANDO O IDE TOTVS DEVELOPER STUDIO](http://tdn.totvs.com/pages/viewpage.action?pageId=23887932)  
[PONTO DE ENTRADA LJ7001 (VALIDAÇÃO TOTAL DA ROTINA)](http://tdn.totvs.com/pages/releaseview.action?pageId=6790877)  
[PONTO DE ENTRADA LJ7026 (POSIÇÕES DA VARIÁVEL ANCCITENS)](http://tdn.totvs.com/pages/releaseview.action?pageId=6790898)
