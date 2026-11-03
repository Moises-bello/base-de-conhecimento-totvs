---
content_hash: f834ad1daa7eb8570be7e50752713db41cfed305ac1dc1a0823a77a1e15726eb
fetched_at: '2026-06-28T21:35:30.450149+00:00'
page_id: '856923748'
product: fluig
source: tdn-fluig
title: 107 - Como criar e configurar o limite de registros de update no banco de dados
  utilizado pelo Fluig
type: documentation
url: https://tdn.totvs.com/display/fluig/107+-+Como+criar+e+configurar+o+limite+de+registros+de+update+no+banco+de+dados+utilizado+pelo+Fluig
version: 10
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** fluig

# Ocorrência

No processo de atualização para o Fluig 1.8.0 são executados updates no banco de dados, onde é realizada a criação de uma tabela temporária para a cópia de registros. É utilizado o limite de 10.000 (dez mil) registros durante a cópia dos dados. Em um ambiente com alto volume de dados, o update pode demorar por conta do total de registros x limite de registros para a cópia na tabela temporária. É possível aumentar esse limite seguindo os passos abaixo, para que o update seja executado em menos tempo.

Atenção

Consulte o seu DBA para realizar a configuração abaixo, para evitar problemas no servidor de banco de dados.

Importante

A configuração descrita nesta documentação é válida para o Fluig 1.7.1 (qualquer release). Ao atualizar para o Fluig 1.8.2, caso o ambiente esteja utilizando o Fluig 1.8.0 ou superior, o update já foi executado e a configuração abaixo não será utilizada, caso aplicada.

# Solução

Veja a seguir o passo a passo:

**Ambiente on-premises:**

1. Pare o serviço do Fluig;
2. Efetue o download do Fluig 1.8.2;
3. Faça a atualização do ambiente para o Fluig 1.8.2, conforme documentação;
4. Navegue até o diretório de instalação do Fluig:

   #f2f2f2#f2f2f2
   * Acesse o diretório onde o Fluig está instalado.
   * Acesse a pasta <FLUIG>/appserver/domain/configuration/
5. Localize e edite o arquivo domain.xml:

   #f2f2f2#f2f2f2
   * No diretório mencionado, localize o arquivo domain.xml
6. No arquivo domain.xml, localize a tag “<system-properties>”

   #f2f2f2#f2f2f2
   * Abra o arquivo domain.xml em um editor de texto de sua preferência.
   * Localize a tag <system-properties>1Imagem
7. Adicione a propriedade FLUIG\_DB\_PROCESS\_DEFINITION\_LIMIT:

   #f2f2f2#f2f2f2
   * Adicione a propriedade FLUIG\_DB\_PROCESS\_DEFINITION\_LIMIT com o valor desejado (value) para ser o limite de registros na cópia de dados na tag <system-properties>

Exemplo:

        <property name="FLUIG\_DB\_PROCESS\_DEFINITION\_LIMIT" value="50000"/>   

1Imagem

8**.** Inicie o serviço do Fluig;

        9. Acompanhe no log a execução do update.

Atenção

Se você utiliza o Fluig em container, deverá criar a propriedade FLUIG\_DB\_PROCESS\_DEFINITION\_LIMIT como um fragmento de XML, conforme [documentado aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=682441318#Guiadeexecu%C3%A7%C3%A3odaplataformaemDocker-SystemProperties).
