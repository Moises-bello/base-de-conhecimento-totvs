---
article_id: 360004941012
category: GPE - eSocial - Não Periódicos
content_hash: 52c6f7472faa609731f80744a403734c7b39d7b75b2c67b8d41c865349d5058d
fetched_at: '2026-06-28T22:45:04.575313+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2200 - Como alterar a Categoria eSocial
  do Trabalhador? O sistema emite o aviso "A categoria esocial pode ser alterada dos
  tipos 102/103/105/106/111 para 101" sempre que tento efetuar uma alteração de categoria
type: support-article
updated_at: '2026-06-15T19:43:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004941012-RH-Linha-Protheus-GPE-eSocial-S-2200-Como-alterar-a-Categoria-eSocial-do-Trabalhador-O-sistema-emite-o-aviso-A-categoria-esocial-pode-ser-alterada-dos-tipos-102-103-105-106-111-para-101-sempre-que-tento-efetuar-uma-altera%C3%A7%C3%A3o-de-categoria
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41245025522839)** Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Como alterar a Categoria eSocial do Trabalhador? O sistema emite o aviso "A categoria esocial pode ser alterada dos tipos 102/103/105/106/111 para 101" sempre que tento efetuar uma alteração de categoria.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053747354)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**  
Conforme regras de validação do *layout* 1.3 descrita abaixo não é permitida a alteração de qualquer categoria. Por esse motivo o sistema emite o aviso "A categoria esocial pode ser alterada dos tipos "[**102, 103, 105, 106, 107, 108, 111**] para [**101**] ou de [**101, 103**] para [**111**]", ao tentar fazer alteração de categorias.  
  
**REGRA\_ALTERA\_CATEG:**  
Só é permitida alteração de categoria de trabalhadores de [102, 103, 105, 106, 107, 108, 111] para [101] ou de [101, 103] para [111]. Não pode ser alterada nos demais casos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41245053018007)  
<https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-s-1-3-nt-06-2026-rev-09-04-2026/regras.html>

**Solução**  
**1.** Caso o trabalhador com a categoria incorreta ainda não esteja no RET (governo), deve ser feita a exclusão no **RH** e **TAF** e depois cadastrar o trabalhador novamente;  
  
**2.** Caso o trabalhador esteja no mês de admissão com a categoria incorreta e já esteja no RET é necessário fazer a exclusão no **TAF** enviar o evento S-3000 (exclusão) para o governo, depois excluir no **RH**.  
  
**3.** Caso o trabalhador não esteja no mês de admissão (**trabalhador antigo**) e foi enviado para o RET com a categoria incorreta, será necessário excluir no **TAF** todos os eventos posteriores ao **S-2200** (folha, afastamentos, etc. gerando o evento **S-3000**).  
Excluir o **S-2200** (trabalhador) no TAF e enviar o S-3000 (exclusão) para o governo.  
No **SIGAGPE** o sistema não vai permitir a alteração da categoria devido as regras do *layout* do eSocial. A única forma de fazer essa alteração é desabilitar os parâmetros do **eSocial** **MV\_RHTAF** e**MV\_EFDAVIS**. Depois de ajustar a categoria habilitar o parâmetro e fazer qualquer alteração no cadastro para o sistema enviar o S-2200 para o TAF, onde será possível transmitir todos os eventos, ou executar a carga inicial somente para esse trabalhador.  
  
**Importante:**

* Deve existir a ciência que esse não é o procedimento padrão e que o governo em nenhum local informa que pode ser alterada a categoria de trabalhadores antigos, sendo de responsabilidade da empresa qualquer problema que venha a ocorrer.
* Caso desabilite o parâmetro para ajuste no GPE certifique-se que nenhum usuário fará integração enquanto o parâmetro estiver desabilitado para não ocorrer erros.
* Sendo assim recomendamos que efetue o contato com o governo para verificar como deve ser tratado esse caso especifico: [Contato eSocial](https://www.gov.br/esocial/pt-br/canais_atendimento)

**Saiba Mais**  
Para saber mais consulte os *links* abaixo:   
[Artigos S-2200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052505613)   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
[Chatbot eSocial](https://chat-app.meudroz.com/#/prechat?header=false&token=dG90dnMtdXNlci0yOkFrVGllLDIwMTck&customerKey=totvs&openDelay=0&typingDelay=2500&watsontoken=false&watsonuser=false&watsonurl=false)
