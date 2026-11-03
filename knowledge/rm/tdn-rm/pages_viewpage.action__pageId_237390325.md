---
content_hash: 10d2bdff6b6ead70a84c4baecf18ba4771a4c1e445dbd2794176e736a8531da4
fetched_at: '2026-06-29T00:08:07.795961+00:00'
page_id: '237390325'
product: rm
source: tdn-rm
title: Diretório Pré Determinado Gerador de Saídas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=237390325
version: 12
---

## **CONTEÚDO**

    O objetivo deste documento é mostrar como é feita a geração de Layouts no Gerador de Saídas em diretório predeterminado. 

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

  Foi criado uma funcionalidade para gerar Layouts em um diretório predeterminado, no qual o usuário poderá alterar o arquivo gerado (Caso tenha permissão). Essa funcionalidade foi adicionada através da criação de um parâmetro, no qual deve-ser informar o diretório padrão onde o layout será salvo.

       Também foi adicionado um parâmetro antes da execução do layout, para permitir que o usuário escolha entre "Salvar o layout em um diretório local", ou  "Salvar o layout  em um diretório padrão (informado no cadastro)".

## **02. REGRA DE NEGÓCIO**

   Foi adicionado dois parâmetros no cadastro de layout gerado pelo "Gerador de Saídas", e um parâmetro antes da execução do Layout.

       Se o parâmetro “**Salvar no diretório padrão**” estiver marcado, informe o diretório onde o Layout será salvo após sua execução, esse diretório poderá ser local ou da rede. Em ambos os casos, o departamento de TI do cliente deverá garantir que: o usuário do RM.Host tenha permissão para Ler, Gravar e Modificar arquivos, e que os usuários operadores do sistema não tenham acesso ao diretório escolhido.

       Na execução do layout, o usuário tem a opção de ignorar o diretório padrão, e salvar-lo em um diretório local de sua escolha.

Observação:

Caso opte pelo diretório local, o relatório será gerado somente no diretório informado. O Layout não será salvo no diretório predefinido, mesmo que esteja parametrizado para isso. Caso o usuário deseje que o Layout seja salvo no diretório definido no cadastro, deverá executá-lo novamente sem marcar essa opção.

      Foram adicionados os seguintes campos na tabela GLayout:

* USADIRETORIOPADRAO.
* DIRETORIOPADRAO.

      No formulário de cadastro de Layouts foram incluídos os controles vinculados aos dois campos citados anteriormente, e um controle para que o usuário possa ignorar o diretório predefinido no formulário de execução do relatório.

### **Imagem demostrativa:**

No momento da geração do arquivo, a flag "Gerar arquivos no servidor" deve ser utilizada apenas para gerar arquivos em servidor, informando um caminho de rede.  
   
  
   
Sem a flag marcada o arquivo será gerado no caminho especificado da máquina, não permitindo a edição manual do caminho, para evitar erros de digitação. Então é necessário indicar o caminho clicando no botão (...) conforme imagens abaixo  
   
  
 

Observação:

Caso a opção “Salvar no diretório padrão” esteja desmarcada, o comportamento atual dos módulos não será alterado.

false

**Versão:** 11.82.XX e 12.01.XX
