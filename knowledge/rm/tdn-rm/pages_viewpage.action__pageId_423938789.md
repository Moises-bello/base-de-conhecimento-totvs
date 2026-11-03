---
content_hash: a192646be71ea66282f7b3b53401c4731e541536309fc8e447b422713810811e
fetched_at: '2026-06-29T00:09:28.761695+00:00'
page_id: '423938789'
product: rm
source: tdn-rm
title: Tipo de Movimento para Recebimento Automático de NF-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938789
version: 4
---

Acesse o menu Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Parâmetros por Filial | Importação/Envio de Arquivo XML", deverá ser preenchido por filial o campo 'Fórmula Tipo Mov. Para Recebimento de NF-e'.   
Este novo parâmetro é do tipo fórmula, e assim, através do mesmo, o usuário poderá implementar uma regra específica para buscar o tipo de movimento que será utilizado no recebimento automático da NF-e de cada filial.  
Foram criadas quatro novas funções de fórmula para auxiliar na criação dessa regra, são elas:

| Tabela | Função |
| --- | --- |
| TABXMLCOLAB | Responsável por fornecer Coligada, Filial, Fornecedor e Natureza de Operação da tabela de entrada do XML. |
| DADOSXMLCOLAB | Responsável por fornecer Qualquer informação do arquivo XML. |
| QTDTAGSXMLCOLAB | Retorna o número de vezes que uma determinada Tag aparece no XML. |
| TABPRDCOLAB | Retorna o conteúdo de um campo do cadastro dos produtos vinculados aos itens constantes do XML. |
