---
article_id: 40562887130903
category: Financeiro - Aplicação / Emprestimos
content_hash: d024a94d30534d914c75894e0f6f3e67e79c7d122d91467fadb4fd9ae911884d
fetched_at: '2026-06-28T22:37:59.376201+00:00'
product: protheus
section_id: 1500001550542
source: central-protheus
title: Cross Segmentos - Backoffice linha Protheus - SIGAFIN - FINA716 Como funciona
  a opção "Considera dias úteis?" para o juros pré-fixado (CBD) no template
type: support-article
updated_at: '2026-06-15T12:28:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40562887130903-Cross-Segmentos-Backoffice-linha-Protheus-SIGAFIN-FINA716-Como-funciona-a-op%C3%A7%C3%A3o-Considera-dias-%C3%BAteis-para-o-juros-pr%C3%A9-fixado-CBD-no-template
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40562933180439) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
FINA716 Como funciona a opção "Considera dias úteis?" para o juros pré-fixado (CBD) no template  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Financeiro - A partir 12.1.2310  
  
**Solução**  
O juros compostos pode ser utilizado tanto na rotina de aplicação como na rotina de empréstimo.

E no momento do cadastro, existe um pergunte "Considera dias úteis?" que poderá influencia no cálculo do juros pré-fixado (CBD)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40562933182615)

Esse pergunte  "Considera dias úteis?"  somente terá efeito caso no seu template tiver a formula de cálculo de juros pós fixado indexado a um índice.

Totalizando duas formulas atuando em conjunto

Exemplo:

Formula 01 Juros Pós fixado (exemplo CDI) + Formula 02 juros pré-fixado (exemplo CDB)

Caso na Formula 02 juros pré-fixado (exemplo CDB) esteja "Considera dias úteis? = NÃO" o calculo será em cima do valor bruto da aplicação ou empréstimo.

Exemplo:

Inclusão do contrato = 30/08/2024  
Resgate do contrato = 19/09/2024  
Valor do Empréstimo = R$ 3.750.000,00  
Taxas do contrato =  pré-fixado ao ano 3,5360460%   +  100% da taxa DI pós fixado

 - Como é feito o cálculo do juros pré-fixado ao ano 3,5360460%

=(1+taxa a.a%)^(1/dias no ano)-1

=(1+3,536046%)^(1/360)-1

=0,0096531% juros ao dia.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41230254929687)

 - Como é feito o cálculo final do juros

=valor do contrato \* (1+taxa ao dia%)^Quantidade de dias entre parcelas - valor do contrato  
=3.750.000,00 \* (1+0,0096531%)^20- 3.750.000,00

**=R$ 7.246,50   "Considera dias úteis? = NÃO"**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41230254931095)

Referente a imagem acima:

**Formula da coluna D**  =(1+B3)^(1/C3)-1  
**Formula da coluna G**  =F3-E3

**Formula da coluna H**  =A3\*(1+D3)^(G3)-A3

2)  Se for utilizado o **"Considera dias úteis? = SIM"**

O sistema irá precisar que seja primeiro atualizado a primeira formula indexada referente ao índice pós fixado (ex: CDI) para depois pegar o valor atualizado CDI e aplicar o formula do pré-fixado CDB

**=R$ 7.286,44 "Considera dias úteis? = SIM"**

Segue o Exemplo:

Cadastro Índices Financeiros

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40562933184791)

Cadastro de atualização de Índice dia a dia conforme o histórico "Série Histórica do DI"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40562887105687)

 - Cadastro de template

Veja que o CDB Pré-fixado **"Considera dias úteis? = SIM"**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40562887107351)

Cadastro do Empréstimo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40562933187223)

 - Provisão das parcelas

**Observação**: Nesta tela não será provisionado o valor de juros referente "100% da taxa DI pós fixado", pois como essa informação geralmente ainda vai sair, o sistema somente irá fazer o cálculo no momento do resgate.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40562933190935)

 - Logado na data do dia 19/09/2024  
E efetuar o resgate

Veja que:

O juros pós fixado = R$ 20.669,46  
O juros pré-fixado = R$ 7.286,44 **"Considera dias úteis? = SIM"**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40562933192599)

Saiba mais:

[FINA716 Como é feito o cálculo dos juros compostos em uma aplicação ou empréstimo?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27324210803735-Cross-Segmentos-Backoffice-linha-Protheus-SIGAFIN-FINA716-Como-%C3%A9-feito-o-c%C3%A1lculo-dos-juros-compostos-em-uma-aplica%C3%A7%C3%A3o-ou-empr%C3%A9stimo)

[FINA716 - Como é efetuado o calculo do juros nas parcelas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13782176773527-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA716-Como-%C3%A9-efetuado-o-calculo-do-juros-nas-parcelas)
