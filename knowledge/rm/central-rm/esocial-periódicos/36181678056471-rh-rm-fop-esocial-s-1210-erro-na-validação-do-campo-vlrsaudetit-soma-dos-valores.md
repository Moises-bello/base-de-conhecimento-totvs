---
article_id: 36181678056471
category: esocial - Periódicos
content_hash: 0a82daa1433bace630bc43dbeeb5a3512f600f6c07d898ae4875560ce2eb21c4
fetched_at: '2026-06-28T22:47:09.498549+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: 'RH - RM - FOP - eSocial - S-1210 - Erro na validação do campo ''vlrSaudeTit'':
  Soma dos valores do Histórico Assistência Saúde não pode ser maior que o valor do
  evento no envelope.'
type: support-article
updated_at: '2026-05-26T19:26:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36181678056471-RH-RM-FOP-eSocial-S-1210-Erro-na-valida%C3%A7%C3%A3o-do-campo-vlrSaudeTit-Soma-dos-valores-do-Hist%C3%B3rico-Assist%C3%AAncia-Sa%C3%BAde-n%C3%A3o-pode-ser-maior-que-o-valor-do-evento-no-envelope
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36181665578647) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
Erro na geração do evento S1210 / ID: IDXXXXXXXXXXXX:  
Erro na validação do campo 'vlrSaudeTit': Soma dos valores do Histórico Assistência Saúde não pode ser maior que o valor do evento no envelope.  
  
**Ambiente**  
TOTVS RH (Linha RM) - Folha de Pagamento - eSocial  
  
**Causa**  
O erro ocorre pois há uma divergência de valores entre o valor do desconto de Assistência Saúde que consta no Envelope de Pagamento e a soma dos valores informados no Histórico de Assistência Saúde do funcionário (que alimenta o grupo de deduções no S-1210). O valor total do desconto que o sistema está tentando levar para o eSocial é maior do que o valor que a folha calculou.  
  
**Solução**  
Para corrigir a divergência e permitir o envio correto do S-1210, siga os passos abaixo:

1. **Conferir o Envelope de Pagamento:**

   * Acesse **Administração de Pessoal → Funcionários** e selecione o colaborador com erro.
   * Vá em **Envelope** e abra a competência correspondente ao envio do S-1210.
   * Localize o **evento de desconto de Assistência/Plano de Saúde** e anote o valor.
2. **Conferir o Histórico de Assistência Saúde:**

   * No mesmo colaborador, acesse **Anexos → Históricos → Histórico de Assistência Saúde**.
   * Filtre pela **Data de Pagamento** referente ao pagamento.
   * Some os valores informados para o titular e para todos os dependentes.
3. **Comparar os valores:**

   * O **Valor total do desconto no Envelope** (passo 1) deve ser **igual** à **soma dos valores no Histórico** (passo 2).
   * Caso o valor do Histórico seja **maior** que o do Envelope, **ajuste o histórico** para que corresponda ao valor realmente descontado.
   * Caso o valor do Envelope esteja incorreto, **corrija o evento de desconto na folha** e **recalcule**.
4. **Gerar novamente o XML:**  
   Após os ajustes, gere e envie novamente o **evento S-1210** ao eSocial.

**Saiba mais:**

Para mais informações sobre a geração do evento S-1210 e o tratamento da Assistência Saúde, acesse:

[RH - RM - FOP - eSocial - Assistência Saúde na geração do S-1210](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20025718353175-RH-RM-FOP-eSocial-Assist%C3%AAncia-Sa%C3%BAde-na-gera%C3%A7%C3%A3o-do-S-1210?source=search)
