---
article_id: 360022206592
category: TAF - REINF
content_hash: 3927e1a45d4296572fa5ce813ba1df3ec8fcbe75b14f32ede0c729d4dba00d46
fetched_at: '2026-06-28T22:41:34.931789+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: 'TAF - REINF - Limpar a base do TAF '
type: support-article
updated_at: '2021-04-28T14:30:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022206592-TAF-REINF-Limpar-a-base-do-TAF
---

**Dúvida**

Efetuar a limpeza de toda a base / tabelas do TAF de acordo com período e escopo pré-definido pelo usuário.

Este recurso pode ser utilizado principalmente com o objetivo de migrar o ambiente do sistema de homologação para produção, ou para manter um ambiente limpo em relação aos dados integrados ao sistema.

Importante: Para o escopo de tabelas EFD Reinf, não serão considerados para exclusão os registros que já tenham sido transmitidos ao Governo, ou quando o TAF estiver configurado para transmissão de eventos ao ambiente de **Produção do Governo.**  
  
**Ambiente**TAF – REINF – A partir da versão 12.1.17  
  
**Solução**  
1.Deixar o parâmetro MV\_TAFAMBR = 2.

Abaixo vídeo para auxiliar o usuário alterar o conteúdo do parâmetro.

![apuracao_reinf_parametro.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360019433952/apuracao_reinf_parametro.gif)

2- Acessar a rotina de Monitoramento/Transmissão e retirar o contribuinte da Receita.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019302951/mceclip0.png)

3- Acessar a rotina de exclusão do período fiscal e validar se a data do fonte TAFAEXCPER é igual ou superior a 11/10/2018

Na tela de parâmetros, no teclado pressione as teclas SHIF + F6.

![data_limpeza_de_base.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360019433112/data_limpeza_de_base.gif)

4- Se a rotina estiver atualizada execute o processo de limpeza de base.

![limpeza_de_base.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360019433252/limpeza_de_base.gif)

**Informações importantes para utilizar a rotina :**

1- Realizar um backup do banco de dados;

2- Para a Reinf o sistema não valida as perguntas de data, ele irá apagar todas as apurações realizadas.

3- Se você desejar excluir notas do TAF por período, pode utilizar a pergunta Movimento Fiscal, mas o sistema apaga os cadastros envolvidos no documento, como por exemplo o participante e produto.
