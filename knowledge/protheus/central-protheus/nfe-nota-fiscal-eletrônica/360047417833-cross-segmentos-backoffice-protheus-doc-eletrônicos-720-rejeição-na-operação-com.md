---
article_id: 360047417833
category: NFe - Nota Fiscal Eletrônica
content_hash: c85391cb68e329eee49417a1b9f86dd740d72bcab49ea49b0a93bf73622b1c52
fetched_at: '2026-06-28T22:40:05.261114+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 720 Rejeição :
  Na operação com Exterior deve ser informada tag idEstrangeiro'
type: support-article
updated_at: '2025-07-14T14:11:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047417833-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-720-Rejei%C3%A7%C3%A3o-Na-opera%C3%A7%C3%A3o-com-Exterior-deve-ser-informada-tag-idEstrangeiro
---

**Dúvida**Como solucionar Rejeição 720: Na operação com Exterior deve ser informada tag idEstrangeiro  ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

Se gerada  nota com **UF EX e CFOP** de operação do **exterior** iniciado **por 3 ou 7 a TAG****idEstrangeiro** deve ser gerada com conteúdo nulo ou preenchida.

* **Conforme o exemplo abaixo:**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067382314)**

1. Se desejar gerar conteúdo na TAG **idEstrangeiro** se nota de entrada preencher o campo **"RG/Ced.Estr."** **A2\_PFISICA**se nota de saída preencher o campo **"RG/Ced.Estr." A1\_PFISICA**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067383694)**

2. Após isso, **exclua a nota e gere** novamente.

* **Saiba mais:**

Caso ***seja devolução de nota do exterior*** que o emitente seja de SP  ***gerar com CFOP***de operação do exterior.  
  
Neste caso como emitente e o destinatário localizada é de SP o CFOP para autorização da nota o CFOP deve ser de operação interna.

Para verificar mais informações sobre a ***legislação da UF de SP verifique o link abaixo:***  
  
[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=271662609)  
  
  
Caso o fiscal da empresa considere que está correto utilizar CFOP de operação do exterior, como desconhecemos saídas contornos, será necessário realizar uma **consulta formal na Sefaz.**

**NT 2022.002 Exceção:** Poderá ser informada a tag: **dest/CNPJ quando o país do destinatário for o Brasil (tag: enderDest/cPais = “1058”)** e existir algum item com a UF de consumo do **combustível igual a exterior** ***(tag:comb/UFCons =“EX”) e com CFOP = “7667*** - Venda de combustível ou lubrificante a consumidor ou usuário final”.

Para habilitar a opção de complemento de combustível nos Livros Fiscais, você deverá:  
  
1. Incluir um grupo de produto (**Combustíveis**);

2. Alterar o cadastro do produto e vincular o grupo no campo **B1\_GRUPO;**

3. Informar o grupo no parâmetro **MV\_COMBUS;**

4. Após gerar a nota, acessar: **Livros Fiscais > Atualizações > Movimentos > NF-e Manual de Entrada / Saída > Complementos;**

**Na versão 4.00 da NF-e será necessário informar os quatro campos abaixo:  
  
· CD6\_CODANP**

**· CD6\_DESANP**

**. CD6\_UFCONS = EX**

**. CDD\_IFCOMP**

Existe a possibilidade do preenchimento automático dos campos da CD6 para isso usar o ponto de entrada [MATUCOMP](http://tdn.totvs.com/pages/releaseview.action?pageId=6077107)

Existe a possibilidade do campo CDD\_IFCOMP ser preenchido automaticamente. Para isso é necessário ativar o parâmetro MV\_ATUCOMP e usar o ponto de entrada [MATUCOMP](http://tdn.totvs.com/pages/releaseview.action?pageId=6077107)

5. Preencher o CFOP no TES da nota no campo **Cod. Fiscal "F4\_CF" = *7667***

* **Validação da Sefaz:**

![720.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/7406053024919)
