---
content_hash: 4e9bfa2602cb783cc2553cf96bf4874e1c62ee767f11ed7b218642e2c490a138
fetched_at: '2026-06-29T00:11:36.931242+00:00'
page_id: '773521363'
product: rm
source: tdn-rm
title: Cadastro de Fórmulas para Central Laudos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=773521363
version: 11
---

## **Índice**

1. **Exemplo de utilização**

itensExemplo de utilização

## **01. EXEMPLO DE UTILIZAÇÃO**

**No RM saúde > Cadastro > Unidade de Diagnóstico > Cadastro de campos para fórmulas**

A partir da versão 2410, foi adicionada a funcionalidade de **variáveis**, que são campos preenchidos automaticamente pelo sistema durante o cálculo das fórmulas.

Atualmente, existem duas variáveis principais:

* **DATAATUAL**: insere automaticamente a data atual do computador no momento do cálculo da fórmula.
* **DUM** (Data da Última Menstruação): preenche automaticamente essa informação caso ela tenha sido registrada previamente na tela de laudagem.

Abaixo, há um exemplo (print) da tela de cadastro de fórmulas e da tela de laudagem para ilustrar o funcionamento.

> **Observação:** todos os exemplos utilizados são fictícios e servem apenas para demonstrar as funcionalidades do sistema.

💡 **Dica importante:** ao cadastrar fórmulas, é essencial utilizar **parênteses** corretamente para garantir a ordem adequada de execução dos cálculos.

   

### Funcionalidade dos campos:

* **Nome**: Abreviatura ou sigla do campo.
* **Descrição**: Nome completo ou explicativo do campo.
* **Tipo**: Define o comportamento do campo na tela de fórmulas. Os tipos disponíveis são:

  + **Número**: Cria um campo formatado que aceita apenas valores numéricos.
  + **Texto**: Cria um campo que pode ser preenchido com letras e/ou números. Este campo apenas substitui o valor original (não permite cálculos).
  + **Data**: Cria um campo de data. Pode ser substituído manualmente ou utilizado em cálculos:

    - Somar ou subtrair com um número ajusta a data em dias.
    - Subtrair uma data de outra retorna a quantidade de dias de diferença.
  + **Fórmula**: Permite a inclusão de outros campos ou valores para criar uma fórmula personalizada dentro do campo.
  + **Lista**: Cria um campo com opções pré-definidas para seleção. O valor escolhido substitui o conteúdo do campo.

**No RM saúde > Cadastro > Unidade de Diagnóstico > Cadastro de fórmulas para laudos**

### Funcionalidade dos campos do Cadastro de Fórmulas:

* **Mnemônico**: Abreviação do nome da fórmula.
* **Nome da Fórmula**: Descrição completa ou identificadora da fórmula.
* **Selecionar Campo**: Exibe os campos previamente cadastrados na opção **Cadastro de Campos para Fórmulas**.  
  É possível criar fórmulas utilizando campos numéricos, campos de data e até mesmo outras fórmulas já existentes.
* **Aba do Exame**: Permite associar exames à fórmula, desde que estejam com a opção **"Laudo pré-impresso"** marcada.

🧾 **Observação:**  
As fórmulas cadastradas serão exibidas automaticamente na **Central de Laudos**, sempre que forem incluídas em exames vinculados.

## **02.  Exemplos:**

## **Número**

Cadastramos dois campos como número 

E criamos uma fórmula para o mesmo 

Desta forma quando utilizar a fórmula na central a tela de calculo aparece para ser preenchido a informação.

O valor é calculado e substituído aonde o curso do texto estiver:

## **03. Texto**

Os campos de texto são usados basicamente para ser substituídos dentro do laudo

## **04. Data**

Existem duas **variáveis de data** disponíveis que podem ser utilizadas diretamente nas fórmulas, sem a necessidade de cadastro prévio:

* **DATAATUAL**: Representa a data em que a fórmula está sendo executada. É preenchida automaticamente pelo sistema no momento do cálculo.
* **DUM** (Data da Última Menstruação): É preenchida automaticamente se essa informação estiver registrada no exame. Caso não esteja, é possível informá-la manualmente na tela de cálculo da fórmula.

Além dessas variáveis, também é possível **cadastrar campos do tipo "Data"**, que podem ser utilizados tanto para substituição manual quanto para cálculos dentro da fórmula.

Nesse caso vamos subtrair datas o resultado vai ser o numero de dias da diferença

Calculo feito

## **05. Fórmula**

O campo do tipo **"Fórmula"** permite realizar cálculos diretamente dentro do campo, podendo inclusive utilizar outros campos como variáveis nas expressõe

Abaixo criamos dois campos numéricos e um campo fórmula

O campo do tipo formula adicionamos o calculo , somando os campos e dividindo por 10.

O cadastro da fórmula foi concluído. Lembre-se de que é possível criar **outros campos do tipo "Fórmula"** e adicioná-los conforme necessário.

Por exemplo, esse recurso pode ser utilizado para **calcular volumes pulmonares ou ovarianos**, criando campos separados para os lados **esquerdo** e **direito**, e depois somando-os em uma fórmula final.

Tela para preencher a formula na central.

Aqui é a formula calculada.

## **06. Lista**

Cadastro de uma lista:

Exemplo da lista na central de laudos aonde ao selecionar o item é substituído pelo campo "Nome".

## **06. Uso do Modelo**

Embora as fórmulas possam ser utilizadas de forma individual, a funcionalidade foi desenvolvida para ser aplicada principalmente em conjunto com o **cadastro de modelo**. Isso permite **posicionar as fórmulas e seus respectivos campos** diretamente dentro do texto do modelo, facilitando a automação no momento da seleção.

Ao selecionar uma fórmula e clicar em **"Selecionar"**, ela será inserida no texto exatamente **na posição onde o cursor estiver localizado**.

Também é possível inserir **campos** no modelo. Esses campos serão automaticamente substituídos pelos valores informados na **tela de cálculo** no momento da geração do laudo. Abaixo, apresentamos um exemplo fictício com várias fórmulas adicionadas ao modelo.

Para adicionar os campos de uma fórmula, observe que ao selecionar, por exemplo, a fórmula **DUM**, os **campos utilizados** por ela aparecem logo abaixo da área de seleção. Basta clicar no campo desejado para que ele seja inserido no texto.  
No exemplo, demonstramos como o cálculo do DUM é construído: após o sinal de **igual (=)**, informamos a fórmula que será executada.

Ao selecionar o modelo na central de laudos a tela de cálculo é aberta com todas as formas que compõem o modelo:

Após informar todos os campos e calcular o modelo preenche o laudo e as informações são substituídas.
