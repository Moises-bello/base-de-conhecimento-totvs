---
article_id: 13483891518103
category: RH - CNAB
content_hash: 62d78a5628e7da4f9b8ed53fc240b7188d1af419da9254df4cb0bcbb87f03858
fetched_at: '2026-06-28T22:43:39.360057+00:00'
product: protheus
section_id: 360004833653
source: central-protheus
title: RH - Linha Protheus -GPE - Como bloquear uma pergunta na geração de líquidos
  (GPEM080)
type: support-article
updated_at: '2025-09-19T19:05:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13483891518103-RH-Linha-Protheus-GPE-Como-bloquear-uma-pergunta-na-gera%C3%A7%C3%A3o-de-l%C3%ADquidos-GPEM080
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32854399564695) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como bloquear uma pergunta na geração de líquidos (GPEM080)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**  
1. Perguntas são parâmetros de rotinas que podem ser configurados no Protheus. Nesta rotina GPEM080, o grupo de perguntas atual e preponderante é o grupo GPEM080R2 (os grupos anteriores permanecem na tabela SX1 : GPEM080 e GPEM080R1).   
  
Documentação atualizado com todos os campos deste grupo de perguntas e suas funcionalidades:  
[RH - Linha Protheus - GPE - Passo a passo para geração do Arquivo CNAB (GPEM080)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8420406092951-RH-Linha-Protheus-GPE-Passo-a-passo-para-gera%C3%A7%C3%A3o-do-Arquivo-CNAB-GPEM080-)

A rotina já possui perguntas com busca as nos parâmetros (figura 1) e também perguntas com COMBO de respostas para pergunta (figura 2) , mas os campos estão livres para edição. A rotina de **Configuração de Perguntas** do Configurador serve para definir uma resposta padrão a estes parâmetros e deixá-los bloqueados para que o usuário não possa alterar.

(Figura 1)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13483680742551)

(Figura 2)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13483872433687)

No exemplo, desta documentação vamos bloquear a pergunta **Linha Vazia no Fim do Arquivo = Não,** para que não ocorra dúvida na geração do arquivo CNAB , descrito na documentação abaixo:  
[RH - Linha Protheus - GPE - Rotina CNAB (GPEM080) cria uma linha vazia no final do arquivo mesmo configurado como "Linha vazia no fim do arquivo = Não"](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051977133-RH-Linha-Protheus-GPE-Rotina-CNAB-GPEM080-cria-uma-linha-vazia-no-final-do-arquivo-mesmo-configurado-como-Linha-vazia-no-fim-do-arquivo-N%C3%A3o-#:~:text=Na%20gera%C3%A7%C3%A3o%20do%20arquivo%20CNAB,vazia%20no%20arquivo%20%3D%20N%C3%A3o%22.&text=Conforme%20an%C3%A1lise%20do%20incidente%2C%20constatamos,parte%20do%20conceito%20do%20CNAB.)  
  
1. Acesse Configurador > Usuário > Senhas > Configuração de Perguntas  
2. Clique em **Incluir**  
3. Em **Grupo**, digite o código do Grupo de Perguntas GPEM080R2  
4. Em **Usuário** ou **Grupo de Usuário**, selecione um usuário ou grupo para associar essa regra de configuração de perguntas  
5. Seção **Perguntas** serão exibidas as perguntas referentes a este grupo. Elas estão todas marcadas em cinza  
6. Para bloquear uma pergunta, clique sobre ela, e pressione a tecle **DEL** do teclado. Neste momento ela já estará bloqueada na rotina. Se quiser inserir um novo valor padrão, digite-o abaixo da coluna **Conteúdo**, ou em casos de campos do tipo combo, selecione o valor padrão  
7. Na imagem de exemplo abaixo, foram bloqueados os 2 primeiros campos do grupo de perguntas

![GIF_bloqueio_de_perguntas.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/13585922291607)

8) Acessar miscelânea -> Líquidos -> Geração de líquidos e verificar que não é possível editar a pergunta para outra configuração além da selecionada no grupo de perguntas via Configurador: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13586288851991)

**Saiba Mais:**  
[Artigos - CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833653-RH-CNAB)
