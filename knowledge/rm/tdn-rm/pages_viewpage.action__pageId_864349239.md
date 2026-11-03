---
content_hash: 0f57714d89cd7af8a5ee0beaaa07538cf8975175caf7eb4faf53789407dbfd3e
fetched_at: '2026-06-29T00:11:55.863794+00:00'
page_id: '864349239'
product: rm
source: tdn-rm
title: 2.1.2 - Comparação de Arquivos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=864349239
version: 13
---

# O que é?

Esta atividade realiza a comparação entre dois arquivos, utilizando os caminhos especificados para cada um deles. A comparação é aplicada exclusivamente a arquivos de texto.

**Exemplo:** “.pdf”, “.txt”, “.doc”, “.xml”

# Para que serve?

Essa atividade é utilizada para validar os resultados dos testes, comparando arquivos gerados durante a execução com arquivos que contêm os resultados esperados. A ferramenta é especialmente útil para garantir que as aplicações produzem saídas corretas e consistentes ao longo do tempo.

Vale destacar que esta atividade compara apenas um arquivo por vez, o que significa que os diretórios utilizados não devem conter mais de um arquivo. Para cada par de arquivos a ser comparado, deve-se criar uma nova atividade. Caso haja necessidade de comparar mais de um arquivo ao mesmo tempo, é recomendável utilizar a opção de comparação por diretórios.

# Exemplo de Uso

Como cadastrarComo Cadastrar 1. Navegação para o cadastro

 1. Navegue no menu do TOTVS Automação de Testes e clique em: **Atividades** → **Arquivos** → **Comparação de Arquivo.**

 2. Na tabela que será mostrada, clique no botão verde em destaque.

2. Link para Definir cabeçalho (Nome e nível de acesso)

[Clique aqui para obter as informações do cabeçalho](https://tdn.totvs.com/pages/viewpage.action?pageId=859591806)

3. Preenchimento dos CamposVersão

Especifica a versão da atividade em questão. O objetivo de versionar uma atividade é para quando necessitamos ter mais de uma atividade em versões diferentes. Isso irá nos auxiliar a ter um histórico de atualizações e assegurar que as mudanças feitas sejam rastreáveis e reversíveis, se necessário.

Se for necessário utilizar mais de uma versão do RM no seu ambiente, é recomendado que a versão da atividade seja compatível com o sistema RM em uso. Caso contrário, pode-se optar por uma versão padrão de sua preferência.

*Exemplo utilizando a versão do RM*

*Exemplo utilizando a versão padrão*

Descrição

Fornece uma descrição detalhada da atividade, explicando seu propósito e operações, facilitando a compreensão e manutenção futura.

Caminho do diretório da esquerda

Este é o diretório do arquivo de referência, ou seja, o arquivo que contêm o resultado esperado que você deseja comparar. Esse arquivo serve como base para a comparação.

Caminho do diretório da direita 

Este diretório contém arquivo que você quer comparar com o arquivo de referência do diretório da esquerda. A comparação identifica diferenças entre os arquivos de ambos os diretórios, ajudando a verificar se o resultado está de acordo com o esperado.

Variáveis de ambiente

As Variáveis de Ambiente são utilizadas para configurar e personalizar o comportamento da Atividade. Elas permitem definir valores específicos ou dinâmicos que podem ser usados durante a execução dos testes, assegurando que o teste execute conforme o ambiente em que o mesmo é executado. As Variáveis de Ambiente são cadastradas no cadastro de Ambiente onde informamos os valores fixos ou de forma dinãmica no cadastro de Script SQL.

Consulte quais campos permitem o uso das Variáveis de Ambiente nessa Atividade:

[Comparação de Arquivos - Variáveis de Ambiente.](https://tdn.totvs.com/pages/viewpage.action?pageId=864995980)

Saiba mais sobre [Ambientes](https://tdn.totvs.com/display/LRM/4+-+Ambientes).

Exemplo prático

Como analista do produto educacional RM, você recebeu o projeto para testar um webservice que gera o histórico escolar de um aluno em formato PDF. Após a solicitação, o arquivo PDF é gerado e salvo em um diretório específico.

Seu objetivo é validar se o relatório foi gerado corretamente, tanto em termos de estrutura quanto de conteúdo, garantindo que todas as informações estejam preenchidas de forma precisa.

Para isso, você deve criar uma atividade de comparação de arquivos. Nesse processo, o diretório à esquerda deverá conter o arquivo de referência, ou gabarito, que representa o padrão esperado. O diretório à direita, por sua vez, deverá conter o arquivo gerado pelo webservice durante o teste.

Ao incluir essa atividade no seu projeto de teste, você poderá verificar de forma automatizada se a geração do relatório foi bem-sucedida e se o conteúdo do PDF corresponde ao esperado. Isso assegura que o sistema esteja funcionando corretamente e que as informações do histórico escolar sejam geradas com precisão.

# Saiba mais

Deve-se sempre informar o nome e a extensão dos arquivos que você quer comparar.

Esta Atividade não fornece ou necessita de recursos.

Esta atividade está restrita a comparar um arquivo por vez; para comparar múltiplos arquivos simultaneamente, a funcionalidade de comparação de diretórios deve ser utilizada.

# FAQ

**P: Quais tipos de arquivos posso comparar?**

R: A atividade se limita à comparação de arquivos de texto, como ".pdf", ".txt", ".doc", e ".xml". Arquivos binários ou outros tipos de documentos não serão comparados corretamente.

**P: Posso comparar mais de um arquivo ao mesmo tempo?**

R: Não, esta atividade compara apenas um arquivo por vez. Se você precisar comparar vários arquivos, utilize a comparação de diretórios.

**P: Minha atividade falhou, e agora?**

**R:** Certifique-se de que o diretório especificado esteja correto, que os arquivos tenham o mesmo conteúdo e que o nome e a extensão dos arquivos estejam corretos.
