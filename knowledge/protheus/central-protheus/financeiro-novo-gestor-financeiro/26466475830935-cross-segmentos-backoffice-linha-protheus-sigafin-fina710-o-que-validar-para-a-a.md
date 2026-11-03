---
article_id: 26466475830935
category: Financeiro - Novo Gestor Financeiro
content_hash: 1b25a97e9465f000e6cb699d6d8f42c3fc58ac45e865ec3f3dfc6d502a3bf5ff
fetched_at: '2026-06-28T22:37:41.494486+00:00'
product: protheus
section_id: 33830415324183
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710 - O que validar
  para a atualização dos saldos no Painel Gestor
type: support-article
updated_at: '2026-06-11T19:46:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26466475830935-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA710-O-que-validar-para-a-atualiza%C3%A7%C3%A3o-dos-saldos-no-Painel-Gestor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28455678449687) Tempo aproximado para leitura: **00:10 min**

**Dúvida**  
O que validar para a atualização dos saldos no Novo Painel Gestor?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.33

**Conceito**

A atualização dos saldos é realizada pelo Job FINA711 executado por grupo de empresas, sendo necessário o agendamento único para o grupo de empresas.

**1º Schedule e Agent Habilitados e ativos**

O Schedule deve ser iniciado, seja o novo (Smart Schedule) ou o antigo (Schedule), conforme ilustrado na imagem abaixo. Caso se trate do antigo, o agente também deve ser iniciado, uma vez que, no novo Smart Schedule, o agente é iniciado automaticamente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26466475811735)

**2º Validar configuração do JOB**

Para LIB anterior a 20260413, Para cada empresa, deve ser configurado um JOB, assim como uma filial, que, por sua vez, irá abranger as demais filiais.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26466475813783)

Na configuração do JOB, temos a opção de atualizar os títulos e pedidos, devem marcar como SIM.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26466508414359)

A partir da LIB 20260413 a configuração dos *jobs***passou a ser única por Grupo de Empresas, não permitida a inclusão das Filiais para processamento.**

**![](https://tdn.totvs.com/download/attachments/667370586/image-2026-6-5_7-16-26.png?version=1&modificationDate=1780654586663&api=v2)**

**Sobre o conteúdo do parâmetro MV\_TFCJOBT**

A partir da liberação das perguntas para o JOB de atualizações de saldos do NGF (FIN711), que possibilita ao cliente escolher se deverá processar os títulos e/ou pedidos, passou-se a armazenar a data de execução desses Jobs de forma isolada.

**Exemplo:**

**TJOBDOC:** armazena a data e hora da última execução da atualização do saldo dos títulos;  
**TJOBORD:** armazena a data e hora da última execução da atualização do saldo dos pedidos;  
Caso o operador opte por executar todos os saldos, ambas as datas serão gravadas para o mesmo dia.

A partir da liberação das perguntas para o JOB de atualizações de saldos do NGF (FIN711), que possibilita ao cliente escolher se deverá processar os títulos e/ou pedidos, passou-se a armazenar a data de execução desses Jobs de forma isolada.

**Exemplo:**

TJOBDOC: armazena a data e hora da última execução da atualização do saldo dos títulos;  
TJOBORD: armazena a data e hora da última execução da atualização do saldo dos pedidos;

Caso o operador opte por executar todos os saldos, ambas as datas serão gravadas para o mesmo dia.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26466475816471)

**Importante**

Caso se trate da cloud da Totvs ou de um ambiente separado para os JOBs, a configuração do JOB da rotina será realizada por meio desse ambiente.

Outro ponto importante, em alguns caso quando é cloud da Totvs, o campo "Comunicação no Cliente" deve ser configurado com "wf"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26466475818519)

Caso a versão utilizada seja a 12.1.2410, é necessário acessar o ambiente Cloud e entrar no Schedule por meio do link disponibilizado pela equipe do Cloud, a fim de realizar a configuração dos jobs no respectivo link do Schedule. Conforme exemplo a seguir:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35543664897175)

O JOB deve ser cadastrado em apenas um ambiente. Se estiver cadastrado em mais de um ambiente para a mesma empresa, isso poderá travar o processo. A validação pode ser feita por meio de um SELECT na tabela XX1.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26466508418711)**

Caso, após todas as validações acima, o erro persista, entre em contato com a equipe de suporte para a coleta dos logs necessários à identificação do problema.

**Saiba mais**

[Novo Gestor Financeiro - FINA710](https://tdn.totvs.com/pages/releaseview.action?pageId=611007335)

[Cross Segmentos - Linha BackOffice Protheus - FINA710 - Saldo do registro/título incorreto - Como atualizar os registros da F76/F75 sem alterar o MV\_TFCJOBT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10994215939735-Cross-Segmentos-Linha-BackOffice-Protheus-FINA710-Saldo-do-registro-t%C3%ADtulo-incorreto-Como-atualizar-os-registros-da-F76-F75-sem-alterar-o-MV-TFCJOBT)
