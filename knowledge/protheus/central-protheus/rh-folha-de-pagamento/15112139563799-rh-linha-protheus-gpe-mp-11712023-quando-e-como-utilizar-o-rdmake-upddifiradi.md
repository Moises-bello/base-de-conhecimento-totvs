---
article_id: 15112139563799
category: RH - Folha de Pagamento
content_hash: 5928cfecae1aa28c20be44ae32e2a37d9310bb33fafd6c0d85c89d27657bb696
fetched_at: '2026-06-28T22:44:11.910747+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE -  MP-1.171/2023 - Quando e como utilizar o RDMake
  UPDDIFIRADI
type: support-article
updated_at: '2025-08-11T19:39:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15112139563799-RH-Linha-Protheus-GPE-MP-1-171-2023-Quando-e-como-utilizar-o-RDMake-UPDDIFIRADI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15273330202135) Tempo aproximado para leitura: **03:00:00 min**

**Ocorrência**Adequação na base de cálculo do IR mês anterior, para clientes que optaram por regime de caixa no ano calendário, e no cálculo da folha na competência anterior por exemplo (04/2023), foi aplicado a tributação completa, e na competência atual (05/2023) no adiantamento a tributação simplificada, é o mais vantajoso.  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da Versão 12.1.33.  
  
**Causa**Cálculo da folha da competência 04/2023 efetuado no modelo de tributação do IR Completo, e adiantamento da competência e pagamento 05/2023 no modelo simplificado como o mais benéfico, calcula IR incorretamente.

**Solução**

Implementada a possibilidade de geração da diferença de IR no adiantamento, para descontar no líquido da folha através do RDMake **UPDDIFIRADI**.

Pacotes com o RDMake:

**12.1.2310: <https://suporte.totvs.com/portal/p/10098/download?e=1123885> (garantia estendida)**

**12.1.2410: <https://suporte.totvs.com/portal/p/10098/download?e=1170810>**

**[Documentação Técnica UPDDIFIRADI](https://tdn.totvs.com/display/public/PROT/DRHCALCPRT-9306+DT+RDMake+UPDDIFIRADI)**

**Importante**A rotina **UPDDIFIRADI**é um RDMake, portanto deve ser compilada no ambiente e incluída manualmente no menu do módulo SIGAGPE como função de usuário, em algum menu conforme preferência.

Exemplo de disponibilização no Menu, após compilação do RDMake:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15111656637079)

Incluído como função de usuário, neste caminho do Menu do Gestão de Pessoal - Miscelânea - Cálculos - RDMAKE - DIF IR ADI:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15111776578455)

Cenário para Utilização do RDMake:

**1 -** Folha da competência de Abril/2023, paga em 05/05/2023, calculada no modelo Completo de IR:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15111861150871)

**Cálculo de IR:**

Base IR: 5.361,83 (verba 112) - 2.144,73 (verba 401 adiantamento pago 19/04 - Não faz base pois é outro período de apuração) - 576,83 (verba 417) INSS dedução legal  = **2.640,27** (verba 705) Base IR folha

Cálculo IR: 2.640,27 (verba 705) - 189,59 (verba 715) dedução dependente \* 7,50% (alíquota de IR faixa 1) - 158,40 (dedução faixa 1) = **25,40 desconto de IR modelo Completo**

**2 -**Cálculo Adiantamento competência Maio/2023, pago em 19/05/2023:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15112299925783)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15112397365911)

Veja que, no Cálculo do Adiantamento foi adotado como mais benéfico o modelo de cálculo do IR Simplificado, porém considerou no cálculo do adiantamento a verba 721 de Base IRRF mês ante (ID0015), já com o desconto de INSS pois no cálculo anterior (Folha), foi utilizado o modelo de cálculo de IR "Completo".

O sistema efetuou o seguinte cálculo:

**Modelo Simplificado:**

Base IR: 2.144,73 (verba 106) + 2.640,27 (verba 721 com o desconto do INSS) = 4.785,00 (verba 701) Base IR folha

Cálculo IR: 4.785,00 (verba 701) - 528,00 dedução simplificada \* 22,50% (alíquota de IR faixa 3) - 651,73 (dedução faixa 3) - 25,40 (verba 795) IR já descontado na folha = **280,69 desconto de IR mais benéfico.**

**Modelo Completo descartado, por ser o menos benéfico:**

Base IR: 2.144,73 (verba 106) + 2.640,27 (verba 721 com o desconto do INSS) = 4.785,00 (verba 701 e 858) Base IR folha

Cálculo IR: 4.785,00 (verba 701 e 858) - 189,59 dedução dependente \* 22,50% (alíquota de IR faixa 3) - 651,73 (dedução faixa 3) - 25,40 (verba 795) IR já descontado na folha = **356,83 desconto de IR descartado (verba 859).**

Cálculo que deveria ter sido efetuado e o RDMake irá apurar as diferenças:

**Modelo Simplificado, descartado, por ser o menos benéfico::**

Base IR: 2.144,73 (verba 106) + 2.640,27 (verba 721 com o desconto do INSS) + 576,83 INSS folha = 5.361,83

Cálculo IR: 5.361,83 - 528,00 dedução simplificada \* 22,50% (alíquota de IR faixa 3) - 651,73 (dedução faixa 3) - 25,40 (verba 795) IR já descontado na folha = **410,48 desconto de IR.**

**Modelo Completo, mais benéfico:**

Base IR: 2.144,73 (verba 106) + 2.640,27 (verba 721 com o desconto do INSS) = 4.785,00 Base IR folha

