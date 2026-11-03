---
article_id: 360019471832
category: RH - Folha de Pagamento
content_hash: 1f46b2dcd74c82c8d293bcf6b34680b4204de6fdf96348d673d2195cdd1d0194
fetched_at: '2026-06-28T22:44:16.150269+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Percentual de cálculo de I.R. para funcionários
  residentes no exterior
type: support-article
updated_at: '2025-08-13T15:01:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019471832-RH-Linha-Protheus-GPE-Percentual-de-c%C3%A1lculo-de-I-R-para-funcion%C3%A1rios-residentes-no-exterior
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26252136299543) Tempo aproximado para leitura: 00:01:30 min**

**Dúvida**Como parametrizar o percentual de cálculo de I.R. para funcionários residentes no exterior?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Procedimentos para utilização:

1. Em **Gestão de Pessoal** (SIGAGPE) acesse Atualizações > Funcionário > Histórico Contrato (GPEA900);

2. Selecione um contrato, clique na pasta **Residente no Exterior** e verifique a disponibilização do novo campo Perc. IR;

3. Informe no **campo Perc. IR**., o respectivo percentual para cálculo do imposto de renda e confirme;

Para cada contrato de funcionário residente no exterior, deve ser informado o percentual de cálculo de I.R. a ser calculado na folha mensal, considerando a legislação vigente e convênios existentes no País.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26252136304919)

4. Acesse Miscelânea > Cálculo > Folha (GPEM020);

5. Informe os parâmetros de acordo com o **Mês e Ano em aberto** (MV\_FOLMES) e efetue o cálculo da folha mensal;

6. Acesse Atualizações > Lançamentos > Mensal (GPEA090);

7. Selecione o **funcionário expatriado que possui o Histórico de Contrato**, cujo percentual IR foi informado. Visualize os lançamentos do imposto de renda calculados, conforme o percentual informado.

**Observações:**  
O cálculo com o percentual de IR informado no Histórico de Contrato dos funcionários expatriados, somente será realizado conforme as seguintes condições:

-O campo Residente no Exterior (**RA\_RESEXT**) do Cadastro de Funcionários (GPEA010) deve estar configurado com a **opção Sim** para o funcionário expatriado;

-As datas de Início e Fim do respectivo Histórico de Contrato, devem estar de acordo com o Mês e Ano em aberto (MV\_FOLMES):

a) A Data de Início deve ser menor ou igual ao Mês/Ano em aberto;

b) A Data Final deve ser maior ou igual ao Mês/Ano em aberto ou em branco, indicando prazo indeterminado para o contrato.

Para percentual de IR zerado, somente será apresentada a verba Base de Cálculo do IR, não havendo o desconto.  
**Para as demais situações**, será considerado o percentual padrão igual a 25%.

-O cálculo do IRRF é feito na verba de ID0066

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[Percentual cálculo IR para funcionários residentes exterior](http://tdn.totvs.com/pages/viewpage.action?pageId=233759652)
