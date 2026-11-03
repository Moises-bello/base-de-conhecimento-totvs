---
article_id: 4404191850135
category: TAF - Lalur
content_hash: 12e2b21ffe51f37607a3c77951244bf878f77a664727a86173dce442b4dbfc80
fetched_at: '2026-06-28T22:41:31.037252+00:00'
product: protheus
section_id: 4404425263639
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - TAF- Roteiro de cadastros e parametrizações
  para apuração do LALUR/LACS
type: support-article
updated_at: '2023-03-24T18:12:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404191850135-Cross-Segmento-Backoffice-Linha-Protheus-TAF-Roteiro-de-cadastros-e-parametriza%C3%A7%C3%B5es-para-apura%C3%A7%C3%A3o-do-LALUR-LACS
---

**Dúvida**

Passo a Passo de cadastros e parametrizações para apuração do LALUR no TAF  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice Linha Protheus - TAF - Todas as versões  
  
**Solução**

**Passo 1- Cadastro de Complemento de Empresa (TAFA050)**

 Trata-se de um cadastro de informações do empregador previstos pelo Fisco, através do Guia Prático de diversas obrigações acessórias. Para apuração do LALUR deverá ser informado a "[Matriz (C1E\_CODFIL)](https://tdn.totvs.com/display/public/TAF/Complemento+de+Empresa+-+TAFA050+-+TAF+-+P12#ComplementodeEmpresaTAFA050TAFP12-PastaComplementodoEstabelecimento)" [Maiores detalhes](https://tdn.totvs.com/x/WcWFDg).

A inclusão do evento deve ser feita para a filial marcada como matriz no complemento cadastral (TAFA050). A simulação e a apuração do evento irá considerar todas as filiais que fazem parte de uma mesma empresa.

Filial LALUR: [Filial LALUR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053727454-TAF-LALUR-Porque-o-TAF-s%C3%B3-permite-apura%C3%A7%C3%A3o-de-uma-filial-por-Empresa-)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360092088933/mceclip0.png)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9455725699351)

**Passo 2 - Base de calculo LALUR/LACS:**

 Para base de cálculo, o TAF considera apenas lançamentos exportados/lançados na rotina TAFA331.

* Cadastro LALUR (CTBS300) + Exportação de movimento (CTBS001) -> para rotina TAFA331

Passo a passo +  Dúvidas frequentes: [Base de calculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063097093-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS300-TAFA344-Quais-valores-o-TAF-considera-para-Base-de-c%C3%A1lculo-IRPJ-CSLL-)

Obs. A rotina de Lançamento contábeis no TAF (TAFA331) aceita lançamentos MANUAIS, porem deve ser utilizado com muito critério, pois há uma validação entre o saldo do Bloco M (Lalur) e Bloco K (ECF) se o saldo da conta divergir o TAF não exporta as fichas do LALUR/LACS para ECF.

**Passo 3 - Cadastro de Tributos (TAFA430)**

 Deverá ser feito o cadastro dos Tributos IRPJ e CSLL com as respectivas informações para a sua apuração de acordo com o regime desejado. [Maiores detalhes.](https://tdn.totvs.com/x/lgF8Dg)

Necessário informar a alíquota do IRPJ, Alíquota de adição e a parcela isenta.

Para o calculo da presunção da Receita Bruta na "Informações especificas do IRPJ" informar a alíquota de presunção e a descrição da receita, no padrão temos 4 alíquotas que poderão ser informadas.

Não é necessário que todas as alíquotas sejam preenchidas, deve corresponder as receitas conforme atividade da empresa.

obs. Deverá haver o cadastro do IRPJ e outro cadastro para CSLL.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402386844951/mceclip0.png)

Tabela Relacionada:

* T0J – Cadastro de Tributos

**Passo 4 - Evento Tributário (TAFA433)**

