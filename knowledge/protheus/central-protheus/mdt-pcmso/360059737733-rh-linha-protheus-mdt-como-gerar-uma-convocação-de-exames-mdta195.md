---
article_id: 360059737733
category: MDT - PCMSO
content_hash: 12cd2c591eef3414617cf146918deb98be11d7b0f30d9bfb57ccaea2c39db190
fetched_at: '2026-06-28T22:44:28.415606+00:00'
product: protheus
section_id: 360010945214
source: central-protheus
title: RH - Linha Protheus - MDT - Como Gerar uma Convocação de Exames (MDTA195)
type: support-article
updated_at: '2025-09-03T14:02:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059737733-RH-Linha-Protheus-MDT-Como-Gerar-uma-Convoca%C3%A7%C3%A3o-de-Exames-MDTA195
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27597822216343)**Tempo aproximado para leitura: 00:01:00 min  
 **Dúvida**Como Gerar uma Convocação de Exames (MDTA195)?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Esta rotina gera a **convocação dos funcionários** para realizarem os **exames periódicos** com base nos parâmetros informados: data de início e término da programação, médico que irá realizar os exames, calendário do horário de trabalho do médico, tempo médio de atendimento e código do exame desejado.  
  
A convocação será realizada com base na programação gerada pelo programa. Os funcionários que possuírem exames programados no período especificado e se enquadrarem nos parâmetros definidos, serão convocados para a realização dos exames periódicos.  
  
O Sistema irá marcar a consulta na agenda do médico, com a observação da data de início e término de realização e incremento do horário de atendimento, conforme o tempo estimado pelo médico para o atendimento de um paciente.

Nesta rotina é possível gerar a **convocação de exames** uma única vez para **diversas filiais,** quando a tabela TMV estiver em modo compartilhado. Basta apenas informar o campos “De Filial (TMV\_FILDE)” e “Até Filial (TMV\_FILATE)” com as filiais desejadas.  
  
Ao utilizar o botão “**Multi inclusão**” é possível selecionar mais de um exame da programação para realizar a inclusão da convocação. A partir deste botão diminuirá a possibilidade de deixar algum exame sem convocação.

Para gerar Convocação acesse o Módulo 35 (SIGAMDT), no seguinte caminho: **Atualizações > PCMSO > Gerar Convocação.  
1.** Na janela de Gerar Convocação, observe as opções no browse:  
• Pesquisar  
• Visualizar  
• Incluir  
• Multi Inclusão (Nesta opção serão apresentados em tela os exames cadastrados e que permitirá selecioná-los.)

• Excluir  
**2.** Para gerar uma nova convocação, selecione a opção "Incluir".  
O Sistema apresenta a tela de inclusão.

**3.** Preencha os campos conforme orientação do help de campo.  
**4.** Confira os dados e confirme a inclusão.  
  
Exemplo da utilização do botão **Multi inclusão**:  
  
![20201123_090300.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360098120414)  
  
Exemplo de Cadastro:

**![20201123_091949.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360100378893)****Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[MP - MDT - Como Gerar Programação (MDTA190)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059737173)  
[Artigos PCMSO](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945214-MDT-PCMSO)
