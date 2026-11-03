---
article_id: 360019721132
category: GPE - eSocial - Periódicos
content_hash: 1449644704dd8d945d9e900117384d9a96392d61b66090bc7725f2dbba74746c
fetched_at: '2026-06-28T22:45:08.848456+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200/S-2299 - O valor 'x' informado
  na tag 'ideTabRubr' não existe na base dados
type: support-article
updated_at: '2025-07-22T13:30:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019721132-RH-Linha-Protheus-GPE-eSocial-S-1200-S-2299-O-valor-x-informado-na-tag-ideTabRubr-n%C3%A3o-existe-na-base-dados
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16977911407639)**Tempo aproximado para leitura**: 00:01:00 min**  
  
**Ocorrência**  
S-1200/S-2299 - "O valor 'x' informado na tag '**ideTabRubr**' não existe na base dados"  
  
Exemplo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407075768983)  
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**  
A mensagem de erro ocorre na integração dos eventos do **GPE** com o **TAF**, os problemas mais comuns são:  
  
**Caso 1:** A Verbas/Rubrica não foi integrada, ou seja, não existe um evento S-1010 com o mesmo código de Rubrica na base do TAF ou o inicio de validade é posterior ao evento que está tentado gerar.  
  
**Caso 2:** Problemas no compartilhamento das tabelas SRV, C8R ou T3M.  
  
**Caso 3:** Ambiente desatualizado.   
  
**Solução**  
**Caso 1:** Acesse o módulo do TAF e verifique se a Rubrica informada no erro existe na base do TAF.  
Utilizando o exemplo da imagem anexa, o valor "0101" deverá ser localizado na tabela T3M, campo T3M\_CODERP. Após essa localização, anote o conteúdo do campo T3M\_ID.  
Dentro da rotina de Rubricas (Módulo 84> Atualizações> Eventos Esocial> Tabelas- Rubricas), precisa existir uma rubrica cujo o conteúdo do campo Iden. Tab. Rub - C8R\_IDTBRU seja exatamente igual ao T3M\_ID.  
  
Caso não encontre a rubrica nessa rotina, realize sua integração da rubrica pela rotina Carga Inicial. O artigo abaixo lhe ajudará nesse processo:  
[RH - Linha Protheus - GPE - eSocial - S-1010 - Após a transmissão dos eventos iniciais (carga inicial), como enviar um único registro para o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046341633)  
  
**Caso 2:** Verifique o se o compartilhamento encontra-se conforme documentação abaixo:   
[RH - Linha Protheus - GPE - eSocial - Como deve ser definido o Compartilhamento de Tabelas SIGAGPE x SIGATAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004178832-MP-GPE-eSocial-Como-deve-ser-definido-o-Compartilhamento-de-Tabelas-SIGAGPE-x-SIGATAF-?source=search)  
  
**Caso 3:** Realize a aplicação dos últimos pacotes conforme o link abaixo:  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)

**Importante**: As Tabelas **T3M**e **C1E**são do**TAF** devem ser **totalmente** **compartilhadas** em qualquer cenário: [http://tdn.totvs.com/x/sIutEw](https://tdn.totvs.com/x/sIutEw)

**Saiba Mais**  
Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://informa.totvs.com/)   
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Para conhecimento dos eventos futuros, acessa a nossa página [***TOTVS Informa***](https://informa.totvs.com/) selecione em categorias a área e pesquise por "**Eventos**".
