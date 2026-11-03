---
content_hash: 2f3293b7c0e5941dbbd88a8aa7420630cbccc67b826eb11c6ed1f33b9b1b9704
fetched_at: '2026-06-29T00:10:42.980101+00:00'
page_id: '549487390'
product: rm
source: tdn-rm
title: MP 932-Percentual SEST/SENAT reduzidos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=549487390
version: 21
---

##### **Dúvida:**

MP 932 - Como deduzir os percentuais SEST/SENAT para autônomos para atender a nova medida provisoria 932?

**Ambie****nte**  
RM – TOTVS Folha de pagamento – Parâmetro disponível a partir dos patchs abaixo: 

* **12.1.24.301**
* **12.1.25.279**
* **12.1.26.225**
* **12.1.27.183**
* **12.1.28.115**

                                                                                          

**Solução**

Para que o percentual de terceiros seja reduzido na geração da Guia de INSS e Folha Analítica foi criado no parametrizador o campo "Percentual SEST/SENAT", onde o usuário informa o percentual que deverá ser utilizado no cálculo do SEST/SENAT para autônomos da folha de pagamento. Caso o percentual não seja preenchido o sistema irá continuar calculando o percentual de 2.5% .

Acessar Configurações | Parametrizador | Folha Normal | Encargos Sociais | Campo Percentual SEST/SENAT

Este campo deve ser preenchido com o percentual desejável para o cálculo dos valores de terceiros para autônomos.

## **Exemplo:**

## **Guia e INSS**

No exemplo abaixo o autônomo tem um valor de prestação de serviço de R$3.000,00 e preencheu o percentual 1,25% no parametrizador:

## **Folha Analítica**
