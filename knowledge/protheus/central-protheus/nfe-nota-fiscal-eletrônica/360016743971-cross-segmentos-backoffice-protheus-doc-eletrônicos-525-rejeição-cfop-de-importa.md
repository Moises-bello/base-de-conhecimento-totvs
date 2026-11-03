---
article_id: 360016743971
category: NFe - Nota Fiscal Eletrônica
content_hash: 3a31e83e2e5507cb50953e0051284bf959c70db897b32e3d8641f0cf87ae54c2
fetched_at: '2026-06-28T22:40:01.461189+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 525 Rejeição :
  CFOP de Importação e não informado dados da DI '
type: support-article
updated_at: '2025-05-27T14:57:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016743971--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-525-Rejei%C3%A7%C3%A3o-CFOP-de-Importa%C3%A7%C3%A3o-e-n%C3%A3o-informado-dados-da-DI
---

**Dúvida**Como corrigir a rejeição 525 - CFOP de Importação e não informado dados da DI?  
  
   
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

**1-** Quando **não usa integração** com o **módulo SIGAEIC é necessário que o parâmetro MV\_EASY= N**

**![20201201_145829.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360101037393/20201201_145829.gif)**

**2-** Acesse a rotina ****Livros Fiscais**-> **Atualizações**->**Movimentos**->**NF manual de Entrada**->**Outras ações**->**Complementos**->**Importação:****

****![20201201_145142.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360101036933/20201201_145142.gif)****

* Fazer o complemento de **importação nos Livros fiscais.**

```
Campos obrigatórios Nota de Importação:
```

**CD5\_NDI** - Número do Documento de Importação (DI/DSI/DA)  
**CD5\_DTDI** - Data de Registro da DI/DSI/DA  
**CD5\_LOCDES** - Local de desembaraço  
**CD5\_UFDES** - Sigla da UF onde ocorreu o Desembaraço Aduaneiro  
**CD5\_DTDES** - Data do Desembaraço Aduaneiro  
**CD5\_CODEXP** - Código do exportador  
**CD5\_NADIC** - Numero da adição  
**CD5\_SQADIC** - Numero seqüencial do item dentro da adição  
**CD5\_CODFAB** - Código do fabricante Estrangeiro  
**CD5\_VTRANS** - Via de Transporte internacional informada na DI  
**CD5\_INTERM** - Forma de importação quanto a intermediação

* **Importante:**

**Se não tiver D.I, deve seguir o seguinte padrão, conforme está no Manual de Orientação de Preenchimento da SEFAZ:**

* Exemplo prático:

A operação foi concluída sem geração de nenhum documento de importação.  
  
Nesse caso deve ser informada a expressão NIHIL no campo Número DI/DSI/ DIRE,...) – tag nDI.  
  
\* Isso o fonte NFESEFAZ já faz automaticamente, basta deixar o campo **CD5\_NDI** em branco

Continuação do Manual de Orientação da SEFAZ:

Sugerimos repetir a data da emissão da NF-e  **dd/mm/aaaa** no campo Data de Registro do documento (tag dDI");  
  
No campo Local de desembaraço **(tag xLocDesemb)**, informar a unidade de onde foi retirada a mercadora;  
  
O campo Número da Adição **(tag nAdicao)** deve ser preenchido com 999.   
  
Verifique se os campos **CD5\_VTRANS e CD5\_INTERM** estão gravados na tabela CD5.

Segue abaixo o **exemplo do XML**, considerando a data de emissão da NF-e/desembaraço em 08/11/2011, UF = “MG” e via de transporte = “Aérea” (“4”):

- <DI>  
<nDI>NIHIL</nDI>  
<dDI>2011-11-08</dDI>  
<xLocDesemb>local de retirada</xLocDesemb>  
<UFDesemb>MG</UFDesemb>  
<dDesemb>2011-11-08</dDesemb>  
<tpViaTransp>4</tpViaTransp>  
<tpIntermedio>1</tpIntermedio>  
<cExportador>Código do Fornecedor</cExportador>  
- <adi>  
<nAdicao>999</nAdicao>  
<nSeqAdic>1</nSeqAdic>  
<cFabricante>Código do Fabricante</cFabricante>  
</adi>  
</DI>  
  
Ou seja, se tiver NTS (Nota de Tributação Simplificada) ou qualquer outro documento com registro no SISCOMEX, deverá ser digitado esse número no campo“Número DI/DSI/ DIRE,...)” – tag “nDI.”.  
Fora dessas situações, aí sim o campo “Número DI/DSI/ DIRE,...)” – tag “nDI.” será preenchido com a expressão "NIHIL".

* **Validação da Sefaz:**

![](http://tdn.totvs.com/download/attachments/54429084/image2017-8-28%2011%3A37%3A38.png?version=1&modificationDate=1503931059000&api=v2)

![](http://tdn.totvs.com/download/attachments/54429084/image2017-8-28%2011%3A38%3A41.png?version=1&modificationDate=1503931122000&api=v2)

* **Saiba mais:**

Aumentamos o campo **CD5\_NDI  -** Número do Documento de Importação (DI/DSI/DA) para até 15 caracteres, assim será possível registrar informações da **Declaração Única de Importação (DUIMP).**

[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=627094959)

* Para que o campo seja **Aumentado realizar as atualizações do link abaixo:**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota técnica 2020.005](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052495714)
