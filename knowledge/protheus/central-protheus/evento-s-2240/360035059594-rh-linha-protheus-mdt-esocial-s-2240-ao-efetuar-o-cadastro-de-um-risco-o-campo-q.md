---
article_id: 360035059594
category: Evento S-2240
content_hash: 0be274101851237db7903456485d738c21dba96b28a964d79a862f298a0c31bb
fetched_at: '2026-06-28T22:45:23.540446+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2240 - Ao efetuar o cadastro de um
  risco, o campo “Qtd. Agente” (TN0_QTAGEN) está arredondando o valor que foi cadastrado
type: support-article
updated_at: '2025-03-03T16:52:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035059594-RH-Linha-Protheus-MDT-eSocial-S-2240-Ao-efetuar-o-cadastro-de-um-risco-o-campo-Qtd-Agente-TN0-QTAGEN-est%C3%A1-arredondando-o-valor-que-foi-cadastrado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30370008344983)**Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**No módulo Medicina e Segurança do Trabalho, ao efetuar o cadastro de um risco pela rotina **MDTA180,** o campo “**Qtd. Agente**” (**TN0\_QTAGEN**) está arredondando o valor que foi cadastrado  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**Esse incidente ocorre, pois o campo **TN0\_QTAGEN** foi alterado para 4 casas decimais conforme validações do eSocial, nesse caso o **X3\_DECIMAL** ficou com 3 casas decimais onde deveria estar com 4.  
  
**Solução**1. Acessar o módulo **Configurador** (**SIGACFG**).  
  
2. Acessar **Base de Dados\Dicionário\Base de Dados**, e no dicionário de dados buscar pela tabela **TN0** / **TN1** / **TLK**.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046407593)  
  
3. **Editar**a tabela e buscar pelo campo **TN0\_QTAGEN** / **TN1\_DEINTE** / **TN1\_ATEINT** / **TLK\_DEQTDE.**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045551494)  
  
4. Alterar o campo e trocar o valor de **Decimal**de 3 para 4, salvar e confirmar a tela**.**  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045551614)  
  
5. Após alterar todos os campos, clicar no **ícone de atualizar**, para gravar as alterações na base de dados.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046408453)  
  
Documentação Completa: <https://tdn.totvs.com/x/laqcHQ>  
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
