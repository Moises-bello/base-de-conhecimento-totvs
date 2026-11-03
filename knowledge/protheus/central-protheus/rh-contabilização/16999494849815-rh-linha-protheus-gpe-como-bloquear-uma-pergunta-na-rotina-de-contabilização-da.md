---
article_id: 16999494849815
category: RH - Contabilização
content_hash: 93840def542e2f2f12c390f83932dc8c702e1dc47ee4be8074b70e676c77387f
fetched_at: '2026-06-28T22:43:45.780542+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Como bloquear uma pergunta na rotina de contabilização
  da folha (GPEM110)
type: support-article
updated_at: '2025-07-22T20:55:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16999494849815-RH-Linha-Protheus-GPE-Como-bloquear-uma-pergunta-na-rotina-de-contabiliza%C3%A7%C3%A3o-da-folha-GPEM110
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16999500241303) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como bloquear uma pergunta na rotina de contabilização da folha (GPEM110)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.

**Solução**

1. Perguntas são parâmetros de rotinas que podem ser configurados no Protheus. Nesta rotina GPEM110, o grupo de perguntas atual é o grupo GPE110A.   
  
A rotina já possui perguntas com busca as nos parâmetros (figura 1) e também perguntas com COMBO de respostas para pergunta (figura 2) , mas os campos estão livres para edição. A rotina de **Configuração de Perguntas** do Configurador serve para definir uma resposta padrão a estes parâmetros e deixá-los bloqueados para que o usuário não possa alterar.

(Figura 1)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16999468949015)

(Figura 2)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16999444865431)  
  
No exemplo, desta documentação vamos bloquear a pergunta **Contabiliza por** pra que seja possível apenas utilizar a opção **Centro de Custos,** para que não seja possível utilizar a opção Contabiliza por matrícula.  
  
1. Acesse Configurador > Usuário > Senhas > Configuração de Perguntas  
2. Clique em **Incluir**  
3. Em **Grupo**, digite o código do Grupo de Perguntas GPE110A  
4. Em **Usuário** ou **Grupo de Usuário**, selecione um usuário ou grupo para associar essa regra de configuração de perguntas  
5. Seção **Perguntas** serão exibidas as perguntas referentes a este grupo. Elas estão todas marcadas em cinza  
6. Para bloquear uma pergunta, clique sobre ela, e pressione a tecle **DEL** do teclado. Neste momento ela já estará bloqueada na rotina. Se quiser inserir um novo valor padrão, digite-o abaixo da coluna **Conteúdo**, ou em casos de campos do tipo combo, selecione o valor padrão  
7. Na imagem de exemplo abaixo, foi bloqueada a opção Contabiliza por Matrícula, mantendo chumbado a opção por Centro de Custos .

![GPEM110.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17005620271511)

**Obs:** o exemplo acima, bloqueou a opção para ADM, considerando que este é o usuário usado no teste.

8) Acessar miscelânea -> Fechamentos -> Contabilização e verificar que não é possível editar a pergunta para outra configuração além da selecionada no grupo de perguntas via Configurador: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17005545958807)

**Saiba Mais:**  
[Página Centralizadora da Contabilização](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109092-RH-Contabiliza%C3%A7%C3%A3o)
