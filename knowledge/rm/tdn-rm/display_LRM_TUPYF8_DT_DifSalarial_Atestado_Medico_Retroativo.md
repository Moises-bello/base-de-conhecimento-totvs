---
content_hash: 62987e2c6b467fa89ac5b6ef3f42a4aebae48a4c4affd7516aea2bd7dd45d9b6
fetched_at: '2026-06-29T00:08:04.108383+00:00'
page_id: '235335941'
product: rm
source: tdn-rm
title: TUPYF8_DT_DifSalarial_Atestado_Medico_Retroativo
type: documentation
url: https://tdn.totvs.com/display/LRM/TUPYF8_DT_DifSalarial_Atestado_Medico_Retroativo
version: 4
---

# DIFERENÇA SALARIAL APÓS LANÇAMENTO DE ATESTADO MÉDICO RETROATIVO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Diferença Salarial* |
| **Situação/Requisito:** | *No cálculo da Diferença Salarial, quando está marcado o parâmetro "Zerar evento de diferença quando o valor ficar negativo", e ocorre um cadastro retroativo de atestado médico, a diferença negativa dos Dias Trabalhados (CC 2) deveria abater do evento de Atestado Médico (CC 145), antes de zerar o evento.*  *Exemplo: Após pagar 30 dias de salário para o funcionário, e liberar a competência, o mesmo foi afastado com data de início no dia 25 do mês anterior, e foi aumentado o salário, também retroativo ao mês anterior. Neste caso, o valor do CC 2 fica negativo, por ser recalculado com 24 dias, ao invés de 30. E são calculados os 6 dias de Atestado Médico no CC 145.  Se o valor negativo da diferença do CC 2 for zerada, o funcionário fica com 36 dias de salário no mês.* |
| **Solução/Implementação:** | *Ajuste na Diferença Salarial, para considerar os valores dos eventos de CC 2 e CC 145 acumulados, antes de consistir o parâmetro "Zerar evento de diferença quando o valor ficar negativo".*  *Ou seja, só zerar o valor se o somatório da diferença dos 2 eventos resultar em um valor negativo.* |
| **Chamados   relacionados:** | *TUPYF8, TUQKAL* |
| **Versões/Release:** | *11.82.43, 12.1.11* |
