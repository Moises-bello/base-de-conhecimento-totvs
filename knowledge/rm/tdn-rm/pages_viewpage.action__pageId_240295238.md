---
content_hash: e340260b82e000e73df6f02051086fdb54930574578ca074be81bc255bc2eefb
fetched_at: '2026-06-29T00:08:09.907777+00:00'
page_id: '240295238'
product: rm
source: tdn-rm
title: NFE0022_Aproveitamento_de_ativo_imobilizado_1/48_CIAP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=240295238
version: 9
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | NF-e - Nota Fiscal Eletrônica |
| **Versões:** | A partir da versão 11.52 |
| **Ocorrência:** | Aproveitamento de ativo imobilizado 1/48 - CIAP |
| **Passo a passo:** | **Introdução:**  Este documento auxilia na criação de movimento para geração da NF-e para o aproveitamento do ativo imobilizado 1/48.  **Criando uma NF-e de Aproveitamento de Ativo Imobilizado 1/48**  1 - Siga os passos da faq de parametrização de movimento de entrada;   2 - **Parametrizar o tipo de movimento:** Acesse o RM Nucleus no seguinte menu: Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Outras Movimentações/Vendas/Compras (dependendo da classificação do tipo movimento desejado) | Selecione o Tipo de movimento e clique em Parametrizar  **Etapa Mov** – **Emitente e Destinatário:** Selecionar nos parâmetros do Tipo de Movimento a opção  “Emitente" = Empresa e "Destinatário” =  Empresa.    **Etapa Item - Preço**: Marcar a opção "Aceitar Preço Zero";    3 -**Produto:** criar um item do tipo produto “Genérico”;  Acesse: Cadastro / Produto e Serviços    4 - **CFOP (Naturezada de operação**): Utilizar CFOP “1.604” sendo a regra de ICMS com situação tributária “00 - Tributada Integralmente”;    5 - Selecionar o tipo de movimento onde será criada NF-e de Aproveitamento de 1/48, informar o CFOP na identificação do movimento;  6 - Inserir o item genérico criado anteriormente e informar quantidade “1”um e valor “0”zero lembrando que a natureza fiscal deverá ser informada também no item;  7 - No tributo do item, informar apenas o valor do ICMS à ser creditado e zerar as outras colunas;  O processo de envio da NF-e deverá ser executado normalmente. |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
