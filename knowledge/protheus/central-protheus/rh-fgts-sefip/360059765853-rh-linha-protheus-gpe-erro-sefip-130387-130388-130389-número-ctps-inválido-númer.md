---
article_id: 360059765853
category: RH - FGTS / SEFIP
content_hash: 201a96bed7a66006b7b7ba422b5f929e6934315b44ab580b6766be4f14f11205
fetched_at: '2026-06-28T22:43:41.277907+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - Erro SEFIP 130387 / 130388 / 130389 - Número CTPS
  inválido. / Número CTPS deve ser informado para Categoria indicada. / Série CTPS
  inválida.
type: support-article
updated_at: '2023-04-28T21:21:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059765853-RH-Linha-Protheus-GPE-Erro-SEFIP-130387-130388-130389-N%C3%BAmero-CTPS-inv%C3%A1lido-N%C3%BAmero-CTPS-deve-ser-informado-para-Categoria-indicada-S%C3%A9rie-CTPS-inv%C3%A1lida
---

**Ocorrência**Ao importar o arquivo SEFIP.RE gerado no Protheus, o validador do programa SEFIP apresenta o seguinte erro 130387 / 130388 / 130389 - Número CTPS inválido. / Número CTPS deve ser informado para Categoria indicada. / Série CTPS inválida.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa****Data ou Conteúdo da rotina Manutenção Hist. Funcionário (Tabela SR9) incorretos** - Esse erro ocorre pois o usuário efetuou uma alteração no cadastro do funcionário, nos Campos de Numero CTPS e Serie CTPS, fazendo com que o sistema grave as alterações na rotina Manutenção Hist. Funcionário (Tabela SR9), a SEFIP busca informação da ultima alteração dos campos, a alteração fica salva com data de Login no sistema - data base sistema.   
  
**Solução**

Verificar na rotina Manutenção Hist. Funcionário, através do caminho Atualização / Funcionários /  Manutenção Hist. Funcionário qual é o conteúdo e data dos campos alterados pelo usuário, efetuar ajuste do conteúdo do campo com data base correta.

**Importante:**Como trata-se de um campo em que o sistema grava histórico de alterações na tabela SR9, é necessário que no momento da alteração do campo a **data base do sistema esteja com a mesma data da competência da geração da SEFIP**, **caso contrário irá gravar uma data futura e não será considerada a ocorrência para geração**.

**OBS:** Caso não possua esta rotina no menu, efetue o procedimento conforme o link abaixo:

[RH - Linha Protheus - GPE - Como realizar manutenção no histórico de alterações do cadastro de funcionários (tabela SR9)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10724875306775-RH-Linha-Protheus-GPE-Como-realizar-manuten%C3%A7%C3%A3o-no-hist%C3%B3rico-de-altera%C3%A7%C3%B5es-do-cadastro-de-funcion%C3%A1rios-tabela-SR9)

**Saiba mais:  [MP - GPE - eSocial - Carteira de Trabalho Digital - o que muda no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037534793-MP-GPE-eSocial-Carteira-de-Trabalho-Digital-o-que-muda-no-Protheus?source=search)**

**https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003115651-RH-FGTS-SEFIP**
