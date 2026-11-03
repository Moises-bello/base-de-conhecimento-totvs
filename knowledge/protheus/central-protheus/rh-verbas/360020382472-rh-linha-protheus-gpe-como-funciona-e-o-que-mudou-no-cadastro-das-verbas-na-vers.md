---
article_id: 360020382472
category: 'RH - Verbas '
content_hash: 8eefb8ed8d3a42aacb19f1ef5db46e115db8698b9fb433ff425829487df790be
fetched_at: '2026-06-28T22:43:20.097829+00:00'
product: protheus
section_id: 360010838314
source: central-protheus
title: RH - Linha Protheus - GPE - Como funciona e o que mudou no cadastro das verbas
  na versão 12
type: support-article
updated_at: '2025-02-18T13:33:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020382472-RH-Linha-Protheus-GPE-Como-funciona-e-o-que-mudou-no-cadastro-das-verbas-na-vers%C3%A3o-12
---

**Dúvida**Como funciona e o que mudou no cadastro das verbas na versão 12  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

1.Diferente da versão 11, na versão 12 o cadastro de verbas é acesso em Atualizações > Definições de Cálculo > Verbas;

 Novos campos na aba Geral:![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016612091/mceclip3.png)

Impr. Verba = Define se a verba de base será impressa nos relatórios. É habilitado somente para as verbas de base;  
Valor de = valor mínimo que poderá ser lançado para a verba;  
Valor até = valor máximo que poderá ser lançado para a verba;  
Ref. de = quantidade mínima de horas dias que pode ser lançada;  
Ref. até = quantidade máxima de horas dias que pode ser lançada;  
Fechamento Competência = Define se o fechamento do período do sistema deverá realizar o fechamento da verba por período ou competência;  
Verba Mês Seguinte = Código da Verba para o próximo período, por exemplo, verbas utilizadas no cálculo férias partidas;  
Código Base Correspondente = Informar a verba de base que será gerada sempre que houver a ocorrência da verba principal e incorporará salário e também se o funcionário estiver de férias no mês todo;  
Empréstimo Consignado = define de a verba é referente a empréstimo consignado;  
Tipo do Código = Base (Provento)= quando a base for referente a um pagamento de verba de  provento. Ex.: id 0318 Base Salário do Mês;  
Base (Desconto)= quando a base for referente a um pagamento de verba de desconto;  
Lançamento Diário = S = se o campo Quantidade de Lançamento estiver com 5, por exemplo, e o campo Lançamento Diário estiver com Sim será possível lançar 5 vezes a verba por dia. Caso contrário, poderá ser lançada a verba 5 vezes no mês.

2. Novos campos na aba Incidências:![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016559592/mceclip4.png)

INSS Férias= Informar se esta verba servirá como base para o cálculo de INSS Férias;  
Base Cálculo= Informar se esta verba é calculada a partir da base de salário do cadastro ou do salário incorporado.  
  
3. Novos campos na aba Outras Informações:![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016612191/mceclip5.png)

Expr. Filtro = possibilita o vinculo ou acumulo de outras verbas à verba primária que possuem cadastro ou alteração. Devem ser informadas verbas que comporão a base de cálculo. Essa verba será utilizada na rotina de Valores Fixos para o Tipo Acumulador.

V. Dif. Fer = Informar o código da verba onde devem ser gravadas as diferenças de férias calculadas na folha de pagamento. Deve ser informado para todas as verbas de férias que as diferenças devam ser apuradas.

4. Nova aba e-Social:![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016559712/mceclip6.png)

5. Nova aba Bloqueios Lançamentos:![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016612431/mceclip7.png)

Os campos na aba Bloqueio de Lançamento definem em quais rotinas será bloqueado o lançamento da verba.
