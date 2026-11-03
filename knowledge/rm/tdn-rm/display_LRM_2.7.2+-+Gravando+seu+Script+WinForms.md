---
content_hash: 7dedc906763856a2ac17025b99e23bed7bbf439174b3f93cafd08e7e87c15521
fetched_at: '2026-06-29T00:11:21.152942+00:00'
page_id: '687766511'
product: rm
source: tdn-rm
title: 2.7.2 - Gravando seu Script WinForms
type: documentation
url: https://tdn.totvs.com/display/LRM/2.7.2+-+Gravando+seu+Script+WinForms
version: 7
---

Para gravar seu script faça o seguinte:

* Carrege o TestFlow 3.0
* Acesse o menu Atividades | Windows | Script WinForms
* Adicione um novo registro e preencha a [Header](https://tdn.totvs.com.br/display/EN/TestFlow+3.0 #header) com as informações necessárias para a correta identificação da mesma e em seguida salve.
* Já dentro do cadastro da gravação informe:
  + Versão na qual está sendo gravado. Posteriomente você poderá duplicar esta gravação para uma outra versão se necessário for.
  + Descrição completa que diga qual a função da gração para que uma futura manutenção seja facilitada.
  + Com o RM já aberto e logado selecionte o [Servidor](https://tdn.totvs.com.br/display/EN/5+-+Servidores) no qual o Host e o RM estão em execução.
  + Após a seleção do servidor os componentes do form do RM que estiver aberto serão apresentados em uma árvore..
    - Após o clique em um dos forms listados será possível visualizar todos os seus componentes .
    - Clique no componente  desejado e escolho no pop-up que será aberto uma das ações disponíveis para o componente (Click, Duplo Click ou Setar Texto)
      * Click → Faz apenas um clique no componente
      * Duplo Click → Faz dois cliques no componente
      * Setar Texto → Preenche o campo com o texto informado no modal
    - Após selecionar a ação será incluído uma ação na timeline na direita com os parâmetros.
  + Aba entre ações
    - Na timeline de ações é possível:
      * Alterar a ordem que as ações são executadas
      * Adicionar ações de timer (delay antes de executar a próxima ação)
      * Alterar o tempo entre ações (entre cada ação no script será adicionado um delay com o tempo informado)
      * Ações
        + É possível selecionar as ações que irão ser testadas na execução, caso não esteja selecionado não será executado
        + É possível verificar o json de configuração da ação do componente criado ao clicar em uma ação
        + É possível excluir a ação e todas as selecionadas
        + É possível executar as ações selecionadas e cancelar também a execução
        + Em alguns tipos de ação é possível informar um código C# para execução antes ou depois da ação. As ações nas quais é possível inserir um C# são identificadas com o ícone "**<>**". Clique no ícone, escolhe quando o código será executado e insira seu cógido.
  + Aba Aguardar Janelas
    - É possível selecionar o tempo em que o script aguardará após abrir uma janela para executar a próxima ação
  + Aba Memória e CPU
    - É possível alterar o tempo entre ações baseado no desempenho durante a execução do script winforms no computador
