---
article_id: 1500003717761
category: Arquitetura Organizacional (SIGAORG)
content_hash: bf2decb199cfc78b02c0d5a5ef284421e0358022613fed62e972ed9757f2452b
fetched_at: '2026-06-28T22:42:52.959502+00:00'
product: protheus
section_id: 1500000904101
source: central-protheus
title: RH - Linha Protheus - ORG - Para que serve a rotina Movimentação de Postos
  (ORGA030) e como incluir
type: support-article
updated_at: '2025-11-18T18:58:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003717761-RH-Linha-Protheus-ORG-Para-que-serve-a-rotina-Movimenta%C3%A7%C3%A3o-de-Postos-ORGA030-e-como-incluir
---

**Dúvida**Para que server a rotina **Movimentação de Postos** (ORGA030) e como incluir?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Arquitetura Organizacional - Todas as versões  
  
**Solução**Esta rotina tem por objetivo registrar e ocupar cada posição aprovada na rotina movimentação de departamento.  
Para cada posto registra-se a função, o tipo de posto, referência de tabela salarial, salário, custo etc. O posto pode ou não estar ocupado, quando ocupado é relacionado a um registro de ocupantes do posto, conforme cadastro de Funcionários ou de Participantes.  
  
Cada posto de trabalho é gerado a partir das solicitações aprovadas na arquitetura de movimentação de departamento.  
  
O posto é um código único dentro do departamento e a partir de sua criação obtém-se o código da função a que se refere, respectiva descrição, código do centro de custo com carga inicial do departamento, o responsável, data de criação, código da classe salarial, tipo do posto que determina se é uma vaga efetiva ou temporária, o período estabelecido para especificar o controle da longevidade do posto, o seu custo por salário, benefícios e encargos.  
  
Para cada funcionário alocado ao posto, é possível registrar a desocupação, o congelamento, cancelamento e solicitação de aumento, conforme opções de Ações Relacionadas.  
  
Acesse  o Módulo 70 **(SIGAORG)**, no caminho: **Atualizações > Movimento > Postos > Atualizar > Ações relacionadas.**Realize a ação conforme necessidade da empresa podendo ser Ocupar / Desocupar / Cancelar / Congelar ou Solicitar.  
  
![WxoMOrzHKh.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500004018342/WxoMOrzHKh.gif)  
  
**Saiba Mais**  
[Artigos sobre arquitetura Organizacional](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206968028-RH-Arquitetura-Organizacional)  
[Artigos sobre Portal Gestão Capital Humano](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)
