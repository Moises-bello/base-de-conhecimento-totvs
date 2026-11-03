---
content_hash: 017fe079cc10b869b586bf9dacdfc0eaabfb559b86899c0dd34cd10d36ef2cfe
fetched_at: '2026-06-29T00:11:55.658185+00:00'
page_id: '862607918'
product: rm
source: tdn-rm
title: 2.1.1 - Comparação de Diretório
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=862607918
version: 24
---

# O que é?

A atividade realiza a comparação de todos os arquivos de um determinado tipo entre dois diretórios diferentes. Ela permite comparar tanto diretórios inteiros quanto arquivos individuais, garantindo que o conteúdo e a estrutura dos dados estejam de acordo com o esperado."

# Para que serve?

Serve para validar os resultados dos testes comparando arquivos e diretórios gerados com resultados esperados. Esta atividade é útil para validar se um arquivo gerado ou diretório modificado após uma execução de uma outra atividade em projeto de teste essencial para garantir a integridade e a precisão dos resultados em projetos de teste.

# Exemplo de Uso

Como cadastrarComo Cadastrar 1. Navegação para o cadastro

 1. Navegue no menu do TOTVS Automação de Testes e clique em: **Atividades** → **Arquivos** → **Comparação de Diretório.**

 2. Na tabela que será mostrada, clique no botão verde em destaque.

  
2. Link para Definir cabeçalho (Nome e nível de acesso)

