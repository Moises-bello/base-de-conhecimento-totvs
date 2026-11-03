---
content_hash: c313caa77ee99bd9b453bc8d85fcd8fbeaf12c4885c9c61a3d84f05affbcc2a5
fetched_at: '2026-06-29T00:09:24.428445+00:00'
page_id: '423937901'
product: rm
source: tdn-rm
title: Versão 11.20.0 (TOTVS Gestão de Planejamento e Controle da Produção)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937901
version: 4
---

**11.20.0 - Parâmetros da Produção:**Implementação de parâmetro "Considera alocação(ões) dos recursos no cálculo do MRPII", na pasta "Ordem de Produção". Quando o parâmetro estiver marcado o RM Factor irá considerar as alocações de recursos (default). Quando este parâmetro estiver desmarcado o RM Factor irá desconsiderar as alocações de recursos (equipamentos e mãos de obra) existentes na base de dados, isto é, todo recurso estará sempre disponível para execução das atividades. Implementação do parâmetro "Permissão para apontamento por usuário" na pasta "Apontamento". Permite consistir usuários que terão permissão de apontamento para as Atividades do item de ordem de produção. Estes usuários deverão ser inseridos no cadastro genérico de Atividades, através da pasta "Permissão para Apontamento". Quando não houver nenhum usuário relacionado a uma atividade ela poderá ser apontada por qualquer usuário que tenha permissão de acesso à tela de apontamento.  
    
 **11.20.0 - Registro da Produção:**Melhoria de consistência para que atividades do item de ordem de produção que estejam no status "Interrompida" sejam consideradas no momento de dar entrada da produção.

**11.20.0 – Outras atualizações:**Realizada melhoria na baixa de materiais e na entrada de produto em estoque para produtos controlados por lote. Na baixa de materiais o sistema irá sugerir a baixa dos lotes mais antigos. No apontamento o sistema irá consumir os lotes mais antigos e na devolução os lotes com data de validade maior, ou seja, os lotes mais novos.  
Realizada melhoria no cálculo do MRPII para quando o sistema está parametrizado para trabalhar com empenho.  
Realizada melhoria nos movimentos de baixa de materiais, empenho e solicitação de compra para que materiais de atividades canceladas não apareçam nos movimentos.  
Realizada melhoria na baixa de materiais para que seja mostrada a quantidade por lote a ser baixada corretamente.  
Realizada melhoria na entrada de produção pelo posto de trabalho para que o sistema retorne as quantidades do estoque intermediário.
