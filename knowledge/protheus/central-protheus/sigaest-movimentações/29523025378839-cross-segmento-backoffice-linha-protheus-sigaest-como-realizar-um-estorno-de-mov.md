---
article_id: 29523025378839
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 29830cf092ba4da20216300b4ad062991c3cd6ef408277eea39ec7c04a8c39c9
fetched_at: '2026-06-28T22:38:54.200311+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST -  Como realizar um
  estorno de movimentação interna?
type: support-article
updated_at: '2025-12-09T20:24:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29523025378839-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-realizar-um-estorno-de-movimenta%C3%A7%C3%A3o-interna
---

O estorno de movimentação interna no TOTVS Protheus deve ser feito na rotina de origem, sem possibilidade de alterar a data do estorno, que será a data de emissão do movimento original. O estorno é confirmado via menu "Outras Ações" e gera um movimento automático. Para excluir estornos da base, é possível configurar a rotina de recálculo do custo médio, com cuidado ao usar a opção que apaga fisicamente os registros para melhorar a performance.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29523025354519) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como realizar o estorno de uma movimentação interna? qual é a data considerada no estorno interno?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
A movimentação interna, pode ser estornada na própria rotina, e isso depende do tipo de movimento que deseja estornar, pois cada tipo de estorno deve ser efetivado na rotina de origem, **não há consideração de parametros** para setar a data de estorno.

**Por exemplo:** você não pode estornar uma movimentação de transferencia entre armazéns(RE4/DE4), através da rotina de movimentação múltipla, será apresentado o seguinte **HELP A240NAO**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29523025355671)

**Sabendo disso, como é que estorna o movimento interno?**

Quando acessar a sua rotina onde o movimento foi originado, primeiramente pressiona F12 e valide como você quer realizar o estorno, se é "por documento" ou "por item", caso a opção esteja disponível na rotina desejada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29523025356695)

**Qual o procedimento para estornar, após escolha de documento ou item desejado?**

Para isso, clique no menu "**Outras Ações**" e após no sub-menu "**Estornar**".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29523025357847)

Será aberto a tela de movimentação do item, para que você possa conferir o item desejado e então basta clicar em **confirmar**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29523025360151)

Dessa forma o movimento ficara com um X na tela, onde o movimento de estorno assume um movimento automático, se você usou uma TM de devolução, então o estorno será 999, e se você usou uma TM de requisição, então o estorno será 499.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29523025361943)

**Qual será a data gravada após o movimento estornado?**

Sempre será a data de EMISSÃO da origem do movimento, porque o estorno representa o cancelamento da movimentação no período, então ele assume a emissão, uma vez que você não consegue estornar movimentos em um período de estoque encerrado.

Após estornado, o movimento terá preenchido o campo D3\_ESTORNO = S em sua base de dados:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29523109928087)

**Eu tenho muitos estornos, e isso compromete meu espaço de maneira significativa, como eu excluo esses movimentos da minha base de dados?**

Na lista de perguntas da rotina de recálculo do custo médio configure o parâmetro **Apagar Estornos**? com o conteúdo igual a Não, com esta configuração a rotina não irá executar a limpeza de registros estornando gerando uma melhora na performance da rotina.

**(aviso) Importante:** O uso da pergunta "**Apaga Estornos = Sim**" **com o uso de procedures, irá excluir fisicamente** os itens estornados nos movimentos internos da tabela SD3, nos movimentos de requisições por lote da tabela SD5 e nos movimentos de distribuição da tabela SDB, no período executado, afim de diminuir o volume de dados a serem tratados visando melhor performance.

**Já o uso sem procedures**, **estes itens estornados são marcados como deletados permanecendo na base.** O maior motivo de serem marcados com delete é que nas versões antigas do Protheus não era possível no ADVPL excluir fisicamente os registros estornados, apenas marca-los como o delete.

**Saiba mais:**

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA340 - Processo padrão para Inventariar produtos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049739614-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA340-Processo-padr%C3%A3o-para-Inventariar-produtos-no-Estoque)

[*SIGAEST - MILE importação de arquivo da tabela SB7 (Digitação do inventário)*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10573324218007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MILE-importa%C3%A7%C3%A3o-de-arquivo-da-tabela-SB7-Digita%C3%A7%C3%A3o-do-invent%C3%A1rio-)

[*Clique aqui e veja mais artigos sobre Inventário no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538961-SIGAEST-INVENT%C3%81RIO)
