---
article_id: 360023352291
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 6cee14e0c2406c64a37e5fd5afe80290b88a981230b6a82b2e6999bebc918ef8
fetched_at: '2026-06-28T22:38:39.651736+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Botão Retornar no Pedido
  de Vendas não demonstra ação - F4NAONOTA
type: support-article
updated_at: '2024-02-21T17:49:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023352291-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Bot%C3%A3o-Retornar-no-Pedido-de-Vendas-n%C3%A3o-demonstra-a%C3%A7%C3%A3o-F4NAONOTA
---

**Dúvida**

Botão Retorno no Pedido de Vendas não demonstra ação F4NAONOTA

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - SIGAFAT - Todas as versões.

**Solução**

Ao acessar a Rotina ' **MATA410** - Pedidos de Venda > Ações Relacionadas > Retornar ' , registrar os dados de filtragem e confirmar, o sistema exibe as Notas de Origem para realizar o Retorno. Porém, **ao selecionar o registro que se deseja retornar e clicar em ' Retorno ' o botão de retorno não demonstra nenhuma ação.**

Ou, ao inserir o Pedido de retorno manualmente e procurar a Nota de Origem não localiza / emite o **HELP F4NAONOTA,** esse comportamento de Clicar no Botão Retorno e não obter nenhuma ação é característico de "sujeira de base".

*Geralmente quando o sistema localiza que já há na base um Pedido de Venda incluído com amarração à Nota de Origem.*

 Nas tabelas SC6 - Itens do PV, SC9 - Liberação e SD2 - Itens Doc. de Saída, não podem conter registros com o campo "**XX\_NFORI**" preenchido para a NF/Item/Quantidade em questão.

Caso contrário, o sistema irá associar que já fora realizada a Devolução e o processo não será devidamente realizado.

 Assim, assumir o procedimento:

Realizar um filtro primeiramente em sua Tabela SC6, para o campo **C6\_NFORI** com conteúdo igual ao número da Nota de Origem (a Nota que precisa devolver) para localizar o Pedido de Venda que já há na base para esta NF de origem.

***Obs. 1: O número da Nota deve estar completo, inclusive com os "0" à esquerda para que o Pedido seja localizado.***

***Obs. 2: Verifique se a TES de devolução está compatível com a TES de entrada no campo F4\_TESDV***

 Tendo localizado o(s) Pedido (s) de Venda que já constam no sistema relacionado à esta Nota, considere:

 Não poderá duplicar a informação (ter mais de um Pedido "empenhando" o mesmo saldo do mesmo relacionamento).

 Assim, se realmente ainda houver saldo - se a Nota já não foi totalmente devolvida (\*), então a devolução deverá ser efetuada (faturada) pelo mesmo Pedido de Venda já incluído no sistema;

Ou então, excluí-lo / alterá-lo para eliminar a "sujeira" e então o sistema irá permitir incluir outro Pedido novo para esta NF de origem (carregando o Pedido automaticamente ao clicar em Retornar).

**(\*) Para se certificar de que a nota não foi totalmente devolvida, verifique os campos D1\_VALDEV e D1\_QTDEDEV que não deverão possuir conteúdos iguais ao D1\_TOTAL e D1\_QUANT respectivamente (conteúdos iguais indica que o mesmo valor/quantidade da NF de entrada foram devolvidos).**

**(\*\*) O Help F4NAONOTA também pode ocorrer quando o menu F12, tanto do documento de entrada (mata103)quanto do pedido de venda (mata410), a pergunta de ambos quanto a operação triangular estiver marcado como sim apenas na entrada e não estiver marcado como Sim no pedido de venda, ou vice-versa, o sistema poderá gerar o Help por que não encontra o fornecedor/ cliente correto para a devolução.**

Saiba Mais: **[FAT0041\_Botão\_Retorno\_no\_Pedido\_de\_Vendas\_HELP\_F4NAONOTA](http://tdn.totvs.com/pages/releaseview.action?pageId=234456010)**