[Clique aqui para obter as informações do cabeçalho](https://tdn.totvs.com/pages/viewpage.action?pageId=859591806)

3. Preenchimento dos CamposVersão

Especifica a versão da atividade em questão. O objetivo de versionar uma atividade é para quando necessitamos ter mais de uma atividade em versões diferentes. Isso irá nos auxiliar a ter um histórico de atualizações e assegurar que as mudanças feitas sejam rastreáveis e reversíveis, se necessário.

Se for necessário utilizar mais de uma versão do RM no seu ambiente, é recomendado que a versão da atividade seja compatível com o sistema RM em uso. Caso contrário, pode-se optar por uma versão padrão de sua preferência.

*Exemplo utilizando a versão do RM*

*Exemplo utilizando a versão padrão*

Descrição de Atividade 

Fornece uma descrição detalhada da atividade, explicando seu propósito e operações, facilitando a compreensão e manutenção futura.

Padrão de busca de arquivos 

 Este parâmetro define quais tipos de arquivos serão incluídos na comparação. Você deve especificar a extensão dos arquivos que deseja comparar, como `.txt`

Exemplo:

Esta opção define se a comparação incluirá os subdiretórios dos diretórios especificados. Se ativada, a ferramenta compara tanto os arquivos do nível principal quanto os contidos nos subdiretórios, garantindo a análise completa da estrutura hierárquica dos diretórios.

Caminho do diretório da esquerda

Este é o diretório onde você armazena os arquivos de referência, ou seja, aqueles que contêm os resultados esperados ou anteriores que você deseja comparar. Esses arquivos servem como base para a comparação e devem estar organizados na mesma estrutura que o diretório da direita.

Caminho do diretório da direita 

Este diretório contém os novos arquivos gerados, que serão comparados com os arquivos do diretório da esquerda. Ele deve replicar a estrutura do diretório da esquerda para que a comparação funcione corretamente. A comparação identifica diferenças entre os arquivos de ambos os diretórios, ajudando a verificar se os novos resultados estão de acordo com os esperados.

Variáveis de ambiente

As Variáveis de Ambiente são utilizadas para configurar e personalizar o comportamento da Atividade. Elas permitem definir valores específicos ou dinâmicos que podem ser usados durante a execução dos testes, assegurando que o teste execute conforme o ambiente em que o mesmo é executado. As Variáveis de Ambiente são cadastradas no cadastro de Ambiente onde informamos os valores fixos ou de forma dinãmica no cadastro de Script SQL.

Consulte quais campos permitem o uso das Variáveis de Ambiente nessa Atividade:

[Comparação de Diretório - Variáveis de Ambiente.](https://tdn.totvs.com/pages/editpage.action?pageId=863911900)

Saiba mais sobre [Ambientes](https://tdn.totvs.com/display/LRM/4+-+Ambientes).

Exemplo práticoExemplo prático

Imagine que você é um Analista do RM e executou um projeto de teste que contém um Webservice que gera dois arquivos em um determinado diretório.

No **Diretório Gabarito** , há um arquivo chamado **Exemplo.txt** com o seguinte conteúdo:

E um outro arquivo chamado txt Exemplo2

Já no **Diretório Resultado**, há apenas um arquivo chamado 'Exemplo.txt' com um conteúdo diferente:

Notamos que o conteúdo do **Diretório Resultado** apresenta uma diferença na escrita em comparação com o **Diretório Gabarito.**

Sendo assim, no log da atividade de comparação de diretórios no **TOTVS Automação de Testes,** é possível observar que houve um erro indicando que o diretório da direita está diferente do diretório da esquerda.

Foi realizada a correção no**Diretório Resultado,**garantindo que contenha os mesmos arquivos e conteúdos em ambos diretórios

Dessa forma, o log da atividade de comparação de diretórios no **TOTVS Automação de Testes** mostra um registro de sucesso, indicando que o diretório à direita **não** difere do diretório à esquerda após a correção do arquivo.

Detalhes da Execução

Para garantir a precisão na validação dos arquivos na **Atividade de comparação de diretório**, analisamos os detalhes de execução de cada arquivo em ambos os diretórios. Isso nos permite identificar diferenças de forma confiável e assegurar que os resultados dos testes estejam de acordo com as expectativas.

No campo **Atividades Executadas**, clique no botão mostrado para ver mais detalhes da execução.

Sendo assim, contamos com os seguintes resultados da execução:

Status

### Status Sucesso:

### 

*Indica que não foram encontradas diferenças entre os diretórios comparados; todos os arquivos e subdiretórios estão idênticos e sincronizados.*

### Status Falha:

*Indica que foram encontradas diferenças entre os diretórios comparados, como arquivos ausentes, conteúdos divergentes ou variações nos atributos dos arquivos.*

Resultado dos Arquivos

**Arquivo Idêntico:** Arquivo presente em ambos os diretórios com conteúdo exatamente igual.

**Arquivo Diferente:** Arquivo presente em ambos os diretórios, mas com diferenças no conteúdo.

**Apenas Esquerda:** Arquivo encontrado apenas no diretório de origem (à esquerda).

**Apenas Direita:** Arquivo encontrado apenas no diretório de destino (à direita).

---

# Saiba mais

Antes de realizar uma comparação, certifique-se de que seus diretórios estejam organizados de forma consistente. Adote uma estrutura de pastas clara e padronizada para evitar confusões e garantir que a ferramenta compare os arquivos corretamente.

Ative a opção "Comparar Subdiretórios" apenas se precisar comparar toda a estrutura hierárquica. Caso contrário, desative-a para acelerar o processo de comparação e concentrar-se apenas nos arquivos principais.

Utilize variáveis de ambiente para ajustar as comparações ao seu ambiente de testes. Isso permite configurar caminhos dinâmicos e outros parâmetros específicos sem a necessidade de ajustes manuais para cada comparação.

Para que a comparação de diretórios funcione corretamente, ambos os diretórios devem ter a mesma estrutura de pastas, incluindo nomes idênticos para os subdiretórios. Além disso, os arquivos a serem comparados devem ter o mesmo nome e extensão.

# FAQ

**P:****O que acontece se os diretórios comparados tiverem estruturas diferentes?**

R: Se os diretórios não tiverem a mesma estrutura, O TOTVS Automação de Testes pode não conseguir comparar todos os arquivos corretamente. Para garantir uma comparação precisa, os diretórios devem ter a mesma organização de pastas e nomes de arquivos.

**P:** **O que devo fazer se a comparação falhar?**

R: Verifique se os caminhos dos diretórios estão corretos, se os arquivos possuem as extensões especificadas, e se as estruturas dos diretórios são idênticas. Se tudo estiver correto, revise as configurações de variáveis de ambiente.
