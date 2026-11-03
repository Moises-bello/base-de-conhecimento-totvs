---
article_id: 21409817835287
category: MDT - Atendimento Médico
content_hash: f4c44fd7be181479080acd941c5d945d0df588a91d778468e140593477424f9e
fetched_at: '2026-06-28T22:44:21.553474+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: 'RH - Linha Protheus - MDT - Quando seleciona o médico No aso Help: FWNOWDITH
  Valor atribuído difere do tamanho do campo (Nome)'
type: support-article
updated_at: '2024-02-19T11:13:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21409817835287-RH-Linha-Protheus-MDT-Quando-seleciona-o-m%C3%A9dico-No-aso-Help-FWNOWDITH-Valor-atribu%C3%ADdo-difere-do-tamanho-do-campo-Nome
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21409817812119) Tempo aproximado para leitura: 00:02:00 min****Ocorrência**  
O que avaliar se gerar a mensagem ao selecionar o médico "Valor atribuído difere do tamanho do campo (Nome)" na rotina de Atestado Aso?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**A mensagem de erro ocorre por existir divergência entre o tamanho dos campos "**Nome do****Usuário**" (TMK\_NOMUSU) e (TMY\_NOMUSU*)*.  
  
**Solução****1-** É necessário aplicar o Pacote e Dicionário de Dados com data igual ou superior a **06/02/2024.**disponível no link: **[Pacote e Dicionário de Dados Expedição Continua MDT](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/MDT_EXPEDICAO_CONTINUA.ZIP)**Através desta atualização **foi ajustado** no compatibilizador a opção de permitir **alterar o tamanho do campo** TMY\_NOMUSU para que ele consiga ser configurável com o mesmo tamanho do campo TMK\_NOMUSU*.***2-** Realizar o ajuste dos campos **manualmente**, é necessário seguir a FAQ:  
[MDT0136 Tamanho dos Campos TMK\_NOMUSU e TMY\_NOMUSU](https://tdn.totvs.com/display/public/PROT/MDT0136+Tamanho+dos+Campos+TMK_NOMUSU+e+TMY_NOMUSU)  
  
**Atenção!**   
Aplicação do acumulado irá apenas alterar a configuração do campo permitindo sua alteração de tamanho, contudo essa alteração deve ser realizada de forma Manual conforme indicação da Documentação Técnica do Produto. Maiores informações consulte:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=821191990>  
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
