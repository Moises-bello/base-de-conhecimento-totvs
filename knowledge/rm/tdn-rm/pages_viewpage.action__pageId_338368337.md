---
content_hash: c11ea77b188cbc6ab06c31797fca517725353414400aa122052a6cbe4ead399a
fetched_at: '2026-06-29T00:08:51.904580+00:00'
page_id: '338368337'
product: rm
source: tdn-rm
title: 1918106 CONTROLADORIA01-879  DT Alteração de Grupo e Taxa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=338368337
version: 5
---

# Alteração de Grupo e Taxa

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Patrimonial |
| **Função:** | Alteração de Múltiplos Patrimônios |
| **Situação/Requisito:** | O cliente realiza a inclusão de alguns bens com datas dentro do período de cálculo atual diferentes do dia 1º (primeiro), onde o sistema está parametrizado para gerar a depreciação somente no 1º dia do mês subsequente à aquisição (se data de aquisição não for 1º dia do mês), assim o sistema não gera a linha de cálculo razão para os bens mesmo o bem possuindo uma taxa de depreciação gerada pelo default do grupo de patrimônio, então ficando da seguinte maneira ao editar o "cenário de cálculo":  TAXA VIGÊNCIA 0% 10/10/2017 4% 01/11/2017  Algumas vezes é necessário que o cliente altere o grupo de patrimônio destes bens e suas respectivas taxas no mesmo período que os bens foram inclusos, porém ao realizar a alteração de grupos destes bens através do processo de alteração de múltiplos patrimônios verifica-se que o bem atualiza a taxa zerada (do período atual) para a nova taxa do grupo, ficando da seguinte forma:  TAXA VIGÊNCIA 10% 10/10/2017 4% 01/11/2017  Assim é necessário o cliente liberar a competência para então realizar novamente o processo de alteração de grupos de patrimônios apenas para atualizar a taxa do patrimônio no "Cenário para cálculo" que fica da seguinte forma:  TAXA VIGÊNCIA 10% 10/10/2017 10% 01/11/2017 |
| **Solução/Implementação:** | Após a alteração do grupo de patrimônio, a taxa de depreciação deve permanecer zerada, se o parâmetro "Data início depreciação igual ao primeiro dia do próximo ano base" estiver marcado, então a taxa de depreciação deve ser igual a zero. Essa situação deve ser verificada se o ano da vigência for igual ao ano de aquisição do patrimônio.  Se o parâmetro "Data padrão de início da depreciação será SEMPRE 1º dia do mês subsequente à aquisição" estiver marcado ou o parâmetro "Data padrão de início da depreciação será 1º dia do mês subsequente à aquisição" estiver marcado, e o dia em que o patrimônio foi adquirido for maior que 1, então a taxa de depreciação deve ser zero. Essa situação só deve ser verificada se o mês e ano da vigência forem iguais ao mês e ano da data de aquisição do patrimônio. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |
