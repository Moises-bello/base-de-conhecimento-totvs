---
article_id: 9675385006231
category: NFe - Nota Fiscal Eletrônica
content_hash: d0c83b00dc698c618c7357feb5471f0f1df86bb5e7d9c5b11be304929132081e
fetched_at: '2026-06-28T22:40:01.545942+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 772 Rejeição:
  Operação Interestadual e UF de destino igual à UF do emitente'
type: support-article
updated_at: '2023-01-25T11:57:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9675385006231--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-772-Rejei%C3%A7%C3%A3o-Opera%C3%A7%C3%A3o-Interestadual-e-UF-de-destino-igual-%C3%A0-UF-do-emitente
---

**Dúvida**Como corrigir 772 Rejeição: Operação Interestadual e UF de destino igual à UF do emitente  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.27

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Se operação Interestadual ***(tag:idDest = 2):*** – UF de destino igual à UF do emitente e CNPJ emissor diferente do CNPJ destinatário (NT 2013/005)

O CFOP é de operação interestadual **(inicia por 2 ou 6)**  devem ser utilizados para operações interestaduais.

1.  Se operação dentro da UF o **CFOP** deve ser alterado no TES da nota no campo **Cod. Fiscal "F4\_CF", para um CFOP de operação interna**iniciado por **1 ou 5;**

![CFOP.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11925899941655)

3- Após isso, exclua a **nota e gere novamente.**

***Observação:*** Não rejeitar se existir algum item com a tag UFCons ***(id:L120)*** diversa da UF do emitente

Para habilitar a opção de complemento de combustível nos Livros Fiscais, você deverá:  
  
1. Incluir um grupo de produto (**Combustíveis**);

![GRUPO_DE_PRODUTO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11545575048087)

2. Alterar o cadastro do produto e vincular o grupo no campo **B1\_GRUPO;**

**![GRUPO_DE_PRODUTO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11545575048087)**

3. Informar o grupo no parâmetro **MV\_COMBUS;**

**![MV_COMBUST.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11545713741975)**

4. Após gerar a nota, acessar: **Livros Fiscais > Atualizações > Movimentos > NF-e Manual de Entrada / Saída > Complementos;**

**![COMP._COMBUSTIVEL.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11546411964311)**

**Na versão 4.00 da NF-e será necessário informar os quatro campos abaixo:  
  
· CD6\_CODANP**

**· CD6\_DESANP**

**. CD6\_UFCONS**

**. CDD\_IFCOMP**

Existe a possibilidade do preenchimento automático dos campos da CD6 para isso usar o ponto de entrada [MATUCOMP](http://tdn.totvs.com/pages/releaseview.action?pageId=6077107)

Existe a possibilidade do campo CDD\_IFCOMP ser preenchido automaticamente. Para isso é necessário ativar o parâmetro MV\_ATUCOMP e usar o ponto de entrada [MATUCOMP](http://tdn.totvs.com/pages/releaseview.action?pageId=6077107)

* ***Validação da Sefaz:***

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9675083465751)
