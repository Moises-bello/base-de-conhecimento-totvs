---
article_id: 8442235970839
category: Escrita Fiscal - Impostos - Cálculos
content_hash: db2f2c3d2e6b52fe273918369bdfc96730e25f399f868409e9c99bb33eb445a2
fetched_at: '2026-06-28T22:39:30.513847+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Alerta ao informar
  Inscrição Estadual de MG no cadastro de Cliente/Fornecedor
type: support-article
updated_at: '2022-08-26T12:33:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8442235970839-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Alerta-ao-informar-Inscri%C3%A7%C3%A3o-Estadual-de-MG-no-cadastro-de-Cliente-Fornecedor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como resolver alerta ao informar Inscrição Estadual de MG no cadastro de Cliente/Fornecedor?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Para o Estado de Minas Gerais, conforme detalhamento abaixo, é necessário que a Inscrição Estadual tenha 13 caracteres, dessa forma para que os cadastros de cliente e fornecedor sejam criados corretamente e assim permitam a validação dessas informações na geração dos arquivos magnéticos, é necessário que sejam acrescentados zeros a esquerda até que se componha uma IE com 13 caracteres.

# Sobre a Inscrição Estadual

Está disponível no site do Sintegra a consulta e validação das Inscrições Estaduais dos Estados, tendo cada Estado sua regra de composição e quantidade de caracteres necessários.

Para o Estado de Minas Gerais, a regra é que a Inscrição Estadual tenha 13 caracteres, como pode ser verificado no site do Sintegra, no link:

<http://www.sintegra.gov.br/Cad_Estados/cad_MG.html>

Neste exemplo, apresentado no site do Sintegra, é possível verificar uma inscrição composta por 13 caracteres:

![](https://tdn.totvs.com/download/attachments/706135215/image2022-8-25_18-35-43.png?version=1&modificationDate=1661464525200&api=v2)

Para consultar uma Inscrição Estadual utilizando o site do Sintegra, ao selecionar o Estado de Minas Gerais é realizado o direcionamento para o portal  deste link <https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc>. Ao informar a IE utilizada como exemplo, na página inicialmente citada do Sintegra, é apresentada sem o zero a esquerda, com menos de 13 caracteres:

![](https://tdn.totvs.com/download/attachments/706135215/image2022-8-25_18-42-58.png?version=1&modificationDate=1661464518580&api=v2)

# Inclusão/alteração no Protheus

No Protheus há validação de acordo com a regra de composição de Inscrição Estadual de cada Estado, dessa forma ao incluir uma IE com menos caracteres é apresentada mensagem e não é possível realizar o cadastro:

![](https://tdn.totvs.com/download/attachments/706135215/image2022-8-25_18-51-18.png?version=1&modificationDate=1661464517973&api=v2)

Para que esta mensagem não seja apresentada, basta que a Inscrição Estadual seja informada com a quantidade necessária de caracteres, conforme regra disponível no site do Sintegra, sendo para o Estado de Minas Gerais 13 caracteres:

![](https://tdn.totvs.com/download/attachments/706135215/CADASTRO_CLIENTE_MG.gif?version=1&modificationDate=1661464515693&api=v2)

# Regras de validação - Arquivos Magnéticos

Ao gerar e validar os arquivos **EFD ICMS/IPI** e **EFD Contribuições** também é realizada uma verificaçãoquanto a quantidade de caracteres informados para as Inscrições Estaduais, gerando erro na validação do arquivo se informado tamanho menor:

![](https://tdn.totvs.com/download/attachments/706135215/image2022-8-25_19-14-25.png?version=1&modificationDate=1661465665830&api=v2)

Dessa forma, não serão realizadas alterações no Protheus até que haja legislação que modifique a regra de validação nos arquivos magnéticos da EFD ICMS/IPI e EFD Contribuições, pois qualquer alteração impactará na validação destes arquivos.

Para mais informações validar no link: <https://tdn.totvs.com/pages/releaseview.action?pageId=706135215>

# Links relacionados

<http://www.sintegra.gov.br/insc_est.html>

<http://www.sintegra.gov.br/Cad_Estados/cad_MG.html>

<http://www.sintegra.gov.br/>

<https://dfe-portal.svrs.rs.gov.br/NFE/CCC>
