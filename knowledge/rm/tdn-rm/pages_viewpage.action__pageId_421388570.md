---
content_hash: beec8c43febc7e3c2275bf1329b549909e6972c03b33eb326ae9f7141cb02d22
fetched_at: '2026-06-29T00:09:17.060534+00:00'
page_id: '421388570'
product: rm
source: tdn-rm
title: Negociação Online
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388570
version: 6
---

A Negociação Online foi desenvolvida com o objetivo de permitir a geração de Acordos Financeiros a partir da seleção de um ou mais lançamentos no Portal do Educacional.  
Processo que está disponível no Menu: Financeiro | Negociação.  
A partir do campo *Opções de Acordo* o usuário pode selecionar os Templates de Acordo já criados com o objetivo de realizar simulações de negociações com valores a pagar contendo o Meio de Pagamento e Parcelas. A partir desses dados, e de outros buscados do cadastro do Template e dos Lançamentos origem, as parcelas serão geradas e exibidas.  
São exibidos os Lançamentos cujo Cliente/Fornecedor esteja vinculado ao usuário do Educacional, podendo ser o próprio aluno ou responsável financeiro. A simulação poderá ser impressa, avançando as etapas do processo, o acordo será gerado a partir dos dados informados.

**Parametrização Essencial**

No Totvs Gestão Financeira Menu Contas a Pagar / Receber | Acordo | Template de Acordo selecionar e editar o Template desejado e habilitar opção: "Disponível para Web".

No cadastro do Perfil dentro do Serviços Globais vincular o Template através do Menu - Anexos:  Templates de Acordo Financeiro.

No cadastro do Template de Acordo no Menu - Anexos vincular a Matriz Aplicada. Ao acessar o Portal do Educacional selecionar a Matriz Aplicada no Contexto.

Além dos itens acima será considerado o Valor Líquido dos Lançamentos Financeiros a negociar validando com a Faixa de Valores parametrizada no Template.  
As regras de Negócio do Totvs Educacional também serão levadas em consideração para definir quais os lançamentos podem sofrer negociação.

**Simulação**

Realizada baseada nos valores do Template dos lançamentos origem e das informações inseridas pelo usuário no Portal (Número de Parcelas e Meio de Pagamento). O valor do Acordo será calculado pela simulação e exibido em tela.  
O Número de Parcelas apresentado será 0 permitindo ao usuário a digitação da quantidade desejada que será validada entre o mínimo e máximo parametrizado no Template de Acordo.  
A alteração do Número de Parcelas e/ ou Meio de Pagamento invalida uma simulação anteriormente feita (os dados simulados invalidados não são exibidos), nesse caso é necessário simular novamente a negociação.  
Os percentuais de juros, desconto e acréscimo buscarão o % máximo parametrizado no template.

**Impressão da Negociação**

Permite que a Simulação da Negociação Online seja impressa, necessário que o Template esteja parametrizado para realizar o processo. A partir da seleção do relatório do gerador serão impressos os dados, onde se inclui descrição do acordo e as parcelas a serem geradas.

**Impressão do Documento de Aceite**

Permite assegurar a aceitação quanto a Negociação realizada, necessário que o Template esteja parametrizado para realizar o processo. A partir do relatório do gerador será apresentado em tela um documento de Aceite da Negociação. Após visualização será obrigatório marcar a opção se está de acordo com o mesmo ou não.

**Confirmar Negociação**

Consiste em gerar as parcelas de Negociação para o Totvs Gestão Financeira baseado na simulação realizada. Ocorrendo erros ou validações quanto ao processo será apresentada em tela mensagens indicativas. Confirmando a geração da Negociação o Acordo será criado conforme dados indicados anteriormente.   
Para realizar a quitação das parcelas utilize o Menu: Gerenciar Acordo.   
Será possível vincular o template de Acordo á matriz aplicada (pode ser a todas disponíveis) do Totvs Educacional, restringindo o template por matriz aos lançamentos, independente do contexto selecionado no portal.

Ex:

Template cód.1 (Pagamento á vista)

Necessário vincular o template ao Perfil do Usuário logado no Totvs Gestão Financeira (Perfil - Mestre)

Necessário vincular o template ao Perfil do Usuário logado no Totvs Educacional (Perfil - Ensino Superior)

Necessário vincular no Template de Acordo no Menu - Anexos - Matriz Aplicada.   
  
**Obs**.: Necessário liberar acesso primeiro no Educacional para serem apresentadas.

Veja Também

* [Negociação Online - Educacional](https://tdn.totvs.com/pages/viewpage.action?pageId=494962674)
* [Boletim Técnico da Negociação Online](http://tdn.totvs.com/x/b-9bGQ)
