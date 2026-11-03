---
content_hash: 121ad90b496b264636f96bdf9b5f3f6fce94bef6082d051da19030650fe9bd12
fetched_at: '2026-06-29T00:08:12.675844+00:00'
page_id: '243646109'
product: rm
source: tdn-rm
title: CTE0002_Parametrizar_filial_para_envio_de_CT-e
type: documentation
url: https://tdn.totvs.com/display/LRM/CTE0002_Parametrizar_filial_para_envio_de_CT-e
version: 1
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | CT-e - Conhecimento de Transporte Eletrônico |
| **Versões:** | A partir da 11.52 |
| **Ocorrência:** | Parametrizar a filial para emissão de CT-e |
| **Passo a passo:** | **Introdução:**  Este documento tem como objetivo orientar a configuração dos parâmetros da CT-e para correta emissão do Conhecimento de transporte eletrônico.  **Procedimentos:**  Acesse o RM Nucleus no seguinte menu: Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Parâmetros por filial | Edite a filial desejada.  Será aberto uma nova janela com os Parâmetros da NF-e e deverá ser configurado conforme passos abaixo.    **Etapa “Conexão NF-e”**  Campo “URL do Servidor Totvs Services:” deve ser preenchido o endereço do TSS que foi configurado na etapa de [NFE0005\_Instalacao\_e\_Configuracao\_do\_TSS](http://tdn.totvs.com/display/LRM/NFE0005_Instalacao_e_Configuracao_do_TSS) . Caso não lembre qual foi o endereço preenchido  verifique as "DICAS DE POSSÍVEIS ERROS" do link anterior.  **Etapa “CT-e”**  No campo “Ambiente de envio” deve ser selecionado Homologação (Ambiente de teste) ou Produção.  No campo “Modalidade de Operação” deve ser selecionado a modalidade que os Conhecimentos de Transporte eletrônico serão emitidas (Normal ou Contingência Offline FS-DA, Contingência SVC - RS ou Contingência SVC - SP).  Nos campos de "Versões de Layout Utilizados" deve ser informado a versão atual, atualmente é "2.00".    **Etapa “Certificação Digital 2/2”**  No campo “Tipo do Certificado Digital:” Selecione o tipo que será utilizado.  No campo “Certificado Digital:” Clique em  e Localize o arquivo do certificado Digital  No campo “Senha da Private Key:” preencha a senha do certificado.  **Observação:** Caso não tenha preparado o certificado [NFE0006\_Certificado\_Digital-Preparar\_Certificado\_Digital\_para\_Emissão\_de\_NF-e](http://tdn.totvs.com/pages/viewpage.action?pageId=233745948)    **Avance até a ultima etapa e Salve os Parâmetros.** |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
