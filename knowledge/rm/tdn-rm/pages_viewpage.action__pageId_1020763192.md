---
content_hash: b91a31a0967ccddf6da41c6a2d63519bc3b0f728d91d4ce6a1a3ed7e188d75cd
fetched_at: '2026-06-29T00:05:48.010694+00:00'
page_id: '1020763192'
product: rm
source: tdn-rm
title: Leitura do Cartão CNPJ no cadastro de fornecedores
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1020763192
version: 6
---

Disponibilização do Recurso

Funcionalidade disponível a partir da release 12.1.2510, patch 12.1.2510.141.

A ferramenta de inteligência artificial, com tecnologia DTA Vision Document, tem como objetivo ler uma imagem (arquivos no formato PDF, PNG, JPEG, JPG e WEBP). Ao habilitarmos esse novo recurso podemos automatizar o preenchimento de alguns campos (listados ao final desse documento) no **cadastro do** **fornecedor**, através da Leitura do Cartão CNPJ.

Para ter acesso a esse recurso é necessário habilitar os parâmetros relacionados à "Inteligência Artificial" do TOTVS Gestão Financeira, marcando o parâmetro "Habilitar assistentes de Inteligência Artificial" e em "Assistentes" marcar o parâmetro "Ler cartão CNPJ no cadastro de Cliente/Fornecedor".

Após habilitação do parâmetro, a tela de **Cadastro de Cliente/Fornecedor** quando selecionada a **Categoria "Pessoa Jurídica"** passa a exibir o botão **"Ler Cartão CNPJ"**na aba *Identificação,* permitindo o acesso ao recurso que realiza a extração dos dados do arquivo enviado.

Campos que são atualizados através da leitura do Cartão CNPJ:

* Nome Fantasia / Social
* Nome
* CPF/CNPJ
* Endereço da aba "Principal"
  + CEP
  + Tipo de Rua (com base no prefixo informado no campo Logradouro do Cartão CNPJ, caso seja Rua ou Avenida)
  + Rua
  + Número
  + Complemento
  + Bairro
  + Estado
  + Município
  + País
  + Telefone
  + Fax (quando há mais de um telefone no campo do Cartão CNPJ)
  + E-mail
  + Contato
* Data Início das Ativ. (na aba Dados Adicionais)

Atenção

* Como o Cartão CNPJ é destinado a Pessoa Jurídica, o recurso só é disponibilizado para a categoria de mesmo tipo.
* Após clicar em enviar, será possível fechar para conferir os dados importados e se necessária nova leitura, deve clicar no botão e enviar novo documento.
* Ao acessar a funcionalidade, selecionando um novo Cartão CNPJ e clicando em enviar dados, todos os campos listados acima são atualizados com as informações contidas no novo documento enviado.
* A funcionalidade de OCR ou reconhecimento de texto, pode apresentar erros de extração dada a qualidade dos documentos enviados. Sempre**confira todos os dados** antes de salvar o fornecedor no sistema.
