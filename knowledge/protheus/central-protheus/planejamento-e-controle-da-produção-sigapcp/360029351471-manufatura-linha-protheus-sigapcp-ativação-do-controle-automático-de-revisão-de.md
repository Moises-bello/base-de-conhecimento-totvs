---
article_id: 360029351471
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 09463d6c7b008d00ba44ad047ce67ee072568264b2a0ca4b725c0fb3e5a89fcd
fetched_at: '2026-06-28T22:42:40.865742+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Ativação do controle automático de
  revisão de estruturas
type: support-article
updated_at: '2023-08-04T13:13:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029351471-Manufatura-Linha-Protheus-SIGAPCP-Ativa%C3%A7%C3%A3o-do-controle-autom%C3%A1tico-de-revis%C3%A3o-de-estruturas
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16530141830039)***Tempo aproximado para leitura: **00:02:23 min****Dúvida**Como fazer uso do **controle de revisões automáticas** no **cadastro de estruturas**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**O **controle automático das revisões de estruturas** permite que ao incluir, excluir ou alterar alguma informação, de acordo com os campos informados na rotina **PCPA116 - Campos para Edição**, uma nova revisão de estrutura seja criada**.**Porém, para iniciar o uso do **controle de revisões automáticas** é necessário realizar alguns ajustes no ambiente, sendo eles descritos nos passos abaixo:   
  
1. Verifique através do **PCPA200 - Manutenção de Estruturas**, em todas as estruturas cadastradas, se os campos **G1\_REVINI - Revisão Inicial do Componente** e **G1\_REVFIM** **- Revisão Final do Componente** estão preenchidos com valores válidos na faixa **de 001 até 999**, sendo que o conteúdo do campo **G1\_REVFIM** deve ser menor ou igual ao valor da revisão que está informada no **MATA010 - Cadastro de Produtos**, no campo **B1\_REVATU - Revisão Atual da Estrutura.**Atente-se para o campo **B1\_REVATU**, se o campo **B1\_REVATU** estiver em branco, ele deve ser preenchido com **001** e todos os componentes da estrutura desse item devem ter os campos **G1\_REVINI** e **G1\_REVFIM** preenchidos com **001.**  
**Exemplo**  
Estrutura com produto acabado na **revisão 003**, e um produto intermediário na **revisão 002.**

![Imagem.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003541341)

Revisão dos **componentes** utilizando **revisão manual**:

![Imagem02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030542151)

Revisão atualizada do **produto acabado** e do **produto intermediário**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030575392)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030541651)

Revisão inicial e final dos **componentes da estrutura** alterados para trabalhar com a **revisão automática**.

![Imagem05.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030541971)

2. Altere o conteúdo do parâmetro **MV\_REVAUT** - **Indica se o controle de revisões será controlado automaticamente** para **T**;  
  
3. Por meio da rotina **PCPA116 - Campos para Edição**, configure os campos que quando tiverem seu conteúdo alterado também devem resultar numa nova **revisão de estruturas**.
