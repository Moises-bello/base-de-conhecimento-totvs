---
content_hash: 60ffe4fe2df815733e807711e426cd90be2f6657ef67c3ffd073c6688fd289eb
fetched_at: '2026-06-28T21:35:17.481468+00:00'
page_id: '1070042085'
product: fluig
source: tdn-fluig
title: Primeiros passos no desenvolvimento TOTVS Fluig
type: documentation
url: https://tdn.totvs.com/display/fluig/Primeiros+passos+no+desenvolvimento+TOTVS+Fluig
version: 8
---

# Introdução

---

Bem-vindo ao Getting Started para Desenvolvimento Fluig.

Este guia prático é direcionado a profissionais que já possuem familiaridade com as tecnologias e linguagens presentes na plataforma TOTVS Fluig.

O foco deste documento é o desenvolvimento de um workflow completo para o lançamento de ausências, abordando os seguintes recursos essenciais:

* Criação e configuração de **formulários** (incluindo campos zoom e estrutura Pai x Filho).
* Configuração de **workflows** (criação de diagramas, mecanismos de atribuição e regras de anexos).
* Desenvolvimento e consumo de **datasets** (criação de datasets internos e avançados e seu consumo no formulário).

# Pré-requisitos do ambiente

---

Antes de iniciar a criação do workflow e seus componentes, certifique-se de que sua máquina atende aos requisitos técnicos abaixo. Estes componentes são essenciais para que o desenvolvimento e a comunicação com o TOTVS Fluig ocorram sem falhas.

## Kit de desenvolvimento Java (JDK)

**O que é:** ferramenta necessária para compilar e desenvolver código Java.

Atenção!

Certifique-se de instalar o **JDK da Oracle**. É obrigatório ter o JDK completo e não apenas o JRE, visto que o JRE serve exclusivamente para executar os programas, e não para criá-los.

## IDE Eclipse e plugin /Fluig Studio

Para desenvolver para a plataforma, utilizamos o Eclipse com ferramenta específica da TOTVS.

* **Versões suportadas:** é necessário utilizar o **Eclipse 2019-R9 (2019-09)** ou o **Eclipse Luna**, pois atualmente são as únicas versões homologadas pela TOTVS.
* **Extensão:** o *plugin* **Fluig Studio** deve estar instalado e configurado. É fundamental garantir que o *plugin* esteja exatamente na mesma versão do servidor Fluig do seu ambiente.

Caso haja divergência entre a versão do seu *plugin* e a do servidor, consulte as documentações abaixo para realizar o *downgrade* ou *upgrade* de versão do *plugin*.

Dica!

Consulte o [Guia de instalação Fluig Studio](https://tdn.totvs.com/pages/viewpage.action?pageId=73078179) e [Como fazer - Instalar Eclipse 2019-R9 + Fluig Studio](https://academy.fluig.com/theme/totvs_fluig_academy/landpage.php?course=95) para o passo a passo detalhado.

Para a boa utilização do Fluig Studio, algumas configurações são necessárias [Configuração para uso inicial do Fluig Studio](https://tdn.totvs.com/pages/viewpage.action?pageId=172297237).

Atenção!

O Eclipse Luna não é compatível com a atualização **Voyager 2.0** do Fluig.

# Configuração do servidor e criação do projeto

---

Para iniciar o desenvolvimento no TOTVS Fluig, o primeiro passo prático é configurar a comunicação com o seu ambiente e criar um projeto no Eclipse para organizar os seus arquivos. Consulte a documentação [Criando um projeto Fluig no Studio](https://tdn.totvs.com/x/UhgSCw) que contém o passo a passo detalhado.

configurando\_eclipsetrue1Passo 1: Selecionar Perspectiva Fluig

* Certifique-se de que a **Perspectiva Fluig** está ativa. Para isso, verifique se o ícone da plataforma está selecionado no canto superior direito do Eclipse, o que habilitará os menus específicos do Fluig.

2Passo 2: Configurar o servidor (Fluig Server)

* Aqui é necessário apontar para qual servidor do Fluig iremos importar e exportar arquivos:  
    
  + Procure a aba **Servers**. Caso não encontre, vá em **Window ⟶ Show View ⟶ Other... ⟶ Fluig ⟶ Fluig Servers**.
  + Clique com botão direito do mouse sobre **Servers ⟶** **Novo ⟶** **Fluig Server**.

3Passo 3: Autenticação e definição

* Na tela exibida, insira as credenciais essenciais para o "*deploy*":  
    
  + **Nome servidor:** um nome para identificar o servidor. **Ex**.: "Servidor Produção".
  + ***Host*****:** o endereço completo. Ex.: [http://lab.fluig.com](https://lab.fluig.com/).
  + **Usuário e Senha**: devem ser de um usuário com perfil de **Administrador** no TOTVS Fluig.
  + Clique em***Finish*** para concluir a criação do servidor.

Dica!

Em ambientes integrados com Identity, utilize as credenciais de login do Identity.

4Passo 4: Teste de conexão

* Clique **duas vezes** no servidor para validar a configuração.

5Passo 5: Criando o projeto

* O projeto funciona como uma pasta raiz que conterá todos os seus componentes: *formulários, diagramas, datasets, mecanismos customizados.*
  + Clique em ***Arquivo ⟶** **Novo ⟶****Projeto Fluig**.*

---

* **Na caixa de dialogo exibida,** digite o nome do seu projeto. Ex.: Getting Started - LANCAMENTO DE AUSENCIA, fluig, etc.
  + Em seguida, clique em **Concluir**.

Importante!

Após o Eclipse criar a estrutura de pastas, trabalharemos especificamente com três delas: **datasets**, **forms** e **workflow**.

# Criando e configurando formulários

---

Antes de entender mais sobre o formulário Fluig, precisamos criar a estrutura básica necessária.

criando-form1Passo1: Novo formulário

* Ao analisarmos o projeto criado anteriormente, precisamos encontrar a pasta **forms.**
* Clique com botão direito do mouse e siga o caminho **New ⟶ Formulário**.

2Passo 2: Nomeie o formulário

* Dê um nome ao formulário e clique em **Finish**. Em seguida uma pasta e o respectivo formulário serão criados.

Dica!

As próximas etapas utilizarão padrões definidos conforme o [Fluig Style Guide](https://style.fluig.com/). O Fluig Style Guide é o framework frontend oficial da plataforma TOTVS Fluig, utilizado para criar interfaces consistentes, responsivas e amigáveis. Ele fornece componentes visuais (botões, tabelas, formulários) e diretrizes de design baseados em HTML, CSS e Javascript, garantindo que aplicações personalizadas sigam o mesmo padrão visual.

* Abaixo é possível ver o HTML do formulário que utilizamos neste projeto, bem como a lista de recursos utilizados na sequência.

xmlformLancaAusencia.htmltrue


# Formulário de Ausências



**ATENÇÃO!** Analise os dados abaixo e clique no botão **ENVIAR** para selecionar como deseja seguir com a solicitação.

**Dados do Solicitante**

Nome do Solicitante:

Unidade:

Tipo da Ausência:

CEP:

Cidade:

Estado:

**Dados da Ausência**

## Regras de Anexo

Obrigatório anexar o atestado médico para continuação no processo. Utilize o botão abaixo para selecionar um arquivo ou tirar foto do documento.

Data de Início da Ausência:

Data de Fim da Ausência:

Anexar Documentos

| Código CID | Descrição |
| --- | --- |
|  |  |

Observações:

**Gestor**

Observações do Gestor:

**RH - Validação**

Observações do RH:
