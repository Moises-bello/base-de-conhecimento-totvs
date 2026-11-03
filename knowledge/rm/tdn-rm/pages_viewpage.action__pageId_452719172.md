---
content_hash: faf64fd7b4f19964adf09e8269967a427997a1a487e61936dc8315d91251f0c8
fetched_at: '2026-06-29T00:10:03.909598+00:00'
page_id: '452719172'
product: rm
source: tdn-rm
title: Liberação de Competência Folha
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719172
version: 19
---

Após o lançamento de todos os dados do mês atual, deve-se executar a rotina de **Liberação de Competência** para criar o novo mês competência.

Na parametrização do processo, o sistema exibirá uma tela para que o usuário defina:

* Data de pagamento da folha do novo mês competência
* Novo mês caixa
* Período de lançamentos

---

## Atenção

* Antes de iniciar a liberação, **faça backup da base de dados**.
* Certifique-se de que **todos os usuários estejam desconectados do sistema**.

---

## Operações realizadas

**1 - Abertura de transação no banco** e execução dos procedimentos abaixo:

* + Remoção dos códigos fixos cujo número de vezes está zerado (todos já lançados).
  + Transferência da ficha financeira para a tabela complementar, conforme parâmetro **“Guarda ficha financeira após 24 meses”**, se ativado na parametrização da Liberação de Competência.

    > **Observação:** A transferência da ficha financeira torna-se opcional. Se o parâmetro não estiver marcado, essa transferência poderá ser feita manualmente posteriormente pelo módulo **Transferência Manual dos Registros da Ficha Financeira**.
  + Atualização dos campos: mês competência, ano competência, mês caixa, ano caixa e dia de pagamento para o próximo mês.
  + Atualização das bases de AAS. **Atenção:**A partir da release **12.1.2606**, essa atualização não ocorre mais, com o objetivo de centralizar as funcionalidades relacionadas ao eSocial.
  + Atualização do número de dependentes para salário-família e sua incidência no cadastro de dependentes.
  + Atualização dos dependentes para IRRF, considerando:

    - Filhos válidos que completaram 22 anos, ou
    - Filhos universitários que completaram 25 anos.  
      Isso ocorrerá apenas se o parâmetro **“Considera a dedução de dependente somente até o mês de aniversário”** estiver ativo em Parametrizador | Folha Normal | Cálculo 2/2.
  + Atualização do final de vigência das tabelas de cálculo, valores fixos e tarifas de vale com vigência final no mês liberado, caso parametrizado para atualização na liberação.
  + Atualização da situação da contribuição sindical:

    - Para “J” (Já descontou) para funcionários que tiveram o código 12 (Desconto Contribuição Sindical) no mês da competência.
    - Para “N” (Não descontou) na liberação de competência dezembro → janeiro para funcionários que estavam com “J”.
  + Atualização dos flags para funcionários que completaram 65 anos no mês liberado.
  + Ajuste da situação e históricos de funcionários com afastamento e retorno dentro do mês.
  + Atualização do histórico de contribuição sindical, caso haja recolhimento no mês.
  + Ajuste da situação e histórico de admitidos e demitidos para o próximo mês.
  + Remoção de eventos zerados da ficha financeira, caso o parâmetro **“Remove Eventos Zerados na Liberação da Competência”** esteja marcado.
  + Atualização do salário, seção e função atual conforme alterações agendadas para o novo mês, refletidas nos históricos.
  + Atualização dos parâmetros locais de todos os usuários para o novo mês/ano.
  + Aprovação automática dos dados do RM Portal configurados para tal.
  + Envio de avisos automáticos pendentes e remoção dos avisos já enviados no mês.
  + Transferência da fila de eventos do eSocial para a fila complementar, conforme parâmetro **“Meses a manter na Fila de Eventos”**, se ativado na parametrização.

**2 - Processamento dos Grupos AAS da ficha financeira**  
O parâmetro **“Processar Grupos AAS da ficha financeira na liberação da Competência”** define o valor padrão do campo homônimo na tela de liberação. Se marcado no parametrizador, virá marcado na liberação, e vice-versa.

**Atenção:**A partir da release **12.1.2606**, este parâmetro foi retirado, com o objetivo de centralizar as funcionalidades relacionadas ao eSocial.

**3 - Seleção de coligadas**  
O usuário deverá selecionar as coligadas para a liberação da competência.

**4 - Uso de parâmetros específicos**  
É possível definir parâmetros específicos por coligada, que terão prioridade sobre os parâmetros gerais. Coligadas sem parametrização específica usarão os parâmetros gerais.

**5 - Validação das coligadas**

* + **Validações padrão:**

    - Férias cadastradas e não calculadas;
    - Férias calculadas e não lançadas;
    - Férias lançadas e não liberadas.
    > O sistema bloqueia a liberação se alguma dessas situações existir.

* + **Validações opcionais (por parametrização):**

    - Geração obrigatória de histórico de provisões:  
      Se nenhum funcionário tiver o histórico gerado, a liberação não será permitida.  
      Se apenas parte dos funcionários tiver o histórico, o sistema alerta e permite ou não continuar conforme decisão do usuário.
    - Geração obrigatória do saldo do FGTS.

* + **Validação da licença de funcionários**
    - O sistema compara a **quantidade de funcionários ativos no produto** com o **limite da licença**, considerando:

      * Funcionários com evento na ficha financeira no mês da liberação (exceto demitidos).
    - Caso o limite seja excedido, o sistema alertará por 2 (duas) liberações consecutivas e na terceira bloqueará a liberação, exigindo contato com o departamento Comercial da TOTVS para regularização.

**Consulta SQL - Quantidade de Funcionários Ativos**

SELECT COUNT(\*) FROM PFUNC (NOLOCK)  
WHERE ((CODSITUACAO <> 'D' AND CODTIPO <> 'A') OR  
      (CODTIPO = 'A' AND CODSITUACAO <> 'D' AND  
      EXISTS (SELECT 1 FROM PFFINANC (NOLOCK)  
              WHERE PFFINANC.CODCOLIGADA = PFUNC.CODCOLIGADA  
                AND PFFINANC.CHAPA = PFUNC.CHAPA  
                AND PFFINANC.ANOCOMP = :ANOCOMP  
                AND PFFINANC.MESCOMP = :MESCOMP)))

* + - A contagem de funcionários na licença é feita via **License Server** do cliente.

**7 - Agendamento**

* + A liberação de competência pode ser agendada para execução automática via JobServer, configurado em modo 3 Camadas, para maior produtividade.
  + Para mais informações sobre configuração, consulte o manual [Link](https://tdn.totvs.com/pages/viewpage.action?pageId=270085915).

**8 - Logs**

* Após a execução, o sistema exibirá logs detalhados da validação, incluindo erros e avisos.
* Caso haja avisos, para continuar a liberação, o usuário deverá marcar:

  + **“Li e estou ciente dos avisos que foram dados para as coligadas abaixo”** e
  + **“Desejo liberar a competência das coligadas que tiveram avisos”**.
* Caso não deseje liberar as coligadas com avisos, basta marcar apenas o primeiro parâmetro para liberar somente as coligadas sem avisos.

|  |  |
| --- | --- |
|  | Veja Também  [Dt - Liberação de Competência Multi-Coligadas](http://tdn.totvs.com/pages/viewpage.action?pageId=342310654) |

---
