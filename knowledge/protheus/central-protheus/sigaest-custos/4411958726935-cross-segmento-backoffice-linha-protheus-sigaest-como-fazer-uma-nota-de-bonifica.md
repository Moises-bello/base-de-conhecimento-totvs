---
article_id: 4411958726935
category: SIGAEST - CUSTOS
content_hash: 3c7bbe560dd4f5d32d666607d1bb17f4fac25e624be58ce87b16a99bb3cefd97
fetched_at: '2026-06-28T22:39:00.755437+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como fazer uma nota
  de Bonificação que atualiza somente quantidade sem atualizar custo ?
type: support-article
updated_at: '2026-06-19T21:23:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411958726935-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-fazer-uma-nota-de-Bonifica%C3%A7%C3%A3o-que-atualiza-somente-quantidade-sem-atualizar-custo
---

O artigo explica como registrar notas de bonificação no TOTVS Protheus, utilizando o campo F4\_BONIF no TES, para atualizar apenas a quantidade do estoque sem alterar o custo do item, mantendo o custo zerado na tabela SD1 e integrando normalmente com os demais módulos.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38662158655127) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**

Como posso fazer uma nota de Bonificação que atualiza somente quantidade, sem atualizar custos e utilizando o conceito do campo F4\_BONIF?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**  
Foi desenvolvida a funcionalidade de registro de notas fiscais de compra em caráter de bonificação, ou seja, a entrada do material **não afetará o seu custo em estoque.**

Com essa nova funcionalidade será possível registrar em uma mesma nota de entrada os itens referentes à bonificação recebida do fornecedor juntamente com itens normais de compra.

Desse modo o estoque do material será atualizado e todas as demais integrações (fiscal, contábil, etc.) serão realizadas normalmente de acordo com o TES, porém o custo do material não será afetado quando for utilizado o conceito de “bonificação”.

Para que o item não tenha o custo de entrada calculado será necessário configurar o novo campo “F4\_BONIF” no cadastro de TES. Ao realizar uma entrada utilizando o TES configurado para “bonificação”, o **sistema não atualizará o custo do item na tabela SD1** (Itens de notas fiscais de entrada), permanecendo zerado.

Segue exemplo:

### **1° Configuração de TES:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411958373399)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411958383895)

### **2° Fazer um Documento de Entrada utilizando a TES correspondente:**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411958407063)

### **3° Validar que apenas a quantidade entrou em seu estoque porém o custo estará zerado por ser tratar de uma nota de bonificação:**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411958488343)

### 

### **Observação:**

### **Caso o campo F4\_BONIF estiver com conteúdo "Não", será custeado o custo do produto da nota fiscal:**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411943685527)

**Curiosidades:**

**Eu não quero que a nota de bonificação, atualize saldo fisico:**

*R: Voce pode usar o conceito de movimentar a nota sem atualizar estoque, isso fara com que não atualize o saldo.*

**Eu não quero que a nota de bonificação, atualize saldo fisico, e preciso movimentar estoque:**

*R: Trativa inexistente no padrão, devera avaliar junto ao seu analista Desenvolvedor, como tratar essa questão mediante uma customização.*

**Saiba mais:**

[*MP - SIGAEST - Como é calculado o campo D1\_CUSTO ao efetuar um Documento de Entrada?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005383202)

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Refaz Custo de Entrada (MATA190) - Conceito e Exemplos*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051999634-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Refaz-Custo-de-Entrada-MATA190-Conceito-e-Exemplos)
