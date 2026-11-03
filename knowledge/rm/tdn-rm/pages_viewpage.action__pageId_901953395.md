---
content_hash: 253a922ff5068f7b64246f3b0de8309e78ecac40f8397393bb37d4d4acc012b7
fetched_at: '2026-06-29T00:12:02.432376+00:00'
page_id: '901953395'
product: rm
source: tdn-rm
title: Grupo de informações da substituição (NFCom)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=901953395
version: 9
---

# gSub- Grupo de informações da substituição

Há casos em que o contribuinte necessita simplesmente trocar a NFCom ainda que válida, mas emitida com algum dado incorreto. Nesses casos, o contribuinte poderá simplesmente substituir a NFCom ou NF modelos 21 ou 22 emitida com erros por outra NFCom.  A original será cancelada e a nova NFCom tomará o seu lugar, registrando um vínculo entre a NFCom substituta e a NFCom substituída. O Grupo gSub será gerado para demonstrar que trata-se de uma operação de substituição.

# Passo a passo

Gerando a SubstituiçãoParametrização

Em um Movimento já parametrizado para emitir NFCom, habilite nos parâmetros do Tipo de Movimento, etapa “MOV – Outros Dados”, o parâmetro “Edita Movimento Relacionado”. 

Criando a substituição

Ao incluir o movimento substituto, preencha o movimento a ser substituído na pasta de identificação.

Obs. Caso este campo esteja em branco a NFCom será transmitida como uma nova NFCom e não NFCom de substituição.

# Montagem do xml

LayoutCampos

| Campo | Grupo Pai | Ocorrência | Ele | Descrição |
| --- | --- | --- | --- | --- |
| **gSub** | **[infNFCom](https://tdn.totvs.com/pages/viewpage.action?pageId=900451399)** | **0-1** | **Grupo** | **Grupo de informações da substituição** |
| chNFCom | gSub | 1-1 | Elemento de Escolha | Este campo deve ser gerado quando a substituição for de Modelo 62 por Modelo 62.  A chave de acesso deve ser gerada na NFCom Original associada ao movimento substituto. |
| **gNF** | **gSub** | **1-1** | **Grupo de Escolha** |  |
| motSub | gSub | 1-1 | Elemento | 01 – Erro de Preço; 02 – Erro Cadastral; 03 – Decisão Judicial; 04 - Erro de Tributação; 05 – Descontinuidade do Serviço |

Exemploxml
49840301763786000161620010000000011083422784

54096208000185
62
21
123123
202509
1
]]>
