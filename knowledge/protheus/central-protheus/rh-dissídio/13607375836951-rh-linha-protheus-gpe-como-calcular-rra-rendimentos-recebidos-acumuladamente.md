---
article_id: 13607375836951
category: RH - Dissídio
content_hash: 9d60e36865b82537aed052e4c69b6da382fbaaa551a655c2d872f134e1953b39
fetched_at: '2026-06-28T22:43:43.266772+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular RRA - Rendimentos Recebidos acumuladamente
type: support-article
updated_at: '2025-08-15T18:24:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13607375836951-RH-Linha-Protheus-GPE-Como-calcular-RRA-Rendimentos-Recebidos-acumuladamente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34214386999063) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como calcular RRA - Rendimentos Recebidos Acumuladamente?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Existem dois processos necessários para que o cálculo do RRA seja feito corretamente, são eles:  
- Na rotina "Complemento Trabalhista" (GPEA850), deve ser cadastrado os identificadores do complemento de RRA e a quantidade de parcelas utilizadas para pagamento das verbas.  
- No "Cadastro de Verbas" (GPEA040), devem ser cadastradas as verbas específicas do cálculo de RRA, que são detalhadas a seguir:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13607175280407)

Abaixo segue procedimentos para o correto cálculo do RRA:  
  
**DISSÍDIO RETROATIVO**

* Em **Gestão de Pessoal** (SIGAGPE), acesse **Atualizações / Definições de Cálculo / Manutenção de Tabelas** (GPEA320).
* Posicione na tabela **S034 - Tabela de IR para RRA** e clique em **Incluir**.
* Informe o **Ano/Mês Inicial** e **Final** de validade das alíquotas (Exemplo: 202301 até 202312).
* Com base na tabela progressiva de IR RRA do Ano-Calendário informado, preencha os demais campos com **Valor de Isenção**, **Rendimentos** (informe o menor valor de cada faixa), **Alíquota** e **Dedução**.
  + O campo **Filial** pode ficar em branco, uma vez que as alíquotas serão as mesmas para todas as filiais.
* Acesse **Atualizações / Definições de Cálculo / Verbas**(GPEA040).
* Cadastre as verbas para cada novo identificador de RRA citado no tópico anterior.
* Configure o campo **RRA (RV\_RRA)** com a opção "**Sim**" para todas as verbas de Diferença de Dissídio (Identificadores de cálculo 0337, 0338, 0340, 0342, 0398, 0399, 0400, 0401, 0402, 0403).
* Acesse **Atualizações / Cadastros / Complementos Trabalhistas** (GPEA850).
* Cadastre os complementos trabalhistas, conforme orientação do help de campo.

**Importante:** A rotina de dissídio não calcula RRA se não for informado um complemento trabalhista.   
O número de parcelas informado no complemento, deve ser o número de parcelas que será utilizado na geração das parcelas do dissídio.

* Acesse **Miscelânea / Reajuste / Dissídio Retroativo** (GPEM690).
* Efetue o cálculo de dissídio e informe no parâmetro **Complemento**, o número do complemento que foi cadastrado na rotina de "Complementos Trabalhistas" (GPEA850) e deverá ser utilizado.
* Após o cálculo, em **Outras Ações**, clique em **Gerar IR RRA**, para efetuar a apuração do IR do RRA.
* Preencha os parâmetros de acordo com orientação do help de campo.
* Após o cálculo, acesse **Atualizações / Lançamentos / RRA** (GPEA840) para conferir os lançamentos gerados.
* Em **Miscelânea / Reajuste / Dissídio Retroativo** (GPEM690) clique em **Outras Ações** e **Geração**
* Informe o complemento trabalhista na pergunta **Complemento** e proceda com a geração das verbas. Caso o complemento não seja informado, as verbas de RRA não serão geradas.

Após a geração das verbas, os dados poderão ser visualizados através da rotina de **Lançamentos por Funcionário** (GPEA580) ou **Valores Futuros** (GPEA110), de acordo com a parametrização da rotina.

**Importante:** Além de todos os itens citados, as verbas de RRA serão geradas apenas se o dissídio estiver sendo calculado com base em verbas pagas em anos anteriores ao do cálculo, Exemplo: Dissídio calculado em 01/03/2023 referente ao período 12/2022.  
  
**RESCISÃO COMPLEMENTAR**

* Em **Gestão de Pessoal** (SIGAGPE), acesse **Atualizações / Definições de Cálculo / Manutenção de Tabelas** (GPEA320).
* Posicione na tabela **S034 - Tabela de IR para RRA** e clique em **Incluir**.
* Informe o **Ano/Mês Inicial** e **Final** de validade das alíquotas (Exemplo: 202301 até 202312).
* Com base na tabela progressiva de IR RRA do Ano-Calendário informado, preencha os demais campos com **Valor de Isenção**, **Rendimentos** (informe o menor valor de cada faixa), **Alíquota** e **Dedução**.
  + O campo **Filial** pode ficar em branco, uma vez que as alíquotas serão as mesmas para todas as filiais.
* Acesse **Atualizações / Definições de Cálculo / Verbas**(GPEA040).
* Cadastre as verbas para cada novo identificador de RRA citado no tópico anterior.
* Acesse **Atualizações / Cadastros / Complementos Trabalhistas** (GPEA850).
* Cadastre os complementos trabalhistas, conforme orientação do help de campo.

Importante: A rotina de rescisão não irá calcular verbas de RRA se não for informado um complemento trabalhista.

* Em **Gestão de Pessoal** (SIGAGPE) acesse **Miscelânea / Cálculos / Rescisão** (GPEM040).
* Posicione em um funcionário e clique em "**Calcular**".
* Informe no campo **Complemento** o código do complemento trabalhista para cálculo do RRA.

Ao confirma o cálculo, as verbas de IR Férias e IR são incorporadas nas verbas IR RRA, bem como a verba de IR 13º é incorporada na verba IR RRA 13º. Isto acontece somente se a rescisão complementar ocorrer em um ano-base diferente da rescisão anterior. No caso de complementar no mesmo ano o cálculo é feito de forma padrão, sem geração de RRA. Da mesma forma, se um complemento não for informado, nenhuma verba de RRA será gerada.

Com estes códigos cadastrados e procedimentos realizados, após a geração do arquivo da DIRF, é possível efetuar a consulta na rotina "Manutenção de Arquivo" (GPEM560), na opção RRA. A partir das verbas que possuem estes códigos, será gerado o registro RRA nas rotinas: Magnético da DIRF (GPEM590) e Informe de Rendimentos (GPEM580) Na tela "Manutenção de RRA" (GPEA840), poderão ser consultados os lançamentos de RRA provenientes do cálculo de dissídio retroativo.

**Saiba mais**  
[RRA - Rendimentos Recebidos Acumuladamente](https://tdn.totvs.com/display/public/PROT/RRA+-+Rendimentos+Recebidos+Acumuladamente#main-dissidio)
