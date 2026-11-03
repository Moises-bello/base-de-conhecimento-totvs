---
content_hash: fd62fdbab6fe062d9b9776f290f1809a9a17b5e2f418a26f385b96b8187b03ce
fetched_at: '2026-06-29T00:09:08.532972+00:00'
page_id: '389552624'
product: rm
source: tdn-rm
title: Informações sobre Segurança e Saúde no Trabalho (SST)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=389552624
version: 1
---

# Adequação à Nota de Documentação Evolutiva 01/2018.

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Folha de Pagamento. |
| **Módulo:** | Administração de Pessoal. |
| **Função:** | Seções. |
| **Situação/Requisito:** | Adequação a Nota de Documentação Evolutiva 'NDE 01/2018 - Eventos de Segurança e Saúde no Trabalho - SST' liberada pela receita federal no dia 30/05/2018. |
| **Solução/Implementação:** | Criação do anexo "Informações de Segurança e Saúde Ocupacional", no cadastro de seções, para inclusão das informações de programas de Segurança e Saúde Ocupacional. |

Para atender a Nota de Documentação Evolutiva **'NDE 01/2018 - Eventos de Segurança e Saúde no Trabalho - SST'**liberada pela receita federal no dia 30/05/2018, foi criado no cadastro de seções o anexo "Informações sobre Segurança e Saúde no Trabalho (SST)", para inclusão das informações dos programas de SST de cada seção. Esse anexo é alimentado pela tabela dinâmica VPROGDOC (Tabela 30: Programas, Planos e Documentos) e compõe as informações do evento S-1005.

Para que o sistema considere a nova tabela liberada pela NDE, será necessária a execução do script que está disponível no RM.Atualizador. Para isso, acesse o RM.Atualizador com o usuário do banco de dados.

***Atenção: Antes de realizar qualquer alteração através do RM.Atualizador é necessário realizar o backup do banco de dados.***

Após a execução do script o novo anexo estará disponível na árvore de segurança do módulo Folha de Pagamento.

Após a liberação de segurança, o anexo estará disponível no cadastro de seções. O novo anexo aparecerá disponível, se houver permissão associada ao perfil, em todos os sistemas que utilizam a rotina de seções.

As informações só poderão ser incluídas nas seções centralizadoras.

Após a inclusão/alteração das informações, o sistema irá gerar automaticamente o gatilho para o envio do evento S-1005.

eSocial | Fila de Eventos

Para gerar o XML é necessário selecionar o evento e acessar o menu -  Processos | Gerar XML.

As *tags* referentes ao programa de Informações sobre Segurança e Saúde do Trabalho (SST) são geradas de acordo com as informações cadastradas no cadastro da seção.

<progSST> - retorna o programa SST vinculado à seção.

<dtIniProg> - data de início da utilização do programa na seção.
