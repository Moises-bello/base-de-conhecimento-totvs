---
content_hash: 8bcb88bdaa80176cce751e119fa267408f8202b228dd2564b27f272b3f23f3db
fetched_at: '2026-06-29T00:05:58.396456+00:00'
page_id: '185757276'
product: rm
source: tdn-rm
title: Como Fazer - Estornar item não Recebido - TOTVS Gestão de estoque, compras
  e faturamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185757276
version: 4
---

|  |  |
| --- | --- |
| Linha | RM |
| Produto | TOTVS Gestão de Estoque, Compra e Faturamento |
| Versões | A partir da 11.50 |
| Processo | Movimentos |
| Subprocesso | Estornar item não Recebido |
| Data da publicação | 16/04/2015 |

**Como Fazer**

 

Como utilizar o recurso de Estornar Item não Recebido?

**Descrição do Processo**

 

A utilização da rotina de Estornar Item não Recebido tem como objetivo reabrir uma cotação e a solicitação de compras relacionada a esta cotação, a partir de uma ordem de compra parcialmente recebida ou, estornar itens que não fizeram parte de uma cotação em um movimento de solicitação de compras, se este movimento for originado do TOP (TOTVS Construção, Obras e Projeto) ou se possuir movimentos anteriores.

Este processo poderá ser usado tanto para movimentos gerados pelo módulo de cotação quanto no faturamento normal de movimentos.

Geralmente surge a necessidade de utilização deste processo quando o Usuário deseja aproveitar os itens que não foram faturados ou, parte do item, no movimento de origem para geração de outro movimento destino.

Neste caso, o Usuário passa a contar com a rotina de Estornar Item não Recebido, a qual faz com que o sistema exclua os itens não recebidos do movimento em questão e reabra o movimento de origem alterando o Status deste Pedido/Solicitação/Cotação para ‘Parcialmente Recebido’ ou "Ordem de Compra Parcialmente Gerada", possibilitando o recebimento deste movimento ou cotação.

OBS: Quando temos um movimento oriundo do TOP que tenha passado por vários faturamentos dentro do sistema TOTVS Controle de Estoque e Faturamento (Nucleus), somente será estornado a quantidade para o TOP quando for executado o processo de "Estornar Item não Recebido" no movimento que teve como origem o TOTVS Construção Obras e Projetos.

**Exemplo:**

Foi criado um movimento do tipo 1.1.04 que teve origem no TOP e este movimento contem 3 itens.

Foi faturado esse movimento integralmente para outro movimento de solicitação do tipo 1.1.05.

Este movimento do tipo 1.1.05 teve 2 dos seus 3  itens envolvidos no processo de cotação.  
Os dois itens foram cotados e após a cotação, foi gerado um movimento do tipo 1.1.03 a partir da cotação para representar a ordem de compra.

O item que sobrou no movimento 1.1.05, poderá ser estornado para o movimento anterior (1.1.04) reabrindo o movimento com a quantidade do item estornado e o movimento do 1.1.05 é encerrado (Status = Recebido). Neste momento, ainda não ocorreu nenhum estorno para o TOP.

Em seguida, é possível neste movimento 1.1.04 que teve origem do TOP, executar o processo de Estornar Item não Recebido" para que quantidade retorne para o pedido do TOP e seja disponibilizada para gerar novos pedidos seja de compra ou cotação.

Após estornar todos os itens necessários, o status do movimento 1.1.04 ficará como recebido.

**Passos para realização do processo:**

- Selecionar movimento a ser Estornado;

- Acessar botão Processos;

- Selecionar opção "Estornar Item não Recebido";

- Marcar o(s) item(ns) que será(ão) estornado(s);

- Clicar em Executar;

**Aplicação dentro do Sistema**

 

Para um melhor entendimento sobre o ato de Estornar item não Recebido, será exemplificado dentro de um caso prático:

*TOTVS Gestão de Estoque, Compras e Faturamento*  GDP Materiais 2

Incluir um movimento do tipo 1.1.XX de Solicitação de compras com dois Itens.

Após salvar o movimento Gere uma cotação utilizando esta solicitação e a partir desta cotação gere uma ordem de compras.

A nota fiscal relacionada a esta Ordem de Compra chegou na empresa, porém nem todos os itens foram recebidos, assim foi feito o recebimento parcial, ou seja, recebeu-se apenas 1 dos itens. Deixando assim o movimento de Ordem de Compra, com 1 item ainda por receber e com o status de "Parcialmente Recebido".

O Fornecedor que disponibiliza o item restante aumentou o valor deste e será necessário cotar novamente este produto para realizar uma compra mais em conta.

Seleciona-se o movimento que possui o item que será cotado novamente, estornando o item desejado, cota-se o mesmo novamente utilizando a mesma cotação, ou exclui-se o item desta cotação (ato que alterará o status desta cotação para "Pedido de compra" novamente), e gera-se uma nova cotação a partir da solicitação de compras gerada que agora se encontrará com status Pendente.

**Informações Adicionais**

Este processo utiliza do processo de conclusão de movimento ao estornar o item não recebido, ou seja, movimento que teve todos os itens recebidos será concluído.

Este processo só pode ser executado em movimento com status ‘Parcialmente Recebido’.

O Estorno de Itens não Recebidos realiza todas as operações para que o sistema identifique o movimento como se o mesmo tivesse sido totalmente recebido/faturado. Estas operações são: Estorno do efeito do estoque, do orçamento, do financeiro.

Após o item ser estornado o status do movimento é alterado para Recebido ou Faturado, conforme tipo de movimento utilizado.

O movimento que teve todos os itens não recebidos estornados, não estará disponível para continuar o faturamento.

Atualmente não tem como desfazer este processo.

Este processo não poderá ser executado em movimentos do tipo 1.2.xx ou 2.2.xx.

É preciso dar permissão ao perfil do usuário para ter acesso a este processo na visão de movimentos, através da aba "acesso a menus" no cadastro de perfis.

Para o correto funcionamento do processo é preciso que o módulo de Cotação esteja parametrizado para que a Cotação permita Gerar Cotação Parcialmente Cotada.

Data de Produção do Documento: 28/02/2012
