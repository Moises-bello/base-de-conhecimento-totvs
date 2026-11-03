---
content_hash: 68c6a0d9c204a8343d0bc8c97b34ddd502c02d17af9a0e37f64e0681a50c46c0
fetched_at: '2026-06-29T00:08:52.657423+00:00'
page_id: '342297880'
product: rm
source: tdn-rm
title: DT - Ajustes na Tela do Assistente de Geração dos Lançamentos Financeiros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=342297880
version: 2
---

# SEPARAÇÃO DO GRUPO DE TABELAS OPCIONAIS EM UM NOVO PASSO DO ASSISTENTE

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Geração dos Lançamentos Financeiros |
| **Situação/Requisito:** | No grupo de Seleção de Lançamentos Ativos, quando a junção do código com a descrição do lançamento é muito longa, parte da descrição é cortada: |
| **Solução/Implementação:** | O grupo de Tabelas Opcionais foi movido para um novo passo do assistente de Geração de Lançamentos Financeiros, logo após a Seleção de Lançamentos Ativos. Assim, tanto o grupo de Seleção de Lançamentos Ativos quanto o grupo de Tabelas Opcionais ficaram em passos separados (passos 2 e 3, respectivamente, onde a tela de Boas-Vindas é considerada o passo 0) do assistente e foram redimensionados para ocupar uma porção maior da tela:        Vale ressaltar que o passo contendo o grupo de Tabelas Opcionais será exibido apenas quando o parâmetro "Usa integração outros backOffice" estiver desmarcado em "Configurações | Parâmetros | Parametrizador | 06.02.06 - Outros BackOffice": |
| **Tickets relacionados:** | 2069288 |
