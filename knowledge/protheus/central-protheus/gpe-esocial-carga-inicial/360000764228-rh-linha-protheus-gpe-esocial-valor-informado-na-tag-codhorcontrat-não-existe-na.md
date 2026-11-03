---
article_id: 360000764228
category: GPE - eSocial - Carga Inicial
content_hash: 4c4c5ccf863b85ef43b00169e7625661c1fb89996df151192ac161d7d0e9cdc6
fetched_at: '2026-06-28T22:45:03.349164+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial- Valor informado na tag codHorContrat não
  existe na base de dados
type: support-article
updated_at: '2022-03-29T18:02:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000764228-RH-Linha-Protheus-GPE-eSocial-Valor-informado-na-tag-codHorContrat-n%C3%A3o-existe-na-base-de-dados
---

**Ocorrência  
TAF** - Totvs Automação Fiscal - **ESOCIAL** - "Valor informado na tag **codHorContrat** não existe na base de dados"  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**A mensagem "valor informado na tag **codHorContrat** não existe na base de dados" é gerada porque está tentando enviar um funcionário no **S-2200** e esse funcionário está vinculado a um turno que não existe na base do **TAF** - Totvs Automação Fiscal.   
  
É necessário que analise o Turnos, Regra e Tabela de horários (tabela de horário padrão) dos funcionários ativos pois o evento de turno é composto pela informação dessas 3 rotinas.   
  
É sabido que na carga inicial dos turnos, caso não estiver associado a nenhum funcionário, o turno não é integrado para o **TAF**- Totvs Automação Fiscal. Portanto estão ocorrendo casos onde na fase 1 existiam turnos que não estavam associados a nenhum funcionário e não foram integrados, porém após a fase 2, surgiu a necessidade de novos funcionários admitidos (sendo cadastrados) utilizarem esses turnos. Porém ao tentar cadastrar um novo funcionário com um desses turnos antigos que não foram integrados, ocorre uma mensagem informando que o turno não foi integrado.  
  
**Solução**A correção foi liberada na Release Oficial expedida e publicada na Central de Downloads.  
O pacote pode ser acessado no endereço:  
12.1.17: <https://suporte.totvs.com/portal/p/10098/download?e=675592> **Importante**Caso esteja com o RPO muito desatualizado, além de aplicar o pacote pontual acima, será necessário atualizar também o pacote acumulado da sua versão conforme a base de conhecimento: [PSIGABD0086 - Qual o link direto para pesquisar e baixar o pacote acumulado do Portal do Cliente?](http://tdn.totvs.com/pages/viewpage.action?pageId=286519628)  
  
**Aceitar apenas fontes atualizados.**
