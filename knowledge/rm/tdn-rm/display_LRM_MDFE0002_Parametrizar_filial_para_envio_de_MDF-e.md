---
content_hash: 45580d5909ad07aad5b79fedabc45b4d66da113646b66671b0869c961dbb6c87
fetched_at: '2026-06-29T00:08:13.606625+00:00'
page_id: '244428499'
product: rm
source: tdn-rm
title: MDFE0002_Parametrizar_filial_para_envio_de_MDF-e
type: documentation
url: https://tdn.totvs.com/display/LRM/MDFE0002_Parametrizar_filial_para_envio_de_MDF-e
version: 1
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | MDF-e - Manifesto Eletrônico de Documentos Fiscais |
| **Versões:** | A partir da 11.52 |
| **Ocorrência:** | Parametrizar a filial para emissão de MDF-e |
| **Passo a passo:** | **Introdução:**  Este documento tem como objetivo orientar a configuração dos parâmetros da MDF-e para correta emissão do Conhecimento de transporte eletrônico.  **Procedimentos:**  Acesse o RM Nucleus no seguinte menu: Opções | Parâmetros | RMNucleus | Integrações | Fiscal.  Para acesso na MDI, siga o seguinte caminho: Ambiente | Parametros | Gestão de Estoque, Compras e Faturamento.  **Na etapa “Parâmetros por Filial”**  Marque a Filial que será parametrizada e clique no botão Parametrizar.  Será aberto uma nova janela com os Parâmetros da NF-e e deverá ser configurado conforme passos abaixo.  **Etapa “Conexão NF-e”**  Campo “URL do Servidor Totvs Services:” deve ser preenchido o endereço do TSS que foi configurado na etapa de  . Caso não lembre qual foi o endereço preenchido  verifique as "DICAS DE POSSÍVEIS ERROS" do link anterior.    **Etapa “Certificação Digital 2/2”**  No campo “Tipo do Certificado Digital:” Selecione o tipo que será utilizado.  No campo “Certificado Digital:” Clique em  e Localize o arquivo do certificado Digital  No campo “Senha da Private Key:” preencha a senha do certificado.  **Observação:** Caso não tenha preparado o certificado .      **Etapa “Ambiente MDF-e”**  No campo “Ambiente de envio” deve ser selecionado Homologação (Ambiente de teste) ou Produção.  No campo “Modalidade de Operação” deve ser selecionado a modalidade que os MDF-es serão emitidos (Normal ou Contingência Offline).  Nos campos de "Versões de Layout" deve ser informado a versão atual, atualmente é "1.00".  Nos campos de "Versões de Layout do Evento" deve ser informado a versão atual dos eventos , atualmente é "1.00".    **Avance até a ultima etapa e Salve os Parâmetros.** |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
