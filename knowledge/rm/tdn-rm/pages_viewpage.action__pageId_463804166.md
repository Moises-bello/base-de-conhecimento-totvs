---
content_hash: b4ed9d56873a73e2665b418cc9da6bd58ffd986268af0ac894341d125672acd4
fetched_at: '2026-06-29T00:10:15.096948+00:00'
page_id: '463804166'
product: rm
source: tdn-rm
title: FISCAL01-8012 - DANFE 4.0 - Ajustes de impressão campos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=463804166
version: 1
---

# DANFE 4.0 - Ajustes de impressão campos

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Relatório DANFE |
| **Situação/Requisito:** | Ajustes que devem ser realizados no DANFE 4.00:   1. Valor Total dos Produtos está com o Bind Incorreto 2. Data e Hora de recebimento não está saindo após o Bind - DhRecbto 3. Não está gerando as informações de contingência (Chave de Acesso) 4. Mensagem DPEC não está saindo no DANFE - Não encontrei tratativa na classe FisDanfe400Provider. 5. Alterar a Descrição do Tipo de Relatório para "DANFE". |
| **Solução/Implementação:** | 1. O valor total dos produtos foi ajustados para o campo correto 2. Foi removido o campo DhRecbto e o bind foi adicionado ao campo data de autorização. A data autorização será impressa com o valor da tag dhRecbto do grupo infProt, se não for possível recuperar esta data do XML, será impresso com a data de autorização da tabela TFNEESTADUAL.DATAAUTORIZAÇÃO. Se a nota estiver em contingência offline esta data ficará em branco. 3. Foi adicionada a chave de contingência ao relatório DANFE 4. A mensagem DPEC não está com problemas 5. Foi alterado o tipo do Relatório para Genérico e alterado o processo de impressão para reconhecer DANFE com a Fonte de dados 4.00 |
