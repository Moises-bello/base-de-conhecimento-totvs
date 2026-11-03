---
content_hash: 0f5544be184a6bc6909180f67db31572af50a18b07bd9dc02cf58c24146074b5
fetched_at: '2026-06-29T00:08:10.458209+00:00'
page_id: '240303564'
product: rm
source: tdn-rm
title: NFE0009_Parametrizar_movimento_de_saida_para_a_emissao_de_NF-e
type: documentation
url: https://tdn.totvs.com/display/LRM/NFE0009_Parametrizar_movimento_de_saida_para_a_emissao_de_NF-e
version: 3
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | NF-e - Nota Fiscal Eletrônica |
| **Versões:** | A partir da 11.52 |
| **Ocorrência:** | Parametrizar tipo de movimento para emissão de NF-e de saida |
| **Passo a passo:** | **Introdução:**  Este documento tem como objetivo orientar os parâmetros específicos do movimento para correta emissão de NF-e, caso deseje criar um novo movimento entre em contato com o suporte do RM Nucleus e após a criação siga este Como Fazer.  **Procedimentos:**   Acesse o RM Nucleus no seguinte menu: Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Outras Movimentações/Vendas (dependendo da classificação do tipo movimento desejado) | Selecione o Tipo de movimento e clique em Parametrizar  **Observação: Para emissão de NF-e de Saída é obrigatório que o código do tipo de movimento seja iniciado por 2.2.xx**  **Etapa Mov – Identificação:**  Nesta Etapa Selecione a Serie para emissão de NF-e, lembrando que a serie obrigatoriamente deve ser numérica, maiores informações sobre o [cadastro da serie](http://totvsconnect.blogspot.com/2011/11/como-fazer-verificar-cadastros-para.html).    **Etapa Mov – Emitente/Destinatário 1/2:**  Nesta Etapa o Emitente deverá ser “Empresa” e o destinatário “Cliente” ou “Fornecedor”.    **Mov – Datas 1/2:**  Nesta etapa deverá ser selecionado “Edita” no campo “Edição da Data de Emissão”.    **Etapa Mov – Datas 2/2:**  Nesta etapa deverá ser selecionado “Edita” no campo “Edição da Data de Saída”.    **Etapa Mov – Transporte 2/3:**  Nesta Etapa deverá ser selecionado o tipo de frete que será praticado no movimento.O campo é obrigatório pela SEFAZ e não poderá ficar como “Não Edita”.    **Etapa Mov – Campos Livres 2/2:**  Nesta Etapa pode ser selecionado a Edição do Histórico para Edita, este campo ira preencher a TAG infCpl do XML da NF-e com as informações preenchidas no movimento.    **Etapa Item – Campos Livres 2/2:**  Nesta Etapa pode ser selecionado a Editar Histórico para Edita, este campo ira preencher a TAG infAdProd do XML da NF-e com as informações preenchidas no movimento.    **Etapa Fis – Natureza:**  No Campo “Edição” do grupo “Natureza” deve ser selecionado “Edita”, no campo “Seleção Automática de Natureza” deve ser selecionado “Seleciona por Item”.    **Etapa Fis – Escrituração 1/2:**  Nesta Etapa deverá ser marcada a opção “Gerar Escrituração” e no campo “Tipo Documento Escrituração” deverá ser selecionado o tipo de documento cadastrado para emissão de NF-e, maiores informações sobre o cadastro do tipo de documento.    **Etapa Fis – Tributação – Item:**  Nesta Etapa deverão ser selecionados os tributos incidentes em cada item do movimento. Exemplo: ICMS, PIS, COFINS, ISS etc.  **Etapa Fis – Tributação – Movimento:**  Nesta Etapa deverão ser selecionados os tributos retidos incidentes na NF-e. Exemplo: COFINS RF, CONTRIBUIÇÃO SOCIAL RF, CSLLRF, IRPF, IRPJ, IRRFPJ etc.  **Etapa Fis - NF-e:**  NF-e Estadual: Selecione o tipo de envio:  Envio manual: será necessário realizar processo de envio da NF-e;  Envio automatico: ao salvar o movimento a NF-e será enviada automaticamente para a sefaz;  DANFE.Net: selecione o relatório DANFE Provider, caso não o tenha entre em contato com nosso Help Desk. |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
