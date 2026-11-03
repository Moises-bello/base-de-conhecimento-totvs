---
content_hash: db191001671d257d691457a7fb54570eec08282a1c02fd3d29b82c00b1305b9f
fetched_at: '2026-07-02T19:24:26.018141+00:00'
page_id: '519714918'
product: protheus
source: tdn-tec
title: 10.5. Assistente de Dicionário de Dados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=519714918
version: 2
---

Ao editar programas fontes AdvPL, você pode utilizar o "Assistente de Dicionário de Dados", acionando `ctrl + alt + espaço`. Com isso você ativa um assistente semelhante ao assistente de código, porém com propostas para selecionar tabelas e/ou campos, a partir do dicionário de dados do Protheus.

1. Posicione o cursor do texto onde deseja iniciar a inserção de alias e/ou campos;
2. Acione `ctrl + alt + espaço`, obtendo algo semelhante a:  
     
   **Nota:** Antes de acionar o "Assistente de Dicionário de Dados", você deve selecionar qual a empresa/filial que irá utilizar.().
3. Há dois blocos de informação. Do lado esquerdo, são as tabelas existentes no dicionário de dados.  
   1. Seleção (único click): ao efetuar a seleção de uma tabela, seus campos (atributos) serão carregados no painel a direita.
   2. Duplo-click: ao efetuar um duplo-click, o alias da tabela será inserido na posição do cursor (em destaque), cabendo a você a finalização do comando.
4. Do lado direito, temos a lista de campos (atributos) da tabela selecionada.  
   1. Seleção (único-click): sem função específica, exceto se efetuado sobre a caixa de marcação (1a). Você pode selecionar quantos campos desejar.  
        
      Quando há campos marcados, a operação selecionada (botões logo abaixo dos painéis) será aplicada a estes.  
        
      O botão "`para atribuição`", irá gerar o código para atribuição de valores aos campos, sendo de sua responsabilidade a finalização do código.  
        
      O botão "`em lista`", irá gerar um código com os campos selecionados, usando o separador indicado (destaque verde). Para uso em *arrays* ou parâmetros, por exemplo.
   2. Duplo-click: ao efetuar um duplo-click, o alias e o atributo serão inseridos na posição do cursor (em destaque), cabendo a você a finalização do comando.
5. Se no editor for detectado ou selecionado uma palavra, será apresentado o *popup* já filtrado.
6. O *popup* apresentado, pode ser encerrado a qualquer momento acionando `ESC`, sem interagir com o código fonte.
