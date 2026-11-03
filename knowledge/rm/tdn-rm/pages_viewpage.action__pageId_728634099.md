---
content_hash: 20dc5f78aafec4da6c3f10da8356e1e83eeb7e81d8195b03bd2bd0992d959134
fetched_at: '2026-06-29T00:11:27.631911+00:00'
page_id: '728634099'
product: rm
source: tdn-rm
title: Índice de Maturidade de Gestão (IMG) no RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=728634099
version: 2
---

O IMG (**Índice de Maturidade de Gestão**) é um índice criado pela TOTVS, em parceria com a FIPE, para analisar o nível de maturidade de gestão das empresas clientes TOTVS, a partir da adoção e do uso da tecnologia no negócio.

O objetivo é demonstrar o quanto você cliente está adotando de nossas soluções, fazendo indicações de rotinas e produtos que possam agregar ainda mais valor ao seu negócio.

A partir do Patch **12.1.2209.140**, os produtos da linha RM estão exibindo em algumas visões de suas funcionalidades um botão, onde irá indicar para o usuário se ele possui sugestões de uso no sistema de acordo com a rotina que está usando e o cálculo de sua jornada (IMG).

**Segue algumas regras sobre este botão do IMG:**

1. Para o botão ser exibido em uma visão de alguma funcionalidade do RM, primeiro o desenvolvimento da Totvs linha RM precisa habilitá-lo.
2. Necessário acesso ao serviço no Azure e IMG para verificar as informações.

**Segue os endereços que precisam estar liberados:**

[**https://analisepreditivarmimg.azurewebsites.net**](https://analisepreditivarmimg.azurewebsites.net/)

[**https://skynet.totvs.com.br**](https://skynet.totvs.com.br/)

     3. O botão somente será exibido caso a classificação do cliente seja menor do que a TOTVS indica para a jornada correspondente a funcionalidade que esteja acessando.

     4. Na primeira vez que o usuário acessar a visão da funcionalidade, será exibido um tooltip com uma mensagem chamando atenção para o botão que contém a indicação do IMG. A partir da segunda vez em diante, caso o usuário não saia do RM.exe e entre de novo, será exibido somente o botão e um hint caso ele passe o mouse sobre o botão.
