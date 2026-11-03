---
content_hash: 70cd02eae533719b63e6bdbc243eed741dc5b2c7b4284b0aeac25e11c21ca742
fetched_at: '2026-06-29T00:09:11.416191+00:00'
page_id: '403746949'
product: rm
source: tdn-rm
title: Campos Complementares (RM)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=403746949
version: 23
---

# Índice

---

# Introdução

---

Campos complementares são os campos que podem ser criados dentro do aplicativo.

# Objetivo

---

Complementar informações de um cadastro, com os dados que você desejar e da maneira que desejar.

# Inserir um campo complementar

---

É possível, por exemplo, criar um campo complementar no cadastro de Funcionários que contenha o Tipo Sanguíneo do funcionário.

É possível criar campos complementares com outros tipos de dados, como números inteiros, data, texto simples, números reais, alfanuméricos, entre outros.

515px  
Para alfanumérico, é possível aplicar um tipo de texto simples, link para um e-mail, link de uma URL e link para chamar um telefone usando o Skype. É preciso que o Skype esteja instalado em sua estação para que funcione corretamente.

Outra vantagem ao usar os campos complementares é que você pode associar o campo a uma tabela dinâmica ou a uma Fórmula.

**Tabela Dinâmica:**

* Tome como exemplo o nosso campo Tipo Sanguíneo. Você pode cadastrar uma tabela dinâmica, e como itens da tabela você inclui os tipos existentes de sangue: A+, B+, AB+ O+, A-, B-, AB- e O-. Depois, associe no cadastro de campo complementar a tabela dinâmica com os tipos de sangue.

**Fórmula:**

* A fórmula é utilizada para validar se o que foi digitado no campo complementar é valido, sendo assim ela deve retornar 1 para positivo e 0 para negativo.

Quando cadastrar um funcionário, você não precisa preencher um tipo de sangue, basta selecionar um na lista que foi cadastrada nos itens da tabela dinâmica. Quando você for associar um campo complementar a uma tabela dinâmica, você poder pesquisar por código ou descrição do campo.

Por fim, você pode definir também o tamanho do texto contido nos dados, definir um valor default (padrão) para vir no campo sempre que criar um registro e definir a ordem de listagem do campo.

# Inserindo Máscara e Formatação

---

**Novidades:**

A partir da versão 12.1.28, será possível incluir máscaras ou formato em campos complementares de tipos específicos, como: real, alfanumérico (telefone) e data.

São disponibilizados alguns valores de máscara e formato padrão, mas também é permitido criar um tipo customizado. Basta clicar na aba 'Tipo Customizado'.

**Recomendações:**

* **Campos do tipo** **telefone**, recomendamos o uso de máscara; Para esse tipo de dado, a máscara proporcionará uma experiência melhor para o usuário do sistema, pois a medida que os números forem digitados, serão exibidos os caracteres da máscara, como por exemplo: (31) 3333-3333.

* **Campos do tipo **r**eal** (monetário em real), recomendamos o uso de formato; Para esse tipo de dado, o formato proporcionará uma experiência melhor para o usuário do sistema, pois a máscara determinaria e limitaria a quantidade de números que o dado deveria conter. O formato, após mudar o foco do campo, ele ajustará o valor, independente da quantidade de números que o valor possuir.

Como será apresentado na tela **antes** de informar os dados:

Como será apresentado na tela **após**informar os dados:

**Obs.:** Alterar máscaras e formatos de campos existentes para uma formatação menor que a atual podem gerar perda de dados.

Ex.: Um campo decimal possui um formato com 2 (duas) casas decimais. Ao alterar o formato desse campo para ter apenas 1 (uma) casa decimal, e editar um registro que já tenha um valor, ele será alterado para ter apenas 1 casa decimal.

# Formato e mascara em campos do tipo Data

### Quando utilizar formato?

O formato é utilizado quando você precisa que os dados inseridos sejam validados em seus respectivos tipos e ordem.  
Por exemplo:  
Ao utilizar o formato: **dd/MM/yyyy** espera-se que o primeiro campo **dd** seja os 2 digitos do dia, o **MM** seja os 2 digitos do mês e **yyyy** seja os 4 digitos do ano. Conforme essa documentação que explica mais sobre os tipos de dados que podem ser utilizados.  
Dessa forma, os dados inseridos serão validados na ordem e tipo informados.

Alguns exemplos de tipos que podem ser utilizados:

|  |  |  |
| --- | --- | --- |
| **Símbolo** | **Descrição** | **Exemplo** |
| dd | Dia do mês (2 dígitos) | 01, 02, 31 |
| MM | Mês (2 dígitos) | 01, 02, 12 |
| yy | Ano (2 dígitos) | 23, 24, 99 |
| yyyy | Ano (4 dígitos) | 2023, 2024, 2999 |
| HH | Hora (2 dígitos) | 00, 01, 23 |
| mm | Minutos (2 dígitos) | 00, 01, 59 |
| ss | Segundos (2 dígitos) | 00, 01, 59 |
| SSS | Milissegundos (3 dígitos) | 000, 001, 999 |
| Z | Fuso horário (UTC) | +00:00, -05:00, +13:00 |
| zzzz | Nome do fuso horário | America/Sao\_Paulo, Europe/Berlin |

### Quando utilizar mascara?

A mascara é um mecanismo que facilita a inserção pois reserva espaços no campo na hora de inserir os valores.  
Os dados inseridos são validados apenas com o local atual do sistema.  
Por exemplo:  
Ao utilizar a mascara **99/99/9999** vai gerar um campo com a seguinte aparência **\_\_/\_\_/\_\_\_\_**.

Se com essa mascara for informado o valor **04/05/2020** no **Brasil** o texto será convertido para o dia **04 de Maio de 2020**,   
já se por exemplo for nos **Estados Unidos** o mesmo valor será convertido para a data **05 de maio de 2020**.

# Quebra de Linha

A partir da versão 12.1.32, quebras de linhas são permitidas apenas em campos complementares do **tipo Texto** ou **tipo Alfanumérico** de **subtipo Texto** caso o campo **Multilinha**esteja marcado:

Importante

A partir da versão 12.1.24.195 e superiores, o tamanho de campos Alfanuméricos podem ser alterados para um valor maior. Reduções de tamanho não são permitidas.

A partir da versão 12.1.28.175, ao trocar de módulo a tela de campos complementares é fechada automaticamente, para que não haja conflito no contexto da aplicação.

Atenção

Campos com nomes que coincidam com campos do Contexto do RM, terão seu valor default atribuído para o valor presente no Contexto na leitura do registro.

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Campos Complementares Globais

falsefalse

**Status:** Finalizado

false

**Data:** 31/10/2018

false

**Autores:**
