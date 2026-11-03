---
article_id: 4420943576599
category: GPE - eSocial - Não Periódicos
content_hash: 37515d0936936a8e74048a85dff94e87de091c3017d424338ecc72e6f73c8107
fetched_at: '2026-06-28T22:45:04.640371+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2205 - Aviso ao alterar cadastro do
  funcionario "Campo RA_CLASEST está com o conteudo referente ao leiaute 2.5. Favor
  corrigir o campo conforme o leiaute S-1.0"
type: support-article
updated_at: '2026-06-16T11:50:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420943576599-RH-Linha-Protheus-GPE-eSocial-S-2205-Aviso-ao-alterar-cadastro-do-funcionario-Campo-RA-CLASEST-est%C3%A1-com-o-conteudo-referente-ao-leiaute-2-5-Favor-corrigir-o-campo-conforme-o-leiaute-S-1-0
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25841715671831) Tempo aproximado para leitura: **01:00:00 min**  
  
**Ocorrência**  
Aviso ao alterar cadastro do funcionario "Campo RA\_CLASEST está com o conteudo referente ao leiaute 2.5. Favor corrigir o campo conforme o leiaute S-1.0"  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**  
A mensagem **Campo RA\_CLASEST está com o conteudo referente ao leiaute 2.5. Favor corrigir o campo conforme o leiaute S-1.0**.   
Ocorre porque no leiaute simplificado do eSocial o governo fez alterações nas informações dos dados de estrangeiro. Devido a isso sempre que o usuario está fazendo alterações no cadastro de um funcionarios com dados de estrageiro onde campo Class. Estra ( RA\_CLASEST) está preenchido com informações do leiaute 2.5 a mensagem será apresentada.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4420950948631)  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse no modulo SIGAGPE (07) o caminho: atualizações > funcionarios > funcionarios **(GPEA010)** ou atualizações > funcionarios > Contr. Individual **(GPEA265)**. E entre no funcionario estrangeiro como alterar.  
  
2. Na aba **Estrangeiro** clique no campo **Class. Estra** ( RA\_CLASEST) e altere o código para o trabalhador de acordo com as opções disponiveis no eSocial Simplificado.  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4420943342871)  
  
**Observação**

* O ajuste deve ser feito para todo o trabalhador que tiver dados na aba estrangeiro para atender a regras do leiaute simplificado do eSocial.
* Essa mensagem ocorre apenas no leiaute simplificado, no leiaute 2.5 os dados do campo são diferentes.
* O ambiente deve estar com a ultima atualização liberada, para isso acesse a pagina de [**Entregas Legais.**](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)

**Saiba Mais**  
Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
