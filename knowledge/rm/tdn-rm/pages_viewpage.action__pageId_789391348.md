---
content_hash: 025b3f8cc0e5027081a7969b21162b635a1a28bf7a35931e36216cff10652395
fetched_at: '2026-06-29T00:11:39.253764+00:00'
page_id: '789391348'
product: rm
source: tdn-rm
title: RM Atualizador - Alertas Versão Expirada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=789391348
version: 3
---

A partir da versão 12.1.2310 foi disponibilizado alertas para apoiar o usuário quanto a correta atualização da versão, identificando possíveis atualizações em versões desatualizadas ou sem a aplicação de patchs e releases mais recentes.

Em situações mais "críticas" será exibido um pop-up com orientações, como por exemplo o caso abaixo onde esta sendo realizada uma atualização para uma versão que já esta fora do calendário de manutenção. (Release expirada)

Quando este pop-up é apresentado, também será exibido na tela de pré-requisitos um alerta, que posteriormente estará disponível no log de atualização da versão.

Em situações de recomendações mais simples como o caso da atualização com patch, mas existindo patch mais recente, não será exibido pop-up, sendo apresentado apenas o alerta na tela de pré-requisitos sobre o patch mais recente disponível.

Na mensagem abaixo o cliente possui um patch mas não é o patch mais recente.

No caso abaixo o cliente esta utilizando uma release que não é a mais recente, o que pode ocasionar em um retrabalho demandando uma nova atualização em breve, visto que a versão irá expirar em breve, além de estar deixando de pegar novidades da próxima versão.

A mensagem abaixo visa orientar o cliente quanto a aplicação de patch na release antes da atualização, sabemos que existe uma prática não recomendada de realização da atualização somente com a execução do instalador da release. Mas é recomendavel que seja aplicado o patch caso ele já esteja disponivel visto que o mesmo pode conter correções de scripts da versão. Neste caso é apresentado o link para download de patch.
