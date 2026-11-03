---
article_id: 10378032393239
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 67b1051670cad4d7aa55e3de6f36773d926db0f372fd70ad872db696ad94485b
fetched_at: '2026-06-28T22:42:11.676438+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - GISSONLINE -
  NGISS_T1 - Como preencher o campo TP_DOC_NF - Tipo da Nota Fiscal Tomador ?
type: support-article
updated_at: '2022-11-21T18:37:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10378032393239-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-GISSONLINE-NGISS-T1-Como-preencher-o-campo-TP-DOC-NF-Tipo-da-Nota-Fiscal-Tomador
---

**Dúvida****GISSONLINE - NGISS\_T1** - Como preencher o campo **TP\_DOC\_NF** - Tipo da **Nota Fiscal Tomador**?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais – A partir da versão 12.1.25  
  
**Solução**

Para este campo o sistema busca a informação de 2 lugares:

1.  Do parâmetro **MV\_GISTPNF** conforme configuração abaixo:

O **MV\_GISTPNF** existe para identificar como deve ser preenchido o campo **TP\_DOC\_NF** da **GISS online** quando a escrituração for por tipo tomador de serviço e o atual comportamento do **Protheus** não atende a necessidade da geração do arquivo da **GISS online**.  
As opções disponíveis no *leiaute* da **GISS online** são:

**Tipo da Nota Fiscal Tomador:**  
**1 - Não Retida**  
**2 - Cancelada**  
**3 - Anulada**  
**4 - Isenta**  
**5 - Retida**  
**6 - Pagamento pelo prestador**  
**7 - Imune**  
**8 - S. Judicial**

Ocorre que algumas das opções são semelhantes dentro do **Protheus**, como por exemplo, **"1 - Não Retida"** e **"6 - Pagamento pelo prestador"**. Para evitar que a escrituração em lote seja feita de forma incorreta foi criado o parâmetro para que ao identificar a necessidade, o cliente venha alterar o comportamento do **Protheus** ao gerar o arquivo.  
Assim, as posições do *array* representam as opções existentes no *leiaute* e os valores dispostos em cada posição, o novo conteúdo que deve ser adotado na geração do arquivo da **GISS online** . Caso o *array* possua suas posições sem conteúdo, indicará ao sistema que deve adotar o comportamento padrão do Protheus.  Caso alguma posição do *array* possua conteúdo, o sistema irá preencher conforme configuração daquela posição não afetando os outros tipos de notas.   
  
Assim temos alguns exemplos:

* Preenchimento na situação onde a opção **"1 - Não Retida"** será considerada pela Prefeitura como **"6 - Pagamento pelo Prestador"** e a opção **"2 - Cancelada"**, será considerada como **"3 - Anulada"** e as demais opções continuarão com seu comportamento padrão:  
  **{“6”,“3”,“”,“”,“”,“”,“”,“”}**
* Preenchimento na situação onde a opção **"1 - Não Retida"** será considerada pela **Prefeitura** como **"6 - Pagamento pelo Prestador"** e as demais opções continuarão com seu comportamento padrão.

**{“6”,“”,“”,“”,“”,“”,“”,“”}**

 As posições do *array* não devem ser preenchidas de forma diferente do exemplo acima, ou seja, devem sempre conter um número que referência uma opção do *leiaute*.  
  
Procedimentos para criar o parâmetro:

**MV\_GISTPNF:**

**Tipo**: Caracter

**Conteúdo**: {“”,“”,“”,“”,“”,“”,“”,“”}

**Descrição**: Relação dos tipos de notas de serviços tomados a serem consideradas para o arquivo da GISS Online.

2.  Se o parâmetro **MV\_GISTPNF** não estiver preenchido, o sistema faz a validação conforme abaixo:

Else // se nenhuma posição do array estiver preenchida o sistema faz como sempre fez

```
//Tipo NF
                If !Empty((cAlias)->F3_DTCANC)// cancelado
                    cTipoNf := "2"
                Elseif (cAlias)->F3_ISENICM > 0 // isento
                    cTipoNf := "4"
                Elseif (cAlias)->F3_RECISS $"2N" // retida
                    cTipoNf := "5"              
                Else 
                    cTipoNf := "1" // não retida
                Endif
```

Se **F3\_DTCANC** preenchido , leva =  cancelado cTipoNf := "2"

Se **F3\_****ISENICM > 0**  leva cTipoNf := "4" - isento

Se **F3\_RECISS = 2- Não**  leva cTipoNf := "5" - Retida

Se **F3\_RECISS = 1- Sim** leva cTipoNf := "1" // não retida
