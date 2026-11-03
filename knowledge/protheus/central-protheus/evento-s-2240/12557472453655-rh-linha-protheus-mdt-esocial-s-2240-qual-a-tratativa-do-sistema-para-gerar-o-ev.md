---
article_id: 12557472453655
category: Evento S-2240
content_hash: ba183194587496cfba47f980fdf253d1d6a7e540c2099488532de7aea3ed303a
fetched_at: '2026-06-28T22:45:23.735903+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2240 - Qual a tratativa do sistema
  para gerar o evento S-2240 na rescisão e buscar informação da tarefa
type: support-article
updated_at: '2025-03-11T19:09:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12557472453655-RH-Linha-Protheus-MDT-eSocial-S-2240-Qual-a-tratativa-do-sistema-para-gerar-o-evento-S-2240-na-rescis%C3%A3o-e-buscar-informa%C3%A7%C3%A3o-da-tarefa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Qual a tratativa do sistema para gerar o evento S-2240 na rescisão e buscar informação da tarefa?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**De acordo com o MOS (Manual de Orientação do eSocial):

"Não é necessário o envio desse evento para informar o fim da exposição a agente nocivo em decorrência de desligamento do trabalhador". Veja documentação:   
[É obrigatório o envio do evento S-2240 na rescisão do funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9697731515287)  
  
Foi criado o parâmetro **MV\_MDTENRE** que define a geração do evento na rescisão. Para alterar esta configuração padrão, basta alterar o conteúdo do parâmetro na rotina **Parâm. MDT**, no menu *Miscelânea - Implantação - Param.Esocial* (**MDTA892**):

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12557646088855)

Caso optado por gerar o evento na rescisão do funcionário, é preciso ficar atento à alguns detalhes, como por exemplo a configuração dos parâmetros **MV\_NG2EAMB**e **MV\_NG2TDES**, responsáveis pela configuração do envio do ambiente e da descrição das atividades respectivamente.  
  
Quando selecionado para buscar as informações da tarefa do funcionário, ocorrerá a mensagem, pois a partir do momento que é feita a rescisão do funcionário, a tarefa é automaticamente finalizada, portanto, não é possível buscar as informações da tarefa do funcionário, gerando o evento com as mesmas em branco. Ao ocorrer estes fatos, o usuário é alertado pelos seguintes avisos:

![](https://tdn.totvs.com/download/attachments/725731064/image2022-12-2_13-58-47.png?version=1&modificationDate=1670001169743&api=v2)

**![](https://tdn.totvs.com/download/attachments/725731064/image2022-12-2_13-59-1.png?version=1&modificationDate=1670001169600&api=v2)**

Ao tentar comunicar o evento gerado ao governo, será retornado uma inconsistência, pois há informações essenciais em branco, se referindo as informações que deveriam ser enviadas nas tags **infoAmb**e **infoAtiv**, que podem ficar em branco por conta de serem buscadas da tarefa.  
  
**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
