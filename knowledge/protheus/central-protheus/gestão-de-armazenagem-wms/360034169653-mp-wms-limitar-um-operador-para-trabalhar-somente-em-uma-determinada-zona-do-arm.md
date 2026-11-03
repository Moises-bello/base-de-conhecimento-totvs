---
article_id: 360034169653
category: Gestão de Armazenagem (WMS)
content_hash: fbfc667cbd7f2c32202f80700b658ad379ba93e29c69871f23186aa353c30cbe
fetched_at: '2026-06-28T22:45:48.197889+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: MP - WMS - Limitar um operador para trabalhar somente em uma determinada zona
  do armazém
type: support-article
updated_at: '2025-10-31T19:55:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034169653-MP-WMS-Limitar-um-operador-para-trabalhar-somente-em-uma-determinada-zona-do-armaz%C3%A9m
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36023888858775)**Tempo aproximado para leitura: **00:01:42**  
**Dúvida**Como limitar um operador para trabalhar somente em uma determinada zona do armazém?  
  
**Ambiente**Microsiga Protheus – Gestão de Armazenagem – A partir da versão 11.80  
  
**Solução**Deve ser cadastrada uma **Regra de Convocação - WMSA350** do tipo limitação para a combinação de armazém e funcionário. Estas duas informações serão sempre levadas em consideração para a limitação da convocação.  
  
A chave para busca das regras de convocação de limitação será sempre pelas seguintes informações:  
**Tipo Regra = 1 Limite + Status = 1 Ativo + Armazem + Funcionario + Codigo Zona + Cod. Servico + Cod. Tarefa + Cod. Atividade.**

A aplicação das regras sempre será da mais abrangente para a mais restritiva. Por exemplo, caso seja encontrada uma regra definida com todos os campos em branco, esta regra será utilizada. Uma vez encontrada uma regra mais abrangente, as mais restritivas não serão analisadas, ou seja, as regras de limitação não são cumulativas, apenas uma regra é aplicada a cada movimentação.

Quando as regras de limitação tiverem a informação **Código Zona** preenchido, a validação ocorrerá contra a zona de armazenagem do endereço destino, no caso de entrada, e contra a zona de armazenagem do endereço origem, no caso de saída. Quando for uma movimentação interna entre endereços será avaliada contra, o primeiro endereço que não for estrutura do tipo **Box/Doca.  
  
Saiba mais**Veja mais detalhes deste processo no documento: [Como limitar um operador para trabalhar somente em uma determinada zona do armazém.](https://tdn.totvs.com/pages/viewpage.action?pageId=654944201)  
Também assista ao *Webinar* sobre o cadastro **Regras de Convocação**: [Webinar TOTVS | Regras para a Convocação WMS](https://www.youtube.com/watch?v=TgvM8CA5LpA)
