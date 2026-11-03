---
content_hash: 5ded9963607323622de6593b3df2ccc0ded7d6a59c44f1810f2c14c1594176f6
fetched_at: '2026-06-29T00:11:50.408293+00:00'
page_id: '840773775'
product: rm
source: tdn-rm
title: Gestão de Caixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=840773775
version: 77
---

**Uma das principais responsabilidades da tesouraria é a gestão das contas bancárias e aplicações financeiras. É necessário garantir que a empresa tenha fundos suficientes para cumprir suas obrigações financeiras, otimizar a liquidez e controlar sua operação de forma eficaz.**

**A ferramenta de gestão de caixa oferece recursos integrados nativamente para apoiar nestas tarefas, facilitando a comunicação entre as áreas, oferecendo informações relevantes e facilitadores para o equilíbrio do caixa.**

Essa jornada começa com o processo de [conciliação](https://tdn.totvs.com/pages/viewpage.action?pageId=421388741), que faz a conferência de toda a movimentação bancária, confrontando o extrato fornecido pelos bancos com a movimentação financeira registrada no sistema . Além da movimentação bancária, este processo também traz o saldo bancário atualizado para a Conta/Caixa (veja mais informações na página ).

Dessa forma, na tela principal da gestão de caixa são exibidos os saldos das contas correntes, caixa e aplicações financeiras, os pagamentos planejados para o período selecionado, e o saldo projetado considerando os pagamentos previstos. Dessa forma é possível verificar se as contas correntes terão fundos suficientes para realizar os pagamentos. Se necessário, nesta mesma tela é possível simular as movimentações bancárias para cobrir saldos negativos ou garantir o saldo mínimo das contas, de acordo com as regras de cada empresa. Após a simulação das movimentações, estas podem ser efetivadas e automaticamente os extratos de caixa correspondentes serão gerados. Além disso, após a efetivação das movimentações e pagamentos, é possível verificar o saldo das contas correntes que ficará parado e avaliar o direcionamento para as aplicações financeiras.

# 🔎 Navegue por assunto



**IMPORTANTE:**

**Funcionalidade está disponível a partir da versão 12.1.2406.109, via portal e MDI.**

**Mais informações e orientações para acesso na documentação abaixo.**

# ▶️ Vídeo de Apresentação

500350

# ▶️ Webinar

500350

visao-geral

## **01. VISÃO GERAL**

Este recurso tem como objetivo dar visibilidade ao gestor financeiro sobre os principais indicadores financeiros, principalmente os valores pendentes a pagar e os saldos das contas.

requisito-instalacao

## **02. PRÉ-REQUISITOS E INSTALAÇÃO**

       Acesse o [portal de downloads](https://suporte.totvs.com/portal/p/10098/download#company/) e realize o download do arquivo pertinente ao TOTVS RM Portal de acordo com a versão desejada na extensão .msi.  
  
       

         Ao realizar a [instalação do RM Portal](https://tdn.totvs.com/pages/viewpage.action?pageId=256317653) é possível optar por uma instalação personalizada caso não deseje instalar todos os Portais disponíveis. No caso do Gestão de Caixa, é necessário realizar a instalação do Portal do Backoffice.  
  
         

configpi

## **03. CONFIGURAÇÃO PÓS-INSTALAÇÃO**

         Acesse o diretório "C:\TOTVS\CorporeRM\FrameHTML\Web\App\Bco\Portal-BackOffice\config" e edite o arquivo 'config.json'. Altere onde está "<http://localhost:8051>" para mesmo o endereço do RM Host. Após a configuração do arquivo o IIS deverá ser reiniciado.

Original:

{  
  "apiServer": "BHN050103490:8051/",  
  "basePath": "",  
  "defaultAlias": "CorporeRM",  
  "urlCorpore": "",  
  "imgBannersLogin": [  
    {  
      "name": "banner01.png"  
    }  
  ]  
}

Configurado:

{  
  "apiServer": "http://**SERVIDOR\_APP\_SERVER:APIPORT**/",  
  "basePath": "",  
  "defaultAlias": "CorporeRM",  
  "urlCorpore": "",  
  "imgBannersLogin": [  
    {  
      "name": "banner01.png"  
    }  
  ]  
}

Exemplo de link de acesso ao Portal do Backoffice baseando no modelo de configuração citado acima: <http://meuservidoriis>/FrameHTML/Web/App/Bco/Portal-BackOffice/#/login

acessoMDI

## **04. ACESSO PELA MDI**

        Na MDI, acesse a aba Gestão Financeira e clique no botão Gestão de Caixa dentro do agrupador Gestão de Caixa.

permissao

## **05. PERMISSÃO**

        Na MDI, acesse o [cadastro de perfis](https://tdn.totvs.com/display/LRM/Perfil) e selecione o sistema 'Gestão Financeira'. Edite o cadastro do perfil associado ao usuário que deseja liberar o acesso ao Gestão de Caixa e clique na aba 'Acesso a Menus'. Por fim, permita o acesso a etapa 05.02.06, conforme demonstrado na imagem abaixo:

         

      Ainda no cadastro de perfis, porém selecionando o sistema 'Serviços globais', edite o cadastro do perfil associado ao usuário e permita acesso a etapa '01.01.01 - Coligadas'. **Obs**: Não é necessário liberar acesso para inclusão/edição da coligada, mas somente de visualização. Exemplo:

filtros

## **06. FILTROS**

Após realizar o login no Portal do Backoffice (com o mesmo usuário e senha utilizada na mdi) ou acessar o Gestão de Caixa através da mdi, utilize a opção 'Filtrar' para iniciar a utilização do Gestão de Caixa. Os filtros serão utilizados para cálculo dos indicadores, sendo necessário o operador financeiro informar as Coligadas, Filiais e o período desejado.

  

### FILTRO AVANÇADO (Somente à partir da versão 12.1.2506.121)

Além dos filtros obrigatórios citados acima, o operador financeiro também poderá filtrar os dados através da Conta/Caixa e/ou dos pagamentos previstos. O componente de filtro avançado será posicionado logo abaixo dos filtros obrigatórios (Coligada, Filial e Período) dentro da tela de filtro do Gestão de Caixa.

Funcionamento:

* O operador financeiro seleciona as Coligadas, Filiais e Período (obrigatórios)
* Em seguida, clica no (s) link (s) **"Conta/Caixa"** e/ou **"Previsão de Pagamentos"** para abrir a tela de construção dos filtros avançados.

Filtro AvançadoFiltros Conta/Caixa

**Construção dos Filtros Avançados da Conta/Caixa**

* Criar ou editar filtros personalizados.
* Informar um nome para o filtro.
* Marcar a visibilidade como **Privado** ou **Público**. Se o operador financeiro definir o filtro como 'Privado', este filtro será exibido apenas para o seu usuário. Caso seja definido como 'Público', o filtro ficará visível para todos os usuários.
* Utilizar o construtor visual para montar regras/grupo de regras (Exemplo: **Codigo da Conta Caixa** Igual "0001" Ou **Tipo de Conta Caixa** Igual "Conta Corrente").

Após configurar o filtro avançado:

* O usuário deve clicar em **“Salvar e Filtrar”** ou apenas **“Filtrar”** (nessa opção o filtro não será gravado no banco de dados).
* O usuário **precisa** clicar no botão **“Aplicar Filtros”** na tela principal dos filtros para efetivar o filtro avançado da Conta/Caixa. Neste caso, serão exibidos os Saldos das Contas conforme a especificação nos filtros.

Filtros Previsão de Pagamentos

**Construção dos Filtros Avançados de Previsão de Pagamentos**

* Criar ou editar filtros personalizados.
* Informar um nome para o filtro.
* Marcar a visibilidade como **Privado** ou **Público**. Se o operador financeiro definir o filtro como 'Privado', este filtro será exibido apenas para o seu usuário. Caso seja definido como 'Público', o filtro ficará visível para todos os usuários.
* Utilizar o construtor visual para montar regras/grupo de regras (Exemplo: **Status do Lançamento** Igual "Em Aberto" Ou **Status da Remessa** = "Remetido").

Após configurar o filtro avançado:

* O usuário deve clicar em **“Salvar e Filtrar”** ou apenas **“Filtrar”** (nessa opção o filtro não será gravado no banco de dados).
* O usuário **precisa** clicar no botão **“Aplicar Filtros”** na tela principal dos filtros para efetivar o filtro avançado de Previsão de Pagamentos. Neste caso, serão exibidos os Saldos das Contas conforme a especificação nos filtros.

indicadores

## **07. INDICADORES**

**Saldo Total:**

* **Conta corrente**: Valor total das movimentações, independente do período definido no filtro, dos títulos cujo o tipo da [conta/caixa](https://tdn.totvs.com/pages/viewpage.action?pageId=421388837) associada seja 'Conta corrente'.
* **Aplicações**: Valor total das movimentações, independente do período definido no filtro, das aplicações financeiras que possuem a [conta/caixa](https://tdn.totvs.com/pages/viewpage.action?pageId=421388837) associada cujo o tipo seja 'Aplicação Financeira'.

**A Pagar:**

* **No período**: Valor acumulado dos títulos a pagar que estão em atraso, vencendo na data corrente e a vencer dentro do período selecionado do filtro.
* **Em atraso**: Títulos a pagar com a data de vencimento menor que a data corrente.
* **Hoje**: Títulos a pagar com a data de vencimento na data corrente.
* **A vencer (Próx. 15 dias)**: Títulos a pagar com a data de vencimento maior que corrente e menor ou igual que a data de corrente, acrescido de 15 dias.
* **Total acumulado**: Soma dos 3 componentes citados acima (valores em atraso, hoje e a vencer).

Observação: É considerado o valor líquido dos títulos a pagar e a data de vencimento dos mesmos, independente do filtro selecionado.

**A Receber:**

* **No período**: Valor acumulado dos títulos a receber que estão em atraso, vencendo na data corrente e a vencer dentro do período selecionado do filtro.
* **Em atraso (Até 30 dias)**: Títulos a receber com a data de vencimento menor que a data corrente, até 30 dias.
* **Hoje**: Títulos a receber com a data de vencimento na data corrente.
* **A vencer**: Títulos a receber com a data de vencimento maior que a data corrente até 15 dias.
* **Total acumulado**: Soma dos 3 componentes citados acima (valores em atraso, hoje e a vencer).

Observação: É considerado o valor original dos títulos a receber e a data de vencimento dos mesmos, independente do filtro selecionado.

saldo-contas

## **08. SALDO DAS CONTAS**

       O gestor/operador financeiro poderá acompanhar o saldo de suas contas correntes e aplicações financeiras, visualizando as informações do seu contas a pagar para estabelecer as ações necessárias no dia a dia para equilibrar o caixa. Na visão dos saldos das contas será possível visualizar os dados:

* **Coligada**: Representa a coligada da [conta/caixa](https://tdn.totvs.com/pages/viewpage.action?pageId=421388837).
* **Filial**: Representa a filial da [conta/caixa](https://tdn.totvs.com/pages/viewpage.action?pageId=421388837).
* **Código**: Representa o código da [conta/caixa](https://tdn.totvs.com/pages/viewpage.action?pageId=421388837).
* **Descrição da Conta/Caixa**: Representa a descrição da [conta/caixa](https://tdn.totvs.com/pages/viewpage.action?pageId=421388837).
* **Banco**: Representa o banco da [conta/caixa](https://tdn.totvs.com/pages/viewpage.action?pageId=421388837).
* **Agência**: Representa a agência do banco da [conta/caixa](https://tdn.totvs.com/pages/viewpage.action?pageId=421388837).
* **Número da conta**: Representa o número da conta do banco da [conta/caixa](https://tdn.totvs.com/pages/viewpage.action?pageId=421388837).
* **[Liquidez](https://tdn.totvs.com/display/public/LRM/Liquidez)**: Representa a liquidez da [conta/caixa](https://tdn.totvs.com/pages/viewpage.action?pageId=421388837).
* **Saldo Conta/Caixa**: Representa o saldo instantâneo da [conta/caixa](https://tdn.totvs.com/pages/viewpage.action?pageId=421388837).
* **Saldo Bancário**: Representa o saldo bancário da [conta/caixa](https://tdn.totvs.com/pages/viewpage.action?pageId=421388837) informado manualmente ou através de importação de arquivo OFX.
* **Valor a Pagar**: Representa o valor que a [conta/caixa](https://tdn.totvs.com/pages/viewpage.action?pageId=421388837) tem que pagar baseado no período escolhido no filtro.
* **Saldo Previsto**: Representa o valor do **Saldo Inicial** - **Valor a Pagar**
* **Valor das Movimentações**: Representa o somatório de todas as movimentações que possuem relação com a [conta/caixa](https://tdn.totvs.com/pages/viewpage.action?pageId=421388837).
* **Saldo Simulado**: Representa o valor do **Saldo Previsto** + **Valor das Movimentações**.

**Obs**:

* + É possível realizar o gerenciamento da ordem e a exibição das colunas citadas acima.
  + Até que o carregamento dos indicadores a pagar seja finalizado, a coluna "**Valor a Pagar**" ficará em carregamento.

incluir-movimentacoes

## **09. INCLUIR MOVIMENTAÇÕES**

        O gestor/operador financeiro, após visualizar as contas que necessitam manutenção no componente anterior (Saldo das Contas), poderá simular as movimentações entre as contas caixas classificadas como 'Conta Correntes' e 'Aplicação financeira' para que seja possível equilibrar os saldos de acordo com a necessidade. É possível selecionar uma conta com o saldo positivo para que seja sua conta de origem (conta de onde será retirado o dinheiro para realizar a transferência) e uma conta com o saldo negativo para que seja sua conta de destino (conta que receberá o dinheiro retirado da conta de origem). Por fim, o gestor/operador financeiro insere o valor que pretende transferir e confirma a simulação para conferir como ficarão os saldos de suas contas, facilitando em sua tomada de decisão.

**Obs**: As contas de origem disponíveis para seleção serão as mesmas contas caixas retornadas na lista de saldo das contas.

                                                                                                     

visao-movimentacoes

## **10. VISÃO DE MOVIMENTAÇÕES PENDENTES**

        O gestor/operador financeiro, após realizar movimentações entre as suas contas que necessitavam de manutenção no componente anterior (Incluir Movimentações), poderá acompanhar as movimentações entre as contas caixas que ainda estão com o status pendentes de aprovação. Na visão de movimentações pendentes será possível visualizar os dados:

* **Id:** Id da movimentação realizada.
* **Status:**Representa o status/situação da movimentação.
* **Coligada origem:** Representa a coligada da conta caixa de origem na movimentação.
* **Conta/Caixa origem:** Representa a conta caixa de origem na movimentação.
* **N. Conta origem:** Representa o número da conta bancária da conta caixa de origem na movimentação.
* **Banco origem:**  Representa o banco da conta caixa de origem na na movimentação.
* **Saldo origem:** Representa o saldo na conta caixa de origem antes de realizar a movimentação.
* **Movimentação:** Representa o valor da movimentação (valor que será retirado da conta de origem e enviado para a conta de destino).
* **Saldo final origem:** Representa o saldo na conta caixa de origem após realizar a movimentação.
* **Coligada destino:** Representa a coligada da conta caixa de destino na movimentação.
* **Conta caixa destino:** Representa a conta caixa de destino na movimentação.
* **N. Conta destino:** Representa o número da conta bancária da conta caixa de destino na movimentação.
* **Banco destino:** Representa o banco da conta caixa de destino na na movimentação.
* **Saldo destino:** Representa o saldo na conta caixa de destino antes de realizar a movimentação.
* **Saldo final destino:** Representa o saldo na conta caixa de destino após realizar a movimentação.

efetivar-movimentacoes

## **11. EFETIVAR MOVIMENTAÇÕES PENDENTES**

        O gestor/operador financeiro, após visualizar as movimentações pendentes no componente anterior (Visão de Movimentações pendentes), poderá efetivar as movimentações entre as contas caixas que estão aguardando efetivação. Com isso, será possível gerar os extratos correspondentes às entradas e saídas nas contas selecionadas. Essa ação garante que as contas estejam em conformidade com o saldo bancário da empresa, facilitando para o gestor/operador financeiro a tomada de decisões com mais previsibilidade e assertividade.

        Para efetivar a movimentação, é necessário:

* Em cada coligada proprietária das contas/caixa envolvidas na operação, é necessário acessar o menu 'Ambiente - Parâmetros  - TOTVS Gestão Financeira - Avançar - Controle Bancário - Avançar' e na etapa "Gestão de Caixa", definir a natureza orçamentária default para ser utilizada na geração do extrato de caixa relacionado a transferência. Mais informações a respeito deste campo, localize o tópico 'Gestão de Caixa' [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=421388840).
* No cadastro das contas/caixa envolvidas na operação, é necessário acessar os anexos, clicar em '[Defaults de Conta/Caixa](https://tdn.totvs.com/pages/viewpage.action?pageId=421388828)' e definir uma filial default para ser utilizada geração do extrato de caixa relacionado a transferência.

excluir-movimentacoes

## **12. EXCLUSÃO DE MOVIMENTAÇÕES PENDENTES**

        O gestor/operador financeiro, após realizar movimentações entre as suas contas que necessitavam de manutenção e visualizá-las no componente "Visão de movimentações pendentes", poderá realizar a exclusão das movimentações entre as contas caixas que estão pendentes e julgar desnecessárias, garantindo assim a atualização e controles das finanças.

historico-movimentacoes

## **13. VISÃO DE HISTÓRICO MOVIMENTAÇÕES**

        O gestor/operador financeiro, após realizar movimentações entre as suas contas que necessitavam de manutenção no componente anterior (Efetivar Movimentações Pendentes), poderá acompanhar as movimentações entre as contas caixas que estão com o status efetivada ou que foram estornadas/canceladas. Na visão de Histórico Movimentações será possível visualizar os dados:

* **Id:** Id da movimentação realizada.
* **Status:**Representa o status/situação da movimentação.
* **Coligada origem:** Representa a coligada da conta caixa de origem na movimentação.
* **Conta/Caixa origem:** Representa a conta caixa de origem na movimentação.
* **N. Conta origem:** Representa o número da conta bancária da conta caixa de origem na movimentação.
* **Banco origem:**  Representa o banco da conta caixa de origem na na movimentação.
* **Saldo origem:** Representa o saldo na conta caixa de origem antes de realizar a movimentação.
* **Movimentação:** Representa o valor da movimentação (valor que será retirado da conta de origem e enviado para a conta de destino).
* **Saldo final origem:** Representa o saldo na conta caixa de origem após realizar a movimentação.
* **Coligada destino:** Representa a coligada da conta caixa de destino na movimentação.
* **Conta caixa destino:** Representa a conta caixa de destino na movimentação.
* **N. Conta destino:** Representa o número da conta bancária da conta caixa de destino na movimentação.
* **Banco destino:** Representa o banco da conta caixa de destino na na movimentação.
* **Saldo destino:** Representa o saldo na conta caixa de destino antes de realizar a movimentação.
* **Saldo final destino:** Representa o saldo na conta caixa de destino após realizar a movimentação.

estornar-movimentacoes

## **14. ESTORNAR MOVIMENTAÇÕES EFETIVADAS**

        O gestor/operador financeiro, após visualizar as movimentações efetivadas no componente anterior (Visão de Histórico Movimentações), poderá estornar/cancelar as movimentações entre as contas caixas que já foram efetivadas. Com isso, será possível cancelar os extratos correspondentes às entradas e saídas nas contas selecionadas. Essa ação garante que as contas estejam em conformidade com o saldo bancário da empresa, facilitando para o gestor/operador financeiro a tomada de decisões com mais previsibilidade e assertividade.
