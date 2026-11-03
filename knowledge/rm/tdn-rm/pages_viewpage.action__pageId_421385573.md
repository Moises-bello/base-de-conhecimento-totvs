---
content_hash: da523c195d17a746fa4fcd96756b0c1a95d420643e5e802fe69fdbcc341efdbf
fetched_at: '2026-06-29T00:09:16.840000+00:00'
page_id: '421385573'
product: rm
source: tdn-rm
title: Fórmulas Visuais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385573
version: 1
---

**Fórmulas Visuais**   
Criadas as seguintes atividades workflows para complementar o módulo de fórmulas visuais:  
 - Cálculo do Projeto.  - Cálculo do Cronograma(atividade e serviços).  - Cálculo do Avanço Físico.  
Para realizar o cadastro da atividade, os seguintes passos devem ser realizados:  
1 - Incluir um novo registro informando os campos obrigatórios:  Descrição - Deve ser informada uma breve descrição para a atividade da fórmula Visual.  Nome da Classe - Deve ser informado o nome da classe que será utilizada na atividade de fórmula visual.  Nome do Assembly - Deve ser infomado o nome do assembly referente a tela que será utilizado na atividade de fórmula visual.  Ativo - Habilitado ou desabilitado.  
**Observação:**  
Dúvidas com relação ao preenchimento dos campos, entrar em contato com o setor TI da sua empresa.  
2 - Uma vez incluídas as atividades, as mesmas ficam disponíveis para utilização no editor de fórmulas visuais.  
Atividades:  
Calcular Projeto  
Esta atividade realiza o cálculo do projeto, baseando-se nos seguintes parâmetros:  
• CodigoColigada(código da coligada): Código da coligada corrente do projeto. • IdProjeto(identificador do projeto): Número de identificação referente ao projeto. • Usuario(código do usuário): Código do usuário logado ao sistema. Se os parâmetros não forem informados, a atividade busca os parâmetros do contexto atual.  
Calcular Cronograma de Serviços  
Esta atividade realiza o cálculo do cronograma de serviços, baseando-se nos seguintes parâmetros:  
• CodigoColigada(código da coligada): Código da coligada corrente do projeto. • IdProjeto(identificador do projeto): Número de identificação referente ao projeto. • Usuario(código do usuário): Código do usuário logado ao sistema. Se os parâmetros não forem informados, a atividade busca os parâmetros do contexto atual.  
Calcular Cronograma de Atividades  
Esta atividade realiza o cálculo do cronograma de atividades, baseando-se nos seguintes parâmetros:  
• CodigoColigada(código da coligada): Código da coligada corrente do projeto. • IdProjeto(identificador do projeto): Número de identificação referente ao projeto. • Usuario(código do usuário): Código do usuário logado ao sistema. Se os parâmetros não forem informados, a atividade busca os parâmetros do contexto atual.  
Calcular Avanço Físico  
Esta atividade realiza o cálculo do avanço físico do projeto, baseando-se nos seguintes parâmetros:  
• CodigoColigada(código da coligada): Código da coligada corrente do projeto. • IdProjeto(identificador do projeto): Número de identificação referente ao projeto. • Usuario(código do usuário): Código do usuário logado ao sistema. Se os parâmetros não forem informados, a atividade busca os parâmetros do contexto atual.  
A utilização das fórmulas serão aplicadas no "Processos - Fórmula Visual" do Assembly informado.  
   
**Exemplo:**  
Cálculo do Projeto  
Criar uma fórmula seguindo os passos citados acima, informando o Assembly Planilha de Atividades. Na planilha de atitividades, clique no botão "Processos - Fórmula Visual" e selecione o nome informado para a fórmula.
