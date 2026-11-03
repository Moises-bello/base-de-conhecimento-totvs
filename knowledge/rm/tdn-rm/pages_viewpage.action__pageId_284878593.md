---
content_hash: a8ec256f1719f1825b1aa61a640c3dd7c046fddd57e848c09a0f1a9ba42600a1
fetched_at: '2026-06-29T00:08:37.181612+00:00'
page_id: '284878593'
product: rm
source: tdn-rm
title: '94774 FISCAL01-173 ECF: Implementação do Registro Y640'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284878593
version: 107
---

# Geração da ECF - Registros Y640 e Y650

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Geração dos registros Y640 e Y650 da ECF |
| **Situação/Requisito:** | Implementação dos registros Y640 e Y650 na ECF. Vide implementações a serem feitas:   * Um novo cadastro no anexo da filial "Parâmetros ECF - Escrituração Contábil Fiscal" que permitirá ao cliente cadastrar as informações a serem exportadas para o registros Y640 e Y650. * Alterações no layout da ECF e do TAF-ECF para carregar tais informações cadastradas e inserí-las nos respectivos registros. * Melhoria no processo de "Cópia de Parâmetros da ECF" para que estas novas informações sejam contempladas. |
| **Solução/Implementação:** | **Cadastros:**   * **Issue FISCAL01-830** * Implementado no anexo da Filial - "Parâmetros ECF - Escrituração Contábil Fiscal" o anexo "Y640 - Participações em Consórcios de Empresas". Este novo cadastro permitirá ao usuário inserir dados que serão  exportados para os registros Y640 e Y650 da ECF.    + **Para criação deste cadastro foram geradas as tabelas DPARTICICONSORCIOSEMPRESASECF (Tabela onde serão cadastrados os dados do registro Y640) e DPARTICIPANTESCONSORCIOSECF(Tabela onde serão cadastradas as informações do registro Y650)**   **Geração da rotina :**   * + **Issue FISCAL01-832**   + Foi realizada a implementação dos registros Y640 (Participações em Consórcios de Empresas) e Y650 (Participantes do Consórcio) no Layout de geração da ECF e de integração da ECF com o TAF (TAF-ECF).     - Registro Y640: será gerado com base nas informações da tabela "DPARTICICONSORCIOSEMPRESASECF". O campo chave do registro será o CNPJ, portanto os dados serão agrupados por esse campo. Para que o registro Y640 seja gerado, é necessário que o anexo “Participações em Consórcios de Empresas” (anexo "Parâmetros ECF" da Filial) esteja preenchido.     - Registro Y650: será gerado com base nas informações da tabela "DPARTICIPANTESCONSORCIOSECF". O campo chave do registro será o CNPJ, portanto os dados serão agrupados por esse campo.   + Para o Layout "TAF-ECF", o sistema gerará os registros "T116" e "T116AA", segundo Layout do TAF-ECF, na tabela "TAFST1".   **Processo de Cópia de Parâmetros da ECF:**   * + **Issue FISCAL01-834**   + Foi criado um novo Parâmetro na Tela do Processo **"Copiar Participações em Consórcios e Empresas Y640 / Y650"**. Quando estiver marcado ao fazer a cópia o sistema também irá copiar os dados do Cadastro de "Y640 - Participações em Consórcios e Empresas" |
| **Conversores e Parâmetros:** | Criação das tabelas está disponível no conversor da versão 12.1.18. |

divs
