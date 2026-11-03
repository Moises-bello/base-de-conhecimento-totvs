---
content_hash: 94263054260f4a48c2b39a2b9df1bc645318aba0509d6e4cc52d858ff1b785bf
fetched_at: '2026-06-29T00:05:53.014591+00:00'
page_id: '1062889046'
product: rm
source: tdn-rm
title: Middleware - Como validar divergências no Relatório de Conferência (IRRF) -
  Informações Complementares
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1062889046
version: 15
---

# Objetivo:

---

       O objetivo deste documento é orientar como validar divergências entre os valores gerados pelo TOTVS Folha de Pagamento e retornados pelo Governo no Relatório de Conferência (IRRF) - Informações Complementares.

Informações

A partir dos Patches:

* 12.1.2502.293
* 12.1.2506.262
* 12.1.2510.182
* 12.1.2602.106
* e superiores

Disponibilizamos no documento abaixo o detalhamento de campos, além de orientações adicionais referentes à situações já mapeadas pela TOTVS:

* **[Relatório de Conferência IRRF S-5002 - MAPEAMENTO e ORIENTAÇÕES](https://tdn.totvs.com/pages/viewpage.action?pageId=1040994699)**

Relatório S-5002Totalizador MensalTotalizador MensalleftRendimento Tributável

O campo **Rendimento Tributável** apresentará as informações de valores relativos ao rendimento tributável mensal e de férias. Sua composição será conforme abaixo:

**Origem Folha**

Somatório das verbas que possuem ***codIncIRRF*** **11** (Mensal) ou **13** (Férias).

Para retornar na tag***codIncIRRF***o valor**11**, o evento (PEVENTO) deve atender uma das seguintes condições:

* `INCIRRF` (incidência de IRRF) = **VERDADEIRO**
* `INCIRRFSUSPENSA`(incidência suspensa) = **VERDADEIRO**
* **DEDUTIVELIRRF** (dedutível IRRF) **=****VERDADEIRO**
* `CODIGOCALCULO` = **204**

Para retornar na tag***codIncIRRF***o valor**13,**o evento (PEVENTO) deve atender uma das seguintes condições:

* `INCIRRFFERIAS` (incidência IRRF férias) = **VERDADEIRO**
* `INCIRRFSUSPENSA`(incidência suspensa)= **VERDADEIRO**
* `DEDUTIVELIRRFFERIAS`(dedutível IRRF Férias) = **VERDADEIRO**
* `CODIGOCALCULO` ∈ **{208, 381}**

**Origem Governo**

Valor da Tag ***vlrRendTrib*** do grupo ***consolidApurMen***, presente no totalizador S-5002 do período de apuração em questão.

---

  **POSSÍVEIS CAUSAS DE DIVERGÊNCIA**

* **Incidência Incorreta**

Para validação, acesse o envelope de pagamento do funcionário e verifique as verbas cujo pagamento está compreendido no período de apuração utilizado na geração do relatório. 

Exemplo validação "Rendimento Tributável" 

Relatório gerado para o período 12/2025

Valor apresentado para o campo "Rendimento tributável" = R$ 2763,37

Para validar se este valor está correto, é necessário verificar as **incidências de IRRF (codIncIRRF = 11 ou 13)** das verbas com **data de pagamento conforme período** informado, ou seja, verbas cuja data de pagamento 12/2025 (independente da competência que estão).

*Importante lembrar que tais verbas podem estar na competência Novembro com pagamento em Dezembro, na competência Dezembro com pagamento em Dezembro, etc. Ou seja, o que importa não é a Competência em que a verba está lançada, e sim, a sua **data de pagamento**.*

Deste funcionário especificamente, só existem verbas com pagamento para Dezembro/25 na competência Dezembro. Considerando as regras de geração do codIncIRRF 11 ou 13, todas as verbas abaixo serão consideradas no relatório:

Somando os valores, chegamos à **R$ 2763,37**.

As incidências também podem ser verificadas através do menu "**Administração de Pessoal | Eventos**", conforme as abas "**Inc. Proventos**" e/ou "**Inc. Descontos**".

Já no ambiente do governo, você poderá verificar a tag ***codIncIRRF*** acessando o menu "**Empregador | Tabelas | Tabela de Rubricas**". As incidências precisam ser iguais entre RM e Governo.  
Lembre-se de conferir o início de validade da parametrização da rubrica:

**Tag codIncIRRF diferente entre Governo e RM: o que fazer?**

Caso a incidência da verba esteja diferente entre RM e Governo, será necessário ajustá-las para que o relatório seja corretamente gerado. Neste caso, siga os passos abaixo:

1. Ajuste a incidência da verba através do menu "**Administração de Pessoas | Eventos**";
2. Acesse o menu "**eSocial | Fila de Eventos**" e faça a edição do Gatilho do evento S-1010;
3. Altere o campo "Competência" indicando a partir de qual mês e ano tal incidência deva ser considerada;
4. Salve o registro e faça a geração do XML;
5. Verifique se a *tag **iniValid*** foi corretamente gerada conforme mês e ano informados no passo 3;
6. Envie o evento S-1010 para o Governo e faça a atualização do Status. Tal evento deverá ficar com status "10 -Aceito RET";
7. Após aceite do S-1010, realize a reabertura da folha no Governo através do envio do S-1298 do período de apuração necessário;
8. Retifique o evento S-1210 e, após ser aceito pelo RET, gere novamente o relatório para conferência;
9. Após todas os ajustes, feche novamente a folha do período de apuração enviando o evento S-1299.

------------------------------------------------------------------

* **Verba não apresentada no XML**

Caso a verba esteja sendo considerada no RM e não esteja no Governo, verifique:

1. Se a base está parametrizada para uso de Tomador de Serviços, veja se foi realizada corretamente a distribuição de tomador através do menu "**Encargos | SEFIP | Distribuir Tomador**";
2. Caso a distribuição esteja correta, ou a base não utilize Tomador de Serviços verifique se a verba está informada como à desconsiderar através do menu "Configurações | Parametrizador | eSocial | Eventos a Desconsiderar". Avalie a necessidade de removê-la;
3. Gere novamente o XML do S-1200 da competência em que a verba está lançada e verifique se a mesma consta no XML;
4. Reabra a folha de pagamento através do evento S-1298;
5. Faça a exclusão do S-1210 vinculado ao S-1200, retifique o S-1200, envio novamente o S-1210;
6. Feche a folha através do evento S-1299.

------------------------------------------------------------------

* **Evento 1/3 Abono de Férias**

O evento **“1/3 de Abono Férias”** possui incidência de **IRRF** e, por isso, é classificado como **rendimento tributável de férias** (*codIncIRRF 13*).  
Dessa forma, o valor **não será exibido no campo “Abono Pecuniário”** do relatório — que apresenta apenas valores com *codIncIRRF 75* — sendo demonstrado no campo **“Rendimento Tributável”**.

Se necessário, verifique se a incidência está corretamente configurada no cadastro da verba.

------------------------------------------------------------------

* **Valor de 1/3 Abono duplicado**

A duplicidade ocorre, geralmente, quando o evento **CC381 – Base de IRRF Férias Envelope** não está sendo considerado corretamente no envio ao eSocial.

Esse evento tem a função de estornar os valores que incidem em IRRF sobre férias no envelope de pagamento, evitando que haja duplicidade na composição do rendimento tributável.

Uma possível causa, seria o evento **CC381** não está sendo levado no XML do evento **S-1200**, o que impede o estorno correto dos valores.

Verifique os seguintes pontos:

* Se o evento **CC381** foi incluído no parametrizador como **“Eventos a Desconsiderar”**  
  → Caso esteja, é necessário removê-lo dessa configuração;
* Caso a coligada utilize Tomador de Serviços:
  + Verificar se o evento está com o parâmetro **“Segue rateio de tomador”** marcado;
  + Confirmar se adistribuição de tomador foi realizada corretamente para essa verba.

------------------------------------------------------------------

* **Adiantamento Salarial indevidamente apresentado no campo "Rendimento Tributável"**

Esse comportamento ocorre quando o evento de adiantamento (código de cálculo **19 – Desconto**) está configurado como **“Dedutível IRRF”** na pasta *“Inc.Descontos”*.

Quando marcado dessa forma, o sistema passa a considerar o valor no cálculo do Rendimento Tributável, resultando em um valor maior do que o esperado.

Para corrigir o comportamento:

* Acessar a configuração do evento (**CC19 – Desconto**);
* Na pasta *“Inc.Descontos”*, alterar a parametrização de: **“Dedutível IRRF”** para **“Estorna IRRF”**.

Com essa configuração:

* O evento de **pagamento do adiantamento salarial** (realizado em caixa diferente da folha) continuará com incidência de IRRF;
* O evento de desconto (**CC19**) passará a **estornar corretamente o valor**, evitando que ele seja considerado indevidamente no campo **“Rendimento Tributável”**.

------------------------------------------------------------------

* **Campo "Rendimento Tributável" maior no governo devido à Pensão Alimentícia de Férias**

Esse comportamento ocorre quando o evento de **pensão alimentícia de férias** está configurado com a flag **“Estorna IRRF”** ou **“Estorna IRRF de Férias”**.

Nessa situação, o evento passa a compor o cálculo do **Código de Cálculo 381 – Base de IRRF Férias (Envelope)**, reduzindo indevidamente a base de IRRF das férias no envelope de pagamento. Como consequência, ocorre divergência e o valor enviado ao governo fica maior do que o esperado no campo *“Rendimento Tributável”*.

Para corrigir o problema:

* Acessar o cadastro do evento de pensão alimentícia de férias;
* Alterar a parametrização de: **“Estorna IRRF” / “Estorna IRRF de Férias”** para **“Dedutível IRRF de Férias”**;
* Ajustar manualmente o valor do **Código de Cálculo 381 – Base de IRRF Férias (Envelope)**;
* Realizar o reprocessamento dos eventos no eSocial:
  + Excluir o evento **S-1210** por meio do **S-3000**;
  + Retificar o evento **S-1200**;
  + Enviar novamente o evento **S-1210**.

Com essa configuração:

* A pensão alimentícia será tratada corretamente como **dedução**;
* A base de IRRF de férias será apurada de forma adequada;
* O valor apresentado no campo **“Rendimento Tributável”** ficará consistente com o esperado pelo eSocial.
* [Código de Cálculo 381 - Base de IRRF Férias Envelope](https://tdn.totvs.com/pages/releaseview.action?pageId=452719713)

------------------------------------------------------------------

Prev. Oficial

O campo **Prev. Oficial** apresentará as informações de valores relativos a Previdência Oficial sobre rendimentos do trabalho, mensal e férias.

**Origem Folha**

Somatório das verbas que possuem ***codIncIRRF*** **41** (Mensal) ou **43** (Férias).

Para retornar na tag**`codIncIRRF`**o valor**41**, o evento (PEVENTO) deve atender simultaneamente às seguintes condições:

* **`FORCARINCIRRF`** = **FALSO**
* **`ISENTOIRRF`** = **FALSO**
* **`TIPOPREVIDENCIACOMPLEMENTAR`** = **NULO**
* **`INCIRRFSUSPENSAO`** = **NULO**
* **`RENDNAOTRIBACORDOINTERNAC`** = **FALSO**
* **`CODIGOCALCULO`** ∈ **{003, 068, 085, 092}**

Para retornar na tag**`codIncIRRF`**o valor**43**:

* Se **`PEVENTO.CODIGO`** for igual a **`ESOCIALEVENTOINSSANTECIPFERIAS`** (quando preenchido), o evento será enquadrado com **`codIncIRRF = 43`**.
* Quando `ESOCIALEVENTOINSSANTECIPFERIAS` não estiver preenchido, o evento (PEVENTO) deve atender simultaneamente às seguintes condições:

  + **`FORCARINCIRRF`** = **FALSO**
  + **`ISENTOIRRF`** = **FALSO**
  + **`TIPOPREVIDENCIACOMPLEMENTAR`** = **NULO**
  + **`INCIRRFSUSPENSAO`** = **NULO**
  + **`RENDNAOTRIBACORDOINTERNAC`** = **FALSO**
  + **`CODIGOCALCULO`** ∈ **{082, 110, 130, 132, 141, 349}**

**Origem Governo**

Valor da Tag ***vlrPrevOficial*** do grupo ***consolidApurMen***, presente no totalizador S-5002 do período de apuração em questão.

---

  **POSSÍVEIS CAUSAS DE DIVERGÊNCIA**

* **Incidência Incorreta**

Para validação, acesse o envelope de pagamento do funcionário e verifique as verbas cujo pagamento está compreendido no período de apuração utilizado na geração do relatório. 

Exemplo validação "Previdência Oficial" 

Relatório gerado para o período 12/2025

Valor apresentado para o campo "Previdência Oficial" = R$ 225,93

Para validar se este valor está correto, é necessário verificar as **incidências de IRRF (codIncIRRF = 41 ou 43)** das verbas com **data de pagamento conforme período** informado, ou seja, verbas cuja data de pagamento 12/2025 (independente da competência que estão).

*Importante lembrar que tais verbas podem estar na competência Novembro com pagamento em Dezembro, na competência Dezembro com pagamento em Dezembro, etc. Ou seja, o que importa não é a Competência em que a verba está lançada, e sim, a sua **data de pagamento**.*

Deste funcionário especificamente, só existem verbas com pagamento para Dezembro/25 na competência Dezembro. Considerando as regras de geração do codIncIRRF 41 ou 43, somente a verba abaixo se enquadra na condição (código de cálculo 3):

Assim, chegamos ao valor de **R$ 225,93**.

As incidências também podem ser verificadas através do menu "**Administração de Pessoal | Eventos**", conforme as abas "**Inc. Proventos**" e/ou "**Inc. Descontos**".

Já no ambiente do governo, você poderá verificar a tag ***codIncIRRF*** acessando o menu "**Empregador | Tabelas | Tabela de Rubricas**". As incidências precisam ser iguais entre RM e Governo.  
Lembre-se de conferir o início de validade da parametrização da rubrica:

*Imagem meramente ilustrativa*

**Tag codIncIRRF diferente entre Governo e RM: o que fazer?**

Caso a incidência da verba esteja diferente entre RM e Governo, será necessário ajustá-las para que o relatório seja corretamente gerado. Neste caso, siga os passos abaixo:

1. Ajuste a incidência da verba através do menu "**Administração de Pessoas | Eventos**";
2. Acesse o menu "**eSocial | Fila de Eventos**" e faça a edição do Gatilho do evento S-1010;
3. Altere o campo "Competência" indicando a partir de qual mês e ano tal incidência deva ser considerada;
4. Salve o registro e faça a geração do XML;
5. Verifique se a *tag **iniValid*** foi corretamente gerada conforme mês e ano informados no passo 3;
6. Envie o evento S-1010 para o Governo e faça a atualização do Status. Tal evento deverá ficar com status "10 -Aceito RET";
7. Após aceite do S-1010, realize a reabertura da folha no Governo através do envio do S-1298 do período de apuração necessário;
8. Retifique o evento S-1210 e, após ser aceito pelo RET, gere novamente o relatório para conferência;
9. Após todas os ajustes, feche novamente a folha do período de apuração enviando o evento S-1299.

------------------------------------------------------------------

* **Campo "Previdência Oficial" com valor zerado na Folha**

Esse comportamento ocorre quando os eventos de INSS (Folha, Férias e 13º), inclusive os eventos de diferença, estão configurados com o parâmetro **"Dedutível IRRF"** marcado na aba **"Inc. Descontos"**.

Com essa configuração, o sistema gera a tag **codIncIRRF** de forma incorreta, fazendo com que os valores desses eventos não sejam considerados na composição dos campos **"Previdência Oficial"** e **"Previdência Oficial 13º"**.

Para corrigir, é necessário desmarcar o parâmetro**"Dedutível IRRF"** desses eventos, garantindo assim a correta apuração dos valores na Folha.

------------------------------------------------------------------

* **Campo "Previdência Oficial" com valor zerado no Governo**

Esse cenário geralmente ocorre devido à configuração incorreta das tags***codIncIRRF***, o que impacta a correta apuração dos valores enviados ao Governo.

Para orientar a correção, consulte o documento: [Divergência de Previdência Oficial do Relatório de Conferência IRRF S-5002](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37856390101783)

------------------------------------------------------------------

* **Verba não apresentada no XML**

Caso a verba esteja sendo considerada no RM e não esteja no Governo, verifique:

1. Se a base está parametrizada para uso de Tomador de Serviços, veja se foi realizada corretamente a distribuição de tomador através do menu "**Encargos | SEFIP | Distribuir Tomador**";
2. Caso a distribuição esteja correta, ou a base não utilize Tomador de Serviços verifique se a verba está informada como à desconsiderar através do menu "Configurações | Parametrizador | eSocial | Eventos a Desconsiderar". Avalie a necessidade de removê-la;
3. Gere novamente o XML do S-1200 da competência em que a verba está lançada e verifique se a mesma consta no XML;
4. Reabra a folha de pagamento através do evento S-1298;
5. Faça a exclusão do S-1210 vinculado ao S-1200, retifique o S-1200, envio novamente o S-1210;
6. Feche a folha através do evento S-1299.

------------------------------------------------------------------

Abono Pecuniário

O campo **Abono Pec.** apresentará as informações de valores relativos ao Abono Pecuniário.

**Origem Folha**

Somatório das verbas que possuem ***codIncIRRF 75***.

Para que o **`codIncIRRF`** retorne o valor **75**, o evento (PEVENTO) deve atender simultaneamente às seguintes condições:

* **`FORCARINCIRRF`** = **FALSO**
* **`ISENTOIRRF`** = **FALSO**
* **`TIPOPREVIDENCIACOMPLEMENTAR`** = **NULO**
* **`INCIRRFSUSPENSAO`** = **NULO**
* **`RENDNAOTRIBACORDOINTERNAC`** = **FALSO**
* **`CODIGOCALCULO`** ∈ **{039, 047, 056, 059, 176, 311, 312, 398}**
* **`INCIRRFFERIAS`** = **FALSO**
* **`INCIRRF`** = **FALSO**
* **`INCIRRF13`** = **FALSO**

**Origem Governo**

Valor da Tag ***vlrAbonoPec*** do grupo ***consolidApurMen***, presente no totalizador S-5002 do período de apuração em questão.

---

  **POSSÍVEIS CAUSAS DE DIVERGÊNCIA**

* **Incidência Incorreta**

Para validação, acesse o envelope de pagamento do funcionário e verifique as verbas cujo pagamento está compreendido no período de apuração utilizado na geração do relatório. 

Exemplo validação "Abono Pec." 

Relatório gerado para o período 12/2025

Valor apresentado para o campo "Abono pecuniário" = R$ 666,67

Para validar se este valor está correto, é necessário verificar as **incidências de IRRF (codIncIRRF = 75)** das verbas com **data de pagamento conforme período** informado, ou seja, verbas cuja data de pagamento 12/2025 (independente da competência que estão).

*Importante lembrar que tais verbas podem estar na competência Novembro com pagamento em Dezembro, na competência Dezembro com pagamento em Dezembro, etc. Ou seja, o que importa não é a Competência em que a verba está lançada, e sim, a sua **data de pagamento**.*

Deste funcionário especificamente, só existem verbas com pagamento para Dezembro/25 na competência Dezembro. Considerando as regras de geração do codIncIRRF 75, somente a verba abaixo se enquadra na condição (código de cálculo 56):

Assim, chegamos ao valor de **R$ 666,67**.

As incidências também podem ser verificadas através do menu "**Administração de Pessoal | Eventos**", conforme as abas "**Inc. Proventos**" e/ou "**Inc. Descontos**".

Já no ambiente do governo, você poderá verificar a tag ***codIncIRRF*** acessando o menu "**Empregador | Tabelas | Tabela de Rubricas**". As incidências precisam ser iguais entre RM e Governo.  
Lembre-se de conferir o início de validade da parametrização da rubrica:

*Imagem meramente ilustrativa*

**Tag codIncIRRF diferente entre Governo e RM: o que fazer?**

Caso a incidência da verba esteja diferente entre RM e Governo, será necessário ajustá-las para que o relatório seja corretamente gerado. Neste caso, siga os passos abaixo:

1. Ajuste a incidência da verba através do menu "**Administração de Pessoas | Eventos**";
2. Acesse o menu "**eSocial | Fila de Eventos**" e faça a edição do Gatilho do evento S-1010;
3. Altere o campo "Competência" indicando a partir de qual mês e ano tal incidência deva ser considerada;
4. Salve o registro e faça a geração do XML;
5. Verifique se a *tag **iniValid*** foi corretamente gerada conforme mês e ano informados no passo 3;
6. Envie o evento S-1010 para o Governo e faça a atualização do Status. Tal evento deverá ficar com status "10 -Aceito RET";
7. Após aceite do S-1010, realize a reabertura da folha no Governo através do envio do S-1298 do período de apuração necessário;
8. Retifique o evento S-1210 e, após ser aceito pelo RET, gere novamente o relatório para conferência;
9. Após todas os ajustes, feche novamente a folha do período de apuração enviando o evento S-1299.

------------------------------------------------------------------

* **Abono Pecuniário sendo considerando no campo "Isento - Outros"**

Para que o Abono Pecuniário de Férias seja considerado corretamente apenas no campo Abono de Férias, siga os passos abaixo:

1. Acesse o menu: Folha de Pagamento | Configurações | Parametrizador | eSocial | Configurações Gerais (6/7).
2. No campo **“Evento Abono de Férias Envelope”**, informe um evento com o **código de cálculo 39**.

   > Caso necessário, crie um evento do tipo **provento**, sem incidências, utilizando o código de cálculo **39**.
3. Após realizar o ajuste, envie o evento **S-1010** ao eSocial com **data de início de validade retroativa a 01/01/2025**.
4. Após o envio do **S-1010**, remova o código de cálculo **39** do evento informado no parametrizador.
5. Na sequência:
   * Exclua o evento **S-1210**;
   * Realize a **retificação do evento S-1200**;
   * Reenvie o **S-1210** para as competências em que ocorreram as inconsistências.

------------------------------------------------------------------

* **Valor de 1/3 de Abono deve aparecer no campo “Abono Pecuniário”?**

Não. O evento **“1/3 de Abono Férias”** possui incidência de **IRRF** e, por isso, é classificado como **rendimento tributável de férias** (*codIncIRRF 13*).

Dessa forma, o valor **não será exibido no campo “Abono Pecuniário”** do relatório — que apresenta apenas valores com *codIncIRRF 75* — sendo demonstrado no campo **“Rendimento Tributável”**.

------------------------------------------------------------------

* **Valor de 1/3 de Abono duplicado no campo "Rendimento Tributável"**

A duplicidade ocorre, geralmente, quando o evento **CC381 – Base de IRRF Férias Envelope** não está sendo considerado corretamente no envio ao eSocial.

Esse evento tem a função de estornar os valores que incidem em IRRF sobre férias no envelope de pagamento, evitando que haja duplicidade na composição do rendimento tributável.

Uma possível causa, seria o evento **CC381** não está sendo levado no XML do evento **S-1200**, o que impede o estorno correto dos valores.

Verifique os seguintes pontos:

* Se o evento **CC381** foi incluído no parametrizador como **“Eventos a Desconsiderar”**  
  → Caso esteja, é necessário removê-lo dessa configuração;
* Caso a coligada utilize Tomador de Serviços:
  + Verificar se o evento está com o parâmetro **“Segue rateio de tomador”** marcado;
  + Confirmar se adistribuição de tomador foi realizada corretamente para essa verba.

------------------------------------------------------------------
