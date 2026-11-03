---
article_id: 13964924601751
category: RH - Arquivos Bancarios
content_hash: c939774c1e64bc252a33023bacfa3144e7d42e02ef8e7f0ba3a9f01ef9bbafc1
fetched_at: '2026-06-28T22:43:38.350288+00:00'
product: protheus
section_id: 360004833673
source: central-protheus
title: RH - Linha Protheus - GPE - Relatório de Líquidos (GPER020) Não Grava Preenchimento
  das Perguntas
type: support-article
updated_at: '2025-09-19T22:43:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13964924601751-RH-Linha-Protheus-GPE-Relat%C3%B3rio-de-L%C3%ADquidos-GPER020-N%C3%A3o-Grava-Preenchimento-das-Perguntas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32323628710807) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Após a geração do relatório de líquidos (GPER020), ao acessar a rotina novamente, o sistema não mantém o preenchimento das perguntas conforme a última geração.  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Este incidente pode ocorrer por falta de atualização na base, ou o cadastro do usuário em questão não está configurado para que as perguntas sejam gravadas.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Verifique se o último Pacote RH Expedição Contínua já foi aplicado em sua base.  
Para realizar o Download do Pacote clique no endereço abaixo:  
[Expedição Contínua RH](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/RH_EXPEDICAO_CONTINUA)

**Observação:** Aplique-o em base de testes e realize um backup do RPO.  
  
2. Acesse o Configurador (SIGACFG) Usuário / Senhas / Usuários (CFGA510), Localize o funcionário e clique em Alterar;  
  
3. Clique na aba "Restrições de Acesso" e em seguida em "Acessos" e verifique se o código **108 - Gravar Resposta Parâmetros** está selecionada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13964453189271)  
  
4. Selecione o código 108 e em seguida clique em Confirmar para salvar a alteração no cadastro do usuário.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13964668307735)  
  
5. Após a alteração no cadastro do o usuário, o mesmo deverá realizar o log off no Protheus e poderá gerar o Relatório de Líquidos normalmente.

**Saiba Mais:**[RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833673-RH-Arquivos-Bancarios) [- Arquivos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833673-RH-Arquivos-Bancarios) [Bancários](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833673-RH-Arquivos-Bancarios)
