---
article_id: 360006767052
category: Ativo Fixo - Aquisição por Transferência
content_hash: 2ba4213de248d4196f3072a0b3487a7e8442424bd93c0bdb804c6e4abee52896
fetched_at: '2026-06-28T22:41:56.922599+00:00'
product: protheus
section_id: 1500001535341
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA251 - Agrupar, Aglutinar
  ou Desmembrar bens do ativo
type: support-article
updated_at: '2024-07-17T17:00:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006767052-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA251-Agrupar-Aglutinar-ou-Desmembrar-bens-do-ativo
---

**Dúvida**

Como aglutinar vários bens em um único ativo, ou como desmembrar um bem para vários?

**Ambiente**Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial – A partir da versão 12  
  
**Solução**  
Para aglutinar vários ativos e compor um único ativo, utilize a rotina de Aquisição por Transferência (**ATFA251**), assim, permitindo selecionar os ativos desejados e gerando o novo ativo.  
  
Os ativos que foram selecionados, sofrem baixa automática pelo sistema.

Modulo **Ativo Fixo** - **Atualização**/ **Movimentos** / **Aquisição por transferência (ATFA251)**

1-Posicione sobre o ativo que deseja transferir e selecione a opção Transfere ou Agrupar.

É apresentada a tela de parâmetros.

Observe as opções disponibilizadas para a pergunta: Descrição estendida?

\* Desconsiderar

\* Atribuir

2- Configure-os conforme orientação do help de campo e confirme

Em seguida, é exibida uma nova janela para a definição dos ativos a serem transferidos.

3- Selecione o intervalo numérico referente ao código dos ativos que serão transferidos e confirme

Será apresentada uma tela com todos os ativos pertencentes aos códigos selecionados.

4- Confirme

É apresentada uma tela para a configuração dos dados do novo ativo.

Observe no rodapé da tela, os campos das pastas Totais do rateio, Detalhes dos impostos e Descrição estendida.

Cada linha inserida é um novo bem definitivo. A soma dos valores dos bens definitivos deve ser exatamente igual à soma dos valores dos adiantamentos selecionados.

5- Confirme os dados

6 - Para **desmembrar** o ativo - selecionar o ativo que deseja desmembrar

Na nova janela determinar o  percentual correspondente ao numero de ativos novos a serem gerados

Ex.:

Percentual % - dividir 100% pela quantidade de Bem que serão gerados

Exemplo :

Ativo quantidade 5 valor 5000,00

Percentual 100% = Qta 5 / 100 = 20%

Desmembramento :

quantidade 1 valor 1000,00 Percentual 20%

quantidade 1 valor 1000,00 Percentual 20%

quantidade 1 valor 1000,00 Percentual 20%

quantidade 1 valor 1000,00 Percentual 20%

quantidade 1 valor 1000,00 Percentual 20%

Sistema irá baixar o bem Original criando assim 5 novos bens

Totalizando valor 5000,00 percentual 100% - do bem original

**Observação importante:**

Ao gerar um novo ativo a partir da rotina de aquisição por transferência, a data de aquisição do bem será gerada com a data base em que foi executado a transferência, não permite gerar com data anterior a data do ultimo calculo de depreciação.

Informações no TDN:

[AQUISIÇÃO POR TRANSFERENCIA](http://tdn.totvs.com/pages/releaseview.action?pageId=6067616)

Diferença entre "Transfere", "Agrupar" e "Detalhar":

[ATFA251 - Transfere, Agrupar e Detalhar](https://tdn.totvs.com/pages/releaseview.action?pageId=312159989)
