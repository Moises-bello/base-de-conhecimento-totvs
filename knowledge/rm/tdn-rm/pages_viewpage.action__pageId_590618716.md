---
content_hash: 033b5298f7f2cd6ad5e2e16480074d6a50c84ac06041a4af934f7043e72be90f
fetched_at: '2026-06-29T00:10:56.076336+00:00'
page_id: '590618716'
product: rm
source: tdn-rm
title: Folha de Pagamento - ATESTADO MÉDICO SEM INCIDÊNCIA EM INSS (CC445)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=590618716
version: 20
---

**A partir das versões:**

* 12.1.27.337
* 12.1.28.243
* 12.1.29.186
* 12.1.31.101
* ou superiores
Cálculo do atestado médico

Durante os primeiros quinze dias do afastamento da atividade por motivo de doença comum, doença ocupacional ou acidente do trabalho, cabe à empresa pagar ao segurado empregado o seu salário integral, porém a contribuição previdenciária patronal, a contribuição de terceiros e o SAT/RAT não incidem sobre esta importância paga pelo empregador referente a esses quinze primeiros dias que antecedem o benefício de auxílio-doença, de acordo com Jurisprudência consolidada do STJ, [Parecer SEI Nº 16120/2020/ME](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes-producao-empresas-e-ambiente-de-testes/#7-23----29-12-2020----parecer-sei-n--16120-2020-me--como-deve-ser-tratada-a-incid-ncia-tribut-ria-nos-15-primeiros-dias-de-afastamento-que-antecedem-o-benef-cio-de-aux-lio-doen-a-), ficaram estabelecidos os critérios para cálculo do atestado médico que antecede ao Afastamento Previdenciário.

**SEGUE ABAIXO O EXEMPLO COM O PASSO A PASSO PARA ADEQUAÇÃO DO [PARECER SEI Nº 16120/2020/ME](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes-producao-empresas-e-ambiente-de-testes/#7-23----29-12-2020----parecer-sei-n--16120-2020-me--como-deve-ser-tratada-a-incid-ncia-tribut-ria-nos-15-primeiros-dias-de-afastamento-que-antecedem-o-benef-cio-de-aux-lio-doen-a-) NA FOLHA DE PAGAMENTO:**

1cadastro de evento

Deverá ser criado um evento com CC445, conforme abaixo:

**OBS: Para que o CC445 esteja disponível, será necessário realizar  algum recalculo ou calculo de eventos.**

Os eventos com códigos de cálculos [445](https://tdn.totvs.com/pages/viewpage.action?pageId=589761956) **NÃO** deverão ter incidências de INSS marcado, conforme print abaixo:

**Atenção:** Este evento deverá ser lançado manualmente ou através do Grupo de Eventos no envelope de pagamento.

Para cálculo da diferença de salário (sobre o evento de Código de Cálculo 445), deverá ser criado um evento com **CC465**, conforme abaixo:

Os eventos com códigos de cálculos [465](https://tdn.totvs.com/pages/viewpage.action?pageId=717693258) **NÃO** deverão ter incidências de INSS marcado, conforme print abaixo:

**Atenção:** 

O evento com CC465 - DIFERENÇA ATESTADO MÉDICO SEM INCIDÊNCIA EM INSS, será lançando no envelope de diferença salarial, após ser calculada pelo módulo Diferença Salarial,  onde o funcionário tenha no envelope original para recálculo, o evento com código de cálculo 445 - ATESTADO MÉDICO SEM INCIDÊNCIA EM INSS. O evento de forma manual no cadastro de eventos.

cadastro do atestado médico

Afastamento cadastrado sem data de retorno e flag 'Afastamento pela previdência social' marcado:

ou com atestados com mais de 15 dias como consequência gerando o afastamento previdenciário.

Lançamento na folha de pagamento

Em casos de o cliente se encontrar nessa situação, foi criado o CC445, para que cliente consiga lançar o evento para fins obrigatórios e em caso de relatórios, como [Sefip](https://tdn.totvs.com/pages/editpage.action?pageId=590043088).

* Em situações que precisarem, basta criar o CC445 conforme descrito anteriormente, lembrando que esse evento deve ser lançado manualmente (quando lançado juntamente com os eventos com códigos de cálculo CC145, ou através do grupo de eventos/manualmente em substituição ao CC145.

No cálculo da diferença salarial (sobre o evento CC 445), deverá ser efetuado o processo de cálculo da diferença salarial e será lançado no envelope o evento com código de cálculo 465 - DIFERENÇA ATESTADO MÉDICO SEM INCIDÊNCIA EM INSS:

Mais Informações

* [PARECER SEI Nº 16120/2020/ME](https://www.gov.br/pgfn/pt-br/assuntos/legislacao-e-normas/documentos-portaria-502/parecer-sei-16120-atualizado.pdf) = Essa alteração é a aplicação do parecer da PGFN da não incidência de INSS Patronal (20% + RAT + Terceiros) **nos primeiros 15 dias de atestado**, quando houver, em seguida o afastamento previdenciário, seja por auxílio doença ou acidente de trabalho.
* Só impacta para os empregadores que tem empregados com atestados de mais de 15 dias no mês e não são optantes do Simples (com exceção do anexo IV).
* Essa não incidência de CPP nos primeiros 15 dias de atestado em caso de afastamento previdenciário é retroativo à comp. 11/2020.
* Esta não incidência de CPP é sobre a importância paga pelo empregador ao empregado nos 15 (quinze) primeiros dias que antecedem o auxílio doença ou acidente trabalho, ou seja, somente se na sequência houver afastamento previdenciário, não se refere a simples atestados menores de 15 dias.
* Em muitos casos daqui pra frente você pode precisar retificar a GFIP e/ou eSocial em função de no momento de lançar o atestado não saber se ele será ou não convertido em um afastamento de fato, já que é a perícia do INSS que define isso.
falseDica

Para que os Códigos de Cálculos sejam disponibilizados no produto para cadastro, é necessário executar qualquer processo de cálculo, como por exemplo, o processo 'Executa Recalculo'.
