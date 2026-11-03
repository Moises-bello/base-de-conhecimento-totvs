---
article_id: 4413439228695
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: cf85c8b88fa841c2ee408ddd8e85b3172de9b7524c4a3529ee8a3c4d87595863
fetched_at: '2026-06-28T22:42:42.082783+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Conceito de opcionais e como cadastrar
type: support-article
updated_at: '2024-10-30T11:06:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413439228695-Manufatura-Linha-Protheus-SIGAPCP-Conceito-de-opcionais-e-como-cadastrar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Qual o conceito de opcionais e como cadastrar?   
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**A utilização de **Grupo de Opcionais** tem a finalidade de otimizar o processo de cadastramento, produção e estoque, permitindo a montagem de estruturas dinâmicas para produtos com opcionais.  
Para ilustrar o funcionamento desta opção, vamos utilizar como exemplo uma cadeira de madeira que pode ser fabricada em quatro cores diferentes: Preto, Azul Amarelo e Vermelho.  
Apesar das quatro cores possíveis o produto fabricado é um só: **Cadeira**, portanto só haverá um código de produto acabado e o Sistema atualiza o estoque desse produto independente da cor. Assim, se uma **OP - Ordem de Produção** para fabricar 20 cadeiras vermelhas é executada o Sistema atualiza o estoque de **Cadeiras** que é o produto acabado, somando as 20 unidades produzidas ao estoque existente. Não haverá distinção de cor ou estoques separados.  
Por isso, recomenda-se que este recurso seja utilizado para venda sob encomenda, já que o produto final sempre tem o código igual.  
Ao abrir uma **OP** ou um **Pedido de Venda**, é solicitado ao usuário que selecione qual dos opcionais cadastrados para o produto será considerado pelo Sistema.  
Se o usuário não escolher nenhum opcional, será utilizado o opcional padrão que foi selecionado no **MATA010** > **Outras Ações** > **Opcional default**, essa informação também fica gravada no campo**B1\_OPC -** **Opcional Default** no **MATA010 - Cadastro do Produtos**.  
O Sistema baseia-se nos opcionais digitados neste campo para calcular os custos de reposição, formação de preços, etc.  
Se o usuário cadastrar numa estrutura um grupo de opcionais mais de uma vez, será apresentado o grupo para seleção somente uma vez e esta escolha será sempre aplicada ao grupo.  
  
**Exemplo:**

| Grupo de Opcional | Item de Opcional | Descrição |
| --- | --- | --- |
| 001 | PRET | Tinta Preta |

Para que o Sistema considere como padrão a fabricação de cadeiras na cor preta, é preciso informar no cadastro do produto **Cadeira** como **Opcional default** o **Grupo** **001** e o **Item PRET**

Para cadastrar o grupo de opcionais acesse a rotina **MATA256 - Cadastro de grupo de opcionais**, clique em **Incluir** e no cabeçalho preencha o código e descrição do grupo. Abaixo inclua os itens opcionais.   
Na rotina **MATA200 - Estrutura** preencha o código do produto pai, e abaixo inclua as **MPs - Matérias primas** e relaciona cada **MP** ao grupo e item opcional através do campo **G1\_GROPC - Grupo Opcio**. e **G1\_OPC - Item Opcion.**Dessa forma ao cadastrar a **OP** para o **PA - Produto Acabado** ao clicar em confirmar o Sistema abrirá uma tela com os opcionais. Neste momento selecione o opcional que está relacionado com a matéria prima desejada. O grupo de opcionais irá empenhar conforme opção selecionada independente se existe saldo em estoque para a **MP**.
