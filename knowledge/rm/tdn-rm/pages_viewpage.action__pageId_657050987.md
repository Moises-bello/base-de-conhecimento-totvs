---
content_hash: 3b81f9ff284a8d7fe9500cad0eb615cf275b2269fd1939d92c553e689fd538f4
fetched_at: '2026-06-29T00:11:13.160546+00:00'
page_id: '657050987'
product: rm
source: tdn-rm
title: '"Executar Código Fonte" em ambientes SmartClient / 3 Camadas'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=657050987
version: 4
---

# Introdução

---

          Neste documento estarão explícitas as informações necessárias para realizar edições na atividade ***Executar Código Fonte*** em ambientes SmartClient / 3 Camadas.

Importante

A partir da versão 12.1.31 (e superiores), é possível realizar alterações em códigos-fonte diretamente pelo RM em ambientes SmartClient ou 3 camadas (Client). Para versões anteriores, acesse a documentação: [Exportação e Importação de Códigos Fontes](https://tdn.totvs.com/x/nUOlGQ), para compreender as limitações e informações importantes.

         Para maiores detalhes da criação e acesso a fórmulas visuais, acesse a documentação

# Especificação:

---

     A atividade “Executar Código Fonte” necessita de arquivos presentes apenas na camada Server. Por esse motivo, era possível editá-la apenas em ambientes Server, por possuírem esses arquivos, porém, agora, mesmo **SmartClient** ou camada **Client** (**3 camadas**) são capazes de editar código-fonte clicando no botão **Editor C#**, tal qual demonstrado abaixo:

Importante

**Lembre-se:**O código-fonte só é gerado ao clicar no botão Editor C#. Caso salve sem clicar em **Editor C#**, e tente exportar o código-fonte, o arquivo virá vazio, pois não houve a geração de código-fonte automaticamente.

Porém é valido frisar que existem algumas limitações. A compilação do código-fonte só passível de ser feita dentro do ambiente Server então, por exemplo, caso seja acionado o botão **Build** dentro do editor, é possível que sejam exibidos erros de referência, tal qual demonstrado abaixo:

Os erros acima acontecem em ambientes SmartClient por não possuir os arquivos (DLL) necessários para a compilação daquele código-fonte. Dessa forma, para conseguir compilar este código-fonte corretamente, siga as informações abaixo:

falseExemploFVExemploFVPasso 01

Após realizar as implementações desejadas no código-fonte, clique em OK. É possível que o aviso abaixo apareça:

Este aviso aparece pelo fato de o Editor C# não ser capaz de sozinho, compilar o código-fonte em questão. Clique em **Sim**

ExemploFVPasso 02

Após seguir os passos para seleção do Código-Fonte, acesse o botão **Salvar e Executar** na Fórmula Visual:

Neste momento, o código-fonte será enviado à camada Server, compilado e executado corretamente, tal qual demonstrado abaixo:

Aviso

Os erros referentes aos arquivos DLL já presentes na camada Server do RM são suportados pela compilação tal qual demonstrado acima, porém erros de referência em DLL's terceiras não são cobertas por essa funcionalidade.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.31 ou Superior

false

**Processo:** Atividade "Executar Código Fonte" da Fórmula Visual

falsefalse

**Status:** **Finalizado**

false

**Data:** 23/12/2021

false

**Autores:**

false
