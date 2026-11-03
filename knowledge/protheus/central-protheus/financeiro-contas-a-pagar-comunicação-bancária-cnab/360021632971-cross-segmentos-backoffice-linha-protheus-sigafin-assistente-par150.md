---
article_id: 360021632971
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 3eed674ed48466653a1dc331f985d0bf8f20cdb7fc92324bfc325070d686387a
fetched_at: '2026-06-28T22:37:55.089812+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN- Assistente PAR150
type: support-article
updated_at: '2022-05-31T02:14:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021632971-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Assistente-PAR150
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:05:00 min  
  
Ocorrência**Ao tentar gerar o arquivo de remessa através da rotina de arquivo de cobranças (FINA150), o sistema apresenta o assistente PAR150.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Causa**Este incidente ocorre devido a inconsistências referente aos dados de banco, agência, conta e sub-conta (Tabela SEE) informados na rotina arquivo de cobranças (FINA150) no momento da geração do arquivo de remessa.  
  
**Solução**  
1. Verificar se o cadastro Parâmetros de Bancos existe na filial que está logado, no caso na tabela SEE (Comunicação Remota) seja exclusiva.  
2. Verificar se o código da SUBCONTA que está usando para processar, existe para o Banco informado nos Parâmetros da rotina.  
3. Verificar se a tabela 17 (genérica) existe na tabela SX5 (dicionário) para filial que está realizando o processamento.  
4. Verificar no cadastro Parâmetros Bancos se no campo Conta(EE\_CONTA) já está informando o número do dígito.
