---
article_id: 28599927559575
category: eSocial - Eventos Totalizadores
content_hash: 1d0455c2fd230701d8ba8b3ed47a3814f172e111feb5c27d1cbb17f37ed5807b
fetched_at: '2026-06-28T22:47:06.976157+00:00'
product: rm
section_id: 1500000834481
source: central-rm
title: RH - RM - FOP - eSocial - Validações quando o evento de Adiantamento 13° Salário
  não deduz FGTS no eSocial
type: support-article
updated_at: '2025-03-05T17:27:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28599927559575-RH-RM-FOP-eSocial-Valida%C3%A7%C3%B5es-quando-o-evento-de-Adiantamento-13-Sal%C3%A1rio-n%C3%A3o-deduz-FGTS-no-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28599924855063) Tempo aproximado para leitura: **00:03:30 min****Dúvida**Quais validações devem ser realizadas quando o evento de Adiantamento 13° Salário não é deduzido no eSocial?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**No RM Folha de Pagamento, há o Código de Cálculo 35 ou 51 (Rescisão) que deve ser utilizado para deduzir o que já foi pago de 13° Salário ao funcionário, seja em casos em que a empresa antecipou o 13° salário e após precisa encaminhar a segunda parcela do 13° salário; ou em que houve a antecipação do 13° salário e após, houve a rescisão do funcionário.

Em qualquer um dos casos, o eSocial deverá recepcionar o evento que possui Código de Cálculo 35 ou 51 e estornar o FGTS que já foi recolhido anteriormente na antecipação. Caso isso não ocorra será necessário realizar os seguintes passos:   
1. Verificar no envelope do funcionário se o evento de desconto de Adiantamento de 13° Salário, consta com o Código de Cálculo 35 ou 51 e, se o evento consta corretamente parametrizado. Para correta parametrização [CLIQUE AQUI](https://tdn.totvs.com/pages/releaseview.action?pageId=452719279);

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28599924857495)

2. Verificar se o evento de Código e Cálculo 35 foi gerado na Distribuição de Tomador (caso trabalhe com tomador de serviços) e se foi gerado no XML S-1200, S-1202 ou S-2299;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28599927510423)

3. Verificar no portal do governo se o evento de Código de Cálculo 35 consta como **Desconto,** Incidência em FGTS **12 - Base de cálculo do FGTS 13° salário**, com mesmo **Identificador de Rubrica** que foi gerado no S-1200 e com **Início da Validade** igual ou anterior ao evento de remuneração que está encaminhando.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28599927522967)

Neste exemplo a Identificação da Tabela de  rubrica está correta, o Início da Validade é anterior à Rescisão (que ocorreu no dia 27/11/2024), porém a incidência de FGTS consta 00.

Para correção será necessário:

* Criar um S-1010, com data de competência igual, ou anterior a 11/2024;
* O XML S-1010 deve possuir incidência 12 em FGTS;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28599927528599)

* Após o evento S-1010 ser Aceito RET, retificar o S-2299.
