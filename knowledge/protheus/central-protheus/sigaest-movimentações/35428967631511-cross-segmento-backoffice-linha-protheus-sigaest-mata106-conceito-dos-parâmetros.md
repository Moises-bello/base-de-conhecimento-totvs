---
article_id: 35428967631511
category: SIGAEST - MOVIMENTAÇÕES
content_hash: a9e4a1a4637fb7f1e54b720b06fafebaea3b3dac3099c415913bc288fceb91de
fetched_at: '2026-06-28T22:38:55.732337+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA106 - Conceito
  dos parâmetros: Considera o Armazém da SA?, Saldo do Armazém? e Saldo Até o Armazém?'
type: support-article
updated_at: '2025-10-14T17:58:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35428967631511-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA106-Conceito-dos-par%C3%A2metros-Considera-o-Armaz%C3%A9m-da-SA-Saldo-do-Armaz%C3%A9m-e-Saldo-At%C3%A9-o-Armaz%C3%A9m
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35428967627031) Tempo aproximado para leitura: **03:00 min**  
  
**Dúvida**  
Qual a funcionalidade dos parâmetros: Considera o Armazém da SA?(MV\_PAR04), Saldo do Armazém?(MV\_PAR05) e Saldo Até o Armazém?(MV\_PAR06) na rotina Gerar Pré-Requisição MATA106?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Quando o pergunte MV\_PAR04 = Considera o Armazém da SA? está desativado(Não), ele não irá considerar os saldos do armazém informado na SA, e os parâmetros MV\_PAR05 = Qual o armazém no "DE" e MV\_PAR06 = Qual o armazém no "ATÉ" passam a ser considerados. Porém, os mesmos **servem único e exclusivamente para validar se possui saldo do produto para atender a SA** dentro do range informado nos parâmetros(Armazém DE/ ATÉ), para que o sistema gere ou não uma Solicitação de Compra(caso o pergunte esteja ativado), para atender a SA. Caso tenha saldo o suficiente para atender à SA em um desses armazéns(diferente do informado na SA), a Pré-requisição será gerada normalmente.

**Ou seja, a requisição em si sempre será realizada para o armazém informado na SA independente da configuração dos parâmetros informado anteriormente nessa documentação.**

Segue exemplo do processo:

Será gerado uma Solicitação ao Armazém e um armazém que não tem saldo(02) em estoque deste produto,  porém no momento de gerar a **Pré-Requisição** não iremos considerar o **Armazém da SA** e com isso é ativado os parâmetros  **Saldo do Armazém**e **Saldo Ate o Armazém**, conforme exemplo abaixo:

Saldo F4:

![](https://tdn.totvs.com/download/attachments/991870790/image-2025-9-29_13-11-0.png?version=1&modificationDate=1759162261017&api=v2)

Realizaremos a solicitação ao armazém **02**: pela rotina MATA105

![](https://tdn.totvs.com/download/attachments/991870790/image-2025-9-29_13-15-33.png?version=1&modificationDate=1759162534003&api=v2)

No momento de gerar a pré-requisição configuramos os parâmetros conforme abaixo: MATA106

**Gera Sol.Compras/Aut.Entrega = Sim**, **Cons. o Armazémda SA = Não**, **Saldo do Armazém= 01**e **Saldo Ate o Armazém 02**

![](https://tdn.totvs.com/download/attachments/991870790/image-2025-9-29_13-18-2.png?version=1&modificationDate=1759162683790&api=v2)

Conforme mencionado anteriormente, ele vai considerar o *range* de armazéns informados nos parâmetros **Saldo do Armazém**e **Saldo Ate o Armazém**.

Ele vai verificar se neste *range* de armazém que informamos tem estoque desse produto e caso tenha saldo para atender a necessidade solicitada não será gerado a solicitação de compras, pois existe o produto em estoque para atender a ela mesmo que em outro armazém.

Como usamos o armazém **02**e não temos estoque deste produto nele, mas existe saldo no armazém **01**, não será gerado a solicitação de compras, pois existe saldo para atender a solicitação.

Mas enquanto não for efetuada a transferência dos saldos do armazém **01**para o armazém **02** pela rotina [**Transferência Múltipla (MATA261)**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011935502-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA261-Transfer%C3%AAncia-M%C3%BAltipla-de-Produtos) não será possível realizar a baixa da requisição na rotina MATA185

Apresentando a mensagem: *Help*: **MA240NEGAT** - Não existe quantidade suficiente em estoque para atender esta requisição.

![](https://tdn.totvs.com/download/attachments/991870790/image-2025-9-29_14-18-48.png?version=1&modificationDate=1759166329853&api=v2)

Para maiores detalhes:

[**Solicitação ao Armazém - Como sistema se comporta com o parâmetro MV\_ESTNEG igual a N**](https://tdn.totvs.com/x/Rr8eOw)

**Saiba mais:**

# [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Solicitação, Pré](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018562511-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Solicita%C3%A7%C3%A3o-Pr%C3%A9-Requisi%C3%A7%C3%A3o-e-Baixa-da-Pr%C3%A9-Requisi%C3%A7%C3%A3o-MATA105-MATA106-MATA185) [Requisição e Baixa da Pré-Requisição - MATA105 - MATA106 - MATA185](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018562511-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Solicita%C3%A7%C3%A3o-Pr%C3%A9-Requisi%C3%A7%C3%A3o-e-Baixa-da-Pr%C3%A9-Requisi%C3%A7%C3%A3o-MATA105-MATA106-MATA185) [*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
