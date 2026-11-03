---
content_hash: a8b0bf32c8d8cd4021e82115f1617578a3da1a035491e1fb962a0f91646611e1
fetched_at: '2026-06-29T00:09:47.245188+00:00'
page_id: '435105008'
product: rm
source: tdn-rm
title: Contrato de Locação - Processo - Gerar lançamentos financeiros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105008
version: 16
---

Este processo gera os lançamentos financeiros para o TOTVS Gestão Financeira ou para Protheus. Após a geração dos lançamentos, os mesmos podem ser visualizados na aba Lançamentos do Contrato da edição do Contrato de Locação. A partir da versão 12.1.2, ao gerar lançamentos, o sistema busca as informações do Tipo evento financeiro informado na aba Identificação da edição do Contrato de Locação, e gera também o Evento Financeiro dos respectivos lançamentos automaticamente.

**Pré-condições:**

* 1 - Ter
* 2 - O contrato de Locação deve estar em seu período de vigência
* 3 - O campo Limite de crédito deve estar com o valor 0 ou então dentro dos limites do valor dos lançamentos. Para verificar estes dados é necessário acessar a aba Dados Adicionais no Cadastro de Clientes.
* 4 - Ter informado o

**Gerando os lançamentos**

* **Passo 1 -**Selecione o Contrato de Locação e acesse: Processo / Gerar Lançamentos Financeiros.
* **Passo 2 -**A tela do processo será exibida. Preencha os campos Data Inicial e Data Final, e clique em Executar.
* **Passo 3 -** Clique em Fechar.

**Parametrizações opcionais**

* Configuração Pro-rata dia

Em casos em que houver cobrança pro-rata dia, poderá ser utilizado mês civil ou comercial. Para tanto, deve-se configurar dois parâmetros em **TOTVS Incorporação>Ambiente>Parâmetros>Totvs Incorporação>Aluguel>Contrato de Locação>Configuração Pro-Rata Dia.**

**1.**  Ao marcar o parâmetro **"Considerar mês civil para cálculo do rateio"**, será considerado mês civil\* para ratear o valor do aluguel (VALOR DO ALUGUEL / QUANTIDADE DE DIAS DO MÊS). Caso este parâmetro não esteja marcado, será considerado mês comercial\*.

**2.** Ao marcar o parâmetro **"Considerar mês civil para aplicação do valor rateado"** será considerado mês civil\* na contagem de dias decorridos do mês para aplicação do valor rateado (VALOR RATEADO X QUANTIDADE DE DIAS DECORRIDOS). Caso este parâmetro não esteja marcado, será considerado mês comercial\*.

Mês comercial = 30 dias.

Mês civil = número de dias real do mês.

**Resumo:**  
VALOR RATEADO = VALOR  DO ALUGUEL / QUANTIDADE DE DIAS DO MÊS (CIVIL OU COMERCIAL) | O parâmetro 1 influencia neste cálculo.

VALOR FINAL ALUGUEL = VALOR RATEADO X QUANTIDADE DE DIAS DECORRIDOS (MÊS CIVIL OU COMERCIAL) | O parâmetro 2 influencia neste cálculo.

**Consultando os lançamentos financeiros**

* Os lançamentos financeiros gerados através da execução do processo podem ser consultados acessando a aba Lançamentos do Contrato na edição do Contrato de Locação ou através do caminho: BackOffice/ Gestão Financeira/ Contas a Pagar - Receber/ Lançamentos.

**Observações:**

* Atualmente o sistema não apresenta um tratamento relacionado a vinculação da Data Inicial e Data Final ao período de vigência do Contrato de Locação. Se for informado um período fora da vigência do Contrato, os lançamentos não serão gerados.
* A partir da versão 12.1.29, quando o Imóvel é de terceiros e seu contrato de administração possui o campo **Cobrança do Imposto sobre o Repasse do Contrato de Administração** definido como "Proprietário" não incidirão sobre os lançamentos de repasse as taxas do contrato de administração. Esta modificação faz-se necessária para a correta geração de impostos para o proprietário do imóvel, de acordo com a Legislação vigente.
* A partir da versão 12.1.2502 ao gerar os lançamentos financeiros de um contrato, o sistema irá sempre preencher o campo *Mês/Ano da Competência*,  com a data da competência da parcela gerada. Este campo pode ser encontrado no próprio lançamento financeiro na aba *"Dados Adicionais".*
* **Obs: Com a reforma tributária**, passamos a gerar no lançamento financeiro, os tributos IBS e CBS com base de cálculo, alíquota e valor, de acordo com a regra tributária informada no contrato de locação.: Para mais informações acesse: [Geração de lançamento financeiros - Locação, Aluguel Complementar e Aluguel em Dobro](https://tdn.totvs.com.br/pages/viewpage.action?pageId=1024340646)
