---
article_id: 21185262789655
category: MDT - Atendimento Médico
content_hash: 09d4327fc0843add1e6360b0946c37afae16e0fbf6c3d8a16a5b6a2d0f1c714d
fetched_at: '2026-06-28T22:44:21.571626+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - Valor atribuído difere do tamanho do campo (Nome)
type: support-article
updated_at: '2024-02-21T13:40:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21185262789655-RH-Linha-Protheus-MDT-Valor-atribu%C3%ADdo-difere-do-tamanho-do-campo-Nome
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21185262768919) Tempo aproximado para leitura: 00:02:00 min****Ocorrência**  
O que avaliar se gerar a mensagem "Valor atribuído difere do tamanho do campo (Nome)" na rotina de Atestado Aso?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**A mensagem de erro ocorre por existir divergência entre o tamanho dos campos "**Nome Proprietário Ficha**" (*TMY\_NOMFIC*) e (*TM0\_NOMFIC)*.  
  
**Solução****1-** É necessário aplicar o Pacote e Dicionário de Dados com data igual ou superior a **06/02/2024.**disponível no link: **[Pacote e Dicionário de Dados Expedição Continua MDT](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/MDT_EXPEDICAO_CONTINUA.ZIP)**Através desta atualização **foi ajustado** no compatibilizador a opção de permitir **alterar o tamanho do campo** *TMY\_NOMFIC* para que ele consiga ser configurável com o mesmo tamanho do campo *TM0\_NOMFIC**.***2-** Realizar o ajuste dos campos **manualmente**, é necessário seguir a FAQ:  
[MDT0135 Tamanho dos Campos TM0\_NOMFIC e TMY\_NOMFIC](https://tdn.totvs.com/display/PROT/MDT0135+Tamanho+dos+Campos+TM0_NOMFIC+e+TMY_NOMFIC)  
  
**Atenção!**   
Aplicação do acumulado irá apenas alterar a configuração do campo permitindo sua alteração de tamanho, contudo essa alteração deve ser realizada de forma Manual conforme indicação da Documentação Técnica do Produto. Maiores informações consulte:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=821191990>  
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
