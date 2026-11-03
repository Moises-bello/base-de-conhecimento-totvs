---
article_id: 20983145867543
category: MDT - PCMSO
content_hash: 5807e1dba45695ddde30d34e82962a89f5952564307914811f715c6101cef17c
fetched_at: '2026-06-28T22:44:28.263790+00:00'
product: protheus
section_id: 360010945214
source: central-protheus
title: RH - Linha Protheus - MDT - Valor atribuído difere do tamanho do campo Nome
  Exame
type: support-article
updated_at: '2025-09-03T14:14:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20983145867543-RH-Linha-Protheus-MDT-Valor-atribu%C3%ADdo-difere-do-tamanho-do-campo-Nome-Exame
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20983191393047) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao cadastrar um exame ao Funcionário através da rotina Exame do Funcionário é apresentado a mensagem "Valor atribuído difere do tamanho do campo (Nome Exame)".  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20983145832215)  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**A mensagem de erro ocorre por existir divergência entre o tamanho dos campos " **Nome Exame** " (**TM4\_NOMEXA**) e (**TM5\_NOMEXA**).  
  
**Solução  
1-** É necessário aplicar o Pacote e Dicionário de Dados com data igual ou superior a **26/01/2024.**disponível no link: **[Pacote e Dicionário de Dados Expedição Continua MDT](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/MDT_EXPEDICAO_CONTINUA.ZIP)**Através desta atualização **foi ajustado** no compatibilizador a opção de permitir **alterar o tamanho do campo** *TM5\_NOMEXA* para que ele consiga ser configurável com o mesmo tamanho do campo *TM4\_NOMEXA.*

**2-** Realizar o ajuste dos campos **manualmente**, é necessário seguir a FAQ:  
[MDT0131 Tamanho dos Campos TM4\_NOMEXA e TM5\_NOMEXA](https://tdn.totvs.com/display/PROT/MDT0131+Tamanho+dos+Campos+TM4_NOMEXA+e+TM5_NOMEXA)

**Atenção!**   
Aplicação do acumulado irá apenas alterar a configuração do campo permitindo sua alteração de tamanho, contudo essa alteração deve ser realizada de forma Manual conforme indicação da Documentação Técnica do Produto. Maiores informações consulte:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=821191990>

**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
