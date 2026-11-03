---
article_id: 360023409732
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 3418444ef8d66175725de3a4f79cee2cd86c3827dfa7b59481bc7ede2d35c438
fetched_at: '2026-06-28T22:42:10.796531+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - DIMESC - Geração
  da Origem 3 no registro 33 do quadro 12
type: support-article
updated_at: '2023-04-20T17:46:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023409732-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-DIMESC-Gera%C3%A7%C3%A3o-da-Origem-3-no-registro-33-do-quadro-12
---

**Dúvida**Como gerar a origem 3 no registro 33 do quadro 12 ?  
  
**Ambiente**Microsiga protheus - Livros fiscais – A partir da versão 11.80  
  
  
**Solução**

Geração da Origem 3 para somente uma guia de recolhimento

Para gerar a origem 3 no registro tipo 33, é necessário preencher os campos "Número **GNRE** Débitos Específicos" e "Cod.Receita e Classe de venc. Débitos Espec." na wizard de geração do arquivo onde informa a montagem do Registro tipo 31.

**Exemplo:**

**![image2018-3-13_14-7-47.png](http://tdn.totvs.com/download/attachments/344472986/image2018-3-13_14-7-47.png?version=1&modificationDate=1520961750000&api=v2)**

Geração da Origem 3 para mais de uma guia de recolhimento

O sistema faz a seguinte validação para carregar a origem 3 no arquivo conforme abaixo:

*If aScan (aGNRE, AllTrim(SF6->F6\_NUMERO))<>0 .Or.;            //Caso esteja lancado na apuracao de icms atraves de subitem*

*AllTrim(SF6->F6\_NUMERO)$aWizard[15][6] .Or.;          //caso esteja informado no wizard o numero da gnre*

*AllTrim(SF6->F6\_CODREC)+"-"+AllTrim(SF6->F6\_CLAVENC)$aWizard[15][7]    //caso esteja informado no wizard o codigo de receita + classe de vencimento*

*GNR->GNR\_ORIGEM    :=    "3"*

No caso quando é necessário gerar mais de uma guia, ele irá buscar as informações do array *aGNRE*, que por sua vez é alimentada através da apuração do ICMS, quando incluído alguns códigos específicos amarrados a guia de recolhimento, conforme o exemplo abaixo:

![image2018-3-13_14-13-16.png](http://tdn.totvs.com/download/attachments/344472986/image2018-3-13_14-13-16.png?version=1&modificationDate=1520961750000&api=v2)

Cada código na coluna "Código" representa uma operação amarrada a uma guia, sendo feito desta forma a origem 3 será gerada para cada guia.

Os códigos podem ser verificados através do nosso boletim.

**Obs.:** Em ambos os casos, a guia de recolhimento já deve estar cadastrada( Tabela SF6 - Rotina MATA960) e preenchida com todas as informações.

Boletim: https://tdn.totvs.com.br/pages/releaseview.action?pageId=655881026
