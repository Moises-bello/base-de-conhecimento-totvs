---
article_id: 4407532460311
category: RH - Integrações
content_hash: c691d1cb05cda64d520cf831f5cfebf5fa8d8f5992d9f34ad3834c865e81f295
fetched_at: '2026-06-28T22:44:47.593837+00:00'
product: protheus
section_id: 32419269542935
source: central-protheus
title: RH - Linha Protheus - PON - Integração Ponto com a Folha com dois períodos
  e mesma verba na RGB
type: support-article
updated_at: '2025-06-13T17:19:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407532460311-RH-Linha-Protheus-PON-Integra%C3%A7%C3%A3o-Ponto-com-a-Folha-com-dois-per%C3%ADodos-e-mesma-verba-na-RGB
---

**Dúvida**Integração Ponto com a Folha com dois períodos e mesma verba na RGB.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução****01. Visão Geral**

A integração do SIGAPON com o SIGAGPE tem a finalidade de levar os resultados (verbas) do período de Ponto, que são apurados na tabela de Resultados (SPB) após o Cálculo Mensal do Ponto, para pagamento na Folha.  
O período de apontamento do ponto e o Período de Cálculo do GPE não são diretamente relacionados, com isso é possível realizar a integração com períodos diferentes entre os módulos.

Este documento apresenta um exemplo de uso onde dois períodos de apontamento são integrados em um mesmo período da folha, mesmo não sendo uma situação usual, demonstra a independência dos módulos.  
  
**02. Exemplo de Utilização**

Para integrar os resultados do Ponto Eletrônico, é preciso ter um período em aberto na Folha de Pagamento em Atualizações > Definições de Cálculos > Períodos

