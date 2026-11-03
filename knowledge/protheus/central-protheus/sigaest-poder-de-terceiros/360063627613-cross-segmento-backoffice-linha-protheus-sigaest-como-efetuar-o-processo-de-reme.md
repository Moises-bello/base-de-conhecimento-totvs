---
article_id: 360063627613
category: SIGAEST - PODER DE TERCEIROS
content_hash: 42601c8270aba9da78047d65d07da05fd4d822dbe224dedc55435cc1a76745f8
fetched_at: '2026-06-28T22:39:03.157537+00:00'
product: protheus
section_id: 1500001538881
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como efetuar o processo
  de Remessa para Beneficiamento de OP Em Terceiros?
type: support-article
updated_at: '2026-06-19T21:30:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063627613-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-efetuar-o-processo-de-Remessa-para-Beneficiamento-de-OP-Em-Terceiros
---

O artigo explica o processo de remessa para Ordem de Produção (OP) feita em terceiros no Protheus, detalhando o cadastro de produtos, tipos de TES, abertura da OP externa, e o retorno da matéria-prima com inclusão do custo do serviço. Destaca a possibilidade de agregar ou não o custo ao produto final e orienta sobre o manejo do saldo em terceiros, além de como realizar o retorno sem baixa automática na OP.

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33398121449751) Tempo aproximado para leitura: 00:04:30 min**

**Dúvida**

Como tratar o processo de Remessa para OP feita Em Terceiros no Protheus?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Abaixo traremos um exemplo genérico desta operação. Lembrando que trata-se apenas de um processo sugestivo, haja vista que algumas empresas tratam alguns passos de formas diferentes para atender ao negócio.

Antes de entrarmos no cenário, é importante avaliarmos 2 parâmetros:

**MV\_TMPAD =** **010**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003390142)

**MV\_PRNFBEN =** **T**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003390162)

**Cenário para o processo:**

- Teremos 3 produtos:

* O PA65 (Produto Final);
* O MP65 (MP que será enviada ao Terceiro para consumo na Ordem de Produção do PA65);
* O MP66 (Criado apenas para gerar o **valor do Serviço da produção**).  ***Obs.:*** O tipo do produto a ser considerado como serviço poderia ser SV ou outra à critério da empresa.

- Teremos 3 tipos de TES:

* 504: Ele terá **F4\_ESTOQUE = Sim** e **F4\_PODER3 = R**. Ela será utilizada ao enviar a Matéria Prima MP65 para o Beneficiamento em Terceiro. Batizaremos este TES de ***REMESSAF4SIM***. Veja a imagem abaixo:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003390422)

* 007: Ele terá **F4\_ESTOQUE = Sim** e **F4\_PODER3 = D (Devolução)**. Ela será utilizada no **"retorno"** da Matéria Prima  MP65. Batizaremos este TES de ***DEVOLUÇÃOF4SIM***. Veja a imagem abaixo:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003390442)

* 001: Ele terá F4\_ESTOQUE = Sim e F4\_PODER3 = N. Ele será utilizado para gerar o valor do Serviço, ou seja, para o MP66. Batizaremos de ***NÃOCONTROLAF4SIM***. Veja a imagem abaixo:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102259014)

**1° Passo** - **Estrutura:** Após o Cadastramento dos 3 produtos via MATA010 (cadastros simples), vamos Estruturar (MATA200) o PA65 > MP65, sendo uma relação de 1:1.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102258974)

**2° Passo** - **Saldos Iniciais:** Daremos Saldo Inicial (MATA220) no nosso MP65. Este saldo será de 50 itens à custo de R$1,00;

![Saldos_Iniciais.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003406102)

**3° Passo** **- Pedido de Venda:** Faremos a remessa ao Terceiro do nosso MP65. Essa remessa será de quantidade 50 utilizando nosso TES batizado de REMESSAF4SIM (504):

![Pedido_de_Venda.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003452001)

**4° Passo** - **Abertura da OP (Y01777):** Agora que nosso MP65 já está no Terceiro (Fornecedor 01), vamos abrir a Ordem de Produção (MATA650). Ela será de quantidade 30, indicando que ela será uma **OP Tipo Externa (C2\_OP = E)**:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003450101)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003450141)

