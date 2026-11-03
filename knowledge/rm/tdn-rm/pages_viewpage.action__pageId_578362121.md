---
content_hash: bd32cfc8ea6b064892663eaebfbaa4f01a34d86a1a57fad38932baf357d6177f
fetched_at: '2026-06-29T00:10:53.292750+00:00'
page_id: '578362121'
product: rm
source: tdn-rm
title: Integração Matrix
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=578362121
version: 12
---

Esta funcionalidade tem por objetivo realizar importação de resultados Matrix 

1. **Visão Geral**
2. **Resultados Laboratoriais**
3. **Importação de Exames Matrix**
4. **Exportação de Resultados Laboratoriais**

SumárioVisão Geral

## **01. VISÃO GERAL**

Caminho da parametrização a partir da versão 2406: **Ambiente Parâmetros > Gestão Hospitalar > Unidade Diagnósticos > Integrações > Laboratoriais > MATRIX**

> ##### **IMPORTANTE:**
>
> ##### Após a versão 2310, com a implementação do método da Lib 'WriteAllBytes' da RMSFile, o caminho configurado no Delphi não deve ser mais o absoluto, e sim apenas a subpasta da integração. Ou seja:
>
> ##### Se era C:\totvs\matrix\resultados, mudar para **matrix\resultados**.
>
> ##### Ao realizar a integração, os resultados irão aparecer na pasta "Arquivos" da pasta "Bin" da respectiva versão. Ex.:
>
> ##### **C:\RM\Atual\Release\Bin\Arquivos\matrix\resultados**
>
> ##### 
>
> ##### Para ambientes Cloud Totvs também torna-se necessário que a pasta e subpasta informada no parâmetro "Caminho para o Matrix" seja criada no CLOUD, entrando em contato com o responsável pelo ambiente e pedir para que seja criada uma pasta dentro do CLOUD na estrutura explicada acima(ex: \Matrix\Integracao), importante salientar que essa pasta deve ser um acessada de forma EXTERNA(FTP Publico). Desta forma para  a Máquina Matrix ou alguma forma automatizada deve colocar os arquivos ".
>
> ##### Em caso de integração matrix para que a assinatura seja exibida corretamente no relatório é necessário que um dos casos a baixos sejam respeitados:
>
> Caminho da parametrização a partir da versão 2406: Ambiente Parâmetros > Gestão Hospitalar > Unidade Diagnósticos > Integrações > Laboratoriais > MATRIX
>
> 1. Sem liberação automática(parâmetro> "Ao Importar Resultado, Exame Já é Considerado como Liberado", Desmarcado)  
>    Quando esse parâmetro está desmarcado, o exame ficará com o status de "Digitação Concluída". Ao executar a ação de liberar o exame, será exibida uma tela para a seleção do responsável técnico pela liberação. No relatório, será exibida a assinatura do responsável técnico selecionado anteriormente.
> 2. Com liberação automática( Parâmetro> "Ao Importar Resultado, Exame Já é Considerado como Liberado", Marcado)  
>    Quando esse parâmetro está marcado, o usuário que executa a exportação da amostra deve ser um responsável técnico. Nesse momento o campo CODMEDRESPLAUDO é preenchido, e o relatório será gerado com a assinatura do técnico que exportou o exame.

Resultados Laboratoriais

## **02. RESULTADOS LABORATORIAIS**

Unidade de Diagnóstico > Resultados Laboratoriais 

Clique no botão "Troca informações com o Matrix" e selecione o submenu "Importar Resultados".

## **02.a TELA RESULTADOS LABORATORIAIS**

Cadastros > Unidade de Diagnóstico > Resultados Laboratoriais

Selecione o exame ao qual já realizou o cadastro de local execução externa.

E clique no ícone  e selecione a opção de exportação desejada.

* + Exportar Todos os Pedidos
  + Exportar Pedidos selecionados
  + Exportar Amostras Selecionadas
  + Exportar todos os Itens Selecionados

Na opção Exportar todos os pedidos não é necessário selecionar todos os pedidos com status Inicial.

Na opção Exportar  Amostras selecionadas devem ser exportadas somente as amostras com checkbox marcado e com status Inicial.

Se estiver habilitado o parâmetro Utiliza triagem de Amostras no DELPHI só será permitido exportar as amostras que já passaram pela triagem, caso contrário exibir a mensagem “Amostras do exame não passaram pelo processo de triagem”.

Na opção Exportar Pedidos Selecionados, devemos exportar para o Matrix somente os pedidos com checkbox marcado e com status Inicial.

Na opção Exportar todos os itens selecionados, devemos exportar os exames selecionados e com status Inicial.  
 

## **FUNCIONALIDADE DO MATRIX COMO LOCAL DE EXECUÇÃO EXTERNA EM PEDIDO DE EXAME**

Nessa tela, sempre que um local externo é selecionado, o campo de método é bloqueado. Para aparecer os parâmetros nos resultados, é necessário que esteja preenchido o campo de método na tela de pedido de exame.

Para solução do problema, o usuário **não** deve selecionar ‘Matrix’ como local de execução externa.

Na tela de pedido de exame, quando o usuário selecionar essa integração na unidade de atendimento do pedido e não preencher o campo de Local de Execução Externa, o sistema automaticamente detectará que aquele exame é realizado via Matrix, e seus processos da integração poderão ser executados normalmente (exportação de amostra, importação de resultado, etc e etc).

Novamente, apesar do exame estar sem o local ‘Matrix’ selecionado, ele conseguirá executar todos os processos da integração. Além disso, com o método preenchido, ele conseguirá visualizar os campos de parâmetros do exame na tela de resultados laboratoriais:

Importação de Exames Matrix

## **03. TELA IMPORTAÇÃO EXAMES MATRIX**

Automaticamente o sistema já submete os arquivos para inclusão de resultados dos exames.

Exportação Resultados laboratoriais

## **04. EXPORTAÇÃO RESULTADOS LABORATORIAIS**

Cadastros > Unidade de Diagnóstico > Locais de Execução Externa 

Na tela de  Locais de Execução Externa deve-se criar um novo local com a nomenclatura "MATRIX"

Cadastros > Unidade de Diagnóstico > Exames e Serviços

Na tela de exames e serviços, dê um duplo click no exame que deseja fazer a exportação matrix.

Na tela de exames e serviços, clique em incluir e selecione a aba execução externa, no campo "Local Execução Externa", selecione "MATRIX" e salve a alteração.

Na tela de Cadastros > Unidade de Atendimento > Selecione a unidade atendimento do exame > Aba Integrações .

Selecione Laboratório "Matrix".
