---
content_hash: 27935e2794059c0e8529d26622ad6932d343ef5ab38fbae63df2e8335619e699
fetched_at: '2026-06-29T00:08:32.728404+00:00'
page_id: '273998988'
product: rm
source: tdn-rm
title: NFCE0003_Parametrizar_Filial_para_emissao_de_NFC-e
type: documentation
url: https://tdn.totvs.com/display/LRM/NFCE0003_Parametrizar_Filial_para_emissao_de_NFC-e
version: 1
---

|  |  |
| --- | --- |
| **Produto:** | NFC-e - Nota Fiscal do Consumidor Eletrônica |
| **Versões:** | A partir da 12.1.7 |
| **Ocorrência:** | Parametrizar Filial para emissão de NFC-e |
| **Passo a passo:** | **Introdução:**  Este documento tem como objetivo orientar a configuração dos parâmetros da NFC-e para correta emissão.  **Procedimentos:**  Acesse o RM Nucleus no seguinte menu: Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento  | Integrações | Fiscal.  **Na etapa “Classificação IBGE Município”**  Selecione a Tabela de classificação IBGE dos municípios conforme imagem abaixo.          **Na etapa “Classificação País BACEN”**  Selecione a Tabela de classificação BACEN dos Países conforme imagem abaixo.          **Na etapa “Parâmetros por Filial”**  Marque a Filial que será parametrizada e clique no botão Parametrizar conforme imagem abaixo.        Será aberto uma nova janela com os Parâmetros da NF-e e deverá ser configurado conforme passos abaixo.  **Etapa “Conexão NF-e”**  Campo “URL do Servidor Totvs Services:” deve ser preenchido o endereço do TSS que foi configurado na etapa de [NF-e - Instalação e Configuração do TSS](http://tdn.totvs.com.br/pages/viewpage.action?pageId=64652506) . Caso não lembre qual foi o endereço preenchido  verifique as "DICAS DE POSSÍVEIS ERROS" do link anterior.       **IMPORTANTE:**  os campos referentes ao grupo de NFS-e Municipal (Modelo Nacional) não são de preenchimento obrigatório. Deveram ser preenchidos somente para o envio de NFS-e (Nota Fiscal de Serviço).    **Etapa “Certificação Digital 1/2”**  No campo “Tipo do Certificado Digital:” Selecione o tipo que será utilizado.  No campo “Certificado Digital:” Clique em  e Localize o arquivo do certificado Digital  No campo “Senha da Private Key:” preencha a senha do certificado.  **Observação:** Caso não tenha preparado o certificado [NFE0003\_Certificado Digital - Preparar Certificado Digital para Emissão de NF-e](http://tdn.totvs.com/display/LRM/NFE0006_Preparar_Certificado_Digital).           **Etapa “Ambiente NFC-e”**  No Campo “Ambiente de envio” deve ser selecionado Homologação (Ambiente de teste) ou Produção.  No Campo "Versão do Layout da NFC-e" colocar a versão do layout atual utilizada pela SEFAZ.  No Campo "URL do QRCODE" colocar a URL fornecida pela SEFAZ do Estado.  No Campo "URL da SEFAZ para Consulta da NFC-e" colocar a URL fornecida pela SEFAZ do Estado.  No Campo "Código de Segurança" colocar o código de segurança fornecido pela SEFAZ do Estado.  No Campo "ID do Código de Segurança" colocar o ID fornecido pela SEFAZ do Estado. |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
