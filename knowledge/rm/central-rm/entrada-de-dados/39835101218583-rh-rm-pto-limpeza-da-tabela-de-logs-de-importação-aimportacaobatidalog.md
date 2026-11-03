---
article_id: 39835101218583
category: Entrada de dados
content_hash: dfe625298823d8523fb6c21fd7e628ead02c03894d87f427e3db5cfea66761e6
fetched_at: '2026-06-28T22:46:30.528185+00:00'
product: rm
section_id: 1500000835061
source: central-rm
title: RH - RM - PTO - Limpeza da tabela de logs de importação (AIMPORTACAOBATIDALOG)
type: support-article
updated_at: '2026-04-20T13:01:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39835101218583-RH-RM-PTO-Limpeza-da-tabela-de-logs-de-importa%C3%A7%C3%A3o-AIMPORTACAOBATIDALOG
---

![relogio_tempo_leitura_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39835101206039) **Tempo aproximado para leitura: 00:02:00 min**  
  
**Dúvida**  
Como realizar a limpeza da tabela AIMPORTACAOBATIDALOG no módulo RM Automação de Ponto e como desativar a geração desses logs para evitar o crescimento excessivo do banco de dados.

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 12

**Solução**  
Os registros da tabela AIMPORTACAOBATIDALOG são gerados para permitir a conferência de importações de batidas realizadas no sistema. A exclusão de registros antigos não causa impacto ou prejuízo ao funcionamento do módulo, sendo recomendado manter apenas os dados dos últimos dois períodos para eventuais consultas. Caso deseje que o sistema interrompa a gravação desses dados, é possível desativar a função através do parametrizador do módulo.

**Passos**  
Para realizar a limpeza manual dos logs:

1. Acesse o módulo **Automação de Ponto**.
2. Vá ao menu **Entrada de Dados** e selecione a opção **Logs da importação**.
3. Selecione os registros que deseja remover.
4. Clique no ícone de **Excluir** (ícone de X na barra de ferramentas).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39873689977111)

Para desativar a geração de novos logs na tabela:

1. Acesse as configurações do sistema e abra o **Parametrizador**.
2. Avance até a etapa **Importação**.
3. Desmarque a opção **Utiliza logs de erros e alertas na importação de batidas**.
4. Avance e salve as alterações para concluir o processo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39873442149143)

**Saiba Mais**  
[Logs de importação](https://tdn.totvs.com/pages/releaseview.action?pageId=452719988)

[RH - RM - PTO - Como importar as batidas para o Automação de Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044528493)
