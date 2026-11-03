---
article_id: 360018477031
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 7cdf833beca49759e0b97bceb48216058ed6bb0bf6ab2e393e2ca7a07f563030
fetched_at: '2026-06-28T22:42:06.665342+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições,
  campo 19 (DESC_DOC_OPER) do registro F100
type: support-article
updated_at: '2022-09-15T20:35:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018477031-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-campo-19-DESC-DOC-OPER-do-registro-F100
---

**Dúvida**Como preencher o campo **Campo 19 (DESC\_DOC\_OPER)** do registro F100 do arquivo da EFD Contribuições?  
  
**Ambiente**Microsiga Protheus – Livros Fiscais – A partir da versão 11.80.  
  
**Solução**Para o preenchimento do campo **19 (DESC\_DOC\_OPER)** do **registro F100** da **EFD Contribuições**, a rotina utiliza o fluxo abaixo:

1. A rotina avalia se esta sendo utilizado o **ponto de entrada SPD10019**:   
  
<https://tdn.totvs.com/pages/releaseview.action?pageId=189302792>

"Disponível o **ponto de entrada SPD10019** para retornar a descrição desejada a ser impressa no **campo 19 do bloco F100 do EFD**."

2. Caso não esteja utilizando o **ponto de entrada SPD10019**, a rotina buscará informações dos campos **E1\_HIST** ou **E2\_HIST** caso o parâmetro **MV\_DESCDOC estiver igual a .T.**

**Procedimentos para criação do parâmetro na estrutura SX6:**

**Nome da Variável:** MV\_DESCDOC

**Tipo:** Caracter

**Descrição:** Habilita o campo E1\_HIST e E2\_HIST para envio da descrição da operação / documentação no bloco F100 do SPED PIS/COFINS.

**Valor Padrão:** Vazio

Depois que o parâmetro for habilitado, basta preencher o campo Histórico (**E1\_HIST**) e (**E2\_HIST**) para envio da descrição da operação / documentação no bloco F100 do SPED PIS/COFINS.

As informações são buscadas das tabelas **SE1 – Contas a Receber** / **SE2 – Contas a Pagar.  
  
Caso o parâmetro MV\_DESCDOC = Vazio ou .F. será verificado ponto de entrada SPD10019. <http://tdn.totvs.com/dosearchsite.action?queryString=SPD10019>**

3-Caso não esteja utilizando o ponto de entrada e nem o parâmetro MV\_DESCDOC:

> Por Documento de Entrada, Saída e Financeiro (Contas a Pagar e Receber), o sistema leva para o campo 19 a descrição: ***Operação referente o Título :0000XX***  
  
|F100|1|SA10100000301||18092020|1000,00|01|1000,0000|5,0000|50,00|01|1000,0000|6,0000|60,00|||||Operação referente o Título :000012|

> Na rotina Demais Documentos PIS/COFINS - FISA048, o sistema busca informações do campo CF8\_DESCPR:  
  
|F100|1|SA10100005301||01092020|10000,00|02|10000,0000|0,6500|65,00|02|10000,0000|3,0000|300,00|||||***111TESTE***|

![](https://totvssuporte.zendesk.com/attachments/token/hY0CdYxcpmuoZRywWuJaXEAt4/?name=inline1100992639.png)
