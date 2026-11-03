---
article_id: 15070592052375
category: RH - Rescisão
content_hash: 6ffa5e93dee35f4b70887d3c64dee1c372c377a92ff40396544bd174afb053f6
fetched_at: '2026-06-28T22:43:49.743885+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Importação dos resultados ponto eletrônico em rescisão
type: support-article
updated_at: '2025-09-08T18:44:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15070592052375-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-dos-resultados-ponto-eletr%C3%B4nico-em-rescis%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34788814393239) Tempo aproximado para leitura: **00:01:30min** **Dúvida**Como importar resultados ponto eletrônico em rescisão?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**

Há 3 opções de importação quando a verba a ser importada já existe na rescisão, são elas:  
•**Substituir**: substitui a verba da Rescisão pela verba importada do Ponto;  
• **Desprezar**: mantém a verba da Rescisão e despreza a verba do resultado do Ponto;  
• **Somar**: soma a quantidade de horas/valor da verba do Ponto à quantidade de horas/valor da verba da Rescisão.

**Importante**

• Só é permitida a importação dos Resultados do período de apontamento em aberto no Ponto Eletrônico, não é permitida a importação de Resultados dos Acumulados de Resultados do Ponto Eletrônico;

• As datas **Data Inicial** e **Data Final** na tela de parametrização para busca dos Resultados devem obedecer aos dias **inicial** e **final** do período de apontamento atual (por exemplo, considerando o parâmetro MV\_PAPONTA como **21/20** e MV\_PONMES como ‘20070121/20070220’, pode-se efetuar importação dos períodos 21/01/07 a 20/02/07,  
21/02/07 a 20/03/07, e assim por diante, sempre efetuando importação de um período de apontamento completo a partir do período de apontamento em aberto);

• Nos casos de soma (opção **Somar**) ou substituição (opção **Substituir**) de lançamentos, caso o tipo de verba do lançamento da Rescisão seja diferente do tipo de verba do Resultado (de **Horas** para **Dias** ou de **Dias** para **Horas**, respectivamente), será efetuada a conversão da quantidade de horas/dias da verba do Resultado para obedecer ao tipo da verba existente na Rescisão;

• A opção substituir não deleta verbas já existentes na RGB, somente substitui valores já integrados.

Procedimentos:

1.No ambiente Gestão de Pessoal, opção **Miscelânea/Cálculos/Rescisão** (GPEM040), preencha os campos **Data de Demissão** (necessariamente uma data do mês seguinte ao mês da competência em aberto na Folha), **Dias de Av. Prévio** e **Tipo de Rescisão**, conforme desejado.

2. Confirme o cálculo.

3. Na tela seguinte é apresentado o novo botão ( ) para importação dos Resultados do Ponto Eletrônico.

4.Ao clicar no botão “Imp. Ponto”, é apresentada a tela para parametrização da importação dos Resultados.

5. Ao clicar no botão “OK” é solicitada a confirmação da importação.

6. Após a confirmação, os Resultados são importados para a Rescisão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15070383912983)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15070393805079)

Observação: Ao utilizar a nova funcionalidade, caso haja verbas a serem importadas dos Resultados do Ponto Eletrônico para a rescisão, será automaticamente efetuada a totalização das verbas rescisórias que estão lançadas mais de uma vez na rescisão, tendo como parâmetro para totalização os lançamentos rescisórios que possuem mesmo Código (**Código Verba**), mesmo Centro de Custo (**C. de Custo**) e mesma Semana (**Nr. Semana**) - tratamento este já efetuado na confirmação do cálculo da rescisão.

**Saiba mais**Para adquirir maior conhecimento acesse o *link* abaixo

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)

<https://tdn.totvs.com/pages/releaseview.action?pageId=235311554>

[RH - Linha Protheus - GPE - Ao tentar excluir uma verba integrada do ponto eletrônico sistema não permite e apresenta mensagem de alerta As verbas vindas do SIGAPON estão bloqueada para exclusão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025899111-RH-Linha-Protheus-GPE-Ao-tentar-excluir-uma-verba-integrada-do-ponto-eletr%C3%B4nico-sistema-n%C3%A3o-permite-e-apresenta-mensagem-de-alerta-As-verbas-vindas-do-SIGAPON-est%C3%A3o-bloqueada-para-exclus%C3%A3o?source=search)
