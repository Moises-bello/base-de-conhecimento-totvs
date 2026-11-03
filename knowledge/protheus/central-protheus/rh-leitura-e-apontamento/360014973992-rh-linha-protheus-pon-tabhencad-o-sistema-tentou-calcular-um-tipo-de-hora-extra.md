---
article_id: 360014973992
category: RH - Leitura e Apontamento
content_hash: 029560101f0af0f7d2df724d084b7d102b2a367c596612bdd44982906ff5418f
fetched_at: '2026-06-28T22:44:46.025683+00:00'
product: protheus
section_id: 32419281460119
source: central-protheus
title: RH - Linha Protheus - PON - TABHENCAD - O sistema tentou calcular um tipo de
  Hora Extra que não está cadastrada
type: support-article
updated_at: '2025-08-14T19:29:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014973992-RH-Linha-Protheus-PON-TABHENCAD-O-sistema-tentou-calcular-um-tipo-de-Hora-Extra-que-n%C3%A3o-est%C3%A1-cadastrada
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34185069694743) Tempo aproximado para leitura: 00:01:30 min****

**Ocorrência**No módulo Ponto Eletrônico, ao tentar realizar apontamento de marcações, o sistema retorna um log de ocorrências em tela **TABHENCAD** - O sistema tentou calcular um tipo de Hora Extra que não está cadastrada.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32080623909143)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Causa**Essa mensagem é gerada, quando não estão cadastradas os 08 **Tipos de Horas Extras** essenciais para apuração do sistema e apontamento correto das horas extras.  
  
**Solução**Para solucionar essa ocorrência, verifique os seguintes passos:  
**1.**Verifique se o compartilhamento das suas tabelas **SP4** e **SP9** estão iguais. Elas precisam obrigatoriamente, ter o mesmo compartilhamento;  
**2.** Tendo a estrutura de forma **compartilhada**, os dados das duas tabelas possuir o **campo filial "em branco"**, de outra forma. Se for **Exclusivo**, os dados das tabelas deverão possuir o campo filial preenchido;  
**3.** Após analisar as orientações acima, verifique se existem os 8 primeiros [**tipos de horas extras**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060489314-RH-Linha-Protheus-PON-Regras-importantes-para-o-cadastro-dos-Tipos-de-Horas-Extras) **(Atualizações>Cadastro do Ponto>Tipos de Horas Extras),** cadastrados;  
**4.**  Orientamos que é necessário utilizar **um evento diferente** para cada tipo de hora extra, veja exemplo abaixo:  
![66.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360010052812)  
  
**Saiba Mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download?e=1080347)
