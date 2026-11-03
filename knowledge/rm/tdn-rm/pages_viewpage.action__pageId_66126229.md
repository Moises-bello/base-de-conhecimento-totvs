---
content_hash: 1cfd2b7411d3b4a9596bee5e18e3f84a1e807a081bd916ec6349df1680ea1be8
fetched_at: '2026-06-29T00:11:13.444521+00:00'
page_id: '66126229'
product: rm
source: tdn-rm
title: NF-e - Parâmetrizar a filial para correta emissão de NF-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=66126229
version: 5
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | NF-e                        **Versão:***apartir 11.40* |
| **Processo** | **:** | Configurar os Parâmetros da filial para correta emissão de NF-e |
| **Subprocesso** | **:** | Configurar os Parâmetros da filial para correta emissão de NF-e |
| **Data da publicação** | **:** | 09/07/2013 |

**Introdução:**

Este documento tem como objetivo orientar a configuração dos parâmetros da NF-e para correta emissão da Nota fiscal eletrônica.

**Procedimentos:**

Acesse o RM Nucleus no seguinte menu: Opções | Parâmetros | RMNucleus | Integrações | Fiscal.

**Na etapa “Classificação IBGE Município”**

Selecione a Tabela de classificação IBGE dos municípios conforme imagem abaixo.

**Na etapa “Classificação País BACEN”**

Selecione a Tabela de classificação BACEN dos Países conforme imagem abaixo.

**Na etapa “Configurações Proxy Server”**

Preencha os campos de Proxy conforme necessidade da empresa (Consulte o TI da empresa para saber esta necessidade, os campos deverão ser preenchido se Proxy controlar o acesso do Nucleus com o TSS).

**Na etapa “Parâmetros por Filial”**

Marque a Filial que será parametrizada e clique no botão Parametrizar conforme imagem abaixo.

Será aberto uma nova janela com os Parâmetros da NF-e e deverá ser configurado conforme passos abaixo.

**Etapa “Conexão NF-e”**

Campo “URL do Servidor Totvs Services:” deve ser preenchido o endereço do TSS que foi configurado na etapa de  . Caso não lembre qual foi o endereço preenchido  verifique as "DICAS DE POSSÍVEIS ERROS" do link anterior.

Campo Versão do Layout de NFS-e Utilizado: informe o layout utilizado pela prefeitura no município de envio da NFS-e.

Campos "Login da Prefeitura","Senha da Prefeitura" e "Autorização da prefeitura" devem ser preenchidos somente quando a prefeitura não utilizar certificado digital.

**IMPORTANTE:**  o campo "Autorização da Prefeitura" não é de preenchimento obrigatório.

**Etapa “Ambiente NF-e”**

No Campo “Ambiente de envio” deve ser selecionado Homologação (Ambiente de teste) ou Produção.

No campo “Modalidade de Operação” deve ser selecionado a modalidade que as notas serão emitidas (Normal, Contingência, DPEC, SCAN etc.).

Na tela de envio das notas esta modalidade pode ser alterada, pode este motivo sugerimos que seja selecionado a opção “Normal”.

No campo “Tempo de espera p/entrar em contingência (seg):” deve ser informado “0”.

**Etapa “Certificação Digital 1/2”**

No campo “Tipo do Certificado Digital:” Selecione o tipo que será utilizado.

No campo “Certificado Digital:” Clique em  e Localize o arquivo do certificado Digital

No campo “Senha da Private Key:” preencha a senha do certificado.

**Observação:** Caso não tenha preparado o certificado .

**IMPORTANTE:** Caso o município (prefeitura), não utilize certificado digital, os campos "Login da Prefeitura" e"Senha da Prefeitura"  devem ser preenchidos na aba "Conexão NF-e".

**Avance até a ultima etapa e Salve os Parâmetros.**

****Para maiores informações:****

**[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)**

**COMUNIDADE **R**[@](https://totvs.byyou.com/?space=rnfe)Nfe**

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções: 2 – (Software), 2 – (Suporte Técnico), 3 - (RM), 3 - (Fiscal), 3 - (Nota Fiscal Eletrônica)
