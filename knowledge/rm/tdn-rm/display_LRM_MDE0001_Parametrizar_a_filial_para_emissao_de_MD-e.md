---
content_hash: ac7240aa6e2da54103bf4f3f89ec2c624b3089616d32056f715f986f2e1c2c43
fetched_at: '2026-06-29T00:08:16.368961+00:00'
page_id: '244940143'
product: rm
source: tdn-rm
title: MDE0001_Parametrizar_a_filial_para_emissao_de_MD-e
type: documentation
url: https://tdn.totvs.com/display/LRM/MDE0001_Parametrizar_a_filial_para_emissao_de_MD-e
version: 1
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | MD-e - Manifestação do Destinatário Eletrônica |
| **Versões:** | a partir da versão 11.82 |
| **Ocorrência:** | Parâmetros a filial para emissão de MD-e |
| **Passo a passo:** | **Introdução:**  Este documento tem como objetivo orientar a configuração dos parâmetros da MD-e para correta emissão do Manifesto do Destinatário eletrônico.  **Procedimentos:**  Acesse o RM Nucleus no seguinte menu: Opções | Parâmetros | RMNucleus | Integrações | Fiscal.  Para acesso na MDI, siga o seguinte caminho: Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento.  **Na etapa “Parâmetros por Filial”**  Marque a Filial que será parametrizada e clique no botão Parametrizar.  Será aberto uma nova janela com os Parâmetros da NF-e e deverá ser configurado conforme passos abaixo.    **Etapa “Conexão NF-e”**  Campo “URL do Servidor Totvs Services:” deve ser preenchido o endereço do TSS que foi configurado na etapa de [NF-e - Instalação e Configuração do TSS](http://tdn.totvs.com.br/pages/viewpage.action?pageId=64652506) . Caso não lembre qual foi o endereço preenchido  verifique as "DICAS DE POSSÍVEIS ERROS" do link anterior.    **Etapa “Manifestos Destinatário”**  No campo “Manifestação Destinatário” deve ser selecionado Homologação (Ambiente de teste) ou Produção.  No campo de "Versão de Sincronização de Documentos" deve ser informado a versão atual, atualmente é "1.01".      **Etapa “Certificação Digital 2/2”**  No campo “Tipo do Certificado Digital:” Selecione o tipo que será utilizado.  No campo “Certificado Digital:” Clique em  e Localize o arquivo do certificado Digital  No campo “Senha da Private Key:” preencha a senha do certificado.  **Observação:** Caso não tenha preparado o certificado .    **Avance até a ultima etapa e Salve os Parâmetros.** |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
