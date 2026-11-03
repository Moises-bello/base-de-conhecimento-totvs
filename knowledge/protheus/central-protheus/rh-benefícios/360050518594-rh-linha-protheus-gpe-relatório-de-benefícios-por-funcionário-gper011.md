---
article_id: 360050518594
category: RH - Benefícios
content_hash: 3cee852e466ab01051c7d9956c88e69bda965d11739535e24ddfcc3ac49a4e8e
fetched_at: '2026-06-28T22:44:04.777660+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Relatório de Benefícios por Funcionário (GPER011)
type: support-article
updated_at: '2025-09-12T14:07:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050518594-RH-Linha-Protheus-GPE-Relat%C3%B3rio-de-Benef%C3%ADcios-por-Funcion%C3%A1rio-GPER011
---

**Dúvida**Relatório de Benefícios por Funcionário GPER011.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**Esta rotina efetua a impressão de todos os benefícios do funcionário, sendo: Vale Refeição, Vale Alimentação, Vale Transporte, Plano de Saúde e Outros Benefícios.

No caso do Plano de Saúde é possível optar pela impressão dos Planos de Dependentes e Agregados.  
  
**Importante:**

* Para a impressão do **Plano de Saúde** será verificado se o período informado nos parâmetros está contido no período de vigência do plano.
* Para a impressão dos Planos Ativos dos Dependentes será verificada a pergunta **Plano Saúde Dependentes** e, caso a mesma esteja como **Sim** será feita a leitura da tabela de Planos Ativos do Dependente (RHL) e verificado se o período informado nos parâmetros está contido no período de vigência do plano.
* Para a impressão dos Planos Ativos dos Agregados será verificada a pergunta **Plano Saúde Agregados** e, caso a mesma esteja como **Sim**será feita a leitura da tabela de Planos Ativos do Agregado (RHM) e verificado se o período informado nos parâmetros está contido no período de vigência do plano.
* Caso a pergunta **Plano de Saúde** esteja como **Não**, não será possível selecionar **Sim** para a impressão dos planos de dependentes e agregados.
* Ao informar um período aberto no parâmetro, os dados de cálculo virão "zerados" para o benefício Plano de Saúde.

Para gerar o relatório, acessar em **Atualizações> Benefícios> Relatório de Benefícios** por funcionário: **![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411048079511)**

1. Em **Relatório de Benefícios por Funcionário** clique em **Parâmetros**.  
   O Sistema apresenta uma janela com os parâmetros referentes ao relatório.
2. Informe os dados conforme orientação dos *helps* de campo.
3. Confira e confirme.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077421994)

**Tabelas Utilizadas**

* SRA – Cadastro de Funcionários
* SRB – Cadastro de Dependentes
* RHK – Planos Ativos Funcionários
* RHL – Planos Ativos Dependentes
* RHM – Planos Ativos Agregados
* SR0 – Itens de Benefícios
* RG2 – Histórico de Benefícios
* SRN – Meios de Transporte
* RFO – Definição de Benefícios
* RIQ – Cálculo de Outros Benefícios
* RIR – Histórico de Outros Benefícios

**Saiba Mais**

[RH - Linha Protheus - GPE - Como cadastrar e calcular assistência médica por faixa salarial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018426472-RH-Linha-Protheus-GPE-Como-cadastrar-e-calcular-assist%C3%AAncia-m%C3%A9dica-por-faixa-salarial?source=search)

[RH - Linha Protheus - GPE - Como cadastrar e calcular assistência odontológica por percentual de salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018671032-RH-Linha-Protheus-GPE-Como-cadastrar-e-calcular-assist%C3%AAncia-odontol%C3%B3gica-por-percentual-de-sal%C3%A1rio?source=search)

[RH - Linha Protheus - GPE - Como excluir / cancelar o cálculo do plano de saúde](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054180934-RH-Linha-Protheus-GPE-Como-excluir-cancelar-o-c%C3%A1lculo-do-plano-de-sa%C3%BAde?source=search)

[RH - Linha Protheus - GPE - Atualização e Cálculo de Benefícios - VT, VR e VA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050068874-RH-Linha-Protheus-GPE-Atualiza%C3%A7%C3%A3o-e-C%C3%A1lculo-de-Benef%C3%ADcios-VT-VR-e-VA?source=search)

[RH - Linha Protheus - GPE - Rotinas envolvidas nos cálculos de Benefícios - VR/VA/VT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050523113-RH-Linha-Protheus-GPE-Rotinas-envolvidas-nos-c%C3%A1lculos-de-Benef%C3%ADcios-VR-VA-VT?source=search)

[RH - Linha Protheus - GPE - Como Cadastrar e Calcular o Vale Transporte](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029037011-RH-Linha-Protheus-GPE-Como-Cadastrar-e-Calcular-o-Vale-Transporte?source=search)

[RH - Linha Protheus - GPE - Como descontar valor Fixo de Vale Transporte](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406270401047-RH-Linha-Protheus-GPE-Como-descontar-valor-Fixo-de-Vale-Transporte?source=search)

[RH - Linha Protheus - GPE - Cadastro e Cálculo do Vale Alimentação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028910152-RH-Linha-Protheus-GPE-Cadastro-e-C%C3%A1lculo-do-Vale-Alimenta%C3%A7%C3%A3o?source=search)

[RH - Linha Protheus - GPE - Como Cadastrar e Calcular o Vale Refeição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028852992-RH-Linha-Protheus-GPE-Como-Cadastrar-e-Calcular-o-Vale-Refei%C3%A7%C3%A3o?source=search)

[RH - Linha Protheus - GPE - Como cadastrar plano de saúde com valor fixo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050979513-RH-Linha-Protheus-GPE-Como-cadastrar-plano-de-sa%C3%BAde-com-valor-fixo?source=search)
