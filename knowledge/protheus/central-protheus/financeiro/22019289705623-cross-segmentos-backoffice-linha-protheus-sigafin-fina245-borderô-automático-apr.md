---
article_id: 22019289705623
category: Financeiro
content_hash: 5cedce29ec2ca5bd528e83641098fe29c290bcb7cafdebd0869530b0ca339162
fetched_at: '2026-06-28T22:38:02.991354+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA245 Borderô Automático
  apresentando HELP: F245BANCOS Problema: Não há bancos configurados para geração
  automática de borderôs'
type: support-article
updated_at: '2024-03-12T20:01:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22019289705623-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA245-Border%C3%B4-Autom%C3%A1tico-apresentando-HELP-F245BANCOS-Problema-N%C3%A3o-h%C3%A1-bancos-configurados-para-gera%C3%A7%C3%A3o-autom%C3%A1tica-de-border%C3%B4s
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22019280746135) Tempo aproximado para leitura: **00:10:00 min****Dúvida**FINA245 Borderô Automático apresentando HELP: F245BANCOS Problema: Não há bancos configurados para geração automática de borderôs  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

**Exemplo 1:** Empresa enviado do banco 341 para o banco do fornecedor 033

A empresa trabalha com o banco 341, e o banco do fornecedor é o banco 033, logo no "MATA070 cadastro de banco" da empresa (tabela SA6)  somente possui o banco 341 cadastrado.

Nesta situação a rotina não tem funcionalidade, pois não foi desenvolvida para trabalhar desta forma, pois é necessário que a empresa seja conveniada com o mesmo código de banco do fornecedor, sendo necessário ter somente o código 033 nos cadastros de:

"MATA070 Cadastro de Banco"

"FINA130 - Parâmetros de banco"

**Exemplo 2:** Empresa enviado do banco 341 para o banco do fornecedor 033

A empresa trabalha com o banco 341 e 033, porém via CNAB ou API usa somente o banco 341,  e o banco do fornecedor é o banco 033, então no cadastro "MATA070 Cadastro de Banco" da empresa (tabela SA6)  possui os bancos 341 e 033, porém na rotina "FINA130 - Parâmetros de banco" (tabela SEE) somente possui o cadastro do banco 341

Nesta situação a rotina não tem funcionalidade, pois será necessário que seja cadastrado na rotina "FINA130 - Parâmetros de banco" o banco 033, onde neste cadastro deverá ser marcado o campo

"**Permite PGTO = SIM**" referente ao código do banco do fornecedor conforme a imagem abaixo:

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/22019289658519)](https://centraldeatendimento.totvs.com/hc/article_attachments/22019289658519)

Importante: Não é necessário cadastrar o mesmo número de agência e conta do fornecedor nos cadastros "MATA070 Cadastro de Banco" e "FINA130 - Parâmetros de banco" , somente é necessário ter o código do banco do fornecedor.

Mais informações:

[Borderô Automático (FINA245 - SIGAFIN)](https://tdn.totvs.com/pages/viewpage.action?pageId=312166157)  
[Exemplo do Processo de Borderô Automático (FINA245 - SIGAFIN)](https://tdn.totvs.com/pages/viewpage.action?pageId=312164184)