![](https://tdn.totvs.com/download/attachments/630381602/image2021-7-20_11-38-31.png?version=1&modificationDate=1626791911543&api=v2)

Configuração do evento do Ponto para pagamento em Folha:  
1. Na aba Geral é necessário vincular uma verba do GPE ao evento, se atentando ao Tipo de Código (Provento, Desconto, Base Provento ou Base Desconto) e a classificação do evento.

![](https://tdn.totvs.com/download/attachments/630381602/image2021-7-20_11-45-42.png?version=1&modificationDate=1626792342717&api=v2)

2. Na aba Banco de Horas, é necessário definir qual a porcentagem do evento que será gerado para a folha e quanto irá para o banco de horas, neste exemplo a totalidade deste evento será contabilizado em Folha de Pagamento, campo Perc. F. Pagto. = 100,00.

![](https://tdn.totvs.com/download/attachments/630381602/image2021-7-20_11-47-38.png?version=1&modificationDate=1626792458770&api=v2)

Cadastro da Verba 600 - Hora Extra 50% (vinculada ao evento 001) com o campo "Lcto Diário" = S-Sim, dessa forma o GPE permite que a mesma verba seja lançada várias vezes no mesmo período de cálculo, considerando a data como parte da chave do registro.

![](https://tdn.totvs.com/download/attachments/630381602/image2021-7-20_11-52-2.png?version=1&modificationDate=1626792722890&api=v2)

Período de Apontamento atual - 01/06/2021 a 30/06/2021

![](https://tdn.totvs.com/download/attachments/630381602/image2021-7-20_11-56-9.png?version=1&modificationDate=1626792969883&api=v2)

Na rotina Integrados da matricula 166666 no dia 01/06/2021 foi apontado o evento 001 - HE 50% AUT. com 1,30 hrs

![](https://tdn.totvs.com/download/attachments/630381602/image2021-7-20_11-54-27.png?version=1&modificationDate=1626792867247&api=v2)  
  
Após calculo Mensal do período 01/06/2021 a 30/06/2021 visualizo nos Resultados a verba 600 - Hora Extra 50% com data de pagamento 30/06/2021.

A hora do apontamento é demonstrada no formato sexagesimal 1:30, após o cálculo mensal esse valor foi convertido para o formato centesimal, resultando em 1,5 horas   
        ![](https://tdn.totvs.com/download/attachments/630381602/image2021-7-20_12-0-47.png?version=1&modificationDate=1626793247273&api=v2)  
  
Em Miscelânea > Fechamentos > Integração com a Folha informar os parâmetros com período 01/06/2021 a 30/06/2021.A data de vencimento preenchida tem que estar dentro da data do pagamento da tela de resultados e da data do período de apontamento em que está aberto.   
![](https://tdn.totvs.com/download/attachments/630381602/image2021-7-20_12-2-47.png?version=1&modificationDate=1626793367727&api=v2)![](https://tdn.totvs.com/download/attachments/630381602/image2021-7-20_12-3-9.png?version=1&modificationDate=1626793389610&api=v2)        ![](https://tdn.totvs.com/download/attachments/630381602/image2021-7-20_12-3-34.png?version=1&modificationDate=1626793414803&api=v2)![](https://tdn.totvs.com/download/attachments/630381602/image2021-7-20_12-4-25.png?version=1&modificationDate=1626793465763&api=v2)  
  
No modulo GPE na rotina Lançamentos > Por Funcionário na matricula 166666 a verba 600 - H.Extra 50% foi gerada com campo Origem = E, que identifica que a verba é originária do ponto.      ![](https://tdn.totvs.com/download/attachments/630381602/image2021-7-20_12-6-48.png?version=1&modificationDate=1626793608993&api=v2)

No Ponto Eletrônico altero o período de Apontamento para 01/07/2021 a 31/07/2021         ![](https://tdn.totvs.com/download/attachments/630381602/image2021-7-20_12-10-26.png?version=1&modificationDate=1626793826777&api=v2)

Na rotina Integrados da matricula 166666 no dia 01/07/2021 foi apontado o evento 001 - HE 50% AUT. com 2,00 hrs

          ![](https://tdn.totvs.com/download/attachments/630381602/image2021-7-20_12-12-25.png?version=1&modificationDate=1626793945173&api=v2)

Após calculo Mensal do período 01/07/2021 à 31/07/2021 a verba 600 - Hora Extra 50% foi gerada nos resultados com horas = 2,00 e data de pagamento 31/07/2021

          ![](https://tdn.totvs.com/download/attachments/630381602/image2021-7-20_12-14-50.png?version=1&modificationDate=1626794090853&api=v2)

Em Miscelânea > Fechamentos > Integração com a Folha preenchido os parâmetros com período 01/07/2021 a 31/07/2021.  
![](https://tdn.totvs.com/download/attachments/630381602/image2021-7-20_12-2-47.png?version=1&modificationDate=1626793367727&api=v2)![](https://tdn.totvs.com/download/attachments/630381602/image2021-7-20_12-3-9.png?version=1&modificationDate=1626793389610&api=v2)        ![](https://tdn.totvs.com/download/attachments/630381602/image2021-7-20_12-19-33.png?version=1&modificationDate=1626794373920&api=v2)![](https://tdn.totvs.com/download/attachments/630381602/image2021-7-20_12-19-58.png?version=1&modificationDate=1626794398940&api=v2)  
  
  
No modulo GPE na rotina Lançamentos > Por Funcionário na matricula 166666  os 2 lançamentos da verba 600 - H.Extra 50% são mantidos:  
Cod.Verba - 600 - H.Extra 50% - Hrs - 1,50 com campo Origem = E e data de referencia 30/06/2021

Cod.Verba - 600 - H.Extra 50%   Hrs - 2,00 com campo Origem = E e data de referencia 31/07/2021        ![](https://tdn.totvs.com/download/attachments/630381602/image2021-7-20_12-21-24.png?version=1&modificationDate=1626794484193&api=v2)  
  
**Saiba Mais**  
Manual ponto eletrônico: <https://tdn.totvs.com/pages/viewpage.action?pageId=630823373>
