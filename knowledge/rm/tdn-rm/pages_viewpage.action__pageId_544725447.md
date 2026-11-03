---
content_hash: 4f60070eb262b7d86273a081f3b46d6e57253d5ff4db7a3109b5880442c15d75
fetched_at: '2026-06-29T00:10:38.755317+00:00'
page_id: '544725447'
product: rm
source: tdn-rm
title: Resumo de Apuração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=544725447
version: 56
---

* Oracle

**Definição**

Este relatório tem a função de apresentar todas as informações sobre o imposto de ICMS que foi apurado no mês informado, comparando as operações de saídas (débitos) com as operações de entradas (créditos) apresentando o saldo final daquele período (em comparação também com o saldo ANTERIOR, sendo positivo ou negativo).

O Resumo de Apuração foi construído através de um relatório do RM Reports que pode ser anexado ao Período de Apuração. Desta forma, podemos tirar proveito de todos os recursos do Reports, além de poder ser facilmente modificado a critério do usuário.

ATENÇÃO

Estes relatórios não estão disponíveis em todas as versões, consulte a nova solução de relatórios disponível no Smart View

Arquivo para geração do relatório 

Para a geração do relatório, foi disponibilizado no TOTVS Compartilhamento o seguinte objeto gerencial: 

**SQL Server**

* FISREL0006 - Resumo de Apuração do ICMS - SQL.TotvsReport

**Oracle**

* FISREL0007 - Resumo de Apuração do ICMS - ORA.TotvsReport

Para obter o relatório via TOTVS Compartilhamento, consulte este link: [TOTVS Compartilhamento](https://tdn.totvs.com/display/LRM/TOTVS+Compartilhamento).

**Procedimentos**

**Passo 1 - Importar o Relatório**

O layout do Resumo de Apuração (FISREL0006) deve ser importado através do [RM Reports](https://tdn.totvs.com/display/LRM/RM+Reports).

**Passo 2 - Anexar o Relatório ao Período de Apuração**

Apos a importação, acesse o Período de Apuração no item Anexos → Relatórios → Inserir Relatórios para associar o Relatório importado à visão do Período de Apuração.

Selecione o relatório importado e associe os parâmetros do relatório aos campos do Período de Apuração.

**Passo 3 - Gerar o Relatório**

Para gerar o relatório, basta ir novamente no item Anexos → Relatórios do Período de Apuração e clicar no relatório em questão. Lembrando que para a correta geração é necessário que o Período de Apuração do mês selecionado esteja encerrado.

**Gráficos**

Foi desenvolvido também um Gráfico representando visualmente as informações do Resumo de Apuração.

Arquivo para geração do gráfico

**SQL Server**

FISGRA0007 - Resumo de Apuração do ICMS - SQL.TotvsGraf 

**Oracle**

FISGRA0010 - Resumo de Apuração do ICMS - ORA.TotvsGraf

Os arquivos foram disponibilizados no **TOTVS Compartilhamento.**Em caso de duvidas, consulte este link: [TOTVS Compartilhamento](https://tdn.totvs.com/display/LRM/TOTVS+Compartilhamento).

Este Gráfico deve ser importados no cadastro de Gráficos e posteriormente associados na visão de Período de Apuração.

Para efetuar a importação do Gráfico, acesse o cadastro [Gestão → Gráficos e execute o processo de Importação de Gráficos](https://tdn.totvs.com/pages/viewpage.action?pageId=237383345).

Após a importação, acesse os Anexos do Período de Apuração > Selecione a opção Gráficos > Inserir Gráfico para anexar esse gráfico como Anexo do Período de Apuração

Associe os parâmetros da consulta aos campos da visão do Período de Apuração

Após anexar o gráfico o mesmo pode ser exibidos através do menu Anexos → Gráficos.

noneWebinar dos relatórios Registro de Entradas\Saídas e Resumo de Apuração

648432
