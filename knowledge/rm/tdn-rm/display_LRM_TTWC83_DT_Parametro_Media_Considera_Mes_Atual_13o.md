---
content_hash: d99b353fc33682ba3ef087111491526597480f5239ae507242339cab2d6fa0bc
fetched_at: '2026-06-29T00:06:23.397268+00:00'
page_id: '224101633'
product: rm
source: tdn-rm
title: TTWC83_DT_Parametro_Media_Considera_Mes_Atual_13o
type: documentation
url: https://tdn.totvs.com/display/LRM/TTWC83_DT_Parametro_Media_Considera_Mes_Atual_13o
version: 2
---

# PARÂMETRO DE MÉDIA PARA CONSIDERAR O MÊS ATUAL NO CÁLCULO DO 13o.

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *13o.Salário* |
| **Situação/Requisito:** | *Na pasta "Média" do cadastro de Sindicato existe o parâmetro "Considera mês de rescisão para média".*  *E na pasta "13o.Salário" existe o parâmetro "Considera mês atual para cálculo de média de 13º".*  *Ou seja, no caso de 13o. na rescisão é verificado o parâmetro da pasta "Média", e no caso de 13o.2a.Parcela é verificado o parâmetro da pasta "13o.Salário".*  *Entretanto, quando está marcado o parâmetro "Utiliza parâmetros específicos para média de 13o.rescisão" da pasta "13o.Salário" é exibida uma nova aba para parâmetros de rescisão, onde também existe a opção "Considera mês atual para cálculo de média de 13º".*  *Este campo está sendo ignorado no cálculo da média de 13o. na rescisão. Independente de estar marcado ou não, o que está sendo considerado é o parâmetro "Considera mês de rescisão para média" da pasta "Média".* |
| **Solução/Implementação:** | *Quando o usuário marca para utilizar parâmetros específicos para média de 13o.rescisão, todos os parâmetros existentes na nova aba devem sobrepor os parâmetros semelhantes já existentes.*  *Ou seja, o parâmetro "Considera mês atual para cálculo de média de 13º" da aba para parâmetros específicos de 13o. rescisão deve sobrepor o "Considera mês de rescisão para média" da pasta "Média".* |
| **Chamados   relacionados:** | *TTWC83, TUBAWK* |
| **Versões/Release:** | *11.82.43, 12.1.10* |
