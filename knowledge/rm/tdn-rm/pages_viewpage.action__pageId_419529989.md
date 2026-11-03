---
content_hash: fa65cb08d7ca2f38bc3f99b95f9b522b8c727971dccdb9dcb61aaa63b22e039c
fetched_at: '2026-06-29T00:09:12.951069+00:00'
page_id: '419529989'
product: rm
source: tdn-rm
title: DSAUGCIH-244 DT Cultura Parcial - Validação da Data da Coleta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=419529989
version: 1
---

# Validação da Data da Coleta

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde. |
| **Módulo:** | Controle de Infecção Hospitalar (CIH) |
| **Função:** | Cultura Parcial - Validação da Data da Coleta |
| **Situação/Requisito:** | As validações referentes aos campos Data Coleta e Hora Coleta foram redefinidas. |
| **Solução/Implementação:** | No caminho de menu do sistema: Paciente >> Internações >> Cultura Parcial  As seguintes regras de validação descritas abaixo foram aplicadas para os campos Data Coleta e Hora Coleta:  Se a 'Data Coleta' for idêntica à data da Internação o sistema preenche "automaticamente" o campo 'Hora Coleta' com o valor 23:59  Se a 'Data Coleta' for idêntica à data da Alta e diferente da data da Internação o sistema preenche automaticamente o campo 'Hora Coleta' com o valor 00:00  Se a 'Data Coleta' for idêntica à data da internação e alta, o sistema deverá preencher automaticamente a 'Hora Coleta'  com o valor de um minuto após a hora da internação. Ex. paciente internado 13/08/2018 07:50hs e com alta em 13/08/2018 18:30hs, o sistema deverá colocar a hora da coleta às '07:51'.  Abaixo detalhe de acesso na tela de Cultura Parcial e indicação dos campos com as regras aplicadas acima: |
