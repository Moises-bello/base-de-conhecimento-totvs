---
content_hash: 9a3a4d5528f9deda86211f905b5bb1fc22e2d1c1efbc94f41a4b2f2502dda631
fetched_at: '2026-06-29T00:08:12.633744+00:00'
page_id: '243645102'
product: rm
source: tdn-rm
title: NFSE0002_Parametrizar_filial_para_emissao_de_NFS-e_(municipal)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243645102
version: 1
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | NFS-e - Nota Fiscal de Serviço Eletrônica (Municipal) |
| **Versões:** | A partir da 11.52 |
| **Ocorrência:** | Configurar os Parâmetros da filial para emissão de NFS-e |
| **Passo a passo:** | **Introdução:**  Este documento tem como objetivo orientar a configuração dos parâmetros da NF-e para correta emissão da Nota fiscal eletrônica.  **Procedimentos:**  Acesse o RM Nucleus no seguinte menu: Acesse o RM Nucleus no seguinte menu: Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento  | Integrações | Fiscal.  **Na etapa “Classificação IBGE Município”**  Selecione a Tabela de classificação IBGE dos municípios conforme imagem abaixo.    **Na etapa “Classificação País BACEN”**  Selecione a Tabela de classificação BACEN dos Países conforme imagem abaixo.    **Na etapa “Configurações Proxy Server”**  Preencha os campos de Proxy conforme necessidade da empresa (Consulte o TI da empresa para saber esta necessidade, os campos deverão ser preenchido se Proxy controlar o acesso do Nucleus com o TSS).  **Na etapa “Parâmetros por Filial”**  Marque a Filial que será parametrizada e clique no botão Parametrizar conforme imagem abaixo.  Será aberto uma nova janela com os Parâmetros da NFS-e e deverá ser configurado conforme passos abaixo.    **Etapa “Conexão NF-e”**  Campo “URL do Servidor Totvs Services:” deve ser preenchido o endereço do TSS que foi configurado na etapa de  . Caso não lembre qual foi o endereço preenchido  verifique as "DICAS DE POSSÍVEIS ERROS" do link anterior.  **Etapa “Ambiente de envio”**  No Campo “Ambiente de envio” deve ser selecionado Homologação (Ambiente de teste) ou Produção.  No campo “Classificação Município” deve ser selecionada a tabela de classificação de município, esta tabela varia de acordo com cada município. Os Municípios Belém, Campinas, Campo Grande, Teresina, Uberlândia, São Luís e Sorocaba utilizam a tabela de Classificação SIAFI os demais municípios utilizam a tabela IBGE    **Etapa “Certificação Digital 1/2”**  No campo “Tipo do Certificado Digital:” Selecione o tipo que será utilizado.  No campo “Certificado Digital:” Clique em  e Localize o arquivo do certificado Digital  No campo “Senha da Private Key:” preencha a senha do certificado.  **Observação:** Caso não tenha preparado o certificado     **Avance até a ultima etapa e Salve os Parâmetros.** |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
