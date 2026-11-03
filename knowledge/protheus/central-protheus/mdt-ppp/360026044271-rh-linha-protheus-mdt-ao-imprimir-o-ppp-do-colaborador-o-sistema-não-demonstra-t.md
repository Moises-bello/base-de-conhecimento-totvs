---
article_id: 360026044271
category: MDT - PPP
content_hash: 47fb881fee22b8830f8f648f9dd30f76a03fe453689a1d8da781913e864b1d83
fetched_at: '2026-06-28T22:44:22.203349+00:00'
product: protheus
section_id: 360010945654
source: central-protheus
title: RH - Linha Protheus - MDT - Ao imprimir o PPP do colaborador o sistema não
  demonstra todos os caracteres da descrição do cargo
type: support-article
updated_at: '2023-12-21T15:06:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026044271-RH-Linha-Protheus-MDT-Ao-imprimir-o-PPP-do-colaborador-o-sistema-n%C3%A3o-demonstra-todos-os-caracteres-da-descri%C3%A7%C3%A3o-do-cargo
---

**Dúvida**O que verificar ao imprimir o PPP do colaborador o sistema não demonstra todos os caracteres da descrição do cargo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Esta documentação refere-se exclusivamente a versão do PPP impresso no Módulo de Medicina e Segurança do Trabalho, rotina MDTR700, não tendo nenhuma relação com o PPP Eletrônico maiores informações consulte:  
[RH - Linha Protheus - MDT - Qual diferença entre o PPP impresso no Módulo Medicina MDTR700 e o PPP da Previdência Social consultado através do APP Meu INSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14223826251287)  
Esse problema na impressão do PPP ocorre pois o parâmetro **MV\_NG2M400** está preenchido com (Não), dessa forma o mesmo limita a impressão para 400 caracteres.  
  
Para correção do incidente basta configurar o parâmetro para (Sim).

Descrição do parâmetro:

![Capturara.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360025096412/Capturara.PNG)  
  
**Saiba Mais**  
[Artigos sobre Medicina e Segurança](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971487-RH-Medicina-e-Seguran%C3%A7a-do-Trabalho)  
[Artigos sobre PPP](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945654-MDT-PPP)
