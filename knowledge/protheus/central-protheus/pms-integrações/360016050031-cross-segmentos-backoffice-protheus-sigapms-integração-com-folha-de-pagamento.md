---
article_id: 360016050031
category: PMS - Integrações
content_hash: 3765508cee899ae118c8d133a819cf63db5458636a9c19f414d30a9cf00781cb
fetched_at: '2026-06-28T22:37:16.761503+00:00'
product: protheus
section_id: 1500001550742
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Integração com Folha de Pagamento
type: support-article
updated_at: '2024-02-23T15:11:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016050031-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Integra%C3%A7%C3%A3o-com-Folha-de-Pagamento
---

**Dúvida**Como integrar o Gestão de Projetos com a Folha de Pagamento?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAPMS - A partir da versão 11.80  
  
**Solução:****1) Cadastrar normalmente o funcionário na folha de pagamento**

Cadastro de verbas - Aba incidências - Campo:  "Ag.Custo PMS" RV\_CUSTEMP = SIM

As verbas que serão consideradas para o cálculo de custo, serão as indicadas com a incidência "Ag.Custo PMS" RV\_CUSTEMP = SIM.

O valor total obtido será rateado nas horas em que o recurso foi efetivamente alocado.

Exemplo: Se o custo total da folha for R$300,00 e o recurso foi alocado 10 horas, o custo hora sera de R$30,00

**2) Cadastrar no Gestão de Projetos o Recurso**

No cadastro de recursos do modulo PMS, na aba de custo real:

Campo Tipo de Apuração = Folha de pagamento,  e no campo Matricula, informar o número que o funcionário foi cadastrado (Conseguira carregar a tabela SRA, de funcionários  Folha de PAGAMENTO).

**3) Custo do Recurso PMSA400 - Esta rotina recalcula os custos dos recursos apontados para um projeto no período solicitado.**

O recálculo será efetuado apenas para os que possuem integração com o Ambiente Gestão de Pessoal. Além disso o campo (AE8\_TPREAL) "Tp. Apuração" no Cadastro de Recursos (Pasta Custo Real), deve estar preenchido com a opção "Folha de Pagamento". E o campo (AE8\_CODFUN) "Matrícula" deve ser preenchido com o código do funcionário a partir do Cadastro de Funcionários.

**4) O custo só será apropriado no recálculo dos custos depois do fechamento da folha.**

Se precisar utilizar o custo do mês, pode-se realizar o seguinte processo:

* A - Criar um campo no AE8 com o custo da última folha;
* B - Utilizar o PE "PMS400CAL" para gravar este valor (Link: <http://tdn.totvs.com.br/pages/releaseview.action?pageId=6795275)>
* C - Utilizar um gatilho para preencher o campo do AFU com o valor deste campo, para ficar com o valor aproximado antes do fechamento da folha.

**Saiba mais:**

**[PMS0002 - Gestão de Projetos e Folha de Pagamento](https://tdn.totvs.com/x/IjcaDg)**

[**PMS0000 - Página centralizadora do PMS**](https://tdn.totvs.com/x/Uq9CLg)
