---
content_hash: 6bbb4e21454b8f4f9d921431b7711b0fac63ab09854667c64cbaa5d886087172
fetched_at: '2026-06-29T00:05:57.206075+00:00'
page_id: '165283342'
product: rm
source: tdn-rm
title: MD-e - Configurar os Parâmetros da filial para emissão de MD-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=165283342
version: 2
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | MD-e                        **Versão:***a partir 11.52* |
| **Processo** | **:** | Configurar os Parâmetros da filial para emissão de MD-e |
| **Subprocesso** | **:** | Configurar os Parâmetros da filial para emissão de MD-e |
| **Data da publicação** | **:** | 03/10/2014 |

**Introdução:**

Este documento tem como objetivo orientar a configuração dos parâmetros da MD-e para correta emissão do Manifesto do Destinatário eletrônico.

**Procedimentos:**

Acesse o RM Nucleus no seguinte menu: Opções | Parâmetros | RMNucleus | Integrações | Fiscal.

Para acesso na MDI, siga o seguinte caminho: Ambiente | Parametros | Gestão de Estoque, Compras e Faturamento.

**Na etapa “Parâmetros por Filial”**

Marque a Filial que será parametrizada e clique no botão Parametrizar.

Será aberto uma nova janela com os Parâmetros da NF-e e deverá ser configurado conforme passos abaixo.

**Etapa “Conexão NF-e”**

Campo “URL do Servidor Totvs Services:” deve ser preenchido o endereço do TSS que foi configurado na etapa de [NF-e - Instalação e Configuração do TSS](http://tdn.totvs.com.br/pages/viewpage.action?pageId=64652506) . Caso não lembre qual foi o endereço preenchido  verifique as "DICAS DE POSSÍVEIS ERROS" do link anterior.

**Etapa “Manifestos Destinatário”**

No campo “Manifestação Destinatário” deve ser selecionado Homologação (Ambiente de teste) ou Produção.

No campo de "Versão de Sincronização de Documentos" deve ser informado a versão atual, atualmente é "1.01".

**Etapa “Certificação Digital 2/2”**

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