Cálculo IR: 4.785,00 - 189,59 dedução dependente \* 22,50% (alíquota de IR faixa 3) - 651,73 (dedução faixa 3) - 25,40 (verba 795) IR já descontado na folha = **356,83 desconto de IR.**

**3 -**Para apurar essa diferença, é necessário seguir os passos abaixo na execução do RDMake **UPDDIFIRADI:**

**-** Apenas será considerado funcionários que possuírem o cálculo do adiantamento no período de 05/2023, no roteiro ADI e no número de pagamento 01 na tabela SRD (Histórico de Movimentos). Ou seja, o período do Adiantamento, pagamento 01 precisa estar fechado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15113420396567)

**-** É necessário que seja efetuado o cadastro manual de um novo período para 05/2023, com número de pagamento 02, contendo apenas o roteiro ADI, necessário que o campo "Per. Ativo" esteja com SIM, no momento da execução do rdmake, pois as informações das diferenças serão gravadas nesse número de pagamento:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15113460669719)

**Observação**

O programa não irá efetuar cadastro automático de período, sendo necessário realizar o processo manualmente.

Caso tenha sido utilizado período com número de pagamento diferente de 01 para cálculo do adiantamento, deverá ser efetuado tratamento manual no código fonte do RDMake disponibilizado na atualização, uma vez que por se tratar de uma função de usuário, é permitido efetuar alterações para se adaptar à necessidade desejada.

**-** Ao executar o RDMake **UPDDIFIRADI**, será exibido a tela abaixo:![](https://centraldeatendimento.totvs.com/hc/article_attachments/15113824496919)

O botão "Abrir" irá abrir a documentação técnica no navegador do usuário.

O botão "Filtrar" permite efetuar filtro conforme campos do cadastro do funcionário, assim como é possível realizar na rotina de cálculo por roteiro.

Ao clicar em "Ok", a rotina irá exibir o aviso abaixo para confirmação do usuário:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15113838716439)

A necessidade desse aviso é para o usuário ter ciência do processo manual que será necessário realizar para a rotina efetuar a apuração corretamente.

Logo abaixo, segue detalhado o passo-a-passo do processamento:

- A rotina irá efetuar filtro no cadastro de funcionário conforme o filtro realizado através do botão "Filtrar". Desses funcionários filtrados, apenas será considerado aqueles que possuírem o cálculo do adiantamento no período de 05/2023, no roteiro ADI e no número de pagamento 01 na tabela SRD (Histórico de Movimentos).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15114072184471)

- A rotina irá carregar as verbas gravadas no cálculo do adiantamento do período de 05/2023, do roteiro ADI e no número de pagamento 01 e irá fazer uma nova apuração de IR. Ao término do processamento, será exibido o log de ocorrência, exibindo o detalhe de cada funcionário que teve diferença gerada, bem como o valor correto e o valor que foi descontado anteriormente:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15114096610711)

- Caso o IR apurado seja maior do que o descontado no cálculo do adiantamento no período de 05/2023, no roteiro ADI e no número de pagamento 01, o sistema irá gravar o IR do adiantamento na verba vinculada ao ID 0009 (I.R. DO ADIANTAMENTO) com o valor da diferença, na mesma data de pagamento, no período de 05/2023, no roteiro ADI, mas no número de pagamento **02.**Por esse motivo, é necessário que seja efetuado o cadastro **manual**de um novo período para 05/2023, com número de pagamento **02**, contendo apenas o roteiro ADI:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15114158096535)Além do IR do adiantamento, também será gerado a verba vinculada ao ID 0045 (Prov. Insuficiência Saldo) de provento de insuficiência de saldo para zerar o líquido desse recibo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15114189094807)

- Após efetuar o fechamento do período, do roteiro **ADI**, pagamento **02** através da rotina GPEM120, o sistema irá demonstrar o IR descontado na verba vinculada ao ID 0012 (I.R. DO ADIANTAMENTO Cód. Base Demo Folha) e a insuficiência de saldo será descontada na folha, na verba vinculada ao ID 0046 (Desc. Insuficiência Saldo). Necessário estar com o período da Folha do mês 05/2023 aberto:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15114293107479)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15114316172567)

- Veja que no cálculo da Folha, a demonstração do valor descontado do IR no Adiantamento (verba 702) já está com os valores corretos **R$ 356,83**, valor calculado no pagamento 01 + valor da diferença calculado no pagamento 02. E a diferença descontada do funcionário,  na verba de insuficiência de saldo 409 (ID0046):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15114473999639)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15114578824087)

**Saiba Mais:**

[https://](https://tdn.totvs.com/pages/releaseview.action?pageId=756458638)[Documentação Técnica](https://tdn.totvs.com/pages/releaseview.action?pageId=756458638)

[https://](https://suporte.totvs.com/portal/p/10098/download)[Link para download do pacote](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/RH_EXPEDICAO_CONTINUA)

[RH - Linha Protheus - GPE - MP-1.171/2023 - Como configurar a nova forma de cálculo de IR no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14626756121367)

[Espaço Fiscal - Totvs](https://www.totvs.com/blog/fiscal-clientes/novo-calculo-de-imposto-de-renda/)

[DOU - MEDIDA PROVISÓRIA nº 1.171, de 30 de ABRIL de 2023](https://www.in.gov.br/en/web/dou/-/medida-provisoria-n-1.171-de-30-de-abril-de-2023-480184173)

[FAQ da Consultoria de Segmentos](https://tdn.totvs.com.br/pages/releaseview.action?pageId=758481181)
