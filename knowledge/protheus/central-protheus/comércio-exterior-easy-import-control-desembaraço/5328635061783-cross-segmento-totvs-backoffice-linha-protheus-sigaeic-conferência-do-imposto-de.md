---
article_id: 5328635061783
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 88e5c081b2460313a1b941f15400b332c1278c5e86cc6995b925f08a0c092cd4
fetched_at: '2026-06-28T22:39:51.013767+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus -SIGAEIC - Conferência do
  Imposto de Importação
type: support-article
updated_at: '2022-04-26T12:18:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5328635061783-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Confer%C3%AAncia-do-Imposto-de-Importa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como realizar a conferência do Imposto de Importação?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Easy Import Control - Todas as versões  
  
**Solução****1.0 Valores Base**  
Os impostos são calculados com base nos seguintes valores:

* Valor FOB, frete, seguro
* Valor CIF
* Despesas base de imposto (base de II)
* Acréscimos /Deduções na adição

**1.1 Valor FOB**  
Custo FOB da mercadoria corresponde ao preço unitário no local de embarque multiplicado pela quantidade, na D.I. é o VMLE (Valor da mercadoria no local de embarque).  
No SIGAEIC, na opção Recebimento de Importação , corresponde ao valor negociado (Vl Neg).  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5326180653847/mceclip0.png)  
Caso este valor esteja incorreto, verifique se:

* A taxa informada no processo esta de acordo com a DI;  
  ![alteracao_taxa.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5326450290967/alteracao_taxa.gif)
* A quantidade, preço e peso dos itens estão de acordo com a Declaração de Importação (DI), este pode ser alterado no Desembaraço, em Outras ações/Itens;  
  ![alteracao_peso.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5326790698903/alteracao_peso.gif)

**1.2 Valor Frete**Frete internacional do processo, na nota fiscal é sempre rateado pelo peso (isto é exigido por legislação), pode ser Prepaid (pago pelo exportador) ou Collect (pago pelo importador). Caso esteja, incorreto verifique o valor informado e taxa do frete.  
  
**1.2.1 Frete Prepaid**  
Na comercial invoice, deve ser colocado no embarque/desembaraço , na opção de inclusão de Invoice . Se na Invoice, o frete estiver destacado dos valores da mercadoria, deve ser preenchido o campo de Frete na Invoice e o campo Frete Incluso deve ficar como NÃO. Se o valor do frete estiver embutido nos valores dos itens da Invoice, o campo Frete Incluso deve ficar como SIM. Neste caso, ele pode ser ou não colocado na capa da Invoice no processo.   
Também deve ser preenchido na aba TRANSPORTE do processo, no campo FRETE PP.  
**1.2.1 Frete Collect**  
Este frete é pago pelo importador aqui no Brasil, portanto é uma despesa, e é o único tipo que gera título no SIGAFIN. Deve ser preenchido apenas no campo FRETE CC da aba Transporte do processo de desembaraço.  
![frete.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5327245570071/frete.gif)

**1.3 Seguro**Sempre é rateado pelo valor do item, caso esteja incorreto verifique o valor e a taxa informados na aba Transporte;  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5327475643671/mceclip1.png)

**1.4 Rateio de despesas base de Imposto de Importação**Favor verifique o documento que consta o criterio de cálculo das despesas: [Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Qual é a fórmula do cálculo do rateio de despesas base de imposto?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053751093)  
A conferência dos valores rateados, pode ser realizada no desembaraço/Recebimento de Importação, nas adições ou nos itens da nota;  
![DESPESA_RATEIO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5328561531543/DESPESA_RATEIO.gif)  
 **1.5 Valor CIF**É composto por:

```
FOB+FRETE+SEGURO+DESPESA (base de Imposto);
```

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5328632534423/mceclip2.png)  
**Observação:** Este pode apresentar o valor incorreto, caso o parâmetro **MV\_EIC0016** esteja habilitado para o processo que possui a DI eletrônica desabilitado, ou seja, parâmetro **MV\_TEM\_DI**=.F.

**1.6 IMPOSTO DE IMPORTAÇÃO**É calculado da seguinte forma:

```
Imposto de Importação = Base de II x Alíquota de II
```

A **Base do Imposto de****Importação** é dada por:

```
Base de II = FOB + FRETE + SEGURO + Despesas base de imposto + Acréscimos – Deduções
```

Para conferência, verifique:

* Se a alíquota do Imposto de Importação que consta na tabela de NCM do item (tabela SYD), encontra-se correta. Em Atualizações -> Tabelas -> N.C.M:  
  ![CONFERENCIA_NCM.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5370111040279/CONFERENCIA_NCM.gif)
* Caso tenha regime de tributação no processo, verifique se a alíquota ad valorem foi informada corretamente para o item; Em Atualizações -> Desembaraço -> Manutenção, posicione no processo e selecione Alterar, após em outras ações-> Regime de Tributação.  
  ![regime_de_tribu__o.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5370828005015/regime_de_tribu__o.gif)

**Observação:** A soma FOB + FRETE + SEGURO + Despesas base de imposto é chamada de CIF , na D.I. corresponde ao "Valor aduaneiro".  
  
**Saiba mais**[Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Como configurar despesa base de imposto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5369655754263)  
[Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Frete TN em território nacional](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418312368407)  
[Recebimento de Importação Nota Fiscal de Importação Divergência de Cálculo](https://tdn.totvs.com.br/pages/releaseview.action?pageId=235581961)
