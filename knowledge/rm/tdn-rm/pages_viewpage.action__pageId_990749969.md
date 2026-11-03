---
content_hash: 30356f102708469e22b5f07eb94d33b53b722e80dca04a67e90b2add7638a6e8
fetched_at: '2026-06-29T00:12:16.468017+00:00'
page_id: '990749969'
product: rm
source: tdn-rm
title: DT - Integração RM X Feedz - Chefe Substituto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=990749969
version: 19
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Integração RM X Feedz - Chefe Substituto |
| País: | Brasil |
| Story: | [DRHROTRM-14780](https://jiraproducao.totvs.com.br/browse/DRHROTRM-14780) |

## **02.** **RELEASES**

* 12.1.2410.301
* 12.1.2502.211
* 12.1.2506.157 e superiores

## **03. SITUAÇÃO/REQUISITO**

Tratar o envio das informações de chefes e supervisores, permitindo definir se o substituto deve ser considerado ou não na integração entre Folha de Pagamento e Gestão de Desempenho da Feedz.

Atualmente ao realizar a associação de líderes, o substituto é enviado automaticamente como padrão.

## **04. SOLUÇÃO**

Foi implementado, no menu Configurações | Parametrizador | Integrações | TOTVS RH Performance e Metas / Feedz, o parâmetro **“Enviar Chefe/Supervisor Substituto”**, que permite definir se os chefes e supervisores com a flag **“Chefe/Supervisor Substituto”**, disponível no menu Administração de Pessoal | Chefes e Supervisores, devem ser incluídos no envio de dados na integração entre a Folha de Pagamento e o Gestão de Desempenho da Feedz.

### **PONTOS DE ATENÇÃO**

**1 -** Por regra de negócio, o parâmetro **“Enviar Chefe/Supervisor Substituto”** virá **desmarcado por padrão** na atualização do release.

**2 -** Quando o parâmetro acima estiver **desmarcado**, os chefes/supervisores que tiverem a flag **“Chefe/Supervisor Substituto”** marcada em seu cadastronão serão enviados na integração.

**3 -** Ao executar o menu Administração de Pessoal | Chefes e Supervisores | Substituição de Chefes e Supervisores ou o processo Definir Substituto no Meu RH ou Portal RM, o sistema insere automaticamente o substituto com a flag **“Chefe/Supervisor Substituto”** marcada.

**4 -** É imprescindível que, ao cadastrar um substituto, o chefe ou supervisor permanente esteja com a **Data Final** superior à competência ou com o campo **“Sempre Válido”** marcado, garantindo que o funcionário não fique sem chefe ou supervisor associado na **Feedz**.

**5 -** Com a implementação deste parâmetro, ao processar a integração com as flags **“Fazer Associação de Líderes”** e **“Prioriza chefe master no envio”** marcadas na tela, a ordem de prioridade para envio do chefe/supervisor passa a desconsiderar inicialmente aqueles que possuem o parâmetro **“Chefe/Supervisor substituto”** marcado. Em seguida, o sistema continuará validando a flag **“Master”** no cadastro de chefe/supervisor.

**Exemplo:**

* + Supervisor e Chefe com o master desmarcado: Será priorizado o envio do Chefe.
  + Supervisor e Chefe com o master marcado: Será priorizado o envio do Chefe.
  + Supervisor com o master marcado e Chefe desmarcado: Será priorizado o envio do Supervisor.
  + 2 Chefes no mesmo nível de seção com o master desmarcado: Será enviado o Chefe com a menor chapa.
  + 2 Chefes no mesmo nível de seção com o master marcado: Será enviado o Chefe com a menor chapa.

**Sendo que:**

* + Quando há mais de um chefe ou supervisor na mesma seção, é considerado o chefe com a menor chapa.
  + São considerados tanto o chefe quanto o supervisor. O supervisor é enviado apenas se não houver chefe na seção ou na hierarquia.

### **Exemplo de como será apresentado os dados na Feedz**

Em uma seção com dois chefes, apenas o substituto possui a flag **“Chefe/Supervisor Substituto”** marcada.

Ao enviar os funcionários e realizar a associação de líderes, será enviado o chefe original da respectiva seção.

## **05****. DOCUMENTAÇÃO**

* [Integração RM X Feedz](https://tdn.totvs.com/pages/viewpage.action?pageId=785614408)
* [Substituição de Chefes e Supervisores](https://tdn.totvs.com.br/pages/releaseview.action?pageId=593259892)
* [Chefes e Supervisores](https://tdn.totvs.com.br/display/LRM/Chefes+e+Supervisores)
* [Chefes e Chefes Externos](https://tdn.totvs.com.br/display/LRM/Chefes+e+Chefes+Externos)
* [Supervisor e Supervisor Externo](https://tdn.totvs.com.br/display/LRM/Supervisor+e+Supervisor+Externo)