**5° e****Crucial****Passo** **- Documento de Entrada****:** Com a OP no Terceiro concluída, faremos o retorno da MP65 e aproveitaremos para incluir o valor do serviço que o Terceiro impôs para o processo produtivo.

Aqui temos alguns detalhes importantíssimos. Vamos listar abaixo:

* Primeiro ato: preencher o cabeçalho da nota, com as informações de Tipo da Nota e Cliente/Fornecedor com base na Remessa;
* Clicar em 'Outras Ações" -> "Retorno Ben" e preencher a OP e TES de Devolução (***DEVOLUÇÃOF4SIM****)*

*![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9988215545111)*

* Após clicar, será preenchido automaticamente os campos "OP", "Docto. Orig", "Serie Orig" e "it. Doc Orig.";

**6° Passo - Ajustes finais e conclusão do Documento de Entrada:**Neste momento, temos o nosso MP65 adicionando com TES para dar baixa do Poder de Terceiros vinculado à OP Externa. Agora, vamos adicionar o produto MP66 (que é o produto que criamos para gerar o valor do serviço). Nele, vamos utilizar TES 001, batizado de ***NAO CONTROLA (PODER DE TERCEIRO) F4 SIM***:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360104441673)

**IMPORTANTE:** Nesse exemplo, referente ao ***Custo do Serviço*** (produto MP66), existem **duas opções** de fluxo para **agregar** ou **não agregar** ao Custo do PA (PA65):

***- 1ª -*** Desejo que o Custo "**seja" agregado** ao Produto que foi Beneficiado (PA65). Nesse caso, ***deve informar*** na linha de item do Documento de Entrada a Ordem de Produção (D1\_OP) para que componha o Custo do Serviço no apontamento da OP.

***- 2ª -*** Desejo que o Custo "**não seja" agregado** ao Produto que foi Beneficiado (PA65). Nesse caso, ***não informar*** na linha de item do Documento de Entrada a Ordem de Produção (D1\_OP).

**7° Passo - Avaliação dos resultados**: Vamos avaliar como ficou a nossa Ordem de Produção, saldo do PA65 e se gerou automaticamente a RE5 do MP65:

SD3: Gerou PR0 do PA65 e RE5 do MP65; 

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003404022)

Saldo PA65: gerado o saldo de 30 ao PA65:

![mceclip20.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102260434)

**Informações adicionais**:

Como a nossa remessa foi de 50, mas só 30 foram consumidos na OP, o Terceiro ainda ficou com 20 itens do MP65. Esses 20 podem ficar em Terceiros para uma nova OP ou simplesmente voltar. No nosso exemplo,  vamos voltar esse saldo para o nosso Estoque.

Com isso, basta fazermos um Documento de Entrada com TES 007, batizado de ***DEVOLUCAOF4SIM***para gerar a baixa do Poder de Terceiros

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003450341)

Com isso, nosso MP65 voltará a ter Saldo de 20 em nosso estoque próprio e quantidade 0 Em Terceiros:

![mceclip23.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360104433693)

Com isso, o processo de Remessa de Beneficiamento Em Terceiros e devolução foram concluídos com sucesso.

**Como fazer retorno de beneficiamento sem dar baixa automática na OP?**

Tem como sim realizar o retorno sem apontar a OP, basta não utilizar o botão "**Retorno Ben**.".

No caso deverá:

* Preencher o código do produto e da TES;
* Clicar no campo "Quantidade" 2x e pressionar a tecla F7 para associar o retorno à nota origem;
* Preencher manualmente o campo "D1\_OP", e salvar o documento (sem utilizar o botão "retorno ben";

Desta forma o material entrará no seu estoque vinculado à OP, porém só irá ser consumido após você realizar o apontamento da mesma na MATA250 quando precisar.

**Saiba mais:**

[*MP - SIGAEST - Processo para recebimento de Beneficiamento com MP de Terceiros*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025818694--MP-SIGAEST-Processo-para-recebimento-de-Beneficiamento-com-MP-de-Terceiros)

[*Clique aqui e veja mais artigos sobre Poder de Terceiros no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012199513-SIGAEST-PODER-DE-TERCEIROS)
