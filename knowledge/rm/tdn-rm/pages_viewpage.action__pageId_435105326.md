---
content_hash: cf7286cf340e7aa86fb1ea6a9b4d4b25e0d514852221ecc98f91fc91c0cdc945
fetched_at: '2026-06-29T00:09:49.581561+00:00'
page_id: '435105326'
product: rm
source: tdn-rm
title: Medidor - Processo - Gerar medições
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105326
version: 4
---

Esse processo tem como objetivo facilitar a inserção de medições para um ou mais medidores.  
Lembrando que a medição também pode ser inserida através do .  
    
**Pré-requisitos**

* Pelo menos um medidor cadastrado
* Permissão para acessar o processo

**Como executar**

* Acesse a visão de medidores através do caminho: TOTVS Incorporação > Condomínio > Medidor
* Selecione um ou mais medidores, no qual se deseja inserir uma medição
* Em processos, selecione a opção **Lançamento de medições**

Será exibida uma tela, conforme o print abaixo  
    
  
**Figura 1 - Tela do processo de Lançamento de Medições**  
      
**Campos da tela de processo**  
    
**Informações Default** Esse campos servem como valores defaults. Podem ser aplicados a um ou mais medidores, desde que esteja selecionado, de uma só vez ao clicar no botão "Aplicar".  Os campos que compõe as informações default são:

* **Data de medição**
* **Competência**
* **Medição**

**Grid**

* **Nome do Empreendimento** Empreendimento ao qual o medidor se encontra associado. Caso o medidor não esteja associado, esse campo não irá exibir um valor
* **Identificador, Número do equipamento, Descrição do Medidor e Tipo de medidor** Informações para identificação do medidor ao qual a leitura será associada
* **Medição Anterior** Valor da última medição informada para o medidor. Será usado no cálculo do consumo
* **Data de medição** Deve ser preenchido com a data da medição que está sendo informada. Esta data deve estar dentro do período no qual o medidor ficou ligado
* **Competência** Deve ser preenchido com a informação do mês/ano de competência da medição. Esta informação indica em qual fechamento esta medição será apurada
* **Medição** Deve ser preenchido com o valor lido no instrumento. Esta informação será usada no cálculo do consumo
* **Consumo** Valor calculado pela diferença da **medição** e da **medição anterior**
* **Constante** Valor da constante informada no cadastro do medidor. Este valor será usado para multiplicar o **consumo**
* **Consumo x Constante** Valor do consumo multiplicado pela constante do medidor. Caso o valor da constante seja 0, ela é ignorada e o valor do **consumo x constante** será o mesmo do **consumo**

**Observações**

* O sistema permite somente uma medição para cada competência. Dessa forma, caso no processo tenha uma tentativa de inserir uma medição em uma competência que já a possui, o sistema irá impedir a operação e alertando no log do processo, que o medidor já possui medição para a competência relatada
* Caso o medidor já possua uma medição cadastrada, o processo irá preencher automaticamente a competência posterior a que já está cadastrada, dessa forma facilitando a inserção de medições. O medidor não possuindo medição, a competência virá vazia na grid
* O sistema não permite que a Medição Atual seja igual ou menor que a Medição Anterior. Dessa forma, caso seja inserido um valor na Medição nas condições citadas anteriormente, o sistema irá exibir uma mensagem de erro e impedindo a execução do processo. Será somente permitido a execução do processo quando todos os medidores tiverem a sua medição válida
