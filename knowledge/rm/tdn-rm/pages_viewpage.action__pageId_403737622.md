---
content_hash: cee1858e3c22bfd9781ad7d49b1060c1b3a6e6c66c29bd7c5c3f119c0d9d39a3
fetched_at: '2026-06-29T00:09:10.961096+00:00'
page_id: '403737622'
product: rm
source: tdn-rm
title: 401179 DT DSAUGCIH-25 Unidade Clínica da Dispensação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=403737622
version: 3
---

# Inclusão de Unidade Clínica na Dispensação do Antibiótico

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Controle de Infecção Hospitalar |
| **Função:** | Informe a função. |
| **Requisito:** | Eu como operador de CCIH, quero obter a informação referente a unidade clinica de dispensação de antibióticos de um sistema HIS, de modo que a unidade clinica ao ser importada no CIH nas dispensações de itens de antibiótico possa permitir o ajuste do BI de "Antibiótico Consumo / DDD" na dimensão antibiótico, pois o mesmo não está aderente no momento.. |
| **Implementação:** | Todas as dispensações importadas devem ter o campo unidade clinica da dispensação, e no sistema CIH, constará na tela de dispensações conforme imagem abaixo e também, no BI de Consumo DDD        No endereço , na view de importação de antibiótico, também foi acrescentado no layout o campo CodClinicaDispensacao |
