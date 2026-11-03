---
article_id: 6621525887383
category: Materiais - Compras (SIGACOM)
content_hash: 5c1e63e0cad0a9b026650ce87e3b1f1a4a506100793528d398e12f74f814220a
fetched_at: '2026-06-28T22:41:19.974104+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Impressão do relatório
  Pedido de Compra (MATR110) o  campo USERLGA está gravando como se ocorresse uma
  alteração. Por que?
type: support-article
updated_at: '2022-06-08T12:21:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6621525887383-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Impress%C3%A3o-do-relat%C3%B3rio-Pedido-de-Compra-MATR110-o-campo-USERLGA-est%C3%A1-gravando-como-se-ocorresse-uma-altera%C3%A7%C3%A3o-Por-que
---

**Dúvida**Ao imprimir o relatório Pedido de Compra (MATR110 ), o campo USERLGA está gravando como se ocorresse uma alteração no Pedido de Compra, sendo que somente foi impresso o relatório. Está correto?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Todas as versões  
  
**Solução**

O log de registro ({*}LOG DE REGISTROS{*} - \*\* CFGX025 ) monitora todas as alterações da tabela que foi configurada, com isso os campos C7\_USERLGA será gravado com a impressão do relatório, pois o mesmo faz o controle de vezes que foi impresso (C7\_QTDREEM)

Nesse caso, seria interessante utilizar o log de auditoria ({*}LOG DE CAMPOS{*} - CFGX052 ), que é possível monitorar os campos específicos.

Segue documentação para auxiliar na configuração [[MP - FRAME - Rotinas de Log e Auditoria](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024872752-MP-FRAME-Rotinas-de-Log-e-Auditoria)]

OBS: O log de auditoria ({*}LOG DE CAMPOS){*} não utiliza os campos \_USERLGI E \_USERLGA .

Caso tenha alguma dúvida sobre como configurar, acione a nossa equipe de framework através de um ticket para auxílio.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
