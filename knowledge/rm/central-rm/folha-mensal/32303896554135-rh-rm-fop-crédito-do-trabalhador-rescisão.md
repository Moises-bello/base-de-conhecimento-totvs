---
article_id: 32303896554135
category: Folha Mensal
content_hash: 7d5fa702f76b305bbb7fb32662f72ec4fc39d33dc66ea2a91fc2a12b20823db3
fetched_at: '2026-06-28T22:46:58.082173+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Crédito do Trabalhador - Rescisão
type: support-article
updated_at: '2025-07-04T20:03:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32303896554135-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-Rescis%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32303896470679) Tempo aproximado para leitura: **00:05:28 min**  
**Dúvida**

Conforme a nova modalidade de crédito trabalhador, como parametrizar o sistema RM para que o desconto seja aplicado corretamente no cálculo da rescisão?

**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos patches:

12.1.2406.277

12.1.2410.229

12.1.2502.145

12.1.2506 e superiores

**Solução**

**Observação:**

*É importante destacar que o sistema não realiza o cálculo de 35% sobre o valor líquido da rescisão para definir o valor a ser descontado do Crédito Trabalhador.*

*No cálculo da rescisão, o sistema irá descontar o valor da parcela prevista no contrato do empréstimo, respeitando a margem consignável já estabelecida (normalmente até 35% da remuneração base, considerando os eventos parametrizados). **O restante das parcelas que não foram descontadas será lançado para desconto em um próximo vínculo empregatício do funcionário.** Para mais informações sobre o tema, clique no link:* [*Manual Operacional do Empregador*](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/manual-operacional-do-empregador-programa-credito-do-trabalhador-v2-16-05-25.pdf?utm_source=chatgpt.com)

Para realizar as parametrizações corretamente, verifique os passos abaixo: 

1. **Cálculo da Rescisão sem Provisionamento (Dados Fictícios):**

Primeiramente, foram informados os eventos a serem considerados para a Base Remuneração do funcionário. Os eventos foram inseridos em**Anexos | Eventos Remuneração Crédito do Trabalhador**: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32303896473111)

1.1 No cadastro do empréstimo existem as seguintes informações: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32303900737431)

1.2 Logo após, acesse **Funcionários | Ícone de Rescisão**, faça o cadastro e clique em **Calcular**. Será aberta a tela com os Parâmetros da Rescisão onde será necessário marcar a flag 'Lançar' para que o empréstimo seja lançado no envelope. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32303896476311)

1.3 Observe que os eventos de Código de cálculo 480 (Desconto Crédito Trabalhador) e o evento de Código de cálculo 482 (Base Remuneração) foram lançados no movimento de rescisão: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32303896478743)

No log de cálculo as informações ficaram da seguinte forma: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32303900741527)

**Importante:** Lembrando que no Evento de Código de cálculo 480, o sistema considera os eventos que foram informados nos Anexos do funcionário. Os eventos de IRRF e INSS são considerados automaticamente sem a necessidade de informá-los. 

Ou seja, o sistema realiza o seguinte cálculo: Proventos- Descontos.

(9.360,85 + 2.340,21) = **11.701,06 é o valor dos proventos.**

Agora, iremos realizar o cálculo considerando o valor da soma dos proventos - os descontos. Ficará da seguinte forma: (11.701,06 - 876,95 - 192,95 - 418,41 - 2.496,52) = **7.266,23 é o valor total da remuneração conforme informado no log de cálculo.**

2. **Cálculo da Rescisão com Provisionamento (Dados Fictícios):**

2.1 No cadastro de empréstimos existe o seguinte cadastro: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32303900743191)

2.2 No período 2 foi lançado o provisionamento no lançamento do adiantamento - perceba que não foi lançado o valor integral do empréstimo no provisionamento porque o adiantamento não atingiu o valor total da parcela do empréstimo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32303896485783)

**Importante:** Esse evento de provisionamento não poderá ter Natureza de Rubrica 9253 - Empréstimo eConsignado - Desconto. 

2.3 Ao lançar a rescisão é necessário marcar a flag para lançar empréstimos conforme exemplo abaixo -

Nesse caso o teste foi com o parâmetro informado manualmente, observe que foi selecionado para descontar apenas a parcela atual: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32303900748439)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32303900749975)

2.4 Observe que os eventos de Código de cálculo 484, Código de cálculo 480 e Código de cálculo 482 foram lançados no envelope de rescisão:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32303900751895)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32303896493335)

No log de cálculo, as informações ficaram da seguinte forma: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32303900757655)

3. **Cálculo da Rescisão considerando Eventos do Crédito Trabalhador na Rescisão:**

3.1 Em **Configurações | Parametrizador | Folha Normal | Eventos do Crédito Trabalhador**, foram inseridos os eventos que devem ser considerados para o cálculo da margem consignável do empréstimo para todos os funcionários: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32303896496407)

**Dica:** Caso tenha eventos a considerar exclusivamente para um funcionário, poderá informar quais eventos quer considerar para a margem consignável do desconto do empréstimo da modalidade 'Crédito do Trabalhador eSocial' usando o anexo Eventos Remuneração Crédito Trabalhador. 

3.2 No cadastro, o empréstimo está com as seguintes informações:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32303900759575)

3.3 Lançamento dos eventos do empréstimo na rescisão: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32303900761111)

A margem consignável foi calculada considerando:

1. Eventos cadastrados no parametrizador anteriormente;
2. Valores de INSS e IRRF calculados na rescisão.

**IMPORTANTE:** Veja que o valor do IRRF FÉRIAS também foi considerado porque deverá considerar todos os eventos de INSS e IRRF lançados no período do cálculo onde está descontando o empréstimo.

4. Sobre o valor total da remuneração será calculado o percentual para a margem consignável informado no cadastro do empréstimo para verificar se desconta o valor integral do empréstimo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32303896503831)

**SAIBA MAIS:**

* [RH - RM - FOP - Dúvidas frequentes: Crédito do Trabalhador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33227187529495-RH-RM-FOP-D%C3%BAvidas-frequentes-Cr%C3%A9dito-do-Trabalhador)
* [FAQ - Crédito do Trabalhador](https://tdn.totvs.com/pages/releaseview.action?pageId=946423249)
* [Crédito do Trabalhador - Linha RM - Medida Provisória Nº 1.292, de 12 de Março de 2025](https://tdn.totvs.com/pages/viewpage.action?pageId=925361639)
