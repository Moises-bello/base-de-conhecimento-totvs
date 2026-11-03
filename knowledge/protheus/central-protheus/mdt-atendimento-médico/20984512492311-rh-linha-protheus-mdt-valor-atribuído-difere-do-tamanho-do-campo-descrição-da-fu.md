---
article_id: 20984512492311
category: MDT - Atendimento Médico
content_hash: 292e955a7abb8034c187db682c4ef867e9ebd1bfa32adac0ae755aa3e44aca60
fetched_at: '2026-06-28T22:44:20.451957+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - Valor atribuído difere do tamanho do campo Descrição
  da Função
type: support-article
updated_at: '2025-08-14T19:10:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20984512492311-RH-Linha-Protheus-MDT-Valor-atribu%C3%ADdo-difere-do-tamanho-do-campo-Descri%C3%A7%C3%A3o-da-Fun%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20984504633623) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**O que avaliar se gerar a mensagem "Valor atribuído difere do tamanho do campo Descrição da Função" na rotina de Ficha Médica?  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**A mensagem de erro ocorre por existir divergência entre o tamanho dos campos "**Descrição da Função**" (*RJ\_DESC*) e (*TM0\_DESCFU*).  
  
**Solução****1-** É necessário aplicar o Pacote e Dicionário de Dados com data igual ou superior a **26/01/2024.**disponível no link: **[Pacote e Dicionário de Dados Expedição Continua MDT](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/MDT_EXPEDICAO_CONTINUA.ZIP)**Através desta atualização **foi ajustado** no compatibilizador a opção de permitir **alterar o tamanho do campo** *TM0\_DESCFU* para que ele consiga ser configurável com o mesmo tamanho do campo *RJ\_DESC**.***2-** Realizar o ajuste dos campos **manualmente**, é necessário seguir a FAQ:  
[MDT0132 Tamanho dos Campos RJ\_DESC e TM0\_DESCFU](https://tdn.totvs.com/display/PROT/MDT0132+Tamanho+dos+Campos++RJ_DESC+e+TM0_DESCFU)  
  
**Atenção!**   
Aplicação do acumulado irá apenas alterar a configuração do campo permitindo sua alteração de tamanho, contudo essa alteração deve ser realizada de forma Manual conforme indicação da Documentação Técnica do Produto. Maiores informações consulte:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=821191990>  
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
