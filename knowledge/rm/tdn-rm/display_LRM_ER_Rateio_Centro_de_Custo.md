---
content_hash: 9581e03d3fb0737a6b5bc57060a2783fa5b75deee9e6d616b4e11fe66d85b2de
fetched_at: '2026-06-29T00:06:01.812510+00:00'
page_id: '198940537'
product: rm
source: tdn-rm
title: ER_Rateio_Centro_de_Custo
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Rateio_Centro_de_Custo
version: 3
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Pessoas | **Módulo** | RHU |
| **Segmento Executor** |  | | |
| **Projeto1** | RHU – DESENVOLVIMENTO RHU007 | **IRM1** | PCREQ-6303 |
| **Requisito1** | PCREQ-6307 | **Subtarefa1** | PDR\_RHU\_RHU007-31 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** |  | **Réplica** |  |
| **País** | (x) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Nas requisições de aumento de quadro, substituição, alteração de dados funcionais, transferência, transferência com alteração de dados funcionais e transferência em lote, o sistema possibilitará ao solicitante/aprovador propor rateio de centro de custos para o funcionário ou vaga relacionado à requisição.

Na efetivação das requisições supracitadas, exceto requisição de aumento de quadro e requisição de transferência em lote, o rateio de centro de custos do funcionário deverá ser aplicado ao cadastro do funcionário. Para a requisição de aumento de quadro, o rateio será aplicado ao funcionário que assumir a vaga criada.

Deverá haver um parâmetro no sistema para ativar/desativar esse recurso.

Os requisitos propostos neste documento se referem às requisições de aumento de quadro, substituição, alteração de dados funcionais, transferência com alteração de dados funcionais e transferência em lote. As demais requisições não terão nenhuma modificação.

 As interfaces web e winforms serão adaptadas para atender aos requisitos deste documento.

*<Nesta etapa informar o objetivo da especificação do requisito, ou seja, o que a funcionalidade deve fazer. Exemplo: Permitir que o usuário defina o percentual mínimo em espécie (dinheiro), a referência mínima para calculo dos débitos do aluno e o período de validade do parâmetro de negociação>.*

## Definição da Regra de Negócio

*MODELO DE SOLUÇÃO*

*,*

*REQUISITOS*

**Parametrização do recurso**

* Fluxograma do processo

Não se aplica.

* Descrição do processo

No parametrizador do sistema, deverá ser criado o parâmetro “Rateio de centro de custos do funcionário”. Esse parâmetro ativará ou desativará o recurso mencionado dentro das requisições definidas neste documento.

* Fluxo principal

1. O usuário acessa o Parametrizador (RH > Gestão de Pessoas > Configurações).
2. O sistema iniciará o processo de parametrização.
3. O usuário seleciona o item “Requisições” e avança o processo.
4. O sistema exibirá os parâmetros das requisições, entre eles o novo parâmetro criado.
5. O usuário ativa ou desativa os parâmetros, conforme sua necessidade.
6. O usuário conclui o processo.
7. O sistema grava as alterações efetuadas

* Regras de negócio

 

* + Comportamento na troca de parâmetro  
    Quando o parâmetro “Rateio de centro de custos do funcionário” for alterado, nenhuma alteração nos dados das requisições existentes será efetuada. Caso o parâmetro seja ativado, as requisições existentes e as novas habilitarão o recurso imediatamente. Caso o parâmetro seja desativado, o recurso será desabilitado. Os dados não serão excluídos, porém  as efetivações que forem efetuadas não considerarão as propostas de rateios e as aprovações também não exibirão as propostas feitas na abertura das requisições antigas.

**Propor rateio de centro de custos em requisições (winforms)**

* Descrição do processo   
  Nas requisições afetadas por esta especificação, será criada uma nova aba que permitirá ao solicitante/aprovador propor um rateio de centro de custos para o funcionário/vaga relacionado à requisição. Após criar uma requisição somente enquanto a mesma estiver com status “Pendente” será possível editar o rateio. Após a requisição estar “Em andamento”, a edição poderá ser feita através da inclusão de pareceres, e um *log* da alteração será gravado acrescido ao parecer.

* Fluxo principal

1. O usuário acessa o cadastro de requisições e cria ou altera uma requisição.
2. O sistema exibirá a tela de cadastro de requisições.
3. O usuário acessa a aba “Rateio de centros de custos”.
4. O sistema mostrará a visão onde o usuário poderá incluir o rateio.
5. O sistema carregará automaticamente o rateio atual do funcionário no momento em que o funcionário for informado na requisição. Indisponível nas requisições de aumento de quadro e transferência em lote.
6. O usuário informará ou alterará o rateio conforme sua necessidade. O rateio sempre deverá totalizar 100%.
7. O usuário salva a requisição.
8. O sistema valida e grava as informações no banco de dados.

****Propor rateio de centro de custos em requisições (webforms)****

* Descrição do processo  
    
  No portal do RH Online, nas requisições, a funcionalidade “Propor rateio” estará disponível nas mesmas requisições citadas anteriormente neste documento.

* Fluxo principal

1. O usuário acessa o Painel de Controle de Requisições.
2. O usuário escolhe qual requisição deseja abrir ou analisar.
3. Caso o usuário escolha analisar uma requisição, será aberta a tela para inclusão de parecer, onde será possível editar o rateio. Caso o usuário escolha abrir uma nova requisição, será exibida a tela para criar a nova requisição.
4. Para visualizar ou editar o rateio, o usuário clicará no botão “Rateio de C. Custos”.
5. O sistema carregará automaticamente o rateio atual do funcionário na primeira vez que a página de rateio for acionada. Indisponível nas requisições de aumento de quadro e transferência em lote.
6. O usuário informará ou alterará o rateio conforme sua necessidade.
7. Para incluir um rateio, o usuário deve clicar no *link* “Incluir novo rateio”.
8. Para editar um rateio, o usuário deve clicar na descrição do centro de custos a ser alterado, que estará num *link*.
9. Para excluir um rateio, o usuário deve clicar no *link* “Excluir”, na linha correspondente ao item que será removido.
10. O rateio sempre deverá totalizar 100%.
11. O usuário pode fechar esta página utilizando o botão “Fechar”.
12. Ao salvar a requisição ou avançar a etapa, o sistema valida e grava as informações no banco de dados.

**Efetivação de requisição**

* Descrição do processo

Caso o novo parâmetro de “Rateio de centro de custos do funcionário” esteja ativado no momento da efetivação e, tenha sido proposto um novo rateio, o processo de efetivação deverá atualizar o rateio do funcionário no seu cadastro.

## Protótipo de Tela

Parametrizador do sistema.

Visão da proposta de rateio

Tela de edição da proposta de rateio.

*Botão “Rateio de C. Custos”*

*Tela de edição da proposta de rateio - web.*

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
