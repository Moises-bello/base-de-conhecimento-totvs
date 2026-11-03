---
article_id: 360021799651
category: RH – DIRF
content_hash: 10c8d1592f2f218c7c4fd196edcbfa640bd4a97cd55ef6fe8a3faa6726b2d38f
fetched_at: '2026-06-28T22:44:06.834070+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar a Pensão Alimentícia para geração
  da DIRF
type: support-article
updated_at: '2025-06-16T20:09:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021799651-RH-Linha-Protheus-GPE-Como-configurar-a-Pens%C3%A3o-Aliment%C3%ADcia-para-gera%C3%A7%C3%A3o-da-DIRF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22108477598999) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como configurar a Pensão Alimentícia para geração da DIRF?   
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões.  
  
**Solução**Os valores e dados referente aos beneficiários serão apresentados somente se estiverem no **Cadastro de Beneficiários**(tabela SRQ), então valide se o cadastro esta correto pelo caminho **>Atualizações >Funcionário >Beneficiários (GPEA280)**, é necessário que constem as verbas de desconto de pensão utilizadas durante o ano-calendário:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11134686460567)

Na rotina **Verbas**, pelo caminho **>Atualizações >Definições de cálculos >Verbas**, na aba **Anuais**, o campo DIRF deve estar preenchido com as seguintes incidências conforme o tipo de verba:

**C - Pensão Judicial  
C1 - 13º Pensão Judicial  
C3 - Pensão Judicial (PLR)  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11134658887575)**

Para a geração dos dados para a DIRF a rotina fará a leitura da tabela SRQ - Beneficiários, relacionando as verbas de cada alimentado com as verbas encontradas na tabela SRD - Acumulados, e distribuindo os valores conforme o mês de pagamento.

Os dados dos alimentados são carregados para a DIRF através do registro INFPA, nele devem constar: CPF do Alimentado, Data de Nascimento, Nome e relação de dependência. Abaixo deste registro os valores pagos ao alimentado mês a mês.

Na manutenção da DIRF é possível visualizar os valores mês a mês de cada um dos beneficiários, utilizando a opção Pensão, localizada na rotina **Manutenção Arquivo**, para isso, entre na rotina pelo caminho **>Miscelânea >Dirf >Manutenção Arquivo**:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11134531440663)  
  
Visualize o funcionário e clique em **Outras Ações >Pensão:**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11134586273303)

Os dados serão apresentados conforme abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12422651138455)

**Observação:**

Para tratar a verba de pensão na DIRF, a rotina valida o cadastro de beneficiário e valida a verba de desconto cadastrada. Desta forma caso ocorra alteração na verba durante o ano, efetuar um novo cadastro, criando uma nova linha ou em caso apenas de alteração de verba, para os meses anteriores a alteração, será necessário incluir o valor manualmente na opção Pensão, em Manutenção de arquivo.

**Saiba Mais**

[RH - Linha Protheus - GPE - Onde ficam as informações de Pensão no Validador da DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004776841-RH-Linha-Protheus-GPE-Onde-ficam-as-informa%C3%A7%C3%B5es-de-Pens%C3%A3o-no-Validador-da-DIRF?source=search)

[RH - Linha Protheus - GPE - O que verificar quando o Sistema não gera a verba de pensão 13º salário na DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023797612-RH-Linha-Protheus-GPE-O-que-verificar-quando-o-Sistema-n%C3%A3o-gera-a-verba-de-pens%C3%A3o-13%C2%BA-sal%C3%A1rio-na-DIRF?source=search)

[RH - Linha Protheus - GPE - É possível gerar informe de rendimento em nome do beneficiário demonstrando os valores pagos de pensão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406761453591-RH-Linha-Protheus-GPE-%C3%89-poss%C3%ADvel-gerar-informe-de-rendimento-em-nome-do-benefici%C3%A1rio-demonstrando-os-valores-pagos-de-pens%C3%A3o?source=search)

[RH - Linha Protheus - GPE - Como incluir verbas na base de cálculo da pensão alimentícia](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048504574-RH-Linha-Protheus-GPE-Como-incluir-verbas-na-base-de-c%C3%A1lculo-da-pens%C3%A3o-aliment%C3%ADcia?source=search)
