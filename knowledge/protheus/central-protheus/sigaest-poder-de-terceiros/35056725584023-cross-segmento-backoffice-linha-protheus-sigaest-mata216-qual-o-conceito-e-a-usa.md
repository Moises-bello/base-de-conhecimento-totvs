---
article_id: 35056725584023
category: SIGAEST - PODER DE TERCEIROS
content_hash: 8e0aaa8c3ef92eae8c162997387d3395e444f574515c798bb5d482e773900e7e
fetched_at: '2026-06-28T22:39:03.220642+00:00'
product: protheus
section_id: 1500001538881
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA216: Qual o conceito
  e a usabilidade da rotina "Refaz Poder de/em Terceiros"?'
type: support-article
updated_at: '2025-09-19T14:14:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35056725584023-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA216-Qual-o-conceito-e-a-usabilidade-da-rotina-Refaz-Poder-de-em-Terceiros
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35056725568407) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Qual é o conceito e a usabilidade da rotina "Refaz Poder de/em Terceiros"?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.33 ou Superior.  
  
**Solução**  
  
A rotina **MATA216 – Refaz Poder de/em Terceiros** tem como objetivo **recalcular e atualizar os saldos de terceiros** na tabela **SB6**.

Essa rotina é usada quando:

* Os saldos de Poder de/em Terceiros estão incorretos;
* Existem registros indevidos na SB6.

O conceito utilizado para a correção é **excluir** as informações da tabela, física ou logicamente, conforme o parâmetro [**MV\_DL216B6**](https://tdn.totvs.com/pages/viewpage.action?pageId=312165442#:~:text=MV_DL216B6,2%20%2D%20Logicamente%2C), permitindo que o sistema reconstrua os dados a partir das tabelas **SD1 e SD2.**  
  
  
**Exemplo de utilização:**

Um pedido foi faturado com um TES que controle poder de/em Terceiros como remessa (F4\_PODER3 = R), porém por algum motivo o sistema não gerou os saldos devidos de controle de poder de/em terceiros na tabela SB6.   
  
Ao executar a rotina **"Refaz Poder de Terceiros"**, o sistema analisa as tabelas SD1 e SD2 para recriar os registros na SB6, desde que os dados estejam corretamente gravados nessas tabelas. Sendo a rotina de Refaz poder de/em Terceiros o primeiro passo para correção de saldos indevidos na SB6.  
  
  
**E se a execução da rotina não corrigir o meu saldo?**

Esse tipo de comportamento pode ocorrer por diversos fatores, porém estarei listando abaixo alguns mais comum.

1. Filtro de produto incorreto na tela de parâmetros da rotina.  
   Neste caso verifique se no filtro "De produto?" e "Até produto?" está com o código de seu produto devidamente informado.
2. Movimentação efetuada com TES que não controla Poder de/em Terceiros ou registros indevidos.  
   Neste caso revise o documento que deve gerar ou abater o saldo de sua SB6 junto às configurações dos TES utilizados.
3. Pontos de entrada e/ou customizações que impactam na gravação direta/ indireta da SB6.  
   Efetuei um teste desativando todos os Pontos de entradas e customizações, conforme documentação abaixo:  
   [**Como desabilitar customizações através do catálogo de personalização do Configurador?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018286552-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-desabilitar-customiza%C3%A7%C3%B5es-atrav%C3%A9s-do-cat%C3%A1logo-de-personaliza%C3%A7%C3%A3o-do-Configurador)
4. Filtro ou inconsistencia diretamente na Procedure da rotina (Procedure 15).  
   Para esse cenário a sugestão é efetuar um teste sem a Procedure instalada e caso o registro seja corrigido efetuar um novo teste com a procedure instalada conforme a documentação abaixo:  
   [**Backoffice (Linha Protheus) - SIGAEST - Procedure Desatualizada ou Incompatível**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15131065568791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Procedure-Desatualizada-ou-Incompat%C3%ADvel?source=search)

Caso após válido não possuia nenhum dos pontos acima, por favor nos envie para o suporte as seguintes informações:

* Qual saldo entende que seria o correto, e qual saldo esta sendo apresentado;
* Já foi executado a rotina para o Produto?;
* Qual seria o passo a passo para simularmos o mesmo comportamente (Se possivel em video);
* Como estão cadastrados os TES envolvidos
* Se efetuar um teste com produtos/ TES novos ocorre o mesmo resultado?
* Inspetor de Objetos para analisarmos os fontes envolvidos

---

**Importante:**

* Por a tabela SB6 se tratar de uma tabela de saldos, a rotina MATA216 - Refaz Poder de/em terceiros não se utiliza do parametro MV\_ULMES para sua execução, corrigido assim toda a tabela independente de data de Emissão;
* Devido a rotina se utilizar da procedure para ganho de performance pode ser que ocorra o erro genérico "[**Erro na chamada do processo**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000275147-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Erro-na-chamada-do-processo-em-rotinas-de-Processamento)", para esses casos já possuimos a documentação de apoio na avaliação e correção;
* A utilização da rotina com a procedure não é obrigatória, porém a execução da rotina sem a mesma pode gerar queda na perfomance da rotina sendo um comportamento normal.

Saiba mais:

[*Clique aqui e veja mais artigos sobre Poder de Terceiros no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012199513-SIGAEST-PODER-DE-TERCEIROS)

[*SIGAEST - MATA216 - Quais Pontos de Entrada disponíveis na rotina*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11880516362263-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA216-Quais-Pontos-de-Entrada-dispon%C3%ADveis-na-rotina)

[SIGAEST - Como eliminar saldo em Poder de terceiro (retorno simbólico)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010519121-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-eliminar-saldo-em-Poder-de-terceiro-retorno-simb%C3%B3lico)
