---
content_hash: 872ade27a8d4b0b5fc0cea2cbbc97d5dd373f0c3f3793f93a2134e06d85fa1fa
fetched_at: '2026-06-29T00:11:02.433742+00:00'
page_id: '618476630'
product: rm
source: tdn-rm
title: Resultado de Exames
type: documentation
url: https://tdn.totvs.com/display/LRM/Resultado+de+Exames
version: 25
---

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Pré-visualização dos laudos**
4. **Imprimir resultado**
5. **Laudo evolutivo**
6. **Gráfico evolutivo**
7. **Configuração do IIS**

falsepaineltrueVisão Geral

## **01. VISÃO GERAL**

Esta tela tem como objetivo visualizar todos os status e resultados dos exames que foram realizados pela unidade diagnóstica da própria instituição. Desta forma a lista de exames visualizada aqui não será necessariamente a mesma contida na tela de .

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

Ao acessar a tela de resultado de exames é possível ver a lista do dos exames de forma gradativa de 7 em 7 conforme a imagem abaixo:

A tabela de resultados contém as seguintes colunas:

* Solicitação: nesta coluna deverá estar descrito se naquela solicitação existem exames de imagem e laboratório ou apenas um deles;
* Nome do solicitante: quem realizou a solicitação do exame;
* Data da solicitação;
* Status: que poderá ser pendente, reconvocação ou liberado. O valor será liberado apenas quando todos os exames da solicitação estiver com status liberado ou liberado para recepção (O).
* Laudo evolutivo: deverá exibir um botão habilitado que permitirá a visualização do laudo evolutivo quando for exame de laboratório. Quando for exame de imagem o botão deve estar desabilitado.
* A **data da coleta** foi adicionado a tela a partir da **versão 12.1.2506**

Através do campo de busca é possível filtrar as solicitações por exames. Ex.: Caso o usuário digite a palavra "hemograma", deverão ser listadas apenas as solicitações que possuírem a palavra hemograma em sua lista de exames.

Através do campo de data é possível filtrar por data da solicitação, onde, caso o usuário preencha, deverá trazer apenas as solicitações geradas naquela data.

Além disso deverá ser possível ordenar as solicitações por Nome do Solicitante e Data da solicitação.

Crescente:

Decrescente:

Ao expandir uma linha da tabela deverá exibir a lista de exames que fazem parte daquela solicitação contendo as seguintes colunas:

* Nome do serviço;
* Tipo de exame: podendo ser exame de imagem ou laboratorial;
* Status: que poderá ser pendente ou liberado.
* Visualizar: deverá exibir um botão habilitado que permitirá a visualização do laudo quando liberado. Quando pendente o botão deve estar desabilitado.
* Gráfico evolutivo: deverá exibir um botão que permita a visualização do gráfico evolutivo.

Além da tabela com os exames é possível realizar a impressão do resultado.

Pré-visualização dos laudos

## **03. PRÉ-VISUALIZAÇÃO DOS LAUDOS**

Na tela de resultados de exames, ao abrir uma solicitação, será possível pré-visualizar o laudo de um exame já liberado. 

Ao clicar no ícone, deverá ser possível pré-visualizar o resultado exame, seja de imagem (será exibido as imagens do exame) ou laboratório.

Imprimir resultado

## **04. IMPRIMIR RESULTADO**

Na tela de resultados de exames, ao escolher uma solicitação ou exames, e em seguida, clicar em imprimir solicitações um arquivo PDF é aberto em uma nova aba com todos os exames escolhidos. 

Ao selecionar um exame ou solicitação com status liberado o botão "Imprimir Resultado" fica habilitado.

* Somente exames ou solicitações com status liberados serão permitidos a impressão;
* No caso de exames de imagem, será impresso o laudo;
* No caso de exames onde o resultado esta disponível atravez de link, o mesmo não será impresso, deverá ser utilizado o botão "Visualizar" para abri-lo.

Laudo evolutivo

## **05. LAUDO EVOLUTIVO**

Na tela de resultados de exames, ao escolher uma solicitação de exames, e em seguida, clicar em laudo evolutivo. 

Será aberto um modal e exibido uma tabela de todos os exames respectivos a aquela ordem de serviço. Ao expandir o exame é mostrado todos parâmetros seguidos dos resultados anteriores classificados por data.

Para cada parâmetro é possível visualizar os valores de referência em forma de texto, um por linha.

Também é possível realizar a paginação dos resultados anteriores, sendo que a ordenação utilizada é a decrescente.

Gráfico evolutivo

## **06. GRÁFICO EVOLUTIVO**

Na tela de resultados de exames, ao escolher uma solicitação de exames, expandir e em seguida, clicar em gráfico evolutivo. 

Será aberto um modal e exibido um gráfico daquele exame com todos parâmetros seguidos dos resultados anteriores classificados por data.

Ao passar o mouse nos pontos é exibido seu respectivo valor.

Pode ser filtrado por 7, 15 e até 30 dias.

Será representado com a escala vertical de valores

e pela escala horizontal de datas.

Configuração do IIS

## **07. Configuração do IIS**

Para que a extensão **ngx-extended-pdf-viewer** funcione corretamente em aplicações hospedadas no IIS (Internet Information Services), é necessário adicionar um novo MIME type à configuração do servidor.

O visualizador depende de arquivos com a extensão **.mjs**, que por padrão não são reconhecidos pelo IIS. A ausência desse MIME type pode causar falhas no carregamento correto do PDF.

Passo necessário:

Adicione o seguinte MIME type nas configurações do IIS:

* **Extensão:** .mjs
* **Tipo MIME**: text/javascript

#### Como adicionar:

1. Abra o **Gerenciador do IIS**.
2. Selecione o site desejado no painel à esquerda.
3. No painel central, clique duas vezes em **Tipos MIME**.
4. No menu à direita, clique em **Adicionar...**.
5. Preencha os campos:

   * **Extensão do nome do arquivo:** .mjs
   * **Tipo MIME:** text/javascript
6. Clique em **OK** para salvar.

Após essa configuração, o **ngx-extended-pdf-viewer** será carregado corretamente e poderá exibir os arquivos PDF conforme esperado.
