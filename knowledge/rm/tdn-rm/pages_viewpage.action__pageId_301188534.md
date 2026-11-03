---
content_hash: 0d6d5e8bfbd241c351cb4d212f26ab3cbe7122a31a669797c9873abe914941af
fetched_at: '2026-06-29T00:08:43.114702+00:00'
page_id: '301188534'
product: rm
source: tdn-rm
title: RMCTB00001_Recálculo de Diferença entre Débitos e Créditos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=301188534
version: 7
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS - Gestão Contábil |
| **Versões:** | 12.1.18 |
| **Ocorrência:** | Recálculo de Diferença entre Débitos e Créditos |
| **Ambiente:** | Novo Modelo BackOffice |
| **Passo a passo:** | **Definição do Processo:**  Este processo tem o objetivo de realizar a recálculo na base de dados a fim de identificar as possíveis diferenças entre os valores de débitos e créditos em lançamentos contábeis.    **Parametrização Necessária:**  As diferenças de valores entre débitos e créditos são consistidas por lançamento, usuário e filial, respeitando sempre a opção definida nos parâmetros do sistema. Se  a opção nos parâmetros “Permite diferenças entre filiais” estiver desmarcada o controle de diferenças entre débitos e créditos será feito por filial dentro do lançamento. Caso contrário, se a opção nos parâmetros estiver marcada, o sistema verificará apenas a diferença entre os valores de débitos e créditos por lançamento, independente das filiais utilizadas.                                         Se o parâmetro “Permite mais de uma diferença” estiver desmarcado será permitido somente uma diferença por usuário                                    **Configurações e Filtros:**  Para executar o processo acesse: Escrituração Contábil / Recálculo / Processo de Recálculo de Diferença entre Débitos e Créditos dos Lançamentos Contábeis  Nesta tela serão definidos todos os filtros a serem considerados pelo sistema:   * Devem-se selecionar quais lotes serão verificados. Deixando em branco, todos os lotes existentes (zero e N) serão analisados. * O intervalo de datas (inicial e final) que corresponde ao período contábil no qual estão compreendidos os lançamentos desejados para análise. * A coligada e a filial. Deixando em branco todas as coligadas/filiais serão verificadas. * **Desenvolvimento/Procedimento**  Para isto deverá ir ao menu Lançamentos/Recalculo Débito X Crédito.  a) Avançar, não informe lote, data inicial e data Final para o processo busque todos os lançamentos da base de dados;      b) Não informe data inicial e data Final para que o processo realize a validação de todos os lançamentos da base de dados. Clique em Analisar, para prosseguir.      c) Após apresentar os registros com as diferenças, selecione a flag "Ao executar este processo, ajuntar os lançamentos por data, corrigindo as diferenças listadas abaixo".    **Atenção:** Este processo somente ira ajustar os lançamentos com valores iguais em partidas de Débito X Crédito que se abatem e na mesma data, caso houver em datas diferentes e valores diferentes estes não são ajustados. E devem ser ajustados manualmente pelo usuário após a conciliação.      **Observação:**Se o parâmetro do sistema “Permite diferença entre filais” estiver marcado, a opção de filtro por coligada/filial não ficará disponível na tela do processo e o sistema realizará a verificação das diferenças por filial.     **Atenção:** Durante a execução do processo o(s) lançamento(s) referente(s) ao(s) lote(s) definido(s) nos filtros será(ão) bloqueado(s) de forma a garantir que nenhuma alteração seja realizada durante a conferência dos valores.    **Log:** Ao final da execução do processo será exibido um Log com todas as diferenças encontradas.  Para visualizar os lançamentos com diferença deve-se clicar no botão “Abrir Visão das Diferenças”.  A partir desta tela pode-se editar o(s) lançamento(s) e alterar os mesmos a fim de acertar a diferença. |
| **Observações:** |  |
