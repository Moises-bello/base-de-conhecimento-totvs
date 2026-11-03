---
article_id: 29255211655703
category: RH - Folha de Pagamento
content_hash: 04ef370bf07bbc3dc076d62b566969f54dfca10f9f55b1e09c650a9c9094f519
fetched_at: '2026-06-28T22:44:14.938780+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: 'RH - Linha Protheus - GPE - Erro de carga de Fórmulas - Nao Foi Possivel Criar
  o Diretorio: \outsourcing\totvs\protheus_data\formpath\rpofrm01 Para a Compilacao
  das Formulas'
type: support-article
updated_at: '2025-09-04T19:18:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29255211655703-RH-Linha-Protheus-GPE-Erro-de-carga-de-F%C3%B3rmulas-Nao-Foi-Possivel-Criar-o-Diretorio-outsourcing-totvs-protheus-data-formpath-rpofrm01-Para-a-Compilacao-das-Formulas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29255224151703) Tempo aproximado para leitura: **00:01:00 min** **Ocorrência**Ao executar rotinas de cálculos no Sistema, gera o log: Não Foi Possível Criar o Diretório \outsourcing\totvs\protheus\_data\formpath\rpofrm01 Para Compilação das Fórmulas ?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29255224152343)  
  
**Causa**  
Log ocorre pois ou o diretório apontado no appserver.ini não existe no servidor ou o diretório esta com permissões inválidas para acesso.  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12  
  
**Solução**É necessário verificar com a equipe Cloud se o diretório que consta no appserver.ini é válido para a criação da pasta RPOFRM e se as permissões do diretório são válidas para geração do RPOFRM.

**Saiba mais:**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
