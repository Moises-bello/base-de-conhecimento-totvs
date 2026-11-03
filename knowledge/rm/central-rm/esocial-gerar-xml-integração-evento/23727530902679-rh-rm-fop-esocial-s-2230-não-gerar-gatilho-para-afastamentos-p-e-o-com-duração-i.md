---
article_id: 23727530902679
category: eSocial - Gerar XML/ Integração Evento
content_hash: e951990070c014909a26b7080b9ad1f8908b3cf9df8146d6e35263c4561853db
fetched_at: '2026-06-28T22:47:13.146600+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - S-2230 - Não gerar gatilho para afastamentos (P e
  O) com duração inferior ao definido no MOS
type: support-article
updated_at: '2024-11-25T13:12:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23727530902679-RH-RM-FOP-eSocial-S-2230-N%C3%A3o-gerar-gatilho-para-afastamentos-P-e-O-com-dura%C3%A7%C3%A3o-inferior-ao-definido-no-MOS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23727530877847) Tempo aproximado para leitura: **00:03:10 min****Dúvida**Qual a função do parâmetro **Não gerar gatilho S-2230 para afastamentos (P e O) com duração inferior ao definido no MOS**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**Em**Configurações Gerais 3/7** há o parâmetro **Não gerar gatilho S-2230 para afastamentos (P e O) com duração inferior ao definido no MOS**. Quando este parâmetro estiver assinalado, o sistema não irá gerar o XML S-2230 para afastamentos em que a duração não seja superior a 15 dias, ou em que dentro de 60 dias a soma dos afastamentos pela mesma doença não seja superior a 15 dias, conforme consta no MOS.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23727530878359)

Para configuração no sistema conforme o MOS, será necessário:

1. Acesse o menu **RH | Folha de Pagamento | Configurações | Parametrizador | eSocial | Configurações Gerais | Configurações Gerais 3/7**. Marque o parâmetro **Não gerar gatilho S-2230 para afastamentos (P e O) com duração inferior ao definido no MOS**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23727510235927)

2. Após, acesse **RH | Folha de Pagamento | Configurações | Parametrizador | Folha de Pagamento | Folha Normal | Afastamento 1/2**. Verifique a parametrização consta conforme estabelecido no MOS;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23727530881431)

3. No histórico de afastamento a coluna Gatilho Pendente Afastamento Inferior ao MOS (Tipo P e O) que fará o controle dos gatilhos gerados na fila de eventos, com os status 1- ( Gatilho pendente de geração); 0 - ( Gatilho gerado ); Branco - ( registros já existentes no histórico anterior a implementação deste controle).

**Exemplo 1 - Afastamento superior a 15 dias**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23727530882327)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23727510241047)

**Exemplo 2 - Dentro de 60 dias a soma dos afastamentos pela mesma doença é superior a 15 dias**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23727530883991)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23727510244759)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23727530886935)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23727530887575)**

**Importante**Caso a parametrização no sistema conste conforme supracitado e, o usuário queira enviar o evento S-2230 com afastamentos com duração inferior ao estabelecido no MOS, faz-se necessário desmarcar a opção **Não gerar gatilho S-2230 para afastamentos (P e O) com duração inferior ao definido no MOS**, excluir o atestado e lançar novamente. Assim o S-2230 será gerado na fila de eventos não periódicos.

**Saiba mais**  
Para mais informações acesse:  
[RH - RM - FOP - Cadastro de atestado que gera afastamento na folha](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053610854-RH-RM-FOP-Cadastro-de-atestado-que-gera-afastamento-na-folha#:~:text=Para%20cadastrar%20o%20atestado%2C%20acesse,e%20os%20demais%20campos%20desejados).
