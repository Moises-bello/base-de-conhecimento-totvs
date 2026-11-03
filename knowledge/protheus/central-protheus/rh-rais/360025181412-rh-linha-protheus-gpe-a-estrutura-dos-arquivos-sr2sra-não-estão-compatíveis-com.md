---
article_id: 360025181412
category: RH - RAIS
content_hash: bc85fd6331aab027b41e5212cde416b93f2e6fbea028771629141c414a7edb95
fetched_at: '2026-06-28T22:44:05.719681+00:00'
product: protheus
section_id: 360000030327
source: central-protheus
title: RH - Linha Protheus - GPE - A estrutura dos arquivos SR2/SRA não estão compatíveis
  com o ano base corrente
type: support-article
updated_at: '2022-03-21T19:43:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025181412-RH-Linha-Protheus-GPE-A-estrutura-dos-arquivos-SR2-SRA-n%C3%A3o-est%C3%A3o-compat%C3%ADveis-com-o-ano-base-corrente
---

**Ocorrência**Ao gerar a RAIS o sistema retorna a seguinte mensagem:  
A estrutura dos arquivos SR2/SRA não estão compatíveis com o ano base corrente  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.17  
  
**Causa**Tamanho do campo R2\_TIPOADM diferente de 2.  
  
**Solução**1. Verificar se o tamanho do campo está diferente de 2, filtrando o campo R2\_TIPOADM na tabela SX3;  
2. Realizar o ajuste via módulo SIGACFG - Configurador, rotina Base de Dados/ Dicionário/ Base de Dados.  
  
Importante que esse ajuste seja feito através do módulo Configurador para que a estrutura (SX3) e a tabela SR2 (Banco de Dados) sejam corrigidas.  
  
**Saiba mais**  
Para verificar as dúvidas mais frequentes sobre a RAIS, acesse o *link*abaixo:  
<https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030327-RH-RAIS>
