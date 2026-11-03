---
article_id: 28659960669335
category: Encargos
content_hash: 251ff3e029d852baa14377865df5fe744046b238931bea1e8723d2047eda4dde
fetched_at: '2026-06-28T22:46:52.241165+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Lançamento financeiro tipo 26 - Total Guia INSS 13º com o mesmo
  valor apresentado na DCTFWeb
type: support-article
updated_at: '2024-12-19T20:10:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28659960669335-RH-RM-FOP-Lan%C3%A7amento-financeiro-tipo-26-Total-Guia-INSS-13%C2%BA-com-o-mesmo-valor-apresentado-na-DCTFWeb
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28659960627479) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como fazer lançamento financeiro tipo 26 - Total Guia INSS 13º com o mesmo valor apresentado  na DCTFWeb?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir da versão 12.1.2209  
  
**Solução**O tipo de lançamento financeiro **26 - Total Guia INSS 13º**, refere-se à soma dos valores totais enviados por meio do eSocial que compõem a DARF gerada na DCTFWeb anual, específica para o 13º salário. O lançamento pode ser realizado por filial ou coligada e tem a opção de ser rateado por centro de custo ou departamento.

Para realizar o lançamento financeiro, acesse **Encargos | Cadastros Financeiros | Parâmetros** e parametrize o lançamento com o tipo **26 - Total Guia INSS 13º** , e também a aba Lançamentos Ativos.

Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28659960631319)

**Importante:** Com o intuito de evitar divergências durante a conferência, o**Relatório de Conferência** de INSS Patronal sempre levará em consideração os autônomos registrados no TOTVS Gestão Financeira. Portanto, o parâmetro **"Desconsiderar Autônomos TOTVS Gestão Financeira"** não será aplicado no referido relatório. Essa abordagem visa garantir a consistência e a coerência dos registros, facilitando o processo de verificação e prevenindo possíveis discrepâncias.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28659948486679)

Em seguida acesse **Encargos | Geração dos lançamentos Financeiros**, preencha os campos necessários

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28659948487703)

Selecione apenas o código ativo associado ao parâmetro financeiro:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28659948489495)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28659960642967)

**Importante**:

1. Não serão utilizados filtros para esse tipo de lançamento financeiro.
2. Para realizar a validação do valores utilize Relatório de Conferência INSS Patronal.
3. Para realizar o cálculo dos valores dos encargos sociais (terceiros, patronal e outros) no lançamento financeiro, é fundamental que o parâmetro "Discriminar Percentual de Terceiros" esteja marcado. Além disso, é necessário garantir que os percentuais estejam cadastrados corretamente na seção Cadastros | Seções | Anexos | Histórico de Percentuais para INSS. Vale ressaltar que, nos casos em que não há recolhimento, como é comum em empresas filantrópicas isentas de determinados encargos, é fundamental preencher os percentuais com "0-zero".  Este procedimento assegura a precisão e a consistência no cálculo dos encargos.
4. A rastreabilidade do lançamento financeiro existente foi desenvolvida especificamente para funcionários cadastrados na folha de pagamento, sendo a chapa o identificador utilizado.

Saiba mais:

[RH - RM - FOP - Lançamento financeiro tipo 25 - Total Guia INSS com o mesmo valor apresentado na DCTFWeb](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13423681275159-RH-RM-FOP-Lan%C3%A7amento-financeiro-tipo-25-Total-Guia-INSS-com-o-mesmo-valor-apresentado-na-DCTFWeb)

[Cadastros Financeiros](https://tdn.totvs.com.br/display/public/LRM/Cadastros+Financeiros)
