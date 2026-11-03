---
article_id: 4467868569111
category: Materiais - Compras (SIGACOM)
content_hash: 6562c8b6232f73d1f6e6b96295735822be72cbeccdbfd72612acc39512ab538f
fetched_at: '2026-06-28T22:41:24.034441+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Possíveis Causas de
  Lentidão ao Classificar um Documento de Entrada
type: support-article
updated_at: '2022-05-16T21:03:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4467868569111-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Poss%C3%ADveis-Causas-de-Lentid%C3%A3o-ao-Classificar-um-Documento-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Ao classificar o Documento de Entrada, a rotina apresenta travamento.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12  
  
**Solução**1. Verifique se há divergência no compartilhamento das tabelas CTG e CQD;

2. Realize um teste desabilitando as contabilizações online através do pergunte do MATA103 - Contabiliza online = Não;

3. A partir da release 33 o parâmetro MV\_NFEDVG estará disponível automaticamente e deve ter seu conteúdo = F

Observação: para *releases* inferiores, somente em pacote de expedição contínua e surtirá efeito somente caso os fontes **MATA103, MATA140 e COMA040** estiverem com data maior ou igual a 26/01/2021.

O parâmetro pode ser inserido manualmente via **SIGACFG**(Configurador):

![imagem1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4468654123927/imagem1.png)

4. Atualização de binários (DbAccess, Appserver e Smarclient)

5. Desabilitando todas customizações pelo catálogo e incluindo a IXBLOG=NORUN. Para maiores detalhes sobre como desabilitar, [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021114292)

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
