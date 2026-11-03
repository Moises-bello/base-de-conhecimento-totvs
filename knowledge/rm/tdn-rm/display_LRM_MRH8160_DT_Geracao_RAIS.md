---
content_hash: 5b96ff6f084d0e5b25849ca0e5da97d7d01a8758590a7234f243c5c37c4ffdc5
fetched_at: '2026-06-29T00:08:29.471050+00:00'
page_id: '272146246'
product: rm
source: tdn-rm
title: MRH8160_DT_Geracao_RAIS
type: documentation
url: https://tdn.totvs.com/display/LRM/MRH8160_DT_Geracao_RAIS
version: 1
---

# Geração RAIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Geração RAIS* |
| **Situação/Requisito:** | Ao gerar arquivo RAIS para um funcionário que não tenha sindicato, por exemplo os estagiários que o sistema permite salvar cadastro sem informar sindicato, o sistema está apresentando o erro abaixo:  “Erro ao calcular campo CampoRaisCNPJContribAssoc - System.NullReferenceException: Referência de objeto não definida para uma instância de um objeto. |
| **Solução/Implementação:** | Ajuste na rotina RAIS quando funcionário não possuir vínculo com sindicato. |
