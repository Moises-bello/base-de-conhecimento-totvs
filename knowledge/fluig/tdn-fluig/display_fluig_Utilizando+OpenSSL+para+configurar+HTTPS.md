---
content_hash: 5cb76cafb6c7048937f319cbacfe3c74b5bef2f54b0a6bc00e79842adb494422
fetched_at: '2026-06-28T21:35:25.358776+00:00'
page_id: '281987983'
product: fluig
source: tdn-fluig
title: Utilizando OpenSSL para configurar HTTPS
type: documentation
url: https://tdn.totvs.com/display/fluig/Utilizando+OpenSSL+para+configurar+HTTPS
version: 19
---

4true.\*ndicenone

# Objetivo

Apresentar uma forma de gerar o arquivo CSR para solicitação de um certificado a uma entidade certificadora utilizando o utilitário OpenSSL. Mostrar também que, através deste utilitário você pode gerar um repositório de certificados no formato PKCS12 para utilizar em configurações do servidor de aplicação dependendo do dimensionamento do ambiente. Além disso, mostrar os comandos para exportação do certificado e chave privada, do repositório com esta extensão.

Atenção!

É importante mencionar que qualquer utilitário que consiga gerar o certificado no formato correto pode ser utilizado. Recomendamos o [OpenSSL](https://www.openssl.org/) pela facilidade de uso e por ser o padrão de mercado. Este procedimento não tem relação com as configurações feitas na plataforma. Portanto, deve ser escolhido o utilitário mais adequado para sua empresa.

Cada entidade certificadora trabalha de forma diferente, com diversos formatos de arquivos. Portanto, muitas vezes, será necessário exportar os arquivos em formatos adequados para a configurações no servidor de aplicação. Algumas não solicitam o arquivo CSR para geração do certificado.

Sugestão

Recomendamos a utilização do sistema operacional **Linux** para a execução desses procedimentos do **OpenSSL**.

# Gerar arquivo CSRCSR

O *Certificate Sign Request* (CSR) é uma arquivo enviado para uma entidade certificadora a fim de ser gerado os certificados de um determinado domínio.

Para gerar este arquivo recomendamos a utilização do utilitário [OpenSSL](https://www.openssl.org/). Sua instalação no servidor da plataforma não tem impacto no funcionamento da plataforma. Para a instalação do [OpenSSL](https://www.openssl.org/) recomendamos fazer [download](https://wiki.openssl.org/index.php/Binaries) da última versão disponível para seu sistema operacional.

Abaixo seguem os passos para a geração do arquivo utilizando como base a ferramenta [OpenSSL](https://www.openssl.org/).

Após abrir o executável é necessário executar o comando para iniciar o procedimento de geração do CSR:

bashEclipse

Informe os dados solicitados pelo OpenSSL para a geração do CSR:

Após a conclusão dos passos serão gerados dois arquivos: o arquivo com extensão CSR (certificate.csr) deve ser submetido à entidade certificadora que irá gerar o certificado. O outro arquivo (arquivo\_chave.key) é a chave privada, que deve ser armazenada em local seguro.

Tanto a chave privada (arquivo\_chave.key) quanto o certificado gerado pela entidade (certificado.crt ou certificado.cer), devem ser salvos em uma pasta no servidor onde fica a aplicação. Recomendamos a criação de uma pasta na raiz da instalação da plataforma (Exemplo: [Instalação da plataforma]/certificado), Vale mencionar que esses arquivos podem ser salvos em qualquer pasta do diretório do servidor.

Quando receber o certificado gerado pela entidade, continue o processo de configuração. Se desejar gerar o repositório (Keystore) no formato PKCS12, siga as instruções abaixo. Para realizar as configurações SSL na plataforma ou também gerar um repositório de certificados na extensão JKS no Java, acesse a documentação .

CSR

# Gerar PKCS12

Os arquivos PKCS12 são um tipo de repositório de certificado utilizado na configuração de HTTPS. Para gerar o repositório é necessário ter o certificado (enviado pela entidade certificadora) e a chave privada.

O arquivo arquivo\_chave.key é a chave privada, enquanto certificado.crt é o certificado retornado pela entidade certificadora.

Após a execução do comando abaixo, é gerado o arquivo com extensão .p12 (repositorio.p12).

bashEclipse

Dependendo do dimensionamento do seu ambiente e web server utilizado, não será necessário ter um repositório com esta extensão portanto, o certificado deverá ser exportado para utilização em outro formato de arquivo.

Para exportar o arquivo "key" do repositório "p12", execute o seguinte comando:

bash

Para exportar o arquivo "crt", "cer" ou "ca" do repositório "p12", execute o seguinte comando:

bashEclipse

Para exportar um certificado com uma cadeia completa, incluindo o certificado intermediário, execute o seguinte comando:

bashEclipseImportante!

Se o Fluig não aceitar a senha configurada no certificado, refaça o pacote utilizando as tags **-legacy** e **-descert**, conforme exemplo abaixo:

bashEclipse

Saiba mais em [Erro de senha incorreta ao configurar certificado HTTPS (*failed to decrypt safe contents entry*)](https://centraldeatendimento.fluig.com/hc/pt-br/articles/22399365622679-Fluig-Plataforma-CON-Erro-de-senha-incorreta-ao-configurar-certificado-HTTPS-failed-to-decrypt-safe-contents-entry).

Para consultar como gerar o Bundle, acesse a documentação de .

Se o repositório de certificados (.p12) estiver em uma pasta específica ou desejar salvar os arquivos exportados em uma pasta específica, o diretório deve ser informado no comando a ser executado. Exemplo:

bashEclipse
