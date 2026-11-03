---
article_id: 360022463371
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: 29227fd60b9b931498ca15d4f9adb30c401daf474476106eee075cd6b4ca915b
fetched_at: '2026-06-28T22:42:07.776190+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Extrator Fiscal
  - Tabela TAFST1, Não Existe
type: support-article
updated_at: '2022-08-18T17:29:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022463371-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Extrator-Fiscal-Tabela-TAFST1-N%C3%A3o-Existe
---

**Ocorrência**Ao acessar o Extrator Fiscal, é apresentada a mensagem que a tabela TAFST1 não existe.  
  
**Ambiente**Microsiga Protheus – Livros Fiscais – A partir da versão 11.80.  
  
**Solução**

1. Realize um DROP das tabelas TAFST1, TAFST2 e TAFXERP;

2. Execute a Wizard de Configuração TAF em: TAF-> Atualizações -> Configs TAF -> Wizard de Configuração;   
3. Confirme através do banco de dados se as tabelas foram recriadas;   
4. Execute o Extrator Fiscal novamente.
