---
article_id: 360047862853
category: RH - Rescisão
content_hash: b2b97df0fa4ed6151f120cfbfc5de2022583e54a03037d5c41ded2b34a114f5c
fetched_at: '2026-06-28T22:43:52.005317+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular rescisão por força maior
type: support-article
updated_at: '2022-08-29T11:08:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047862853-RH-Linha-Protheus-GPE-Como-calcular-rescis%C3%A3o-por-for%C3%A7a-maior
---

**Dúvida**Como calcular Rescisão por força maior?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17

**Solução**  
Para calcular rescisão por força maior será necessário cadastrar um novo tipo de rescisão na tabela S043 - Manutenção de tabela, conforme exemplificado abaixo:

 Em Atualizações > Definições de Cálculo > Manutenção de tabelas > Tabela S043 - Tipos de Rescisão

A **tabela S043** serve para que o usuário tenha a opção de calcular a rescisão conforme legislação e configurar cada tipo de desligamento.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068799674/mceclip2.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068783554/mceclip1.png)

A **tabela S043** serve para que o usuário tenha a opção de calcular a rescisão conforme legislação e configurar cada tipo de desligamento.

O único cálculo que o sistema não fará é o pagamento em 50% das verbas de 13º salário, Férias Proporcionais e 1/3, pois como não há legislação sobre pagamento em 50% dessas verbas em caso de rescisão por força maior, o sistema sempre calculará integralmente, as demais verbas é possível cadastrar e parametrizar o pagamento na Tabela S043 de acordo com a documentação acima.

Após criar o novo tipo de rescisão acesse a rotina de rescisão em Miscelânea > Cálculos > Rescisão, preencha os dados do cabeçalho utilizando o tipo de rescisão criado e efetue o calculo.

**Saiba Mais**Para adquirir informações adicionais sobre como criar um Novo tipo de Rescisão, acesse o link: **<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004395831-MP-GPE-Como-cadastrar-um-novo-tipo-de-rescis%C3%A3o>**

#
