---
article_id: 360045086954
category: NFe - Nota Fiscal Eletrônica
content_hash: 6bc05529ebd90bfc975ccc5181abacb263e1aab28d399b97b90918211141b701
fetched_at: '2026-06-28T22:40:00.407131+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 029 : Falha de
  schema no grupo de Tags <detExport> '
type: support-article
updated_at: '2021-10-11T15:23:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045086954--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-029-Falha-de-schema-no-grupo-de-Tags-detExport
---

**Dúvida**Como solucionar a rejeição no grupo de TAGS detExport ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

* Para notas emitidas pelo **Faturamento:**

1 - Ao gerar **falha de Schema** referente ao grupo **detExport** verifique se o seu XML gerou conforme o exemplo abaixo:

Se sim, a falha ocorre devido obrigatoriedade das TAGS **nRE, chNFe, qExport**que devem **estar preenchidas as três ou não devem ser geradas.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063327093/mceclip0.png)

2 - Verifique com o fiscal de sua empresa se a exportação é **direta ou indireta**, pois sabemos que a **exportação indireta** há transmissão de uma nota de importação anteriormente, sendo necessário referenciar essa nota no pedido de venda.  
  
Se a mesma for referenciada manualmente os campos **NF . Ori , Serie Ori e Item Ori** devem ser preenchidos. O mais aconselhável é o preenchimento automático pelo gatilho **F4 (Nota de saída).**  
  
Gravando o conteúdo nos campos:  
**D2\_ITEMORI, D2\_SERIORI, D2\_NFORI**  
  
Além disso no complemento de exportação **os três campos são obrigatórios:**

**CDL\_NRREG <nRE>**  
**CDL\_CHVEXP <chNFe>**  
**CDL\_QTDEXP <qExport>**

3 -Em caso de **exportação direta** a **nota não é referenciada** a um documento de entrada e os três campos no **complemento de exportação devem ficar em branco** para que a nota seja transmitida e autorizada.

**CDL\_NRREG <nRE>**  
**CDL\_CHVEXP <chNFe>**  
**CDL\_QTDEXP <qExport>**

* **Saiba mais:**

Foi Ajustada validação para que as *tags*do grupo **exportInd** (Grupo sobre exportação indireta) sejam montadas no Xml **caso a Natureza da Exportação seja Exportação Indireta** e os campos Número do Registro de Exportação (**Nr Registro**), Chave de Acesso da NF-e recebida para exportação (**Chv. NFe**) e Quantidade do item exportado (**Qtde. Exp.**) estejam preenchidos.

* Conforme o parecer da consultoria:

[RICMS/SP - Exportação Indireta - Nota Fiscal de Exportação](https://tdn.totvs.com/x/91OeI)

Para isso, **será necessário estar com o NFESEFAZ** atualizado do link abaixo:

12.1.27:[https://r.totvs.io/p/970079 ;](https://r.totvs.io/p/970079)

12.1.25:[https://r.totvs.io/p/970078 ;](https://r.totvs.io/p/970078)

12.1.23:[https://r.totvs.io/p/970077 ;](https://r.totvs.io/p/970077)

12.1.17:[https://r.totvs.io/p/970076 ;](https://r.totvs.io/p/970076)

Dessa forma o grupo **detExport** só será gerado se o campo no complemento de exportação **CDL\_NATEXP = 1** **Exportação Indireta**

**1 - Exportação Indireta**

**2- Exportação Direta**
