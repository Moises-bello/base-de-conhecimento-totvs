---
content_hash: f7d3dfe7a148c8193f292e687c2f270b53066d1cdc79d12c6aeb18b849feec5d
fetched_at: '2026-06-29T00:11:13.463572+00:00'
page_id: '66126298'
product: rm
source: tdn-rm
title: NFS-e - Configurar os Parâmetros da filial para correta emissão de NFS-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=66126298
version: 2
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | NFS-e                        **Versão:***apartir 11.40* |
| **Processo** | **:** | Configurar os Parâmetros da filial para correta emissão de NFS-e |
| **Subprocesso** | **:** | Configurar os Parâmetros da filial para correta emissão de NFS-e |
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

Será aberto uma nova janela com os Parâmetros da NFS-e e deverá ser configurado conforme passos abaixo.

**Etapa “Conexão NF-e”**

Campo “URL do Servidor Totvs Services:” deve ser preenchido o endereço do TSS que foi configurado na etapa de [NF-e - Instalação e Configuração do TSS](http://tdn.totvs.com.br/pages/viewpage.action?pageId=64652506) . Caso não lembre qual foi o endereço preenchido  verifique as "DICAS DE POSSÍVEIS ERROS" do link anterior.

**Etapa “Ambiente de envio”**

No Campo “Ambiente de envio” deve ser selecionado Homologação (Ambiente de teste) ou Produção.

No campo “Classificação Município” deve ser selecionada a tabela de classificação de município, esta tabela varia de acordo com cada município. Os Municípios Belém, Campinas, Campo Grande, Teresina, Uberlândia, São Luís e Sorocaba utilizam a tabela de Classificação SIAFI os demais municípios utilizam a tabela IBGE

**Etapa “Certificação Digital 1/2”**

No campo “Tipo do Certificado Digital:” Selecione o tipo que será utilizado.

No campo “Certificado Digital:” Clique em  e Localize o arquivo do certificado Digital

No campo “Senha da Private Key:” preencha a senha do certificado.

**Observação:** Caso não tenha preparado o certificado [Certificado Digital - Preparar Certificado Digital para Emissão de NF-E](http://tdn.totvs.com.br/pages/viewpage.action?pageId=65208525).

**Avance até a ultima etapa e Salve os Parâmetros.**

****Para maiores informações:****

**[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)**

**COMUNIDADE **R**[@](https://totvs.byyou.com/?space=rnfe)Nfe**

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções: 2 – (Software), 2 – (Suporte Técnico), 3 - (RM), 3 - (Fiscal), 3 - (Nota Fiscal Eletrônica)
