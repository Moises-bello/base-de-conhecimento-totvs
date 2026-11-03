---
article_id: 360015528671
category: ' RH - Funcionários'
content_hash: 5e144fafe45c1b01dc031c97f83700e975758752108b9f541ca1b085f0f83d9d
fetched_at: '2026-06-28T22:44:48.224708+00:00'
product: protheus
section_id: 32419218165783
source: central-protheus
title: RH - Linha Protheus - PON - Como funciona a Troca de Turno dos funcionários
type: support-article
updated_at: '2025-12-26T17:06:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015528671-RH-Linha-Protheus-PON-Como-funciona-a-Troca-de-Turno-dos-funcion%C3%A1rios
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34784536225559) Tempo aproximado para leitura: 00:01:30 min**  
  
**Dúvida**  
Como funciona a Troca de Turno dos funcionários?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
A **Troca de Turno** é uma rotina de muita importância para que a [**montagem dos calendários**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016361412)dos funcionários fiquem correto.   
Nessa rotina, informamos sob qual Regra de Apontamento, Turno de Trabalho e Sequência da Tabela de Horário Padrão o funcionário estará atrelado.  
Além disso, é de extrema importância que as informações estejam corretas para que o **processo de Leitura/Apontamento** funcione corretamente, bem como a impressão de relatórios como Espelho de Ponto e os arquivos fiscais **AFDT e ACJEF**.  
  
Para **cada Período de Apontamento**, deve existir um registro com o **primeiro dia do período**, ou seja, se o **período vigente for de 01/10 à 31/10**, obrigatoriamente deve existir um registro com a data de **01/10.** Mesmo que o funcionário não tenha tido uma troca de Regra/Turno/Sequência, o registro deve existir.  
  
Essa rotina é alimentada automaticamente quando o usuário processa o [**Fechamento Mensal**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004103232-RH-Linha-Protheus-PON-Como-efetuar-o-Fechamento-Mensal-do-Ponto)do período e o novo é aberto de forma subsequente, é criado um registro de Troca de Turno com o **primeiro dia do novo período** .   
\*\*Esses dados (Regra/Turno/Sequência) não podem ser alterados diretamente diretamente pelo Cadastro de Funcionários, essa ação é permitida unicamente no momento da admissão.

Para **executar a troca de turno** acesse **Atualizações> Cadastro do Funcionários> Troca de Turno**   
- Incluir (para colaboradores recém admitidos);  
Ou  
- Outras Ações > Alterar (para alterar o turno de trabalho, sequencia ou regra de apontamento) de funcionários já existentes.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404848795543)  
  
  
**Importante:** A troca de turno deve conter uma sequencia logica, o conteúdo dos campos **Turno De, Seq. De, Regra De** precisam respeitar os dados dos campos da linha superior **Turno Para, Seq. Para e Regra Para.**  
  
  
  
**Saiba mais**  
[**Manual do Ponto Eletrônico**](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[**Pacote de Expedição Contínua Acumulado de RH**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
