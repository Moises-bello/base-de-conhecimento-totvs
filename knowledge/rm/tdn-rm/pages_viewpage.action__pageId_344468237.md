---
content_hash: baf7fc6dd9cb8fdb8eaba1d80b1739d555c4b6a1a7c8709fc62a48d253a0c23d
fetched_at: '2026-06-29T00:08:53.311213+00:00'
page_id: '344468237'
product: rm
source: tdn-rm
title: RMFIS00004_Criação da tabela TAFST1
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=344468237
version: 2
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.1 |
| **Ocorrência:** | Criação da tabela TAFST1 para integração entre RM x TAF (Utilizado apenas em contingência) |
| **Ambiente:** |  |
| **Passo a passo:** | A tabela TAFST1 será necessária na integração entre os produtos RM e TAF em contingência , modelo banco a banco, a mesma será criada no wizard de instalação do TAF.  Caso já possua o TAF instalado e necessite criar a tabela TAFST1 em outra base de dados deve seguir os procedimentos abaixo:   1. Acesse o TAF com o usuário admin. Não é necessário preencher o campo de senha 2. Acesse o menu Atualizações | Configs. Taf | Wizard de Configuração Taf 3. No wizerd de configuração acione o botão "Avançar" e selecione o Grupo de Empresa na próxima tela conforme imagem abaixo: 4. Selecione as duas opções conforme imagem: 5. No campo destacado abaixo informe o nome da conexão ODBC/dbAccess da base onde a tabela TAFST1 deve ser criada. 6. Informe a porta de conexão do Web Service e o ambiente 7. Acione o botão "Processar as configurações realizadas neste assistente..." para que as configurações sejam processadas e criado a tabela TAFST1 na base parametrizada. |
| **Observações:** |  |
