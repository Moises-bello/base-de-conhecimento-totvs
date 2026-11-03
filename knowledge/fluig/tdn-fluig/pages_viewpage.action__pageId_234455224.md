---
content_hash: 605a36de7d515f0f283cdc171d68d4ab5a2cb19ec2df5da9d163c89482d688c3
fetched_at: '2026-06-28T21:35:21.495626+00:00'
page_id: '234455224'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Adapters
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=234455224
version: 20
---

.\*ndice

# Falando de *adapters*...

---

Os *adapters* são componentes JAVA responsáveis pela comunicação da plataforma com o a ser executado. Os aplicativos podem usar *adapters* padrões, que serão liberados na plataforma e terão o processo de suporte normalmente ou poderão ser *adapters* desenvolvidos sob demanda para aplicativos variados.

O TOTVS Fluig disponibiliza dois *adapters* padrões:

* **CommandLine**: o qual permite a utilização de qualquer aplicativo via linha de comando. Esse *adapter* possui o parâmetro padrão “WORKDIR”, que tem a mesma função do “Iniciar em” nos atalhos do Windows.

* **Web**: o qual permite a utilização de aplicativos Web. Esse *adapter* possui o parâmetro padrão “TARGET”, o qual permite definir a janela na qual a página será aberta.

Os produtos Datasul EMS2, EMS5 e HCM disponibilizam um *adapter* para comunicação com a plataforma Fluig, permitindo acessá-los por intermédio da plataforma.

É importante saber que os *adapters* que acessam diretamente os produtos Datasul (EMS/HCM), possuem a característica de realizar o controle e gerenciamento das sessões do produto, evitando o consumo de licenças sem necessidade.

Quando o acesso aos produtos Datasul é por intermédio da plataforma, é necessário que o Progress esteja instalado na máquina local.

Importante!

Devido a necessidade de execução de applets, este recurso não tem seu funcionamento como esperado. Os applets são uma tecnologia depreciada e por este motivo foram descontinuados pelos navegadores no geral.

## Ver *adapters*

---

**01.** No menu principal, clique em  **Painel de controle**.

**02**. Localize o agrupador **Desenvolvimento**.

**03**. Clique em  ***Adapters***.

**04.** Veja os *adapters* existentes.

## Adicionar *adapter*

---

**01.** No menu principal, clique em  **Painel de controle**.

**02**. Localize o agrupador **Desenvolvimento**.

**03**. Clique em  ***Adapters***.

**04.** Clique em **Adicionar**.

**05.** Insira o código do *adapter* que deseja incluir.

**06.** Insira a descrição do *adapter* que deseja incluir.

**07.** Insira o endereço onde se encontra o arquivo JAR.

**08.** Clique em **Salvar**.

## Editar *adapter*

---

**01.** No menu principal, clique em  **Painel de controle**.

**02**. Localize o agrupador **Desenvolvimento**.

**03**. Clique em  ***Adapters***.

**04.** Selecione o *adapter* que deseja editar.

**05.** Clique em **Editar**.

**06.** Efetue as alterações desejadas.

#f2f2f2#f2f2f2Não é permitido editar o código do *adapter*.

**07.** Clique em **Salvar**.

## Excluir *adapter*

---

**01.** No menu principal, clique em  **Painel de controle**.

**02**. Localize o agrupador **Desenvolvimento**.

**03**. Clique em  ***Adapters***.

**04.** Selecione o *adapter* que deseja excluir.

**05.** Clique em **Remover**.

Fique atento!

Esta documentação é válida a partir da atualização **Voyager (2.0)**. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê na sua plataforma.
