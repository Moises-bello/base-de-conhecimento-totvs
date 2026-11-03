---
article_id: 23059022049943
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 3f56a663b1d9e0678b368f3fdb7ea5c5b83a00f88544bb6bd31172b72aea1726
fetched_at: '2026-06-28T22:38:42.547872+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Devolução de compras de uma
  nota fiscal de entrada com erros
type: support-article
updated_at: '2024-04-25T20:30:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23059022049943-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Devolu%C3%A7%C3%A3o-de-compras-de-uma-nota-fiscal-de-entrada-com-erros
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23059015648919) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como fazer uma devolução de compras de uma nota de entrada com erros? É recomendável?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Caso identifique que a nota de entrada foi lançada de forma errada em comparação às premissas mencionadas acima (por exemplo com um TES que não está devidamente configurado).

É necessário excluir o documento de entrada e lançar novamente, para então gerar o Pedido e Nota de saída. Não é possível apenas alterar algo no TES pois o comportamento não será mudado visto que a alteração foi depois de já ter lançado a Nota e realizados devidos relacionamentos.

**OBSERVAÇÃO 1:** Não é procedimento correto alterar o cadastro de um TES!

Caso identifique que lançou a nota com um TES que não está de acordo com o especificado, o correto é localizar outro TES já cadastrado que atenda aos requisitos, ou então, incluir o cadastro de um novo TES para atender à necessidade; e então, realizar o lançamento com o TES correto. Porém, deixar o outro TES intacto (pois alterações comprometem o histórico de movimentações no sistema).

Se validar a nota de entrada e estiver correta nos requisitos, tanto Tipo da nota quanto os TES com devidas amarrações, é possível, que algum TES já tenha sofrido alteração no cadastro (justamente o processo que não é indicado).

Desta forma, para fins de TESTE, inclua uma nova nota de entrada igual a nota em questão (mesmo Cliente/produto/TES) e refaça o processo. Poderá validar que, se as amarrações de TES estiverem corretas, de acordo com o orientado aqui, o processo será concluído corretamente.  
Sendo assim, será de qualquer forma, necessário excluir a nota de entrada e lançar novamente para alimentar as devidas tabelas relacionadas.

* Dúvidas sobre a parte do documento de entrada (origem), contate a Equipe Protheus Compras.

**OBSERVAÇÃO 2:** Caso ainda queira devolver essa compra pelo pedido de vendas, siga a documentação do Saiba Mais, no final dessa documentação!

**Saiba mais:**

[**FAT0007 Realizar uma Devolução de Compras**](https://tdn.totvs.com/x/g0FtDQ)
