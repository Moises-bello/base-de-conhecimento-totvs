---
content_hash: 8381a12ea513434f73827a017dbf45001e092a305e0d4f22950280444b447780
fetched_at: '2026-06-29T00:09:19.594508+00:00'
page_id: '422545620'
product: rm
source: tdn-rm
title: Gerar SPED Fiscal
type: documentation
url: https://tdn.totvs.com/display/LRM/Gerar+SPED+Fiscal
version: 11
---

#f5f5f5#363636noneSPED Fiscal

## **Conteúdo**

2. 2.1.   
   2.2.

## **01. Gerar SPED FiscalGerarSPED**

Para gerar as informações para o SPED Fiscal, o usuário deverá acessar o menu Rotinas Legais | Rotinas Estaduais | SPED Fiscal. Na tela que será apresentada, o usuário deverá escolher a filial para a qual deseja gerar a rotina e, em seguida, clicar no botão configurar, localizado no lado superior direito da caixa de listagem das filiais.

Todos os campos da tela deverão ser preenchidos de acordo com o período e perfil de contribuinte no qual a empresa está enquadrada. Em seguida o botão OK deverá ser clicado. A filial parametrizada será transportada para a caixa de listagem à direita da tela. Este passo deverá ser repetido tantas vezes quantas forem as filiais a se parametrizar. O usuário poderá excluir uma ou mais filiais já parametrizadas. Para isso, basta selecioná-las clicando na caixa de seleção que está a frente do nome da filial e clicar no botão de exclusão.

Para alterar a parametrização, selecione as filiais e clique no botão de edição de registros. Terminadas as parametrizações das filiais, o usuário deverá clicar no botão executar para gerar as informações.  
  
***Dica*:** Para selecionar todas as filiais de uma só vez, segure a tecla "control" (Ctrl) do seu teclado e clique na caixa de seleção que está na frente do nome da coligada.

## **02. AtualizaçõesAtualizacoes**

Nesta seção, serão adicionadas informações referentes às atualizações feitas no sistema para a geração do SPED Fiscal.

### 02.1. 12.1.2912129

      A partir da versão 12.1.29 ,foi disponibilizada a opção de gravar as preferências do usuário.

     

      Por padrão, ao selecionar o processo, a flag "Gravar Preferências do Usuário" permanece marcada. Caso o usuário opte por não gravar suas preferências, a flag pode ser desmarcada. Essas preferências serão gravadas de acordo com o usuário que está gerando a rotina na coligada do contexto. O sistema irá gravar todos os parâmetros escolhidos pelo usuário no processo de geração do SPED Fiscal.

### 02.2. 12.1.22091212209

      A partir da versão 12.1.2209, haverá apenas uma opção para salvar o arquivo gerado pelo SPED, na aba "Personalização".

     

      Caso esta opção esteja marcada, ao fim da geração do arquivo do SPED, uma janela se abrirá, permitindo selecionar o local desejado para que o arquivo seja salvo.

      Caso esta opção esteja desmarcada, o arquivo gerado será salvo na pasta "Arquivos", que fica no diretório onde o RM.Host foi instalado. Se esta pasta não existir, ela será criada automaticamente.

      É possível configurar outra pasta padrão sem ser a "Arquivos" para que o arquivo do SPED seja salvo caso a opção esteja desmarcada. Para isso, basta adicionar a tag <add key="FileServerPath" value="Seu\_Diretorio\_Aqui"> no arquivo de configuração do RM.Host.  
      Para mais informações sobre a tag FileServerPath, acesse a [documentação Configuração das Tags FileServerPath e LogPath](https://tdn.totvs.com/display/LRM/Configuracao+das+Tags+FileServerPath+e+LogPath).

## **03. ObservaçõesObservacoes**

Para que as informações do inventário (Registro H) sejam geradas corretamente, antes da geração, usuário deverá disparar a rotina de geração de Saldos e Custos no TOTVS Gestão de Estoque, Compra e Faturamento caso o possua. Se não possuir ele deverá inserir estas informações no PVA após validar o arquivo gerado pelo TOTVS Gestão Fiscal.

***Observação***: Na geração do bloco H para quando o campo "Motivo do Inventário 2" estiver preenchido, serão gerados os registros H005, H010 e H020 com as alterações feitas em "Dados Fiscais por UF" (cadastro de produto) no mês anterior ao período de geração do SPED.

Para gerar informação referente ao ressarcimento/complemento ICMS ST basta marcar a opção "Gerar ressarcimento/complemento ICMS ST".

Caso o usuário queira executar outras tarefas enquanto gera o SPED Fiscal ele deverá, antes de executar o processo, clicar no botão opções e desmarcar o item Aguardar a Execução do Processo. Desta forma os outros menus ficarão livres para ser acessados. Mas só faça isto se for realmente necessário pois o processamento destas informações já é pesada e executar outras tarefas no TOTVS Gestão Fiscal ao mesmo tempo pode carregar ainda mais o processamento e comprometer a performance da rotina.

Para maiores informações a respeito do enquadramento do perfil do contribuinte, consulte o manual na página do [SPED Fiscal no Site da Receita Federal](http://sped.rfb.gov.br/arquivo/show/2322).
