---
article_id: 360025721813
category: RH - Dissídio
content_hash: 67cb730fed743307427a3993db75742dd7bf3d0644a7fdf97d07dd9b77710e8c
fetched_at: '2026-06-28T22:43:43.321009+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Como recriar roteiros e recompilar a fórmula VALDISSI
type: support-article
updated_at: '2025-08-20T13:06:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025721813-RH-Linha-Protheus-GPE-Como-recriar-roteiros-e-recompilar-a-f%C3%B3rmula-VALDISSI
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34314789602711) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Como recriar roteiros e recompilar a fórmula VALDISSI?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 11.80  
  
**Solução**Renomeie as tabelas de fórmulas e roteiros, para que o sistema recrie no padrão:  
-SRY;  
-SRM;

Acesse o **Configurador (SIGACFG)**, entre em Base de Dados> Dicionários> Base de Dados. Selecione no canto superior esquerdo Dicionário de Dados e depois selecione o ícone com o símbolo de lupa:![](https://centraldeatendimento.totvs.com/hc/article_attachments/34314789604119)

Será apresentada a tela abaixo. No campo de pesquisa, digite SRY e clique em Buscar. Depois selecione o ícone Editar: ![](https://centraldeatendimento.totvs.com/hc/article_attachments/34314799488791)

No exemplo abaixo, a tabela SRY possui o nome SRYT10, altere para um nome que não exista em seu ambiente, SRYT10\_T por exemplo:**![](https://centraldeatendimento.totvs.com/hc/article_attachments/34314799490455)**

Após a alteração, o campo Nome será alterado como SRYT10\_T. Clique em Confirmar:**![](https://centraldeatendimento.totvs.com/hc/article_attachments/34314789606039)**

Será apresentado o *browse* novamente. Clique no ícone com desenho Disquete. Será aberta uma nova janela, clique em Avançar em todas as janelas que forem mostradas:

**Esta ação depende de acesso exclusivo:****![](https://centraldeatendimento.totvs.com/hc/article_attachments/34314789607191)**

Será apresentada a janela abaixo ao fim do processamento. Verifique se será apresentada a mensagem:

**Atualização finalizada com sucesso e Finalize.****![](https://centraldeatendimento.totvs.com/hc/article_attachments/34314799496599)**

Após a execução do processo acima com as duas tabelas citadas, entre na rotina de roteiro de cálculo (Atualizações> Definições de Cálculo> Roteiro de Cálculo) para que as tabelas sejam recriadas. Este processo demorará alguns minutos.

Após recriar os roteiros, entre alterando o roteiro da FOLHA e inclua uma nova linha para lançar a fórmula VALDISSI no roteiro.![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040557253)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039726934)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040557833)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039727634)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040558673)

Saiba Mais:  
[Página Centralizadora do Dissídio (GPEM690)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)
