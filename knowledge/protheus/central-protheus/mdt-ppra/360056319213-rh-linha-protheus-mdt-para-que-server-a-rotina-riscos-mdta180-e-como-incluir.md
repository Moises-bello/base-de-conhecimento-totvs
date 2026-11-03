---
article_id: 360056319213
category: MDT - PPRA
content_hash: bed7271de3e7bfd65e845184c1de5b800ca18e27f101f7932f1ee79e8d10ad44
fetched_at: '2026-06-28T22:44:27.432496+00:00'
product: protheus
section_id: 360010945454
source: central-protheus
title: RH - Linha Protheus - MDT - Para que server a rotina Riscos (MDTA180) e como
  incluir
type: support-article
updated_at: '2025-10-10T11:13:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056319213-RH-Linha-Protheus-MDT-Para-que-server-a-rotina-Riscos-MDTA180-e-como-incluir
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19994447899031)** Tempo aproximado para leitura: **00:03:00 min****Dúvida**Para que serve a rotina **Riscos** (MDTA180) e como incluir um registro?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**É responsável pelo cadastro efetivo do **Risco** bem como todos os vínculos de informações. Também é informado a abrangência do risco, podendo ser: por Centro de Custo, Função ou Tarefa.   
  
Estes riscos são debatidos e estudados na área de segurança e saúde do trabalho, principalmente na elaboração e implementação dos programas de **PPRA** e **PCMSO**. O controle de riscos de uma empresa se torna necessário principalmente por dois fatores:   
  
1. Ter dados suficientes para elaboração de um PPRA conciso;   
2. Ter controle de possíveis doenças ocasionadas aos funcionários durante o trabalho, evitando assim a incidência de processos cíveis que a empresa possa necessitar responder.  
  
O **risco** no módulo de Medicina e Segurança do Trabalho é cadastrado de forma estruturada para que as informações sejam adquiridas separadamente, permitindo informações mais genéricas quando possível e cadastros finais mais detalhados.

Antes de Cadastrar um risco é necessário verificar se existe a configuração dos seguintes processos:  
  
**Agente**  
Em caso de duvidas acesse o artigo: [MP - MDT - O que é Agente de Risco e quais as categorias dos agentes causadores de risco](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049964453)  
  
**Fonte Geradora**  
Em caso de duvidas acesse o artigo: [MP - MDT - Para que serve a rotina Fonte Geradora (MDTA095) e onde fazer os cadastros no sistema](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054490414)  
 **Tarefa**  
Em caso de duvidas acesse o artigo: [MP - MDT - Para que server a rotina Tarefas Por Funcionário (MDTA090) e como incluir](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055465733)  
  
**Centro de Custo**O conteúdo provindo deste campo diz respeito a fonte geradora da tabela Centro de Custo (CTT).   
 **Função**O conteúdo provindo deste campo diz respeito a fonte geradora da tabela Função (SRJ).   
  
Campos e Informações no cadastro do Risco:

* **Número Risco:** Código de controle interno do risco. Este código é gerado sequencialmente pelo próprio sistema;
* **Data Reconhecimento:** Data em que o risco foi reconhecido como tal na empresa;
* **Agente:** Código do agente relacionado ao risco. Consulta padrão (F3) disponível;
* **Fonte Geradora:** Código da fonte geradora do risco. Consulta padrão (F3) disponível.
* **Centro Custo:** Código do centro de custo onde está presente o risco. Neste campo pode ser informado “**\***” caso o risco seja comum entre todos os centros de custo. Consulta padrão (F3) disponível;
* **Função:** Código da função que exerce exposição ao risco. Neste campo pode ser informado “**\***” caso o risco seja comum entre todas as funções. Consulta padrão (F3) disponível.
* **Tarefa:** Código da tarefa que está exposta ao risco. Neste campo pode ser informado “**\***” caso o risco seja comum entre todas as tarefas.

Adicionais: Com objetivo de armazenar o máximo de informações sobre o risco, a rotina apresenta campos como:

