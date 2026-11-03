---
content_hash: 775b61477a2108c5e92cf44220ebb40b99c2cea63f38f137fbfff5497a7e7e3d
fetched_at: '2026-06-29T00:10:22.035533+00:00'
page_id: '496032263'
product: rm
source: tdn-rm
title: Acelerador criação de API RM - Plugin Informativos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=496032263
version: 16
---

As dicas abaixo tem o objetivo de agilizar e auxiliar a geração de API baseada em DataServer no RM.

**Vantagens:**

1 - Garantia de que os nomes entre as classes e o schema serão iguais, evitar possíveis erros de digitação.

2 - Garantia de que as definições do esquema seguem corretamente as definições do RM já informadas na GDIC.

3 - Documenta as próprias informações de Api no dicionario de dados do RM.

4 - Possibilita a padronização de campos conforme a base de dados RM, exemplo evitar que em uma tabela o CODCOLIGADA seja CompanyId e em outra seja AffiliateId, ou CreatedUserCode para RecCreatedBy tenha outros nomes em outras Api por exemplo RecCreatedCod.

**Etapas:**

1 - Na tabela base para disponibilização da API verificar a existência do preenchimento da coluna APIName.  
  
Exemplo:

SELECT APINAME,\* FROM HATENDIMENTOBASE

Exemplo:

2 - Montar um script com updates para preencher o campo API Name para as colunas que serão expostas.

sqlGera Script GDIC

Exemplo:

Resultado Gerado:

UPDATE GDIC SET APINAME = '' WHERE TABELA = 'HATENDIMENTOBASE' AND COLUNA = 'ALERTADISPARADO' -- ALERTADISPARADO.'  
UPDATE GDIC SET APINAME = '' WHERE TABELA = 'HATENDIMENTOBASE' AND COLUNA = 'ASSUNTOOC' -- Assunto tratado pelo atendimento.'  
UPDATE GDIC SET APINAME = '' WHERE TABELA = 'HATENDIMENTOBASE' AND COLUNA = 'RECMODIFIEDBY' -- Autor da última modificação no registro'

Informar o valor do campo API Name em cada linha do resultado.

UPDATE GDIC SET APINAME = StartDate WHERE TABELA = 'HATENDIMENTOBASE' AND COLUNA = 'ABERTURA' -- Data de abertura do atendimento.'  
UPDATE GDIC SET APINAME = ScheduleDate WHERE TABELA = 'HATENDIMENTOBASE' AND COLUNA = 'AGENDADOPARA' -- Data de agendamento.'  
UPDATE GDIC SET APINAME = PreviousScheduleDate WHERE TABELA = 'HATENDIMENTOBASE' AND COLUNA = 'AGENDADOPARAANTERIOR' -- Data de agendamento anterior.'

3 - Executar o Informativus

Quem quiser instalar o Informativus, segue o caminho:

* \\tecnologiabh.bh01.local\rmflex$\Outros\Ferramentas\Informativus

+ InformativusSetup.msi;

O Informativus possui vários ***Plugins*** de customização.

CAMINHO: \\tecnologiabh.bh01.local\rmflex$\Outros\Ferramentas\Informativus\Plugins

* NA ABA LISTA DE TABELAS BOTÃO DIRETO NA TABELA CARREGAR DICIONÁRIO DE DADOS.
