---
article_id: 360014404172
category: RH - Leitura e Apontamento
content_hash: 44c8bd9ceac16244f0caf040a7cdeeff5fc848ffe70d72204a15465980eec913
fetched_at: '2026-06-28T22:44:45.927141+00:00'
product: protheus
section_id: 32419281460119
source: central-protheus
title: RH - Linha Protheus - PON - Como gerar marcações automáticas pela rotina de
  Leitura/Apontamento
type: support-article
updated_at: '2026-05-26T17:46:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014404172-RH-Linha-Protheus-PON-Como-gerar-marca%C3%A7%C3%B5es-autom%C3%A1ticas-pela-rotina-de-Leitura-Apontamento
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35502126134679) Tempo aproximado para leitura: 00:02:00 min**Dúvida**Como gerar as marcações automáticas pela rotina de Leitura/Apontamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Para gerar as marcações automáticas pela rotina de Leitura e Apontamento, realize os seguintes passos:  
  
1 - Acesse o módulo **16-SIGAPON**, em **Atualizações > Cadastro do Ponto > Regras Apontamento**, aba **Marcações Automáticas**. No campo **Marcs. Auto.**, preencha as posições das batidas que serão buscadas e geradas com base na tabela de horário padrão. Nos campos **Gerar para Dias sem marcações** e **Completa Marcações**, preencha com **Sim**. É possível também parametrizar se existe necessidade de gerar as marcações com **minutos aleatórios**. Para isso, deixe o campo **Marcação Aleatória** como **Sim** e, no campo **Minut. Aleat.**, preencha a **quantidade de minutos desejada**.  
  
Importante ressaltar que, quando o campo D. Sem Marca. estiver como **SIM**, deve ser parametrizado no **cadastro do Turno de Trabalho** se também deverá ser gerada marcação para os **dias não trabalhados** através do campo **Mc. Aut. D. Ntr.** Este campo só deve ser configurado caso queiram gerar marcações nos tipos de **dias não trabalhados**.  
  
Veja a tela da regra de apontamento na aba '**Marcações Automáticas**':![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000107461)  
  
Veja, grifado no turno, o campo sobre geração de marcações automáticas em dias não trabalhados:  
Se o campo estiver preenchido conforme abaixo, para os dias não trabalhados serão geradas as marcações automáticas:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101201953)  
  
2 - Na Tabela de Horário Padrão, todos os dias devem estar com horário preenchido, mesmo os não trabalhados. Caso o turno tenha um intervalo cadastrado, o campo 1ª Saída Intervalo deve estar como **Sim**:  
![Tabela.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360009845552)  
Para mais detalhes desta configuração acesse a documentação:  
[RH - Linha Protheus - PON - Tabela de Horário Padrão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047920293-RH-Linha-Protheus-PON-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o)  
  
3 - Para a montagem do calendário e alocação correta das batidas, deve existir o registro de Troca de Turno com o primeiro dia do Período de Apontamento.  
**Exemplo:** Período de apontamento: 01/08/2018 a 31/08/2018. A Troca de Turno deve conter o registro conforme abaixo:  
![48.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360009776531)  
  
 Execute a rotina de Leitura/Apontamento acessando em Miscelânea > Cálculos > Leitura/Apontamento. Para apenas o processamento para geração de marcações automáticas, basta optar pela pergunta **Processamento igual à Apontamento**. Todos os funcionários que estiverem alocados a esta Regra de Apontamento terão as marcações automáticas lançadas pelo sistema:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30800917824791)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30800912610967)

**Saiba mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Como gerar marcações automáticas através da rotina Geração de Marcações](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018535311-RH-Linha-Protheus-PON-Como-gerar-marca%C3%A7%C3%B5es-autom%C3%A1ticas-atrav%C3%A9s-da-rotina-Gera%C3%A7%C3%A3o-de-Marca%C3%A7%C3%B5es)
