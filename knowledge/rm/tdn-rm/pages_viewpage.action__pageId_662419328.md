---
content_hash: bd9f5d9fcb6d86376b5c3ffdf40c5ed6fd48057b7db4f142d1538c209bdbc42f
fetched_at: '2026-06-29T00:11:16.122363+00:00'
page_id: '662419328'
product: rm
source: tdn-rm
title: Ciclo de Transporte (F6)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=662419328
version: 25
---

**Ciclo de transporte por distância percorrida**

Este parâmetro é usado na integração do TOTVS Obras de Projetos com o App Minha Obra para o cálculo da distância percorrida dos ciclos de transporte que forem desse tipo.

KM  fixa entre os marcadores de distância :

Este campo define um default para a distância fixa em quilômetros entre os marcadores de distância. O valor aqui informado será automaticamente preenchido no  do tipo distância percorrida e será usada no .

**Informa equipamento responsável pela carga:**

Indicativo se deve ser informado nos apontamentos de carga do App Minha Obra o equipamento que foi o responsável pela carga do caminhão ou outro veículo que executará o ciclo de transporte. Será preenchido pelo apontador da carga através da seleção desse equipamento, dentre os equipamentos sincronizados no App Minha Obra.

Caso este campo seja marcado, além de ser exigido o seu preenchimento nos apontamentos de carga do [App Minha Obra](https://tdn.totvs.com/display/public/MOBILE/Guia+de+Uso+-+Minha+Obra#tudo-sobre-funcionalidades-interfaces), a informação do Equipamento Responsável pela Carga passará a ser demonstrada no TOTVS Construção Obras e Projetos nos anexos de  e  dos Ciclos de Transporte  Incluir um Veja mais ou Saiba mais com o link da tela dos apontamentos de Ciclo de Transporte. 

Atenção! Esse parâmetro só pode ser marcado caso o parâmetro de Mobilidade | Equipamento "Tratamento para sincronismo de equipamentos" esteja marcado com a opção 'Sincroniza todos os equipamentos associados aos projetos do coletor'. 

**Campos Complementares a serem exibidos no App Minha Obra**

Permite parametrizar os Campos Complementares dos Apontamentos de Ciclo de Transporte (máximo de 5 campos), cujo preenchimento será realizado no App Minha Obra pelos apontadores da Carga e da Descarga.

Este parâmetro somente estará habilitado se existirem campos complementares de Apontamento de Ciclo de Transporte cadastrados em "Cad. Gerais | Campos Complementares | Apontamentos de Ciclo de Transporte". Saiba mais em

Após realizado o cadastro dos campos complementares, basta informá-los nesse parâmetro, e ficarão disponíveis na tela de , tanto do sistema quanto no [App Minha Obra](https://tdn.totvs.com/display/public/MOBILE/Guia+de+Uso+-+Minha+Obra#tudo-sobre-funcionalidades-interfaces) .

A ordem dos campos complementares definirá a ordem de exibição no App, ou seja, o Campo Complementar 1 será o primeiro a ser exibido na tela do apontamento de carga e de descarga do App Minha Obra, o Campo Complementar 2 será o segundo a ser exibido e assim, sucessivamente.

Cada parâmetro pode ser preenchido com um campo complementar e, na tela de preenchimento dos apontamentos de carga e descarga do App Minha Obra, serão exibidos somente os 5 campos complementares informados nos parâmetros acima, conforme parametrizado em cada projeto, ou seja, podem ser parametrizados campos complementares diferentes em cada projeto.

Os campos complementares dos apontamentos de ciclo de transporte não serão impressos nos comprovantes de carga ou descarga.

A limitação da exibição dos nomes dos campos no App Minha Obra é limitada a 30 caracteres.