* **Data Avaliação:** Data em que foi realizado a quantificação do risco;
* **Data Eliminação:** Data em que o risco foi eliminado da empresa;
* **Agente:** Define a quantidade de agente encontrado no local do risco;
* **Unidade Medida:** Define a unidade de medida utilizada para quantificar o agente;
* **Tempo Exposição:** Tempo em que os funcionários ficam expostos ao risco;
* **Repetição:** Quantidade de vezes em que pode repetir a exposição ao risco;
* **Intervalo:** Período de tempo entre uma exposição e outra;
* **Considerar:**  Define em que lugares deve ser impresso informações sobre a exposição ao risco, podendo ser: ASO, Nenhum, ASO e PPP ou PPP;
* **Grau Risco:** Identificação do tamanho do risco, podendo ser: Pequeno, Médio ou Grande;
* **Mapa Risco:** Indica em qual mapa o risco deve ser apresentado, podendo ser: CIPA, SESMT ou AMBOS;
* **Ambiente**: Código do ambiente físico onde o risco está localizado;
* **Tipo Exposição**. Indica o tipo de exposição do risco, podendo ser: Habitual/Permanente, Ocasional/Intermitente, Ausência de Agente Nocivo, Eventual ou Habitual/Intermitente;
* **Complemento Exposição:** Descritivo complementar ao tipo de exposição;
* **EPC Eficaz:** Informa se o equipamento de proteção coletiva é eficaz contra o risco;
* **Necessário EPI:** Indica se para a exposição ao risco é necessário a utilização de equipamento de proteção individual;
* **Fase Obra:** Código da fase da obra a ser vinculada ao risco;
* **Subfase:** Código da subfase da obra;
* **Atividade Insalubre:** Indica se a exposição ao risco é insalubre, podendo ser: Salubre ou Insalubre;
* **Atividade Periculosa:** Indica se a exposição ao risco é periculosa ou não, podendo ser: Não Periculosa ou Periculosa;
* **Enquadramento Legal:** Descritivo do enquadramento legal do risco quanto a insalubridade ou periculosidade;
* **Técnica Utilizada:** Descritivo da técnica de medição utilizada para quantificar o agente;
* **Adicional:** Indica o tipo de adicional que o risco fornece. Este campo é de preenchido automático pelo sistema;
* **Categoria do Risco:**. Indica qual categoria se aplica ao risco, podendo ser: Irrelevante, De Atenção, Crítica ou Intolerável;
* **Intensidade:**. Indica o percentual de intensidade do risco, podendo ser: 10%, 20%, 30%, 40% ou Não Caracteriza;
* **Adicional Folha:** Indica se o risco gera adicional em folha de pagamento, podendo ser: Sim ou Não. Se possuir adicional (opção “S”), envia e-mail para o RH comunicando;
* **Danos Causados:** Descritivo que indica os danos causados ao funcionário por conta da exposição ao risco;
* **Situação Encontrada:** Descritivo da situação ergonômica encontrada no local do risco. Campo habilitado apenas para agente do tipo ergonômico;
* **Situação Desejada:** Descritivo da situação ergonômica desejada no local do risco. Campo habilitado apenas para agente do tipo ergonômico;

**Status:** Informa a situação ergonômica atual do risco, podendo ser: Adequada ou Inadequada. Campo habilitado apenas para agente do tipo ergonômico.  
  
É possível na parte inferior da tela vincular **medidas de controle ao risco**. Para isso, basta informar o campo Controle com o código da medida de controle. Consulta padrão (F3) disponível.

Em caso de dúvidas acesse: [MP - MDT - Para que server a rotina Medidas Controle (MDTA135) e como incluir](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054498154)  
  
No menu Outras Ações > **Prod. Químicos**, é possível vincular ao risco um produto químico, basta informar o código do produto químico cadastrado. Esta opção está disponível apenas para agentes do tipo “Químico”.  
Em caso de dúvidas acesse: [MP - MDT - Para que serve a rotina Produtos Químicos (MDTA183) e onde fazer os cadastros no sistema](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054492094)  
  
No menu Outras Ações > **Func. Exp. Risco**, é possível visualizar todos os funcionários expostos com base nos dados preenchidos sobre o risco.  
  
Para cadastrar uma tarefa acesse no modulo **SIGAMDT (35)** o caminho: Atualizações > PPRA > Riscos.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360092212194)  
  
OBS: Não pode ter espaço antes e após no preenchimento dos campos com \* (asteriscos) conforme documentação.

**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
