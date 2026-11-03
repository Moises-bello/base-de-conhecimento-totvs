---
content_hash: c5e6bf47019b20e56e8efa8e9d42870867952c45bd4f2074866c2280ee64ce3a
fetched_at: '2026-06-29T00:08:09.899110+00:00'
page_id: '240295209'
product: rm
source: tdn-rm
title: NFE0024_Alteração_do_layout_para_3.10
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=240295209
version: 3
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | NF-e - Nota Fiscal Eletrônica |
| **Versões:** | A partir da 11.52 |
| **Ocorrência:** | NF-e - Alteração do layout para 3.10 |
| **Passo a passo:** | **Introdução**  Este documento tem como finalidade auxiliar na alteração do layout para 3.10 da NF-e. Legislação regulamentada através da norma técnica NT2013/005.  **Passo 1:**  **Para a utilização do novo layout faz se necessário a atualização da biblioteca e a execução de um SCRIPT, ambos disponíveis no portal de Download.**  1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte)  2. Faça o login, com seu Email e Senha. 3. Na barra de menu superior, clique em DOWNLOAD.  **A partir: Biblioteca: 11.52.64.100**  A partir: Biblioteca: 11.82.36  Script: **PACOTE\_NFE\_3.10\_NET.zip**  **Passo 2:**  Além de atualizar a biblioteca e executar o script, também é necessário a atualização do TSS para a versão 2.40 ou superior.  1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte)  2. Faça o login, com seu Email e Senha. 3. Na barra de menu superior, clique em DOWNLOAD.  Busque por TSS.  **Passo 3:**  No RM Nucleus acesse: Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Parâmetros por filial | selecione a filial desejada | clique em parametrizar | aba conexão NF-e| Campo Versão do Layout da NF-e Utilizado | altere o conteúdo do campo para 3.10.    **Dicas:**  Alguns campos tornaram se obrigatório coma mudança do layout, segue:  **Tag dhSaiEnt** (Data e Hora de Saída) – Torna-se necessário a parametrização do tipo de movimento na etapa Mov – Dadas 2/2, campo Edição da hora de saída/entrada deve estar como edita ou mostra.  **indPres** (Indicador de presença do comprador no estabelecimento comercial no momento da operação) – No movimento - aba integrações – menu fiscal – campo Operação Presencial, deve ser selecionado a opção desejada, duvidas vide manual de orientação do contribuinte.  **idEstrangeiro** (Identificação estrangeiro) – Acesse o cadastro do cliente/fornecedor :  **1-**    Cliente seja Pessoa Jurídica: o campo “Documentos Estrangeiros” será apresentado se o estado no endereço do não estiver marcado como nacional.  **2-**    Cliente pessoa física: o campo  “Documentos Estrangeiros”  será  apresentado ao selecionar a opção “Estrangeira” no campo Nacionalidade.    Demais informações e campos específicos devem ser verificadas na norma técnica NT 2013/005, disponível do site da SEFAZ. |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
