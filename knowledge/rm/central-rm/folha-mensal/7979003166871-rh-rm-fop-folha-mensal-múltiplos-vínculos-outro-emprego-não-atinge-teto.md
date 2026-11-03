---
article_id: 7979003166871
category: Folha Mensal
content_hash: 0855d09b32018913db00295ca1995de0dfb1d06a8f86f66a94828266bfd53ab9
fetched_at: '2026-06-28T22:46:59.134131+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Folha Mensal: Múltiplos Vínculos Outro emprego Não Atinge
  Teto'
type: support-article
updated_at: '2024-06-13T18:25:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7979003166871-RH-RM-FOP-Folha-Mensal-M%C3%BAltiplos-V%C3%ADnculos-Outro-emprego-N%C3%A3o-Atinge-Teto
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24163836246295)**Tempo aproximado para leitura:**00:04:07 min  
  
Dúvida**  
Como realizar calculo folha mensal Múltiplos Vínculos Outro emprego não atinge o teto?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**

Para solucionar esta dúvida, realize os seguintes passos:  
  
1- Parametrizar o sistema para o processo de múltiplos vínculos para atender o cálculo de INSS conforme o eSocial.

* Para calcular o INSS conforme o eSocial, será necessário marcar o parâmetro “Calcula INSS conforme eSocial” e informar a partir de quando o sistema iniciará a calcular desta forma, em Configurações | Parametrizador | Folha Normal | Geral;
* O sistema não irá trabalhar mais com chapa centralizadora, para atender o eSocial;
* Marcando esse parâmetro em uma coligada, todas deverão estar marcadas;
* O sistema irá validar a base de calculo através do CPF do funcionário.

Acessando o caminho: **Configurações | Parametrizador | Folha normal | Geral**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10168833186711)  
  
2- Foram criados novos códigos de cálculo **do Tipo Base / Valor** para controle do cálculo dos múltiplos vínculos. Diante disso, verifique se eles estão cadastrados no sistema.

Foram criados novos códigos de cálculo para controle do cálculo dos múltiplos vínculos:  
  
[Código de Cálculo 29 - INSS Outro Emprego](https://tdn.totvs.com/pages/viewpage.action?pageId=452719905)  
[Código de Cálculo 181 - Base INSS Outro Emprego Desconto Complementar](https://tdn.totvs.com/pages/viewpage.action?pageId=452719925)  
[417- Base Tributada de INSS Autônomos Múltiplos Vínculo](https://tdn.totvs.com.br/pages/viewpage.action?pageId=492700190)

[418 - Base de INSS Autônomo outro Emprego](http://tdn.totvs.com/pages/viewpage.action?pageId=510508458)

[428 - Base Tributada De Inss Folha Primeira Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857540)

[429 - Base Tributada De Inss Folha Segunda Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857547)

[430 - Base Tributada De Inss Folha Terceira Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857555)

[431 - Base Tributada De Inss Folha Quarta Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857562)

[432 - Base Tributada De Inss 13º Primeira Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857570)

[433 - Base Tributada De Inss 13º Segunda Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857577)

[434 - Base Tributada De Inss 13º Terceira Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857583)

[435 - Base Tributada De Inss 13º Quarta Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857591)

Os códigos de cálculo abaixo deixaram de ser utilizados no processo:

[387 - Base Tributada de INSS Folha Múltiplos Vínculos](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719615)

[388 - Base Tributada de INSS 13º Múltiplos Vínculo](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718955)  
  
3- Informe o evento com código de calculo 181 e código de cálculo 29 em Códigos Fixos dentro do cadastro do funcionário:   
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7978829442711)  
  
Obs.: Informar a Base total que foi utilizada para calcular INSS na outra empresa no evento com cc181 e informar o valor do INSS que foi descontado no evento com cc29.  
  
4- Acessar Grupo de Eventos utilizado para lançamento da folha  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24163852089239)  
  
Marque a flag que corresponde ao "Tipo de Lançamento" que foi informado no código fixo  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24163852097943)  
  
5- Após realizar o lançamento, veja que será descontado o INSS proporcional para não ultrapassar o Teto do INSS.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7978874016791)  
  
Log de calculo:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7978923280791)

**Saiba Mais**

[RH - RM - FOP - Múltiplos Vínculos: Quando utilizar os códigos de cálculo 72, 181 e 29 no cálculo de INSS Múltiplos Vínculos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063693393-RM-FOP-Quando-utilizar-os-c%C3%B3digos-de-c%C3%A1lculo-72-181-e-29-no-c%C3%A1lculo-de-INSS-M%C3%BAltiplos-V%C3%ADnculos-?source=search)
