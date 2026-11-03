---
article_id: 360061829673
category: LEGAIS - BLOCO H/MATR460
content_hash: afeb216279bb5f6d4c09edab437edd347e3f51683b6566a3b69bbcd0e68d6c62
fetched_at: '2026-06-28T22:42:15.061268+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Dicas de Análise dos
  Saldos no Relatório MATR460 (P7)
type: support-article
updated_at: '2026-03-13T18:39:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061829673-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Dicas-de-An%C3%A1lise-dos-Saldos-no-Relat%C3%B3rio-MATR460-P7
---

O relatório MATR460 (Inventário Modelo 7) mostra saldos físicos e custos ao final do mês, mas pode gerar dúvidas devido a parâmetros como "Prods com Saldo Zerado?". Para conferir saldos, compare com o relatório MATR260 e a tabela SB9. Para estoques de terceiros, verifique parâmetros MV\_CONTERC e use o MATR480. Para custos, confirme a data de fechamento e recalcule custo médio (MATA330). Se houver inconsistências, execute a rotina MATA216 para refazer poder de terceiros.

**Dúvida**

Como posso identificar de onde o relatório MATR460 está imprimindo determinado saldo físico ou de custo?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

O Relatório MATR460 (Inventário Modelo 7) é utilizado frequentemente quando o usuário precisa avaliar os saldos ao final do mês (Embora ele seja apenas espelho do Bloco H). Contudo, por alguns momentos ao imprimirmos este relatório, gera-se dúvidas sobre saldos e custos de determinados produtos. Com isso vamos abordar neste artigo algumas dicas que auxiliarão numa análise das impressões deste relatório.

**Observação importante:**

Atente-se às perguntas como "Prods c/ Saldo Neg?", " Prods c/ Saldo Zerado?", "Lista Custo Zerado?". Estas perguntas podem fatalmente gerar impressão diferente do desejado.

**Exemplo de possível "impressão incorreta" no MATR460:**  Se parametrizar o campo **"Prods com Saldo Zerado?" = Não**, se um produto A tiver armazém 01 e 02 e, por algum motivo no armazém 01 tiver saldo físico zerado, a impressão ignorará o custo que estiver atrelado ao armazém 01. Ele só irá trazer o custo e quantidade do armazém 02.

**Caso tenha dúvida do saldo físico impresso de determinado(s) produto(s) em estoque próprio:**

- No MATR460, emita o relatório filtrando apenas ele, a data do último fechamento e avalie os armazéns (se selecionou todos) ou não;

- Compare-o com o relatório MATR260. [**Clique aqui e veja como parametrizar o MATR260 para comparação com o MATR460**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020482651-MP-SIGAEST-Comparar-MATR460-com-MATR260)**;**

- Compare o saldo físico e de custo com o que está na tabela SB9 - Saldos Iniciais, no campo **B9\_QINI.**

**Caso tenha dúvida no saldo físico impresso de determinado(s) produto(s) em estoque de/em terceiros:**

- Se o problema for no estoque EM terceiros, avalie se utiliza os parâmetros MV\_CONTERC. Se estiver como T (True), avalie o armazém delegado no parâmetro MV\_ALMTERC e veja seu saldo no MATR260 no último fechamento. [**Clique aqui e veja como parametrizar o MATR260 para comparação com o MATR460**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020482651-MP-SIGAEST-Comparar-MATR460-com-MATR260)

- Avalie se o saldo em poder de/em terceiros é coerente utilizando o Relatório MATR480 (Relatório de controle de poder de/em terceiros). Nele é possível filtrar o produto e um período extenso para entender, na coluna "Saldo", qual o saldo está em poder de/em terceiros para o produto;

- Avalie as TES envolvidas nas movimentações que geraram saldo de/em terceiros. Caso entre a remessa e devolução tenha utilizado TES que não atualiza Estoque (F4\_ESTOQUE = N), avalie a possibilidade de alterar o conteúdo do parâmetro MV\_SDTESN3 ([**clique aqui e entenda melhor a relação deste parâmetro com o MATR460 para saldo de/em terceiros**](https://tdn.totvs.com/pages/releaseview.action?pageId=235594782));

**Caso tenha dúvida no custo de determinado(s) produto(s):**

- Certifique-se de que está delegando a "Data de fechamento" conforme a última virada de saldos;

- Avaliar se foi executado o Recálculo do Custo Médio (MATA330) e checar, na tabela SB9 - Saldos Iniciais, os campos B9\_VINI1...5 para entender se o saldo bate com o que o relatório está imprimindo;

- Comparar com  o relatório MATR900 ([**clique aqui e entenda melhor como parametrizar o relatório MATR900 para análise de custos**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011930291-MP-SIGAEST-An%C3%A1lise-de-Custos-MATR900-Kardex-por-Per%C3%ADodo)) e veja se o custo final (cujo último movimento seja igual ou anterior à data do ultimo fechamento) batem;

**Refazendo Poder de Terceiros**

Caso os dados em outros relatórios e/ou tabelas correlatas (SB6 - Saldo DE/EM Terceiros, SB2 - Saldo Físico e Financeiro, SB9 - Saldos Iniciais, SF4 - TES) estejam trazendo dados coerentes e apenas o MATR460 esteja mesmo assim apresentando dados inconsistentes, avalie a possibilidade de executar a rotina **MATA216 (Refaz Poder de Terceiros)** para o produto ao qual estiver com esta divergência.

**Saiba mais:**

[*MP - SIGAEST - Parâmetros (SX6) relacionados ao relatório MATR460 - Registro de Inventário Modelo 7*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001351901-MP-SIGAEST-Par%C3%A2metros-SX6-relacionados-ao-relat%C3%B3rio-MATR460-Registro-de-Invent%C3%A1rio-Modelo-7)

[*Perguntas do relatório MATR460 (Inventário Modelo 7)*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001540542)

[*MP - SIGAEST - Validação do Parâmetro MV\_R460TPC*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001352161-MP-SIGAEST-Valida%C3%A7%C3%A3o-do-Par%C3%A2metro-MV-R460TPC)

[*Clique aqui e veja mais artigos sobre Bloco H e MATR460 (P7) no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033001-SIGAEST-LEGAIS)
