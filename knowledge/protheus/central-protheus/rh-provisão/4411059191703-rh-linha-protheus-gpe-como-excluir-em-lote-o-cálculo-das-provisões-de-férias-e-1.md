---
article_id: 4411059191703
category: RH - Provisão
content_hash: 465ddf4bcde47847859e92a7c421dcce9b2544b7632f6ce75d4dd59a454eabf5
fetched_at: '2026-06-28T22:43:56.896555+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Como Excluir Em Lote o Cálculo das Provisões de
  Férias e 13º Salário
type: support-article
updated_at: '2024-05-14T13:42:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411059191703-RH-Linha-Protheus-GPE-Como-Excluir-Em-Lote-o-C%C3%A1lculo-das-Provis%C3%B5es-de-F%C3%A9rias-e-13%C2%BA-Sal%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19193227024919) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Como Excluir Em Lote o Cálculo das Provisões de Férias e 13º Salário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Implementada a possibilidade de exclusão em lote de cálculos de provisão na rotina **GPEA070**, através do botão "Exclusão em lote" disponível em "Outras Ações".   
Ao clicar nessa opção será exibido uma janela, onde será possível efetuar um filtro dos dados através da Data de/Data Até de cálculo, Filial, Matrícula, Centro de custo, Situação de folha e Categoria do funcionário.  
  
A melhoria depende da aplicação da atualização liberada no pacote de expedição do módulo RH a partir de **27/08/2021** e da execução do **UPDDISTR** com o dicionário diferencial para os releases iguais ou superiores a versão 12.1.25.  
  
Para acessar o pacote RH Expedição Contínua da Versão 12.1.2210, acesse: [Clique Aqui](https://suporte.totvs.com/portal/p/10098/download?e=1080347)  
Para acessar o pacote RH Expedição Contínua da Versão 12.1.2310, acesse: [Clique Aqui](https://suporte.totvs.com/portal/p/10098/download?e=1123885)  
  
Para release 12.1.17, o ajuste deverá ser feito **manualmente**.  
  
Foi efetuado a criação do grupo de perguntas GPM070EXCL, conforme estrutura abaixo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411058843799)

Para excluir as provisões em lote, realize os seguintes passos:  
  
1. Acesse: Miscelanea > Provisões > Provisões de Férias/13º Salário (GPEA070), em seguida clique em Outras Ações e Exclusão em Lote;

2. Clique em Outras Ações > Parâmetros, e preencha as perguntas para exclusão dos cálculos das provisões e clique em Confirmar:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23469547276567)  
  
**Data De?** : Deve ser informada a data Inicial para exclusão das provisões;

**Data Até?** : Deve ser informada a data Final para exclusão das provisões;

**Filial?** : Deve ser informada uma ou mais Filiais para exclusão das provisões. Para excluir provisões de Todas as Filiais informe o intervalo " -ZZZZZZZZZZ" ou insira a primeira e última filiais separadas por um traço;

**Matricula?** : Deve ser informada uma ou mais Matrculas para exclusão das provisões. Para excluir provisões de Todos os funcionários informe o intervalo "000000-999999" ou insira a primeira e última matriculas separadas por um traço;

**Centro de Custo?** : Deve ser informado um ou mais Centros de Custos para exclusão das provisões. Para excluir provisões de Todos os Centros de Custos informe o intervalo " -ZZZZZZZZZZZZZ" ou insira o primeiro e último Centro de Custo separados por um traço;

**Situações?** : Selecione a Situação dos funcionários, para exclusão das provisões. Podem ser selecionadas Todas as Situações;

**Categorias?** : Selecione a Categoria dos funcionários, para exclusão das provisões. Podem ser selecionadas Todas as Categorias.

3. Após finalizar o processo, será exibido um log de ocorrências com as Matriculas, Filiais, Data da Provisão, Tipo de Provisão e Verbas que foram excluídas:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23469547288855)  
  
  
  
**Saiba Mais:**[Documentação Técnica](https://tdn.totvs.com/pages/releaseview.action?pageId=634287667)  
[Protheus - RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
