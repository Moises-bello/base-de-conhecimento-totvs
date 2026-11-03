---
content_hash: 5faad3df9ef576b4eebdb58d09ad080823a296137ae5524a9a4b1bb072833d85
fetched_at: '2026-06-29T00:08:59.756830+00:00'
page_id: '364912686'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-2470 DT Código defensivo do desconto por antecipação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364912686
version: 1
---

# CÓDIGO DEFENSIVO DO DESCONTO POR ANTECIPAÇÃO - 12.1.20

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | Acesso a funcionalidades do sistema que utilizam desconto por antecipação em bases habilitadas para se trabalhar com desconto e bases não habilitadas. |
| **Situação/Requisito:** | Alguns menus de desconto por antecipação ficavam desabilitados tais como: Cadastro do desconto por antecipação, Alteração de vencimento de desconto por antecipação e Desconto por antecipação de parcelas. |
| **Solução/Implementação:** | - Tratamento de visibilidade e validação dos campos de Ordem de aplicação do desconto por antecipação e afeta base de cálculo nas seguintes rotinas:      - Cadastro de bolsa no contrato do aluno      - Cadastro de bolsas      - Cadastro de concessão de bolsas      - Concessão de bolsas futuras  - Visibilidade do campo "Considera desconto por antecipação" na edição do contrato  - Acesso ao processo de alteração de vencimento de desconto por antecipação somente se rodar os últimos scripts de ajustes para o SER EDUCACIONAL  - Acesso à visualização de descontos por antecipação da parcela somente se rodar os últimos scripts de ajustes para o SER EDUCACIONAL  - Acesso À visualização de detalhamento de bolsas de desconto por antecipação somente se rodar os últimos scripts de ajustes para o SER EDUCACIONAL  - Baixa de lançamentos com desconto por antecipação passa a consultar as tabelas SBOLSALANDESCPONTUAL e SBOLSALAN ao invés de proporcionalizar se tiver rodado os scripts  - Não será gerado lançamento utilizando desconto por antecipação se os scripts não tiverem sido executados na base do cliente.  - Menus de desconto por antecipação passam a ficar habilitados. O usuário conseguirá cadastrar os descontos mas não conseguirá utilizar os mesmos na geração de lançamentos. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
