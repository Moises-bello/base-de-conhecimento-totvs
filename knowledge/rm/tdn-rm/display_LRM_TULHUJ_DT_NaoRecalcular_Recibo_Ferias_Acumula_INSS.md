---
content_hash: 1735c40f79cf4ddea90d388625f748439ceb7a5cffbaca947b42be6b79bbe360
fetched_at: '2026-06-29T00:08:03.911016+00:00'
page_id: '235329019'
product: rm
source: tdn-rm
title: TULHUJ_DT_NaoRecalcular_Recibo_Ferias_Acumula_INSS
type: documentation
url: https://tdn.totvs.com/display/LRM/TULHUJ_DT_NaoRecalcular_Recibo_Ferias_Acumula_INSS
version: 2
---

# OPÇÃO NÃO RECALCULAR DO RECIBO DE FÉRIAS NÃO DISCRIMINA INSS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Recibo de Férias* |
| **Situação/Requisito:** | *No cálculo do recibo de férias partidas, quando o parâmetro "Discrimina INSS no recibo de férias" está desmarcado, o desconto de INSS é calculado para as duas competências, mas o valor é acumulado todo no evento de CC 82 (INSS Férias no Mês).*  *Na pasta Bases da tela do Recibo é exibido o valor do desconto discriminado por competência, e estes valores que são utilizados para lançar os descontos discriminados no envelope do funcionário.*  *Entretanto, quando é feito alguma alteração manual do recibo de férias, e é marcada a opção de "Não Recalcular", os valores são salvos novamente, e na pasta Bases os descontos de INSS são acumulados no campo do 1o. mês.*  *E assim o lançamento das férias para o envelope não processa o evento de CC 130 (INSS Férias Próximo Mês).* |
| **Solução/Implementação:** | *Ajuste na opção de "Não Recalcular" do Recibo de Férias para que, ao processar a atualização do dados, efetuar a discriminação dos valores do desconto de INSS na pasta Bases, mesmo quando o parâmetro "Discrimina INSS no recibo de férias" estiver desmarcado.* |
| **Chamados   relacionados:** | *TULHUJ, TUPKPB* |
| **Versões/Release:** | *11.82.43, 12.1.11* |
