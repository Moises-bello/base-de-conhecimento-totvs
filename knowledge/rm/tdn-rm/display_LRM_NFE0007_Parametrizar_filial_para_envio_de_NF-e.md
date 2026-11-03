---
content_hash: 07dd3a7552501284652267142cd736ec4d1dba3e75838fee718a1bcc15932019
fetched_at: '2026-06-29T00:08:10.059512+00:00'
page_id: '240300900'
product: rm
source: tdn-rm
title: NFE0007_Parametrizar_filial_para_envio_de_NF-e
type: documentation
url: https://tdn.totvs.com/display/LRM/NFE0007_Parametrizar_filial_para_envio_de_NF-e
version: 3
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | NF-e - Nota Fiscal Eletrônica |
| **Versões:** | A partir da 11.52 |
| **Ocorrência:** | Configurar os Parâmetros da filial para emissão de NF-e |
| **Passo a passo:** | **Introdução:**  Este documento tem como objetivo orientar a configuração dos parâmetros da NF-e para correta emissão da Nota fiscal eletrônica.  **Procedimentos:**  Acesse o RM Nucleus no seguinte menu: Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento  | Integrações | Fiscal.  **Na etapa “Classificação IBGE Município”**  Selecione a Tabela de classificação IBGE dos municípios conforme imagem abaixo.      **Na etapa “Classificação País BACEN”**  Selecione a Tabela de classificação BACEN dos Países conforme imagem abaixo.      **Na etapa “Configurações Proxy Server”**  Preencha os campos de Proxy conforme necessidade da empresa (Consulte o TI da empresa para saber esta necessidade, os campos deverão ser preenchido se Proxy controlar o acesso do Nucleus com o TSS).  **Na etapa “Parâmetros por Filial”**  Marque a Filial que será parametrizada e clique no botão Parametrizar conforme imagem abaixo.  Será aberto uma nova janela com os Parâmetros da NF-e e deverá ser configurado conforme passos abaixo.      **Etapa “Conexão NF-e”**  Campo “URL do Servidor Totvs Services:” deve ser preenchido o endereço do TSS que foi configurado na etapa de [NF-e - Instalação e Configuração do TSS](http://tdn.totvs.com.br/pages/viewpage.action?pageId=64652506) . Caso não lembre qual foi o endereço preenchido  verifique as "DICAS DE POSSÍVEIS ERROS" do link anterior.  **IMPORTANTE:**  os campos referentes ao grupo de NFS-e Municipal (Modelo Nacional) não são de preenchimento obrigatório. Deveram ser preenchidos somente para o envio de NFS-e (Nota Fiscal de Serviço).  **Etapa “Ambiente NF-e”**  No Campo “Ambiente de envio” deve ser selecionado Homologação (Ambiente de teste) ou Produção.  No campo “Modalidade de Operação” deve ser selecionado a modalidade que as notas serão emitidas (Normal, Contingência, DPEC, SCAN etc.).  Na tela de envio das notas esta modalidade pode ser alterada, pode este motivo sugerimos que seja selecionado a opção “Normal”.  No campo “Tempo de espera p/entrar em contingência (seg):” deve ser informado “0”.      **Etapa “Certificação Digital 1/2”**  No campo “Tipo do Certificado Digital:” Selecione o tipo que será utilizado.  No campo “Certificado Digital:” Clique em  e Localize o arquivo do certificado Digital  No campo “Senha da Private Key:” preencha a senha do certificado.  **Observação:** Caso não tenha preparado o certificado . |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
