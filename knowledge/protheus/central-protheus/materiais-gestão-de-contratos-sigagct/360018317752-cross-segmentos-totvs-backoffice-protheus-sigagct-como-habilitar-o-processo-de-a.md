---
article_id: 360018317752
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 6e4ef8bd3845ff8ebeb0946d4c7780f0d9eac3e8542c1075eecae1d3072f1db9
fetched_at: '2026-06-28T22:37:21.521122+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como habilitar o processo
  de alçadas por Documento na inclusão da medição?
type: support-article
updated_at: '2025-12-24T11:32:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018317752-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-habilitar-o-processo-de-al%C3%A7adas-por-Documento-na-inclus%C3%A3o-da-medi%C3%A7%C3%A3o
---

**Dúvida**  
Como habilitar o processo de alçadas na inclusão da medição ?  
  
**Ambiente**  
Microsiga Protheus – Gestão de Contratos – A partir da versão 11.80  
  
**Solução**  
  
Caso se se deseje configurar o se tenha dificuldade no processo de aprovação de alçada na medição de Contrato, orienta-se realizar os seguintes passos:   
  
1. Acesse o módulo Configurador (SIGACFG);

2. Acesse o caminho Base de Dados - Dicionário - Base de Dados;

3. Localize o parâmetro **MV\_CNMDALC**;

4. Configure o mesmo como S (Sim);

5. Na inclusão do Tipo de Contrato preencha o campo Alc. Contrato (**CN1\_ALCCTR**) igual a "Documento" e informe o grupo de aprovação no campo Grp. Apr Med (**CN1\_GRPAPR**); Ao selecionar igual 0=Todos ou 1= Documento, será habilitado o campo **CN1\_GRPSIT,** o qual o preenchimento se torna obrigatório:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6898738492439)

6.  No inclusão do tipo de planilha, preencha o campo **Alc. Medição** - **CNL\_ALMED** conforme sua alçada.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10116742562455)

7. Na rotina Grupo de Aprovação(MATA114) marque na Aba Tipo de Documentos a Opção Mediçoes.

**Obs:**Para habilitar a Aba Tipo de Documentos habilite o parâmetro MV\_ALTPDOC no configurador do sistema.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4574413546647)

8. Na inclusão do contrato verifique que foi preenchido o campo Grp. Apr MD (**CN9\_GRPAPR**);

9. Na inclusão da medição certifique que o campo Aprovadores (**CND\_APROV**) estará preenchido, mas se faz necessário o Grupo de Aprovação preenchido no Tipo de Contrato;

10. Ao incluir a medição a mesma ficará com legenda cinza;

11. Acesse a rotina Liberação de Documentos (MATA094) e realize a aprovação.   
  
 Abaixo o exemplo de uma medição com o Status "Meidção Bloqueada" para liberação da alçada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013959951)

**Obs1:**

Nesta configuração de alçada são gerados na tabela de alçada SCR no Tipo de Documento (CR\_TIPO), e browse da rotina de Liberação de Documentos (MATA094) os Documentos do Tipo "**MD**" .

**Obs2:**

No caso da situação em que uma medição de determinada competencia é "Rejeitada" no seu processo de alçada e possui este status "Medição Rejeitada", para que a competencia em questão possa ser medida novamente, se faz necessário:

* ou a alteração da medição já incluida que esta "Rejeitada" para que ela passe novamente pelo processo de alçada e seja aprovada,
* ou que essa medição "Rejeitada" seja excluida, para inclusão de uma nova medição a ser aprovada novamente.

***Saiba Mais:***

[Alçada nas medições de contrato no módulo de Gestão de Contrato](http://tdn.totvs.com/pages/viewpage.action?pageId=268579126)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
