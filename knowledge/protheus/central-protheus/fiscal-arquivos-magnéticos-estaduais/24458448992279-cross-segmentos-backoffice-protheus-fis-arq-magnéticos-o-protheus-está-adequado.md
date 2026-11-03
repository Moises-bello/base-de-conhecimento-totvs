---
article_id: 24458448992279
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 1786215a1a9f2303e5477f663d3489673f18686149cdaa8589461742cde0e930
fetched_at: '2026-06-28T22:42:09.211977+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - O Protheus
  está adequado para a entrega da DIRBI?
type: support-article
updated_at: '2025-01-17T20:19:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24458448992279-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-O-Protheus-est%C3%A1-adequado-para-a-entrega-da-DIRBI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24458448960535) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**O **Protheus** está adequado para a entrega da **DIRBI – Declaração de Incentivos, Renúncias, Benefícios e Imunidades de Natureza Tributária?**  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Solução**

A transmissão da DIRBI pode ser realizada por intermédio de aplicação disponibilizada no Portal eCAC, da página internet da Secretaria Especial da Receita Federal do Brasil, ou por intermédio de serviço de API próprio, que permite o envio de lotes por meio da Loja SERPRO, cuja URL principal é:  
<https://apicontador-sisenparam.estaleiro.serpro.gov.br>

Fizemos uma análise e segundo contrato de prestação de software não temos a obrigatoriedade de implantação por ser um regime especial. Além da loja da SERPRO monetizar a comunicação e a Totvs não possui uma procuração em nome de seus clientes para realizar a contratação dessas APIs, e por isso não é possível implementar o desenvolvimento do arquivo da DIRBI.

Conforme IN destaca no **Art.11**(abaixo) com isso não temos ação por parte da **TOTVS** para desenvolvimento de arquivo para essa obrigação.  
  
*"Art. 11. Será disponibilizado serviço para que os desenvolvedores de software possam elaborar soluções integradas com os sistemas informatizados da RFB, a fim de permitir a transmissão, via web service, de arquivo gerado por sistema próprio do sujeito passivo, contendo as informações previstas nos leiautes, assinado digitalmente para transformá-lo em um documento eletrônico nos termos da legislação de regência, com o objetivo de garantir a integridade dos dados e a autoria do emissor."*  
  
A elaboração da **DIRBI** será mediante a utilização de formulários próprios do Centro Virtual de Atendimento ao Contribuinte **e-CAC**, disponíveis no site da **Secretaria Especial da Receita Federal do Brasil – RFB** e na Internet pelo endereço eletrônico <https://www.gov.br/receitafederal>, para a apresentação é obrigatória a assinatura digital mediante utilização de certificado digital válido.

**5.** **Informações Complementares - Adequação de nossos produtos TOTVS**  
A DIRBI tem por objetivo, fazer com que as pessoas jurídicas informem os incentivos, renúncias, benefícios ou imunidades tributárias usufruídos, sendo assim, destacamos que nos casos de Regime Especial, Convenções Coletivas, Acordos Sindicais, normas municipais em municípios com menos de 500 mil habitantes, processos judiciais, liminar, mandado de segurança e tudo aquilo que direcionado apenas a uma empresa ou segmento, a Totvs, conforme estabelecido em seu contrato padrão (ano 2019 - cláusula 17.3), não possui obrigatoriedade de implementar em suas linhas de produto padrão.

Caso nosso cliente necessite de algum tratamento ou controle diferenciado que atenda a sua demanda, poderá ser orientado a buscar uma customização ou um Desenvolvimento Participativo que avaliará e desenvolverá um projeto rotina ou sistema de acordo com a particularidade desta norma, desenhada para o seu negócio. Caso o cliente prefira inserir as informações manualmente, recomendamos que nossas linhas de produto sejam flexíveis para permitir essa inserção manual no sistema.

**API Integra Contador**

Atualmente, a DIRBI é elaborada por meio de formulários próprios do e-CAC, acessíveis no site da Receita Federal. No entanto, a IN 2.198/2024 já previa a disponibilização futura de uma API para facilitar a integração dos sistemas de software com a plataforma da Receita. Atendendo a essa previsão, a Receita Federal lançou a API do Sistema de Gestão de Benefícios Fiscais, disponível na plataforma “Integra Contador” da Loja SERPRO. Essa API permite a integração automática dos sistemas de contabilidade com a DIRBI, facilitando o envio e a consulta de declarações.

Ressaltamos, porém, que os serviços do Integra Contador, adquiridos por meio da Loja SERPRO, são pagos e, atualmente, a TOTVS não possui integração com ambientes monetizados. Caso os solicitantes que contrataram o produto não possuam procuração do contribuinte (como software-houses) e queiram realizar serviços em nome do procurador (por exemplo, escritórios de contabilidade), será necessário enviar um documento XML assinado digitalmente pelo certificado digital do procurador, através de um serviço auxiliar de Autenticação de Procurador.

Para maiores informações sobre o API Contador, [clique aqui.](https://www.totvs.com/blog/fiscal-clientes/dirbi-api-do-sistema-de-gestao-de-beneficios-fiscais/)

Segue informações completas sobre o assunto no link abaixo disponibilizado pela Consultoria de Segmentos da **TOTVS**:  
  
**DIRBI – Declaração de Incentivos, Renúncias, Benefícios e Imunidades de Natureza Tributária**  
<https://www.totvs.com/blog/fiscal-clientes/dirbi-declaracao-de-incentivos-renuncias-beneficios-e-imunidades-de-natureza-tributaria/>

**Blog fiscal TOTVS:**  
<https://www.totvs.com/blog/fiscal-clientes/dirbi-api-do-sistema-de-gestao-de-beneficios-fiscais/>

**Orientações**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=859059943>

Por gentileza verifique se sua empresa está elegível a entrega da obrigação, se **SIM**, alinhe junto ao Fiscal da empresa as ações de forma direta no **e-CAC** enquanto não é disponível o leiaute de importação.
