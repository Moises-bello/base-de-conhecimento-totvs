---
article_id: 31152092269591
category: eConsignado (Crédito do Trabalhador)
content_hash: 0289548985858656a5a96e1addd5fa181e652439ab7cecf51c56d64a6385c345
fetched_at: '2026-06-28T22:43:07.259072+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE - eConsignado - Como lançar manualmente em Valores
  Futuros o Credito do Trabalhador (MP nº 1.292/2025) e calcular desconto na Folha
  de Pagamento
type: support-article
updated_at: '2026-01-14T20:13:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31152092269591-RH-Linha-Protheus-GPE-eConsignado-Como-lan%C3%A7ar-manualmente-em-Valores-Futuros-o-Credito-do-Trabalhador-MP-n%C2%BA-1-292-2025-e-calcular-desconto-na-Folha-de-Pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31152120538903) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
eConsignado - Como calcular na folha de pagamento com Credito Trabalhador (MP nº 1.292/2025)?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) GPE - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para realizar o calculo do Empréstimo Consignado Crédito do Trabalhador para atender a Medida Provisória nº1.292/2025 na folha de pagamento, realize os passos abaixo:

**1.** Acesse a rotina **Verbas** em **Atualizações > Definições de Cálculo > Verbas (GPEA040)** cadastre uma verba Tipo **Desconto,** com os campos**Emp. Cons.** preenchido com **Sim, Natureza** preenchido com **9253 e Cd Inc FGTS** preenchido com **31** [RH - Linha Protheus - GPE - Como cadastrar verba de Emprestimo Consignado para atender à Medida Provisória que institui o Crédito do Trabalhador (MP 1.292/2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/31149947210519-RH-Linha-Protheus-GPE-Como-cadastrar-verba-de-Emprestimo-Consignado-para-atender-%C3%A0-Medida-Provis%C3%B3ria-que-institui-o-Cr%C3%A9dito-do-Trabalhador-MP-1-292-2025);

**2.** Acesse a rotina **Mnemônicos** em **Atualizações > Definições de Cálculos > Mnemônicos (GPEA300)** onde foi criado o mnemônico **P\_LIMECONS** que deverá ser ativado com **.T.;**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31290273792407)

Dessa forma será considerado o percentual cadastrado no mnemônico **P\_PERECONS** para realizar o calculo de desconto na folha de pagamento;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32691518223639)

**3.** Acesse a rotina **Valores Futuros** em **Atualizações > Lançamentos > Valores Futuros (GPEA110)** selecione o **Funcionário > Clique em Incluir** (Caso não tenha lançamentos anteriores para o funcionário. Se existirem lançamentos anteriores para o funcionário **Clique em Alterar**) e preencha os campos conforme informações do [Portal Emprega Brasil](https://servicos.mte.gov.br/spme-v2/#/login) consultados no relatório detalhado disponível.:

* **Código da Verba**: Código da nova verba cadastra (preenchimento obrigatório);
* **Valor Principal**: Valor contratado de Empréstimo (preenchimento obrigatório);
* **Número de Parcelas**: Preenchido com a quantidade de parcelas contratadas (preenchimento obrigatório);
* **Empréstimo Consignado**: Informando se o Empréstimo é Consignado (preenchimento obrigatório);
* **Número do Contrato**: Número do contrato de empréstimo (preenchimento obrigatório);
* **Consig. FGTS**: Informar se o Empréstimo consignado tem garantia do FGTS (preenchimento obrigatório);
* **Mat. Inst eConsig.**: Informar a Matricula da instituição Consignatária, cadastrada na Caixa (Código do Banco - preenchimento obrigatório);
* **Observação eConsig.**: Informar observação sobre o empréstimo (Preenchimento opcional);

Após o preenchimento dos campos conforme a necessidade clique em **Salvar**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32249445414551)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32249417303575)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32249417306135)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32249445419671)

**4.** Calcule a folha em **Miscelânea > Cálculos > Por Roteiros (GPEM020)**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32249417308311)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32249417309591)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32249417311511)

**5.** Verifique o calculo em **Consultas > Cadastros > Recibo Pagamento (GPEA630)**, selecione o Funcionário e **Clique em Visualizar**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32249417312663)

Para o calculo da verba E03 é considerado:

Salário - INSS - IRRF = Base de calculo

Base de Calculo \* % do P\_PERCONS = Valor de desconto

R$5000 - R$509,58 - R$335,15 = R$4155,27 (Base de Cálculo)

R$4155,27 \* 35% = R$1454,34 (Máximo a ser descontado)

A parcela lançada é no valor de R$166,66 estando dentro do calculo do percentual de 35%, dessa forma sistema irá gerar a verba E03 do econsignado integral. Caso a parcela seja superior a 35% da base, o sistema só irá calcular os 35%, deixando um saldo a ser quitado pelo funcionário na instituição financeira, e sendo dever do empregador informar referente ao saldo de quitação.

**Observações**

Para **lançamentos manuais** diretamente na rotina de Valores Futuros, **não é necessário** vincular as verbas na tabela **S154 - Verbas Credito do Trabalhador**, tendo em vista que esta tabela **não será validada** quando feito o **lançamento** direto na rotina. Basta **criar** **mais** de uma verba **igual a verba principal** para que cada numero de contrato tenha sua própria verba (exemplo: 15 contratos = 15 verbas).  
  
OBs. Realizado ajuste para reutilização de verba usada em empréstimo pago ou com status descontinuado.  
  
Diferente da rescisão, onde a limitação do desconto ocorre a partir de um **percentual do líquido,** na **folha** o desconto será limitado pela **Margem de consignação**, que será obtida através do seguinte cálculo:  
**Margem de Consignação = Base do INSS - ( INSS + IR + Verbas de Pensão )**  
**Desconto Máximo = Margem de Consignação / 100 \* P\_PERCONS**

Adicionalmente foi criado o mnemônico **P\_DEDCONS** onde poderá ser incluído **outras verbas de desconto** (as verbas aqui informadas devem ser separadas com **barras.** Exemplo: "001/002/003"),  que devam ser **abatidas** da **Margem de Consignação total antes** da aplicação do percentual de desconto máximo.

Esse mnemônico foi criado devido a inexistência de informações completas sobre as verbas que deveriam ser consideradas na formação da base.

**Saiba mais:**

[RH - Linha Protheus - GPE - Como cadastrar verba de Empréstimo Consignado para atender à Medida Provisória que institui o Crédito do Trabalhador (MP 1.292/2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/31149947210519-RH-Linha-Protheus-GPE-Como-cadastrar-verba-de-Emprestimo-Consignado-para-atender-%C3%A0-Medida-Provis%C3%B3ria-que-institui-o-Cr%C3%A9dito-do-Trabalhador-MP-1-292-2025)

[Crédito do Trabalhador](https://tdn.totvs.com/pages/releaseview.action?pageId=944703898)

[RH - Folha Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
