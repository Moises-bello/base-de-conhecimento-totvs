---
content_hash: 614312d1862b8c11f0ed7a5b80eeaa67302fa3f2fe01d145a674411e9482ecfb
fetched_at: '2026-06-28T21:35:28.859826+00:00'
page_id: '699193954'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Importar processo com imagem no Fluig utilizando APIs
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=699193954
version: 22
---

4.\*ndice

# Objetivo

---

O objetivo deste guia é demonstrar as formas de importar um processo, utilizando APIs, para que o Fluig exiba corretamente a imagem do fluxo do processo.

# Falando da imagem do processo no Fluig

---

A imagem do fluxo do processo que é exibida na movimentação de solicitações não é gerada pelo *back-end* do Fluig. Os modeladores web e do Fluig Studio, ao liberarem uma nova versão do processo enviam também a imagem no formato SVG (*Scalable Vector Graphics*).

Caso a importação de um processo seja realizado sem o envio da imagem, o Fluig exibirá a mensagem “*Não foi possível exibir o fluxo do processo*” na página de movimentação de processos.

# Pré-requisitos

---

Para executar os passos desse guia, é necessário:

* O Fluig Plataforma deve estar na atualização 1.7.0-200608 ou superior;

* Ter o [Fluig Studio instalado](https://tdn.totvs.com/pages/viewpage.action?pageId=73078179);

* Ser um usuário administrador;

* Obter o arquivo XML do processo;

* Obter o arquivo SVG com o fluxo do processo.

# Obtendo o arquivo XML  e o SVG do processo

---

O XML e a imagem SVG do processo ficam disponíveis na pasta “\workflow\.resources”, na workspace do Fluig Studio. Para que a imagem SVG seja gerada automaticamente a cada alteração no processo, é necessário alterar as configurações do Fluig Studio. Para isso, siga os passos a seguir:

Passo 1Passo 1

* Acesse **Window**, em seguida clique na opção **Preferences**:

Passo 2

* Localize o agrupador **Fluig,** expanda as configurações de salvamento e clique em **Save**:

Passo 3

* Após concluir o passo 2, marque a opção **Automaticamente salvar para o formato SVG quando salvar o diagrama**:

Passo 4

* Reinicie o Fluig Studio.
Passo 5

* Após reiniciar o Fluig Studio, ao alterar e salvar um processo no mesmo, o arquivo SVG estará disponível na pasta **.resources**, além do arquivo XML:

# Enviando o fluxo do processo no caso da API pública

---

A imagem do fluxo do processo pode ser enviada de duas formas utilizando API REST:

* enviar o SVG separadamente, após importação do processo (**recomendado**);

* adicionar o SVG no XML do processo (**avançado**).

Observe abaixo os passos para cada uma delas.

## Enviar o SVG separadamente (recomendado)

---

Esse método é mais simples e não requer manipulação do arquivo XML do processo. Para isso siga os passos a seguir:

**01.** Efetue a importação do processo utilizando a API [/v2/processes/import/xml](https://api.fluig.com/latest/process-management/swagger-ui/#/Processes/importNewProcess), informando corretamente os parâmetros necessários segundo o Swagger.

**02.** Após a importação com sucesso do processo desejado, envie a imagem SVG utilizando a API [/v2/processes/{processId}/process-versions/{processVersion}/diagram](https://api.fluig.com/latest/process-management/swagger-ui/#/Processes/updateProcessVersionSVG) seguindo os parâmetros detalhados no Swagger.

## Adicionar o SVG no XML do processo (avançado)

---

Nesse método, é necessário incluir o conteúdo do arquivo SVG do fluxo no XML do processo. Para isso siga os passos a seguir:

**01.** Abra o arquivo XML do processo no editor de texto de sua preferência.

**02.** Antes do fechamento da tag “ProcessDefinitionVersion”, inclua a tag “processDiagram”:

#f2f2f2#f2f2f2

trueExemplo

]]>

**03.** Na tag “processDiagram” deve ser informado o conteúdo do arquivo SVG. Para isso, basta abrir o arquivo SVG no editor de texto de sua preferência e copiar todo o conteúdo. 

#f2f2f2#f2f2f2

trueExemplo

<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" style="s
...
</svg>
 
]]>Importante!

Ao utilizar esse método são necessários alguns cuidados:

* realizar o [processo de escape](https://pt.wikipedia.org/wiki/Caractere_de_escape) do conteúdo do arquivo SVG antes de incluir na tag “processDiagram” do XML do processo;

* após a inclusão da tag, garantir que o arquivo XML é um XML válido (evitar tags abertas, XML mal formado, etc);

* no editor de texto utilizado, verificar se a codificação está configurada para UTF-8. Caso seja utilizada outra codificação, o processo importado não exibirá corretamente caracteres especiais, por exemplo, acentuação, etc.

# No SOAP

---

No SOAP /webdesk/ECMWorkflowEngineService?wsdl, pode ser usado um dos métodos **importProcess** (seja somente o processo ou com formulário) informando a imagem no formato SVG na tag *attachments*, marcando como anexo e como não principal.

trueExemplo

true
false
svgaqui
]]>Importante!

O conteúdo do arquivo SVG deve ser enviado em **bytes**.

# Gerar a imagem pelo Painel de controle

---

Essa é a forma mais simples, porém, é limitada à processos que também possam ser editados pela web. É recomendada para processos antigos ou que foram migrados a partir do TOTVS ECM 3.0.

https://tdn.totvs.com/download/attachments/699193954/Gerador%20de%20imagem%20de%20processo.gif?version=2&modificationDate=1658339131037&api=v2truevideo-filledAssista ao vídeo#0897E9INLINE

**01.** No menu principal, clique em  **Painel de controle**.

**02**. Localize o agrupador **Parâmetros técnicos**.

**03**. Clique em  **Gerador de imagem de processo**.

**04.** Clique em **Gerar diagramas** para gerar a imagem do processo para solicitações em aberto que ainda não a possuem.

**05.** Na mensagem exibida, clique em **Ok**.

#f2f2f2#f2f2f2

Acesse nossa documentação e saiba mais sobre o recurso [Gerador de imagem de processo](https://tdn.totvs.com/x/Xyg-Dg) no TOTVS Fluig.

Esta documentação é válida a partir da atualização **Voyager (2.0)**. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê na sua plataforma.
