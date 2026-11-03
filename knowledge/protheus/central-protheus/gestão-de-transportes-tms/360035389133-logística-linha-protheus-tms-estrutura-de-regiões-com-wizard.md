---
article_id: 360035389133
category: Gestão de Transportes (TMS)
content_hash: 5ebcba5bc314f87196073dbb6b397ab7f38669b57aa001e16b67519828866064
fetched_at: '2026-06-28T22:45:27.731515+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Estrutura de regiões com Wizard
type: support-article
updated_at: '2023-10-31T19:17:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035389133-Log%C3%ADstica-Linha-Protheus-TMS-Estrutura-de-regi%C3%B5es-com-Wizard
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:03:00 min**  
**Dúvida**Como configurar a **Estrutura de Regiões** utilizando o **Wizard**?  
  
**Ambiente**

TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Esta rotina tem como finalidade, determinar a área de atuação da transportadora, informando as hierarquias existentes entre as **regiões de atendimento**, **estados** e **filiais da transportadora**.  
  
Ao cadastrar a **estrutura de regiões**, são definidas as regras de hierarquia de atendimento as quais serão utilizadas em outros pontos do Sistema, tais como:

* **Cálculo de Frete**;
* **Rotas de Transferência**;
* **Determinar Distâncias**;
* **Tabela de Frete**;
* **Ajuste de Frete**;
* **Cópia de Ajustes**.

O cadastro da **estrutura de regiões** fica localizado em **Atualizações\Logística\Estrutura de Regiões - TMSA120**.  
  
O **Wizard** de cadastro, é um facilitador para o manuseio do cadastro de regiões. Ele é apresentado quando, na janela principal da rotina **Estrutura de Regiões**, o usuário clica com o botão direito na opção **Wizard**.  
  
Quando a **estrutura de regiões** é criada pelo **Wizard**, o código das regiões é criado automaticamente, baseando-se no código de cidades do **IBGE**.  
  
Ao ser acionado, o **Wizard** apresenta dois painéis ao lado da estrutura. O primeiro painel contém os seguintes **botões**:

* **Selecionar Tudo;**
* **Incluir Item Selecionado na Árvore da estrutura de regiões;**
* **Excluir item posicionado na árvore da estrutura de regiões.** Tem a mesma funcionalidade da opção **Excluir,** do menu de **opções;**
* **Desmarcar tudo;**
* **Pesquisar no Grid:** Essa opção chamará uma janela contendo o **índice de pesquisa do grid** em questão**;**

O segundo painel contém 4 pastas a seguir:

* **Estado**
* **Filial**
* **Código do Município**
* **Grp. Região**

Para cadastro da mesma, com o **Wizard** aberto, posicione o cursor na pasta da esquerda no item desejado e no **Wizard** selecione quais itens deseja relacionar a estrutura.   
  
**Importante**  
Sugerimos que a estrutura criada, siga a hierarquia demonstrada no vídeo, sendo:

* O **país** no topo da estrutura;
* Abaixo dele os **estados**;
* Dentro de cada estado, a **filial** que corresponde ao estado em questão;
* E abaixo das filiais e estados as **cidades** que a transportadora atende.

Com a estrutura desenhada da forma sugerida, evitará que ao emitir **CT-e** e **MDF-e** não apresente erros de rejeição devido as regiões envolvidas no processo.  
  
Atentar-se também para o preenchimento do parâmetro **MV\_CDRORI**, pois é necessário fazer o relacionamento das regiões. Neste parâmetro deve ser informado qual o **código da região da transportadora**, ou seja, **código do município** criado pela estrutura de regiões. Lembrando que, o mesmo deve ser criado por filial, onde cada filial deverá informar o código ao qual a mesma se encontra.  
  
**Glossário  
CT-e** - Conhecimento de Transporte Eletrônico;**IBGE** -Instituto Brasileiro de Geografia e Estatística;  
**MDF-e** - Manifesto Eletrônico de Documentos Fiscais.  
  
**Anexo**Vídeo demonstrando o processo para cadastro da estrutura:
