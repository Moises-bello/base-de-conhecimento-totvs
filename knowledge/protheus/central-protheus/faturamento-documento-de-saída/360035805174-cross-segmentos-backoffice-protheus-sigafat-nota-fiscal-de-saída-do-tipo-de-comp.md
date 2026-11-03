---
article_id: 360035805174
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 74ff34c2eee9d6f1657106214ddf40e308d75ee85b40734fd4fa41d13b40caba
fetched_at: '2026-06-28T22:38:44.096002+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Nota Fiscal de Saída do Tipo
  de Complemento de Preço
type: support-article
updated_at: '2026-02-09T19:28:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035805174-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Nota-Fiscal-de-Sa%C3%ADda-do-Tipo-de-Complemento-de-Pre%C3%A7o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38279193000599)** **Tempo aproximado para leitura:****00:02:30 min**

**Dúvida**

Quais os procedimentos para lançamento de Nota Fiscal de Saída do Tipo de Complemento de Preço?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Verifique o vídeo How To do processo: [How To | MP - SIGAFAT - Complemento de Preço/Quantidade](https://youtu.be/cBr9Jf93TGI)

Realize o procedimento abaixo para incluir a nota de complemente de preço:

**1.** Insira o Pedido de Venda (**MATA410**);

**2.** Altere o campo "Tipo Pedido (**C5\_TIPO**)" para "**Compl. Preco/Quantidade**";

**3.** Informe o Cliente **(C5\_CLIENTE);**  
Caso o Completo é nota fiscal faturada que utilizou a entidade Fornecedor, é necessário cadastrá-lo como Cliente pra realizar o complemento de preço/ valor.

**4.** Altere o campo "Tipo Compl. (**C5\_TPCOMPL**)" para "**Preço**";

**5.** Informe o produto;

**6.** Informe o valor do complemento de preço nos campos "**Prc Unitario** (**C6\_PRCVEN**)" e "**Vlr.Total** (**C6\_VALOR**)"; preço unitário e valor total devem estar **iguais;**

**7.** Insira o número da nota de origem no campo "**N.F.Original** (**C6\_NFORI**)" e preencha os campos "**Serie Orig.**" e "**Item NF. Orig**"   
Caso o complemento não seja da entidade Fornecedor, há possibilidade buscar pela tecla [**F4**] no campo "**C6\_NFORI**";

**8.** Após confirme e fature a nota.

![complemento_de_pre_o.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360047655673)

**Observação:** Para notas de complemento de preço ou quantidade, a TES utilizada deve ser a mesma da nota fiscal de origem, pois a movimentação é baseada na operação original. Exceções podem ocorrer apenas em situações de complemento de tributos (ex.: ICMS/IPI não destacado na nota original), onde pode ser necessária uma TES com a configuração fiscal correspondente.

Para maiores informações sobre complemento de tributos, orientamos contatar a equipe Protheus Fiscal.

**Saiba mais:**

* [Complemento de Preço / Quantidade](https://tdn.totvs.com/x/ghGWDg)
