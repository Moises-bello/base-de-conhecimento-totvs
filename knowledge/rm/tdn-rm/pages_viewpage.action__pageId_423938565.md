---
content_hash: ea8ddb84e30d2fb615babd0574210508a3ceddc0a17eeae3934068f062cc9a8c
fetched_at: '2026-06-29T00:09:27.899790+00:00'
page_id: '423938565'
product: rm
source: tdn-rm
title: Versão 11.50.0 (TOTVS Manutenção)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938565
version: 4
---

**Migração do processo de Requisição de Material** O processo de requisição de OS foi migrado para .NET nesta versão.   
Com o processo de requisição de OS migrado é possível que a requisição respeito os mesmos parâmetros realizados no TOTVS Gestão de Estoque, Compras e Faturamento além de ter a possibilidade de utilizar as mesmas funcionalidades e recursos já disponibilizados pelo TOTVS Gestão de Estoque, Compras e Faturamento através do movimento .NET.

**Migração do processo** Iniciar execução dos serviços orçados O processo de iniciar a execução dos serviços orçados da OS foi migrado.   
Agora ao clicar na OS com o botão direito do mouse e iniciar o serviço o sistema exibe um wizard responsavel por executar este processo.  
Novo parâmetro "Excluir histórico de indicador de uso do objeto filho" Foi criado na tela "Cancelar Agregação/Desagregação" o parâmetro "Excluir Histórico de indicador de uso do objeto filho".

**Marcando este parâmetro é possível cancelar uma agregação** que possua indicadores de uso lançados com data posterior a data de agregação pelo objeto filho. Com o parâmetro "Excluir Histórico de indicador de uso do objeto filho" marcado, os indicadores de uso dos objetos filhos que foram gerados pela agregação com datas posteriores a mesma são excluídos possibilitando a desagregação do objeto filho.   
Anteriormente para realizar uma desagregação o usuário deveria excluir manualmente os indicadores dos objetos filhos antes de executar o processo de cancelamento da agregação.
