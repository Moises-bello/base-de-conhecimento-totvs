---
article_id: 11246718897175
category: eSocial - Gerar XML/ Integração Evento
content_hash: fc36a9088fd825d714937c1095b394d4920bbd52a485cb723f6e29da6843ab99
fetched_at: '2026-06-28T22:47:12.964002+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro na integração com o TAF: O valor informado
  na tag codRubr existe na base de dados, mas está atualmente com status Registro
  Transmitido com inconsistência(s)'
type: support-article
updated_at: '2024-12-26T16:05:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11246718897175-RH-RM-FOP-eSocial-Erro-na-integra%C3%A7%C3%A3o-com-o-TAF-O-valor-informado-na-tag-codRubr-existe-na-base-de-dados-mas-est%C3%A1-atualmente-com-status-Registro-Transmitido-com-inconsist%C3%AAncia-s
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28789250973975) Tempo aproximado para leitura: **00****:01:00 min****Ocorrência**Ao enviar os eventos S-1200 e S-2299 é apresentado a mensagem **Registro não integrado. Duplo clique para mais informações! Erro 1 - Fila de Integração: O valor 'xxxx' informado na *tag* codRubr existe na base de dados, mas está atualmente com status Registro Transmitido com inconsistência(s).**  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**O erro ocorre quando um evento que compõe as verbas do XML encontra-se no TAF, mas o S-1010 deste evento está com status com inconsistência dentro do TAF.

**Solução**Para correção da ocorrência favor realizar as validações abaixo:1. Primeiramente será necessário identificar qual a rubrica que possui status com inconsistência no TAF. Para isso, acesse **Atualizações | Eventos Esocial | Tabelas | Rubricas;**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11246350932375)

2. Filtre pelo tipo de registro **Status Reg.** e informe o número 3 na pesquisa (Este valor representa os eventos inconsistentes no TAF). Todos os eventos com status 3 (inconsistentes) serão apresentados na tela;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11246398101655)

2. Verifique o erro apresentado na inconsistência do evento e se será necessário alterar o evento ou exclui-lo;  
3. Após correção ou exclusão, encaminhe novamente o evento com a remuneração.

**Saiba mais**Para mais informações acesse:   
**-**[Automação Fiscal - Configuração - Como excluir eventos com status inconsistente no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035475634-Automa%C3%A7%C3%A3o-Fiscal-Configura%C3%A7%C3%A3o-Como-excluir-eventos-com-status-inconsistente-no-TAF)
