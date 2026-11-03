---
article_id: 41080868422167
category: Materiais - Compras (SIGACOM)
content_hash: 10846d6d5034a2ac18c1a0356a72befadeab29982efd467000d676e60691bf68
fetched_at: '2026-06-28T22:41:21.852487+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - O arquivo XXX
  não pode ser incluído pois já existe na pasta do banco de conhecimento
type: support-article
updated_at: '2026-06-09T11:28:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41080868422167-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-O-arquivo-XXX-n%C3%A3o-pode-ser-inclu%C3%ADdo-pois-j%C3%A1-existe-na-pasta-do-banco-de-conhecimento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41080868412183) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Ao anexar arquivo no Banco de Conhecimento do Novo Fluxo de Compra ocorre o erro "O arquivo não pode ser incluído pois já existe na pasta do banco de conhecimento", como solucionar?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Compras - a partir da Release 12.1.2310

**Solução**

Este incidente ocorre devido a uma validação de segurança e integridade padrão do sistema. O Protheus padrão **não permite a inclusão de arquivos que possuam nomes duplicados** dentro do Banco de Conhecimento. Se um arquivo com o exato mesmo nome (ex: `FICHACADASTRAL.PDF`) já tiver sido anexado anteriormente, o sistema bloqueará a nova inclusão.

Atualmente, não há customizações ou parâmetros disponíveis que permitam sobrescrever arquivos ou ignorar essa validação no momento do anexo via Novo Fluxo de Compras (NFC).

Portanto, será necessário sempre renomear o arquivo quando for colocar no banco de conhecimento pela segunda vez.

Caso se deseje, pode-se registrar uma sugestão de melhoria na Central Colaborativa da TOTVS para que o time de produto avalie ou pode validar a possibilidade de desenvolvimento de um Ponto de Entrada participativo específico para essa demanda.

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Novo Fluxo de Compras - NFC (PGCA010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19838751317655-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Novo-Fluxo-de-Compras-NFC-PGCA010)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
