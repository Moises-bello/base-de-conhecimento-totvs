---
content_hash: d9486e2d05eb266388b9335962b0227530a4217b6d9ede77b6e3438f5faa476d
fetched_at: '2026-06-29T00:09:37.142892+00:00'
page_id: '425459567'
product: rm
source: tdn-rm
title: Boletim Técnico - Negociação Online
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459567
version: 5
---

Os passos a seguir servirão de guia para a utilização da Negociação Online disponível no portal do Educacional, menu "Financeiro/Negociação". A partir da seleção dos lançamentos em abertos e de uma  Opção de Acordo, o usuário pode fazer uma simulação da negociação e visualizar as novas parcelas, seus valores e respectivos vencimentos.

Serão exibidos, para seleção, os Lançamentos cujo Cliente/Fornecedor esteja vinculado ao usuário no Educacional, podendo ser o próprio aluno ou o responsável financeiro. A simulação poderá ser impressa e, avançando as etapas do  processo, o acordo será gerado a partir dos dados informados.

Para utilização da  Negociação Online, a parametrização do Acordo no Educacional devem ser realizado (Processo 15.02 – Tesouraria | Geral 1/2).

**Atenção**

Existe tag de segurança para a Negociação Online. É preciso liberar a visualização no Perfil do usuário do Portal.

**Parametrização do Template de Acordo**

O Template de Acordo deve ser previamente cadastrado na Gestão Financeira. Somente templates com opção "Disponível para Web" marcado serão apresentados no Portal do Aluno para utilização na negociação.

Acesse: "Contas a Pagar/Receber | Acordo | Template de Acordo".   
 Ao cadastrar o Template, atenção para dois itens:

Informar no Anexo "Matriz Aplicada" do Cadastro do Templete de Acordo, as Matrizes para as quais o Template deve ser apresentado para utilização pelo Aluno.

O Perfil de Usuário vinculado ao Aluno também deve ser parametrizado para permitir a visualização do Template. Isso é realizado associando o Template de Acordo ao perfil, através do Anexo "Templates de Acordo Financeiro".  
    
   
    
**Portal**

No Portal, a Negociação Online está disponível no menu: "Financeiro | Negociação".

Seleção do Tipo de Acordo

Serão exibidos todos os Lançamentos cujo Cliente/Fornecedor está vinculado ao usuário no Educacional. Selecione os lançamentos para os quais se deseja realizada a negociação e clique no botão "Negociar".  
  

O sistema irá apresentar os Templates de Acordo, cadastrados na Gestão Financeira, que atendem ao contexto dos lançamentos que foram selecionados para a negociação, com base em seus valores.  
    
   
    
 Após selecionar uma opção de acordo, o sistema habilita a opção de simulação dos valores. Os campos "Parcelas" e "Meio de Pagamento" podem ou não ser editadas pelo Aluno. Esse comportamento é definido, também, no Cadastro do Template de Acordo.  
    
   
    
Simulação

Com base no Template selecionado, o sistema irá calcular e apresentar as futuras parcelas com seus valores e respectivos vencimentos e forma de pagamento.   
   
   
    
 A alteração do Número de parcelas e/ou Meio de Pagamento invalida a simulação feita; os dados simulados invalidados não serão mais exibidos, sendo necessário simular novamente a negociação.

Serão utilizados os percentuais máximos de juros, desconto e acréscimo parametrizados no Template para aplicação sobre o valor dos lançamentos que estão sendo negociados.

Confirmação

Existem três formas de confirmação da negociação:

* Ao criar,
* Ao aprovar
* Ao pagar a primeira parcela.

Nessa etapa serão geradas as parcelas da negociação no TOTVS Gestão Financeira, baseadas na simulação feita no Portal. Caso ocorra algum erro será apresentada mensagem indicativa e o problema descrito na tela. Ao confirmar a geração o Acordo será criado. Para realizar a quitação das parcelas consultar: (BOLETIM TECNICO : CONTROLE DE ALÇADA).  
  
  
  
 Visualização dos novos lançamentos no Portal e TOTVS Gestão Financeira:  
  
  
**Impressão da Negociação**

Esta opção estará disponível caso o Template esteja parametrizado para imprimir a simulação (campo "Impressão da Negociação do Acordo" preenchido). A partir da seleção do relatório do Gerador de Relatórios será impresso os dados da negociação, onde se incluem os dados do Acordo e as parcelas a serem geradas.  
  
  
  
**Impressão do Documento de aceite**

Caso o Template de acordo esteja parametrizado para obter aceite do Documento de Acordo, antes de finalizar a geração do processo, será necessário gerar o documento de Aceite da Negociação e marcar se está de acordo com o mesmo. Somente com a opção afirmativa do aceite será possível confirmar a negociação.  
  
  
  
  O sistema irá respeitar as informações do perfil e Template, após realizar  Logout – Login da aplicação. As alterações passarão a valer ao iniciar o sistema ou o Portal do Aluno.

Para cancelamento de um acordo gerado pelo Portal, é preciso cancelar primeiramente os Boletos gerados para depois cancelar o Acordo, através do TOTVS Gestão Financeira, pelo menu "*Contas a Pagar/Receber | Acordo | Gerenciar Acordo*".
