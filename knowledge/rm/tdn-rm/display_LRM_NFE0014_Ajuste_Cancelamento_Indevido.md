---
content_hash: a3292c49efb9783f45649f1b5593a99dcf12e73becb777592a366cbd30017f1a
fetched_at: '2026-06-29T00:08:09.888390+00:00'
page_id: '240294987'
product: rm
source: tdn-rm
title: NFE0014_Ajuste_Cancelamento_Indevido
type: documentation
url: https://tdn.totvs.com/display/LRM/NFE0014_Ajuste_Cancelamento_Indevido
version: 7
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | NF-e - Nota Fiscal Eletrônica |
| **Versões:** | A partir da 11.52 |
| **Ocorrência:** | Cancelamento indevido |
| **Passo a passo:** | **Introdução:**  Este documento tem como objetivo orientar os parâmetros específicos para emissão e NF-e de Ajuste – Cancelamento Indevido.  ANTEÇÃO: A NF-e de Cancelamento Indevido Ocorre quando a empresa cancela uma NF-e indevidamente e necessita enviar uma segunda NF-e de saída referenciando a NF-e cancelada, mas antes da emissão verifique com a SEFAZ se o procedimento está correto diante da situação.  **Procedimentos:**  Acesse o RM Nucleus no seguinte menu: Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Outras Movimentações/Vendas/Compras (dependendo da classificação do tipo movimento desejado) | Selecione o Tipo de movimento e clique em Parametrizar.  **Etapa Mov – Outros Dados:**  Nesta Etapa marque a opção “Usar Copia de Movimento por referência”, selecione o motivo 21 “Cópia NF-e de Ajuste – Cancelamento Indevido” avance até a ultima etapa e salve as alterações.    Acesse a aba na qual parametrizou o tipo de movimento (Compras, Vendas ou Outras Movimentações) | preencha o filtro informando o tipo de movimento e filial | Processos | Assistente de copia por referencia | Avance e selecione o movimento que será referenciado | Selecione os itens e finalize o processo.  Altere o movimento conforme as regras da SEFAZ e envie a NF-e normalmente. |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
