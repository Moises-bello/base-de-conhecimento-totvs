---
content_hash: f95ecbb6eca6053d855c6c3f5db75871107443ac5ae96cdc86ed4d12fdd07f39
fetched_at: '2026-06-29T00:09:08.946226+00:00'
page_id: '390404049'
product: rm
source: tdn-rm
title: 3554113 FOPROTINAS01-5380 DT Erro Filtro Gestão Férias Portal Chapa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=390404049
version: 2
---

# FILTRO DE CHAPA EM GESTÃO DE FÉRIAS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção & Projetos |
| **Módulo:** | TOTVS Folha de Pagamento. |
| **Função:** | Filtro em Gestão de Férias. |
| **Situação/Requisito:** | Ao acessar no menu de Gestão de férias do portal a aba 'Filtro', e clicar sob o lookup de busca do Filtro de chapa, está sendo apresentado o erro 'Quantidade de parâmetros passados para o SQL não corresponde ao esperado'. |
| **Solução/Implementação:** | A solução foi remover o filtro padrão ao usar o lookup de Chapa. Este filtro é usado internamente para adicionar um filtro padrão para algumas consultas. No caso do lookup, não é necessário. |
| **Tickets relacionados:** | 3554113 |