Esse cadastro é muito importante e é usado como base para apuração dos tributos, nele também existem opções como a simulação do calculo dos impostos e cópia de eventos tributário visando facilitar os cadastros [Maiores detalhes.](https://tdn.totvs.com/x/UgHRDg)

A inclusão do evento deve ser feita para a filial marcada como matriz no complemento cadastral (TAFA050). A simulação e a apuração do evento irá considerar todas as filiais que fazem parte de uma mesma empresa.

* Cadastro Evento Tributário: [Evento Tributário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404225269527-Cross-Segmento-Backoffice-Linha-Protheus-TAF-TAFA433-Cadastro-do-Evento-tributario-BLOCO-M-e-BLOCO-N)
* Simulação LALUR: [Simulação apuração IRPJ/CSLL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402387769623-Cross-Segmento-Backoffice-Linha-Protheus-TAF-TAFA433-Simula%C3%A7%C3%A3o-apura%C3%A7%C3%A3o-LALUR)

**Passo 5- Contas da Parte B do LALUR**

- Nesse cadastro deve ser criada uma lista de contas que irão afetar a apuração dos tributos. São contas de Adição, Exclusão, Dedução/Compensação de tributo e Compensação de base negativa/Compensação de Prejuízo.  
[Maiores detalhes.](https://tdn.totvs.com/x/V7qFDg)

Compensação de Prejuízo: [Compensação de prejuízo parte B, com reflexo na parte A](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037921673-MP-SIGACTB-LALUR-COMPENSA%C3%87%C3%83O-DE-PREJU%C3%8DZO-PARTE-B-COM-REFLEXO-NA-PARTE-A-)

**Passo 6 - Períodos de Apuração (TAFA444)**

- Nesse cadastro deverão ser incluídos os períodos de apuração de acordo com a periodicidade definida no cadastro do Tributo. É nele que ficam também outras funcionalidades importantes como o encerramento do período, que é a parte  final do processo de calculo dos impostos, geração de guias de arrecadação, inclusão encerramento e reabertura de períodos em lote visando facilitar o cadastro, etc...  
[Maiores detalhes.](https://tdn.totvs.com/x/u-EJE)

[Encerramento, Período e Apuração](https://tdn.totvs.com.br/pages/releaseview.action?pageId=244428177)

A primeira parte deste cadastro é o relacionamento com o tributo cadastrado no passo 2.

* Para empresa de Lucro Real ANUAL: Deverá ser cadastrado mensalmente o período +o período de ajuste anual (01/01/xx ate 31/12/xx selecionando a opção "PER.ANUAL"). Totalizando 13 períodos.
* Para empresa Trimestral, deve ser cadastrado somente os períodos trimestrais. Totalizando 4 períodos.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404193470231/mceclip0.png)

Tabelas Relacionadas

* CWU – Cadastro de Eventos Especiais
* CWV – Cadastro de Período de Apuração

**Passo 7 - Vigência dos Eventos Tributários (TAFA438)**

Para que os eventos tributários possam calcular os impostos, devem ser cadastradas vigências conforme o período de apuração e associadas a cada evento.  
[Maiores Detalhes.](https://tdn.totvs.com/x/TwGdDg)

Cadastro de Vigência: [Vigência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404413683351-Cross-Segmento-Backoffice-Linha-Protheus-TAF-TAFA438-Cadastro-de-vig%C3%AAncia-do-evento-tribut%C3%A1rio)

**Dúvidas Frequentes:**

É possível gerar somente o LALUR pelo sistema ou só é possível gerar se for fazer a ECF?

Resp: Para a apuração do LALUR só utilizamos da ECF o plano de contas, então se já possui plano de contas no TAF (tabela C1O) e não houve alteração e inclusão de conta contábil. Não é necessário exportar o ECF (ctbs001 + ecf) antes de exportar as movimentações para o lalur (ctbs001 + lalur).

Mas se é a primeira vez que esta gerando o ECF, ou esta em um ambiente novo ou mudou de plano de contas, é necessário exportar o ECF primeiro para que o plano de contas seja populado na tabela do TAF (C1O).

Os movimentos, saldos e valores do Lalur, não dependem da ECF para serem apurados. Após a apuração há possibilidade de exportar as fichas do LALUR para o bloco M e N da ECF, nesse caso, o ECF precisa ter sido exportado para o TAF pois a exportação do bloco M e N faz validação com o bloco K da ECF.

[Base de calculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063097093-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS300-TAFA344-Quais-valores-o-TAF-considera-para-Base-de-c%C3%A1lculo-IRPJ-CSLL-)
