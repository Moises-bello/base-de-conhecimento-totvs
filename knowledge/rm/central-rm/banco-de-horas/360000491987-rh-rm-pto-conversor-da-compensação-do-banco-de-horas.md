---
article_id: 360000491987
category: Banco de Horas
content_hash: 6d9aa6ca18a8a7532396da60bfb19ff6af60b9074f82953b471e39df43a58cef
fetched_at: '2026-06-28T22:46:27.752832+00:00'
product: rm
section_id: 1500000835081
source: central-rm
title: RH - RM - PTO - Conversor da compensação do banco de horas
type: support-article
updated_at: '2025-05-12T17:11:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000491987-RH-RM-PTO-Conversor-da-compensa%C3%A7%C3%A3o-do-banco-de-horas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16820573827223) Tempo aproximado para leitura: 00:01:30 min  
  
Dúvida**  
Como executar o conversor da compensação?

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 11.80

**Solução**

Gostaria de informar que, a partir da versão 11.50, foi implementado um novo modelo de banco de horas. Durante a conversão da base de dados para a versão 11.50 ou superior, o sistema realiza a conversão dos dados das tabelas antigas de banco (ABANCOHORFUN ou ACOMPFUN) para a nova tabela (ABANCOHORFUN). O conversor de compensação foi disponibilizado na aplicação devido a inconsistências nas bases de dados referente as tabelas de banco de horas.  
  
**Importante:** Este processo deve ser executado **apenas** quando solicitado pela equipe de Suporte.

Caso a equipe de Suporte tenha solicitado o processo de **Conversão da compensação**, siga as instruções abaixo para executá-lo:

1. Acesse o gerenciador de banco de dados.
2. Execute as sentenças SQL a seguir para remover os dados das novas tabelas de banco de horas:

```
   DELETE FROM ABANCOHORFUNDETALHE
   DELETE FROM ASALDOBANCOHORFUNDETALHE
```

Antes de prosseguir para o próximo passo, faça logout do seu banco de dados.

1. Acesse o sistema **RM** e clique sobre a aba "**Executar"**.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21244851750551)
2. No campo "Localizar", pesquise por **Conversor da compensação**.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21244866552855)
3. Na seção **Ponto**, clique sobre o Conversor da Compensação.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21244851851287)
4. Nas versões mais recentes, faça a seleção do grupo de funcionários desejados, ou clique diretamente no botão executar para que o processo seja realizado globalmente.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21244866615831)
5. Irá iniciar a execução do processo, e no fim irá aparecer a mensagem que foi o mesmo foi concluído.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21244866647703)
6. Em versões mais antigas, ao clica sobre Conversor da "Compensação" será aberta uma mensagem informando o início do processo será exibida.   
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360000827408)  
     
   **Observação**: É importante ressaltar que o processo de **conversor da compensação** não apresenta nenhum indicador de progresso durante a execução. Durante esse processo, nenhuma alteração deve ser feita no módulo de **Automação de Ponto**. Portanto, se houver mais de um usuário utilizando o módulo de **Automação de Ponto**, certifique-se de que nenhum deles esteja logado no sistema.
7. Ao final da execução do processo, uma mensagem será exibida conforme mostrado na tela abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360000827428)  
  
**Atenção**:

Se a rotina de conversão da compensação está sendo realizada após **importar o saldo de banco de horas** através de um arquivo txt, após a execução do processo, **não deve ser recalculado o ponto** do funcionário para que o processo não seja revertido.

Isso ocorre pelo seguinte motivo: quando se realiza um recálculo no ponto, o primeiro processo executado pelo sistema é a deleção dos dados de tabelas relacionadas ao cálculo, naquele período. Isso também envolve tabelas de banco de horas, que são alimentadas por meio de dados constantes no período em que se está realizando o cálculo.

Após isso, o sistema realiza o cálculo com base nas parametrizações e dados existentes, populando as tabelas de movimento, abono, extras, atrasos, faltas, e alimentando o banco de horas, etc.

Como a importação realizada inclui informações que não são exatamente provenientes de batidas, extras, atrasos e faltas existentes no período, elas não retornam após o recálculo.

Assim sendo, a orientação é incluir essas informações de banco, com data anterior ao período atual (estando nele), e depois, ao avançar o período (definindo como ativo), o sistema automaticamente já incorpora esses valores no saldo do banco de horas.

**Saiba mais:**

[Conversor de Compensação](https://tdn.totvs.com/pages/viewpage.action?pageId=146180251)
