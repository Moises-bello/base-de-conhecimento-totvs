---
content_hash: 2b1018578f0e2146e8db1f971e5b5a425b0cbadd073674abc6f0f78c6a7f2dab
fetched_at: '2026-06-29T00:08:09.893744+00:00'
page_id: '240295187'
product: rm
source: tdn-rm
title: NFE0015_Ajuste_Estorno
type: documentation
url: https://tdn.totvs.com/display/LRM/NFE0015_Ajuste_Estorno
version: 5
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | NF-e - Nota Fiscal Eletrônica |
| **Versões:** | A partir da 11.52 |
| **Ocorrência:** | Estorno |
| **Passo a passo:** | **Introdução:**  Este documento tem como objetivo orientar a emissão de NF-e de Ajuste de Estorno.  **ATENÇÃO**: A NF-e de Estorno ocorre quando a empresa perdeu o prazo de cancelamento da NF-e, então é gerada uma NF-e de Estorno referenciando a NF-e que não pode mais ser cancelada, mas antes da emissão verifique com a SEFAZ se o procedimento está correto diante da situação.  **Procedimentos:**  Acesse o RM Nucleus no seguinte menu: Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Outras Movimentações/Vendas/Compras (dependendo da classificação do tipo movimento desejado) | Selecione o Tipo de movimento e clique em Parametrizar.  **Etapa Mov – Outros Dados:**  Nesta Etapa marque a opção “Usar Copia de Movimento por referência”, selecionando o motivo 22 ou 23 (Cópia NF-e de Ajuste – Estorno de Venda ou Cópia NF-e de Ajuste – Estorno de Compra) e salve as alterações.    Acesse a aba na qual parametrizou o tipo de movimento (Compras, Vendas ou Outras Movimentações) | preencha o filtro informando o tipo de movimento e filial | Processos | Assistente de copia por referencia | Avance e selecione o movimento que será referenciado | Selecione os itens e finalize o processo.  Altere o movimento conforme as regras da SEFAZ e envie a NF-e normalmente. |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
