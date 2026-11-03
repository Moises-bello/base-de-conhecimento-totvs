---
content_hash: cdbb7c0c456dc009e1a418224b058c9d0493d5039dba3b21992938a656024131
fetched_at: '2026-07-02T19:24:20.399204+00:00'
page_id: '244932005'
product: protheus
source: tdn-tec
title: Duplo click no favoritos do Menu Logix o programa não é executado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244932005
version: 1
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

|  |  |
| --- | --- |
| Situação | Duplo click em programa da área de favoritos do menu Logix MEN1100 não executa programa |
| Ocorrência | Ao acessar o menu MEN1100 via SCHMTL, usando Firefox, IE ou Chrome, após autenticar qualquer usuário, quando existem programas apresentados na tela de fundo (lista de programas favoritos), ao tentar dar duplo click sobre um dos programas favoritos na tela, não executa o respectivo programa. Mas se pressionar o botão direito do mouse e no menu pop-up apresentado, selecionar opção "Executa processo", o programa é executado normalmente. |
| Correção | Corrigido problema no componente TPaintPanel, ao executar o duplo click sobre o componente estava ocorrendo um erro |
| Informações adicionais | * Referente ao chamado: não há chamado associado * Referente à ocorrência: SCHTML-452 * Disponível a partir da build 7.00.131227A - 3.2.0 do SmartClient HTML |
