---
article_id: 360016173392
category: Cadastros
content_hash: bde5f4799cc6567e8378411bfa94c01554810d0ca85b6692ec0750e9b50d4260
fetched_at: '2026-06-28T22:46:28.517303+00:00'
product: rm
section_id: 1500000861582
source: central-rm
title: RH - RM - PTO - Cadastrar e associar a compensação de dia ponte
type: support-article
updated_at: '2025-01-21T15:56:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016173392-RH-RM-PTO-Cadastrar-e-associar-a-compensa%C3%A7%C3%A3o-de-dia-ponte
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19408702513431) Tempo aproximado para leitura: 00:01:30 min**

**Dúvida**  
Como cadastrar e associar a compensação de dia ponte?  
 **Ambiente**RH - RH (Linha RM) - TOTVS Automação de Ponto – A partir da versão 11.80  
  
**Solução**Para cadastrar e associar a compensação de dia ponte, siga os passos abaixo.

1. Acesse o módulo de **Automação de Ponto**, selecione a guia **Cadastros** e acesse o menu **Compensação de dia ponte**.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/25829892974231)
2. Selecione a opção **Incluir**, preencha o cadastro com código e descrição desejados e clique no botão **Salvar**.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/25829892984855)
3. Após salvar o registro, acesse o menu **Anexos** e selecione a opção **Período Compensação de Dia Ponte**.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/25829889587607)
4. Neste anexo, clique em **Incluir** e faça o cadastro das informações de seu dia ponte. Após as alterações desejadas, salve o registro.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/25829892991767)  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/25829893008151)
5. Para associar esta compensação aos funcionários, acesse o **Parametrizador do Funcionário** e preencha o código cadastrado no campo **Compensação dia ponte** na etapa **Tabela**.![](https://centraldeatendimento.totvs.com/hc/article_attachments/25829889605015)

**Importante**

O cadastro do dia ponte só será considerado se for registrado apenas para jornadas com índice de trabalho.

O período de compensação será considerado apenas para jornadas que tenham índice de trabalho (incrementar ou decrementar) ou para jornadas com índice de compensação (incrementar).

Não sendo acatado para dias descanso ou feriado.

O conceito do cadastro do dia ponte é não gerar Falta para o funcionário no dia ao qual este for definido como ponte. Ou seja, o funcionário não irá trabalhar em um determinado dia e este dia será "compensado" dentro de um intervalo estipulado estendendo ou diminuindo a jornada.   
Caso no dia da ponte definido o funcionário trabalhe, será gerado ocorrência de EA (Extra Normal Autorizado) independente se o dia é um Descanso, Feriado ou Compensado. O dia ponte sobrepõe a jornada.

**Saiba Mais**  
Para maiores informações sobre a parametrização do dia ponte, acesse a documentação:  
[Compensação de Dia Ponte](https://tdn.totvs.com/pages/releaseview.action?pageId=452719120)

[RH - RM - PTO - Associação global de Dia Ponte aos funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043972154)
