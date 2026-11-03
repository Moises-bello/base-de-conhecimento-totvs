---
article_id: 5743820814487
category: RH - Lançamentos
content_hash: 74ef10c9600ae73917633fecdb7941ea58b685fc7fb9ef553824f02287c40bc5
fetched_at: '2026-06-28T22:43:31.295326+00:00'
product: protheus
section_id: 360010781734
source: central-protheus
title: RH - Linha Protheus - GPE - Importar valores de coparticipação - Importação
  de variáveis tabela RHO
type: support-article
updated_at: '2026-06-03T19:04:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5743820814487-RH-Linha-Protheus-GPE-Importar-valores-de-coparticipa%C3%A7%C3%A3o-Importa%C3%A7%C3%A3o-de-vari%C3%A1veis-tabela-RHO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18181274663575) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como importar valores de coparticipação, via rotina de Importação de Variáveis para a tabela RHO?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões.

**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
  
**1.** Criar um Layout **TXT**;

Abra um Bloco de Notas ou Notepad++, Clicar em **Exibir** e clicar em **Barra de Status**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18179813002519)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18180528837143)

**Observação:** Sempre que finalizar uma linha, clique na tecla **Enter**, para que a ultima linha do arquivo fique em branco.

**2.** Crie um **Layout de Importação** em **Atualizações > Definições de Cálculos >** **Layout de Importação**;  
  
Exemplo: Coparticipação   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18180594320919)  
  
**RHO\_FILIAL** - Dados da Filial. No exemplo está configurado para ler a matricula e vincular a filial, porém é possível retirar a fórmula para importar mais de uma filial por vez.   
**RHO\_MAT** - Dados da matricula do funcionário (no exemplo informando no TXT da coluna 01 a 06)  
**RHO\_DTOCOR** - Dados da data de ocorrência (no exemplo está configurado para usar a data de log do sistema)  
**RHO\_TPFONR** - Dados do Tipo do Fornecedor contendo duas opções **1 - Assistência Medica** ou **2- Assistência Odontológica** (no exemplo estou informando no TXT da coluna 07 a 07)   
**RHO\_CODFOR** - Código do Fornecedor de acordo com o cadastrado nos Planos Ativos (no exemplo informando no TXT da coluna 08 a 10)  
**RHO\_CODIGO** - Código da Sequencia referente ao cadastro do Dependente (no exemplo no TXT da coluna 11 a 12)  
**RHO\_ORIGEM** - Dados de origem do lançamento podendo ser 3 opções **1 - Titular**, **2-** **Dependente** e **3- Agregado** (no exemplo no TXT da coluna 13 a 13)  
**RHO\_PD** - Código da Verba - usar a verba de desconto da coparticipação (no exemplo no TXT da coluna 14 a 16)  
**RHO\_COMPPG** - Dados da Competência de Pagamento a qual será descontado (importante que esteja de acordo com a folha vigente "Aberta" no exemplo no TXT da coluna 17 a 22)  
**RHO\_CPF** - Obrigatório quando possuir dependentes e para arquivos que precise somar os descontos  (no exemplo no TXT da coluna 23 a 33)  
**RHO\_VALOR** - Dados de Valor a ser descontado do Funcionário (no exemplo no TXT da coluna 34 a 39)  
  
**3. Importe** o arquivo para o Sistema acessando a rotina **Importação de Variáveis** em **Miscelânea > Importação > Importação de Variáveis**;  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18180824614423)

Em parâmetros no **Arquivo** selecione o **TXT** de importação criado:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18180906550679)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18180813777431)

No **Código** selecione o **Layout de importação** Criado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18180904181911)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18180859186071)  
  
  
**Sobrepõe** = **SIM** / **NAO** (SIM valida apenas o ultimo importado / NAO soma os valores)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18180928010263)

**Situações** = ADFT ou A\*FT

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18180988958743)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18180973628567)

**Data Referência** = Sempre a data da competência que será pago ou descontado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18181019972887)

Clique em **OK.** E preencha os demais parâmetros:  
  
**Tipo Lançamento = 1 - Coparticipação** ou **2 - Reembolso**  
**Competência pagamento =** Mesma competência utilizada no **TXT**  
**Exclusão** = **1 - Não** ou **2- Sim**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18181122121367)  
  
**4.** **Clique** em **OK** e **OK** Novamente;  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18181171135383)  
  
**5. Clique** em **OK** para visualizar o **Log de Ocorrências**;  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18181226219543)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18181227437463)  
  
  
**6.** Verifique o lançamento da Coparticipação em **Atualizações > Benefícios > Planos de Saúde > Coparticipações** selecione o **Funcionário** e clique em **Visualizar**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18181278420247)  
  
   
**Observação:** Após realizar a importação de variáveis para a tabela RHO - Coparticipação, **realize o calculo** do roteiro PLA antes da integração dos roteiros com a folha de pagamento.   
  
  
**Saiba Mais**  
[RH - Linha Protheus - Importação de variáveis tabela RHO, não soma valores de coparticipação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000621761-RH-Linha-Protheus-Importa%C3%A7%C3%A3o-de-vari%C3%A1veis-tabela-RHO-n%C3%A3o-soma-valores-de-coparticipa%C3%A7%C3%A3o?source=search)  
[RH - Linha Protheus - GPE - Pontos de entrada existentes na rotina GPEA210 - Importação de Variáveis](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402260296983-RH-Linha-Protheus-GPE-Pontos-de-entrada-existentes-na-rotina-GPEA210-Importa%C3%A7%C3%A3o-de-Vari%C3%A1veis?source=search)  
[RH - Linha Protheus - GPE - Importação de variáveis de coparticipação quando houver mais de 1 dependente ou agregado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038792513-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-de-vari%C3%A1veis-de-coparticipa%C3%A7%C3%A3o-quando-houver-mais-de-1-dependente-ou-agregado?source=search)  
[RH - Linha Protheus - GPE - Importação de variáveis Coparticipação, dependentes ficam deletados na RHO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036186414-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-de-vari%C3%A1veis-Coparticipa%C3%A7%C3%A3o-dependentes-ficam-deletados-na-RHO?source=search)
