---
content_hash: da5f36d9f99434ae4649e68dd1ff02bf9f6366ac4edbdb9f48dc9be1ccc12541
fetched_at: '2026-06-29T00:09:29.756318+00:00'
page_id: '425458255'
product: rm
source: tdn-rm
title: Criação de Campos Complementares para Inscrição e Matrícula
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458255
version: 20
---

Opcionalmente, o usuário poderá criar campos complementares para compor o cadastro. Os "Campos complementares" da inscrição e da matrícula serão disponibilizados no sistema pelo menu: Campos complementares => Inscrição e matrícula do candidato.**(\*1)**

Nota (\*1)

A partir da versão 12.1.2406, os campos complementares também poderão ser utilizados na matrícula, então o nome exibido passará a ser "Inscrição e matrícula de candidato" .

É possível criar campos complementares com outros tipos de dados, como números inteiros, data, texto simples, números reais, alfanuméricos, entre outros.

Para alfanumérico, é possível aplicar um tipo de texto simples, link para um e-mail, link de uma URL e link para chamar um telefone usando o Skype. É preciso que o Skype esteja instalado em sua estação para que funcione corretamente.

Outra vantagem ao usar os campos complementares é que você pode associar o campo a uma tabela dinâmica ou a uma Fórmula.

**Tabela Dinâmica:**

* Tome como exemplo o nosso campo Tipo Sanguíneo. Você pode cadastrar uma tabela dinâmica, e como itens da tabela você inclui os tipos existentes de sangue: A+, B+, AB+ O+, A-, B-, AB- e O-. Depois, associe no cadastro de campo complementar a tabela dinâmica com os tipos de sangue.

**Fórmula:**

* A fórmula é utilizada para validar se o que foi digitado no campo complementar é valido, sendo assim ela deve retornar 1 para positivo e 0 para negativo.

Caso o campo complementar seja criado usando o “Subtipo do campo como Texto” será possível aplicar uma máscara customizada que também será aplicada no portal.

É importante ressaltar que serão permitidos somente os tipos e caracteres disponibilizados nos “Tipos Customizados” do cadastro do campo complementar.

Importante

O portal do processo seletivo não aceita campos complementares do tipo data com "máscara" definida com informação de hora, somente data (exemplo: dd/MM/yyyy), para utilização de hora no campo de data é necessário utilizar a opção de formato no campo complementar.

Tipo de data não aceito não aceito:

Tipo de data aceito:

No TOTVS Processo Seletivo, para que os campos complementares sejam utilizados, é preciso que sejam habilitados para a filial através do processo .

Mesmo que um processo seletivo esteja parametrizado para ser visível em todas as filiais, e este processo possua campos complementares, é necessário realizar o processo de habilitação dos campos complementares em todas as filiais. Caso contrário eles não serão exibidos.
