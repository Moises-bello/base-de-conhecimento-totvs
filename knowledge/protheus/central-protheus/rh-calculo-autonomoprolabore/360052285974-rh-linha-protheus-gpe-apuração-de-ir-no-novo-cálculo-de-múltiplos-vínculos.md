---
article_id: 360052285974
category: RH - Calculo Autonomo/Prolabore
content_hash: 63c4d59aaf275f6ee6b5713b236b386d670b04a8f30bc4149785cee1859822e4
fetched_at: '2026-06-28T22:43:15.073009+00:00'
product: protheus
section_id: 360011983113
source: central-protheus
title: RH - Linha Protheus - GPE - Apuração de IR no novo cálculo de múltiplos vínculos
type: support-article
updated_at: '2025-05-07T14:41:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052285974-RH-Linha-Protheus-GPE-Apura%C3%A7%C3%A3o-de-IR-no-novo-c%C3%A1lculo-de-m%C3%BAltiplos-v%C3%ADnculos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19425486474775) Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**Apuração de IR no novo cálculo de múltiplos vínculos.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal -  partir da versão 12.1.25  
  
**Causa**De acordo com a orientação da Consultoria Tributária, disponível no endereço: [Orientações Consultoria de Segmentos - TPPBAJ - Retenção Imposto de Renda para Empregados com Múltiplos Vínculos](https://tdn.totvs.com/pages/viewpage.action?pageId=145359841), é necessário apuração separada do IR por cada fonte pagadora.  
  
**Solução**De forma a flexibilizar a questão da apuração do IR no novo cálculo de múltiplos vínculos (mnemônico **P\_MULTV** ativo), foi criado o mnemônico **P\_TPAPUIR**, que poderá ser configurado da seguinte forma:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084409414)  
  
A diferença na apuração do IR entre as configurações encontra-se disponível abaixo:  
Cadastro de filiais no sistema Protheus:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084409434)

**Observação**: todas as empresas fazem parte do mesmo grupo de empresas, ou seja, é utilizado a gestão de empresas.

**Observação**: os números de CNPJ utilizados no exemplo foram gerados através de sites disponíveis na internet e somente servem para exemplificação.

O funcionário possui os vínculos abaixo:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085590233)  
  
Verifique nos links abaixo o exemplo de cálculo:

* [P\_TPAPUIR com "1"](https://tdn.totvs.com/pages/releaseview.action?pageId=556861963# "P_TPAPUIR configurado com \"1\"")
* [P\_TPAPUIR com "2"](https://tdn.totvs.com/pages/releaseview.action?pageId=556861963# "P_TPAPUIR configurado com \"2\"")
* [P\_TPAPUIR com "3"](https://tdn.totvs.com/pages/releaseview.action?pageId=556861963# "P_TPAPUIR configurado com \"3\"")

**Observação**

Tal implementação altera apenas e exclusivamente a apuração do **IR**; o **INSS** permanece inalterado, isto é, é considerado a base e o desconto já efetuado em vínculo(s) anterior(es) independente da fonte pagadora.

 

**Saiba Mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - MP-1.171/2023 - Como configurar a nova forma de cálculo de IR no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14626756121367)  
[DOU - MEDIDA PROVISÓRIA nº 1.171, de 30 de ABRIL de 2023](https://www.in.gov.br/en/web/dou/-/medida-provisoria-n-1.171-de-30-de-abril-de-2023-480184173)  
[FAQ da Consultoria de Segmentos](https://tdn.totvs.com.br/pages/releaseview.action?pageId=758481181)  
[Espaço Fiscal - Totvs](https://www.totvs.com/blog/fiscal-clientes/novo-calculo-de-imposto-de-renda/)
