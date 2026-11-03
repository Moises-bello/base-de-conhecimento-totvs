---
article_id: 14232047812119
category: GPE - eSocial - Carga Inicial
content_hash: 165810c212a489971abe903e0cbe41f2dff3818c8cba691aa57945e79d92a1d7
fetched_at: '2026-06-28T22:45:03.278419+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1010 - O valor 'XXXX' informado na
  tag natRubr não existe na base de dados.
type: support-article
updated_at: '2024-06-20T17:29:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14232047812119-RH-Linha-Protheus-GPE-eSocial-S-1010-O-valor-XXXX-informado-na-tag-natRubr-n%C3%A3o-existe-na-base-de-dados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24317786783895) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**O que fazer quando ao alterar o cadastro de verbas, sistema gera mensagem "**o valor 'XXXX' informado na tag natRubr não existe na base de dados**"?  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14231405925399)  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para solução do erro apresentado, será necessário realizar os passos abaixo:  
  
1. Atualizar **fontes** do módulo **GPE**: [Pacote e Dicionário Correções Expedição Continua RH](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/RH_EXPEDICAO_CONTINUA)   
2. Atualizar **fontes** e **dicionário** do módulo **TAF**: [Pacote e Dicionário Correções Expedição Continua TAF](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/TAF_EXPEDICAO_CONTINUA.ZIP)   
3. Acessar acesse a tabela S047 para atualiza-la: [RH - Linha Protheus - GPE - eSocial - Como atualizar as tabelas S047, S048, S049, S054, S050, S056, S057 e S138, conforme layout S-1.1 do eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016801271)  
4. Atualizar as autocontidas: [Automação Fiscal - CONFIGURAÇÃO - Atualização das tabelas autocontidas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034479973-Automa%C3%A7%C3%A3o-Fiscal-CONFIGURA%C3%87%C3%83O-Atualiza%C3%A7%C3%A3o-das-tabelas-autocontidas)  
Verifique se a natureza foi criada corretamente na S047 e também no TAF deve ser criada na tabela C89.  
  
Exemplo GPE:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14231947943447)  
Exemplo TAF:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14231807366039)

**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[RH - Linha Protheus - GPE - eSocial - S-1010 - Após a transmissão dos eventos iniciais (carga inicial), como enviar um único registro para o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046341633)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
