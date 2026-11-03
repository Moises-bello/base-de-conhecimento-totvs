---
content_hash: 42708730562718d821dad96eb48fccda609b2ff4bcb3443589aab240f347d07d
fetched_at: '2026-06-29T00:09:24.090312+00:00'
page_id: '423937886'
product: rm
source: tdn-rm
title: Fabricantes
type: documentation
url: https://tdn.totvs.com/display/LRM/Fabricantes
version: 59
---

Cadastro responsável por registrar fabricantes de produtos.

Procedimento para cadastro

Localizado no menu "Cadastros → Fabricantes",

 A denominação "Fabricante" para esta tabela é default do sistema e poderá ser alterada através do menu [Ambiente | Parâmetros | Gestão de Estoque Compras e Faturamento | Tabelas | Fabricantes | no campo Nome Fabricante](https://tdn.totvs.com/x/GstEGQ).

Podem ser vinculados ao cadastro do produto na tela aba identificação do [cadastro de Produtos](https://tdn.totvs.com/x/ActEGQ).

Cards2Identificação

* **Código**: Deve ser informado um código que identificará o fabricante, conforme máscara definida nos parâmetros.
* **Descrição**: Deve ser informado um nome ou uma descrição para o fabricante
* **CNPJ**: Deve ser informado o número de inscrição/cnpj do fabricante
* **Inscrição Estadual:** Deve ser informado a inscrição estadual do fabricante

3Endereço

* **Rua**: Deve ser informado a rua do endereço do fabricante
* **Número**: Deve ser informado o número do endereço do fabricante
* **Complemento**: Deve ser informado, caso seja necessário, um complemento para o endereço do fabricante
* **Bairro:** Deve ser informado o bairro do endereço do fabricante
* **Cidade:** Deve ser informado a cidade do endereço do fabricante
* **Estado:** Deve ser informado o estado do endereço do fabricante
* **CEP:** Deve ser informado o CEP do endereço do fabricante
* **País:** Deve ser informado o país
* **Telefone:** Deve ser informado a inscrição estadual do fabricante
* **Celular:** Deve ser informado a inscrição estadual do fabricante
* **Contato:** Deve ser informado a inscrição estadual do fabricante
4Outros Dados

                                             

* **Desconto Padrão**: Deve ser informada o valor de desconto padrão para o fabricante
* **Comissão (%)**: Deve ser informada a porcentagem que representará o valor da comissão para o fabricante
* **Observação** : Deve ser informada uma informação complementar, caso seja necessário
* **Classificação:** São campos que podem ser customizados para trazer informações adicionais caso haja necessidade

Usar Inteligência Artificial Para Extrair Dados

Essa funcionalidade tem o objetivo de facilitar o cadastro de um fabricante, permitindo o upload de um arquivo contendo as informações necessárias para o registro. O sistema realiza automaticamente a extração dos dados do fabricante e preenche os campos do formulário, restando ao usuário apenas validar as informações. Esses dados podem ser obtidos a partir do Cartão CNPJ ou do Comprovante de Inscrição e de Situação Cadastral.

Para utilizar esta funcionalidade, deve ser marcando a flag Usar inteligência artificial para auxiliar no preenchimento de cadastro disponibilizada em  [Ambiente | Parâmetros | Gestão de Estoque Compras e Faturamento | Parâmetros Gerais | Definições Gerais | Definições Gerais 3/3](https://tdn.totvs.com/x/GstEGQ)

Aviso

Recurso disponivel a partir da versão 12.1.2602.

Processo de importação dos dados.

Ao Incluir o cadastro de Fabricantes, o botão Extrair Dados Doc. estará habilitado conforme a imagem abaixo:

Clicando no botão será aberta a tela onde iremos selecionar o arquivo dentro de nosso ambiente de trabalho:

Ao Clicar no botão Cartão CNPJ Fabricante será aberta uma tela para selecionar o arquivo desejado.

Após a Seleção deste arquivo deve-se clicar em Enviar Dados e o upload do arquivo será iniciado, quando  
o processo for finalizado o sistema irá retornar a tela abaixo:

Clicando no OK e fechando a tela anterior os dados do Fabricante estarão preenchidos.

Cópia de Fabricantes Entre Coligadas

É possível se copiar registros fabricantes de uma coligada para outra, para isso, utilize o processo '[Copiar Fabricantes entre coligadas](https://tdn.totvs.com/x/p8hEGQ)' e informe para qual coligada, se a cópia será só do registro corrente ou todos e se o registro já existir na coligada destino se mantém o registro existente ou se copia o novo por cima.
